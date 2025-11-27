import pandas as pd

def add_capitals(df: pd.DataFrame, capitals: pd.DataFrame) -> pd.DataFrame:
    """Ajoute les capitales et coordonnées géographiques au dataset principal."""
    return df.merge(capitals, on="country", how="left")
