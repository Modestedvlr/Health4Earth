#!/usr/bin/env python3
"""
scripts/build_all_series.py

But : lire les CSV bruts dans data/raw/ et produire website/data/all_series.json
Format de sortie (extrait) :
{
  "FRA": {
    "country": "France",
    "capital": "Paris",
    "lat": 48.8566,
    "lon": 2.3522,
    "series": {
       "co2": {"2000": 3.2, "2001": 3.4, ...},
       "pollution": {"2000": 12.3, ...},
       "life": {"2000": 78.2, ...},
       "mortality": {"2000": 10.2, ...}
    }
  },
  ...
}
"""
from pathlib import Path
import pandas as pd
import json
import pycountry
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

RAW = Path("data/raw")
OUT = Path("website/data")
OUT.mkdir(parents=True, exist_ok=True)

def to_iso3(name):
    """Try to map a country name to ISO3 using pycountry (with fuzzy fallback)."""
    if not isinstance(name, str) or name.strip() == "":
        return None
    try:
        return pycountry.countries.lookup(name).alpha_3
    except Exception:
        try:
            # fuzzy
            res = pycountry.countries.search_fuzzy(name)
            if res:
                return res[0].alpha_3
        except Exception:
            return None
    return None

def build_co2():
    f = RAW / "owid-co2-data.csv"
    if not f.exists():
        print("⚠️ owid-co2-data.csv absent:", f)
        return {}
    df = pd.read_csv(f, low_memory=False)
    # ensure iso_code column exists
    if "iso_code" not in df.columns:
        # try lowercase
        df.columns = df.columns.str.lower()
    df = df.rename(columns=lambda c: c.strip())
    if "iso_code" not in df.columns:
        print("⚠️ owid-co2: pas de colonne iso_code")
        return {}

    # keep rows with 3-char iso
    df = df[df["iso_code"].astype(str).str.len() == 3]
    df = df[["iso_code", "year", "co2"]].dropna(subset=["co2"])
    df["year"] = df["year"].astype(int)
    out = {}
    for iso, group in df.groupby("iso_code"):
        series = {str(int(r.year)): float(r.co2) for r in group.itertuples()}
        out[iso] = {"co2": series}
    print("co2 countries:", len(out))
    return out

def build_life():
    f = RAW / "WHO_life_expectancy.csv"
    if not f.exists():
        print("⚠️ WHO_life_expectancy.csv absent:", f)
        return {}
    df = pd.read_csv(f, low_memory=False)
    # find life column (may contain trailing space)
    cols = [c for c in df.columns]
    # heuristique pour la colonne life
    life_col = None
    for c in cols:
        if c.strip().lower().startswith("life"):
            life_col = c
            break
    if life_col is None:
        print("⚠️ impossible de trouver colonne espérance de vie dans WHO_life_expectancy.csv")
        return {}

    # unify
    df = df.rename(columns={life_col: "life", "Country": "country", "Year": "year"})
    if "year" not in df.columns:
        # try lowercase
        df.columns = df.columns.str.strip()
        df = df.rename(columns={c: c.strip() for c in df.columns})
    out = {}
    # convert years
    df = df.dropna(subset=["country", "year", "life"])
    df["year"] = df["year"].astype(int)
    for country, g in df.groupby("country"):
        iso = to_iso3(country)
        if iso is None:
            # skip or log
            # try to match with a direct name mapping (some names require manual)
            # we'll skip for now
            # print("no iso for", country)
            continue
        series = {str(int(r.year)): float(r.life) for r in g.itertuples()}
        out.setdefault(iso, {})["life"] = series
    print("life countries:", len(out))
    return out

