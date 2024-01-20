def parse_data(data):
    month_mapping = {'Jan': 1, 'Fev': 2, 'Mar': 3, 'Abr': 4,
                 'Mai': 5, 'Jun': 6, 'Jul': 7, 'Ago': 8,
                 'Set': 9, 'Out': 10, 'Nov': 11, 'Dez': 12}
    data['Mês'] = data['Mês'].map(month_mapping)

    data['Chamadas Realizadas'] = data['Chamadas Realizadas'].astype(int)
    data['Dia'] = data['Dia'].astype(int)
    data['Mês'] = data['Mês'].astype(int)

    data['Valor Pago'] = data['Valor Pago'].str.lstrip('R$ ').astype(int)

    data['Status de Pagamento'] = data['Status de Pagamento'].map({'Pago': 1, 'Não pago': 0}).astype(int)

    data1 = data.groupby('Equipe')['Valor Pago'].sum().reset_index()

    data2 = data.groupby('Dia')['Chamadas Realizadas'].sum().reset_index()

    return data1, data2

def graph_title(title):
    return dict(text=f"{title}", font=dict(size=24))
