import plotly.graph_objects as go
from utils import graph_title

def graph_team_sales(dataframe):
    fig = go.Figure(go.Bar(
        x=dataframe['Valor Pago'],
        y=dataframe['Equipe'],
        orientation='h',
        textposition='auto',
        text=dataframe['Valor Pago'],
        insidetextfont=dict(family='Times', size=12)
    ))
    
    fig.update_layout(title=graph_title("Vendas por equipe"))

    return fig