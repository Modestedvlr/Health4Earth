import pooch
import pandas as pd
import os

# L'URL officielle des données CO2 (Our World in Data)
URL_CO2 = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"

def load_co2_data() -> pd.DataFrame:
    """
    Télécharge automatiquement les données CO2 depuis le dépôt OWID
    et les charge dans un DataFrame pandas.
    
    Les données sont mises en cache localement (dans le dossier OS par défaut)
    pour ne pas les retélécharger à chaque fois.
    """
    # Pooch gère le téléchargement et le cache
    file_path = pooch.retrieve(
        url=URL_CO2,
        known_hash=None,  # On met None pour l'instant (on accepte les mises à jour du fichier)
        fname="owid_co2_data.csv",
        path=pooch.os_cache("health4earth"), # Stockage propre dans le cache système
        progressbar=True
    )
    
    # On charge le CSV téléchargé
    df = pd.read_csv(file_path)
    return df

# Exemple d'utilisation si on lance le script directement
if __name__ == "__main__":
    df = load_co2_data()
    print(f"Données chargées ! Taille : {df.shape}")
    print(df.head())