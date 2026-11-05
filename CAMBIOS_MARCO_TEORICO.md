# Cambios al Marco Teórico (Sección 2)

Guía para reescribir la Sección 2 del documento final a partir de las decisiones registradas en `DECISIONES_METODOLOGICAS.md` (DM-01 a DM-07). Indica, subsección por subsección, qué se conserva, qué cambia y qué se agrega, con referencias propuestas para cada concepto nuevo.

**Nivel de cambio:**
- **Ninguno:** se conserva tal cual.
- **Menor:** ajustes de una o dos oraciones.
- **Moderado:** se reescribe parte del contenido.
- **Mayor:** se reescribe o reemplaza la subsección completa.
- **Nueva:** subsección que no existe en la versión actual.
- **Pendiente:** depende de una decisión todavía abierta.

---

## Resumen

La base del marco teórico se conserva: antecedentes, sistema de subtes de Buenos Aires y fundamentos de aprendizaje automático (unas 7 de sus 12 páginas) sólo requieren ajustes menores. Los cambios se concentran en dos lugares:

- **2.4.1** (aprendizaje automático para series temporales): pasa del pronóstico de corto plazo a la planificación por temporada (DM-06).
- **2.5** (comparación de distribuciones): KDE y Kolmogorov-Smirnov se reemplazan por perfiles normalizados, distancia de variación total e inferencia por permutación (DM-04, DM-07).

A eso se suman unas 2–3 páginas de contenido nuevo. En conjunto, cerca de **un tercio** del marco teórico cambia en sustancia.

| Se elimina | Se agrega |
|---|---|
| Prueba de Kolmogorov-Smirnov | Tipos de día (Hábil / Sábado / Domingo-Feriado) |
| KDE de valores por intervalo | Perfil normalizado y distribución horaria |
| Pronóstico de un paso y de varios pasos (estrategias recursiva y directa) | Distancia de variación total (TV) |
| Regresión lineal como modelo de referencia | Test de permutación, *bootstrap*, comparaciones múltiples, tamaño de efecto |
| Presión de andén como métrica (umbral fijo) | Horizonte de pronóstico, evaluación con origen móvil, modelos de referencia, descomposición volumen × forma |
| | Frecuencia mínima requerida y estación determinante |

---

## Tabla de cambios por subsección

