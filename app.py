import os

import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input, clientside_callback

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

month_mapping = {'Jan': 1, 'Fev': 2, 'Mar': 3, 'Abr': 4,
             'Mai': 5, 'Jun': 6, 'Jul': 7, 'Ago': 8,
             'Set': 9, 'Out': 10, 'Nov': 11, 'Dez': 12}

df = pd.read_csv('dataset_vendas.csv')
parsed_data = parse_data(df, month_mapping)

team_options = [{'label': 'Todas as Equipes', 'value': 'all_teams'}]
for team in parsed_data['Equipe'].unique():
    team_options.append({'label': team, 'value': team})

month_options = []
for month_label, month_value in month_mapping.items():
    month_options.append({'label': month_label, 'value': month_value})

month_options = sorted(month_options, key=lambda month_value: month_value['value'])
month_options.append({'label': 'Todos os Meses', 'value': 'all_months'})

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])

app.layout = dbc.Container([
    
    dbc.Row([
        html.A(
            html.H1("Sales Analytics"),
            href="https://github.com/MoranggNormal/pydash",
            style={"textDecoration": "none"},
        ),     
    ], className="w-75 mx-auto my-5"),
    
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
                    id='current_month'
            )), 
            dbc.Col(
                [
                    html.Label(className="fa fa-sun", htmlFor="theme_selector", style={'margin-right': '10px'}),
                    dbc.Switch(value=False, id='theme_selector', className="custom-switch"),
                    html.Label(className="fa fa-moon", htmlFor="theme_selector", style={'margin-left': '5px'}),
                ],
                width={'size': 2},
                className="d-flex align-items-center"
            ),
        ],
        className="w-75 g-2 mx-auto flex-nowrap mt-3 mt-md-0",
        align="center",
        ),
    
    dbc.Row(
        dbc.Col(
            dbc.Card([
                dbc.Row([
                    dbc.Col(
                        dcc.Graph(id='top_consultants_plus_team_by_value_bar_chart', style={"height": "300px"}),
                        width={'size': 12},  md={'size': 9}
                    ),
                    dbc.Col(
                        dcc.Graph(id='top_consultants_plus_team_by_value', style={"height": "300px"}),
                        width={'size': 12}, md={'size': 3}
                    ),
                ]),
                ],
            ), className="mx-auto"
        ),
        className="mt-5 mx-auto"
    ),
        
    dbc.Row([
        dbc.Col(
            dbc.Row([
                dbc.Card(
                    dcc.Graph(id="average_calls_by_days_of_the_month", style={"height": "300px"}),
                    className="mt-2"
                ),
                dbc.Card(
                    dcc.Graph(id="average_calls_by_month", style={"height": "300px"}),
                    className="mt-2",
                ),
            ]),
            width={"size": 12}, md={"size":4}
        ),
        dbc.Col(
            dbc.Row([
                dbc.Col(
                    dbc.Card(
                        dcc.Graph(id="team_sales", style={"height": "300px"}), className="mt-2",
                    ),
                width={"size": 12}),
                dbc.Col(
                    dbc.Card(
                        dcc.Graph(id="earnings_per_month_plus_segregation_by_team", style={"height": "300px"}),
                        className="mt-2"
                    ),
                width={"size": 12}),
            ]),
            width={"size": 12}, md={"size":5}
        ),
        dbc.Col(
            dbc.Row([
                dbc.Card(
                    dcc.Graph(id="indicators_best_consultant", style={"height": "300px"}),
                    className="mt-2"
                ),
                dbc.Card(
                    dcc.Graph(id="indicators_best_equip", style={"height": "300px"}),
                    className="mt-2"
                ),
            ]),
            width={"size": 12}, md={"size":3},
        ),
        ],
        className="mx-auto mt-2",
    ),
    
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dcc.Graph(id='advertising_on_piechart', style={"height": "300px"})
            ),
            width={"size": 12}, md={"size": 3},
        ),
        dbc.Col(
            dbc.Card(
                dcc.Graph(id='amounts_paid_through_advertising', style={"height": "300px"})
            ),
            width={"size": 12}, md={"size": 6},
        ),
        dbc.Col(
            dbc.Card(
                dcc.Graph(id='indicators_total_earnings', style={"height": "300px"})
            ),
            width={"size": 12}, md={"size": 3},
        ),
    ], className="g-2 mx-auto my-2"),
        
    # dcc.Graph(id='paid_and_not_paid'),
    # dcc.Graph(id='indicators_total_calls'),

], fluid=True)

