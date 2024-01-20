import plotly.graph_objects as go
from utils import graph_title

def graph_team_sales(df1):
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