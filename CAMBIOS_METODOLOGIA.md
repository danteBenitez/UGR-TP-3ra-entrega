# Cambios a la Metodología (Sección 3)

Guía para reescribir la Sección 3 del documento final a partir de las decisiones registradas en `DECISIONES_METODOLOGICAS.md` (DM-01 a DM-07). Complementa a `CAMBIOS_MARCO_TEORICO.md` (Sección 2) y a `ESTRUCTURA_SECCION_4.md` (Sección 4).

**Nivel de cambio:** Ninguno · Menor (una o dos oraciones) · Moderado (parte del contenido) · Mayor (subsección completa) · Pendiente (depende de una decisión abierta).

---

## Resumen

La metodología cambia bastante más que el marco teórico: **cerca del 60–70% de la Sección 3**. Es esperable, porque la sección describe procedimientos y la mayoría cambió. Se conservan el enfoque (cuantitativo, no experimental), la adaptación de CRISP-DM y la organización en fases; cambia el contenido de casi todas ellas.

- **Se reescriben por completo:** 3.4 (análisis exploratorio y comparación) y 3.5 (ingeniería de características).
- **Se reescriben en gran parte:** 3.3 (preparación), 3.6 (modelado) y 3.7 (evaluación).
- **Cambios moderados:** 3 (introducción), 3.1 (enfoque y fases), 3.2 (comprensión y adquisición) y 3.8 (métricas operativas).
- **Cambios menores:** 3.9 (herramientas).

---

## Criterios derivados

Tres criterios que la Sección 3 debe explicitar. No requieren una decisión propia porque se siguen de decisiones ya tomadas, pero hoy son inconsistentes entre el análisis y el código del modelo (rama `origin/model`).

1. **Exclusión de días sin servicio (se sigue de DM-04).** Se excluyen los días-estación con **ingreso total nulo**, tanto en el análisis como en el modelo. El código del modelo usaba un umbral de menos de 20 ingresos diarios, que se abandona en favor del criterio único de DM-04. El análisis de sensibilidad de DM-04 muestra que la elección casi no altera los resultados (menos de 0,4 pp en la retención de red); lo que importa es la coherencia.
2. **Acotamiento de valores atípicos (se sigue del alcance de DM-04: día típico para servicios regulares).** En los **datos de entrenamiento del modelo**, los ingresos por ventana que superan un umbral alto se acotan a ese umbral. Como el método fundamenta la diagramación regular, y los eventos excepcionales requieren decisiones operativas propias, que esos días no arrastren la estimación es coherente con el alcance.
   - El umbral se calcula por estación × tipo de día (tres categorías, DM-03) usando **sólo datos anteriores al origen** de cada evaluación, para no introducir fuga. El código actual usa el máximo entre el percentil 99,9 y Q3 + 4,5·IQR, calculado por estación × hábil/no laborable sobre 2014–2017; debe adaptarse a ambos puntos.
   - El **análisis descriptivo e inferencial** (retención, TV, permutación) usa los valores observados sin acotar, de modo que los días excepcionales siguen visibles en la caracterización.
   - Debe corregirse el texto actual de 3.3, que afirma que los eventos reales "deban conservarse".
3. **Cierres parciales en el modelo (se sigue del alcance de DM-04; contraparte del criterio 2).** Los días con ingreso positivo pero menor al 10% de la mediana de la estación para su tipo de día (cierres parciales) se excluyen del cálculo de niveles, perfiles y rezagos del modelo, y de sus objetivos de entrenamiento. La mediana se calcula sólo con datos anteriores a cada origen. La evaluación incluye todos los días con servicio, y el análisis descriptivo los conserva (con análisis de sensibilidad, DM-04). Sin este criterio, el nivel reciente de algunas estaciones caía a ~1 pasajero diario (cierres dominicales de la Línea B a fines de 2014 con 1 o 2 ingresos registrados) y desestabilizaba el modelo de volumen (DM-06).

---

## Tabla de cambios por subsección

