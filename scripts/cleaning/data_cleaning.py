import pandas as pd

# Chargement des données brutes
co2 = pd.read_csv("data/raw/owid-co2-data.csv", usecols=['country', 'year', 'co2', 'pm25'])
life = pd.read_csv("data/raw/WHO_life_expectancy.csv", usecols=['country', 'year', 'life_expectancy'])
mort = pd.read_csv("data/raw/WHO_air_pollution_mortality.csv", usecols=['country', 'year', 'mortality_rate'])

# Harmonisation des colonnes
for df in [co2, life, mort]:
    df.columns = df.columns.str.lower()

# Fusion
df = co2.merge(life, on=['country', 'year'], how='inner')
df = df.merge(mort, on=['country', 'year'], how='inner')

# Nettoyage
df = df.dropna()
df = df[df['year'] >= 2000]   # Filtre temporel cohérent

# Sauvegarde propre
df.to_csv("data/clean/health4earth_dataset.csv", index=False)

print("Dataset nettoyé et enregistré dans data/clean/health4earth_dataset.csv")
