import plotly.express as px
from dash import dcc
from main.dataset import df

def component():
    df_normalized = df.groupby(['date_of_incident', 'state']).size().reset_index(name='occurrence')

    # date_of_incident
    # axes: incident_datetime, annual_average_employees, BAD: state, total_hours_worked,
    # size: occurrence
    # COLOR: establishment_type, size, incident_outcome/type_of_incident

    fig = px.scatter(
        df_normalized,
        x="state",
        y="date_of_incident",
        # size="occurrence",
        color="occurrence",
        # z="establishment_type",
        # hover_name="country",
        size_max=60,
    )

    fig.update_layout(
        margin={"l": 0, "r": 0, "t": 0, "b": 0},
        legend=dict(
            x=0.02,
            y=0.98,
        ),
        xaxis=dict(
            title=dict(
                text="State",
                standoff=0,
            ),
            ticks="inside",
            showgrid=True,
        ),
        yaxis=dict(
            title=dict(
                text="Date of incident",
                standoff=0,
            ),
            ticks="inside",
            showgrid=True,
        ),
    )

    return dcc.Graph(
        figure=fig,
        id='bubble_chart'
    )
