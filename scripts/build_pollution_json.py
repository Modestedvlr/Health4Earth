import pandas as pd
import json
from pathlib import Path

INPUT = "data/raw/WHO_air_pollution_mortality.csv"
OUTPUT = "website/data/series_pollution.json"

df = pd.read_csv(INPUT)

# On garde seulement "Both sexes" pour éviter les doublons
df = df[df["Dim1"] == "Both sexes"]

# ON PREND LA BONNE CLÉ : SpatialDimValueCode (ISO-A3)
df = df[["SpatialDimValueCode", "FactValueNumeric"]]

out = {
    row.SpatialDimValueCode: {"pollution": float(row.FactValueNumeric)}
    for _, row in df.iterrows()
}

Path(OUTPUT).write_text(json.dumps(out, indent=2))
print(f"OK → {OUTPUT}")
