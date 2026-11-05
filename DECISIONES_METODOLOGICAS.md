# Registro de Decisiones Metodológicas

Registro de los cambios de método, correcciones y reinterpretaciones del análisis, con su justificación y su impacto sobre los resultados y sobre el **marco teórico** de la entrega escrita. Cada cambio que altere qué se mide, cómo se infiere o cómo se interpreta un resultado debe registrarse aquí antes de incorporarse al texto.

**Estados:** `Propuesta` (en discusión) · `Aceptada` (pendiente de implementar) · `Implementada` · `Descartada`

---

## DM-01 · Corrección del parseo de fechas
- **Estado:** Implementada (2026-11-04, commit `b39f47a`)
- **Tipo:** Corrección de error (no es un cambio de método)
- **Problema:** `pd.to_datetime(format='mixed', dayfirst=True)` invertía día y mes en las fechas ISO de 2014, 2015, 2018 y 2019 cuando el día era ≤ 12. Cerca del 36% de los días de esos años quedaban con día de semana, mes, feriado y tipo de día erróneos.
- **Cambio:** Parseo con formatos explícitos (`%Y-%m-%d`, `%d/%m/%Y`), validación de que cada archivo anual sólo contiene fechas de su año y control de calidad de calendario (sección 2.5 del notebook).
- **Impacto en resultados:** Todos los indicadores cambian. Retención global 42,03% → 27,86%; eventos de presión de andén 5.253 → 750.
- **Impacto en el marco teórico:** Ninguno. Sí en la sección de resultados y discusión (ver DM-02 y DM-03).

## DM-02 · Reinterpretación de la presión de andén
- **Estado:** Implementada (2026-11-04, commit `6a9b3bb`); la métrica se reemplaza por la frecuencia mínima requerida (ver DM-05)
- **Tipo:** Reinterpretación de un resultado
- **Cambio:** Con los datos corregidos, los 750 intervalos críticos ocurren todos en Constitución, el 92% entre las 07:00 y las 10:00 y casi todos en sábados. Se elimina la afirmación de saturación generalizada en nodos de transbordo durante fines de semana; el hallazgo se interpreta como persistencia del viaje laboral matutino de los sábados en la cabecera de la Línea C.
- **Impacto en el marco teórico:** La discusión no puede apoyarse en la idea de que la reducción de frecuencias de fin de semana satura los nodos de transbordo en general.

## DM-03 · Clasificación de tipos de día: Hábil / Sábado / Domingo-Feriado
- **Estado:** Implementada (2026-11-05). La clasificación se calcula con `agregar_calendario()` (notebook, sección 2.2), que se aplica en la ingesta y al cargar los datos cacheados; la sección 2.6 muestra los días por tipo y las excepciones. Todas las tablas y figuras usan las tres categorías. *Nota:* las cifras de evidencia de esta entrada son las del análisis exploratorio previo (Jueves Santo todavía contado como feriado); con la clasificación implementada, la retención de red es 38,58% (Sábado) y 19,60% (Domingo-Feriado), y la de los feriados, 21,95%; tras excluir los días sin servicio (DM-04), 38,59%, 19,80% y 22,21%. Con el método de DM-04, la TV mediana entre domingos y feriados es 0,049 (rango 0,022–0,085), sin diferencia significativa en 5 de las 44 estaciones.
- **Tipo:** Cambio de clasificación

### Decisión
Se reemplaza la dicotomía Hábil / No Laborable por **tres categorías**, que coinciden con los cronogramas de servicio del operador (Emova opera con horarios de días hábiles, de sábados y de domingos y feriados):

| Categoría | Incluye |
|---|---|
| **Hábil** | Lunes a viernes no feriados |
| **Sábado** | Sábados no feriados y **Jueves Santo** cuando no coincide con otro feriado |
| **Domingo-Feriado** | Domingos y feriados nacionales, incluidos los **feriados con fines turísticos** (puentes) |

### Por qué no dos categorías
Los días no laborables no son un régimen homogéneo:
- **Volumen:** la retención es de 38,48% en sábados, 18,78% en domingos y 22,87% en feriados.
- **Forma:** la distancia de variación total (TV, ver DM-04) entre sábado y domingo tiene una mediana de 0,170 entre estaciones (rango 0,091–0,311), del mismo orden que la distancia entre domingo y día hábil (0,193). El sábado tiene una meseta centrada en el mediodía; el domingo, su máximo al atardecer.

Agruparlos mezcla dos perfiles distintos en uno que no representa a ninguno.

### Por qué feriados junto con domingos
No se asume: se contrastó con los datos (análisis exploratorio, 1.000 permutaciones estratificadas por año-trimestre, excluyendo días sin servicio):
- **Forma:** la TV entre domingos y feriados tiene una mediana de 0,052 entre estaciones (rango 0,025–0,089), cerca de un tercio de la distancia sábado-domingo.
- **Feriado por feriado:** de los 108 feriados observados, el perfil de red de 92 se parece más al domingo medio que al sábado o al día hábil.
- **Volumen:** los feriados son algo más concurridos que los domingos (retención mediana 22,5% frente a 18,5%).
- El test de permutación rechaza la igualdad de forma en 42 de 44 estaciones, pero con un tamaño de efecto pequeño (TV ≈ 0,05). Es un caso de lo señalado en DM-04: con este volumen de datos, diferencias menores resultan significativas, y lo relevante es la magnitud.

El agrupamiento queda así respaldado tanto por la práctica operativa como por los datos. La diferencia residual se informa como hallazgo: los feriados tienen forma de domingo, con algo más de volumen.

### Excepciones
- **Jueves Santo** (sólo cuando no coincide con otro feriado; en el período: 2014, 2017, 2018 y 2019). Legalmente es un día no laborable optativo, no un feriado. Los datos muestran demanda de sábado (3 de los 4 días) o de día hábil (1), lejos del domingo (TV mediana 0,171 al domingo frente a 0,090 al día hábil). El operador lo trata como sábado: en 2024 "el Subte funcionará con el horario de los días sábado" (*enelsubte.com*, "Cronograma de servicio de Subte para la Semana Santa", 27/03/2024). Se clasifica como **Sábado**. *Supuesto:* la fuente es posterior al período de estudio; se asume que la práctica operativa era la misma en 2014–2019. En 2015 y 2016 el Jueves Santo coincidió con feriados nacionales (2 de abril y 24 de marzo) y se mantiene como Domingo-Feriado.
- **Feriados con fines turísticos** (puentes; 12 días en el período). Su demanda queda entre la de sábado y la de domingo (6 se parecen más al sábado, 5 al domingo, 1 al día hábil). Se clasifican como **Domingo-Feriado**, consistente con su tratamiento como feriado en la operación del servicio. La demanda intermedia se menciona como matiz.

