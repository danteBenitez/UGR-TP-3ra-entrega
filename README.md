# Variación y Modelado Predictivo de la Demanda en el Subte de CABA (Líneas A, B y C)
### Preprocesamiento Masivo, EDA, Validación Estadística, Ingeniería de Series Temporales y Aprendizaje Supervisado (2014–2019)

Este repositorio contiene el pipeline analítico y predictivo completo para el estudio empírico y modelado de la demanda de pasajeros en la Red de Subterráneos de la Ciudad Autónoma de Buenos Aires (Líneas A, B y C, 44 estaciones), evaluando la heterogeneidad entre **días hábiles y no laborables** (sábados, domingos y feriados nacionales) bajo la metodología **CRISP-DM adaptada a series temporales** (Fases 1 a 8).

---

## 📊 Principales Hallazgos y Resultados (EDA + Modelado)

1. **Volumen Procesado y Grilla Temporal:** Más de 70 millones de transacciones de molinetes consolidadas en **44 estaciones** (2014–2019) y regularizadas en una matriz equidistante de **7.145.292 registros** (76 ventanas comerciales de 15 min por día, `05:00` a `23:45`).
2. **Heterogeneidad Estadística (Kolmogorov-Smirnov):** Se rechazó $H_0$ en el **100% de las 44 estaciones** ($p < 10^{-15}$), validando que las distribuciones de demanda en días no laborables difieren estructuralmente del régimen laboral.
3. **Modelado Supervisado (Regresión Lineal vs. Gradient Boosting / XGBoost):**
   - Bajo partición estrictamente cronológica (*Time-Based Splitting*: `Train` 2014–2017, `Val` 2018, `Test` 2019), **XGBoost** superó de forma contundente al baseline lineal en el año de prueba (2019):
     - **RMSE:** Reducción del **23,09%** (`56,01` vs `72,82` pax/15min).
     - **MAE:** Reducción del **31,98%** (`22,31` vs `32,80` pax/15min).
     - **Bondad de ajuste:** **$R^2 = 0,9502$** en test (frente a $0,9157$ del modelo lineal).
   - En pronósticos *Multi-Step* hacia el futuro, XGBoost retiene un **$R^2 = 0,9437$** a 30 minutos y **$R^2 = 0,9261$** a 60 minutos.
4. **Métricas Operativas Derivadas (Fase 8):**
   - El modelo predice el Ratio de Retención por estación con un error medio de solo **0,58 puntos porcentuales**, captura el desplazamiento horario de los picos (*peak shift* vespertino en fines de semana) y clasifica las 44 estaciones en **4 Categorías Operativas según Presión de Andén**.

---

## 📁 Estructura del Repositorio

