#!/usr/bin/env python3
"""
scripts/predict_france.py

Charge website/data/all_series.json,
entraîne une régression linéaire (année -> valeur) pour chaque indicateur
présent pour la France (FRA) et prédit jusqu'à 2030.

Sortie : website/data/france_forecast.json et website/data/france_forecast.csv
"""
import json
from pathlib import Path
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

IN = Path("website/data/all_series.json")
OUT_JSON = Path("website/data/france_forecast.json")
OUT_CSV = Path("website/data/france_forecast.csv")

def fit_and_predict(series_dict, start_year=2024, end_year=2030):
    # series_dict: { "1990": v, "1991": v, ... }
    years = np.array(sorted([int(y) for y in series_dict.keys()]))
    vals = np.array([series_dict[str(y)] for y in years], dtype=float)
    X = years.reshape(-1, 1)
    y = vals
    model = LinearRegression()
    model.fit(X, y)
    future_years = np.arange(start_year, end_year+1)
    preds = model.predict(future_years.reshape(-1,1))
    return dict(zip([str(int(y)) for y in future_years], preds.tolist())), float(model.coef_[0]), float(model.intercept_)

def main():
    data = json.loads(IN.read_text(encoding="utf-8"))
    fra = data.get("FRA")
    if fra is None:
        raise ValueError("France (FRA) non trouvée dans all_series.json")
    series = fra.get("series", {})
    forecasts = {}
    rows = []
    for key, s in series.items():
        # s is dict year->value (e.g., s = {"2000": 3.2, ...})
        if not isinstance(s, dict) or len(s) < 5:
            continue
        pred_dict, slope, intercept = fit_and_predict(s, start_year=max(int(k) for k in s.keys())+1, end_year=2030)
        forecasts[key] = {"forecast": pred_dict, "slope": slope, "intercept": intercept}
        # rows for CSV: merge history + forecast
        for y, v in s.items():
            rows.append({"indicator": key, "year": int(y), "value": float(v), "type": "history"})
        for y, v in pred_dict.items():
            rows.append({"indicator": key, "year": int(y), "value": float(v), "type": "forecast"})

    OUT_JSON.write_text(json.dumps({"FRA": {"forecasts": forecasts}}, indent=2, ensure_ascii=False), encoding="utf-8")
    pd.DataFrame(rows).to_csv(OUT_CSV, index=False)
    print("France forecasts exported:", OUT_JSON, OUT_CSV)

if __name__ == "__main__":
    main()
