import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *
from globals import *
from components import sidebar
from components import extratos
from components import dashboards



#Layout
content = html.Div(id="page-content")

app.layout = dbc.Container(children = [
    dcc.Store(id="store-receitas", data=df_receitas.to_dict()),
    dcc.Store(id="store-despesas", data=df_despesas.to_dict()),
    dcc.Store(id="stored-cat-receitas", data=df_cat_receita.to_dict()),
    dcc.Store(id="stored-cat-despesas", data=df_cat_despesa.to_dict()),


    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            sidebar.layout
        ], md=2),
        dbc.Col([
            content
        ], md=10)
    ])

], fluid=True)

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')])

def render_page(pathname):
    if pathname == '/' or pathname == '/dashboards':
        return dashboards.layout
    if pathname == '/extratos':
        return extratos.layout

if __name__ == '__main__':
    app.run(port="8051", debug=True)