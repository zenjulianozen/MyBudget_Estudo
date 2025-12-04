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

graph_margin = dict(l=25, r=25, t=25, b=0)

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

#Receitas
@app.callback(
    [Output("dropdown-receita", "options"),
     Output('dropdown-receita', "value"),
     Output("p-receita-dashboards", "children")],
     [Input("store-receitas", "data")])

def populate_dropdownvalues(data):
    #import pdb
    #pdb.set_trace()

    df =pd.DataFrame(data)
    valor = df["Valor"].sum()
    val = df.Categoria.unique().tolist()

    return ([{"label": x, "value": x} for x in val], val, f"R${valor}")

#Despesas
@app.callback(
    [Output("dropdown-despesa", "options"),
     Output('dropdown-despesa', "value"),
     Output("p-despesa-dashboards", "children")],
     [Input("store-despesas", "data")]
)

def populate_dropdownvalues(data):
    #import pdb
    #pdb.set_trace()

    df =pd.DataFrame(data)
    valor = df["Valor"].sum()
    val = df.Categoria.unique().tolist()

    return ([{"label": x, "value": x} for x in val], val, f"R${valor}")

#Saldo
@app.callback(
    Output("p-saldo-dashboards", "children"),
    [Input("store-despesas", "data"),
     Input("store-receitas", "data")]
)

def saldo_total(despesas, receitas):
    df_receitas = pd.DataFrame(receitas)
    df_despesas = pd.DataFrame(despesas)

    valor = df_receitas["Valor"].sum() - df_despesas["Valor"].sum()

    return f"R${valor}"


#Filtros
@app.callback(
    Output("graph1", "figure"),
    [Input('store-despesas', 'data'),
     Input('store-receitas', 'data'),
     Input('dropdown-despesa', 'value'),
     Input('dropdown-receita', 'value')])

def update_output(data_despesa, data_receita, despesa, receita):
    # import pdb
    # pdb.set_trace()

    df_despesas = pd.DataFrame(data_despesa).set_index("Data")[["Valor"]]
    df_ds = df_despesas.groupby("Data").sum().rename(columns={"Valor": "Despesa"})

    df_receitas = pd.DataFrame(data_receita).set_index("Data")[["Valor"]]
    df_rc = df_receitas.groupby("Data").sum().rename(columns={"Valor": "Receita"})

    df_acum = df_ds.join(df_rc, how="outer").fillna(0)
    df_acum["Acum"] = df_acum["Receita"] - df_acum["Despesa"]
    df_acum["Acum"] = df_acum["Acum"].cumsum()
    

    fig=go.Figure()
    fig.add_trace(go.Scatter(name="Fluxo de Caixa", x=df_acum.index, y=df_acum["Acum"], mode="lines"))

    fig.update_layout(margin=graph_margin)
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    fig.update_xaxes(tickformat="%d/%m/%Y")


    return fig
