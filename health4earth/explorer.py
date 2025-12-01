# health4earth/explorer.py
from pathlib import Path
import pandas as pd

class Health4EarthExplorer:
    def __init__(self, data_dir=Path("data")):
        self.data_dir = data_dir
        self.df = None

    def load_data(self):
        # exemple: concat de 3 CSV harmonisés
        co2 = pd.read_csv(self.data_dir / "raw/co2.csv")
        mort = pd.read_csv(self.data_dir / "raw/air_pollution_mortality.csv")
        life = pd.read_csv(self.data_dir / "raw/life_expectancy.csv")
        # harmoniser keys/colonnes ici...
        self.df = self._merge_clean(co2, mort, life)
        return self

    def _merge_clean(self, co2, mort, life):
        # jointures sur country_code + year, normalisation des noms
        # (à compléter selon tes fichiers)
        return co2

    def export_web(self):
        from .data_transform import export_web_ready
        export_web_ready(self.df)