### Observaciones sobre la fuente de feriados
La librería `holidays` lista entre 17 y 20 fechas por año. Incluye el Jueves Santo y los feriados puente. Cuando dos feriados coinciden en una fecha, la registra con un solo nombre.

### Impacto en el marco teórico
- La definición operativa de tipo de día pasa de dos a tres categorías y se fundamenta tanto en la práctica operativa (cronogramas del operador) como en la evidencia empírica.
- Las hipótesis y comparaciones se formulan entre tres categorías (Hábil–Sábado, Hábil–Domingo-Feriado, Sábado–Domingo-Feriado).
- Se explicitan las excepciones (Jueves Santo, puentes) y el supuesto sobre la práctica operativa.

## DM-04 · Rediseño de la validación estadística: volumen y forma
- **Estado:** Implementada (2026-11-05). Notebook: exclusión de días sin servicio al cargar los datos (2.4) y sensibilidad (2.7); retención con IC por bootstrap de fechas completas, 2.000 remuestreos (sección 5); perfiles normalizados, TV y test de permutación con B = 10.000 y Holm (sección 6). Se eliminan el KDE y la prueba K-S. La banda simultánea se implementó en la figura de diferencias por ventana.
- **Tipo:** Cambio de método inferencial (reemplaza el test K-S actual)

**Núcleo del método** (lo esencial para el marco teórico):
1. Separar **volumen** (cuánta demanda se pierde) de **forma** (cuándo ocurre dentro del día).
2. Estimar el volumen con el ratio de retención y su intervalo de confianza; medir la forma con la **distancia de variación total (TV)** entre perfiles diarios normalizados.
3. Contrastar la forma con un **test de permutación sobre días completos**, estratificado por año-mes, con corrección de Holm entre estaciones.

El resto del registro detalla y justifica cada elemento.

### Problema del diseño actual
El test actual aplica K-S de dos muestras sobre todos los intervalos de 15 minutos de cada estación, agrupados por tipo de día. Presenta tres problemas:
1. **No evalúa la hipótesis de interés.** Compara la distribución de *valores* por intervalo, sin considerar en qué momento del día ocurren. Una diferencia sólo de volumen (un día no laborable que fuera un día hábil escalado) también llevaría a rechazar H₀. El test, por lo tanto, no distingue entre "hay menos demanda" y "la demanda se distribuye distinto en el día", que es la afirmación central del trabajo.
2. **Viola el supuesto de independencia.** Los intervalos de un mismo día están fuertemente autocorrelacionados; los p-valores asintóticos de K-S no son válidos.
3. **No es informativo.** Con n ≈ 150.000 por estación, cualquier diferencia resulta significativa; el rechazo en el 100% de las estaciones no dice nada sobre la magnitud.

### Reformulación: dos preguntas separadas
La diferencia entre días hábiles y no laborables se descompone en dos dimensiones, con el **día-estación** como unidad de análisis:
- **Volumen:** ¿cuánta demanda se pierde? → se **estima**, sin contraste de hipótesis.
- **Forma:** ¿cuándo ocurre la demanda dentro del día? → H₀ꜰ: el perfil intradiario (proporción de los ingresos del día en cada ventana de 15 min) es igual entre tipos de día.

### Volumen
Ratio de retención con intervalo de confianza al 95% por *bootstrap* sobre días: se remuestrean días completos dentro de cada tipo de día y se recalcula el ratio.

No se plantea un contraste de hipótesis sobre el volumen: que la demanda no laborable sea menor que la hábil no está en discusión, y un test sólo confirmaría lo evidente. Lo relevante para la decisión operativa es la **magnitud** de la caída y su precisión, que es lo que informa el intervalo de confianza.

### Forma
1. **Perfil diario normalizado.** Cada día-estación se representa como un vector de 96 proporciones que suman 1. Esto elimina el volumen: un día que fuera una versión escalada de otro tendría exactamente el mismo perfil.
2. **Perfil medio por estación y tipo de día.** Para cada estación, se promedian los perfiles diarios de todos sus días hábiles (perfil *p*) y, por separado, los de todos sus días no laborables (perfil *q*). Cada día pesa lo mismo, de modo que los días de mayor afluencia no dominan la forma. El resultado es un único valor de TV por estación.

   *Justificación de la ponderación uniforme:* el método busca fundamentar la diagramación de servicios **regulares**, por lo que el perfil relevante es el del día típico. Que no todos los sábados tengan la misma concurrencia es parte de esa realidad y debe reflejarse en el perfil. Ponderar por volumen haría que los días excepcionalmente concurridos (eventos, fechas especiales) arrastraran el perfil hacia situaciones que requieren decisiones operativas específicas, fuera del alcance de este análisis.
3. **Estadístico principal: distancia de variación total (TV).** Sean pᵢ y qᵢ las proporciones de la demanda diaria que ingresa en la ventana *i* en el perfil medio de días hábiles y de días no laborables, respectivamente. Cada ventana se compara únicamente con la misma ventana del otro perfil:
   $$TV = \tfrac{1}{2}\sum_{i=1}^{96} |p_i - q_i| \;=\; 1 - \sum_{i=1}^{96} \min(p_i, q_i)$$
   En cada ventana, min(pᵢ, qᵢ) es la porción de la demanda diaria que ambos perfiles comparten; su suma es la superposición total entre perfiles. TV es la proporción de la demanda diaria **no compartida** (0 = perfiles idénticos; 1 = perfiles sin ninguna ventana en común). Por ejemplo, TV = 0,30 indica que el 70% de la distribución horaria de la demanda coincide entre ambos tipos de día y el 30% restante no.
