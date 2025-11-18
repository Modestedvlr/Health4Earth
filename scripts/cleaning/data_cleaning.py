import pandas as pd

# Chargement des données
co2 = pd.read_csv("data/owid-co2-data.csv", usecols=['country', 'year', 'co2', 'pm25'])
life = pd.read_csv("data/WHO_life_expectancy.csv", usecols=['country', 'year', 'life_expectancy'])
mort = pd.read_csv("data/WHO_air_pollution_mortality.csv", usecols=['country', 'year', 'mortality_rate'])

# Harmonisation des noms de colonnes
for df in [co2, life, mort]:
    df.columns = df.columns.str.lower()

# Fusion progressive
df = co2.merge(life, on=['country', 'year'], how='inner')
df = df.merge(mort, on=['country', 'year'], how='inner')

# Nettoyage final
df = df.dropna()
df = df[df['year'] >= 2000]  # Filtrage temporel

# Sauvegarde
df.to_csv("data/health4earth_dataset.csv", index=False)
