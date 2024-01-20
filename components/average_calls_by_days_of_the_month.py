import plotly.graph_objects as go
from utils import handle_annotation, graph_title

def graph_average_calls_by_days_of_the_month(df2):
    fig = go.Figure(go.Scatter(x=df2['Dia'], y=df2['Chamadas Realizadas'], mode='lines', fill='tonexty'))

    fig.add_annotation(handle_annotation(f"Média : {round(df2['Chamadas Realizadas'].mean(), 2)}"))

    fig.update_layout(title=graph_title("Chamadas médias por dia do mês"))

    return fig