4. **Localización (opcional, ilustrativa).** Para mostrar *en qué franjas* difieren los perfiles, se grafica la curva de diferencias por ventana (qᵢ − pᵢ) para algunas estaciones representativas. Si se desea indicar qué ventanas difieren significativamente, puede agregarse una banda ±c: en cada permutación (ver *Inferencia*) se registra la mayor diferencia absoluta entre todas las ventanas, y c es el percentil 95 de esos máximos. Las ventanas que superan ±c difieren con un error del 5% para el conjunto de las 96 ventanas a la vez. La banda puede omitirse si complica la presentación; la curva por sí sola ya cumple la función descriptiva.

**¿Por qué TV y no K-S sobre el perfil acumulado?** El estadístico K-S (máxima diferencia entre perfiles acumulados) coincide con TV cuando un tipo de día está simplemente "adelantado" respecto del otro, pero la subestima cuando las curvas acumuladas se cruzan, porque las diferencias de signo opuesto se compensan. Un análisis exploratorio sobre las 44 estaciones muestra dos grupos:
- **Estaciones de origen residencial** (p. ej. San Pedrito, Carabobo, Echeverría, Constitución): las curvas no se cruzan y K-S = TV. La diferencia es un desplazamiento temporal: el día hábil comienza más temprano.
- **Estaciones centrales** (p. ej. Florida, Piedras, Diagonal Norte, Plaza de Mayo, Leandro N. Alem): las curvas se cruzan de 1 a 3 veces y TV es entre 1,5 y 2 veces K-S. La diferencia es una redistribución: pico vespertino de regreso en días hábiles frente a demanda distribuida al mediodía en no laborables.

K-S subestimaría sistemáticamente la diferencia de forma justamente en las estaciones del Microcentro, centrales para la argumentación del trabajo.

**Limitación de TV:** no considera la distancia temporal (desplazar un pico 15 minutos o 6 horas puede pesar lo mismo). Se acepta esta limitación; la curva de diferencias por ventana (punto 4) muestra dónde ocurren los desplazamientos.

### Inferencia: test de permutación
Bajo H₀ꜰ, la etiqueta de tipo de día no aporta información sobre el perfil. El procedimiento, para cada estación, es:
1. Calcular TV con las etiquetas reales (TV_obs).
2. Reasignar aleatoriamente las etiquetas entre días completos, conservando la cantidad de días de cada tipo, y recalcular TV. Repetir B veces (B ≥ 10.000; ver nota).
3. p-valor = (1 + número de permutaciones con TV ≥ TV_obs) / (B + 1). El +1 incluye la asignación observada entre las posibles y evita p-valores iguales a cero; el p-valor mínimo alcanzable es 1/(B + 1).

*Nota sobre B:* con corrección de Holm sobre 44 estaciones, el menor p-valor ajustado alcanzable es 44/(B + 1). Con B = 1.000 ese piso es 0,044, apenas por debajo de 0,05, y todos los rechazos aparecen con el mismo valor. Con B = 10.000 el piso baja a 0,0044.

Como se permutan días completos, la dependencia entre intervalos de un mismo día se conserva y deja de afectar la inferencia. El único supuesto es la **intercambiabilidad de los días** bajo H₀ꜰ: si el tipo de día no influyera en el perfil, cualquier día podría haber tenido cualquiera de las etiquetas. La permutación se hace dentro de cada combinación año-mes (permutación estratificada), de modo que sólo se intercambian etiquetas entre días comparables en estación del año y nivel de demanda.

Con 44 estaciones se corrige por comparaciones múltiples (Holm). La corrección de Holm es válida cualquiera sea la dependencia entre los tests de las distintas estaciones. Dado el tamaño muestral (~2.100 días por estación), se espera significancia en casi todas; **el resultado principal es el tamaño de efecto** (TV, ratio de retención con su IC), y el p-valor es un control complementario.

### Decisiones de procesamiento asociadas
- Los días-estación con ingreso total nulo se excluyen **tanto del análisis de volumen como del de forma** (ver *Decisiones tomadas*). En el de forma, además, su perfil no está definido.
- Los días con ingreso bajo pero no nulo (cierres parciales) se mantienen; su efecto se informa como análisis de sensibilidad.
- Las categorías de tipo de día son las que se adopten en DM-03.

### Evidencia preliminar (exploratoria)
Corresponde a la clasificación binaria actual, con permutación no estratificada y 1.000–2.000 permutaciones:

| Estación | TV | TV máximo en las permutaciones | Ventanas significativas |
|---|---|---|---|
| Constitución | 0,301 | 0,027 | 67 / 94 |
| Carlos Gardel | 0,133 | 0,025 | 32 / 90 |

### Impacto en el marco teórico
- La hipótesis se reformula como H₀ꜰ (forma del perfil intradiario); el volumen pasa a ser una magnitud estimada con su intervalo de confianza, no un contraste.
- El objeto de análisis se acota explícitamente al día típico para la diagramación de servicios regulares; los días excepcionales (eventos) quedan fuera del alcance.
- La demanda se define como **condicionada a la operación del servicio**; los días sin servicio (cierres) no forman parte de la población analizada.
- La unidad de análisis pasa del intervalo de 15 minutos al día-estación, y se discute explícitamente el supuesto de intercambiabilidad.
- El test K-S se **reemplaza** por la distancia de variación total, con inferencia por permutación en lugar de una distribución asintótica.
- Se incorporan la corrección por comparaciones múltiples y la primacía del tamaño de efecto sobre la significancia.

### Alternativas descartadas
- **K-S sobre perfiles acumulados:** subestima las diferencias cuando las curvas se cruzan (ver arriba).
- **Regresión log(ingresos) ~ tipo de día × franja horaria** con errores agrupados por día, y **ANOVA funcional:** son válidas, pero más complejas de presentar, sin ventaja clara para esta entrega.
- **Distancia de Wasserstein (W₁)** como estadístico complementario (minutos de desplazamiento medio de la demanda): agrega una segunda medida de forma sin cambiar la argumentación.
- **Test a nivel de red y corrección max-T (Westfall-Young):** sólo serían necesarios para una afirmación inferencial sobre la red en conjunto, que el trabajo no plantea (ver *Decisiones tomadas*).