| Subsección actual | Cambio | Qué cambia | Fuente |
|---|---|---|---|
| **2 (introducción)** | Menor | El párrafo sobre "dos métodos para comparar distribuciones… de forma gráfica y analítica" describe el nuevo enfoque | DM-04 |
| **2.1.1 Zimmo et al. (2023)** | Menor | Aclarar que aborda pronóstico de corto plazo; sigue justificando la agregación en 15 minutos | DM-06 |
| **2.1.2 Zeb et al. (2025)** | Ninguno | Sigue respaldando el uso de variables de calendario como indicadores de régimen | — |
| **2.1.3 Carvajal et al. (2025)** | Menor | La misma aclaración que en 2.1.1 | DM-06 |
| **2.1.4 Vargas y Porras Roque (2023)** | Ninguno | — | — |
| **2.2.1 Historia** | Ninguno | Ya menciona que Emova distingue hábiles, sábados, domingos y feriados (respalda DM-03) | — |
| **2.2.2 Limitaciones** | Menor–moderado | El punto 1 afirma que las reducciones lineales generan "hacinamiento en andenes críticos"; los datos corregidos no lo muestran de forma generalizada. El punto 3 cambia su métrica sustituta: frecuencia requerida en lugar de presión de andén | DM-02, DM-05 |
| **2.2.3.1 Curvas de demanda** | Moderado | Agregar el **perfil normalizado** como definición de distribución horaria | DM-04, DM-07 |
| **2.2.3.2 Presión del andén** | Mayor (reemplazo) | Pasa a ser "Frecuencia requerida y estación determinante" | DM-05 |
| **2.2.3.3 Frecuencia de despacho** | Menor | Se conserva; pasa a ser el concepto central de la métrica operativa | DM-05 |
| **2.2.3.4 Flujo de pasajeros** | Menor | Agregar el volumen diario como agregado | DM-06 |
| **2.2.3.5 Ratio de retención** | Moderado | Redefinir sobre ingresos diarios medios por estación, condicionados a la operación del servicio, por tipo de día y con IC | DM-03, DM-04 |
| **Nueva: tipos de día** | Nueva | Tres categorías vinculadas a los cronogramas del operador y excepciones | DM-03 |
| **2.3 / 2.3.1 Aprendizaje automático, supervisado** | Ninguno | — (ver errores a corregir) | — |
| **2.3.2 Métricas de regresión** | Menor | Agregar las métricas a nivel de perfil y definir R² | DM-06 |
| **2.3.3 Gradient boosting** | Menor–moderado | Mencionar XGBoost, la no extrapolación de tendencias y la predicción del cociente al nivel reciente | DM-06 |
| **2.3.4 Regresión lineal** | Mayor (reemplazo) | Pasa a ser "Modelos de referencia": perfil histórico y estacional ingenuo | DM-06 |
| **2.4 Series temporales** | Menor | Explicitar la tendencia, causa del sesgo de nivel | DM-06 |
| **2.4.1 Aprendizaje automático para series temporales** | Mayor | Se reescribe para la planificación por temporada | DM-06 |
| **2.5 Comparación de distribuciones** | Moderado | Se reformula como comparación de perfiles de demanda, separando volumen y forma | DM-04 |
| **2.5.1 KDE** | Mayor | Se elimina o se reemplaza por el perfil normalizado | DM-04, DM-07 |
| **2.5.2 Kolmogorov-Smirnov** | Mayor | Se reemplaza por la distancia de variación total | DM-04 |
| **Nueva: inferencia** | Nueva | Permutación, *bootstrap*, comparaciones múltiples y tamaño de efecto | DM-04 |

---

## Estructura propuesta del capítulo

```text
2. Marco teórico
 2.1. Antecedentes                                   (se conserva; aclaraciones en 2.1.1 y 2.1.3)
 2.2. Subterráneos en la Ciudad Autónoma de Buenos Aires
      2.2.1. Historia                                (sin cambios)
      2.2.2. Limitaciones o problemáticas            (ajustes en puntos 1 y 3)
      2.2.3. Tipos de día y cronogramas de servicio  (NUEVA)
      2.2.4. Métricas de demanda de subtes           (ex 2.2.3)
             2.2.4.1. Curvas de demanda y distribución horaria
             2.2.4.2. Frecuencia requerida y estación determinante  (reemplaza a Presión del andén)
             2.2.4.3. Frecuencia de despacho
             2.2.4.4. Flujo de pasajeros y volumen diario
             2.2.4.5. Ratio de retención de demanda
 2.3. Machine Learning
      2.3.1. Aprendizaje supervisado para tareas de regresión
      2.3.2. Métricas de evaluación de regresión     (+ R² y métricas de perfil)
      2.3.3. Modelos de regresión: Gradient Boosting
      2.3.4. Modelos de referencia                   (reemplaza a Regresión lineal)
 2.4. Series temporales
      2.4.1. Pronóstico orientado a la planificación (reescrita)
 2.5. Comparación de perfiles de demanda             (reformulada)
      2.5.1. Perfil normalizado y distancia de variación total
      2.5.2. Inferencia por permutación
      2.5.3. Intervalos de confianza por bootstrap
      2.5.4. Comparaciones múltiples y tamaño de efecto
```

La subsección 2.2.3 de la versión actual pasa a ser 2.2.4 para dar lugar a los tipos de día. Si se prefiere no renumerar, los tipos de día pueden ir como 2.2.3.6.

---

## Detalle de los cambios

### 2 (introducción)
Reemplazar la última oración ("hacemos referencia a dos métodos para comparar distribuciones estadísticas… de forma gráfica y analítica") por una que anuncie la comparación de perfiles de demanda en sus dos dimensiones, volumen y distribución horaria, y la inferencia estadística utilizada.

