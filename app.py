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


if __name__ == '__main__':
    app.run_server(debug=True)