```text
EDA/
├── data_processed/                     # Datasets procesados en formato Parquet
│   ├── subte_consolidado_15min.parquet # Demanda agregada cada 15 min (2014-2019)
│   ├── subte_diario_estaciones.parquet # Demanda diaria consolidada por estación
│   └── subte_modelado_15min.parquet    # Matriz equidistante con lags y geolocalización (7.14M filas)
├── output/
│   ├── graficos/                       # Figuras analíticas y de modelado en alta resolución (300 DPI)
│   │   ├── 01_curva_demanda_dia_semana.png
│   │   ├── 02_curva_demanda_estacional_mes.png
│   │   ├── 03_perfil_horario_por_linea.png
│   │   ├── 04_comparativa_habil_nolab_estaciones_clave.png
│   │   ├── 05_kde_habil_vs_nolaborable.png
│   │   ├── 06_presion_anden_ventanas_criticas.png
│   │   ├── 07_comparativa_prediccion_real_vs_modelos.png
│   │   ├── 08_evaluacion_errores_e_importancia_variables.png
│   │   └── 09_categorizacion_estaciones_presion_predicha.png
│   ├── tablas/                         # Tablas tabuladas en Markdown (Fases 3 a 8)
│   │   ├── 01_resumen_nulos_limpieza.md
│   │   ├── 02_estadisticas_descriptivas.md
│   │   ├── 03_ratios_retencion_linea.md
│   │   ├── 04_ratios_retencion_top_bottom_estaciones.md
│   │   ├── 05_resultados_kolmogorov_smirnov_44_estaciones.md
│   │   ├── 06_presion_anden_analisis.md
│   │   ├── 07_auditoria_limpieza_modelado.md
│   │   ├── 08_comparativa_modelos_metricas.md
│   │   └── 09_metricas_operativas_predichas.md
│   └── resumen_metodologia.md          # Síntesis interpretativa para el informe
├── src/                                # Módulos Python del pipeline
│   ├── preprocesamiento.py             # Ingesta por bloques, sanitización y normalización
│   ├── eda_visualizaciones.py          # Generador de gráficos EDA (Figuras 01 a 06)
│   ├── validacion_estadistica.py       # Test K-S, ratios de retención y presión de andén histórica
│   ├── estaciones_geo.py               # Coordenadas geolocalizadas y metadatos espaciales (44 estaciones)
│   ├── preparacion_modelado.py         # Grilla equidistante, limpieza de cierres/outliers, lags y split temporal
│   ├── modelado_evaluacion.py          # Regresión Lineal vs XGBoost, evaluación MSE/RMSE/MAE y Fase 8
│   └── generar_notebook.py             # Generador del Jupyter Notebook reproducible
├── notebook_eda_subte.ipynb            # Jupyter Notebook completo (EDA + Modelado + Evaluación)
├── run_analysis.py                     # Script orquestador end-to-end (Pasos 1 a 5)
├── requirements.txt                    # Dependencias del proyecto
└── .gitignore                          # Exclusión de datos crudos masivos (6.7 GB) y temporales
```

---

## 🚀 Instalación y Puesta en Marcha

### 1. Clonar el Repositorio
```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd EDA
```

### 2. Configurar el Entorno e Instalar Dependencias
Se recomienda utilizar Python 3.10 o 3.11:
```bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

---

## 💻 Modos de Uso

Los datasets optimizados en Parquet se encuentran versionados en `data_processed/` (~11 MB), por lo que **no es necesario descargar los 6.7 GB de CSVs crudos** para reproducir los análisis.

### Opción A: Ejecución Completa por Consola (Recomendado)
Ejecuta el script orquestador `run_analysis.py`, que recorre automáticamente los 5 pasos del pipeline:
```bash
python run_analysis.py
```
*(Opcionales disponibles:)*
- `python run_analysis.py --only-modeling`: Corre únicamente la preparación de series temporales, el entrenamiento de modelos y las métricas operativas (Pasos 4 y 5).
- `python run_analysis.py --force-reprocess`: Si colocaste los 6 CSVs originales en `csv/`, fuerza la re-ingesta y limpieza de los 70M de registros desde cero.

### Opción B: Ejecución en Jupyter Notebook o VS Code
1. Abre el archivo `notebook_eda_subte.ipynb` en Jupyter o VS Code.
2. Selecciona el kernel de Python correspondiente.
3. Presiona **"Run All" / "Ejecutar todas las celdas"**. El cuaderno ejecutará de principio a fin el preprocesamiento, los contrastes estadísticos, el EDA visual, el entrenamiento de modelos y la evaluación operativa.

### Opción C: Ejecución en Google Colab
1. Sube el cuaderno `notebook_eda_subte.ipynb` a Google Colab.
2. Clona el repositorio en una celda inicial para disponer de los datos y scripts modulares:
   ```python
   !git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   %cd TU_REPOSITORIO
   !pip install -r requirements.txt
   ```
3. Menú **Entorno de ejecución** $\to$ **"Ejecutar todas"** (`Ctrl + F9`).

---

## 📑 Licencia y Fuentes
- **Fuente de datos:** Registros oficiales de ingresos por molinetes de la Red de Subterráneos de CABA (Líneas A, B y C, período 2014 a 2019), Gobierno de la Ciudad Autónoma de Buenos Aires.
- **Ámbito académico:** Trabajo Práctico de Metodología de la Investigación y Ciencia de Datos — Universidad de Gran Rosario (UGR).
