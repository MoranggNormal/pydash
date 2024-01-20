import os

import pandas as pd
import plotly.graph_objects as go
from dash import Dash, html, dcc, callback, Output, Input

from utils import parse_data, graph_title

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
        
df1, df2 = parse_data(df)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Python Dash', style={'textAlign':'center'}),
    dcc.Graph(id='team-sales'),
    
    dcc.Graph(id='average_calls_by_days_of_the_month')
])

@callback(Output('team-sales', 'figure'),Input('team-sales', 'clickAnnotationData'))
def update_graph(clickAnnotationData):
    fig = go.Figure(go.Bar(
        x=df1['Valor Pago'],
        y=df1['Equipe'],
        orientation='h',
        textposition='auto',
        text=df1['Valor Pago'],
        insidetextfont=dict(family='Times', size=12)
    ))
    
    fig.update_layout(title=graph_title("Vendas por equipe"))

    return fig

@callback(Output('average_calls_by_days_of_the_month', 'figure'), Input('average_calls_by_days_of_the_month', 'clickAnnotationData'))
def update_graph(clickAnnotationData):
    fig = go.Figure(go.Scatter(x=df2['Dia'], y=df2['Chamadas Realizadas'], mode='lines', fill='tonexty'))
    
    fig.add_annotation(text=f"Média : {round(df2['Chamadas Realizadas'].mean(), 2)}",
        xref="paper", yref="paper",
        font=dict(
            size=30,
            color='gray'
            ),
        align="center", bgcolor="rgba(0,0,0,0.8)",
        x=0.025, y=0.90, showarrow=False)
    
    fig.update_layout(title=graph_title("Chamadas médias por dia do mês"))
    
    return fig


server = app.server

if __name__ == '__main__':
    app.run_server(debug=os.getenv("DEBUG", False))