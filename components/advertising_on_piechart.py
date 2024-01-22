import plotly.graph_objects as go
from utils import graph_title

def graph_advertising_on_piechart(dataframe, theme):
    fig = go.Figure()
    
    fig.add_trace(go.Pie(labels=dataframe['Meio de Propaganda'], values=dataframe['Valor Pago'], hole=.7))
    
    if theme:
        fig.update_layout(template="plotly_dark")
        
    return fig