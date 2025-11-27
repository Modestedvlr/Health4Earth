import pandas as pd
from health4earth import data_clean

def test_clean_dataframe():
    df = pd.DataFrame({"A": [1, None, 3]})
    cleaned = data_clean.clean_dataframe(df)
    assert cleaned.isna().sum().sum() == 0
