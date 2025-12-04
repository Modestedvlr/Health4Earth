import pytest
from health4earth.data_ingest import load_merged_data

def test_ingest_merged_data():
    """
    Vérifie que le chargement fusionné fonctionne et renvoie les bonnes colonnes.
    """
    try:
        df = load_merged_data()
        
        # 1. Vérification structurelle
        assert df is not None
        assert not df.empty
        
        # 2. Vérification des colonnes critiques pour le projet
        expected_cols = ['country', 'year', 'co2', 'pollution_deaths', 'life_expectancy']
        for col in expected_cols:
            assert col in df.columns, f"La colonne {col} est manquante !"
            
        # 3. Vérification du contenu (types)
        # On s'assure que le CO2 est bien numérique
        assert df['co2'].dtype.kind in 'fi' # float ou int

    except Exception as e:
        pytest.fail(f"Le pipeline d'ingestion a échoué : {e}")