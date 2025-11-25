import pandas as pd
import os

# Création du dossier de sortie si nécessaire
os.makedirs("data/clean", exist_ok=True)

# -----------------------
# 1️⃣ Chargement des données
# -----------------------

# CO2 (sans pm25, si cette colonne n'existe pas)
co2 = pd.read_csv("data/raw/owid-co2-data.csv", usecols=['country', 'year', 'co2'])

# Espérance de vie
life = pd.read_csv("data/raw/WHO_life_expectancy.csv", usecols=['Country', 'Year', 'Life expectancy '])

# Mortalité liée à la pollution de l'air
mort = pd.read_csv("data/raw/WHO_air_pollution_mortality.csv")

# -----------------------
# 2️⃣ Harmonisation des colonnes
# -----------------------
co2.columns = co2.columns.str.lower()
life.columns = ['country', 'year', 'life_expectancy']  # correction du nom avec espace
mort.columns = mort.columns.str.lower()

# -----------------------
# 3️⃣ Nettoyage WHO_air_pollution_mortality
# -----------------------
mort = mort.rename(columns={
    "location": "country",
    "period": "year",
    "factvaluenumeric": "mortality_rate"
})
mort = mort[["country", "year", "mortality_rate"]].dropna()

# -----------------------
# 4️⃣ Fusion progressive
# -----------------------
df = co2.merge(life, on=['country', 'year'], how='inner')
df = df.merge(mort, on=['country', 'year'], how='inner')

# -----------------------
# 5️⃣ Filtrage années
# -----------------------
df = df[df['year'] >= 2000]

# -----------------------
# 6️⃣ Export
# -----------------------
df.to_csv("data/clean/health4earth_dataset.csv", index=False)

print("Dataset final créé : data/clean/health4earth_dataset.csv")
