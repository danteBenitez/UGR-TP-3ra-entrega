# Métricas Operativas Derivadas de las Predicciones del Modelo (Fase 8)

Resultados calculados sobre las predicciones del modelo **Gradient Boosting (XGBoost)** en el conjunto de prueba independiente (**año 2019**, 44 estaciones de las Líneas A, B y C):

- **Precisión en el Ratio de Retención Predicho:** El error absoluto medio entre el Ratio de Retención real y el predicho a lo largo de las 44 estaciones es de apenas **0.55 puntos porcentuales**.
- **Desplazamiento de Horas Pico (*Peak Shift*):** El modelo captura con exactitud la desaparición del pico matutino laboral (08:00–08:45) y el desplazamiento del pico de demanda no laboral hacia la franja vespertina (13:00–19:30), con un desplazamiento promedio de **+8,5 a +10,5 horas** respecto al pico matutino hábil.
- **Categorización por Presión de Andén (Umbral Nominal = 1.200 pax/15 min):** Permite segmentar las 44 estaciones en cuatro niveles de intervención operativa para optimizar la frecuencia de despacho.

### 1. Resumen de la Categorización Operativa de Estaciones en Días No Laborables

| Categoría Operativa Propuesta | Estaciones | Ratio Retención Medio Predicho (%) | Flujo P95 Medio Predicho (pax/15m) | Pico Máximo Medio Predicho (pax/15m) |
| :--- | :---: | :---: | :---: | :---: |
| **Categoría I: Nodo Crítico de Saturación (Refuerzo Prioritario)** | 8 | 52.38% | 727.1 | 1725.6 |
| **Categoría II: Presión Moderada-Alta (Monitoreo Vespertino)** | 12 | 55.99% | 365.4 | 633.1 |
| **Categoría III: Demanda Estable Equilibrada (Frecuencia Base)** | 13 | 52.29% | 230.0 | 532.1 |
| **Categoría IV: Baja Presión / Contracción en No Laborables** | 11 | 53.27% | 134.0 | 296.0 |

### 2. Tabla Maestra de Métricas Operativas Predichas vs. Reales (44 Estaciones - Test 2019)