| Subsección actual | Cambio | Qué cambia | Fuente |
|---|---|---|---|
| **3 (introducción)** | Menor, pero necesario | Restos de la plantilla, Fig. 2 ajena al trabajo, "ocho fases" frente a nueve subsecciones; el propósito pasa a ser anticipar la demanda de la próxima temporada | DM-06 |
| **3.1 Enfoque y fases** | Moderado | Estrategia en dos líneas (análisis observado y modelo de planificación); se rehace la Tabla 1 | DM-04, DM-06, DM-07 |
| **3.2 Fases 1 y 2** | Moderado | Unidad de análisis, tres tipos de día, geolocalización opcional | DM-03, DM-04 |
| **3.3 Fase 3: preparación** | Moderado–mayor | Parseo explícito de fechas y control de calendario, clasificación de tipos de día, exclusión de días sin servicio, grilla regular, acotamiento de atípicos sólo para el modelo | DM-01, DM-03, DM-04, criterios derivados |
| **3.4 Fase 4: exploratorio y comparación** | Mayor | Se reemplazan KDE y K-S por perfiles, retención con IC, TV y permutación | DM-03, DM-04, DM-07 |
| **3.5 Fase 5: características** | Mayor | Dos objetivos (volumen y forma), variables a la fecha de origen, sólo rezagos estacionales; se eliminan los horizontes de uno y varios pasos | DM-06 |
| **3.6 Fase 6: modelado** | Moderado–mayor | Modelos de referencia en lugar de la regresión lineal; XGBoost sobre el cociente de volumen; predicción = volumen × forma | DM-06 |
| **3.7 Fase 7: evaluación** | Moderado–mayor | Origen móvil por temporada; métricas por ventana y por perfil; tres tipos de día | DM-06 |
| **3.8 Fase 8: métricas operativas** | Mayor | Sin desplazamiento de picos; la presión de andén se reemplaza por la frecuencia mínima requerida; categorización por estación determinante | DM-05, DM-06, DM-07 |
| **3.9 Herramientas** | Menor | Bibliotecas efectivamente usadas, entorno reproducible, notebook único y registro de decisiones | — |

---

## Detalle de los cambios

### 3 (introducción)
- **Eliminar los restos de la plantilla:** "Debe hacer una introducción del tópico de la sección de dos párrafos pero no debe quedar como una sección" y "Descripción del procedimiento o metodología que se utilizará para la ejecución".
- **Eliminar la Fig. 2 ("Fases (son ejemplos)")**, una imagen de ejemplo del ciclo de proyecto de Ambler, ajena al trabajo. Si se quiere una figura, puede reemplazarse por un diagrama propio de las fases.
- **Corregir la cantidad de fases:** el texto dice "ocho fases" y la sección tiene nueve subsecciones de fase. Con la estructura propuesta abajo son ocho fases más una subsección de herramientas que no es una fase.
- **Propósito:** reemplazar "construir un modelo capaz de anticipar el flujo por estación y ventana horaria" por "construir un modelo capaz de anticipar la demanda por estación, tipo de día y ventana horaria **de la próxima temporada**, con la información disponible antes de su inicio".

### 3.1 Enfoque metodológico y fases
Reemplazar la estrategia general ("estimar una función que, a partir de características temporales, espaciales y de rezagos, prediga la cantidad de ingresos… sobre sus predicciones se calculan… el desplazamiento de las horas pico y la presión de andén") por una estrategia en dos líneas:
1. **Análisis de los datos observados:** caracterizar la demanda y contrastar la hipótesis, separando volumen (retención) y distribución horaria (TV), con inferencia por permutación (OE1 e hipótesis).
2. **Modelo de planificación:** proyectar la demanda de la próxima temporada como volumen diario × distribución horaria, evaluarlo contra modelos de referencia y derivar de sus proyecciones las métricas operativas (OE2, OE3 y OE4).

**Tabla 1 propuesta** (fases y objetivos):

