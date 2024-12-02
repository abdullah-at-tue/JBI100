import plotly.express as px
from dash import dcc
from main.dataset import df

# df['time_of_incident'] = pd.to_datetime(df['time_of_incident'], format='%H:%M:%S.%f')
# df['time_of_incident_hours'] = df['time_of_incident'].dt.hour + \
#                                 df['time_of_incident'].dt.minute / 60 + \
#                                 df['time_of_incident'].dt.second / 3600
# df['day_of_month_incident'] = df['date_of_incident'].dt.day

df = df.sample(int(len(df)*0.01))
def component():
    # GROUP AND COLOR
    fig = px.parallel_coordinates(
        df[[
            "size",
            "annual_average_employees",
            "incident_outcome",
            "dafw_num_away",
            "djtr_num_tr",
            "type_of_incident",
        ]],
        labels={
            "size": "Size",
            "annual_average_employees": "Annual Average Employees",
            "incident_outcome": "Incident Outcome",
            "dafw_num_away": "Days away from work",
            "djtr_num_tr": "Days needed to transfer",
            "type_of_incident": "Type of Incident",
        },
        # color="state",
        # color_continuous_scale=px.colors.diverging.Tealrose,
        # color_continuous_midpoint=2,
    )

    return dcc.Graph(
        figure=fig,
        id='multi_axis'
    )
