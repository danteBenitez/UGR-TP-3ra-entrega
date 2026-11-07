# Pendientes para la segunda pasada

Cambios detectados después de empezar la pasada de pulido. Las ubicaciones siguen la numeración del documento de cambios (Claude Doc).

## 0. Quedó sin aplicar en la primera pasada (Google Doc "Grupo 34", secciones 1 a 4)

Revisión del Google Doc al empezar la pasada de resultados.

**Correcciones menores:**

| Ubicación | Cambio |
| :--- | :--- |
| Título de la Sección 4 | "4. Propuesta de solución" → "4. Desarrollo de la solución" (nombre de la consigna) |
| 2.2.4.3, 2.2.4.4 y 2.2.4.5 | Renumerar como 2.2.4.2, 2.2.4.3 y 2.2.4.4 (falta la 2.2.4.2 desde que se eliminó "Presión del andén") |
| Título de 3.5 | Aplicar el estilo "Encabezado 3" (como 3.4 y 3.6); hoy es texto en negrita y no aparece en el índice |
| Título de 3.9 | "3.9. Fase 9: Herramientas y reproducibilidad." → "3.9. Herramientas y reproducibilidad" |
| 3.4, viñeta *Resultado principal* | Agregar al final "; el p-valor es un control complementario (Sección 2.5.4)", salvo que se haya quitado a propósito |
| Índice | Actualizarlo después de los cambios de títulos |

**Reemplazos de contenido pendientes** (el texto nuevo está en el documento de cambios, en la sección del mismo nombre):

- **2.3.4:** "Modelos de regresión: Regresión lineal" → "Modelos de referencia".
- **2.4.1:** "Modelos de *machine learning* para series temporales" → "Pronóstico orientado a la planificación". Antes de copiarlo, decidir si se usa la versión más abstracta propuesta (horizonte e información disponible, origen móvil, enfoque descendente), sin los detalles de nuestro caso, que ya están en 3.5 y 3.7. Versión abstracta:

  > **2.4.1 Horizonte de pronóstico e información disponible**
  >
  > El horizonte de un pronóstico (la antelación con que se lo produce respecto del período que proyecta) depende de la decisión que informa. Un pronóstico con origen en *t* sólo puede usar la información disponible en *t*; usar datos posteriores constituye una fuga de datos. Por eso el horizonte define qué variables son admisibles: un rezago menor que el horizonte no está disponible al pronosticar, mientras que las variables de calendario y los rezagos estacionales (el valor de un ciclo estacional antes) sí pueden estarlo (Hyndman y Athanasopoulos, 2021).
  >
  > La evaluación con **origen móvil** aplica el mismo principio: el modelo se reentrena en orígenes sucesivos, sólo con los datos anteriores a cada uno, y se evalúa en el período siguiente. Así se obtienen varias evaluaciones fuera de muestra en lugar de una (Tashman, 2000).
  >
  > Una serie desagregada también puede pronosticarse por partes: el total de cada período y la proporción que corresponde a cada subperíodo, cuyo producto reconstruye la serie (enfoque descendente o *top-down*; Hyndman y Athanasopoulos, 2021).

  Si se usa, agregar a 3.5 la oración que lo aplica a nuestro caso: un día como total y sus 96 ventanas como proporciones. Verificar la sección exacta de Hyndman y Athanasopoulos sobre el enfoque descendente.
- **2.5:** título "Comparación de distribuciones" → "Comparación de perfiles de demanda", y su introducción (hoy sigue la lista original de usos de la comparación de distribuciones). 2.5.1 a 2.5.4 ya están actualizadas.

## 1. Frecuencia requerida: alinear con el método de carga máxima de Ceder (2019)

**Fuente:** Ceder (2019), sección 3.2 *Max load (point check) methods*, ecuación 3.1:

F_j = P̄_mj / (γ_j · c)

| Ceder | Este trabajo | Diferencia |
| :--- | :--- | :--- |
| F_j: formaciones requeridas en el período *j* (usualmente una hora) | f_req por línea, tipo de día y hora | Ninguna; las franjas de una hora coinciden con su período habitual |
| c: capacidad del vehículo | C_l: capacidad por formación | Ninguna |
| γ_j: factor de carga | φ: ocupación objetivo (= 1 a 4 pax/m²) | Sólo el nombre |
| P̄_mj: carga máxima media **a bordo** en el punto de máxima carga del recorrido | Ingresos de la estación de mayor demanda | **Sustitución:** sin egresos no se conoce la carga a bordo |

