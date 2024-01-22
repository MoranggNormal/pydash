from utils import graph_title
import plotly.express as px

def graph_amounts_paid_through_advertising(dataframe):
    fig = px.line(dataframe, y="Valor Pago", x="Mês", color="Meio de Propaganda")
    
    return fig