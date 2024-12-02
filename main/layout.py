from main.components import bubble_chart, heatmap, parallel_coordinates
from dash import html

def component():
    return html.Div(
        [
            html.Div(
                [
                    bubble_chart(),
                    heatmap()
                ],
                className="relative",
            ),
            html.Div(
                parallel_coordinates(),
                className="relative",
            )
        ]
)
