# health4earth/data_transform.py
import pandas as pd
from pathlib import Path

def export_web_ready(df: pd.DataFrame, outdir=Path("data/processed")):
    outdir.mkdir(parents=True, exist_ok=True)
    # Séries par indicateur
    for col in ["co2_emissions_per_capita", "air_pollution_mortality_rate", "life_expectancy"]:
        series = df[["country_code", "year", col]].dropna()
        series.to_json(outdir / f"series_{col}.json", orient="records")
    # Métadonnées pays + capitales
    meta = df.drop_duplicates(subset=["country_code"])[["country_code", "country_name", "capital", "lat", "lon", "region"]]
    meta.to_json(outdir / "countries.json", orient="records")
    