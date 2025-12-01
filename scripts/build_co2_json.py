import pandas as pd
import json
from pathlib import Path

INPUT = "data/raw/owid-co2-data.csv"
OUTPUT = "website/data/series_co2.json"

df = pd.read_csv(INPUT)

# On retire les régions "World", etc.
df = df[df["iso_code"].str.len() == 3]

# On garde la dernière année disponible par pays
df = df.sort_values(["iso_code", "year"]).groupby("iso_code").tail(1)

out = {
    row.iso_code: {"co2": float(row["co2"])}
    for _, row in df.iterrows()
    if not pd.isna(row["co2"])
}

Path(OUTPUT).write_text(json.dumps(out, indent=2))
print(f"OK → {OUTPUT}")