**Consecuencia:** los ingresos de una estación nunca superan la carga máxima a bordo, por lo que nuestro resultado es una **cota inferior** de la frecuencia requerida, también en las cabeceras: allí los ingresos son la carga con que parte el tren, pero la carga máxima de la línea suele alcanzarse más adelante. La frase "exacto sólo en las cabeceras" sobreafirma.

### 1.1 Reemplazar el párrafo agregado en 2.2.4.2 (Frecuencia de despacho)

> La **frecuencia requerida** en un período *j* (usualmente una hora) es el cociente entre la carga máxima a bordo en ese período y la capacidad útil de cada formación, F_j = P_mj / (γ_j · c), donde *c* es la capacidad de la formación y γ_j el factor de carga objetivo (método de carga máxima; Ceder, 2019). Sin registros de egreso la carga a bordo es desconocida, por lo que este trabajo la sustituye por los ingresos de la estación de mayor demanda, que llamamos **estación determinante**. Como esos ingresos no superan la carga máxima, el resultado es una **cota inferior** de la frecuencia requerida. Cuando la oferta no absorbe la demanda se produce hacinamiento en andenes, lo que motiva el cálculo.

### 1.2 Quitar "exacto en las cabeceras" en el resto del documento

| Ubicación | Donde dice | Poner |
| :--- | :--- | :--- |
| 1.5, viñeta *Frecuencia requerida* | "el resultado es un indicador del orden de magnitud, exacto sólo en las cabeceras" | "el resultado es una cota inferior de la frecuencia requerida" |
| 2.2.2, punto 3 | "que es un indicador del orden de magnitud y sólo es exacta en las cabeceras de línea" | "que es una cota inferior de la frecuencia necesaria" |
| 3.8, viñeta *Frecuencia mínima requerida* | "es un indicador del orden de magnitud, exacto sólo en las cabeceras" | "es una cota inferior de la frecuencia requerida (Sección 2.2.4.2)" |
| 4.5.2, nota de la Tabla 4.7 | "¹ Cabecera de línea: la frecuencia requerida es exacta. En el resto es un indicador del orden de magnitud." | "¹ Cabecera de línea: los ingresos equivalen a la carga con que parte el tren. En todas las estaciones, la frecuencia requerida es una cota inferior." |

### 1.3 Notación (opcional, por coherencia con la fuente)

- En 3.8, la fórmula puede usar la notación de Ceder: F(l, d, j) = máx_{s ∈ l} B(s, d, j) / (γ · C_l), con γ = 1.
- En el párrafo de capacidad de 3.8, "la ocupación objetivo se fija en φ = 1" pasa a "el factor de carga se fija en γ = 1".
- Citar la sección: "(Ceder, 2019, sec. 3.2)".

### 1.4 En el repositorio (pendiente de aplicar)

- `notebook_eda_subte.ipynb`, sección 7.4: el texto de la limitación ("exacto sólo en las cabeceras") y el encabezado de la Tabla 10 ("En las cabeceras la frecuencia requerida es exacta"); fórmula con γ en lugar de φ.
- `DECISIONES_METODOLOGICAS.md`, DM-05: la oración de limitación y la referencia a Ceder (2019, sec. 3.2) como origen de la fórmula.

## 2. Estructura del informe final: seguir exactamente la consigna

La consigna del informe final pide siete partes y la plantilla tiene seis secciones numeradas. Se adopta la numeración de la consigna:

| N.º | Sección (consigna) | Contenido actual en el documento de cambios |
| :--- | :--- | :--- |
| 1 | Introducción, problema y objetivos | Sección 1 (sin cambios de numeración) |
| 2 | Marco teórico | Sección 2 |
| 3 | Metodología | Sección 3 |
| 4 | **Desarrollo de la solución** | **Nueva: falta redactarla** (ver abajo) |
| 5 | Resultados obtenidos y su análisis | Actual Sección 4 "Propuesta de solución", con su introducción de dos párrafos |
| 6 | Conclusiones | Actual Sección 5 |
| 7 | Bibliografía | Actual Sección 6 "Referencias" |
| 8 | Anexos | Actual Sección 7 (A1 pasa a ser la estructura del repositorio o el diagrama de flujo; no hay clases) |
| 9 | Soporte digital | Actual Sección 8 |