### Decisiones tomadas
- **Volumen: sólo estimación** (2026-11-04). Se reporta el ratio de retención con su IC, sin contraste (ver *Volumen*).
- **Ponderación uniforme de los días en el perfil medio** (2026-11-04). Se descarta la ponderación por volumen (ver justificación en *Forma*, punto 2).
- **Exclusión de los días con ingreso nulo** (2026-11-04). Se mide la **demanda condicionada a la operación del servicio**: la diagramación se decide para los días en que la estación funciona.
  - *Evidencia de que los ceros son cierres y no ausencia de demanda:* hay 360 días-estación con ingreso nulo. El 66% cae en días no laborables (que son el 32% de todos los días), con 148 en domingos. Aparecen agrupados por línea en domingos consecutivos (p. ej. ~15 estaciones de la Línea B en noviembre-diciembre de 2014), patrón propio de cierres por obras. Ninguna fecha tiene la red completa en cero, por lo que no son fallas de registro.
  - *Sesgo que se evita:* incluirlos promedia la demanda con días sin servicio, concentrados en domingos, y **subestima** la demanda no laborable.
  - *Coherencia:* otros 1.271 días-estación no tienen ningún registro en los datos y ya quedaban excluidos de hecho. La exclusión de los ceros trata igual "sin datos" y "sin servicio", y coincide con el análisis de forma.
  - *Sensibilidad (clasificación binaria actual):* retención de red 27,86% incluyendo ceros, 28,03% excluyéndolos y 28,21% excluyendo además los 384 días con ingreso positivo menor al 10% de la mediana de la estación para su tipo de día. Por estación, el cambio máximo al excluir ceros es de +0,84 pp (Carlos Gardel: 62,22% → 63,05%). Los resultados se mueven menos de 0,4 pp a nivel de red, por lo que no dependen de este tratamiento. El umbral del 10% es arbitrario y sólo se usa como chequeo, no como criterio de exclusión.
- **Tamaño de los estratos de permutación: sin acción con tres categorías** (2026-11-04). Se había planteado que los estratos año-mes podían ser demasiado chicos; el conteo muestra que no lo son.
  - *Con tres categorías* (Hábil / Sábado / Domingo-Feriado), todo estrato año-mes contiene al menos 18 días hábiles, 3 sábados y 4 domingos o feriados, y ningún estrato carece de alguna categoría. Lo que limita un test de permutación es la cantidad de asignaciones posibles, no la de días: un estrato típico (21 hábiles + 4 sábados) admite 12.650 asignaciones distintas, y el conjunto de los 72 estratos, del orden de 10²⁹⁵. Las 10.000 permutaciones aleatorias se extraen de un espacio en la práctica ilimitado.
  - *Si los feriados se separan como cuarta categoría* (DM-03): hay ~1 feriado por mes y 9 estratos sin ninguno. Esos estratos no sesgan el test (simplemente no aportan a la comparación con feriados), pero la comparación queda con ~90 días. En ese caso se usarán estratos año-trimestre **sólo para las comparaciones que involucren feriados**, resignando algo de control estacional a cambio de estratos con suficientes días.
- **Dependencia entre estaciones: se resuelve en la presentación** (2026-11-04). Las 44 estaciones comparten el mismo calendario, por lo que un factor que afecte a ciertos días (paros, clima, eventos) incide en todas a la vez y sus resultados no son evidencias independientes. Esto no invalida ningún test: cada test por estación es válido por separado y la corrección de Holm lo es bajo cualquier dependencia. El problema sólo aparece al resumir: no se presentará el recuento "X de 44 estaciones difieren" como confirmaciones independientes, sino la **distribución de los tamaños de efecto** (TV) entre estaciones. No se plantea un test a nivel de red.

### Decisiones pendientes
Ninguna.

## DM-05 · De "presión de andén" a frecuencia mínima requerida
- **Estado:** Aceptada (2026-11-05), pendiente de implementar. Requiere relevar la capacidad de la flota actual de cada línea (ver *Datos necesarios*).
- **Tipo:** Cambio de métrica operativa y del Objetivo Específico 4

### Problema
La métrica actual compara los ingresos de cada estación por ventana de 15 minutos con un umbral único de 1.200 pasajeros. El umbral sólo se justifica en un comentario del código: frecuencias de 8 a 12 minutos en días no laborables, formaciones de cinco coches con 900–1.000 pasajeros "a capacidad de diseño" y 1,2–1,5 trenes por ventana **por sentido**. Tiene seis problemas:

| Problema | ¿Se resuelve con una fuente? |
|---|---|
| **1. Capacidad por formación sin fuente.** "Capacidad de diseño" admite densidades de pie muy distintas (confortable ≈ 4 pax/m², de aglomeración ≈ 6 o más), y el material rodante difiere entre líneas y cambió durante 2014–2019 | **Sí:** capacidad por línea según el material rodante publicado, con una densidad explícita |
| **2. Frecuencia supuesta.** Los 8–12 minutos se asumen para todas las líneas y horarios. El operador publica los cronogramas actuales, pero en 2014–2019 operaba Metrovías, con otros cronogramas | **Parcialmente:** los históricos podrían recuperarse de archivos web o informes de SBASE |
| **3. Sentidos.** Los ingresos de una estación intermedia abordan trenes en ambos sentidos, por lo que la capacidad ofrecida allí es del orden del doble de la de un sentido. En una **cabecera** todos abordan en un único sentido y la comparación es correcta | **Sí:** contando los sentidos servidos por cada estación |
| **4. Pasajeros a bordo.** En una estación intermedia el tren llega parcialmente ocupado; la capacidad libre es la capacidad menos la carga, que sin registros de egreso es **desconocida** | **No:** es una propiedad de los datos. Sólo en las cabeceras el tren parte vacío |
| **5. Combinaciones.** Quienes transbordan dentro del área paga no pasan por molinete, por lo que los ingresos subestiman los abordajes en estaciones de combinación | **No:** se declara como limitación |
| **6. Umbral único.** La capacidad por ventana depende de la línea, el tipo de día y la franja horaria | **Sí**, una vez resueltos los puntos 1 y 2 |

El problema 4 no es de fuentes: aun con capacidades y cronogramas exactos, en una estación intermedia la comparación sólo da una **cota inferior** de la ocupación.

### Decisión
Se invierte la pregunta. En lugar de comparar la demanda con una oferta que habría que suponer, se calcula la **frecuencia mínima requerida** para atender la demanda proyectada (opción C de las evaluadas).

