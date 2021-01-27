import os

import dash
import sys
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

server = app.server

activities = [{'label':'Lecture', 'value':'Lecture'}, {'label':'Studying', 'value':'Studying'}, {'label':'Singing', 'value':'Singing'}, {'label':'Social Event', 'value':'Social Event'}, {'label':'Exercising', 'value':'Exercising'}]
app.layout = html.Div([
    html.H6("Event Information"),
    #MAKE ROOM ID A DROP DOWN?
    html.Div(["RoomID: ",
              dcc.Dropdown(id='room-dropdown', value='test', options=[{'label':'hello', 'value':'hello'}])]), #placeholder rooms
    html.Br(),
    html.Div(["Duration of Event (min): ",
              dcc.Input(id='time-input', value = 0, type='number')]),
    html.Br(),
    html.Div(["Number of Occupants: ",
              dcc.Input(id='occupant-input', value = 0, type='number')]),
    html.Br(),
    html.Div(["Activity: ",
              dcc.Dropdown(id='activity-dropdown', value ='test', options=activities)]),
#     html.Br(),
#     html.Button('Reset', id='reset-button'),
    html.Br(),
    html.Button('Go', id = 'go-button', n_clicks = 0),
    html.Br(),
    html.Div(id = 'calc-output', children = 'Enter values to calculate risk')

])

@app.callback(
    dash.dependencies.Output('calc-output', 'children'),
    [dash.dependencies.Input('go-button', 'n_clicks')],
    [dash.dependencies.Input('activity-dropdown', 'value')],
    [dash.dependencies.Input('room-input', 'value')],
    [dash.dependencies.State('time-input', 'value')],
    [dash.dependencies.State('occupant-input', 'value')]
)
def update_calc(n_clicks, activity_dropdown, room_input, time_input, occupant_input, ):
    # if n_clicks >= 1:
    #     total_ir = ui_calc(activity_dropdown, room_input, time_input, occupant_input, rid_path)
    #     total_inf = int(occupant_input * total_ir)
    #     to_return = 'The risk of holding a(n) {} event for {} minutes in {} is {}%, given the most recent infection rates. With {} occupants, it is likely that {} occupant(s) will be infected.'.format(activity_dropdown, 
    #                                                                                                                             time_input, 
    #                                                                                                                             room_input, 
    #                                                                                                                             round((total_ir * 100),2), 
    #                                                                                                                             occupant_input,
    #                                                                                                                             total_inf)
    #     return to_return
    # else:
    return 'Enter Values to get risk calculation'

if __name__ == '__main__':
    app.run_server(debug=True)
