import os

import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input

import dash_bootstrap_components as dbc

from utils import parse_data

from components.average_calls_by_month import graph_average_calls_by_month
from components.average_calls_by_days_of_the_month import graph_average_calls_by_days_of_the_month
from components.team_sales import graph_team_sales
from components.amounts_paid_through_advertising import graph_amounts_paid_through_advertising
from components.advertising_on_piechart import graph_advertising_on_piechart
from components.earnings_per_month_plus_segregation_by_team import graph_earnings_per_month_plus_segregation_by_team
from components.paid_and_not_paid import graph_paid_and_not_paid
from components.indicators_best_consultant import graph_indicators_best_consultant
from components.indicators_best_equip import graph_indicators_best_equip
from components.indicators_total_earnings import graph_indicators_total_earnings
from components.indicators_total_calls import graph_indicators_total_calls
from components.top_consultants_plus_team_by_value import graph_top_consultants_plus_team_by_value
from components.top_consultants_plus_team_by_value_bar_chart import graph_top_consultants_plus_team_by_value_bar_chart

main_config = {
    "hovermode": "x unified",
    "legend": {"yanchor":"top", 
                "y":0.9, 
                "xanchor":"left",
                "x":0.1,
                "title": {"text": None},
                "font" :{"color":"white"},
                "bgcolor": "rgba(0,0,0,0.5)"},
    "margin": {"l":0, "r":0, "t":20, "b":0}
}

month_mapping = {'Jan': 1, 'Fev': 2, 'Mar': 3, 'Abr': 4,
             'Mai': 5, 'Jun': 6, 'Jul': 7, 'Ago': 8,
             'Set': 9, 'Out': 10, 'Nov': 11, 'Dez': 12}

df = pd.read_csv('dataset_vendas.csv')
parsed_data = parse_data(df, month_mapping)

team_options = [{'label': 'Todas as Equipes', 'value': 'all_teams'}]
for team in parsed_data['Equipe'].unique():
    team_options.append({'label': team, 'value': team})

month_options = [{'label': 'Mês', 'value': 'all_months'}]
for month in parsed_data['Mês'].unique():
    month_key = [key for key, value in month_mapping.items() if value == month][0]

    month_options.append({'label': month_key, 'value': month})
    
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand("Python Dash", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://github.com/MoranggNormal/pydash",
                style={"textDecoration": "none"},
            ),
            dbc.Row([
                    dbc.Col(
                        dcc.Dropdown(
                        options=team_options,
                        value='all_teams',
                        clearable=False,
                        id='current_team'
                    )),
                    dbc.Col(
                        dcc.Dropdown(
                            options=month_options,
                            value='all_months',
                            clearable=False,
                            id='month_team'
                    )),
                ],
                className="g-2 ms-auto flex-nowrap mt-3 mt-md-0",
                align="center",
                ),
            ], className="my-5"
        ),
    
    dbc.Card(
        dbc.Row([
            dbc.Col(
                dcc.Graph(id='top_consultants_plus_team_by_value_bar_chart'),
                width={'size': 6}
            ),
            dbc.Col(
                dcc.Graph(id='top_consultants_plus_team_by_value'),
                width={'size': 6}
            ),
        ], className="w-75 mx-auto flex-nowrap"),
    ),
        

    dcc.Graph(id='team_sales'),
    dcc.Graph(id='average_calls_by_days_of_the_month'),
    dcc.Graph(id='average_calls_by_month'),
    dcc.Graph(id='amounts_paid_through_advertising'),
    dcc.Graph(id='advertising_on_piechart'),
    dcc.Graph(id='earnings_per_month_plus_segregation_by_team'),
    dcc.Graph(id='paid_and_not_paid'),
    dcc.Graph(id='indicators_best_consultant'),
    dcc.Graph(id='indicators_best_equip'),
    dcc.Graph(id='indicators_total_earnings'),
    dcc.Graph(id='indicators_total_calls'),

], fluid=True)

@callback(Output('top_consultants_plus_team_by_value_bar_chart', 'figure'), Input('top_consultants_plus_team_by_value_bar_chart', 'clickAnnotationData'))
def update_graph_top_consultants_plus_team_by_value_bar_chart(clickAnnotationData):
    data = parsed_data.groupby(['Equipe', 'Consultor'])['Valor Pago'].sum()
    data = data.sort_values(ascending=False)
    data = data.groupby('Equipe').head(1).reset_index()
    return graph_top_consultants_plus_team_by_value_bar_chart(data)

@callback(Output('team_sales', 'figure'),Input('team_sales', 'clickAnnotationData'))
def update_graph_team_sales(clickAnnotationData):
    data = parsed_data.groupby('Equipe')['Valor Pago'].sum().reset_index()
    return graph_team_sales(data)

@callback(
        Output('average_calls_by_days_of_the_month', 'figure'), 
        Input('average_calls_by_days_of_the_month', 'clickAnnotationData'),
        Input('current_team', 'value'))