Para cada línea *l*, tipo de día *d* y ventana *t* de la temporada proyectada:

$$f_{\text{req}}(l, d, t) = \max_{s \in l} \frac{k_s \cdot B(s, d, t)}{C_l \cdot \varphi}$$

donde:
- *B(s, d, t)* son los ingresos proyectados de la estación *s* en la ventana (modelo de DM-06);
- *C_l* es la capacidad por formación de la línea;
- *φ* es la ocupación objetivo;
- *k_s* = 1 en las **cabeceras** (todos los ingresos abordan en un sentido) y *k_s* = ½ en las **estaciones intermedias** (reparto parejo entre sentidos, el supuesto más favorable).

El resultado se expresa en trenes por ventana de 15 minutos o como intervalo máximo entre trenes (15 / *f*<sub>req</sub> minutos).

**Interpretación:**
- **En las cabeceras** (Plaza de Mayo y San Pedrito en la Línea A; Leandro N. Alem y Juan Manuel de Rosas en la B; Retiro y Constitución en la C) el tren parte vacío y la frecuencia requerida es **exacta**, salvo por los transbordos.
- **En las estaciones intermedias** es una **cota inferior**. La frecuencia real necesaria es mayor, porque el tren llega con pasajeros y porque el reparto entre sentidos no suele ser parejo. Si una estación intermedia ya exige una frecuencia alta, la exigencia real es al menos esa.
- La frecuencia se fija por línea, no por estación. La **estación determinante** es la que impone el máximo en cada línea, tipo de día y franja.

### Ventajas
- Se expresa en la variable de decisión del problema: la frecuencia, que la introducción del documento identifica como "la principal palanca operativa".
- **No requiere los cronogramas de 2014–2019,** sólo la capacidad de las formaciones, que es documentable.
- Se integra con el modelo de planificación (DM-06): la proyección de la próxima temporada da directamente la frecuencia mínima por línea, tipo de día y franja horaria.
- Hace explícita la limitación por ausencia de egresos, en lugar de ocultarla en un umbral.

### Alcance y papel de la capacidad (2026-11-05)
La métrica se aplica a las **proyecciones del modelo** para una temporada, no a la demanda histórica. Su propósito es dar un dominio de aplicación a las predicciones y sostener la importancia de ajustar el nivel de frecuencia; no es una auditoría de la oferta pasada. En consecuencia:
- **Capacidad de referencia: la flota actual** publicada por el operador, que es la que atendería una temporada proyectada. No se reconstruye la capacidad año por año de 2014–2019.
- **La categorización de estaciones no depende de la capacidad.** *C_l* y *φ* son constantes dentro de cada línea, por lo que la estación determinante (la de mayor demanda a absorber) es la misma cualquiera sea la capacidad. Lo mismo vale para las comparaciones entre tipos de día y franjas dentro de una línea: la frecuencia requerida es proporcional a la demanda.
- **La capacidad sólo fija la escala absoluta:** traduce "esta estación determina la frecuencia" en "requiere *N* trenes por ventana de 15 minutos" o "un tren cada *X* minutos". Los valores absolutos se presentan como ilustración del orden de magnitud, con la capacidad declarada como supuesto.

*Nota sobre la flota histórica:* entre 2014 y 2019 el servicio lo operaba Metrovías S.A., que en diciembre de 2021 pasó a denominarse Emova con el inicio de una nueva concesión. El material rodante es propiedad de la Ciudad, por lo que el cambio de operador no implica un cambio de flota. Durante el período, las tres líneas renovaron o combinaron flotas (Línea A: CITIC-CNR Serie 200, con flotas temporales Fiat-Materfer y Siemens-O&K; Línea B: Mitsubishi ex-Eidan 500, CAF 5000 y CAF 6000; Línea C: Nagoya 250/300/1200, Nagoya 5000 y, desde ~2018, CITIC-CNR Serie 200). Reconstruir una capacidad por línea y año sería necesario para comparar la demanda con la oferta histórica, lo que esta métrica no hace.

### Datos necesarios
- **Capacidad por coche de la flota actual de cada línea,** según el material rodante publicado por el operador o la Ciudad (*Material rodante – Buenos Aires Ciudad*, ya citado) o las fichas técnicas de los fabricantes. Si una línea opera hoy con flotas mixtas, se toma la **menor capacidad en servicio**: es la opción conservadora, porque da una frecuencia requerida mayor.
- **Coches por formación** de cada línea, para pasar de capacidad por coche a capacidad por formación (*C_l*).
- **Densidad de pie** con la que está definida la capacidad publicada. Si las fuentes usan densidades distintas o no la declaran, se recalcula a partir de la superficie del coche con una densidad común tomada de un estándar documentado (por ejemplo, los niveles de servicio del *Transit Capacity and Quality of Service Manual*; Ryus, 2013). Se vincula con la decisión pendiente sobre la ocupación objetivo.

### Categorización de estaciones (OE4)
Se basa en la frecuencia requerida, con reglas explícitas aplicadas por código:
- **Estaciones determinantes:** las que fijan la frecuencia de su línea en algún tipo de día y franja, con la proporción de ventanas en que lo hacen.
- **Exigencia relativa:** frecuencia requerida por la estación respecto de la de su línea, por tipo de día.
- El detalle de las categorías y sus cortes se define al implementar, de modo que tabla y figura se generen con las mismas reglas.

### Impacto en los objetivos
- **Objetivo Específico 4:** "Proponer una categorización de las estaciones según la frecuencia mínima requerida para atender la demanda proyectada, identificando las estaciones que determinan la frecuencia de cada línea por tipo de día y franja horaria, con el fin de orientar la optimización de la frecuencia de la línea completa."

### Impacto en el marco teórico
- **2.2.3.2 (presión del andén):** se reemplaza por "Frecuencia requerida y estación determinante": la relación entre demanda, capacidad por formación, ocupación objetivo y frecuencia, y el carácter de cota inferior en estaciones intermedias. La noción de presión de andén puede conservarse como motivación.
- **2.2.3.3 (frecuencia de despacho):** se conserva; pasa a ser el concepto central de la métrica.
- **2.2.2, punto 3 (ausencia de egresos):** se reformula. La métrica sustituta ya no es la presión de andén sino la frecuencia requerida, exacta en cabeceras y cota inferior en el resto.
- **Nueva referencia:** el estándar de densidad de pie y la fuente de capacidad del material rodante.

