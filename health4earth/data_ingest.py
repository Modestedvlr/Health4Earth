import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")

def download_datasets():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # CO2 (Our World in Data)
    co2_url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
    pd.read_csv(co2_url).to_csv(RAW_DIR / "co2.csv", index=False)

    # Pollution mortality (Our World in Data)
    pollution_url = "https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Air%20pollution%20mortality/air-pollution-mortality.csv"
    pd.read_csv(pollution_url).to_csv(RAW_DIR / "pollution.csv", index=False)

    # Life expectancy (Our World in Data)
    life_url = "https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Life%20expectancy%20(Clio-Infra)/life-expectancy.csv"
    pd.read_csv(life_url).to_csv(RAW_DIR / "life.csv", index=False)

    print("Datasets downloaded to data/raw/")
