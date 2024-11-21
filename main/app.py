from dash import Dash
from main.components import main

app = Dash(__name__)
app.title = "JBI100 VIS - group 13"

app.layout = main()
