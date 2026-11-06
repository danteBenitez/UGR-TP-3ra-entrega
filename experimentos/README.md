# Experimentos exploratorios (DM-06)

Scripts que generaron la evidencia exploratoria de **DM-06** en `DECISIONES_METODOLOGICAS.md`: modelo de planificación con horizonte de una temporada, evaluado con origen móvil por trimestre de 2019. **El modelo definitivo está implementado en `notebook_eda_subte.ipynb` (sección 7)**, con criterios que difieren de estos scripts (96 ventanas, días sin servicio con ingreso nulo, exclusión de cierres parciales, ajuste de hiperparámetros); estos scripts se conservan como registro de la exploración.

Desde la raíz del repositorio (XGBoost es dependencia del proyecto, `xgboost-cpu`):

```bash
# 1. XGBoost directo sobre ingresos por ventana + línea base de perfil histórico.
#    Guarda las predicciones de 2019 (las usa el experimento 2 para comparar sobre las mismas filas).
uv run python experimentos/exp_seasonal_model.py \
    data_processed/subte_consolidado_15min.parquet /tmp/exp_preds_2019.parquet

# 2. Separación volumen × forma (V0, V1, V2 × forma histórica y de los últimos 12 meses).
uv run python experimentos/exp_volume_shape.py \
    data_processed/subte_consolidado_15min.parquet /tmp/exp_preds_2019.parquet
```

Cada script tarda unos 2 minutos (12 núcleos, ~6 GB de RAM).
