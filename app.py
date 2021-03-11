import os
import visdcc
import sys
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

import dash_table
import base64
import io
import json
import ast
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








data_table = pd.DataFrame(["Name of Building", "Room Name", "Area of Room (m2)", "Height of Room (ft)", "Minimum VAV (cfm)", "Maximum VAV (cfm)", "ASHRAE Recommended VAV"], 
                          ["Building", "Room", "Area", "Height", "VAVmin", "VAVmax", "VAVrecommended"]).transpose()

data = pd.DataFrame()
app.layout = html.Div([
    html.H6("Event Information"), 
    html.Div(["Building: ", 
              dcc.Dropdown(id = 'building-dropdown', value = list(vav_room.keys())[0],options = [{'label': name, 'value': name} for name in room_names])]), 
    html.Br(), 
    html.Div(["RoomID: ",
              dcc.Dropdown(id='room-dropdown', value = list(vav_room.keys())[0],options = [{'label':name, 'value':name} for name in room_names])]),
    html.Br(),
    html.Div(["VAV Level: ", dcc.Dropdown(id='vav-dropdown')]),
    html.Br(), 
    html.Br(), 
    html.Div(["VAV Value: ", dcc.Input(id = "vav-value", value = 0, type = "text"), " CFM. "]), 
    
    html.Div(id = "vavnotice"), 
    html.Br(),
    html.Div(["Air Purifier: ", dcc.Input(id = "air", value = 0, type = "number"), " CFM. "]), 
    html.Br(), 
    html.Div(["Duration of Event : ",
              dcc.Input(id='time-input', value = 0, type='number'), " Minutes. "]), 
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
    html.Div(id = 'return_value'), 
    html.Br(), 
    html.H5("Advanced Information"), 
    html.Br(), 
    html.Details(children = [
        html.Summary("Add Custom Rooms"), 
        html.Div("You can upload your custom rooms files using the given format: "), 
        dash_table.DataTable(columns = [{"name": i, "id": i} for i in data_table.columns], 
                            data = data_table.to_dict("records")), 
        
        html.Div(["Sample Files can be downloaded: ", html.A("click", href = "custom_rooms.csv", download = "custom_rooms.csv")]), 
        html.Div(["Upload Custom Files: ", dcc.Upload(id = 'upload-data', 
                                                      children = html.Div(['Drag and Drop or ', html.A('Select Files')]), 
                                                      style = {'width': '100%','height': '60px','lineHeight': '60px','borderWidth': 
                                                               '1px','borderStyle': 'dashed','borderRadius': '5px','textAlign': 'center',
                                                               'margin': '10px'})]), 
        html.Div(id = "updated_rooms"),  
        html.Br(), 
        html.Div("It is strongly suggested to remove your custom rooms before leaving the website. "), 
        html.Button("Remove Custom Rooms", id = "remove_rooms", n_clicks = 0), 
        html.Div(id = "removed_rooms"), 
    ]), 
    html.Br(), 
    html.Details(children = [
        html.Summary("Modify Assumptions"), 
        html.Div(["Please read Important Assumptions before editing these assumptions. ", 
                 "Infection Rate could vary from region to region so we include input boxes for you to quickly modify it. ", 
                 "Other assumptions tend not to vary in different regions and they are selected based on our researches. ", 
                 "If you want to modify them anyway, please download the ", 
                 html.A("assumptions file", href = "assumptions.txt", download = "assumptions.txt"),  
                 ". You can modify the downloaded file using Notepad. ", 
                 "After modifying you can upload it to our application. "]), 
        html.Br(), 
        html.Div("Please Click Go Again to Get Updated Estimations After Any Modification. "), 
        html.Br(), 
        html.Div(["Infection Rate: ", dcc.Input(id = 'infection_rt', value = assumptions.var["infection_rate"], type='number')]), 
        html.Div(id = "update_rt"), 
        html.Br(), 
        html.Div("Other Advanced Assumptions"), 
        html.Br(), 
        html.Div(["Upload Your Assumptions Files: ", dcc.Upload(id = 'updated', 
                                                      children = html.Div(['Drag and Drop or ', html.A('Select Files')]), 
                                                      style = {'width': '100%','height': '60px','lineHeight': '60px','borderWidth': 
                                                               '1px','borderStyle': 'dashed','borderRadius': '5px','textAlign': 'center',
                                                               'margin': '10px'})]), 
        html.Div(id = "updated_assumptions"), 
        html.Br(), 
        html.Button("Remove Custom Assumptions", id = "remove_assumptions", n_clicks = 0), 
        html.Div(id = "rm_assumptions"), 
    ])
])