### 2.1 Renumeración en el texto

- **Figuras y tablas de resultados:** Fig. 4.1–4.10 → Fig. 5.1–5.10; Tabla 4.1–4.8 → Tabla 5.1–5.8 (también las menciones dentro del texto: "Tablas 4.4 y 4.5", "Fig. 4.5 a 4.7", la Tabla 5.8 de síntesis por objetivo, etc.).
- **Subsecciones de resultados:** 4.1–4.6 → 5.1–5.6 (4.3.1 → 5.3.1, 4.5.2 → 5.5.2, etc.).
- **Referencias cruzadas a la Sección 4:** en 2.2.3 ("se contrasta con los datos en la Sección 4") y en 3.4/3.8 si las hubiera → Sección 5. Las referencias de los resultados a la Sección 3 (p. ej., "Sección 3.7") no cambian.
- **Pendientes de este archivo:** la nota de la Tabla 4.7 (punto 1.2) pasa a ser de la Tabla 5.7, y 4.5.2 pasa a 5.5.2.

### 2.2 Sección 4 nueva: Desarrollo de la solución

**Redactada en el documento de cambios (Claude Doc), "Sección 4: Desarrollo de la solución":** introducción, 4.1 a 4.4, Tabla 4.1, Fig. 4.1 y 4.3 (diagramas) y la lista de capturas a tomar (Fig. 4.2, 4.4, 4.5 y 4.6). Lo que sigue es el esquema original, como referencia.

**Capturas del notebook: se agregan en la segunda pasada.** En la primera pasada se pegan sólo los dos diagramas. Al agregar las capturas, renumerar las figuras de la Sección 4 por orden de aparición. Con la ubicación prevista en la tabla de capturas del documento de cambios, el orden final es: 4.1 arquitectura, 4.2 índice del notebook, 4.3 modelo de planificación, 4.4 celda de la sección 7.4, 4.5 caché, 4.6 control de calendario. Si en la primera pasada los diagramas quedan como Fig. 4.1 y 4.2, el del modelo pasa a 4.3 (y su mención en el texto de 4.3). Si alguna captura cambia de lugar o se descarta, recalcular el orden.

La metodología (3) explica qué se decidió y por qué; esta sección describe lo construido y cómo funciona, con esquemas y capturas, sin repetir la justificación. La consigna de la plantilla para la sección 4 (introducción de dos párrafos sin título de subsección) se aplica aquí.

- **4.1 Arquitectura:** diagrama de flujo: CSV anuales → ingesta y normalización → calendario y controles de calidad → caché Parquet → (a) retención y comparación de perfiles, (b) modelo de planificación, (c) métricas operativas → tablas y figuras.
- **4.2 Componentes:** un párrafo por bloque, con la sección del notebook que lo implementa y lo que produce.
- **4.3 El modelo de planificación como herramienta:** diagrama: fecha de planificación → variables a esa fecha → nivel reciente × factor estacional del año previo → forma reciente → perfil proyectado → frecuencia requerida; cómo se usa para una temporada nueva. La justificación de V1 queda en 3.6 y la comparación de modelos en 5.4.
- **4.4 Decisiones de implementación:** notebook único que regenera todo, caché Parquet con `FORCE_REPROCESS`, dependencias fijadas con uv, controles incorporados (parseo de fechas por archivo, control de calendario).
- **Capturas:** estructura de secciones del notebook y una tabla de salida (p. ej., estaciones determinantes).

### 2.3 Bibliografía: APA

La consigna pide "preferentemente normas APA"; la plantilla pedía IEEE. Las referencias actuales ya siguen un estilo autor-año cercano a APA. Confirmar con la cátedra cuál rige; si es APA, la conversión a IEEE deja de ser necesaria y alcanza con uniformar el formato APA.

## 3. Marco teórico: quitar metodología de la Sección 2.5

