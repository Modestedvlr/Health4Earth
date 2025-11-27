import pandas as pd
import json
from pathlib import Path

RAW = Path("data/raw")
WEB = Path("website/data")

def build_pollution_json():
    # Charger le fichier WHO
    df = pd.read_csv(RAW / "WHO_air_pollution_mortality.csv")

    # Trouver l'indicateur pollution de l'air (évite les erreurs)
    pollution_indicators = df[df["Indicator"].str.contains(
        "air pollution", case=False, na=False
    )]["Indicator"].unique()

    if len(pollution_indicators) == 0:
        raise ValueError("Aucun indicateur lié à la pollution de l’air trouvé.")
    
    # Si plusieurs, on garde le premier (ou on peut filtrer plus précisément)
    indicator = pollution_indicators[0]
    print(f"📌 Indicateur utilisé : {indicator}")

    # Filtrer uniquement cet indicateur
    df = df[df["Indicator"] == indicator]

    # Renommer les colonnes selon le dataset WHO
    df = df.rename(columns={
        "Location": "country",
        "Period": "year",
        "FactValueNumeric": "pollution_deaths"
    })

    # Garder uniquement les colonnes utiles
    df = df[["country", "year", "pollution_deaths"]]

    # Convertir l'année en entier
    df["year"] = df["year"].astype(int)

    # Prendre la dernière année disponible
    latest_year = df["year"].max()
    print(f"📅 Dernière année trouvée : {latest_year}")

    df_latest = df[df["year"] == latest_year]

    # Construire dictionnaire final
    pollution_dict = {
        row["country"]: {"pollution": row["pollution_deaths"]}
        for _, row in df_latest.iterrows()
    }

    # Sauvegarde JSON
    WEB.mkdir(parents=True, exist_ok=True)
    with open(WEB / "series_pollution.json", "w") as f:
        json.dump(pollution_dict, f, indent=2)

    print("✅ Fichier series_pollution.json exporté dans website/data/")


if __name__ == "__main__":
    build_pollution_json()