| Fase | Descripción | Objetivo vinculado |
|---|---|---|
| 1. Comprensión del problema | Unidades de análisis (día-estación y ventana de 15 min), tipos de día y horizonte de planificación | General |
| 2. Adquisición y comprensión de datos | Relevamiento de fuentes, cobertura y diccionario de datos | General |
| 3. Preparación de datos | Parseo de fechas y control de calendario, tipos de día, exclusión de días sin servicio, grilla regular, acotamiento de atípicos para el modelo | OE1, OE2 |
| 4. Análisis exploratorio y comparación de perfiles | Curvas de demanda, retención con IC, distribución horaria (TV) y contraste por permutación | OE1, hipótesis |
| 5. Ingeniería de características | Volumen diario y forma; variables a la fecha de origen; rezagos estacionales | OE2 |
| 6. Modelado | Modelos de referencia y XGBoost sobre el volumen; recomposición volumen × forma | OE2 |
| 7. Evaluación | Origen móvil por temporada; métricas por ventana y por perfil | OE2 |
| 8. Métricas operativas proyectadas | Retención y distribución horaria proyectadas; frecuencia mínima requerida y categorización de estaciones | OE3, OE4 |

### 3.2 Fases 1 y 2: comprensión del problema y adquisición de datos
- **Unidad de análisis:** distinguir dos niveles.
  - *Inferencia y volumen:* el **día-estación**, porque los intervalos de un mismo día no son independientes (DM-04).
  - *Distribución horaria y modelo:* la **ventana de 15 minutos** dentro del día-estación.
- **Variable observada:** ingresos por molinete agregados por estación, fecha y ventana. Sin cambios.
- **Categorías de comparación:** reemplazar "días hábiles y no laborables (considerando, además, sábados, domingos y feriados por separado cuando el análisis lo requiera)" por las **tres categorías** de DM-03 (Hábil, Sábado, Domingo-Feriado), con remisión al marco teórico.
- **Horizonte:** agregar que el modelo planifica con una temporada de anticipación (DM-06).
- **Geolocalización:** pasa a ser opcional. Con la identidad de la estación como variable, el modelo ya captura lo que es fijo por estación; puede conservarse para interpretación o figuras.
- **Tabla 2 (tareas de adquisición):** sin cambios de fondo. En "Identificación de vacíos y feriados" puede agregarse la verificación de formatos de fecha por año.

### 3.3 Fase 3: preparación y limpieza de datos
Reescribir la lista de procedimientos para que describa lo que el notebook efectivamente hace:
- **Integración y normalización:** se conserva; agregar la normalización de las 44 estaciones a nombres canónicos.
- **Parseo de fechas (nuevo):** los archivos usan dos formatos (`AAAA-MM-DD` y `DD/MM/AAAA`). Se parsean con formatos explícitos y se valida que cada archivo anual contenga sólo fechas de su año. Un **control de calendario** verifica que ningún año tenga domingos con demanda de día hábil (DM-01).
- **Tipos de día (nuevo):** clasificación en tres categorías con el calendario de feriados nacionales, incluidas las excepciones de Jueves Santo y feriados puente (DM-03).
- **Días sin servicio:** se excluyen los días-estación con ingreso total nulo, en el análisis y en el modelo (criterio derivado 1). Reemplaza la redacción actual sobre "distinción entre cierres de servicio, ventanas sin registro y errores de carga".
- **Ventanas sin registro:** dentro de un día con servicio, una ventana sin registros significa que no hubo ingresos; se completa con 0 en una grilla regular de ventanas (05:00 a 23:45).
- **Feriados y eventos atípicos:** reemplazar el texto actual. Los feriados ya no se filtran: se clasifican (punto anterior). Los valores extremos se **acotan sólo en los datos de entrenamiento del modelo** (criterio derivado 2), y se elimina la afirmación de que los eventos reales "deban conservarse".

