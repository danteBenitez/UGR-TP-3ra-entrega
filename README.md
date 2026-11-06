# Variación de la Demanda en el Subte de CABA (Líneas A, B y C)
### Preprocesamiento Masivo, Análisis Exploratorio de Datos (EDA) y Validación Estadística (2014–2019)

Este repositorio contiene el pipeline analítico y el código fuente para el estudio empírico de la demanda de pasajeros en la Red de Subterráneos de la Ciudad Autónoma de Buenos Aires (Líneas A, B y C), evaluando la heterogeneidad entre **días hábiles y no laborables** (sábados, domingos y feriados nacionales).

---

## 📊 Principales Hallazgos y Resultados

1. **Volumen Procesado:** Más de 70 millones de registros de molinete (41 millones correspondientes a las Líneas A, B y C), consolidados en **44 estaciones** oficiales en intervalos de 15 minutos y agregados diarios.
2. **Tres tipos de día:** el análisis distingue días **hábiles**, **sábados** y **domingos y feriados**, en coincidencia con los cronogramas del operador (ver `DECISIONES_METODOLOGICAS.md`, DM-03).
3. **Distribución horaria:** la distancia de variación total entre los perfiles normalizados de días hábiles y no laborables tiene una mediana de **0,169** para los sábados (0,085–0,313) y de **0,186** para los domingos y feriados (0,075–0,413), con diferencias significativas en las 44 estaciones (test de permutación sobre días completos, corrección de Holm). Las mayores diferencias se dan en cabeceras residenciales y de transbordo; domingos y feriados tienen distribuciones muy similares entre sí (TV mediana 0,049).
4. **Ratio de Retención** (días con servicio, IC 95% por bootstrap): la red retiene el **38,59%** (37,47–39,72) de la demanda hábil los sábados y el **19,80%** (19,20–20,37) los domingos y feriados.
   - *Mayor Retención (Polos recreativos / transbordo):* **Carlos Gardel** (72,19% los sábados; 55,53% los domingos y feriados), **Alberti** y **Plaza Miserere** los sábados (54,10% y 53,00%), **Independencia** y **Retiro** los domingos y feriados (31,58% y 28,02%).
   - *Mayor Contracción (Distrito financiero / administrativo):* **Plaza de Mayo** y **Diagonal Norte** los sábados (18,47% y 18,76%); **Diagonal Norte** y **Florida** los domingos y feriados (9,18% y 9,22%).
5. **Presión de Andén:** Con un umbral supuesto de 1.200 pax / 15 min, los 750 intervalos críticos en días no laborables ocurren todos en **Constitución**, el 92% entre las 07:00 y las 10:00 y casi todos en sábados (727; 23 en domingos y feriados), con tendencia creciente en el período. Esta métrica será reemplazada por la frecuencia mínima requerida (DM-05).
6. **Modelo de planificación por temporada:** proyectando cada trimestre de 2019 con los datos anteriores a su inicio, el modelo estacional **V1 × forma** (volumen diario × distribución horaria) reproduce la retención por estación con un error medio de 1,2 pp (sábados) y 0,7 pp (domingos y feriados) y el volumen medio con un error de 3,8%. Los modelos XGBoost mejoran la precisión por ventana pero sobreestiman el nivel de 2019; se adopta V1 × forma según el criterio fijado antes de la evaluación (DM-06).

---

## 📁 Estructura del Repositorio

