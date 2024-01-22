import plotly.graph_objects as go
from utils import handle_annotation, graph_title

def graph_average_calls_by_days_of_the_month(dataframe, theme):
    fig = go.Figure(go.Scatter(x=dataframe['Dia'], y=dataframe['Chamadas Realizadas'], mode='lines', fill='tonexty'))

    fig.add_annotation(handle_annotation(f"Média : {round(dataframe['Chamadas Realizadas'].mean(), 2)}"))

    if theme:
        fig.update_layout(template="plotly_dark")
        
    return fig