### 2.1.1 y 2.1.3 (antecedentes)
Agregar una oración a cada uno: el estudio aborda el pronóstico de corto plazo (minutos a horas), mientras que este trabajo se orienta a la planificación con horizonte de una temporada. Lo que se toma de ellos se mantiene: agregación en 15 minutos y superioridad de los modelos no lineales (Zimmo); predicción sin datos de egreso y CRISP-DM (Carvajal).

### 2.2.2 (limitaciones)
- **Punto 1:** la afirmación de que las reducciones lineales de frecuencia provocan "hacinamiento en andenes críticos" se presenta como hecho. Con los datos corregidos, la presión de andén elevada en días no laborables se concentra en Constitución, los sábados por la mañana (DM-02). Conviene presentarla como problema a evaluar, o respaldarla con una fuente.
- **Punto 3:** se mantiene la limitación por ausencia de registros de egreso. La métrica sustituta deja de ser la presión de andén y pasa a ser la frecuencia mínima requerida, exacta en las cabeceras y cota inferior en las estaciones intermedias (DM-05).

### 2.2.3 (nueva): tipos de día y cronogramas de servicio
Contenido:
- El operador organiza el servicio con tres cronogramas: días hábiles, sábados, y domingos y feriados (Horarios del servicio – Emova, ya citado).
- Definición operativa de las tres categorías del trabajo: **Hábil**, **Sábado** y **Domingo-Feriado**.
- Excepciones:
  - **Jueves Santo** no coincidente con otro feriado: día no laborable optativo que el operador atiende con horario de sábado (*enelsubte.com*, 2024); se clasifica como Sábado.
  - **Feriados con fines turísticos** (puentes): se clasifican como Domingo-Feriado.
- La agrupación de domingos y feriados se valida con los datos en los resultados (Sección 4), no se asume.

*Fuentes:* Horarios del servicio – Emova (ya citada); "Cronograma de servicio de Subte para la Semana Santa", *enelsubte.com*, 27/03/2024 (nueva).

### 2.2.3.1 (curvas de demanda): agregar la distribución horaria
- Mantener la definición actual de curva de demanda.
- Agregar el **perfil normalizado**: proporción de los ingresos del día que ocurre en cada ventana de 15 minutos. Elimina el volumen y permite comparar *cuándo* ocurre la demanda entre tipos de día y estaciones de distinto tamaño.
- Definir la **distribución horaria de la demanda** como ese perfil. Es el concepto que reemplaza al "desplazamiento de las horas pico" (DM-07): una red con días hábiles bimodales, meseta de sábado y máximo dominical al atardecer no se describe bien como un pico que se traslada.

*Referencias:* Ceder (2019) y Boyce (2006), ya citadas, tratan los perfiles de carga como base de la diagramación.

### 2.2.3.2 (reemplazo): frecuencia requerida y estación determinante
Reemplaza a "Presión del andén" (DM-05). Contenido:
- **Relación entre demanda y oferta:** la frecuencia necesaria para atender una demanda depende de la capacidad por formación y de la ocupación objetivo. La frecuencia mínima requerida es el cociente entre los abordajes por ventana y la capacidad útil por tren (capacidad × ocupación objetivo).
- **Capacidad por formación:** se define a una densidad de pie explícita, tomada de un estándar (niveles de servicio del TCQSM; Ryus, 2013), con datos del material rodante de cada línea.
- **Cabeceras y estaciones intermedias:** en una cabecera el tren parte vacío y todos los ingresos abordan en un sentido, por lo que la frecuencia requerida es exacta. En una estación intermedia el tren llega con pasajeros, carga desconocida sin registros de egreso, y los ingresos se reparten entre sentidos; la frecuencia requerida es una cota inferior.
- **Estación determinante:** la frecuencia se fija por línea; la estación que impone la mayor frecuencia requerida en cada tipo de día y franja es la determinante.
- La noción de presión de andén puede conservarse como motivación (hacinamiento cuando la oferta no absorbe la demanda), sin usarse como métrica.

