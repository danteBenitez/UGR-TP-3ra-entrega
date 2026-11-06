# Modelo de Planificación por Temporada: Desempeño por Perfil

Métricas sobre el perfil de cada estación y tipo de día en 2019, el nivel relevante para la diagramación: distancia de variación total entre el perfil proyectado y el observado (mediana entre estaciones y tipos de día), error absoluto medio del ratio de retención por estación, error relativo medio del volumen diario medio por estación y tipo de día, y error relativo mediano del volumen de cada día-estación.

| Modelo | TV de forma (mediana) | Error retención Sábado (pp) | Error retención Domingo-Feriado (pp) | Error de volumen medio (%) | Error diario mediano (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Perfil histórico | 0.030 | 3.80 | 1.14 | 10.11 | 12.57 |
| V1 × forma | 0.018 | 1.23 | 0.69 | 3.80 | 8.43 |
| XGBoost directo | 0.043 | 3.07 | 4.57 | 19.48 | 9.77 |
| V2 × forma | 0.018 | 0.80 | 0.75 | 6.81 | 7.67 |
