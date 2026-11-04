# Variación de la Demanda en el Subte de CABA (Líneas A, B y C)
### Preprocesamiento Masivo, Análisis Exploratorio de Datos (EDA) y Validación Estadística (2014–2019)

Este repositorio contiene el pipeline analítico y el código fuente para el estudio empírico de la demanda de pasajeros en la Red de Subterráneos de la Ciudad Autónoma de Buenos Aires (Líneas A, B y C), evaluando la heterogeneidad entre **días hábiles y no laborables** (sábados, domingos y feriados nacionales).

---

## 📊 Principales Hallazgos y Resultados

1. **Volumen Procesado:** Más de 70 millones de transacciones de molinetes consolidadas en **44 estaciones** oficiales en intervalos de 15 minutos y agregados diarios.
2. **Heterogeneidad Estadística (Kolmogorov-Smirnov):** Se rechazó $H_0$ en el **100% de las 44 estaciones** ($p < 10^{-15}$ en todas), validando que las distribuciones temporales de demanda en días no laborales difieren cuantitativa y cualitativamente del régimen laboral.
3. **Ratio Global de Retención:** La demanda no laborable retiene en promedio un **42,03%** del flujo hábil (caída del 57,97%).
   - *Mayor Retención (Polos recreativos / transbordo):* **Carlos Gardel (70,43%)**, **Independencia (50,24%)**, **Retiro (49,14%)** y **Plaza Miserere (49,07%)**.
   - *Mayor Contracción (Distrito financiero / administrativo):* **Diagonal Norte (28,72%)**, **Plaza de Mayo (28,99%)** y **Florida (30,18%)**.
4. **Presión de Andén:** Se identificaron ventanas críticas en fines de semana donde la tasa de afluencia por 15 minutos en nodos de transbordo (Constitución, Retiro, Lacroze) supera los 1.200 a 1.500 pax, provocando hacinamiento transitorio ante reducciones excesivas de frecuencias.

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