*Referencias:* Ryus (2013), ya citada, por los niveles de servicio y la densidad de pie (verificar que respalde el uso; el TCQSM trata el hacinamiento en andenes y la capacidad de los vehículos, no un indicador llamado "presión de andén"); Ceder (2019), ya citada, por la determinación de frecuencias a partir de perfiles de carga; *Material rodante – Buenos Aires Ciudad*, ya citada, por la capacidad de las formaciones.

### 2.2.3.4 (flujo de pasajeros)
Agregar que el flujo también se agrega a nivel diario (**volumen diario** por estación), que es la componente de nivel del modelo (DM-06).

### 2.2.3.5 (ratio de retención)
Precisar la definición:
- Numerador y denominador son **ingresos diarios medios por estación**, calculados sobre días con servicio (los cierres se excluyen; la demanda se mide condicionada a la operación del servicio).
- Se calcula para cada tipo de día no laborable (Sábado y Domingo-Feriado) respecto de Hábil.
- Se informa con un **intervalo de confianza** (ver 2.5.3), sin contraste de hipótesis: que la demanda no laborable sea menor no está en discusión; lo relevante es la magnitud.

### 2.3.2 (métricas de regresión)
- **Agregar R²** (coeficiente de determinación), que los resultados usan pero el marco no define.
- **Agregar métricas a nivel de perfil**, el nivel relevante para un cronograma:
  - distancia de variación total entre el perfil predicho y el observado (ver 2.5.1);
  - error en el ratio de retención y en el volumen diario medio por estación.
- Corregir los errores señalados más abajo.

*Referencias:* Hyndman y Athanasopoulos (2021), sección 5.8 (precisión de los pronósticos) y cap. 7 (R²).

### 2.3.3 (gradient boosting)
- Mencionar **XGBoost** como la implementación utilizada.
- Explicar que los modelos de árboles **no extrapolan**: sus predicciones quedan dentro del rango de valores vistos en el entrenamiento, por lo que no pueden proyectar una tendencia. Por eso el modelo de volumen predice el **cociente respecto del nivel reciente**, y no el volumen absoluto (DM-06).
- Corregir la descripción de la regularización (ver errores).

*Referencias:* Friedman (2001); Chen y Guestrin (2016); Hastie, Tibshirani y Friedman (2009), cap. 10.

### 2.3.4 (reemplazo): modelos de referencia
Reemplaza a "Regresión lineal". Contenido:
- Todo modelo predictivo debe compararse contra una referencia simple; si no la supera, su complejidad no se justifica.
- **Perfil histórico:** promedio de la demanda por estación × tipo de día × ventana sobre los datos disponibles.
- **Modelo estacional ingenuo:** proyecta el nivel reciente ajustado por el patrón estacional observado en el año previo.
- La regresión lineal puede mencionarse brevemente como alternativa no utilizada, o eliminarse.

*Referencia:* Hyndman y Athanasopoulos (2021), sección 5.2 (métodos de referencia, incluido el estacional ingenuo).

### 2.4 (series temporales)
Agregar la **tendencia** entre las propiedades de una serie (hoy se mencionan autocorrelación, estacionalidad y estacionariedad). Es relevante porque el cambio de nivel entre años es la principal fuente de error de los modelos (DM-06).

### 2.4.1 (reescrita): pronóstico orientado a la planificación
Se elimina el pronóstico de un paso y de varios pasos y las estrategias recursiva y directa (Bontempi, 2013, puede dejar de citarse). Contenido nuevo:
- **Horizonte de pronóstico:** el horizonte lo fija la decisión que el pronóstico informa. Un cronograma se planifica con antelación (una temporada), por lo que sólo puede usarse la información disponible antes de su inicio.
- **Información admisible y fuga de datos:** se conserva el argumento actual sobre la fuga de datos y se extiende: los rezagos de corto plazo (15 minutos, una hora, un día) no existen al momento de planificar. Se usan **rezagos estacionales** (misma ventana y día de semana un año antes) y **perfiles históricos calculados a la fecha de inicio de cada temporada**.
- **Evaluación con origen móvil:** se conserva la partición cronológica (*time-based splitting*) y se extiende: para cada temporada de prueba, el modelo se entrena sólo con los datos anteriores a su inicio. Simula el proceso real de planificación y da varias evaluaciones fuera de muestra en lugar de una.
- **Descomposición volumen × forma:** la demanda por ventana se modela como el producto del volumen diario y la proporción del día en cada ventana. La forma es estable y se estima con datos recientes; el volumen concentra la incertidumbre (tendencia, calendario).

