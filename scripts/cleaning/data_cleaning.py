import pandas as pd
import os

# Création du dossier clean s'il n'existe pas
os.makedirs("data/clean", exist_ok=True)

# -------------------------------
# Chargement des données utiles
# -------------------------------

# CO2 et PM2.5
co2 = pd.read_csv("data/raw/owid-co2-data.csv", usecols=['country', 'year', 'co2', 'pm25'])

# Espérance de vie
life = pd.read_csv("data/raw/WHO_life_expectancy.csv", usecols=['country', 'year', 'life_expectancy'])

# Mortalité due à la pollution de l'air
mort = pd.read_csv("data/raw/WHO_air_pollution_mortality.csv")

# -------------------------------
# Nettoyage et harmonisation
# -------------------------------

# Harmoniser les noms de colonnes
for df in [co2, life, mort]:
    df.columns = df.columns.str.lower()

# Nettoyage du dataset de mortalité
mort = mort.rename(columns={
    "location": "country",
    "period": "year",
    "factvaluenumeric": "mortality_rate"
})
mort = mort[["country", "year", "mortality_rate"]].dropna()

# -------------------------------
# Fusion des datasets
# -------------------------------

df = co2.merge(life, on=['country', 'year'], how='inner')
df = df.merge(mort, on=['country', 'year'], how='inner')

# Filtrer à partir de l'année 2000
df = df[df['year'] >= 2000]

# -------------------------------
# Export du dataset final
# -------------------------------

df.to_csv("data/clean/health4earth_dataset.csv", index=False)

print("Dataset nettoyé et sauvegardé dans data/clean/health4earth_dataset.csv")
