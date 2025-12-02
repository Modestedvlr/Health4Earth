import pandas as pd
import pytest
from health4earth.analytics import HealthAnalyzer

@pytest.fixture
def fake_df():
    """Crée un petit DataFrame fictif pour tester la logique sans internet."""
    return pd.DataFrame({
        "country": ["France"] * 10 + ["USA"] * 10,
        "year": list(range(2000, 2010)) * 2,
        "co2": [100 + i for i in range(10)] + [500 + i*2 for i in range(10)],
        "pollution_deaths": [50 - i for i in range(10)] + [100 - i for i in range(10)],
        "life_expectancy": [80 + i*0.1 for i in range(10)] + [78 + i*0.1 for i in range(10)]
    })

def test_analyzer_init(fake_df):
    analyzer = HealthAnalyzer(fake_df)
    assert analyzer.data is not None

def test_get_country_data(fake_df):
    analyzer = HealthAnalyzer(fake_df)
    df_fr = analyzer.get_country_data("France")
    assert len(df_fr) == 10
    assert df_fr['country'].unique()[0] == "France"

def test_prediction_structure(fake_df):
    """Teste si la prédiction renvoie bien le format attendu."""
    analyzer = HealthAnalyzer(fake_df)
    
    # On demande une prédiction jusqu'en 2015 (nos données s'arrêtent en 2009)
    df_pred = analyzer.predict_evolution("France", "co2", year_horizon=2015)
    
    assert df_pred is not None
    assert "type" in df_pred.columns
    assert "Prédiction" in df_pred["type"].unique()
    assert df_pred["year"].max() == 2015