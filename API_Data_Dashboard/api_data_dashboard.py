import requests
import pandas as pd
import matplotlib.pyplot as plt
import logging


# ----------------------------
# Configuration
# ----------------------------

API_URL = "https://restcountries.com/v3.1/all?fields=name,region,population,area,capital"


# ----------------------------
# Logging Setup
# ----------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)


# ----------------------------
# API Connection
# ----------------------------

def fetch_data(url: str) -> list:
    logging.info("Connecting to API...")

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    logging.info("API connection successful.")
    return response.json()


# ----------------------------
# Data Processing
# ----------------------------

def process_data(raw_data: list) -> pd.DataFrame:
    records = []

    for country in raw_data:
        capital_list = country.get("capital", [])
        capital = capital_list[0] if capital_list else None

        records.append({
            "Country": country.get("name", {}).get("common"),
            "Region": country.get("region"),
            "Population": country.get("population", 0),
            "Area": country.get("area", 0),
            "Capital": capital
        })

    df = pd.DataFrame(records)

    df = df.dropna(subset=["Country"])
    df = df.sort_values(by="Population", ascending=False)

    return df


# ----------------------------
# Visualization
# ----------------------------

def create_dashboard(df: pd.DataFrame):
    top_10 = df.head(10).copy()

    top_10["Population_Millions"] = top_10["Population"] / 1_000_000

    plt.figure(figsize=(12, 6))
    plt.bar(top_10["Country"], top_10["Population_Millions"])

    plt.title("Top 10 Most Populated Countries")
    plt.xlabel("Country")
    plt.ylabel("Population (Millions)")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# ----------------------------
# Main Execution
# ----------------------------

def main():
    try:
        raw_data = fetch_data(API_URL)
        df = process_data(raw_data)

        print("\nTop 10 Most Populated Countries:\n")
        print(df.head(10))

        create_dashboard(df)

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