def update_graph_average_calls_by_days_of_the_month(clickAnnotationData, value):
    if value == 'all_teams':
        data = parsed_data.groupby('Dia')['Chamadas Realizadas'].sum().reset_index()
    else:
        data = parsed_data[parsed_data['Equipe'] == value]
        data = data.groupby('Dia')['Chamadas Realizadas'].sum().reset_index()
    return graph_average_calls_by_days_of_the_month(data)

@callback(
        Output('average_calls_by_month', 'figure'), 
        Input('average_calls_by_month', 'clickAnnotationData'),
        Input('current_team', 'value'))
def update_graph_average_calls_by_month(clickAnnotationData, value):
    if value == 'all_teams':
        data = parsed_data.groupby('Mês')['Chamadas Realizadas'].sum().reset_index()
    else:
        data = parsed_data[parsed_data['Equipe'] == value]
        data = data.groupby('Mês')['Chamadas Realizadas'].sum().reset_index()
    return graph_average_calls_by_month(data)

@callback(
    Output('amounts_paid_through_advertising', 'figure'),
    Input('amounts_paid_through_advertising', 'hoverData'),
    Input('current_team', 'value'))
def update_graph_amounts_paid_through_advertising(hoverData, value):
    if value == 'all_teams':
        data = parsed_data.groupby(['Meio de Propaganda', 'Mês'])['Valor Pago'].sum().reset_index()
    else:
        data = parsed_data[parsed_data['Equipe'] == value]
        data = data.groupby(['Meio de Propaganda', 'Mês'])['Valor Pago'].sum().reset_index()
    return graph_amounts_paid_through_advertising(data)

@callback(
    Output('advertising_on_piechart', 'figure'),
    Input('advertising_on_piechart', 'clickAnnotationData'),
    Input('current_team', 'value'))
def update_graph_advertising_on_piechart(clickAnnotationData, value):
    if value == 'all_teams':
        data = parsed_data.groupby('Meio de Propaganda')['Valor Pago'].sum().reset_index()
    else:
        data = parsed_data[parsed_data['Equipe'] == value]
        data = data.groupby('Meio de Propaganda')['Valor Pago'].sum().reset_index()
    return graph_advertising_on_piechart(data)

@callback(Output('earnings_per_month_plus_segregation_by_team', 'figure'), Input('earnings_per_month_plus_segregation_by_team', 'clickAnnotationData'))
def update_graph_earnings_per_month_plus_segregation_by_team(clickAnnotationData):
    df5 = parsed_data.groupby(['Mês', 'Equipe'])['Valor Pago'].sum().reset_index()
    df5_group = parsed_data.groupby('Mês')['Valor Pago'].sum().reset_index()
    return graph_earnings_per_month_plus_segregation_by_team(df5, df5_group)

@callback(Output('paid_and_not_paid', 'figure'), Input('paid_and_not_paid', 'clickAnnotationData'))
def update_graph_paid_and_not_paid(clickAnnotationData):
    data = parsed_data.groupby('Status de Pagamento')['Chamadas Realizadas'].sum()
    return graph_paid_and_not_paid(data)

@callback(Output('indicators_best_consultant', 'figure'), Input('indicators_best_consultant', 'clickAnnotationData'))
def update_graph_indicators_best_consultant(clickAnnotationData):
    data = parsed_data.groupby(['Consultor', 'Equipe'])['Valor Pago'].sum()
    data.sort_values(ascending=False, inplace=True)
    data = data.reset_index()
    return graph_indicators_best_consultant(data)

@callback(Output('indicators_best_equip', 'figure'), Input('indicators_best_equip', 'clickAnnotationData'))
def update_graph_indicators_best_equip(clickAnnotationData):
    data = parsed_data.groupby('Equipe')['Valor Pago'].sum()
    data.sort_values(ascending=False, inplace=True)
    data = data.reset_index()
    return graph_indicators_best_equip(data)

@callback(
    Output('indicators_total_earnings', 'figure'), 
    Input('indicators_total_earnings', 'clickAnnotationData'),
    Input('current_team', 'value'))
def update_graph_indicators_total_earnings(clickAnnotationData, value):
    if value == 'all_teams':
        data = parsed_data
    else:
        data = parsed_data[parsed_data['Equipe'] == value]
    return graph_indicators_total_earnings(data)

@callback(Output('indicators_total_calls', 'figure'), Input('indicators_total_calls', 'clickAnnotationData'))
def update_graph_indicators_total_calls(clickAnnotationData):
    return graph_indicators_total_calls(parsed_data)

@callback(Output('top_consultants_plus_team_by_value', 'figure'), Input('top_consultants_plus_team_by_value', 'clickAnnotationData'))
def update_graph_top_consultants_plus_team_by_value(clickAnnotationData):
    data = parsed_data.groupby(['Equipe', 'Consultor'])['Valor Pago'].sum()
    data = data.sort_values(ascending=False)
    data = data.groupby('Equipe').head(1).reset_index()
    return graph_top_consultants_plus_team_by_value(data)

server = app.server

if __name__ == '__main__':
    app.run_server(debug=os.getenv("DEBUG", False))