@app.callback(
    dash.dependencies.Output('vavnotice', 'children'), 
    dash.dependencies.Input('vav-value', "value"))
def notice(value): 
    if value == -1: 
        return "A value of -1 indicates the VAV of given option is unavailable, please select 'custom' and input custom VAV or select 'recommended' and use recommended VAV instead. "
    else: 
        return "" 
@app.callback(
    dash.dependencies.Output('rm_assumptions', 'children'), 
    dash.dependencies.Input('remove_assumptions', 'n_clicks'))
def remove_custom_rooms(n_clicks): 
    if n_clicks >= 1: 
        with open("assumptions_original.txt") as fs: 

            readata = fs.read() 
    
        newdata = ast.literal_eval(readata)
        newdata["infection_rate"] = 0.0075
        newvar = assumptions.var
        for i in newvar: 
            newvar[i] = newdata[i]
        update_var(newvar)
        return "Custom Assumptions Removed!" 

@app.callback(
    dash.dependencies.Output("update_rt", "children"), 
    dash.dependencies.Input('infection_rt', 'value')) 
def update_infection(rt): 
    newvar = assumptions.var
    newvar["infection_rate"] = rt
    update_var(newvar)
    return "Current Infection Rate: " + str(rt)




@app.callback(
    dash.dependencies.Output('updated_assumptions', 'children'), 
    dash.dependencies.Input('updated', 'contents'), 
    dash.dependencies.Input('infection_rt', 'value'), 
    dash.dependencies.State('updated', 'filename'),
    dash.dependencies.State('updated', 'last_modified')) 
def update_custom_assumptions(contents, infection_rt, filename, fs): 
    print("content clicked")
    if contents is not None: 
        with open(filename) as fs: 

            readata = fs.read() 
    
        newdata = ast.literal_eval(readata)
        newdata["infection_rate"] = infection_rt 
        newvar = assumptions.var
        for i in newvar: 
            newvar[i] = newdata[i]
        update_var(newvar)
        return "Custom Assumptions " + str(var) + " Updated! " 
    else: 
        return "Current Assumptions: " + str(var)



def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            newdata = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            newdata = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
    
    return newdata
    
    
@app.callback(
    dash.dependencies.Output('removed_rooms', 'children'), 
    dash.dependencies.Input('remove_rooms', 'n_clicks'))
def remove_custom_rooms(n_clicks): 
    if n_clicks >= 1: 
        data = pd.read_csv("rm_original.csv")
        data.to_csv("rm.csv", index = False)
        print("Removed")
        return "Custom Rooms Removed!" 

@app.callback(
    dash.dependencies.Output('updated_rooms', 'children'), 
    dash.dependencies.Input('upload-data', 'contents'),
    dash.dependencies.State('upload-data', 'filename'),
    dash.dependencies.State('upload-data', 'last_modified'))
def update_custom_rooms(contents, filename, fs): 
    print("content clicked")
    if contents is not None: 
        print("content inputed")
        newdata = parse_contents(contents, filename, fs)
        data = pd.read_csv("rm.csv") 
        data = data.append(newdata)
        data.to_csv("rm.csv", index = False)
        return "Custom Rooms " + str(list(newdata["Building"].unique())) + " Updated! "
    else: 
        return "Nothing Uploaded. "

@app.callback(
    dash.dependencies.Output('building-dropdown', 'options'), 
    dash.dependencies.Input('updated_rooms', 'children'), 
    dash.dependencies.Input('removed_rooms', 'children')) 
def update_dataset(updated, removed):
    if "Custom" in updated:
        data = pd.read_csv("rm.csv")
        return [{'label': name, 'value': name} for name in list(data["Building"].unique())]
    else: 
        return [{'label': name, 'value': name} for name in list(rooms["Building"].unique())]

@app.callback( 
    dash.dependencies.Output('removed_rooms', 'n_clicks'), 
    dash.dependencies.Input('removed_rooms', 'children') 
)
def update_remove_clicks(remove_button):
    if remove_button is not None: 
        return 0
    return remove_button


@app.callback(
    dash.dependencies.Output('room-dropdown', 'options'),
    [dash.dependencies.Input('building-dropdown', 'value')]
)
def update_rooms(building):
    data = pd.read_csv("rm.csv")
    data = data[data["Building"] == building]
    return [{'label': name, 'value': name} for name in list(data["Room"].unique())]