def build_pollution():
    f = RAW / "WHO_air_pollution_mortality.csv"
    if not f.exists():
        print("⚠️ WHO_air_pollution_mortality.csv absent:", f)
        return {}
    df = pd.read_csv(f, low_memory=False)
    # We observed SpatialDimValueCode = ISO, Period = year, FactValueNumeric = numeric value
    cols = [c for c in df.columns]
    # standardize names
    rename_map = {}
    if "SpatialDimValueCode" in df.columns:
        rename_map["SpatialDimValueCode"] = "iso"
    elif "SpatialDimValueCode".lower() in [c.lower() for c in df.columns]:
        # handle different casings
        for c in df.columns:
            if c.lower() == "spatialdimvaluecode":
                rename_map[c] = "iso"
    if "Period" in df.columns:
        rename_map["Period"] = "year"
    if "FactValueNumeric" in df.columns:
        rename_map["FactValueNumeric"] = "value"
    if "Value" in df.columns and "FactValueNumeric" not in df.columns:
        rename_map["Value"] = "value"  # fallback

    df = df.rename(columns=rename_map)
    if "iso" not in df.columns:
        # maybe ISO is in SpatialDimValueCode with different name - try 'SpatialDimValueCode'
        possible = [c for c in df.columns if c.lower().startswith("spatial")]
        if possible:
            df = df.rename(columns={possible[0]: "iso"})

    if "value" not in df.columns:
        # try FactValueNumeric
        possible = [c for c in df.columns if c.lower().startswith("factvaluenumeric")]
        if possible:
            df = df.rename(columns={possible[0]: "value"})

    if "iso" not in df.columns or "year" not in df.columns or "value" not in df.columns:
        print("⚠️ colonnes attendues manquantes dans WHO_air_pollution_mortality.csv:", df.columns)
        return {}

    # Option: keep only both sexes to avoid duplicates
    if "Dim1" in df.columns:
        try:
            df = df[df["Dim1"].str.contains("Both", na=False)]
        except Exception:
            pass

    df = df.dropna(subset=["iso", "year", "value"])
    df["year"] = df["year"].astype(int)
    out = {}
    for iso, g in df.groupby("iso"):
        series = {str(int(r.year)): float(r.value) for r in g.itertuples()}
        out.setdefault(iso, {})["pollution"] = series
    print("pollution countries:", len(out))
    return out

def build_capitals():
    f = RAW / "capitales.csv"
    if not f.exists():
        print("⚠️ capitales.csv absent:", f)
        return {}
    df = pd.read_csv(f, low_memory=False)
    # expected columns: city,country,latitude,longitude
    candidates = [c.strip().lower() for c in df.columns]
    colmap = {}
    for c in df.columns:
        lc = c.strip().lower()
        if lc in ["city", "ville", "capital"]:
            colmap[c] = "city"
        if lc in ["country", "pays"]:
            colmap[c] = "country"
        if "lat" in lc:
            colmap[c] = "lat"
        if "long" in lc or "lon" in lc:
            colmap[c] = "lon"
    df = df.rename(columns=colmap)
    if not all(k in df.columns for k in ["city", "country", "lat", "lon"]):
        print("⚠️ capitales.csv attendus: city,country,lat,lon  ; colonnes trouvées:", df.columns)
        # still try to proceed by guessing
    out = {}
    for r in df.itertuples():
        country_name = getattr(r, "country", None)
        iso = to_iso3(country_name) if country_name else None
        if iso is None:
            # try to match by exact country string in pycountry
            try:
                iso = pycountry.countries.search_fuzzy(country_name)[0].alpha_3
            except Exception:
                iso = None
        if iso is None:
            continue
        try:
            lat = float(getattr(r, "lat"))
            lon = float(getattr(r, "lon"))
        except Exception:
            lat = None; lon = None
        city = getattr(r, "city", None)
        out[iso] = {"capital": city, "lat": lat, "lon": lon, "country_name": country_name}
    print("capitals countries:", len(out))
    return out

def merge_all(co2, life, pollution, capitals):
    all_keys = set()
    for d in (co2, life, pollution, capitals):
        all_keys |= set(d.keys())
    result = {}
    for iso in sorted(all_keys):
        entry = {}
        # prefer a country name from capitals or from co2 file if present
        country_name = None
        if iso in capitals and capitals[iso].get("country_name"):
            country_name = capitals[iso]["country_name"]
        # else try to infer from pycountry
        try:
            country_name = country_name or pycountry.countries.get(alpha_3=iso).name
        except Exception:
            pass
        entry["country"] = country_name
        # capital
        if iso in capitals:
            entry["capital"] = capitals[iso].get("capital")
            entry["lat"] = capitals[iso].get("lat")
            entry["lon"] = capitals[iso].get("lon")
        else:
            entry["capital"] = None
            entry["lat"] = None
            entry["lon"] = None

        # series
        s = {}
        if iso in co2:
            s["co2"] = co2[iso]["co2"]
        if iso in pollution:
            s["pollution"] = pollution[iso]["pollution"]
        if iso in life:
            s["life"] = life[iso]["life"]
        # mortality could be from pollution dataset or gbd if needed; keep as 'mortality' if available
        # for now we use pollution dataset as mortality metric if named 'pollution' -> keep both
        result[iso] = {"country": entry["country"], "capital": entry["capital"], "lat": entry["lat"], "lon": entry["lon"], "series": s}
    return result

def main():
    co2 = build_co2()
    life = build_life()
    pollution = build_pollution()
    caps = build_capitals()
    merged = merge_all(co2, life, pollution, caps)
    # write out
    out_file = OUT / "all_series.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)
    print("✅ all_series.json written:", out_file)
    print("Total countries:", len(merged))

if __name__ == "__main__":
    main()