@callback(
    Output('top_consultants_plus_team_by_value_bar_chart', 'figure'),
    Input('top_consultants_plus_team_by_value_bar_chart', 'clickAnnotationData'),
    Input('current_month', 'value'),
    Input('theme_selector', 'value'))
def update_graph_top_consultants_plus_team_by_value_bar_chart(clickAnnotationData, month, theme):
    if month == 'all_months':
        data = parsed_data.groupby(['Equipe', 'Consultor'])['Valor Pago'].sum()
    else:
        data = parsed_data[parsed_data['Mês'] == month].groupby(['Equipe', 'Consultor'])['Valor Pago'].sum()

    data = data.sort_values(ascending=False).groupby('Equipe').head(1).reset_index()
    
    return graph_top_consultants_plus_team_by_value_bar_chart(data, theme)

@callback(
    Output('team_sales', 'figure'),
    Input('team_sales', 'clickAnnotationData'),
    Input('current_month', 'value'),
    Input('theme_selector', 'value'))
def update_graph_team_sales(clickAnnotationData, month, theme):
    
    if month == 'all_months':
        data = parsed_data.groupby('Equipe')['Valor Pago'].sum().reset_index()
    else:
        data = parsed_data[parsed_data['Mês'] == month].groupby('Equipe')['Valor Pago'].sum().reset_index()
    
    return graph_team_sales(data, theme)

@callback(
        Output('average_calls_by_days_of_the_month', 'figure'), 
        Input('average_calls_by_days_of_the_month', 'clickAnnotationData'),
        Input('current_team', 'value'),
        Input('theme_selector', 'value'))
def update_graph_average_calls_by_days_of_the_month(clickAnnotationData, value, theme):
    if value == 'all_teams':
        data = parsed_data.groupby('Dia')['Chamadas Realizadas'].sum().reset_index()
    else:
        data = parsed_data[parsed_data['Equipe'] == value]
        data = data.groupby('Dia')['Chamadas Realizadas'].sum().reset_index()
    return graph_average_calls_by_days_of_the_month(data, theme)

@callback(
        Output('average_calls_by_month', 'figure'), 
        Input('average_calls_by_month', 'clickAnnotationData'),
        Input('current_team', 'value'),
        Input('theme_selector', 'value'))
def update_graph_average_calls_by_month(clickAnnotationData, value, theme):
    if value == 'all_teams':
        data = parsed_data.groupby('Mês')['Chamadas Realizadas'].sum().reset_index()
    else:
        data = parsed_data[parsed_data['Equipe'] == value]
        data = data.groupby('Mês')['Chamadas Realizadas'].sum().reset_index()
    return graph_average_calls_by_month(data, theme)

@callback(
    Output('amounts_paid_through_advertising', 'figure'),
    Input('amounts_paid_through_advertising', 'hoverData'),
    Input('current_team', 'value'),
    Input('theme_selector', 'value'))
def update_graph_amounts_paid_through_advertising(hoverData, value, theme):
    if value == 'all_teams':
        data = parsed_data.groupby(['Meio de Propaganda', 'Mês'])['Valor Pago'].sum().reset_index()
    else:
        data = parsed_data[parsed_data['Equipe'] == value]
        data = data.groupby(['Meio de Propaganda', 'Mês'])['Valor Pago'].sum().reset_index()
    return graph_amounts_paid_through_advertising(data, theme)

@callback(
    Output('advertising_on_piechart', 'figure'),
    Input('advertising_on_piechart', 'clickAnnotationData'),
    Input('current_team', 'value'),
    Input('current_month', 'value'),
    Input('theme_selector', 'value'))
def update_graph_advertising_on_piechart(clickAnnotationData, value, month, theme):
    if value == 'all_teams':
        filtered_data = parsed_data
    else:
        filtered_data = parsed_data[parsed_data['Equipe'] == value]

    if month != 'all_months':
        filtered_data = filtered_data[filtered_data['Mês'] == month]

    grouped_data = filtered_data.groupby('Meio de Propaganda')['Valor Pago'].sum().reset_index()

    return graph_advertising_on_piechart(grouped_data, theme)

@callback(
    Output('earnings_per_month_plus_segregation_by_team', 'figure'),
    Input('earnings_per_month_plus_segregation_by_team', 'clickAnnotationData'),
    Input('theme_selector', 'value'))
