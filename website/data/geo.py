import geopandas as gpd
from pathlib import Path

# Chemin vers le shapefile téléchargé
shapefile = Path("data/raw/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp")

# Charger avec GeoPandas
world = gpd.read_file(shapefile)

# Sauvegarder en GeoJSON
output = Path("website/data/world.geojson")
world.to_file(output, driver="GeoJSON")

print(f"GeoJSON exporté vers {output}")