2.5.2, 2.5.3 y 2.5.4 ya se reescribieron en términos generales en el documento de cambios, y sus decisiones pasaron a 3.4 (viñeta *Contraste* y nueva viñeta *Resultado principal*). Queda un recorte menor:

| Ubicación | Donde dice | Poner | Motivo |
| :--- | :--- | :--- | :--- |
| 2.5.1, segundo párrafo | "Eso ocurre cuando la demanda se redistribuye a lo largo del día, como en las estaciones céntricas." | "Eso ocurre cuando la demanda se redistribuye a lo largo del día." | "Las estaciones céntricas" es un resultado (Sección 5) |

## 4. Marco teórico: explicaciones poco precisas

Criterio: cada método del marco teórico debe explicar **en qué consiste** (el procedimiento, no sólo su nombre y su propósito) y **qué supuestos necesita** para ser válido. Revisión de la Sección 2 completa (documento de cambios más el texto original que se conserva), por prioridad:

### 4.1 Graves: no describen el método ni sus supuestos

- **2.5.3 Bootstrap.** Hoy es un párrafo que nombra el remuestreo "con reposición" sin explicarlo. Falta:
  - *Qué es remuestrear con reposición:* de una muestra de *n* observaciones se extraen al azar *n* observaciones, devolviendo cada una antes de la siguiente extracción; así una misma observación puede aparecer varias veces en el remuestreo y otras no aparecer.
  - *La idea central (principio de sustitución):* la distribución de la muestra hace de distribución de la población; recalcular el estadístico en muchos remuestreos imita cómo variaría si se repitiera el muestreo.
  - *El procedimiento:* repetir *B* veces (remuestrear, recalcular) y tomar los percentiles 2,5 y 97,5 de los *B* valores (intervalo por percentiles); qué aporta un *B* grande.
  - *Supuestos:* observaciones independientes e idénticamente distribuidas, y una muestra representativa; con observaciones dependientes, la unidad que se remuestrea es el bloque (*bootstrap* por bloques), y el supuesto pasa a ser la independencia entre bloques. El intervalo por percentiles supone además que la distribución del estadístico no está muy sesgada.
