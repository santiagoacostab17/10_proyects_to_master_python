import pandas as pd
import os

# -----------------------------
# Configuration
# -----------------------------
INPUT_FOLDER = "data"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# -----------------------------
# Data Cleaning Function
# -----------------------------
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean a DataFrame by:
    - Dropping fully empty columns
    - Dropping fully empty rows
    - Filling remaining NaNs with 0
    """
    df = df.dropna(axis=1, how='all')
    df = df.dropna(axis=0, how='all')
    df = df.fillna(0)
    return df

# -----------------------------
# Data Summarization Function
# -----------------------------
def summarize_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate descriptive statistics for both numeric and categorical columns
    """
    return df.describe(include='all').transpose()  # Transpose for readability

# -----------------------------
# Batch Processing
# -----------------------------
def process_files(input_folder: str, output_folder: str):
    files = [f for f in os.listdir(input_folder) if f.endswith(('.csv', '.xlsx'))]

    for file_name in files:
        file_path = os.path.join(input_folder, file_name)

        # Read file
        if file_name.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path, engine='openpyxl')

        # Clean data
        df_clean = clean_data(df)

        # Save cleaned data
        clean_file_path = os.path.join(output_folder, f"clean_{file_name}")
        if file_name.endswith('.csv'):
            df_clean.to_csv(clean_file_path, index=False)
        else:
            df_clean.to_excel(clean_file_path, index=False, engine='openpyxl')

        # Generate summary
        summary_df = summarize_data(df_clean)

        # Save summary
        summary_file_path = os.path.join(output_folder, f"summary_{file_name}")
        if file_name.endswith('.csv'):
            summary_df.to_csv(summary_file_path)
        else:
            summary_df.to_excel(summary_file_path, engine='openpyxl')

        print(f"Processed: {file_name}")

# -----------------------------
# Run the Batch Processor
# -----------------------------
if __name__ == "__main__":
    process_files(INPUT_FOLDER, OUTPUT_FOLDER)
