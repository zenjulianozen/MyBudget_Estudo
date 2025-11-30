from dash import html, dcc, Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar

from app import app

layout = dbc.Col([
    dbc.Row([
        html.Legend("Tabela de Despesas"),
        html.Div(id='tabela-despesas', className='dbc')
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id="bar-graph", style={"margin-right": "20px"})
        ], width=9, style={"height": "100%"}),
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("R$ 4400,00", id="valor_despesa_card", style={"font-size": "60px"}),
                    html.H6("Total de Despesas")
                ], style={"text-align": "center", "padding-top": "30px"})
            )
        ], width=3)
    ])
], style={"margin": "10px"})