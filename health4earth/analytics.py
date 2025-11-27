import pandas as pd

def correlation_analysis(df: pd.DataFrame):
    """Calcule les corrélations entre CO2, pollution et espérance de vie."""
    return df[["co2", "pollution", "life_expectancy"]].corr()
