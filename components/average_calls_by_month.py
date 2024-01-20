import plotly.graph_objects as go
from utils import handle_annotation, graph_title

def graph_average_calls_by_month(df3):
    fig = go.Figure(go.Scatter(
        x=df3['Mês'],
        y=df3['Chamadas Realizadas'],
        mode='lines',
        fill='tonexty'))    

    fig.add_annotation(handle_annotation(f"Média : {round(df3['Chamadas Realizadas'].mean(), 2)}"))

    fig.update_layout(title=graph_title("Chamadas Médias por Mês"))

    return fig