@app.callback(
    dash.dependencies.Output('vav-dropdown', 'options'),
    [dash.dependencies.Input('room-dropdown', 'value')]
)
def update_date_dropdown(name):
    return [{"label": "Custom", "value": "custom"}, {"label": "ASHRAE Recommended Minimum", "value": "recommended"}, 
            {'label': 'Max', 'value': "max"},{'label': 'Min', 'value': "min"}, {'label': 'Median', 'value': "median"}]

@app.callback(
    dash.dependencies.Output('vav-value', 'value'),
    [dash.dependencies.Input('vav-dropdown', 'value')], 
    [dash.dependencies.Input('building-dropdown', 'value')], 
    [dash.dependencies.Input('room-dropdown', 'value')]
)
def update_vav(vselect, building_id, roomid): 
    if vselect in ["min", "max", "median", "recommended"]: 
        return get_vav(rid_path, building_id, roomid, vselect, 0)
    else: 
        return 0

@app.callback(
    dash.dependencies.Output('calc-output', 'children'),
    [dash.dependencies.Input('go-button', 'n_clicks')],
    [dash.dependencies.Input('building-dropdown', 'value')], 
    [dash.dependencies.Input('activity-dropdown', 'value')],
    [dash.dependencies.Input('room-dropdown', 'value')],
    [dash.dependencies.Input('vav-dropdown', 'value')], 
    [dash.dependencies.Input('vav-value', 'value')], 
    
    
    [dash.dependencies.Input('air', 'value')], 
    [dash.dependencies.Input('masks-radio', 'value')],
    [dash.dependencies.State('time-input', 'value')],
    [dash.dependencies.State('occupant-input', 'value')]
)
def update_calc(n_clicks, building_input, activity_dropdown, room_input,vav_dropdown, vav_value, air, mask_tf, time_input, occupant_input):
    if n_clicks >= 1: 
        if vav_dropdown == "custom": 
            if (vav_value is None) or (vav_value == ""):
                return
            else: 
                comp_ir = ui_calc(activity_dropdown, building_input, room_input, time_input, occupant_input, mask_tf, rid_path, air, vav_value)
        else:           
            comp_ir = ui_calc(activity_dropdown, building_input, room_input, time_input, occupant_input, mask_tf, rid_path, air, vav_dropdown)
        total_inf = int(occupant_input * comp_ir)
        to_return = 'The risk of an individual infected because of holding a(n) {} event for {} minutes in {} is {}%, given the most recent infection rates. With {} occupants, it is likely that {} occupant(s) will be infected.'.format(activity_dropdown, 
                                                                                                                                time_input, 
                                                                                                                                room_input, 
                                                                                                                                round((comp_ir * 100),2), 
                                                                                                                                occupant_input,
                                                                                                                                total_inf)
        return to_return
   


    else:
        return 'Enter Values to get risk calculation' 
   

@app.callback(
    dash.dependencies.Output('return_value', 'children'),
    [dash.dependencies.Input('go-button', 'n_clicks')], 
    [dash.dependencies.Input('building-dropdown', 'value')], 
    [dash.dependencies.Input('activity-dropdown', 'value')],
    [dash.dependencies.Input('room-dropdown', 'value')],
    [dash.dependencies.Input('vav-dropdown', 'value')], 
    [dash.dependencies.Input('vav-value', 'value')],  
    
    [dash.dependencies.Input('air', 'value')], 
    [dash.dependencies.Input('masks-radio', 'value')],
    [dash.dependencies.State('time-input', 'value')],
    [dash.dependencies.State('occupant-input', 'value')])
def reval(n_clicks, building_input, activity_dropdown, room_input, vav_dropdown, vav_value, air, mask_tf, time_input, occupant_input):
    if n_clicks >= 1: 
        if vav_dropdown == "custom": 
            if (vav_value is None) or (vav_value == ""):
                return
            else: 
                ir = ui_calc(activity_dropdown, building_input, room_input, time_input, occupant_input, mask_tf, rid_path, air, vav_value)
                vav = get_vav(rid_path, building_input, room_input, vav_value, 0)
        else: 
            ir = ui_calc(activity_dropdown, building_input, room_input, time_input, occupant_input, mask_tf, rid_path, air, vav_dropdown)
            vav = get_vav(rid_path, building_input, room_input, vav_dropdown, 0)
        results = str({"act": activity_dropdown, "building": building_input, "rm": room_input, "ti": time_input, "occupants": occupant_input, "masks": mask_tf, 
                      "vav": vav, "air_purifier": air, "ir": round((ir * 100),2)})
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
    app.run_server(debug = True)

    
    
