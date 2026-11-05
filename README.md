# Variación de la Demanda en el Subte de CABA (Líneas A, B y C)
### Preprocesamiento Masivo, Análisis Exploratorio de Datos (EDA) y Validación Estadística (2014–2019)

Este repositorio contiene el pipeline analítico y el código fuente para el estudio empírico de la demanda de pasajeros en la Red de Subterráneos de la Ciudad Autónoma de Buenos Aires (Líneas A, B y C), evaluando la heterogeneidad entre **días hábiles y no laborables** (sábados, domingos y feriados nacionales).

---

## 📊 Principales Hallazgos y Resultados

1. **Volumen Procesado:** Más de 70 millones de registros de molinete (41 millones correspondientes a las Líneas A, B y C), consolidados en **44 estaciones** oficiales en intervalos de 15 minutos y agregados diarios.
2. **Heterogeneidad Estadística (Kolmogorov-Smirnov):** Se rechazó $H_0$ en el **100% de las 44 estaciones** ($p < 10^{-15}$ en todas; $D$ entre 0,30 y 0,76), indicando que las distribuciones de demanda por intervalo en días no laborables difieren de las de días hábiles.
3. **Ratio Global de Retención:** La demanda no laborable retiene en promedio un **27,86%** del flujo hábil (caída del 72,14%).
   - *Mayor Retención (Polos recreativos / transbordo):* **Carlos Gardel (62,22%)**, **Independencia (38,39%)**, **Alberti (36,41%)**, **Retiro (36,26%)** y **Plaza Miserere (36,15%)**.
   - *Mayor Contracción (Distrito financiero / administrativo):* **Diagonal Norte (13,27%)**, **Florida (13,63%)** y **Plaza de Mayo (14,65%)**.
   - *Sábado ≠ Domingo:* los sábados retienen el **38,48%** de la demanda hábil, los domingos el **18,78%** y los feriados el **22,87%**.
4. **Presión de Andén:** Con un umbral supuesto de 1.200 pax / 15 min, los 750 intervalos críticos en días no laborables ocurren todos en **Constitución**, el 92% entre las 07:00 y las 10:00 y mayoritariamente en sábados (688; el resto en feriados, ninguno en domingos), con tendencia creciente en el período.

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
