from main.components import menu, two_scatter_plots
from dash import html

def component():
    return html.Div(
        id="app-container",
        children=[
            menu(),
            two_scatter_plots()
        ]
    )
