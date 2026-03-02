# 🌍 API Data Dashboard

A modular **Python data pipeline** that ingests real-time country data from a public REST API, transforms it into a structured analytical dataset, and generates insights through both static and interactive visualizations.

This project reflects a production-style analytics workflow:

API Ingestion → Data Validation → Transformation → Feature Engineering → Analysis → Visualization

---

## 📊 Dashboard Preview

<p align="center">
  <img src="./images/dashboard_preview.png" width="800">
</p>

---

## 🧠 Key Capabilities

- REST API integration with status validation and error handling  
- JSON normalization into structured pandas DataFrames  
- Data cleaning and integrity checks  
- Feature engineering: **Population Density metric**  
- Exploratory analysis (Top 10 population ranking)  
- Dual visualization layer:
  - Matplotlib (analytical reporting)
  - Plotly (interactive exploration)

---

## ⚙️ Architecture

```
API Request
    ↓
JSON Response
    ↓
Data Cleaning & Validation
    ↓
Feature Engineering
    ↓
Exploratory Analysis
    ↓
Visualization
```

---

## 🛠 Tech Stack

- Python 3  
- requests  
- pandas  
- matplotlib  
- plotly  

---

## 🚀 Setup & Execution

```bash
git clone https://github.com/yourusername/api-data-dashboard.git
cd api-data-dashboard
python -m pip install requests pandas matplotlib plotly
python api_data_dashboard.py
```

---

## 📊 Analytical Output

- Top 10 most populated countries  
- Population vs Area distribution analysis  
- Regional segmentation insights  
- Derived population density metric  

---

## 📈 Project Value

This repository simulates a real-world analytics pipeline involving:

- External data ingestion  
- Automated transformation workflow  
- Insight extraction  
- Data storytelling through visualization  

The architecture can be adapted to financial APIs, engagement analytics, churn modeling, or monetization dashboards.

---

## 👨‍💻 Author

**Santiago Acosta**  
Data Analyst | Python | SQL | Business Intelligence  
