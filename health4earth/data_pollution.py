# health4earth/data_pollution.py
import pandas as pd
import json
from pathlib import Path

RAW = Path("data/raw")
WEB = Path("website/data")

def build_pollution_json():
    df = pd.read_csv(RAW / "WHO_air_pollution_mortality.csv")

    df = df.rename(columns={
        'Location': 'country',
        'Period': 'year',
        'Value': 'pollution'
    })

    import pycountry
    def get_iso3(name):
        try:
            return pycountry.countries.lookup(name).alpha_3
        except:
            return None

    df['iso3'] = df['country'].apply(get_iso3)
    df = df.dropna(subset=['iso3', 'pollution'])

    latest_year = df['year'].max()
    df_latest = df[df['year'] == latest_year]

    pollution_dict = {row['iso3']: {'pollution': row['pollution']} for _, row in df_latest.iterrows()}

    WEB.mkdir(parents=True, exist_ok=True)
    with open(WEB / "series_pollution.json", "w") as f:
        json.dump(pollution_dict, f, indent=2)

    print("✅ series_pollution.json généré")

if __name__ == "__main__":
    build_pollution_json()
