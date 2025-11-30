from dash import html, dcc, Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar

from app import app

card_icon = {
    "color": "white",
    "textAlign": "center",
    "fontSize": 30,
    "margin": "auto"
}

layout = dbc.Col([
    dbc.Row([

        #Saldo Total
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Saldo"),
                    html.H5('R$5400,00', id="p-saldo-dashboards", style={}),
                ], style={'padding-left': "20px", "padding-top": "10px"}),
                dbc.Card([
                    html.Div(className='fa fa-university', style=card_icon),                   
                ], color="warning", style={"maxWidth": 75, "height": 100, "margin-left": "-10px"})
            ])
        ], width=4),

        #Saldo Receita
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Receita"),
                    html.H5('R$10000,00', id="p-receita-dashboards", style={}),
                ], style={'padding-left': "20px", "padding-top": "10px"}),
                dbc.Card([
                    html.Div(className='fa fa-smile-o', style=card_icon),                   
                ], color="success", style={"maxWidth": 75, "height": 100, "margin-left": "-10px"})
            ])
        ], width=4),

        #Saldo Despesa
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Despesa"),
                    html.H5('R$4600,00', id="p-despesa-dashboards", style={}),
                ], style={'padding-left': "20px", "padding-top": "10px"}),
                dbc.Card([
                    html.Div(className='fa fa-meh-o', style=card_icon),                   
                ], color="danger", style={"maxWidth": 75, "height": 100, "margin-left": "-10px"})
            ])
        ], width=4)
    ], style={"margin": "10px"}),


    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Legend("Filtrar Lançamentos", className="card-title"),
                html.Label("Categorias de Receitas"),
                html.Div(
                    dcc.Dropdown(
                        id="dropdown-receita",
                        clearable=False,
                        style={"width": "100%"},
                        persistence=True,
                        persistence_type="session",
                        multi=True
                    )
                ),

                html.Label("Categorias de Despesas", style={"margin-top": "10px"}),
                dcc.Dropdown(
                    id="dropdown-despesa",
                    clearable=False,
                    style={"width": "100%"},
                    persistence=True,
                    persistence_type="session",
                    multi=True
                ),

                html.Legend("Período de Análise", style={"margin-top": "10px"}),
                dcc.DatePickerRange(
                    month_format="Do MMM, YY",
                    end_date_placeholder_text="Data...",
                    start_date=datetime(2025, 11, 1).date(),
                    end_date=datetime.today() + timedelta(days=31),
                    updatemode="singledate",
                    id="date-picker-config",
                    style={'z-index': "100"}
                )
            ], style={'height': "100%", "padding": "20px"})
        ], width=4),

        dbc.Col([
            dbc.Card([
                dcc.Graph(id="graph1"),
            ], style={'height': "100%", "padding": "10px"})
        ], width=8)
    ], style={"margin": "10px"}),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dcc.Graph(id="graph2"),
            ], style={'height': "100%", "padding": "10px"})
        ], width=6),

        dbc.Col([
            dbc.Card([
                dcc.Graph(id="graph3"),
            ], style={'height': "100%", "padding": "10px"})
        ], width=3),

        dbc.Col([
            dbc.Card([
                dcc.Graph(id="graph3"),
            ], style={'height': "100%", "padding": "10px"})
        ], width=3)
    ], style={"margin": "10px"})
])