### Impacto en la metodología y los resultados
- **3.8:** la presión de andén se reemplaza por la frecuencia mínima requerida y la categorización por estación determinante.
- **Sección 4 (4.5.2):** la Fig. 4.10 pasa a mostrar la frecuencia requerida por línea, tipo de día y franja; la Tabla 4.8, la categorización.

### Decisiones pendientes
1. **Ocupación objetivo** (*φ*): definir si la capacidad se toma a una densidad confortable con *φ* = 1, o a la capacidad nominal con un factor de planificación (p. ej., 0,8).
2. **Contraste con los cronogramas publicados (opcional).** Comparar la frecuencia requerida con la programada actualmente por el operador, como ilustración de la brecha entre oferta y demanda proyectada. Las proyecciones se construyen con datos de 2014–2019 y los cronogramas son actuales; la comparación debe presentarse con esa salvedad.

## DM-06 · Reorientación del modelo predictivo hacia la planificación de cronogramas
- **Estado:** Aceptada (2026-11-04), pendiente de implementar. Afecta el trabajo de modelado de la rama `origin/model`.
- **Tipo:** Cambio de diseño del modelo y de los objetivos específicos 2 a 4

### Problema
El modelo actual (rama `origin/model`; sección 4.3 del documento) predice la demanda de los **próximos 15 minutos** a partir de los ingresos reales de la última hora (`lag_1` a `lag_4` y `media_movil_1h`, que concentran ~65% de la importancia de XGBoost). Es un modelo de pronóstico en tiempo real. El objetivo general, en cambio, es *apoyar el diseño de los cronogramas de servicio*, que se planifican con antelación, cuando esa información todavía no existe.

De ahí se siguen tres problemas:
1. **Los objetivos 3 y 4 resultan circulares.** Calcular el ratio de retención o la presión de andén "a partir de las predicciones" de 2019, con un modelo que recibe los ingresos reales de los 15 minutos previos, reproduce los valores observados de 2019 (42,12% predicho frente a 42,38% observado). Valida el modelo, pero no aporta información que no estuviera ya en los datos.
2. **El desempeño reportado no demuestra utilidad.** Un perfil histórico sin aprendizaje automático y sin rezagos recientes alcanza un desempeño equivalente al de la regresión lineal *con* rezagos del documento (ver *Evidencia*). La mayor parte del R² = 0,95 corresponde al patrón diario regular.
3. **El "desplazamiento de horas pico de más de 9 horas" es un artefacto.** El código busca el pico hábil entre las 06:00 y las 11:00 y el no laborable entre las 11:00 y las 22:00, lo que fuerza un desplazamiento grande.

Además, el modelo fue entrenado con los datos previos a la corrección de DM-01 (fechas con día y mes invertidos), por lo que todas sus variables y métricas por tipo de día están afectadas.

### Decisión
- El modelo se orienta a la **planificación de cronogramas**, con un **horizonte de una temporada**: el cronograma de una temporada se decide con la información disponible hasta su inicio.
- Se abandona el modelo de pronóstico en tiempo real (un paso y varios pasos adelante, estrategias recursiva y directa).

### Información admisible
- **Sí:** variables de calendario (tipo de día según DM-03, ventana de 15 min, mes, posición de los feriados), identidad y geolocalización de la estación, y todo lo observado **hasta el fin de la temporada anterior** (nivel reciente, perfiles de meses recientes, misma temporada del año previo).
- **No:** cualquier dato de la temporada que se planifica (rezagos de 15 min, de 1 hora, del día o de la semana anterior).

### Diseño de evaluación
- **Evaluación con origen móvil por temporada:** para cada temporada de 2019, el modelo se entrena sólo con datos anteriores a su inicio y predice esa temporada. Son cuatro evaluaciones fuera de muestra en lugar de una. Las temporadas de 2018 se usan de la misma forma para el ajuste de hiperparámetros.
- **Línea base obligatoria: perfil histórico.** Es el promedio de los ingresos por estación × tipo de día × ventana de 15 minutos sobre todos los datos anteriores al origen. Todo modelo de aprendizaje automático debe compararse contra esta línea base.
- **Métricas en dos niveles:**
  - *Por ventana:* MSE, RMSE y MAE, como en el marco teórico.
  - *Por perfil* (el nivel relevante para un cronograma): distancia de variación total entre el perfil predicho y el observado por estación y tipo de día (ver DM-04), y error en el ratio de retención por estación.

### Evidencia (exploratoria)
Datos corregidos (DM-01), tres tipos de día (DM-03), horario 05:00–23:45, días-estación con menos de 20 ingresos excluidos y ventanas faltantes como 0 (mismos criterios que la rama `origin/model`).

*Partición única (entrenamiento 2014–2018, prueba 2019):*

| Predicción para 2019 | RMSE | MAE | R² |
|---|---|---|---|
| Perfil histórico (estación × tipo de día × ventana) | 73,7 | 33,0 | 0,914 |
| Perfil histórico × factor mensual | 73,0 | 31,4 | 0,916 |
| *Documento: regresión lineal con rezagos de la última hora* | *72,8* | *32,8* | *0,916* |
| *Documento: XGBoost con rezagos de la última hora* | *56,0* | *22,3* | *0,950* |

*Origen móvil por trimestre de 2019:*

| Variante | RMSE | MAE |
|---|---|---|
| **A. Perfil histórico** (todos los datos previos) | **72,8** | 32,4 |
| B. Mismo trimestre de años previos | 73,3 | 31,6 |
| C. B ajustado al nivel del último trimestre | 73,8 | 32,7 |

- Los ajustes estacionales y de nivel construidos a mano no mejoran el perfil histórico simple; el ajuste de nivel empeora el error de retención de los sábados (3,7 pp frente a ~1,5 pp).
- A nivel de perfil, el perfil histórico reproduce 2019 con una TV mediana de 0,032 y un error medio de retención de ~1,5 pp (sábados) y ~0,8–1,0 pp (domingos y feriados).
- El error remanente (~73 RMSE por ventana) corresponde principalmente a la variabilidad entre días alrededor del perfil típico, no predecible con información disponible una temporada antes. Perder los rezagos recientes (RMSE 56 → ~73) no afecta el objetivo de planificación: esa diferencia es variación de corto plazo a la que un cronograma no puede responder.
- *Advertencia:* las cifras del documento provienen de los datos sin corregir y con valores atípicos acotados; la comparación es aproximada.

