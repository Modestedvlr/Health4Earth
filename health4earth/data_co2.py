import pandas as pd
import json
from pathlib import Path

RAW = Path("data/raw")
WEB = Path("website/data")

def build_co2_json():
    # Charger le fichier OWID
    df = pd.read_csv(RAW / "owid-co2-data.csv")

    # Garder colonnes utiles
    df = df[["iso_code", "year", "co2_per_capita"]].dropna(subset=["iso_code"])

    # Prendre la dernière année disponible
    latest_year = df["year"].max()
    df_latest = df[df["year"] == latest_year]

    # Transformer en dictionnaire {ISO3: {co2: valeur}}
    co2_dict = {row["iso_code"]: {"co2": row["co2_per_capita"]}
                for _, row in df_latest.iterrows()}

    # Sauvegarder dans website/data
    WEB.mkdir(parents=True, exist_ok=True)
    with open(WEB / "series_co2.json", "w") as f:
        json.dump(co2_dict, f, indent=2)

    print("✅ Fichier series_co2.json exporté dans website/data/")

if __name__ == "__main__":
    build_co2_json()