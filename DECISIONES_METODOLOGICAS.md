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
- **Estado:** Implementada (2026-11-04, commit `6a9b3bb`); el umbral sigue en revisión (ver DM-05)
- **Tipo:** Reinterpretación de un resultado
- **Cambio:** Con los datos corregidos, los 750 intervalos críticos ocurren todos en Constitución, el 92% entre las 07:00 y las 10:00 y casi todos en sábados. Se elimina la afirmación de saturación generalizada en nodos de transbordo durante fines de semana; el hallazgo se interpreta como persistencia del viaje laboral matutino de los sábados en la cabecera de la Línea C.
- **Impacto en el marco teórico:** La discusión no puede apoyarse en la idea de que la reducción de frecuencias de fin de semana satura los nodos de transbordo en general.

## DM-03 · Clasificación de tipos de día: Hábil / Sábado / Domingo-Feriado
- **Estado:** Aceptada (pendiente de implementar en el notebook). Hoy el notebook sólo incluye la desagregación descriptiva (sección 5.1); los análisis siguen usando la dicotomía Hábil / No Laborable.
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
- **Estado:** Propuesta
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

## DM-05 · Umbral de presión de andén
- **Estado:** Propuesta (pendiente de discusión)
- **Problema:** El umbral de 1.200 pax / 15 min compara los ingresos totales de la estación (ambos sentidos) con la capacidad de despacho estimada por sentido, y sus supuestos (frecuencia, capacidad por formación) no tienen fuente citada.
- **Impacto en el marco teórico:** A definir según la alternativa que se adopte.
