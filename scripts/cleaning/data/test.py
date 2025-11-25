import plotly.express as px
import pandas as pd
df_map = pd.read_csv("data/clean/health4earth_cities.csv")

fig = px.scatter_geo(df_map, lat='latitude', lon='longitude', hover_name='city',
                     size='co2',  # taille du marker selon CO2 par exemple
                     projection="natural earth")
fig.show()

