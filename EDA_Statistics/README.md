# Exploratory Data Analysis & Statistics — Northwind Dataset

Full EDA pipeline applied to the Northwind business dataset: distributions, correlations, outlier detection, and statistical summaries to surface actionable insights from sales, product, and customer data.

---

## Objective

Apply a structured EDA process to a real business dataset to answer:

- What does the revenue distribution look like across products, categories, and regions?
- Are there statistically significant correlations between discount, quantity, and revenue?
- Where are the outliers and what do they tell us about the business?
- Which variables drive sales performance the most?

---

## Dataset

**Northwind Traders** — a sample business database representing a fictional import/export company.

| Table | Description |
|---|---|
| `orders` | Sales transactions with date, customer, employee |
| `order_details` | Line items: product, quantity, unit price, discount |
| `products` | Product catalog with category and supplier |
| `customers` | Customer info and region |
| `categories` | Product categories |

---

## Project Structure

    eda-northwind/
    │
    ├── data/
    │   └── northwind_clean.csv
    │
    ├── notebooks/
    │   └── eda_northwind.ipynb
    │
    ├── assets/
    │   └── *.png
    │
    ├── requirements.txt
    └── README.md

---

## EDA Pipeline

1. Data Loading & Inspection
2. Univariate Analysis — distributions, skewness, kurtosis
3. Bivariate Analysis — scatter plots, regression lines, time trends
4. Correlation Analysis — Pearson & Spearman heatmaps
5. Outlier Detection — IQR method & Z-score
6. Statistical Summaries — by category, product, and customer

---

## Tools

| Tool | Purpose |
|---|---|
| `pandas` | Data loading, cleaning, transformation |
| `seaborn` | Statistical visualizations |
| `matplotlib` | Custom plot formatting |
| `scipy.stats` | Correlation tests, Z-scores |
| `jupyter` | Interactive notebook environment |

---

## Author

**Santiago Acosta** — Data Analyst | Bogotá, Colombia
Portfolio: [santiagoacostab17.github.io](https://santiagoacostab17.github.io)
