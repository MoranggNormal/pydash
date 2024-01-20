import plotly.graph_objects as go
from utils import graph_title

def graph_top_consultants_plus_team_by_value(dataframe):
    fig = go.Figure(go.Pie(labels=dataframe['Consultor'] + ' - ' + dataframe['Equipe'], values=dataframe['Valor Pago'], hole=.6))
    
    fig.update_layout(title=graph_title("Top Consultant per Equipa e seus valores de venda"))
    
    return fig