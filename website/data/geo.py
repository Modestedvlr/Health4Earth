import geopandas as gpd
from pathlib import Path

# Chemin vers le shapefile Natural Earth
shapefile = Path("data/raw/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp")

# Charger les données
world = gpd.read_file(shapefile)

# Garder uniquement les colonnes utiles
world = world[["ADMIN", "ISO_A3", "geometry"]]

# Exporter en GeoJSON
output = Path("website/data/world.geojson")
output.parent.mkdir(parents=True, exist_ok=True)
world.to_file(output, driver="GeoJSON")

print(f"world.geojson exporté vers {output}")
