import plotly.express as px

def plot_time_series(df, country):
    """Trace les séries CO2, pollution et espérance de vie pour un pays donné."""
    subset = df[df["country"] == country]
    fig = px.line(subset, x="year", y=["co2", "pollution", "life_expectancy"],
                  title=f"Indicateurs pour {country}")
    return fig
