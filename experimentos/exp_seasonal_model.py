"""Experimento exploratorio DM-06: modelo de planificación con horizonte de una temporada.
Evaluación con origen móvil por trimestre de 2019; features calculadas 'as-of' el inicio
de cada trimestre (sin fuga). Compara XGBoost contra la línea base de perfil histórico."""
import sys, time
import numpy as np, pandas as pd, holidays, xgboost as xgb

PARQUET = sys.argv[1]
t0 = time.time()
log = lambda *a: print(f"[{time.time()-t0:6.0f}s]", *a, flush=True)

d = pd.read_parquet(PARQUET, columns=['estacion', 'fecha', 'ventana_15min', 'ingresos'])
d = d[d.ventana_15min >= '05:00']
day = d.groupby(['estacion', 'fecha']).ingresos.transform('sum')
d = d[day >= 20]
act = d[['estacion', 'fecha']].drop_duplicates()
wins = sorted(d.ventana_15min.unique())
win = pd.DataFrame({'ventana_15min': wins, 'win': np.arange(len(wins), dtype=np.int16)})
g = act.merge(win, how='cross').merge(d, how='left', on=['estacion', 'fecha', 'ventana_15min'])
g['ingresos'] = g.ingresos.fillna(0).astype(np.float32)
g = g.drop(columns='ventana_15min')
del d, act
g['est'] = g.estacion.astype('category').cat.codes.astype(np.int16)

h = holidays.Argentina(years=range(2013, 2021))
cal = pd.DataFrame({'fecha': pd.date_range('2014-01-01', '2019-12-31')})
name = cal.fecha.dt.date.map(h.get)
dow = cal.fecha.dt.day_of_week
cal['dow'] = dow.astype(np.int8)
cal['tipo'] = np.select(
    [name == 'Jueves Santo', name.notna(), dow == 6, dow == 5],
    [1, 2, 2, 1], default=0).astype(np.int8)
cal['es_feriado'] = (name.notna() & (name != 'Jueves Santo')).astype(np.int8)
cal['es_puente'] = name.fillna('').str.contains('turístic').astype(np.int8)
hol = set(pd.to_datetime([k for k, v in h.items() if v != 'Jueves Santo']))
cal['pre_feriado'] = (cal.fecha + pd.Timedelta(days=1)).isin(hol).astype(np.int8)
cal['post_feriado'] = (cal.fecha - pd.Timedelta(days=1)).isin(hol).astype(np.int8)
cal['mes'] = cal.fecha.dt.month.astype(np.int8)
cal['dia_mes'] = cal.fecha.dt.day.astype(np.int8)
cal['q'] = cal.fecha.dt.quarter.astype(np.int8)
cal['qidx'] = ((cal.fecha.dt.year - 2014) * 4 + cal.q - 1).astype(np.int8)
g = g.merge(cal, on='fecha', how='left')
log("grilla:", len(g), "filas")

key = g[['est', 'fecha', 'win', 'ingresos']]
for lag in (364, 728):
    k = key.copy(); k['fecha'] = k.fecha + pd.Timedelta(days=lag)
    g = g.merge(k.rename(columns={'ingresos': f'lag_{lag}'}), on=['est', 'fecha', 'win'], how='left')
del key

starts = {qi: pd.Timestamp(2014 + qi // 4, 3 * (qi % 4) + 1, 1) for qi in range(24)}
daily = g.groupby(['est', 'tipo', 'fecha', 'q'], as_index=False).ingresos.sum()
feat_parts = []
for qi in range(4, 24):
    S = starts[qi]; qq = qi % 4 + 1
    hist = g[g.fecha < S]
    rec = hist[hist.fecha >= S - pd.DateOffset(months=3)]
    K = ['est', 'tipo', 'win']
    f = hist.groupby(K).ingresos.mean().rename('perfil_hist').to_frame()
    f = f.join(hist[hist.q == qq].groupby(K).ingresos.mean().rename('perfil_mismo_trim'))
    f = f.join(rec.groupby(K).ingresos.mean().rename('perfil_reciente'))
    dh = daily[daily.fecha < S]
    lv = (dh[dh.fecha >= S - pd.DateOffset(months=3)].groupby(['est', 'tipo']).ingresos.mean()
          / dh.groupby(['est', 'tipo']).ingresos.mean()).rename('nivel_reciente')
    vol = dh.groupby(['est', 'tipo']).ingresos.mean().rename('vol_diario_hist')
    f = f.reset_index().join(lv, on=['est', 'tipo']).join(vol, on=['est', 'tipo'])
    f['qidx'] = qi
    feat_parts.append(f)
feats = pd.concat(feat_parts, ignore_index=True)
g = g[g.qidx >= 4].merge(feats, on=['est', 'tipo', 'win', 'qidx'], how='left')
del feats, feat_parts, daily
for c in g.select_dtypes('float64').columns:
    g[c] = g[c].astype(np.float32)
log("features as-of listas:", len(g), "filas")

FEATS = ['est', 'win', 'dow', 'tipo', 'es_feriado', 'es_puente', 'pre_feriado', 'post_feriado',
         'mes', 'dia_mes', 'lag_364', 'lag_728', 'perfil_hist', 'perfil_mismo_trim',
         'perfil_reciente', 'nivel_reciente', 'vol_diario_hist']

preds = []
for o in (20, 21, 22, 23):
    tr = g[(g.qidx >= 4) & (g.qidx <= o - 2)]
    va = g[g.qidx == o - 1]
    te = g[g.qidx == o].copy()
    dtr = xgb.DMatrix(tr[FEATS], label=tr.ingresos, nthread=12)
    dva = xgb.DMatrix(va[FEATS], label=va.ingresos, nthread=12)
    params = dict(objective='reg:squarederror', tree_method='hist', max_depth=8, eta=0.08,
                  subsample=0.8, colsample_bytree=0.8, min_child_weight=50, nthread=12, max_bin=256)
    m = xgb.train(params, dtr, num_boost_round=1500, evals=[(dva, 'val')],
                  early_stopping_rounds=50, verbose_eval=False)
    te['pred_xgb'] = np.clip(m.predict(xgb.DMatrix(te[FEATS], nthread=12),
                                       iteration_range=(0, m.best_iteration + 1)), 0, None)
    te['pred_base'] = te.perfil_hist
    preds.append(te[['estacion', 'est', 'tipo', 'fecha', 'win', 'qidx', 'ingresos', 'pred_xgb', 'pred_base']])
    log(f"origen 2019T{o-19}: train {len(tr):,} | mejor iteración {m.best_iteration}")
    del dtr, dva, tr, va

pd.concat(preds, ignore_index=True).to_parquet(sys.argv[2], index=False)
log("predicciones guardadas")
