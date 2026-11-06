# Estructura de la Sección 4: Propuesta de solución

Esqueleto de la sección 4 del documento final, alineado con los objetivos (1.3), la hipótesis (1.4) y las decisiones metodológicas registradas en `DECISIONES_METODOLOGICAS.md`. Indica qué resultado va en cada subsección, de dónde sale y si ya está disponible.

**Estado de cada elemento:**
- ✅ Disponible en el notebook (puede requerir regenerarse).
- 🔧 Requiere implementar una decisión ya tomada (DM-03, DM-04 o DM-06).
- ⏳ Requiere datos o una decisión todavía abierta (capacidad por formación y ocupación objetivo, DM-05).

---

## Convenciones (normas de la cátedra y criterios propios)

- La sección abre con dos párrafos introductorios que **no** forman una subsección.
- Cada resultado se presenta en tres bloques: **Qué muestra** (descripción del dato, métrica o figura), **Cómo se interpreta** (lectura espacial, temporal u operativa) y **Qué aporta** (contribución a un objetivo o a la hipótesis).
- Las figuras llevan la descripción **debajo**; las tablas, el título **encima**. Toda figura y tabla se menciona en el texto antes de aparecer, como "Fig. 4.x" o "Tabla 4.x".
- Las figuras y tablas se ubican en el extremo superior o inferior de la página.
- **Toda cifra del texto sale de una salida del notebook.** No se escriben números a mano que el notebook no produzca.
- **Lenguaje proporcional a la evidencia.** Se informan tamaños de efecto con su incertidumbre. Se evitan expresiones como "contundencia matemática", "rigor incontrovertible" o "cumplimiento pleno".
- Los tipos de día son tres: **Hábil, Sábado y Domingo-Feriado** (DM-03).

---

## Párrafos introductorios (borrador)

> En esta sección se presentan los resultados de aplicar la metodología descrita en la Sección 3 a los registros de ingreso por molinete de las Líneas A, B y C del Subte de Buenos Aires entre 2014 y 2019: más de 70 millones de registros, consolidados en ventanas de 15 minutos para las 44 estaciones de la red. El análisis se organiza en torno a una distinción central: la variación de la demanda entre tipos de día tiene dos dimensiones, el **volumen** (cuánta demanda se mantiene) y la **forma** (cómo se distribuye a lo largo del día), y cada una responde a una decisión distinta de la diagramación del servicio: cuántas formaciones despachar y en qué franjas.
>
> Los resultados se presentan en el orden de los objetivos específicos. Primero se describe la calidad de los datos y se caracterizan las curvas de demanda (Objetivo Específico 1). Luego se cuantifican el volumen y la forma de la variación entre tipos de día y se contrasta la hipótesis de heterogeneidad (Objetivos Específicos 1 y 3). A continuación se evalúa el modelo predictivo, orientado a planificar el cronograma de una temporada con la información disponible antes de su inicio (Objetivo Específico 2). Por último, se derivan de sus proyecciones las métricas operativas y la categorización de estaciones (Objetivos Específicos 3 y 4).

---

## 4.1. Datos procesados y control de calidad

*Apoya a todos los objetivos. Es breve: el procedimiento está en la Sección 3; aquí sólo van sus resultados.*

| Elemento | Contenido | Fuente | Estado |
|---|---|---|---|
| **Tabla 4.1.** Cobertura de los datos | Registros brutos y filtrados por año; 44 estaciones; días-estación sin servicio excluidos (DM-04); distribución de días por tipo de día y excepciones (Jueves Santo, feriados puente) | Notebook 2.3–2.7; tabla `01_resumen_nulos_limpieza.md` | ✅ |
| Texto | Control de calendario (sección 2.5 del notebook) y corrección del parseo de fechas, en una o dos oraciones | DM-01 | ✅ |

**Qué aporta:** acredita que los resultados descansan sobre un calendario verificado y sobre una definición explícita de la población analizada (días con servicio).

---

## 4.2. Caracterización de las curvas de demanda (Objetivo Específico 1)

### 4.2.1. Perfiles horarios por tipo de día
| Elemento | Contenido | Fuente | Estado |
|---|---|---|---|
| **Fig. 4.1** | Perfil horario medio de la red para Hábil, Sábado y Domingo-Feriado | Notebook 4.1; `01_curva_demanda_dia_semana.png` | ✅ |

**Cómo se interpreta:** patrón bimodal de los días hábiles frente a la meseta del mediodía del sábado y el máximo al atardecer del domingo.

