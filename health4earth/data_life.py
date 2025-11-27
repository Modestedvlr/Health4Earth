import pandas as pd
import json
from pathlib import Path

RAW = Path("data/raw")
WEB = Path("website/data")

def build_life_json():
    df = pd.read_csv(RAW / "WHO_life_expectancy.csv")

    # Renommer les colonnes (attention aux espaces !)
    df = df.rename(columns={
        "Country": "country",
        "Year": "year",
        "Life expectancy ": "life_expectancy"
    })

    # Garder uniquement ce qu'on veut
    df = df[["country", "year", "life_expectancy"]]

    # Dernière année dispo
    latest_year = df["year"].max()
    df_latest = df[df["year"] == latest_year]

    # Transformer en dictionnaire
    life_dict = {
        row["country"]: {"life": row["life_expectancy"]}
        for _, row in df_latest.iterrows()
    }

    # Sauvegarde
    WEB.mkdir(parents=True, exist_ok=True)
    with open(WEB / "series_life.json", "w") as f:
        json.dump(life_dict, f, indent=2)

    print("✅ Fichier series_life.json exporté dans website/data/")

if __name__ == "__main__":
    build_life_json()