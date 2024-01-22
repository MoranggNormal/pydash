import plotly.graph_objects as go
from utils import graph_title

def graph_indicators_total_earnings(dataframe):
    fig = go.Figure()
    fig.add_trace(go.Indicator(mode='number',
            title = {"text": f"<span style='font-size:150%'>Valor Total</span><br><span style='font-size:70%'>Em Reais</span><br>"},
            value = dataframe['Valor Pago'].sum(),
            number = {'prefix': "R$"}
    ))
    return fig