### 3.4 Fase 4: análisis exploratorio y comparación de perfiles
Se reescribe. Contenido:
- **Curvas de demanda:** perfiles horarios medios por tipo de día, por línea y en estaciones representativas; estacionalidad mensual por tipo de día.
- **Volumen:** ratio de retención por línea y estación, para Sábado y Domingo-Feriado respecto de Hábil, con **IC 95% por bootstrap** sobre días. Sin contraste de hipótesis (DM-04).
- **Distribución horaria:** perfil normalizado por estación y tipo de día; **distancia de variación total** entre perfiles; curva de diferencias por ventana para localizar las franjas que difieren (DM-04, DM-07).
- **Contraste de la hipótesis:** test de permutación sobre días completos, estratificado por año-mes, con B ≥ 10.000 y corrección de Holm entre las 44 estaciones. El resultado principal es el tamaño de efecto.
- **Validación de las categorías:** comparación domingo frente a feriado con el mismo método, que respalda su agrupación (DM-03).
- **Se elimina:** el método gráfico KDE y la prueba de Kolmogorov-Smirnov.
- Se conserva el cierre ("el resultado de esta fase justifica la hipótesis de heterogeneidad…"), ajustado a volumen y distribución horaria.

### 3.5 Fase 5: ingeniería de características y variables objetivo
Se reescribe. Contenido:
- **Dos variables objetivo:**
  - *Volumen diario* por estación-día, modelado como **cociente respecto del nivel reciente** (promedio de los últimos tres meses antes del origen), porque los modelos de árboles no extrapolan tendencias.
  - *Forma:* perfil normalizado de los últimos 12 meses por estación × tipo de día. Se estima directamente, sin modelo, porque es estable.
- **Variables admisibles,** calculadas **a la fecha de inicio de cada temporada**, también para las temporadas de entrenamiento:
  - *Calendario:* tipo de día, día de la semana, mes, día del mes, feriado, puente, víspera y día posterior a un feriado.
  - *Estación:* identidad (y opcionalmente geolocalización).
  - *Rezagos estacionales:* volumen de 52 semanas antes.
  - *Niveles:* nivel reciente, nivel histórico, factor estacional del año previo.
- **Se eliminan:** los rezagos de corto plazo (`lag_1` a `lag_4`, `media_movil_1h`, rezagos de un día y de una semana) y los horizontes de uno y varios pasos con las estrategias recursiva y directa.

### 3.6 Fase 6: modelado
- **Modelos de referencia** (reemplazan a la regresión lineal como base):
  - *Perfil histórico:* promedio por estación × tipo de día × ventana sobre los datos anteriores al origen.
  - *Estacional ingenuo:* nivel reciente × factor estacional del año previo, multiplicado por la forma.
- **Modelo de aprendizaje automático:** XGBoost sobre el cociente de volumen, multiplicado por la forma.
- **Estructura alternativa:** XGBoost directo sobre los ingresos por ventana, con las mismas variables admisibles, para mostrar el efecto de separar volumen y forma. Ambos modelos XGBoost reciben el mismo esfuerzo de ajuste y el mismo tratamiento del nivel (DM-06).
- El modelo de pronóstico en tiempo real no se incluye ni se menciona.
- **Ajuste de hiperparámetros:** con las temporadas de 2018, respetando el mismo esquema de origen móvil.
- Si la regresión lineal se mantiene, debe usarse con las mismas variables admisibles y presentarse como un modelo más, no como la referencia.

### 3.7 Fase 7: validación y evaluación
- **Evaluación con origen móvil por temporada:** para cada temporada de 2019, el modelo se entrena sólo con datos anteriores a su inicio y predice esa temporada. Reemplaza la partición única (entrenamiento 2014–2017, validación 2018, prueba 2019). Se conserva el argumento sobre la fuga de datos.
- **Métricas por ventana:** MSE, RMSE, MAE y R².
- **Métricas por perfil** (nivel relevante para la diagramación): TV entre perfil predicho y observado, error de retención y error de volumen medio por estación, y sesgo de volumen por temporada y tipo de día.
- **Criterio de selección:** reemplazar "priorizando aquel que minimice el error de generalización de forma consistente en ambos tipos de día" por: el modelo se adopta si supera a los modelos de referencia en las métricas por perfil, de forma consistente en los **tres** tipos de día y en las cuatro temporadas.

