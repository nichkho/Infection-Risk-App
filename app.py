import os
import visdcc
import sys
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

from calculator import *

rid_path = 'rm.csv'
room_df = pd.read_csv(rid_path)
rooms = room_df.copy()

rooms_id = []
for rid in room_df['Room']:
    rooms_id.append({'label': rid, 'value': rid})

vav_room = {'Select...': [0,0,0]}
index = 0
for i in rooms['Room']:
    vav_room[i] = [rooms['VAVmin'][index], rooms['VAVmax'][index], (rooms['VAVmin'][index] + rooms['VAVmax'][index])/2]
    index += 1
room_names = list(vav_room.keys())


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_scripts = ['event.js']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets, external_scripts = external_scripts)

server = app.server
activities = [{'label':'Lecture', 'value':'Lecture'}, {'label':'Studying', 'value':'Studying'}, {'label':'Singing', 'value':'Singing'}, {'label':'Social', 'value':'Social'}, {'label':'Exercising', 'value':'Exercising'}]


data = pd.DataFrame()
app.layout = html.Div([
    html.H6("Event Information"),
    html.Div(["RoomID: ",
              dcc.Dropdown(id='room-dropdown', value = list(vav_room.keys())[0],options = [{'label':name, 'value':name} for name in room_names])]),
    html.Br(),
    html.Div(["VAV Level: ",
             dcc.Dropdown(id='vav-dropdown')]),
    html.Br(), 
    html.Div(["VAV Value: ", dcc.Input(id = "vav-value", value = 0, type = "text")]), 
    html.Br(),
    html.Div(["Duration of Event (min): ",
              dcc.Input(id='time-input', value = 0, type='number')]),
    html.Br(),
    html.Div(["Number of Occupants: ",
              dcc.Input(id='occupant-input', value = 0, type='number')]),
    html.Br(),
    html.Div(["Activity: ",
              dcc.Dropdown(id='activity-dropdown', value ='test', options=activities)]),
    html.Br(),
    html.Div(["Masks: ",
              dcc.RadioItems(id = 'masks-radio', value = 0,
    options=[
        {'label': 'Masks', 'value': 1},
        {'label': 'No Masks', 'value': 0},
    ], labelStyle={'display': 'inline-block'})  ]),

    html.Br(),
    html.Button('Go', id = 'go-button', n_clicks = 0),
    html.Br(),
    html.Div(id = 'calc-output', children = 'Enter values to calculate risk'), 
    html.Br(), 
    html.Button("Add to Visualization", id = "addvi", n_clicks = 0), 
    visdcc.Run_js(id = 'jct'), 
    html.Br(), 
    #html.Div([dcc.Graph(id = 'vi')], style={'width': '70%', 'display': 'inline-block', 'padding': '0 20'})
    html.Div(id = 'return_value')
])

@app.callback(
    dash.dependencies.Output('vav-dropdown', 'options'),
    [dash.dependencies.Input('room-dropdown', 'value')]
)
def update_date_dropdown(name):
    return [{'label': 'Min', 'value': "min"}, {'label': 'Average', 'value': "average"}, 
            {'label': 'Max', 'value': "max"}, {"label": "Custom", "value": "custom"}]

@app.callback(
    dash.dependencies.Output('vav-value', 'value'),
    [dash.dependencies.Input('vav-dropdown', 'value')] 
)
def update_vav(vselect):
    if vselect == "min": 
        return "Min"
    elif vselect == "max": 
        return "Max"
    elif vselect == "average": 
        return "Average"
    else: 
        return 0

@app.callback(
    dash.dependencies.Output('calc-output', 'children'),
    [dash.dependencies.Input('go-button', 'n_clicks')],
    [dash.dependencies.Input('activity-dropdown', 'value')],
    [dash.dependencies.Input('room-dropdown', 'value')],
    [dash.dependencies.Input('vav-dropdown', 'value')], 
    
    
    [dash.dependencies.Input('vav-value', 'value')], 
    
    [dash.dependencies.Input('masks-radio', 'value')], 
    [dash.dependencies.State('time-input', 'value')], 
    [dash.dependencies.State('occupant-input', 'value')] 
)
def update_calc(n_clicks, activity_dropdown, room_input, vav_dropdown, vav_value, mask_tf, time_input, occupant_input):
    if n_clicks >= 1:
        if vav_dropdown == "custom": 
            if (vav_value is None) or (vav_value == ""):
                return
            else: 
                comp_ir = ui_calc(activity_dropdown, room_input, time_input, occupant_input, mask_tf, rid_path, vav_value)
        else:        
            comp_ir = ui_calc(activity_dropdown, room_input, time_input, occupant_input, mask_tf, rid_path, vav_dropdown)
            total_inf = int(occupant_input * comp_ir)
            to_return = 'The risk of an individual infected because of holding a(n) {} event for {} minutes in {} is {}%, given the most recent infection rates. With {} occupants, it is likely that {} occupant(s) will be infected.'.format(activity_dropdown, 
                                                                                                                                    time_input, 
                                                                                                                                    room_input, 
                                                                                                                                    round((comp_ir * 100),2), 
                                                                                                                                    occupant_input,
                                                                                                                                    total_inf)
        return to_return
    else:
        return 'Enter Values to get risk estimation'

@app.callback(
    dash.dependencies.Output('return_value', 'children'),
    [dash.dependencies.Input('go-button', 'n_clicks')], 
    [dash.dependencies.Input('activity-dropdown', 'value')],
    [dash.dependencies.Input('room-dropdown', 'value')],
    [dash.dependencies.Input('vav-dropdown', 'value')], 
    
    
    [dash.dependencies.Input('vav-value', 'value')], 
    [dash.dependencies.Input('masks-radio', 'value')],
    [dash.dependencies.State('time-input', 'value')],
    [dash.dependencies.State('occupant-input', 'value')])
def reval(n_clicks, activity_dropdown, room_input, vav_dropdown, vav_value, mask_tf, time_input, occupant_input):
    
    
    
    
    
    
    if n_clicks >= 1:
        if vav_dropdown == "custom": 
            if (vav_value is None) or (vav_value == ""):
                return
            else: 
                ir = ui_calc(activity_dropdown, room_input, time_input, occupant_input, mask_tf, rid_path, vav_value)
                vav = get_vav(rid_path, room_input, vav_value)
        else:
            ir = ui_calc(activity_dropdown, room_input, time_input, occupant_input, mask_tf, rid_path, vav_dropdown)
            vav = get_vav(rid_path, room_input, vav_dropdown)
            results = str({"act": activity_dropdown, "rm": room_input, "ti": time_input, "occupants": occupant_input, "masks": mask_tf, 
                      "vav": vav, "ir": round((ir * 100),2)})
        
        
        
        
        
        return results
    return ""

@app.callback(
    dash.dependencies.Output('jct', 'run'),
    [dash.dependencies.Input('addvi', 'n_clicks')])
def cross_domain(n_clicks): 
    if n_clicks >= 1: 
        return "message()"
    return "console.log(0)"
   


if __name__ == '__main__':
    app.run_server(debug=True)

    
    
    
    
    
    
    
    