- **2.5.4 Comparaciones múltiples.** La corrección de Holm se nombra pero no se describe. Falta:
  - *Qué controla:* la tasa de error por familia (probabilidad de al menos un falso positivo entre las *m* pruebas).
  - *El procedimiento, con fórmula:* ordenar los *m* p-valores de menor a mayor, p₍₁₎ ≤ p₍₂₎ ≤ … ≤ p₍ₘ₎, y rechazar las hipótesis H₍₁₎, …, H₍ₖ₋₁₎, donde *k* es el primer índice que no cumple

    ```latex
    p_{(k)} \leq \frac{\alpha}{m - k + 1}
    ```

    Es decir, el menor p-valor se compara con α/*m* (como en Bonferroni), el siguiente con α/(*m* − 1), y así hasta el primero que no cumple. Forma equivalente, que es la que reporta el notebook (Tabla 5.3, "p ajustado"):

    ```latex
    \tilde{p}_{(k)} = \max_{j \leq k} \; \min\{1, \, (m - j + 1)\, p_{(j)}\}
    ```

    y se rechaza cada hipótesis con p̃ ≤ α. El máximo hace que los p-valores ajustados respeten el orden de los originales.
  - *Por qué Holm y no Bonferroni:* controla la misma tasa y nunca rechaza menos.
  - *Supuestos:* ninguno sobre la dependencia entre pruebas (ya se dice); conviene explicar por qué no lo necesita.
  - *Tamaño de efecto:* se usa el término sin definirlo (la magnitud de la diferencia, en unidades interpretables, independiente del tamaño de la muestra).

### 4.2 Importantes: imprecisos o incorrectos

- **2.3.4 Modelos de referencia.** Lo que se llama "modelo estacional ingenuo" no es el estacional ingenuo estándar (que repite el valor de un ciclo atrás, ŷ_{t+h} = y_{t+h−m}; Hyndman y Athanasopoulos, 2021), sino una variante que ajusta el nivel reciente por un factor estacional. Definir ambos con fórmula, nombrar nuestra variante como tal y explicar por qué una referencia simple es exigente en series con estacionalidad marcada.
- **2.4 Series temporales, estacionariedad (texto original).** "Una serie estacionaria es aquella que tiene media y varianza estáticas, de modo que los datos pueden fluctuar con la estacionalidad" es incorrecto: una serie con estacionalidad no es estacionaria. Definición: media y varianza constantes y autocovarianza que depende sólo del rezago.
- **2.3.3 Gradient boosting (texto original + corrección).** Falta el núcleo: cada árbol nuevo se ajusta al gradiente negativo de la función de pérdida evaluado en la predicción actual (con error cuadrático, los residuos), y el modelo final es la suma de los árboles escalados por la tasa de aprendizaje. "Funcional de riesgo" aparece sin definir. Para XGBoost, mencionar que agrega una penalización por la complejidad de los árboles.

### 4.3 Menores

- **2.5.2 Permutación.** Definir intercambiabilidad (la distribución conjunta no cambia al permutar las etiquetas) y aclarar que con *B* permutaciones aleatorias el p-valor es una aproximación de Monte Carlo al que daría el conjunto de todas las permutaciones; "al menos tan extremo" significa, para *TV*, "al menos tan grande".
- **2.3.2.4 R².** Aclarar que puede ser negativo cuando el modelo es peor que predecir la media.
- **2.4, autocorrelación (texto original).** "Valores altos producen valores altos" sugiere causalidad; mejor "tienden a seguir a".

Sin problemas de este tipo: 2.2.4.1 (perfil normalizado), 2.2.4.4 (retención), 2.3.1, 2.3.2.1 a 2.3.2.3, 2.5.1 (TV). La 2.2.4.2 (frecuencia requerida) ya tiene su cambio en el punto 1, y la 2.4.1 tiene pendiente la versión más abstracta.

## 5. Quitar el relato del registro de decisiones

El documento final no debe contener frases que sólo se entienden con el registro de decisiones (cuándo se fijó un criterio, nombres internos de opciones). Ya están corregidas en el documento de cambios; aplicar en el documento final:

| Ubicación | Donde dice | Poner |
| :--- | :--- | :--- |
| 3.6, último párrafo | "…sobre los cuatro trimestres de 2018. La opción de años de entrenamiento es el tratamiento común del nivel para ambos." | "…sobre los cuatro trimestres de 2018." |
| 3.7, segundo párrafo | "…y el error en el volumen medio. El criterio de adopción se fijó antes de la evaluación final: el modelo con aprendizaje automático se adopta si supera al estacional ingenuo en todas las métricas; si no, se adopta este último." | "…y el error en el volumen medio." |
| 5.4 (antes 4.4), *Qué aporta* | "Conforme al criterio fijado antes de la evaluación, como V2 no supera a V1 en todas las métricas, se adopta **V1 × forma**." | "Como V2 × forma no supera a V1 × forma en todas las métricas y está peor calibrado en volumen, se adopta **V1 × forma**." |
| 6 (antes 5), Conclusiones, punto 2 | "…pero sobreestima el nivel de 2019; según el criterio fijado antes de la evaluación, se adoptó el modelo estacional, mejor calibrado en volumen." | "…pero sobreestima el nivel de 2019; se adoptó el modelo estacional, mejor calibrado en volumen y más simple." |

**A decidir:** 3.9 termina con "Las decisiones metodológicas y su justificación se documentan en un registro de decisiones dentro del mismo repositorio, como parte de la trazabilidad del trabajo." Sólo remite al registro, no depende de su contenido; puede quedar o quitarse.

## 6. Otros pendientes ya conocidos

- **3.2 (Fases 1 y 2):** puede reducirse a cambios de palabras sobre el texto original (unidades de análisis, tres tipos de día, quitar la información geolocalizada) en lugar de reemplazar los dos párrafos.
- **Referencias:** uniformar el formato según la norma que confirme la cátedra (punto 2.3).
- **Objetivos específicos 2–4:** acordar la nueva redacción con el equipo.
- **Borrador Word (`documento/Grupo34_borrador.docx`):** quedó desactualizado respecto del documento de cambios (Fig. 4.10, Tabla 4.7, Tabla 3 de capacidades, referencias de capacidad, cambios de la revisión de redacción).
