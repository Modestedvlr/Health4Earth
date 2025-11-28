import pandas as pd
import pycountry
import json
from pathlib import Path

INPUT = "data/raw/WHO_life_expectancy.csv"
OUTPUT = "website/data/series_life.json"

def to_iso3(name):
    try:
        return pycountry.countries.lookup(name).alpha_3
    except:
        return None

df = pd.read_csv(INPUT)

# dernière année pour chaque pays
df = df.sort_values(["Country", "Year"])
df = df.groupby("Country").tail(1)

df["iso3"] = df["Country"].apply(to_iso3)
df = df.dropna(subset=["iso3"])

out = {
    row.iso3: {"life": float(row["Life expectancy "] )}
    for _, row in df.iterrows()
}

Path(OUTPUT).write_text(json.dumps(out, indent=2))
print(f"OK → {OUTPUT}")
