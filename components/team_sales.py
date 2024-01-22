import plotly.graph_objects as go

def graph_team_sales(dataframe, theme):
    fig = go.Figure(go.Bar(
        x=dataframe['Valor Pago'],
        y=dataframe['Equipe'],
        orientation='h',
        textposition='auto',
        text=dataframe['Valor Pago'],
        insidetextfont=dict(family='Times', size=12)
    ))

    if theme:
        fig.update_layout(template="plotly_dark")
    
    return fig