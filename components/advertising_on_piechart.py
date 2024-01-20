import plotly.graph_objects as go
from utils import graph_title

def graph_advertising_on_piechart(dataframe):
    fig = go.Figure()
    
    fig.add_trace(go.Pie(labels=dataframe['Meio de Propaganda'], values=dataframe['Valor Pago'], hole=.7))
    fig.update_layout(title=graph_title("Propaganda em PieChart"))
    
    return fig