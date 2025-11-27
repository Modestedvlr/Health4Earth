import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie un DataFrame : supprime les NA et harmonise les colonnes."""
    df = df.dropna()
    df.columns = [c.strip().lower() for c in df.columns]
    return df
