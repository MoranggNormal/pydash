import plotly.graph_objects as go
from utils import handle_annotation, graph_title

def graph_average_calls_by_month(dataframe):
    fig = go.Figure(go.Scatter(
        x=dataframe['Mês'],
        y=dataframe['Chamadas Realizadas'],
        mode='lines',
        fill='tonexty'))    

    fig.add_annotation(handle_annotation(f"Média : {round(dataframe['Chamadas Realizadas'].mean(), 2)}"))

    return fig