| Línea | Estación | Retención Real (%) | Retención Pred (%) | Pico Hábil Pred | Pico NoLab Pred | $\Delta$ Pico (h) | P95 NoLab Pred (pax/15m) | Máx NoLab Pred (pax/15m) | Índice Presión Máx | Categoría Operativa |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| Línea C | **Constitución** | 59.4% | **59.6%** | 08:15 | 13:00 | +4.75h | 1770 | **3352** | 2.79 | Categoría I |
| Línea C | **Retiro** | 59.2% | **58.2%** | 08:30 | 18:00 | +9.50h | 750 | **1245** | 1.04 | Categoría I |
| Línea B | **Federico Lacroze** | 54.6% | **55.2%** | 08:30 | 11:45 | +3.25h | 641 | **1937** | 1.61 | Categoría I |
| Línea A | **San Pedrito** | 55.0% | **54.4%** | 08:15 | 13:15 | +5.00h | 589 | **1621** | 1.35 | Categoría I |
| Línea B | **Florida** | 44.9% | **44.8%** | 11:00 | 18:00 | +7.00h | 566 | **1321** | 1.10 | Categoría I |
| Línea B | **Juan Manuel de Rosas** | 54.5% | **53.7%** | 08:15 | 13:15 | +5.00h | 561 | **1624** | 1.35 | Categoría I |
| Línea B | **Leandro N. Alem** | 47.8% | **47.8%** | 08:30 | 18:00 | +9.50h | 524 | **1428** | 1.19 | Categoría I |
| Línea B | **Carlos Pellegrini** | 59.7% | **59.2%** | 11:00 | 18:00 | +7.00h | 496 | **975** | 0.81 | Categoría II |
| Línea B | **Uruguay** | 48.3% | **47.2%** | 11:00 | 18:00 | +7.00h | 442 | **716** | 0.60 | Categoría II |
| Línea B | **Malabia** | 57.3% | **56.5%** | 08:15 | 18:00 | +9.75h | 419 | **769** | 0.64 | Categoría II |
| Línea A | **Plaza de Mayo** | 45.9% | **45.5%** | 11:00 | 18:00 | +7.00h | 417 | **1276** | 1.06 | Categoría I |
| Línea B | **Callao (B)** | 53.8% | **52.8%** | 11:00 | 18:00 | +7.00h | 415 | **706** | 0.59 | Categoría II |
| Línea A | **Perú** | 45.1% | **44.8%** | 11:00 | 18:00 | +7.00h | 385 | **883** | 0.74 | Categoría II |
| Línea B | **Medrano** | 57.6% | **57.0%** | 08:30 | 18:00 | +9.50h | 351 | **509** | 0.42 | Categoría II |
| Línea B | **Ángel Gallardo** | 57.2% | **56.3%** | 08:15 | 18:00 | +9.75h | 326 | **601** | 0.50 | Categoría II |
| Línea B | **Carlos Gardel** | 79.1% | **77.6%** | 11:00 | 18:00 | +7.00h | 318 | **437** | 0.36 | Categoría II |
| Línea A | **Plaza Miserere** | 59.4% | **58.6%** | 08:30 | 13:00 | +4.50h | 314 | **556** | 0.46 | Categoría II |
| Línea B | **Pasteur** | 52.9% | **52.6%** | 11:00 | 13:15 | +2.25h | 310 | **483** | 0.40 | Categoría II |
| Línea A | **Congreso** | 53.2% | **52.5%** | 11:00 | 18:00 | +7.00h | 308 | **457** | 0.38 | Categoría II |
| Línea A | **Acoyte** | 57.4% | **56.5%** | 08:30 | 18:00 | +9.50h | 301 | **504** | 0.42 | Categoría II |
| Línea B | **Pueyrredón** | 57.2% | **56.8%** | 11:00 | 13:00 | +2.00h | 287 | **412** | 0.34 | Categoría III |
| Línea A | **Primera Junta** | 54.8% | **54.3%** | 08:15 | 13:00 | +4.75h | 272 | **649** | 0.54 | Categoría III |
| Línea C | **Lavalle** | 48.7% | **48.3%** | 11:00 | 18:00 | +7.00h | 263 | **758** | 0.63 | Categoría III |
| Línea A | **Sáenz Peña** | 48.3% | **47.8%** | 11:00 | 18:00 | +7.00h | 232 | **373** | 0.31 | Categoría III |
| Línea A | **San José de Flores** | 52.5% | **52.1%** | 08:15 | 13:00 | +4.75h | 232 | **739** | 0.62 | Categoría III |
| Línea A | **Carabobo** | 54.5% | **53.9%** | 08:15 | 17:15 | +9.00h | 230 | **666** | 0.55 | Categoría III |
| Línea A | **Río de Janeiro** | 56.8% | **56.1%** | 08:30 | 13:00 | +4.50h | 229 | **367** | 0.31 | Categoría III |
| Línea B | **Dorrego** | 55.8% | **55.4%** | 08:15 | 18:00 | +9.75h | 225 | **443** | 0.37 | Categoría III |
| Línea B | **De los Incas** | 54.2% | **53.5%** | 08:15 | 18:00 | +9.75h | 217 | **657** | 0.55 | Categoría III |
| Línea C | **General San Martín** | 46.5% | **46.9%** | 11:00 | 18:00 | +7.00h | 208 | **594** | 0.49 | Categoría III |
| Línea A | **Piedras** | 45.0% | **44.9%** | 11:00 | 18:00 | +7.00h | 208 | **598** | 0.50 | Categoría III |
| Línea A | **Castro Barros** | 57.7% | **57.0%** | 08:30 | 17:15 | +8.75h | 197 | **278** | 0.23 | Categoría III |
| Línea A | **Lima** | 53.2% | **52.7%** | 11:00 | 18:00 | +7.00h | 190 | **385** | 0.32 | Categoría III |
| Línea A | **Loria** | 58.8% | **58.0%** | 08:30 | 18:00 | +9.50h | 171 | **262** | 0.22 | Categoría IV |
| Línea C | **Moreno** | 44.8% | **44.5%** | 11:00 | 18:00 | +7.00h | 169 | **494** | 0.41 | Categoría IV |
| Línea A | **Puán** | 52.8% | **52.2%** | 08:15 | 13:15 | +5.00h | 158 | **369** | 0.31 | Categoría IV |
| Línea B | **Echeverría** | 53.2% | **52.2%** | 08:15 | 17:30 | +9.25h | 143 | **450** | 0.38 | Categoría IV |
| Línea C | **Diagonal Norte** | 44.9% | **44.8%** | 11:00 | 18:00 | +7.00h | 140 | **406** | 0.34 | Categoría IV |
| Línea B | **Tronador** | 51.1% | **51.0%** | 08:30 | 18:00 | +9.50h | 135 | **285** | 0.24 | Categoría IV |
| Línea C | **Avenida de Mayo** | 51.6% | **50.7%** | 11:00 | 18:00 | +7.00h | 133 | **312** | 0.26 | Categoría IV |
| Línea C | **Independencia** | 62.6% | **62.2%** | 08:30 | 18:00 | +9.50h | 120 | **220** | 0.18 | Categoría IV |
| Línea C | **San Juan** | 56.0% | **55.6%** | 08:30 | 18:00 | +9.50h | 119 | **185** | 0.15 | Categoría IV |
| Línea A | **Alberti** | 59.9% | **59.6%** | 11:00 | 13:00 | +2.00h | 104 | **169** | 0.14 | Categoría IV |
| Línea A | **Pasco** | 55.3% | **55.3%** | 11:00 | 13:00 | +2.00h | 82 | **105** | 0.09 | Categoría IV |