*Referencias:* Hyndman y Athanasopoulos (2021), secciones 5.8–5.10 (evaluación y validación cruzada para series temporales); Tashman (2000); Talashuk y Radečić (2021), ya citada.

### 2.5 (reformulada): comparación de perfiles de demanda
Reformular la introducción: la comparación entre tipos de día se hace sobre dos dimensiones separadas, **volumen** (cuánta demanda se mantiene; ratio de retención) y **forma** (cómo se distribuye en el día; perfil normalizado). Una diferencia sólo de volumen no implica una diferencia de forma, y es la forma la que sostiene la afirmación central del trabajo: la demanda no laborable no es una versión escalada de la hábil.

### 2.5.1 (reemplaza a KDE): perfil normalizado y distancia de variación total
- Se elimina el KDE en su forma actual. La versión vigente afirma que permite observar "el desplazamiento temporal de las horas pico", pero el KDE aplicado a los valores por intervalo no contiene la hora del día. El perfil normalizado *es* una distribución sobre la hora del día y cumple esa función.
- **Distancia de variación total (TV)** entre dos perfiles p y q:
  - TV = ½ Σᵢ |pᵢ − qᵢ| = 1 − Σᵢ min(pᵢ, qᵢ).
  - Cada ventana se compara sólo con la misma ventana del otro perfil.
  - Interpretación: proporción de la demanda diaria **no compartida** entre ambos perfiles (0 = idénticos; 1 = sin superposición).
- **Relación con Kolmogorov-Smirnov** (justifica el reemplazo): el estadístico K-S aplicado a perfiles acumulados coincide con TV cuando un perfil está simplemente adelantado respecto del otro, pero la subestima cuando las curvas acumuladas se cruzan. En esta red eso ocurre en las estaciones centrales, donde la diferencia es una redistribución de la demanda y no un desplazamiento.
- **Curva de diferencias por ventana** (qᵢ − pᵢ): localiza en qué franjas difieren los perfiles.

*Referencias:* Gibbs y Su (2002), que definen TV, K-S y otras métricas entre distribuciones y sus relaciones; Levin y Peres (2017), cap. 4.

### 2.5.2 (nueva): inferencia por permutación
- **Idea:** bajo la hipótesis nula, la etiqueta de tipo de día no aporta información sobre el perfil; reasignar las etiquetas al azar genera la distribución del estadístico bajo H₀, sin supuestos sobre su forma.
- **Unidad de permutación:** el día completo. Los intervalos de un mismo día están correlacionados; permutar días completos conserva esa dependencia y la vuelve inocua.
- **Supuesto:** intercambiabilidad de los días bajo H₀. Se refuerza con **permutación estratificada** (sólo se intercambian etiquetas dentro de cada año-mes).
- **p-valor:** (1 + número de permutaciones con estadístico ≥ observado) / (B + 1), que nunca es cero.
- **Por qué no K-S asintótico:** sus p-valores suponen observaciones independientes, que los intervalos de 15 minutos no son.

*Referencias:* Good (2005); Phipson y Smyth (2010) para el cálculo del p-valor.

### 2.5.3 (nueva): intervalos de confianza por bootstrap
- Remuestreo con reposición de días completos para estimar la variabilidad del ratio de retención.
- Intervalo de confianza al 95% por percentiles.

*Referencia:* Efron y Tibshirani (1993).

### 2.5.4 (nueva): comparaciones múltiples y tamaño de efecto
- **Comparaciones múltiples:** al contrastar 44 estaciones, la probabilidad de algún falso positivo crece; la **corrección de Holm** la controla y es válida cualquiera sea la dependencia entre los tests.
- **Tamaño de efecto y significancia:** con miles de días por estación, diferencias pequeñas resultan significativas. El p-valor indica que una diferencia no es atribuible al azar, no que sea relevante; el resultado principal es el **tamaño de efecto** (TV, ratio de retención con su IC).
- **Dependencia entre estaciones:** las estaciones comparten el calendario, por lo que sus resultados no son evidencias independientes; un resumen de red se presenta como distribución de tamaños de efecto, no como recuento de rechazos.

