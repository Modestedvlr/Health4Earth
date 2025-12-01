import pandas as pd
import pytest
from health4earth.analytics import HealthAnalyzer

# Création de données fictives pour les tests
@pytest.fixture
def fake_df():
    return pd.DataFrame({
        "year": [2020, 2021, 2022],
        "co2": [100, 110, 105],
        "pollution": [40, 60, 45],
        "life_expectancy": [80, 79, 81]
    })

def test_analyzer_init(fake_df):
    """Test si la classe s'initialise bien."""
    analyzer = HealthAnalyzer(fake_df)
    assert analyzer.data is not None

def test_correlation(fake_df):
    """Test du calcul de corrélation."""
    analyzer = HealthAnalyzer(fake_df)
    corr_matrix = analyzer.correlation_analysis()
    
    # La matrice doit être de taille 3x3
    assert corr_matrix.shape == (3, 3)
    # La diagonale d'une corrélation est toujours égale à 1.0
    assert corr_matrix.iloc[0, 0] == 1.0

def test_missing_columns():
    """Test si l'erreur est bien levée quand il manque des colonnes."""
    bad_df = pd.DataFrame({"co2": [1, 2]}) # Manque pollution et life_expectancy
    
    with pytest.raises(ValueError):
        HealthAnalyzer(bad_df)