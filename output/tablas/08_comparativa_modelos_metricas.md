# Evaluación y Comparación de Modelos Supervisados (Fases 6 y 7)

### 1. Desempeño Global en Validación (2018) y Prueba (2019) — One-Step Forecasting (15 min)

> [!IMPORTANT]
> **Resultado Principal:** El modelo de ensamble **Gradient Boosting (XGBoost)** supera de forma contundente al modelo base de **Regresión Lineal** en el conjunto de prueba independiente (2019), reduciendo el **RMSE en un 23.09%** (56.01 vs 72.82 pax/15min) y el **MAE en un 31.98%** (22.31 vs 32.80 pax/15min), alcanzando un coeficiente de determinación **$R^2 = 0.9502$**.

| Conjunto Temporal | Modelo Supervisado | MSE ($\text{pax}^2$) | RMSE ($\text{pax/15m}$) | MAE ($\text{pax/15m}$) | $R^2$ |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Validación (2018)** | Regresión Lineal (Baseline) | 6,237.92 | 78.98 | 34.71 | 0.9137 |
| **Validación (2018)** | **Gradient Boosting (XGBoost)** | **4,195.08** | **64.77** | **24.02** | **0.9420** |
| **Prueba / Test (2019)** | Regresión Lineal (Baseline) | 5,303.09 | 72.82 | 32.80 | 0.9157 |
| **Prueba / Test (2019)** | **Gradient Boosting (XGBoost)** | **3,136.87** | **56.01** | **22.31** | **0.9502** |

### 2. Desempeño en Prueba (2019) Desagregado por Régimen de Día (Hábil vs. No Laborable)

| Tipo de Día | Modelo | MSE | RMSE (pax/15m) | MAE (pax/15m) | $R^2$ |
| :--- | :--- | :---: | :---: | :---: | :---: |
| Hábil | Regresión Lineal | 6,359.94 | 79.75 | 36.40 | 0.9143 |
| Hábil | **Gradient Boosting (XGBoost)** | 3,743.05 | **61.18** | **24.63** | 0.9496 |
| No Laborable | Regresión Lineal | 3,107.65 | 55.75 | 25.33 | 0.9092 |
| No Laborable | **Gradient Boosting (XGBoost)** | 1,877.63 | **43.33** | **17.49** | 0.9451 |

### 3. Desempeño en Prueba (2019) Desagregado por Línea

| Línea | Modelo | MSE | RMSE (pax/15m) | MAE (pax/15m) | $R^2$ |
| :--- | :--- | :---: | :---: | :---: | :---: |
| Línea A | Regresión Lineal | 1,895.36 | 43.54 | 24.28 | 0.9190 |
| Línea A | **Gradient Boosting (XGBoost)** | 770.47 | **27.76** | **15.84** | 0.9671 |
| Línea B | Regresión Lineal | 4,349.23 | 65.95 | 35.14 | 0.8960 |
| Línea B | **Gradient Boosting (XGBoost)** | 2,071.31 | **45.51** | **23.06** | 0.9505 |
| Línea C | Regresión Lineal | 13,897.59 | 117.89 | 45.37 | 0.9213 |
| Línea C | **Gradient Boosting (XGBoost)** | 9,866.79 | **99.33** | **33.79** | 0.9441 |

### 4. Evaluación por Horizonte de Predicción (One-Step vs. Multi-Step en Test 2019)

| Horizonte de Pronóstico | Modelo | MSE | RMSE (pax/15m) | MAE (pax/15m) | $R^2$ |
| :--- | :--- | :---: | :---: | :---: | :---: |
| H=1 (+15 min, One-Step) | Regresión Lineal | 5,303.09 | 72.82 | 32.80 | 0.9157 |
| H=1 (+15 min, One-Step) | **Gradient Boosting (XGBoost)** | 3,136.87 | **56.01** | **22.31** | 0.9502 |
| H=2 (+30 min, Multi-Step) | Regresión Lineal | 7,156.86 | 84.60 | 39.31 | 0.8863 |
| H=2 (+30 min, Multi-Step) | **Gradient Boosting (XGBoost)** | 3,542.33 | **59.52** | **24.37** | 0.9437 |
| H=4 (+60 min, Multi-Step) | Regresión Lineal | 12,512.85 | 111.86 | 52.86 | 0.8012 |
| H=4 (+60 min, Multi-Step) | **Gradient Boosting (XGBoost)** | 4,652.91 | **68.21** | **27.94** | 0.9261 |

### 5. Top 10 Características Más Relevantes en Gradient Boosting (XGBoost)

| Ranking | Característica | Importancia Relativa (%) |
| :---: | :--- | :---: |
| 1 | `media_movil_1h` | 46.85% |
| 2 | `lag_1` | 32.59% |
| 3 | `lag_2` | 5.75% |
| 4 | `lag_7d` | 3.22% |
| 5 | `hora_decimal` | 1.79% |
| 6 | `ventana_idx` | 1.73% |
| 7 | `longitud` | 1.30% |
| 8 | `distancia_centro_km` | 1.21% |
| 9 | `lag_1d` | 0.96% |
| 10 | `lag_4` | 0.64% |