def update_graph_earnings_per_month_plus_segregation_by_team(clickAnnotationData, theme):
    df5 = parsed_data.groupby(['Mês', 'Equipe'])['Valor Pago'].sum().reset_index()
    df5_group = parsed_data.groupby('Mês')['Valor Pago'].sum().reset_index()
    return graph_earnings_per_month_plus_segregation_by_team(df5, df5_group, theme)

@callback(
    Output('paid_and_not_paid', 'figure'),
    Input('paid_and_not_paid', 'clickAnnotationData'),
    Input('theme_selector', 'value'))
def update_graph_paid_and_not_paid(clickAnnotationData, theme):
    data = parsed_data.groupby('Status de Pagamento')['Chamadas Realizadas'].sum()
    return graph_paid_and_not_paid(data, theme)

@callback(
    Output('indicators_best_consultant', 'figure'),
    Input('indicators_best_consultant', 'clickAnnotationData'),
    Input('current_month', 'value'),
    Input('theme_selector', 'value'))
def update_graph_indicators_best_consultant(clickAnnotationData, month, theme):
    if month == 'all_months':
        data = parsed_data.groupby(['Consultor', 'Equipe'])['Valor Pago'].sum().reset_index()
    else:
        data = parsed_data[parsed_data['Mês'] == month].groupby(['Consultor', 'Equipe'])['Valor Pago'].sum().reset_index()
    
    return graph_indicators_best_consultant(data.sort_values(by='Valor Pago', ascending=False), theme)


@callback(
    Output('indicators_best_equip', 'figure'),
    Input('indicators_best_equip', 'clickAnnotationData'),
    Input('current_month', 'value'),
    Input('theme_selector', 'value'))
def update_graph_indicators_best_equip(clickAnnotationData, month, theme):
    if month == 'all_months':
        filtered_data = parsed_data
    else:
        filtered_data = parsed_data[parsed_data['Mês'] == month]

    grouped_data = filtered_data.groupby('Equipe')['Valor Pago'].sum()
    sorted_data = grouped_data.sort_values(ascending=False).reset_index()

    return graph_indicators_best_equip(sorted_data, theme)

@callback(
    Output('indicators_total_earnings', 'figure'), 
    Input('indicators_total_earnings', 'clickAnnotationData'),
    Input('current_team', 'value'),
    Input('current_month', 'value'),
    Input('theme_selector', 'value'))
def update_graph_indicators_total_earnings(clickAnnotationData, value, month, theme):
    if value == 'all_teams':
        filtered_data = parsed_data
    else:
        filtered_data = parsed_data[parsed_data['Equipe'] == value]

    if month == 'all_months':
        data = filtered_data
    else:
        data = filtered_data[filtered_data['Mês'] == month]

    return graph_indicators_total_earnings(data, theme)

@callback(
    Output('indicators_total_calls', 'figure'),
    Input('indicators_total_calls', 'clickAnnotationData'),
    Input('theme_selector', 'value'))
def update_graph_indicators_total_calls(clickAnnotationData, theme):
    return graph_indicators_total_calls(parsed_data, theme)

@callback(
    Output('top_consultants_plus_team_by_value', 'figure'),
    Input('top_consultants_plus_team_by_value', 'clickAnnotationData'),
    Input('current_month', 'value'),
    Input('theme_selector', 'value'))
def update_graph_top_consultants_plus_team_by_value(clickAnnotationData, month, theme):

    if month == 'all_months':
        data = parsed_data.groupby(['Equipe', 'Consultor'])['Valor Pago'].sum()
    else:
        data = parsed_data[parsed_data['Mês'] == month].groupby(['Equipe', 'Consultor'])['Valor Pago'].sum()

    data = data.sort_values(ascending=False).groupby('Equipe').head(1).reset_index()
    
    return graph_top_consultants_plus_team_by_value(data, theme)


clientside_callback(
    """
    (switchOn) => {
       switchOn
         ? document.documentElement.setAttribute('data-bs-theme', 'dark')
         : document.documentElement.setAttribute('data-bs-theme', 'light')
       return window.dash_clientside.no_update
    }
    """,
    Output("theme_selector", "id"),
    Input("theme_selector", "value"),
)

server = app.server

if __name__ == '__main__':
    app.run_server(debug=os.getenv("DEBUG", False))