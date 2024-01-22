import plotly.graph_objects as go
from utils import graph_title

def graph_indicators_total_calls(dataframe, theme):
        fig = go.Figure()
        
        fig.add_trace(go.Indicator(mode='number',
                title = {"text": f"<span style='font-size:150%'>Chamadas Realizadas</span>"},
                value = len(dataframe[dataframe['Status de Pagamento'] == 1])
        ))
        fig.update_layout(title=graph_title("Indicators - Total de Chamadas"))
        
        if theme:
                fig.update_layout(template="plotly_dark")
        
        return fig