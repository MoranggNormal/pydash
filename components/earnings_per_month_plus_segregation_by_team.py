import plotly.graph_objects as go
from utils import graph_title
import plotly.express as px

def graph_earnings_per_month_plus_segregation_by_team(df5, df5_group):
    fig = px.line(df5, y="Valor Pago", x="Mês", color="Equipe")
    
    fig.add_trace(go.Scatter(y=df5_group["Valor Pago"], x=df5_group["Mês"], mode='lines+markers', fill='tonexty', fillcolor='rgba(255, 0, 0, 0.2)', name='Total de Vendas'))
    
    return fig