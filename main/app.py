from dash import Dash
from main.layout import component as layout
from dash_bootstrap_templates import load_figure_template

load_figure_template("darkly") # https://dash-bootstrap-components.opensource.faculty.ai/docs/themes

app = Dash(__name__) # Bootstrap js: external_scripts=[{'src': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js'}]
app.title = "JBI100 VIS - group 13"

app.layout = layout()
