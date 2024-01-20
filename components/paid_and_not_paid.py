import plotly.graph_objects as go
from utils import graph_title

def graph_paid_and_not_paid(dataframe):
    fig = go.Figure()
    
    fig.add_trace(go.Pie(labels=['Não Pago', 'Pago'], values=dataframe, hole=.6))
    fig.update_layout(title=graph_title("Pagos e não pagos"))
    
    return fig