import pytest
from health4earth.data_ingest import load_co2_data

# On marque ce test comme "slow" ou "web" car il utilise internet
# (C'est optionnel, mais c'est une bonne pratique)
def test_load_co2_returns_dataframe():
    """Vérifie que le téléchargement et le chargement renvoient bien un DataFrame."""
    try:
        df = load_co2_data()
        
        # Vérifications de base
        assert df is not None
        assert not df.empty
        assert "country" in df.columns
        assert "year" in df.columns
        assert "co2" in df.columns
        
    except Exception as e:
        pytest.fail(f"Le téléchargement a échoué : {e}")