```text
EDA/
├── data_processed/                     # Datasets procesados de alta eficiencia (formato Parquet)
│   ├── subte_consolidado_15min.parquet # Demanda cada 15 min por estación (11.3 MB)
│   └── subte_diario_estaciones.parquet # Demanda diaria consolidada (356 KB)
├── output/
│   ├── graficos/                       # Figuras analíticas en alta resolución (PNG 300 DPI)
│   │   ├── 01_curva_demanda_dia_semana.png
│   │   ├── 02_curva_demanda_estacional_mes.png
│   │   ├── 03_perfil_horario_por_linea.png
│   │   ├── 04_comparativa_habil_nolab_estaciones_clave.png
│   │   ├── 05_retencion_por_estacion_ic.png
│   │   ├── 06_presion_anden_ventanas_criticas.png
│   │   ├── 07_tv_distribucion_horaria_por_estacion.png
│   │   ├── 08_diferencias_por_ventana_estaciones_representativas.png
│   │   ├── 09_perfiles_observados_vs_proyectados.png
│   │   └── 10_sesgo_volumen_por_temporada.png
│   ├── tablas/                         # Tablas tabuladas en Markdown
│   │   ├── 01_resumen_nulos_limpieza.md
│   │   ├── 02_estadisticas_descriptivas.md
│   │   ├── 03_ratios_retencion_linea.md
│   │   ├── 04_ratios_retencion_top_bottom_estaciones.md
│   │   ├── 05_distribucion_horaria_tv_permutacion.md
│   │   ├── 06_presion_anden_analisis.md
│   │   ├── 07_modelo_desempeno_por_ventana.md
│   │   ├── 08_modelo_desempeno_por_perfil.md
│   │   └── 09_retencion_proyectada_vs_observada.md
│   └── resumen_metodologia.md          # Síntesis interpretativa para la sección escrita
├── notebook_eda_subte.ipynb            # Pipeline completo: ingesta → EDA → validación → exportación de tablas y gráficos
├── pyproject.toml / uv.lock            # Dependencias del proyecto (gestionadas con uv)
├── PLAN.md                             # Consigna del análisis
├── DECISIONES_METODOLOGICAS.md         # Registro de cambios de método y su impacto en el marco teórico
├── CAMBIOS_MARCO_TEORICO.md            # Guía de cambios a la Sección 2 (Marco teórico) según las decisiones
├── CAMBIOS_METODOLOGIA.md              # Guía de cambios a la Sección 3 (Metodología) según las decisiones
├── ESTRUCTURA_SECCION_4.md             # Esqueleto de la Sección 4 (Propuesta de solución) del documento final
├── experimentos/                       # Scripts exploratorios que respaldan DM-06 (modelo por temporada)
└── .gitignore                          # Exclusión de datos crudos (6.7 GB) y temporales
```

---

## 🚀 Instalación y Puesta en Marcha

### 1. Clonar el Repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd EDA
```

### 2. Instalar Dependencias
El proyecto usa [uv](https://docs.astral.sh/uv/) y requiere Python 3.14 o superior:
```bash
uv sync
```

### 3. Ejecutar el Análisis
Todo el pipeline vive en un único notebook, `notebook_eda_subte.ipynb`. Ejecutado de principio a fin, regenera las tablas (`output/tablas/`) y los gráficos (`output/graficos/`).

Los datasets procesados (`data_processed/`) ya se encuentran incluidos en el repositorio (ocupan solo 11.6 MB en conjunto), por lo que **no es necesario descargar los 6.7 GB de CSVs originales** para reproducir los resultados: el notebook usa los parquet cacheados si existen.

- **Exploración interactiva:** abrir el notebook en VS Code / Jupyter seleccionando el kernel del entorno `.venv`.
- **Ejecución completa sin interfaz:**
  ```bash
  uv run jupyter nbconvert --to notebook --execute --inplace notebook_eda_subte.ipynb
  ```
  La ejecución completa tarda unos 15 minutos; la mayor parte corresponde al ajuste de hiperparámetros del modelo (sección 7.1).
- **Re-ingesta desde los CSV originales:** colocar los 6 archivos `historico_AAAA.csv` en `csv/` y fijar `FORCE_REPROCESS = True` en la celda de configuración del notebook. Esto regenera además `data_processed/` y la tabla `01_resumen_nulos_limpieza.md`.

---

## 📄 Licencia y Fuentes
- **Fuente de datos:** Registros de molinetes del Subterráneo de la Ciudad Autónoma de Buenos Aires (Líneas A, B y C - 2014 a 2019).
- Desarrollado como parte de la investigación en Metodología y Análisis de Operación de Transporte Público.
