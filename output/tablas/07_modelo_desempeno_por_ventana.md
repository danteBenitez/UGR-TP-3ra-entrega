# Modelo de Planificación por Temporada: Desempeño por Ventana

Proyección de cada trimestre de 2019 con datos anteriores a su inicio (origen móvil). Hiperparámetros elegidos con los trimestres de 2018: XGBoost directo profundidad 8, años de entrenamiento: recientes; V2 × forma profundidad 8, años de entrenamiento: todos.

| Segmento | Modelo | RMSE (pax/15 min) | MAE (pax/15 min) | R² | Sesgo de volumen (%) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| Total | Perfil histórico | 64.65 | 25.64 | 0.923 | -5.18 |
| Total | V1 × forma | 61.65 | 22.61 | 0.930 | +2.36 |
| Total | XGBoost directo | 59.25 | 23.93 | 0.936 | +6.27 |
| Total | V2 × forma | 59.11 | 21.77 | 0.936 | +5.68 |
| Hábil | Perfil histórico | 74.57 | 31.04 | 0.923 | -4.04 |
| Hábil | V1 × forma | 71.95 | 27.35 | 0.928 | +2.51 |
| Hábil | XGBoost directo | 68.91 | 27.98 | 0.934 | +5.24 |
| Hábil | V2 × forma | 68.68 | 26.19 | 0.935 | +5.64 |
| Sábado | Perfil histórico | 42.24 | 18.38 | 0.868 | -14.48 |
| Sábado | V1 × forma | 32.90 | 14.38 | 0.920 | -0.35 |
| Sábado | XGBoost directo | 34.00 | 17.09 | 0.914 | +7.89 |
| Sábado | V2 × forma | 32.33 | 14.24 | 0.922 | +4.46 |
| Domingo-Feriado | Perfil histórico | 31.31 | 11.61 | 0.784 | -10.64 |
| Domingo-Feriado | V1 × forma | 29.26 | 11.61 | 0.811 | +3.84 |
| Domingo-Feriado | XGBoost directo | 28.12 | 14.40 | 0.826 | +21.17 |
| Domingo-Feriado | V2 × forma | 30.08 | 11.43 | 0.801 | +8.00 |