### 4.2.2. Perfiles por línea y en estaciones representativas
| Elemento | Contenido | Fuente | Estado |
|---|---|---|---|
| **Fig. 4.2** | Perfil por línea y tipo de día (3 paneles) | Notebook 4.3; `03_perfil_horario_por_linea.png` | ✅ |
| **Fig. 4.3** | Perfiles en estaciones representativas de cada grupo identificado en DM-04: origen residencial (p. ej. San Pedrito), central (p. ej. Florida), transbordo (p. ej. Constitución) y recreativa (Carlos Gardel) | Notebook 4.4; `04_comparativa_habil_nolab_estaciones_clave.png` | ✅ |

La selección de estaciones se justifica por los grupos observados en los datos, no a mano como hasta ahora.

### 4.2.3. Estacionalidad mensual
| Elemento | Contenido | Fuente | Estado |
|---|---|---|---|
| **Fig. 4.4** | Volumen diario medio por mes, por tipo de día | Notebook 4.2; `02_curva_demanda_estacional_mes.png` | ✅ |

**Qué aporta:** además de describir la estacionalidad, justifica que la planificación se haga por temporada (DM-06).

---

## 4.3. Variación entre tipos de día: volumen y distribución horaria (Objetivos Específicos 1 y 3; hipótesis)

### 4.3.1. Volumen: ratio de retención
| Elemento | Contenido | Fuente | Estado |
|---|---|---|---|
| **Tabla 4.2.** Retención por línea y tipo de día | Ingresos diarios medios y ratio de retención de Sábado y de Domingo-Feriado respecto de Hábil, con IC 95% por *bootstrap* | Notebook 5.1; `03_ratios_retencion_linea.md` | ✅ |
| **Fig. 4.5** | Retención por estación con IC (44 estaciones ordenadas; Sábado y Domingo-Feriado) | Notebook 5.3; `05_retencion_por_estacion_ic.png` | ✅ |

**Cómo se interpreta:** brecha territorial entre el Microcentro (retención de ~19% los sábados y de 9–12% los domingos y feriados) y los polos recreativos y de transbordo.

### 4.3.2. Distribución horaria: distancia entre perfiles
| Elemento | Contenido | Fuente | Estado |
|---|---|---|---|
| **Fig. 4.6** | Distancia de variación total (TV) por estación para Hábil–Sábado y Hábil–Domingo-Feriado, ordenada y coloreada por línea | Notebook 6.3; `07_tv_distribucion_horaria_por_estacion.png` | ✅ |
| **Fig. 4.7** | Curva de diferencias por ventana en las estaciones representativas, con banda simultánea | Notebook 6.3; `08_diferencias_por_ventana_estaciones_representativas.png` | ✅ |
| **Tabla 4.4** *(opcional)* | Horarios de los máximos reales por tipo de día, como dato descriptivo, sin cálculo de desplazamiento ni contraste (DM-07) | Nueva | Opcional, no implementada |

**Cómo se interpreta:** la Fig. 4.6 dimensiona cuánto difiere la distribución horaria; la Fig. 4.7 localiza en qué franjas, que es la información accionable para la diagramación (dónde reforzar o reducir el servicio). Se distinguen dos grupos de estaciones. En las de origen residencial la diferencia es un desplazamiento temporal (el día hábil empieza antes). En las centrales es una redistribución (pico vespertino de regreso frente a demanda al mediodía).

### 4.3.3. Contraste de la hipótesis
| Elemento | Contenido | Fuente | Estado |
|---|---|---|---|
| **Tabla 4.3.** Test de permutación por estación | Resumen por línea: rango de TV, p-valores ajustados por Holm. Incluye la comparación Domingo frente a Feriado que respalda la agrupación de DM-03 | Notebook 6.2; `05_distribucion_horaria_tv_permutacion.md` | ✅ |

**Qué aporta:** contrasta la hipótesis con el tamaño de efecto como resultado principal. El resumen de red se presenta como distribución de efectos, no como recuento de rechazos (DM-04).

---

## 4.4. Modelo predictivo para la planificación por temporada (Objetivo Específico 2)

### 4.4.1. Diseño de la evaluación
Texto breve, sin figura: horizonte de una temporada, información admisible, evaluación con origen móvil por temporada de 2019 y perfil histórico como línea base. Remite a la Sección 3 y a DM-06.

### 4.4.2. Desempeño comparado
| Elemento | Contenido | Fuente | Estado |
|---|---|---|---|
| **Tabla 4.5.** Desempeño por ventana | RMSE, MAE y R² por tipo de día: perfil histórico, V1 × forma, XGBoost directo y V2 × forma | Notebook 7.2; `07_modelo_desempeno_por_ventana.md` | ✅ |
| **Tabla 4.6.** Desempeño por perfil | TV entre perfil predicho y observado, error de retención y error de volumen medio por estación | Notebook 7.2; `08_modelo_desempeno_por_perfil.md` | ✅ |

