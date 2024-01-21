import plotly.graph_objects as go

def parse_data(data, month_mapping):

    data['Mês'] = data['Mês'].map(month_mapping)

    data['Chamadas Realizadas'] = data['Chamadas Realizadas'].astype(int)
    data['Dia'] = data['Dia'].astype(int)
    data['Mês'] = data['Mês'].astype(int)

    data['Valor Pago'] = data['Valor Pago'].str.lstrip('R$ ').astype(int)

    data['Status de Pagamento'] = data['Status de Pagamento'].map({'Pago': 1, 'Não pago': 0}).astype(int)

    return data

def graph_title(title):
    return dict(text=f"{title}", font=dict(size=24))

def handle_annotation(text):

    annotation = go.layout.Annotation(
        text=text,
        xref="paper",
        yref="paper",
        font=dict(size=30, color='gray'),
        align="center",
        bgcolor="rgba(0,0,0,0.8)",
        x=0.025,
        y=0.90,
        showarrow=False
    )

    return annotation