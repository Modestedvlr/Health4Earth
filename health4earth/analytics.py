import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class HealthAnalyzer:
    """
    Moteur d'analyse statistique et prédictive Health4Earth.
    Gère les régressions linéaires pour les projections 2025-2050.
    """

    def __init__(self, df: pd.DataFrame):
        self.data = df.sort_values('year')

    def get_country_data(self, country: str) -> pd.DataFrame:
        """Extrait les données spécifiques à un pays."""
        return self.data[self.data['country'] == country].copy()

    def predict_evolution(self, country: str, target_col: str, year_start_pred=2024, year_end=2050):
        """
        Prédit l'évolution future d'un indicateur.
        Utilise les données depuis 2000 pour entraîner le modèle.
        """
        df_country = self.get_country_data(country)
        # On entraîne sur les 20 dernières années pour avoir une tendance récente
        df_train = df_country[df_country['year'] >= 2000].dropna(subset=[target_col])
        
        if len(df_train) < 5:
            return None 

        # Machine Learning
        X = df_train[['year']].values
        y = df_train[target_col].values
        
        model = LinearRegression()
        model.fit(X, y)

        # Génération des années futures (de maintenant à 2050)
        future_years = np.arange(year_start_pred, year_end + 1).reshape(-1, 1)
        future_preds = model.predict(future_years)
        
        # DataFrame Prédiction
        df_future = pd.DataFrame({
            'year': future_years.flatten(),
            target_col: future_preds,
            'type': 'Prédiction',
            'country': country
        })
        
        # DataFrame Historique (pour l'affichage complet)
        df_history = df_country[['year', target_col]].copy()
        df_history['type'] = 'Historique'
        df_history['country'] = country
        
        return pd.concat([df_history, df_future])