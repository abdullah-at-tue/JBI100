import plotly.express as px
from dash import html, dcc
from main.dataset import df

def component():
    if df.empty:
        return html.Div("No data to display on the map.", className="alert alert-warning")

    df_normalized = df.groupby(['lat', 'lng']).size().reset_index(name='occurrence')

    fig = px.density_mapbox(
        df_normalized,
        lat="lat",
        lon="lng",
        z="occurrence",
        radius=15,
        zoom=3,
        mapbox_style="carto-darkmatter",
        center={"lat": 37.0902, "lon": -95.7129},
        opacity=0.6
    )

    fig.update_traces(
        hovertemplate=(
            "Latitude: %{lat}<br>"
            "Longitude: %{lon}<br>"
            "Occurrences: %{z}<br>"
        ),
        customdata=df_normalized[['lat', 'lng', 'occurrence']],
    )

    fig.update_layout(
        margin={"l": 0, "r": 0, "b": 0, "t": 0},
        mapbox=dict(
            bearing=0,
            pitch=0,
            zoom=3,
            # dragmode='select'
        ),
        autosize=True,  # Ensure map fills the container
        coloraxis_colorbar=dict(
            x=0.9,
            y=0.5,
            thickness=10,
            lenmode="fraction",
            len=0.8,
            title="Occurrences",
            title_font=dict(color="white"),
            tickfont=dict(color="white")
        ),
    )

    return dcc.Graph(
        id="heatmap",
        figure=fig,
        style={"width": "50vw"},
    )

