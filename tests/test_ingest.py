from health4earth import data_ingest
from pathlib import Path

def test_load_co2_data():
    path = Path("data/raw/co2.csv")
    assert path.exists(), "Le fichier co2.csv doit exister"
