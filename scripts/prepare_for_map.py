import pandas as pd

# Chargement des données
df = pd.read_csv("data/clean/health4earth_dataset.csv")
cities = pd.read_csv("data/raw/cities.csv")

# Fusion : associer chaque ville aux données du pays correspondant
df_map = cities.merge(df, left_on='country', right_on='country', how='left')

# Export pour visualisation
df_map.to_csv("data/clean/health4earth_cities.csv", index=False)
print("Dataset pour carte créé : data/clean/health4earth_cities.csv")
