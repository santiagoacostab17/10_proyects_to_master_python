# 🗂️ Batch CSV & Excel Processor

## 📌 Overview
A **Python command-line program** that **automatically cleans, aggregates, and summarizes multiple CSV and Excel datasets**.  

Designed for **data analysts and business intelligence workflows**, it demonstrates **pandas, OpenPyXL, and automation best practices** while providing a fully functional **batch processor** for real-world datasets.

---

## ⚙️ Features

- Automatically process **all CSV and Excel files** in a folder  
- **Clean data** by removing empty rows/columns and filling missing values  
- Generate **descriptive statistics** for numeric and categorical data  
- Save **cleaned datasets** and **summary reports** to an output folder  
- Modular, reusable **Python functions** for cleaning and summarizing  
- Supports **large batch processing** with progress tracking  

---

## 🛠️ How It Works

1. **Configuration**  
   - Define input and output folders.  
   - Automatically create the output folder if it doesn't exist.

2. **Data Cleaning (`clean_data`)**  
   - Remove fully empty rows and columns.  
   - Replace remaining missing values with `0`.

3. **Data Summarization (`summarize_data`)**  
   - Generate descriptive statistics for numeric and categorical columns.  
   - Transpose the summary table for readability.

4. **Batch Processing (`process_files`)**  
   - Loop through all CSV/XLSX files in the input folder.  
   - Read, clean, save cleaned data, generate summary, and save summary.  
   - Log each processed file to the console.

---

## 📊 Process Flow Diagram

A visual representation of the **batch data cleaning and summarization workflow**:  

[![Data Pipeline Flowchart](./images/batch_flow.png)](./images/batch_flow.png) 
*Shows steps from reading files, cleaning, summarizing, and saving results.*

---

## 🚀 Usage

1. Place your `.csv` and `.xlsx` files in the `data` folder.  
2. Run the script:  
```bash
python batch_processor.py