### 3.8 Fase 8: métricas operativas proyectadas
- **Ratio de retención:** se calcula sobre las proyecciones para temporadas no vistas por el modelo. Ya no reproduce valores observados (DM-06).
- **Distribución horaria:** reemplaza al desplazamiento de las horas pico. Se compara el perfil proyectado de cada tipo de día con TV y la curva de diferencias (DM-07).
- **Frecuencia mínima requerida** (reemplaza a la presión de andén, DM-05): para cada línea, tipo de día y ventana, el máximo entre estaciones de los ingresos proyectados dividido por la capacidad útil por formación (capacidad × ocupación objetivo). Los ingresos cuentan completos en las cabeceras y a la mitad en las estaciones intermedias (reparto parejo entre sentidos). Se expresa en trenes por ventana o como intervalo máximo entre trenes. Es exacta en las cabeceras y una cota inferior en las estaciones intermedias, por la carga a bordo desconocida y el reparto real entre sentidos.
- **Categorización de estaciones:** por **estación determinante** (la que fija la frecuencia de su línea en cada tipo de día y franja) y por exigencia relativa respecto de su línea, con **reglas explícitas aplicadas por código** sobre las proyecciones, de modo que tablas y figuras no puedan contradecirse.
- **Contraste con los cronogramas publicados** (opcional): como validación independiente, declarando la diferencia de período si se usan los cronogramas actuales.

### 3.9 Herramientas y reproducibilidad
- **Bibliotecas:** pandas, NumPy, SciPy, matplotlib y seaborn; **holidays** (fuente del calendario de feriados, relevante para DM-03); **XGBoost** (modelado); pyarrow (formato Parquet). scikit-learn puede dejar de mencionarse si no se usa (dependía de la regresión Ridge).
- **Entorno reproducible:** dependencias declaradas en `pyproject.toml` y fijadas en `uv.lock`, gestionadas con uv.
- **Notebook único:** todo el procedimiento se ejecuta en `notebook_eda_subte.ipynb`, que regenera datos procesados, tablas y figuras.
- **Registro de decisiones:** las decisiones metodológicas y su justificación se documentan en `DECISIONES_METODOLOGICAS.md`, como parte de la trazabilidad del trabajo.
- **Numeración:** presentarla como subsección final (3.9 Herramientas y reproducibilidad), no como "Fase 9".

---

## Coherencia entre secciones

Al reescribirse, cada parte de la Sección 3 debe corresponderse con el marco teórico y los resultados:

| Metodología | Marco teórico | Resultados |
|---|---|---|
| 3.2 Unidades de análisis y tipos de día | 2.2.3 (tipos de día) | 4.1 |
| 3.3 Preparación | 2.2.3, 2.2.4.5 | 4.1 |
| 3.4 Exploratorio y comparación | 2.2.4.1, 2.5.1–2.5.4 | 4.2, 4.3 |
| 3.5–3.7 Modelo | 2.3.2–2.3.4, 2.4.1 | 4.4 |
| 3.8 Métricas operativas | 2.2.4 | 4.5 |

(Numeración del marco teórico según la estructura propuesta en `CAMBIOS_MARCO_TEORICO.md`.)

---

## Pendiente

- **Datos para la frecuencia requerida (DM-05):** capacidad por coche y coches por formación de la flota actual de cada línea, densidad de pie y ocupación objetivo. Sólo afectan la escala absoluta de 3.8: la categorización de estaciones no depende de ellos.
- **Definición de temporada (DM-06, decisión pendiente 1):** afecta 3.2 (horizonte), 3.5 (fecha de origen de las variables) y 3.7 (temporadas de evaluación).
