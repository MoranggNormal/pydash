import plotly.graph_objects as go
from utils import graph_title

def graph_indicators_best_equip(dataframe, theme):
    fig = go.Figure()
    
    fig.add_trace(go.Indicator(mode='number+delta',
            title = {"text": f"<span style='font-size:150%'>{dataframe['Equipe'].iloc[0]} - Top Team</span><br><span style='font-size:70%'>Em vendas - em relação a média</span><br>"},
            value = dataframe['Valor Pago'].iloc[0],
            number = {'prefix': "R$"},
            delta = {'relative': True, 'valueformat': '.1%', 'reference': dataframe['Valor Pago'].mean()}
    ))

    if theme:
        fig.update_layout(template="plotly_dark")
         
    return fig
