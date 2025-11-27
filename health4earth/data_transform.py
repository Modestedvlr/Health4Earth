import pandas as pd
import json
from pathlib import Path

PROC_DIR = Path("data/processed")
WEB_DIR = Path("website/data")

def export_json():
    WEB_DIR.mkdir(parents=True, exist_ok=True)

    # CO2
    co2 = pd.read_csv(PROC_DIR / "co2_clean.csv")
    latest_year = co2["year"].max()
    co2_latest = co2[co2["year"] == latest_year]
    co2_dict = {row["iso_code"]: {"co2": row["co2_per_capita"]} for _, row in co2_latest.iterrows()}
    json.dump(co2_dict, open(WEB_DIR / "series_co2.json", "w"))

    # Pollution
    pollution = pd.read_csv(PROC_DIR / "pollution_clean.csv")
    latest_year = pollution["year"].max()
    poll_latest = pollution[pollution["year"] == latest_year]
    poll_dict = {row["country"]: {"pollution": row["pollution_deaths"]} for _, row in poll_latest.iterrows()}
    json.dump(poll_dict, open(WEB_DIR / "series_pollution.json", "w"))

    # Life expectancy
    life = pd.read_csv(PROC_DIR / "life_clean.csv")
    latest_year = life["year"].max()
    life_latest = life[life["year"] == latest_year]
    life_dict = {row["country"]: {"life": row["life_expectancy"]} for _, row in life_latest.iterrows()}
    json.dump(life_dict, open(WEB_DIR / "series_life.json", "w"))

    print("Exported JSON files to website/data/")
