# health4earth/data_life.py
import pandas as pd
import json
from pathlib import Path

RAW = Path("data/raw")
WEB = Path("website/data")

def build_life_json():
    df = pd.read_csv(RAW / "WHO_life_expectancy.csv")

    # Normaliser le nom de la colonne (attention aux espaces)
    df = df.rename(columns={'Country': 'country', 'Year': 'year', 'Life expectancy ': 'life_expectancy'})

    # Pour avoir les ISO3, on utilise pycountry
    import pycountry
    def get_iso3(name):
        try:
            return pycountry.countries.lookup(name).alpha_3
        except:
            return None

    df['iso3'] = df['country'].apply(get_iso3)
    df = df.dropna(subset=['iso3'])

    latest_year = df['year'].max()
    df_latest = df[df['year'] == latest_year]

    life_dict = {row['iso3']: {'life': row['life_expectancy']} for _, row in df_latest.iterrows()}

    WEB.mkdir(parents=True, exist_ok=True)
    with open(WEB / "series_life.json", "w") as f:
        json.dump(life_dict, f, indent=2)

    print("✅ series_life.json généré")

if __name__ == "__main__":
    build_life_json()
