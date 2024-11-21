from main.plots import Scatterplot
from dash import html, callback, Output, Input
from main.dataset import df

scatterplot1 = Scatterplot("Scatterplot 1", 'sepal_length', 'sepal_width', df)
scatterplot2 = Scatterplot("Scatterplot 2", 'petal_length', 'petal_width', df)

def component():
    return html.Div(
        id="right-column",
        className="nine columns",
        children=[
            scatterplot1,
            scatterplot2
        ],
    )

@callback(
        Output(scatterplot1.html_id, "figure"), [
            Input("select-color-scatter-1", "value"),
            Input(scatterplot2.html_id, 'selectedData')
        ])
def update_scatter_1(selected_color, selected_data):
    return scatterplot1.update(selected_color, selected_data)

@callback(
    Output(scatterplot2.html_id, "figure"), [
        Input("select-color-scatter-2", "value"),
        Input(scatterplot1.html_id, 'selectedData')
    ])
def update_scatter_2(selected_color, selected_data):
    return scatterplot2.update(selected_color, selected_data)
