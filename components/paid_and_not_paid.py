import plotly.graph_objects as go
from utils import graph_title

def graph_paid_and_not_paid(dataframe, theme):
    fig = go.Figure()
    
    fig.add_trace(go.Pie(labels=['Não Pago', 'Pago'], values=dataframe, hole=.6))
    fig.update_layout(title=graph_title("Pagos e não pagos"))
    
    if theme:
        fig.update_layout(template="plotly_dark")
        
    return fig