### Experimentos con aprendizaje automático (exploratorios, 2026-11-05)
Mismo esquema: origen móvil por trimestre de 2019 y mismos criterios de datos. Todas las variables se calculan **a la fecha de inicio de cada trimestre**, también para los trimestres de entrenamiento (cada uno recibe los perfiles y niveles que un planificador habría tenido al comenzar ese trimestre), para evitar fugas a través de los promedios. Para cada trimestre de prueba, el modelo se entrena con los trimestres anteriores hasta dos antes del origen y usa el inmediatamente anterior para la detención temprana. Configuración única, sin ajuste de hiperparámetros.

**Experimento 1: XGBoost directo sobre ingresos por ventana.**
- *Variables:* calendario (ventana, día de semana, tipo de día, mes, día del mes, feriado, puente, víspera y día posterior a feriado), estación, rezagos estacionales (misma ventana y día de semana 52 y 104 semanas antes), perfiles históricos (total, mismo trimestre de años previos, últimos 3 meses) y nivel reciente.
- *Resultado:* mejora el RMSE por ventana en ~10% respecto del perfil histórico, pero tiene un **sesgo de volumen** fuerte: sobreestima los domingos y feriados en 17% (hasta 29% en algunos trimestres). El ~90% de la importancia corresponde a los perfiles históricos; la detención temprana ocurre entre las iteraciones 29 y 70, señal de poca información más allá del perfil.

**Experimento 2: separación volumen × forma.** La predicción por ventana es el volumen diario predicho multiplicado por la forma (proporción del día en cada ventana).
- *Forma:* promedio de las proporciones diarias por estación × tipo de día × ventana, con igual peso por día (como en DM-04). Se comparan la historia completa y los últimos 12 meses.
- *Volumen diario por estación-día:*
  - **V0:** promedio histórico por estación × tipo de día.
  - **V1 (estacional ingenuo):** nivel de los últimos 3 meses × factor estacional del año previo (cociente entre ese trimestre del año anterior y los 3 meses que lo precedieron).
  - **V2 (XGBoost):** predice el **cociente respecto del nivel reciente**, para no tener que extrapolar la tendencia, con variables de calendario, feriados, factor estacional y volumen de 52 semanas antes.

*Resultados (2019, origen móvil por trimestre):*

| Modelo | RMSE | MAE | Sesgo de volumen | TV de forma (mediana) | Error ret. sábado | Error ret. dom-fer | Error de volumen medio |
|---|---|---|---|---|---|---|---|
| Perfil histórico | 72,8 | 32,4 | −5,3% | 0,030 | 3,8 pp | 1,2 pp | 10,3% |
| XGBoost directo | 65,8 | 28,5 | +6,0% | 0,027 | 2,2 pp | 3,5 pp | 16,4% |
| V1 × forma 12 meses (sin aprendizaje automático) | 69,3 | 28,6 | **+2,2%** | **0,018** | 1,2 pp | 0,6 pp | **3,6%** |
| **V2 × forma 12 meses** | **65,4** | **26,9** | +5,5% | **0,018** | **0,8 pp** | **0,6 pp** | 6,4% |

Las últimas cuatro columnas miden la calidad del perfil por estación × tipo de día, promediado en 2019. El error mediano del volumen diario por estación-día es 12,6% (perfil histórico), 8,5% (V1) y 7,2% (V2).

*Conclusiones:*
- **La separación resuelve el problema de nivel:** el error de volumen medio baja de 10–16% a 4–6%, y desaparecen los sesgos extremos por tipo de día.
- **La forma debe estimarse con datos recientes:** la de los últimos 12 meses (TV 0,018) supera a la de la historia completa (0,030–0,033). Los patrones horarios cambian lentamente entre años.
- **V2 × forma** es el mejor modelo en general: iguala o mejora al XGBoost directo por ventana y tiene los menores errores de retención. Su debilidad es una **sobreestimación sistemática de ~5,5%**, probablemente porque aprendió el crecimiento de 2015–2018 y lo proyectó sobre un 2019 que no creció.
- **V1 × forma**, sin aprendizaje automático, es el **mejor calibrado en volumen** y constituye una referencia difícil de superar.
- El aporte del aprendizaje automático se concentra en la variación entre días (feriados y calendario): el error mediano diario baja de 8,5% (V1) a 7,2% (V2).

*Reproducibilidad:* los scripts de estos experimentos no están versionados en el repositorio; las cifras deben regenerarse al implementar el modelo en el notebook.

### Estructura propuesta del modelo
**Predicción = volumen diario × forma intradiaria reciente.**
- **Forma:** perfil medio de proporciones diarias de los últimos 12 meses por estación × tipo de día.
- **Volumen:** V1 (estacional ingenuo) como referencia y V2 (XGBoost sobre el cociente respecto del nivel reciente) como aporte del aprendizaje automático.
- **Coherencia con el resto del trabajo:** es la misma separación de DM-04, de modo que el análisis y el modelo comparten un único marco. Además, cada componente responde a una decisión de diagramación: el volumen determina la cantidad de servicios por tipo de día, y la forma, su distribución horaria.
- **Expectativa de desempeño:** R² ≈ 0,93 por ventana, error de retención de ~0,6–0,8 pp y error de volumen medio de 4–6%.

### Impacto en los objetivos
- **Objetivo general:** sin cambios; la reorientación lo cumple con mayor fidelidad.
- **OE2:** se reformula como predecir la demanda esperada por estación × ventana × tipo de día **para una temporada futura**, comparando modelos supervisados contra el perfil histórico.
- **OE3 y OE4:** retención, perfiles y presión de andén se calculan sobre las proyecciones de temporadas no vistas por el modelo, y dejan de ser circulares.
- **Hipótesis:** sin cambios.

