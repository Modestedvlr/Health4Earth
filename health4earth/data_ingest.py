import pandas as pd
from pathlib import Path

def load_co2_data(path: Path) -> pd.DataFrame:
    """Charge les données de CO2 depuis un fichier CSV."""
    return pd.read_csv(path)

def load_pollution_data(path: Path) -> pd.DataFrame:
    """Charge les données de mortalité liée à la pollution."""
    return pd.read_csv(path)

def load_life_expectancy_data(path: Path) -> pd.DataFrame:
    """Charge les données d'espérance de vie."""
    return pd.read_csv(path)
