import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class HealthAnalyzer:
    """
    Moteur d'analyse statistique et prédictive du projet Health4Earth.
    
    Cette classe encapsule la logique métier et les algorithmes de Machine Learning.
    Elle suit le paradigme de Programmation Orientée Objet (POO).
    
    Attributes:
        data (pd.DataFrame): Le jeu de données complet chargé en mémoire.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Initialise l'analyseur.
        
        Args:
            df (pd.DataFrame): Le DataFrame issu de `load_merged_data`.
        """
        self.data = df.sort_values('year')

    def predict_evolution(self, country: str, target_col: str, year_horizon: int = 2030):
        """
        Prédit l'évolution future d'un indicateur jusqu'à une année donnée.
        
        Méthodologie :
            Utilise une **Régression Linéaire** (Scikit-Learn) entraînée sur les 
            20 dernières années de données disponibles pour projeter la tendance.
        
        Args:
            country (str): Le pays cible (ex: 'France').
            target_col (str): La variable à prédire ('co2', 'life_expectancy').
            year_horizon (int): L'année cible de la prédiction (défaut 2030).
            
        Returns:
            pd.DataFrame: Un tableau contenant l'historique réel et les années prédites.
            Retourne None si les données sont insuffisantes.
        """
        df_country = self.data[self.data['country'] == country].copy()
        df_recent = df_country[df_country['year'] >= 2000].dropna(subset=[target_col])
        
        if len(df_recent) < 5:
            return None 

        X = df_recent[['year']].values
        y = df_recent[target_col].values
        
        model = LinearRegression()
        model.fit(X, y)

        future_years = np.arange(df_country['year'].max() + 1, year_horizon + 1).reshape(-1, 1)
        future_preds = model.predict(future_years)
        
        df_future = pd.DataFrame({
            'year': future_years.flatten(),
            target_col: future_preds,
            'type': 'Prédiction',
            'country': country
        })
        
        df_history = df_country[['year', target_col]].copy()
        df_history['type'] = 'Historique'
        df_history['country'] = country
        
        return pd.concat([df_history, df_future])