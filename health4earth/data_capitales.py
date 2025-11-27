import pandas as pd
import json
from pathlib import Path

RAW = Path("data/raw")
PROC = Path("data/processed")
WEB = Path("website/data")

def load_capitales():
    # Fichier CSV avec capitales, ISO3, lat/lon
    df = pd.read_csv(RAW / "capitales.csv")
    df = df[["country", "capital", "iso3", "lat", "lon"]]
    return df.set_index("iso3")

def load_indicateurs():
    co2 = pd.read_csv(PROC / "co2_clean.csv")  # colonnes: iso_code, year, co2_per_capita
    pollution = pd.read_csv(PROC / "pollution_clean.csv")  # colonnes: country, year, pollution_deaths
    life = pd.read_csv(PROC / "life_clean.csv")  # colonnes: country, year, life_expectancy

    return co2, pollution, life

def build_json():
    capitales = load_capitales()
    co2, pollution, life = load_indicateurs()

    result = {}

    for iso, row in capitales.iterrows():
        cap = row["capital"]
        lat = row["lat"]
        lon = row["lon"]

        # Filtrer les séries par code ISO ou pays
        co2_series = co2[co2["iso_code"] == iso][["year", "co2_per_capita"]]
        poll_series = pollution[pollution["country"] == row["country"]][["year", "pollution_deaths"]]
        life_series = life[life["country"] == row["country"]][["year", "life_expectancy"]]

        # Fusionner les séries par année
        df = pd.merge(co2_series, poll_series, on="year", how="outer")
        df = pd.merge(df, life_series, on="year", how="outer").sort_values("year")

        # Nettoyer et convertir en liste
        series = []
        for _, r in df.iterrows():
            series.append({
                "year": int(r["year"]),
                "co2": r.get("co2_per_capita", None),
                "pollution": r.get("pollution_deaths", None),
                "life": r.get("life_expectancy", None)
            })

        result[cap] = {
            "lat": lat,
            "lon": lon,
            "iso": iso,
            "series": series
        }

    WEB.mkdir(parents=True, exist_ok=True)
    with open(WEB / "series_capitales.json", "w") as f:
        json.dump(result, f, indent=2)

    print("Fichier series_capitales.json exporté dans website/data/")

if __name__ == "__main__":
    build_json()
