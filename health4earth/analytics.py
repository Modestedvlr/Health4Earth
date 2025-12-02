import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class HealthAnalyzer:
    """
    Moteur d'analyse pour Health4Earth.
    Permet l'extraction de statistiques et la prédiction ML.
    """

    def __init__(self, df: pd.DataFrame):
        self.data = df.sort_values('year')

    def get_country_data(self, country: str) -> pd.DataFrame:
        """Retourne les données d'un pays spécifique."""
        return self.data[self.data['country'] == country].copy()

    def predict_evolution(self, country: str, target_col: str, year_horizon: int = 2030):
        """
        Prédit l'évolution d'une variable jusqu'à l'année horizon.
        Utilise une Régression Linéaire sur les 20 dernières années.
        
        Args:
            country (str): Nom du pays (ex: 'France').
            target_col (str): Colonne à prédire ('co2', 'pollution_deaths', 'life_expectancy').
            year_horizon (int): Année cible (défaut 2030).
            
        Returns:
            pd.DataFrame: DataFrame contenant historique + prédictions.
        """
        df_country = self.get_country_data(country).dropna(subset=[target_col])
        
        # On ne garde que les données récentes pour la tendance (ex: depuis 2000)
        df_recent = df_country[df_country['year'] >= 2000]
        
        if len(df_recent) < 5:
            return None # Pas assez de données fiables

        # Machine Learning (Scikit-Learn)
        X = df_recent[['year']].values
        y = df_recent[target_col].values
        
        model = LinearRegression()
        model.fit(X, y)

        # Génération des années futures
        last_year = int(df_country['year'].max())
        future_years = np.arange(last_year + 1, year_horizon + 1).reshape(-1, 1)
        future_preds = model.predict(future_years)
        
        # Création du DataFrame de résultat
        df_future = pd.DataFrame({
            'year': future_years.flatten(),
            target_col: future_preds,
            'type': 'Prédiction'
        })
        
        # On ajoute le pays pour faciliter l'affichage
        df_future['country'] = country
        
        # On combine avec l'historique
        df_history = df_country[['year', target_col]].copy()
        df_history['type'] = 'Historique'
        df_history['country'] = country
        
        return pd.concat([df_history, df_future])