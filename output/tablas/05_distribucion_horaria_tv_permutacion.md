# Distribución Horaria de la Demanda: Distancia de Variación Total y Test de Permutación

### Diseño
- **Perfil normalizado:** proporción de los ingresos del día en cada ventana de 15 minutos; perfil medio por estación y tipo de día, con igual peso por día.
- **Tamaño de efecto:** distancia de variación total, $TV = \tfrac{1}{2}\sum_i |p_i - q_i|$: proporción de la demanda diaria no compartida entre ambos perfiles.
- **Inferencia:** test de permutación de días completos (10,000 permutaciones), estratificado por año-mes (año-trimestre en Domingo – Feriado), con corrección de Holm entre las 44 estaciones para cada comparación. El menor p-valor ajustado alcanzable es 0.0044.
- **Hábil – Sábado** y **Hábil – Domingo-Feriado** contrastan la hipótesis; **Sábado – Domingo-Feriado** y **Domingo – Feriado** validan las categorías de tipo de día.

### Resumen por Línea

Mediana de $TV$ entre las estaciones de la línea [mínimo – máximo] y mayor p-valor ajustado por Holm.

| Comparación | Línea | Estaciones | TV mediana [mín – máx] | p ajustado (Holm) máximo |
| :--- | :--- | :---: | :---: | :---: |
| Hábil – Sábado | Línea A | 18 | 0.172 [0.085 – 0.313] | 0.0044 |
| Hábil – Sábado | Línea B | 17 | 0.177 [0.092 – 0.261] | 0.0044 |
| Hábil – Sábado | Línea C | 9 | 0.167 [0.100 – 0.225] | 0.0044 |
| Hábil – Sábado | **Red (A, B, C)** | 44 | 0.169 [0.085 – 0.313] | 0.0044 |
| Hábil – Domingo-Feriado | Línea A | 18 | 0.181 [0.075 – 0.402] | 0.0044 |
| Hábil – Domingo-Feriado | Línea B | 17 | 0.205 [0.081 – 0.413] | 0.0044 |
| Hábil – Domingo-Feriado | Línea C | 9 | 0.180 [0.144 – 0.403] | 0.0044 |
| Hábil – Domingo-Feriado | **Red (A, B, C)** | 44 | 0.186 [0.075 – 0.413] | 0.0044 |
| Sábado – Domingo-Feriado | Línea A | 18 | 0.136 [0.119 – 0.246] | 0.0044 |
| Sábado – Domingo-Feriado | Línea B | 17 | 0.207 [0.164 – 0.302] | 0.0044 |
| Sábado – Domingo-Feriado | Línea C | 9 | 0.131 [0.090 – 0.243] | 0.0044 |
| Sábado – Domingo-Feriado | **Red (A, B, C)** | 44 | 0.165 [0.090 – 0.302] | 0.0044 |
| Domingo – Feriado | Línea A | 18 | 0.030 [0.022 – 0.067] | 0.0308 |
| Domingo – Feriado | Línea B | 17 | 0.058 [0.046 – 0.085] | 0.4714 |
| Domingo – Feriado | Línea C | 9 | 0.050 [0.030 – 0.067] | 0.1268 |
| Domingo – Feriado | **Red (A, B, C)** | 44 | 0.049 [0.022 – 0.085] | 0.4714 |

### Resultados por Estación

