# health4earth/data_co2.py
import pandas as pd
import json
from pathlib import Path

RAW = Path("data/raw")
WEB = Path("website/data")

def build_co2_json():
    df = pd.read_csv(RAW / "owid-co2-data.csv")

    # On garde l'année la plus récente pour chaque pays
    latest_year = df['year'].max()
    df_latest = df[df['year'] == latest_year]

    # On garde ISO3 et émissions CO2
    df_latest = df_latest[['iso_code', 'co2']]
    df_latest = df_latest.dropna(subset=['iso_code', 'co2'])

    co2_dict = {row['iso_code']: {'co2': row['co2']} for _, row in df_latest.iterrows()}

    WEB.mkdir(parents=True, exist_ok=True)
    with open(WEB / "series_co2.json", "w") as f:
        json.dump(co2_dict, f, indent=2)

    print("✅ series_co2.json généré")

if __name__ == "__main__":
    build_co2_json()
