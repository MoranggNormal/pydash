import plotly.graph_objects as go
from utils import graph_title

def graph_top_consultants_plus_team_by_value_bar_chart(dataframe):
    fig = go.Figure(go.Bar(x=dataframe['Consultor'], y=dataframe['Valor Pago'], textposition='auto', text=dataframe['Valor Pago']))
    
    fig.update_layout(title=graph_title("Top Consultores por Equipe"))
    
    return fig