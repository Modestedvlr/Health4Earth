import pandas as pd

def merge_datasets(co2: pd.DataFrame, pollution: pd.DataFrame, life: pd.DataFrame) -> pd.DataFrame:
    """Fusionne les trois datasets sur country et year."""
    df = co2.merge(pollution, on=["country", "year"], how="inner")
    df = df.merge(life, on=["country", "year"], how="inner")
    return df
