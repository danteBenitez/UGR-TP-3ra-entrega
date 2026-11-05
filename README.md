# Variación de la Demanda en el Subte de CABA (Líneas A, B y C)
### Preprocesamiento Masivo, Análisis Exploratorio de Datos (EDA) y Validación Estadística (2014–2019)

Este repositorio contiene el pipeline analítico y el código fuente para el estudio empírico de la demanda de pasajeros en la Red de Subterráneos de la Ciudad Autónoma de Buenos Aires (Líneas A, B y C), evaluando la heterogeneidad entre **días hábiles y no laborables** (sábados, domingos y feriados nacionales).

---

## 📊 Principales Hallazgos y Resultados

1. **Volumen Procesado:** Más de 70 millones de registros de molinete (41 millones correspondientes a las Líneas A, B y C), consolidados en **44 estaciones** oficiales en intervalos de 15 minutos y agregados diarios.
2. **Tres tipos de día:** el análisis distingue días **hábiles**, **sábados** y **domingos y feriados**, en coincidencia con los cronogramas del operador (ver `DECISIONES_METODOLOGICAS.md`, DM-03).
3. **Heterogeneidad Estadística (Kolmogorov-Smirnov):** Se rechazó $H_0$ en las **44 estaciones**, tanto para hábil frente a sábado ($D$ entre 0,27 y 0,76) como para hábil frente a domingo-feriado ($D$ entre 0,34 y 0,77), con $p < 10^{-15}$. Este contraste será reemplazado según DM-04.
4. **Ratio de Retención:** la red retiene el **38,58%** de la demanda hábil los sábados y el **19,60%** los domingos y feriados.
   - *Mayor Retención (Polos recreativos / transbordo):* **Carlos Gardel** (72,29% los sábados; 54,14% los domingos y feriados), **Alberti** y **Plaza Miserere** los sábados (54,14% y 53,01%), **Independencia** y **Retiro** los domingos y feriados (31,69% y 28,14%).
   - *Mayor Contracción (Distrito financiero / administrativo):* **Diagonal Norte** y **Plaza de Mayo** los sábados (18,70% y 18,76%); **Florida** y **Diagonal Norte** los domingos y feriados (9,04% y 9,18%).
5. **Presión de Andén:** Con un umbral supuesto de 1.200 pax / 15 min, los 750 intervalos críticos en días no laborables ocurren todos en **Constitución**, el 92% entre las 07:00 y las 10:00 y casi todos en sábados (727; 23 en domingos y feriados), con tendencia creciente en el período. Esta métrica será reemplazada por la frecuencia mínima requerida (DM-05).

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
│   │   ├── 05_kde_habil_vs_nolaborable.png
│   │   └── 06_presion_anden_ventanas_criticas.png
│   ├── tablas/                         # Tablas tabuladas en Markdown
│   │   ├── 01_resumen_nulos_limpieza.md
│   │   ├── 02_estadisticas_descriptivas.md
│   │   ├── 03_ratios_retencion_linea.md
│   │   ├── 04_ratios_retencion_top_bottom_estaciones.md
│   │   ├── 05_resultados_kolmogorov_smirnov_44_estaciones.md
│   │   └── 06_presion_anden_analisis.md
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
- **Re-ingesta desde los CSV originales:** colocar los 6 archivos `historico_AAAA.csv` en `csv/` y fijar `FORCE_REPROCESS = True` en la celda de configuración del notebook. Esto regenera además `data_processed/` y la tabla `01_resumen_nulos_limpieza.md`.

---

## 📄 Licencia y Fuentes
- **Fuente de datos:** Registros de molinetes del Subterráneo de la Ciudad Autónoma de Buenos Aires (Líneas A, B y C - 2014 a 2019).
- Desarrollado como parte de la investigación en Metodología y Análisis de Operación de Transporte Público.
