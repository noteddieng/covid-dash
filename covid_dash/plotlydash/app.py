import dash

from dash import dash_table
from dash import dcc 
from dash import html
from dash import Dash

from .data import create_dataframe
from .layout import html_layout


def create_dashboard(server):
    dash_app = dash.Dash(
        server=server, 
        routes_pathname_prefix='/dashapp/', 
        external_stylesheets=[
            '/static/dist/css/styles.css'
        ]
    )

    dash_app.layout = html.Div(id = 'dash-container')

    return dash_app.server


