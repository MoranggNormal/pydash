import os

import pandas as pd
import plotly.graph_objects as go
from dash import Dash, html, dcc, callback, Output, Input

from components.average_calls_by_month import graph_average_calls_by_month
from components.average_calls_by_days_of_the_month import graph_average_calls_by_days_of_the_month
from components.team_sales import graph_team_sales

from utils import parse_data

main_config = {
    "hovermode": "x unified",
    "legend": {"yanchor":"top", 
                "y":0.9, 
                "xanchor":"left",
                "x":0.1,
                "title": {"text": None},
                "font" :{"color":"white"},
                "bgcolor": "rgba(0,0,0,0.5)"},
    "margin": {"l":0, "r":0, "t":20, "b":0}
}

df = pd.read_csv('dataset_vendas.csv')
        
parsed_data = parse_data(df)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Python Dash', style={'textAlign':'center'}),
    dcc.Graph(id='team_sales'),
    dcc.Graph(id='average_calls_by_days_of_the_month'),
    dcc.Graph(id='average_calls_by_month')
])

@callback(Output('team_sales', 'figure'),Input('team_sales', 'clickAnnotationData'))
def update_graph(clickAnnotationData):
    data = parsed_data.groupby('Equipe')['Valor Pago'].sum().reset_index()
    return graph_team_sales(data)

@callback(Output('average_calls_by_days_of_the_month', 'figure'), Input('average_calls_by_days_of_the_month', 'clickAnnotationData'))
def update_graph(clickAnnotationData):
    data = parsed_data.groupby('Dia')['Chamadas Realizadas'].sum().reset_index()
    return graph_average_calls_by_days_of_the_month(data)

@callback(Output('average_calls_by_month', 'figure'), Input('average_calls_by_month', 'clickAnnotationData'))
def update_graph_average_calls_by_month(clickAnnotationData):
    data = parsed_data.groupby('Mês')['Chamadas Realizadas'].sum().reset_index()
    return graph_average_calls_by_month(data)

server = app.server

if __name__ == '__main__':
    app.run_server(debug=os.getenv("DEBUG", False))