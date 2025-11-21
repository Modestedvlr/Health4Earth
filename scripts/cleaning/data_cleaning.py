import pandas as pd

# Chargement des données
co2 = pd.read_csv("data/raw/owid-co2-data.csv", usecols=['country', 'year', 'co2', 'pm25'])
life = pd.read_csv("data/raw/WHO_life_expectancy.csv", usecols=['country', 'year', 'life_expectancy'])
mort = pd.read_csv("data/raw/WHO_air_pollution_mortality.csv")

# Harmonisation des colonnes
for df in [co2, life, mort]:
    df.columns = df.columns.str.lower()

# Nettoyage WHO_air_pollution_mortality → garder seulement les colonnes utiles
mort = mort.rename(columns={
    "location": "country",
    "period": "year",
    "factvaluenumeric": "mortality_rate"
})
mort = mort[["country", "year", "mortality_rate"]]
mort = mort.dropna()

# Merge progressif (CO2 + espérance de vie + mortalité due à la pollution)
df = co2.merge(life, on=['country', 'year'], how='inner')
df = df.merge(mort, on=['country', 'year'], how='inner')

# Filtrage années
df = df[df['year'] >= 2000]

# Export
df.to_csv("data/clean/health4earth_dataset.csv", index=False)