**Qué aporta:** dimensiona la mejora real del aprendizaje automático frente a una referencia honesta. Se reporta aunque sea modesta (DM-06, decisión pendiente 2).

### 4.4.3. Análisis de errores
| Elemento | Contenido | Fuente | Estado |
|---|---|---|---|
| **Fig. 4.8** | Perfiles observados frente a proyectados (modelo adoptado) para una temporada de 2019, en las estaciones representativas | Notebook 7.3; `09_perfiles_observados_vs_proyectados.png` | ✅ |
| **Fig. 4.9** | Sesgo de volumen por temporada y tipo de día de cada modelo | Notebook 7.3; `10_sesgo_volumen_por_temporada.png` | ✅ |

**Cómo se interpreta:** la forma se proyecta con precisión una temporada antes; el nivel es la componente incierta.

---

## 4.5. Métricas operativas proyectadas y frecuencia requerida (Objetivos Específicos 3 y 4)

### 4.5.1. Retención y forma proyectadas
| Elemento | Contenido | Fuente | Estado |
|---|---|---|---|
| **Tabla 4.7.** Retención proyectada frente a observada por estación | Para las temporadas evaluadas de 2019, con el modelo adoptado (V1 × forma) | Notebook 7.3; `09_retencion_proyectada_vs_observada.md` | ✅ |

### 4.5.2. Frecuencia mínima requerida y categorización de estaciones
| Elemento | Contenido | Fuente | Estado |
|---|---|---|---|
| **Fig. 4.10** | Frecuencia mínima requerida (o intervalo máximo entre trenes) por línea, tipo de día y franja horaria, para la temporada proyectada; distinguiendo valores exactos (cabeceras) y cotas inferiores (estaciones intermedias) | Nueva | 🔧 DM-05 y DM-06 · ⏳ capacidad de la flota actual (sólo para la escala absoluta) |
| **Tabla 4.8.** Categorización de estaciones | Estaciones determinantes por línea, tipo de día y franja, con la proporción de ventanas en que fijan la frecuencia, y exigencia relativa respecto de su línea | Nueva | 🔧 DM-05 y DM-06 (no depende de la capacidad) |

**Qué aporta:** traduce la proyección de demanda en la variable de decisión del problema, la frecuencia por línea, e identifica qué estaciones la determinan. La categorización sale de reglas aplicadas por código, de modo que tabla y figura no puedan contradecirse como en la versión anterior (Tabla 4.7 frente a Fig. 4.9).

---

## 4.6. Correspondencia con objetivos e hipótesis

| Elemento | Contenido | Estado |
|---|---|---|
| **Tabla 4.9.** Síntesis | Para cada objetivo específico y para la hipótesis: resultado principal, evidencia (figura o tabla) y grado de cumplimiento, incluidas las limitaciones | Al final |

Sirve de puente con las Conclusiones (Sección 5) sin introducir elementos nuevos.

---

## Qué se elimina de la versión actual de la Sección 4

| Elemento actual | Motivo | Reemplazo |
|---|---|---|
| Todas las cifras (Tablas 4.1, 4.2, 4.6; texto) | Calculadas con fechas invertidas (DM-01) | Regenerar desde el notebook |
| Fig. 4.5 (KDE) y Tabla 4.3 (K-S) | El KDE de valores por intervalo no muestra la distribución horaria; el diseño del K-S no evalúa la hipótesis (DM-04) | 4.3.2 y 4.3.3 |
| Tablas 4.4 y 4.5 (horizontes de 15, 30 y 60 min) y Fig. 4.7 | Modelo de tiempo real, ajeno al objetivo (DM-06) | 4.4 |
| Desplazamiento de picos "de más de 9 horas" | Artefacto de ventanas forzadas (DM-06); el concepto se reemplaza por la distribución horaria (DM-07) | 4.3.2 |
| Fig. 4.8 y Tablas 4.6–4.7 de presión de andén | Datos con errores, umbral sin fundamento y categorización inconsistente con su figura (DM-02); la métrica se reemplaza por la frecuencia mínima requerida (DM-05) | 4.5.2 |
| Recomendación de uso en centros de control en tiempo real | Fuera del alcance (DM-06) | — |

---

## Orden de implementación sugerido

1. **DM-03** (tres tipos de día) en el notebook → habilita 4.1, 4.2 y la Tabla 4.2.
2. **DM-04** (retención con IC, TV y test de permutación) → habilita 4.3.1–4.3.3.
3. **DM-06** (modelo volumen × forma, integrando y reescribiendo `origin/model`) → habilita 4.4 y 4.5.1.
4. **DM-05** (frecuencia mínima requerida) → habilita la Tabla 4.8; la Fig. 4.10 requiere además la capacidad de la flota actual.
5. Redacción de 4.6 y de las Conclusiones.