| Línea | Estación | TV Hábil – Sábado (p Holm) | TV Hábil – Domingo-Feriado (p Holm) | TV Sábado – Domingo-Feriado (p Holm) | TV Domingo – Feriado (p Holm) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| Línea A | Acoyte | 0.198 (0.0044) | 0.300 (0.0044) | 0.131 (0.0044) | 0.035 (0.0044) |
| Línea A | Alberti | 0.157 (0.0044) | 0.075 (0.0044) | 0.181 (0.0044) | 0.027 (0.0060) |
| Línea A | Carabobo | 0.250 (0.0044) | 0.355 (0.0044) | 0.127 (0.0044) | 0.031 (0.0044) |
| Línea A | Castro Barros | 0.115 (0.0044) | 0.193 (0.0044) | 0.119 (0.0044) | 0.022 (0.0308) |
| Línea A | Congreso | 0.096 (0.0044) | 0.094 (0.0044) | 0.127 (0.0044) | 0.025 (0.0060) |
| Línea A | Lima | 0.156 (0.0044) | 0.144 (0.0044) | 0.150 (0.0044) | 0.039 (0.0044) |
| Línea A | Loria | 0.085 (0.0044) | 0.169 (0.0044) | 0.134 (0.0044) | 0.025 (0.0044) |
| Línea A | Pasco | 0.088 (0.0044) | 0.130 (0.0044) | 0.122 (0.0044) | 0.027 (0.0308) |
| Línea A | Perú | 0.188 (0.0044) | 0.136 (0.0044) | 0.177 (0.0044) | 0.058 (0.0044) |
| Línea A | Piedras | 0.239 (0.0044) | 0.165 (0.0044) | 0.189 (0.0044) | 0.045 (0.0044) |
| Línea A | Plaza Miserere | 0.136 (0.0044) | 0.225 (0.0044) | 0.135 (0.0044) | 0.038 (0.0044) |
| Línea A | Plaza de Mayo | 0.243 (0.0044) | 0.158 (0.0044) | 0.246 (0.0044) | 0.067 (0.0044) |
| Línea A | Primera Junta | 0.218 (0.0044) | 0.342 (0.0044) | 0.148 (0.0044) | 0.031 (0.0044) |
| Línea A | Puán | 0.235 (0.0044) | 0.335 (0.0044) | 0.145 (0.0044) | 0.027 (0.0060) |
| Línea A | Río de Janeiro | 0.151 (0.0044) | 0.253 (0.0044) | 0.135 (0.0044) | 0.024 (0.0189) |
| Línea A | San José de Flores | 0.236 (0.0044) | 0.354 (0.0044) | 0.134 (0.0044) | 0.029 (0.0051) |
| Línea A | San Pedrito | 0.313 (0.0044) | 0.402 (0.0044) | 0.215 (0.0044) | 0.059 (0.0044) |
| Línea A | Sáenz Peña | 0.150 (0.0044) | 0.102 (0.0044) | 0.137 (0.0044) | 0.029 (0.0044) |
| Línea B | Callao (B) | 0.123 (0.0044) | 0.093 (0.0044) | 0.164 (0.0044) | 0.047 (0.2550) |
| Línea B | Carlos Gardel | 0.092 (0.0044) | 0.205 (0.0044) | 0.168 (0.0044) | 0.063 (0.0132) |
| Línea B | Carlos Pellegrini | 0.169 (0.0044) | 0.139 (0.0044) | 0.188 (0.0044) | 0.052 (0.4714) |
| Línea B | De los Incas | 0.189 (0.0044) | 0.329 (0.0044) | 0.212 (0.0044) | 0.049 (0.0044) |
| Línea B | Dorrego | 0.138 (0.0044) | 0.253 (0.0044) | 0.223 (0.0044) | 0.050 (0.0044) |
| Línea B | Echeverría | 0.261 (0.0044) | 0.413 (0.0044) | 0.207 (0.0044) | 0.046 (0.0044) |
| Línea B | Federico Lacroze | 0.166 (0.0044) | 0.373 (0.0044) | 0.302 (0.0044) | 0.085 (0.0240) |
| Línea B | Florida | 0.215 (0.0044) | 0.143 (0.0044) | 0.211 (0.0044) | 0.063 (0.1268) |
| Línea B | Juan Manuel de Rosas | 0.231 (0.0044) | 0.403 (0.0044) | 0.231 (0.0044) | 0.061 (0.0044) |
| Línea B | Leandro N. Alem | 0.234 (0.0044) | 0.171 (0.0044) | 0.269 (0.0044) | 0.058 (0.0044) |
| Línea B | Malabia | 0.170 (0.0044) | 0.265 (0.0044) | 0.174 (0.0044) | 0.050 (0.0044) |
| Línea B | Medrano | 0.118 (0.0044) | 0.191 (0.0044) | 0.167 (0.0044) | 0.062 (0.0044) |
| Línea B | Pasteur | 0.227 (0.0044) | 0.081 (0.0044) | 0.241 (0.0044) | 0.062 (0.0044) |
| Línea B | Pueyrredón | 0.177 (0.0044) | 0.114 (0.0044) | 0.216 (0.0044) | 0.054 (0.0044) |
| Línea B | Tronador | 0.214 (0.0044) | 0.255 (0.0044) | 0.207 (0.0044) | 0.054 (0.0060) |
| Línea B | Uruguay | 0.192 (0.0044) | 0.157 (0.0044) | 0.205 (0.0044) | 0.065 (0.0051) |
| Línea B | Ángel Gallardo | 0.145 (0.0044) | 0.267 (0.0044) | 0.182 (0.0044) | 0.061 (0.0044) |
| Línea C | Avenida de Mayo | 0.131 (0.0044) | 0.144 (0.0044) | 0.131 (0.0044) | 0.040 (0.0044) |
| Línea C | Constitución | 0.167 (0.0044) | 0.403 (0.0044) | 0.243 (0.0044) | 0.061 (0.0044) |
| Línea C | Diagonal Norte | 0.168 (0.0044) | 0.166 (0.0044) | 0.149 (0.0044) | 0.067 (0.0044) |
| Línea C | General San Martín | 0.183 (0.0044) | 0.168 (0.0044) | 0.090 (0.0044) | 0.061 (0.0044) |
| Línea C | Independencia | 0.106 (0.0044) | 0.167 (0.0044) | 0.133 (0.0044) | 0.031 (0.0625) |
| Línea C | Lavalle | 0.210 (0.0044) | 0.196 (0.0044) | 0.129 (0.0044) | 0.064 (0.0044) |
| Línea C | Moreno | 0.225 (0.0044) | 0.180 (0.0044) | 0.113 (0.0044) | 0.050 (0.0044) |
| Línea C | Retiro | 0.129 (0.0044) | 0.194 (0.0044) | 0.143 (0.0044) | 0.031 (0.0140) |
| Línea C | San Juan | 0.100 (0.0044) | 0.182 (0.0044) | 0.127 (0.0044) | 0.030 (0.1268) |