*Referencias:* Holm (1979); Wasserstein y Lazar (2016); Sullivan y Feinn (2012).

---

## Errores a corregir (independientes de las decisiones)

1. **2.3.2.1 (MSE):** afirma que el error cuadrático medio "penaliza altamente incluso las diferencias pequeñas". Es al revés: al elevar al cuadrado, los errores pequeños se atenúan y los grandes se amplifican.
2. **2.3.2 (fórmulas):** las sumatorias van de *i* = 0 a *N*; deben ir de *i* = 1 a *N* (o de 0 a *N* − 1). En la fórmula del MAE falta el subíndice en la predicción (ȳᵢ).
3. **2.3.3 (gradient boosting):** el paso sobre regularización ("la combinación lineal de predictores débiles (con mayor residuo) tenga un coeficiente asociado menor") no describe el método. La regularización principal es la **tasa de aprendizaje** (*shrinkage*), que escala por igual la contribución de cada árbol nuevo; a eso se suman la profundidad máxima y el submuestreo.
4. **2.3 (introducción):** los ejemplos de aplicación (clasificación de textos, reconocimiento de entidades, síntesis de voz) no se relacionan con el trabajo; conviene reemplazarlos por aplicaciones en transporte.
5. **2.2.3.2:** verificar que Ryus (2013) respalde los conceptos para los que se cita (ver arriba).

---

## Pendiente

- **2.2.3.2 (frecuencia requerida):** falta relevar la capacidad por formación de cada línea y fijar la densidad de pie y la ocupación objetivo (DM-05, decisión pendiente 1).

---

## Referencias propuestas (nuevas)

Verificar edición y datos antes de incorporarlas en formato IEEE.

- Chen, T., y Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 785–794.
- Efron, B., y Tibshirani, R. J. (1993). *An Introduction to the Bootstrap*. Chapman & Hall.
- Friedman, J. H. (2001). Greedy function approximation: A gradient boosting machine. *The Annals of Statistics*, 29(5), 1189–1232.
- Gibbs, A. L., y Su, F. E. (2002). On choosing and bounding probability metrics. *International Statistical Review*, 70(3), 419–435.
- Good, P. (2005). *Permutation, Parametric, and Bootstrap Tests of Hypotheses* (3.ª ed.). Springer.
- Hastie, T., Tibshirani, R., y Friedman, J. (2009). *The Elements of Statistical Learning* (2.ª ed.). Springer.
- Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics*, 6(2), 65–70.
- Hyndman, R. J., y Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (3.ª ed.). OTexts. https://otexts.com/fpp3/
- Levin, D. A., y Peres, Y. (2017). *Markov Chains and Mixing Times* (2.ª ed.). American Mathematical Society.
- Phipson, B., y Smyth, G. K. (2010). Permutation P-values should never be zero. *Statistical Applications in Genetics and Molecular Biology*, 9(1).
- Sullivan, G. M., y Feinn, R. (2012). Using effect size—or why the P value is not enough. *Journal of Graduate Medical Education*, 4(3), 279–282.
- Tashman, L. J. (2000). Out-of-sample tests of forecasting accuracy: An analysis and review. *International Journal of Forecasting*, 16(4), 437–450.
- Wasserstein, R. L., y Lazar, N. A. (2016). The ASA statement on p-values: Context, process, and purpose. *The American Statistician*, 70(2), 129–133.
- *enelsubte.com* (2024, 27 de marzo). Cronograma de servicio de Subte para la Semana Santa. https://enelsubte.com/noticias/cronograma-de-servicio-de-subte-para-la-semana-santa-2/

**Referencias actuales que dejan de ser necesarias:** Conover (1999), si se elimina por completo la prueba K-S; Bontempi (2013), si se eliminan las estrategias de varios pasos; Silverman (2018), si se elimina el KDE.
