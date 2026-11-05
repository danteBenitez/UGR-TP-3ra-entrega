"""Experimento exploratorio DM-06 (2): separación volumen × forma.
Mismo esquema que exp_seasonal_model.py: origen móvil por trimestre de 2019,
features 'as-of' el inicio de cada trimestre."""
import sys, time
import numpy as np, pandas as pd, holidays, xgboost as xgb

PARQUET, PREV_PREDS = sys.argv[1], sys.argv[2]
t0 = time.time()
log = lambda *a: print(f"[{time.time()-t0:6.0f}s]", *a, flush=True)

# ---------------------------------------------------------------- grilla (idéntica al experimento anterior)
d = pd.read_parquet(PARQUET, columns=['estacion', 'fecha', 'ventana_15min', 'ingresos'])
d = d[d.ventana_15min >= '05:00']
d = d[d.groupby(['estacion', 'fecha']).ingresos.transform('sum') >= 20]
act = d[['estacion', 'fecha']].drop_duplicates()
wins = sorted(d.ventana_15min.unique())
win = pd.DataFrame({'ventana_15min': wins, 'win': np.arange(len(wins), dtype=np.int16)})
g = act.merge(win, how='cross').merge(d, how='left', on=['estacion', 'fecha', 'ventana_15min'])
g['ingresos'] = g.ingresos.fillna(0).astype(np.float32)
g = g.drop(columns='ventana_15min')
del d
g['est'] = g.estacion.astype('category').cat.codes.astype(np.int16)

h = holidays.Argentina(years=range(2013, 2021))
cal = pd.DataFrame({'fecha': pd.date_range('2014-01-01', '2019-12-31')})
name = cal.fecha.dt.date.map(h.get)
dow = cal.fecha.dt.day_of_week
cal['dow'] = dow.astype(np.int8)
cal['tipo'] = np.select([name == 'Jueves Santo', name.notna(), dow == 6, dow == 5], [1, 2, 2, 1], default=0).astype(np.int8)
cal['es_feriado'] = (name.notna() & (name != 'Jueves Santo')).astype(np.int8)
cal['es_puente'] = name.fillna('').str.contains('turístic').astype(np.int8)
hol = set(pd.to_datetime([k for k, v in h.items() if v != 'Jueves Santo']))
cal['pre_feriado'] = (cal.fecha + pd.Timedelta(days=1)).isin(hol).astype(np.int8)
cal['post_feriado'] = (cal.fecha - pd.Timedelta(days=1)).isin(hol).astype(np.int8)
cal['mes'] = cal.fecha.dt.month.astype(np.int8)
cal['dia_mes'] = cal.fecha.dt.day.astype(np.int8)
cal['q'] = cal.fecha.dt.quarter.astype(np.int8)
cal['qidx'] = ((cal.fecha.dt.year - 2014) * 4 + cal.q - 1).astype(np.int8)
g = g.merge(cal[['fecha', 'tipo', 'q', 'qidx']], on='fecha', how='left')

# ---------------------------------------------------------------- nivel diario y proporciones intradiarias
daily = g.groupby(['estacion', 'est', 'fecha'], as_index=False).ingresos.sum().rename(columns={'ingresos': 'vol'})
daily = daily.merge(cal, on='fecha', how='left')
g = g.merge(daily[['est', 'fecha', 'vol']], on=['est', 'fecha'])
g['share'] = (g.ingresos / g.vol).astype(np.float32)
lag = daily[['est', 'fecha', 'vol']].copy(); lag['fecha'] += pd.Timedelta(days=364)
daily = daily.merge(lag.rename(columns={'vol': 'vol_lag364'}), on=['est', 'fecha'], how='left')
log("grilla:", len(g), "| días-estación:", len(daily))

