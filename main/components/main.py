from main.components.menu import component as menu
from main.components.two_scatter_plots import component as two_scatter_plots
from dash import html

def component():
    return html.Div(
        id="app-container",
        children=[
            menu(),
            two_scatter_plots()
        ]
    )
