import pandas as pd

class HealthAnalyzer:
    """
    Classe chargée d'analyser les relations statistiques entre les facteurs environnementaux
    et la santé publique.
    
    Attributes:
        data (pd.DataFrame): Le jeu de données complet contenant CO2, pollution et espérance de vie.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Initialise l'analyseur avec un DataFrame.

        Args:
            df (pd.DataFrame): Le DataFrame contenant les données.
        
        Raises:
            ValueError: Si les colonnes requises sont absentes.
        """
        required_columns = ["co2", "pollution", "life_expectancy"]
        
        # Vérification défensive : on s'assure que les colonnes existent
        missing = [col for col in required_columns if col not in df.columns]
        if missing:
            raise ValueError(f"Le DataFrame manque les colonnes suivantes : {missing}")
            
        self.data = df

    def correlation_analysis(self) -> pd.DataFrame:
        """
        Calcule la matrice de corrélation entre les variables clés.

        Returns:
            pd.DataFrame: Une matrice de corrélation (3x3).
        """
        # On utilise self.data qui a été stocké dans __init__
        return self.data[["co2", "pollution", "life_expectancy"]].corr()

    def get_polluted_years(self, threshold: float = 50.0) -> pd.DataFrame:
        """
        Identifie les années où la pollution a dépassé un certain seuil.

        Args:
            threshold (float): Le seuil de pollution (par défaut 50.0).

        Returns:
            pd.DataFrame: Les lignes filtrées correspondant aux années critiques.
        """
        return self.data[self.data["pollution"] > threshold]