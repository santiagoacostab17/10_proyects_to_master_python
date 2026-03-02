# 🌍 Countries API Dashboard

A minimal data analysis project that consumes the REST Countries API, transforms JSON data into a structured dataset, and generates a clear analytical dashboard using Python.

---

## 📊 Dashboard Preview

![Dashboard Preview](images/dashboard_preview.png)

---

## 🛠 Tech Stack

- Python
- requests
- pandas
- matplotlib

---

## ⚙️ What the Script Does

1. Connects to the REST Countries API  
2. Retrieves selected fields (name, region, population, area, capital)  
3. Converts nested JSON into a structured pandas DataFrame  
4. Cleans and sorts the data by population  
5. Normalizes population values to millions  
6. Displays the Top 10 most populated countries  
7. Generates a labeled bar chart dashboard  

---

## ⚙️ How to Run

```bash
pip install requests pandas matplotlib
python api_data_dashboard.py
