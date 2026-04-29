# 🌍 Análisis de Migración Internacional (Siglo XXI)

Proyecto de análisis de datos enfocado en identificar patrones y factores socioeconómicos asociados a los flujos migratorios entre países.

---

## 🎯 Objetivo

Analizar datos de migración internacional para detectar tendencias relevantes y comprender cómo variables como el PIB y el IDH influyen en los movimientos de población.

---

## 🧠 Alcance del proyecto

El análisis incluye:

- Limpieza y transformación de datos
- Detección y eliminación de outliers (IQR)
- Estandarización de variables categóricas
- Análisis exploratorio (EDA)
- Agrupamiento y agregaciones
- Generación de nuevas variables analíticas
- Exportación de dataset limpio

---

## 🗂️ Estructura del proyecto


migracion-analisis/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
│
├── src/
│ ├── limpieza.py
│ ├── analisis.py
│
├── main.py
├── requirements.txt
└── README.md


---

## ⚙️ Tecnologías utilizadas

- Python 3
- Pandas
- NumPy
- Matplotlib / Seaborn

---

## 🔄 Pipeline de datos

1. Carga de datos CSV
2. Detección de outliers mediante IQR
3. Limpieza de datos
4. Transformación de variables categóricas
5. Análisis estadístico
6. Generación de variables derivadas
7. Exportación de dataset limpio

---

## 📊 Principales análisis realizados

- Media y mediana de migrantes
- Migración total por razón
- PIB promedio por país de origen/destino
- Diferencias de IDH entre países
- Identificación de patrones socioeconómicos

---

## 📈 Visualizaciones (EDA)

### Distribución de migrantes
![Gráfico 1](images/grafico1.png)

### Migrantes por razón de migración
![Gráfico 2](images/grafico2.png)

### Relación entre PIB y migración
![Gráfico 3](images/grafico3.png)

### Diferencias de IDH
![Gráfico 4](images/grafico4.png)
---

## ▶️ Cómo ejecutar

```bash
git clone https://github.com/IsaUrdaneta/migracion-analisis.git
cd migracion-analisis
pip install -r requirements.txt
python main.py

📌 Resultados clave (ejemplo)
La mayoría de migraciones se concentran por razones económicas
Existe relación positiva entre PIB destino y flujo migratorio
El IDH del país destino suele ser mayor que el de origen


🚀 Posibles mejoras
Modelos predictivos de migración
Dashboard interactivo (Power BI / Streamlit)
Integración con APIs de datos reales
Series temporales


👩‍💻 Autor
Isanevys Urdaneta
Ingeniera de Petróleo | Data Analyst en formación