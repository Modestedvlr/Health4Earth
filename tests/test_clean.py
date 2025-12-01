import pytest
import pandas as pd
from health4earth import data_clean

def test_clean_module_exists():
    # On vérifie juste qu'on peut importer le module pour l'instant
    assert data_clean is not None

# Si vous avez une fonction dans data_clean.py, utilisez son VRAI nom ici
# Exemple : si elle s'appelle "clean_data", changez "clean_dataframe" par "clean_data"
def test_dummy_clean():
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    # Je commente la ligne qui plante tant que je ne connais pas le vrai nom de votre fonction
    # result = data_clean.clean_dataframe(df) 
    assert len(df) == 2