### Impacto en el marco teórico
- **2.4 / 2.4.1 (series temporales):** se eliminan el pronóstico de un paso y de varios pasos y las estrategias recursiva y directa. Se incorporan el horizonte de pronóstico orientado a la planificación, la línea base de perfil histórico y la evaluación con origen móvil.
- **2.3.2 (métricas):** se agregan las métricas a nivel de perfil (TV y error de retención), en conexión con DM-04.
- **2.1 (antecedentes):** se conservan, aclarando que Zimmo et al. (2023) y Carvajal et al. (2025) abordan pronóstico de corto plazo, a diferencia de este trabajo.
- **2.3 (aprendizaje automático en general):** sin cambios. En 2.3.3 conviene precisar que el gradient boosting se aplica al volumen diario relativo al nivel reciente, y explicar por qué los modelos de árboles no extrapolan tendencias.
- **Estructura del modelo:** se incorpora la descomposición de la demanda en volumen y forma, vinculada a la separación de DM-04.

### Impacto en la metodología y el código
- **Metodología:**
  - 3.5: se eliminan `lag_1` a `lag_4` y `media_movil_1h`; las variables se calculan a la fecha de inicio de cada temporada.
  - 3.6: se incorporan la línea base y la estructura volumen × forma.
  - 3.7: se adopta la evaluación con origen móvil por temporada.
  - 3.8: las métricas operativas se calculan sobre las proyecciones.
  - Se elimina el cálculo del desplazamiento de horas pico (ver DM-07).
- **Código (`origin/model`):**
  - *Reutilizable:* la preparación de datos (grilla regular de 76 ventanas por día, detección de cierres y variables geográficas).
  - *A eliminar o reescribir:* los rezagos recientes, los objetivos de varios pasos y el cálculo de picos con ventanas forzadas.
  - Debe integrarse al notebook único y reentrenarse con los datos corregidos, después de implementar DM-03 y DM-04.
- **Resultados y conclusiones:**
  - El R² por ventana bajará respecto del 0,95 actual; debe presentarse en relación con la línea base, no con el modelo de tiempo real.
  - Se elimina la recomendación de integrar el modelo en los centros de control en tiempo real.

### Decisiones pendientes
1. **Definición de temporada.** Se usaron trimestres calendario. El primer trimestre mezcla el valle estival de enero y febrero con la reactivación de marzo, y es donde más difieren las variantes. Idealmente, las temporadas deberían coincidir con los períodos en que el operador modifica sus cronogramas; si no se conocen, se usan trimestres o se separa el verano (enero–febrero) como período propio.
2. **Resultado si el aprendizaje automático no supera la línea base.** Los experimentos muestran una mejora modesta pero consistente (V2 sobre V1 en error diario y retención). Si al implementarlo la mejora no se confirma, se informará como hallazgo: con horizonte de una temporada, la estructura regular del calendario explica casi toda la demanda que un cronograma puede atender. El modelo V1 × forma es en sí un modelo estadístico válido.
3. **Sesgo de V2.** Diagnosticar y corregir la sobreestimación de ~5,5%. Opciones: entrenar sólo con años recientes, incorporar una variable de tendencia o combinar V2 con V1. Corregido el sesgo, V2 debería superar a V1 en todas las métricas; si no lo hace, se adopta V1.

## DM-07 · De "desplazamiento de las horas pico" a "distribución horaria de la demanda"
- **Estado:** Aceptada (2026-11-05), pendiente de incorporar al documento.
- **Tipo:** Reformulación del Objetivo Específico 3 y de la hipótesis

### Problema
El objetivo específico 3, la hipótesis y la descripción del tema (1.2) usan el "desplazamiento de las horas pico" como una de las dos dimensiones de la variación. El concepto presupone que existe un pico único que se traslada en el tiempo, y eso no se cumple en esta red:
- **Días hábiles:** dos picos (matutino y vespertino).
- **Sábados:** una meseta centrada en el mediodía.
- **Domingos y feriados:** un máximo al atardecer.

El perfil no laborable no es una versión desplazada de ninguno de los picos hábiles, sino una organización distinta de la demanda. Por eso el cálculo anterior necesitó forzar ventanas de búsqueda y produjo un desplazamiento de "más de 9 horas" (DM-06). La métrica está mal definida para estos datos, no sólo mal calculada.

Además, lo que el trabajo busca establecer es si la distribución de la demanda en días no laborables difiere de la de días hábiles, no si un pico particular se movió.

### Decisión
Se reemplaza el "desplazamiento de las horas pico" por la **distribución horaria de la demanda**, medida con los instrumentos de DM-04:
- **Magnitud de la diferencia:** distancia de variación total (TV) entre perfiles normalizados.
- **Localización:** curva de diferencias por ventana, que indica qué franjas concentran más o menos demanda en cada tipo de día (p. ej., en Constitución, exceso hábil entre las 07:00 y las 08:15 y exceso no laborable hacia las 19:00). Para la diagramación es más útil que un único número de horas, porque señala dónde reforzar o reducir el servicio.
- **Opcional:** los horarios de los máximos reales de cada tipo de día pueden informarse como dato descriptivo, sin calcular un desplazamiento ni someterlo a contraste.

### Propuestas de redacción
- **Objetivo Específico 3:** "Cuantificar el ratio de retención y la diferencia en la distribución horaria de la demanda entre tipos de día, a partir de las proyecciones del modelo para temporadas no observadas" (en conjunto con DM-06).
- **Hipótesis:** "La demanda de pasajeros en días no laborables en la red de subtes es estructuralmente no uniforme y presenta diferencias significativas estación por estación, tanto en el ratio de retención respecto de los días hábiles como en la distribución horaria de la demanda."
- **Descripción del tema (1.2):** reemplazar "el desplazamiento de las horas pico (la alteración cronológica de los momentos de mayor afluencia)" por "la distribución horaria de la demanda (cómo se reparte la afluencia a lo largo del día)".

### Impacto en el marco teórico y la metodología
- **2.2.3 (métricas de demanda):** se define la distribución horaria como el perfil normalizado (proporción de la demanda diaria en cada ventana), con la TV como medida de diferencia (DM-04). No se agrega una métrica de desplazamiento de picos.
- **3.8 (métricas operativas):** se elimina el desplazamiento de las horas pico; la comparación de perfiles proyectados se hace con TV y la curva de diferencias.
- **Sección 4:** se elimina la subsección propia del desplazamiento de picos; su contenido queda cubierto por el análisis de forma (ver `ESTRUCTURA_SECCION_4.md`).