# ---------------------------------------------------------------- features 'as-of' por trimestre
starts = {qi: pd.Timestamp(2014 + qi // 4, 3 * (qi % 4) + 1, 1) for qi in range(24)}
vparts, sparts = [], []
for qi in range(4, 24):
    S = starts[qi]; qq = qi % 4 + 1
    dh = daily[daily.fecha < S]
    by = ['est', 'tipo']
    m = lambda x: x.groupby(by).vol.mean()
    vol_hist = m(dh)
    vol_rec = m(dh[dh.fecha >= S - pd.DateOffset(months=3)])
    # factor estacional del año previo: trimestre q del año anterior / 3 meses previos a ese trimestre
    S1 = S - pd.DateOffset(years=1)
    trim_prev = m(dh[(dh.fecha >= S1) & (dh.fecha < S1 + pd.DateOffset(months=3))])
    pre_prev = m(dh[(dh.fecha >= S1 - pd.DateOffset(months=3)) & (dh.fecha < S1)])
    f = pd.DataFrame({'vol_hist': vol_hist, 'vol_rec': vol_rec, 'trim_prev': trim_prev, 'pre_prev': pre_prev})
    f['vol_rec'] = f.vol_rec.fillna(f.vol_hist)
    f['s_factor'] = (f.trim_prev / f.pre_prev).replace([np.inf, -np.inf], np.nan).fillna(1.0)
    f['qidx'] = qi
    vparts.append(f.reset_index())
    # forma: promedio de proporciones diarias (cada día pesa lo mismo, DM-04)
    gh = g[g.fecha < S]
    s = gh.groupby(['est', 'tipo', 'win']).share.mean().rename('shape_hist').to_frame()
    s = s.join(gh[gh.fecha >= S - pd.DateOffset(months=12)].groupby(['est', 'tipo', 'win']).share.mean().rename('shape_12m'))
    s['qidx'] = qi
    sparts.append(s.reset_index())
vf = pd.concat(vparts, ignore_index=True)
sf = pd.concat(sparts, ignore_index=True)
daily = daily[daily.qidx >= 4].merge(vf, on=['est', 'tipo', 'qidx'], how='left')
for c in ['vol_hist', 'trim_prev', 'vol_lag364']:
    daily[f'r_{c}'] = daily[c] / daily.vol_rec
daily['y_ratio'] = daily.vol / daily.vol_rec
log("features as-of listas")

# ---------------------------------------------------------------- modelos de volumen diario
VFEATS = ['est', 'tipo', 'dow', 'es_feriado', 'es_puente', 'pre_feriado', 'post_feriado', 'mes', 'dia_mes',
          's_factor', 'r_vol_hist', 'r_trim_prev', 'r_vol_lag364']
daily['V0'] = daily.vol_hist
daily['V1'] = daily.vol_rec * daily.s_factor
daily['V2'] = np.nan
for o in (20, 21, 22, 23):
    tr = daily[(daily.qidx >= 4) & (daily.qidx <= o - 2)]
    va = daily[daily.qidx == o - 1]
    te = daily.qidx == o
    params = dict(objective='reg:squarederror', tree_method='hist', max_depth=6, eta=0.05,
                  subsample=0.8, colsample_bytree=0.8, min_child_weight=20, nthread=12)
    mdl = xgb.train(params, xgb.DMatrix(tr[VFEATS], label=tr.y_ratio), 2000,
                    evals=[(xgb.DMatrix(va[VFEATS], label=va.y_ratio), 'val')],
                    early_stopping_rounds=100, verbose_eval=False)
    r = mdl.predict(xgb.DMatrix(daily.loc[te, VFEATS]), iteration_range=(0, mdl.best_iteration + 1))
    daily.loc[te, 'V2'] = np.clip(r, 0, None) * daily.loc[te, 'vol_rec']
    log(f"volumen 2019T{o-19}: mejor iteración {mdl.best_iteration}")

# ---------------------------------------------------------------- recomposición volumen × forma
T = g[g.qidx >= 20].merge(sf, on=['est', 'tipo', 'win', 'qidx'], how='left') \
     .merge(daily[['est', 'fecha', 'V0', 'V1', 'V2']], on=['est', 'fecha'], how='left')
for v in ('V0', 'V1', 'V2'):
    T[f'{v}xS'] = T[v] * T.shape_hist
T['V2xS12'] = T.V2 * T.shape_12m
T['V1xS12'] = T.V1 * T.shape_12m
prev = pd.read_parquet(PREV_PREDS)[['est', 'fecha', 'win', 'pred_base', 'pred_xgb']]
T = T.merge(prev, on=['est', 'fecha', 'win'], how='left')
assert T.pred_base.notna().all(), "filas no alineadas con el experimento anterior"

MODELS = [('pred_base', 'Perfil histórico'), ('pred_xgb', 'XGBoost directo (exp. 1)'),
          ('V0xS', 'V0 hist × forma'), ('V1xS', 'V1 estacional ingenuo × forma'),
          ('V2xS', 'V2 XGBoost volumen × forma'), ('V2xS12', 'V2 × forma últimos 12 meses'), ('V1xS12', 'V1 × forma últimos 12 meses')]
tn = {0: 'Hábil', 1: 'Sábado', 2: 'Dom-Fer'}

print("\n=== Por ventana de 15 min (2019, origen móvil por trimestre) ===")
rows = []
for seg, df in [('Total', T)] + [(tn[t], T[T.tipo == t]) for t in (0, 1, 2)]:
    for c, lab in MODELS:
        e = df.ingresos - df[c]
        rows.append(dict(segmento=seg, modelo=lab, RMSE=np.sqrt((e ** 2).mean()), MAE=e.abs().mean(),
                         R2=1 - (e ** 2).sum() / ((df.ingresos - df.ingresos.mean()) ** 2).sum(),
                         sesgo_pct=(df[c].sum() / df.ingresos.sum() - 1) * 100))
print(pd.DataFrame(rows).round(2).to_string(index=False))

print("\n=== Volumen diario por estación-día (2019) ===")
D = T.groupby(['est', 'tipo', 'fecha', 'qidx'])[['ingresos'] + [c for c, _ in MODELS]].sum().reset_index()
rows = []
for c, lab in MODELS:
    ape = np.abs(D[c] / D.ingresos - 1) * 100
    rows.append(dict(modelo=lab, MAPE_dia=ape.mean(), MdAPE_dia=ape.median(),
                     **{f'sesgo_{tn[t]}': (D[D.tipo == t][c].sum() / D[D.tipo == t].ingresos.sum() - 1) * 100 for t in (0, 1, 2)}))
print(pd.DataFrame(rows).round(2).to_string(index=False))

print("\nSesgo de volumen por trimestre (%), total red:")
b = D.groupby('qidx')[['ingresos'] + [c for c, _ in MODELS]].sum()
print(((b[[c for c, _ in MODELS]].div(b.ingresos, axis=0) - 1) * 100).rename(index=lambda i: f"2019T{i-19}")
      .rename(columns=dict(MODELS)).round(1).to_string())

print("\n=== Por perfil (estación × tipo de día, promedio 2019) ===")
P = T.groupby(['est', 'tipo', 'win'])[['ingresos'] + [c for c, _ in MODELS]].mean().reset_index()
V = D.groupby(['est', 'tipo'])[['ingresos'] + [c for c, _ in MODELS]].mean().unstack()
for c, lab in MODELS:
    tv = P.groupby(['est', 'tipo']).apply(lambda x: 0.5 * np.abs(x.ingresos / x.ingresos.sum() - x[c] / x[c].sum()).sum())
    out = f"{lab:30s} TV med {tv.median():.3f}"
    for t in (1, 2):
        ro = V['ingresos'][t] / V['ingresos'][0] * 100; rp = V[c][t] / V[c][0] * 100
        out += f" | ret. {tn[t]} err {np.abs(ro - rp).mean():.2f} pp"
    out += f" | vol. medio est×tipo err {np.abs(V[c].stack() / V['ingresos'].stack() - 1).mean() * 100:.1f}%"
    print(out)
log("fin")
