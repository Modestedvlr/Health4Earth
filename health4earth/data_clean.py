import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
PROC_DIR = Path("data/processed")

def clean_co2():
    df = pd.read_csv(RAW_DIR / "co2.csv")
    df = df[["iso_code", "country", "year", "co2_per_capita"]].dropna(subset=["iso_code"])
    df.to_csv(PROC_DIR / "co2_clean.csv", index=False)

def clean_pollution():
    df = pd.read_csv(RAW_DIR / "pollution.csv")
    df = df[["Entity", "Year", "Air pollution (total deaths per 100,000)"]]
    df = df.rename(columns={"Entity": "country", "Year": "year", "Air pollution (total deaths per 100,000)": "pollution_deaths"})
    df.to_csv(PROC_DIR / "pollution_clean.csv", index=False)

def clean_life():
    df = pd.read_csv(RAW_DIR / "life.csv")
    df = df[["Entity", "Year", "Life expectancy (years)"]]
    df = df.rename(columns={"Entity": "country", "Year": "year", "Life expectancy (years)": "life_expectancy"})
    df.to_csv(PROC_DIR / "life_clean.csv", index=False)

if __name__ == "__main__":
    PROC_DIR.mkdir(parents=True, exist_ok=True)
    clean_co2()
    clean_pollution()
    clean_life()
    print("Cleaned datasets saved to data/processed/")
