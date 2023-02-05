import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from dash import dcc, html, Dash
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from utility_functions import add_pie_chart, add_subplots, line_chart, bar_plot, bar_graph_rooftop, \
    unassigned_tgm_distribution, barplot_subplots

app = Dash(external_stylesheets=[dbc.themes.QUARTZ])
app.config.suppress_callback_exceptions = True

df = pd.read_csv(
    "https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Other/Dash_Introduction/intro_bees.csv")

df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)


@app.callback(
    Output(component_id='my_bee_map', component_property='figure'),
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Year"] == option_slctd]
    dff = dff[dff["Affected by"] == "Varroa_mites"]

    fig = go.Figure(
        data=[go.Choropleth(
            locationmode='USA-states',
            locations=dff['state_code'],
            z=dff["Pct of Colonies Impacted"].astype(float),
            colorscale='Reds'
        )]
    )

    fig.update_layout(
        title_text="No of Sales by State",
        title_xanchor="center",
        title_font=dict(size=24),
        title_x=0.5,
        geo=dict(scope='usa'),
    )

    return fig


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return dbc.Container([

            dbc.Row([
                dbc.Col(dcc.Graph(figure=line_chart()),

                        width={'size': 8},className='mb-4'),

                dbc.Col([

                    html.P("A sample description describing the data")

                ], width={'size': 3}, className='text-primary mb-4', style={'margin-top': '250px'})
            ]),

            dbc.Row([

                dbc.Col([
                    dcc.Graph(figure=add_subplots())
                ], width={'size': 7, 'order': 2, 'offset': 2}, className='mb-4'

                ),

                dbc.Col([
                    html.P('A simple trace of subplot for demo purpose'),
                ], width={'size': 3}, className='mb-4', style={'margin-top': '250px'}

                )
            ], justify='start'),

            dbc.Row([

                dbc.Col([
                    dcc.Graph(figure=bar_plot())
                ], width={'size': 7}, className='mb-4'

                ),

                dbc.Col([
                    html.P('A simple trace of barplot for demo purpose'),
                ], width={'size': 3, 'order': 2, 'offset': 2}, className='mb-4', style={'margin-top': '250px'}

                )
            ], justify='start'),
            # Horizontal:start,center,end,between,around

            dbc.Row([
                dbc.Col([
                    html.P("A sample description for pie chart")
                ], width={'size': 5, 'order': 1}, className='mb-4',style={'margin-top': '250px'}

                ),

                dbc.Col([
                    dcc.Graph(figure=add_pie_chart())
                ], width={'size': 7, 'order': 2}, className='mb-4'

                )], justify='start'),

            dbc.Row([
                dbc.Col([
                    html.P("testing chart")
                ], width={'size': 5, 'order': 2}, className='mb-4', style={'margin-top': '250px'}

                ),

                dbc.Col([
                    dcc.Graph(figure=bar_graph_rooftop())
                ], width={'size': 7, 'order': 1}, className='mb-4'

                )], justify='start'),

            dbc.Row([
                dbc.Col([
                    html.P("A sample description for bar tgm services")
                ], width={'size': 5, 'order': 1}, className='mb-4', style={'margin-top': '250px'}

                ),

                dbc.Col([
                    dcc.Graph(figure=unassigned_tgm_distribution())
                ], width={'size': 7, 'order': 2}, className='mb-4'

                )], justify='start'),

            dbc.Row([
                dbc.Col([
                    html.P("A sample description for tgm services")
                ], width={'size': 3, 'order': 1}, className='mb-4', style={'margin-top': '250px'}

                ),

                dbc.Col([
                    dcc.Graph(figure=barplot_subplots())
                ], width={'size': 7, 'order': 2,'offset':2}, className='my-5'

                )], justify='start'),

            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(id="slct_year",
                                 options=[
                                     {"label": "2015", "value": 2015},
                                     {"label": "2016", "value": 2016},
                                     {"label": "2017", "value": 2017},
                                     {"label": "2018", "value": 2018}],
                                 multi=False,
                                 value=2015,
                                 # style={'width': "40%"},
                                 className='mb-4'
                                 ),

                    dcc.Graph(id='my_bee_map', figure={}),

                ], width={'size': 7}),

                dbc.Col([
                    html.P("A sample text for demo purposes")

                ], width={'size': 3, 'offset': 1}, style={'margin-top': '250px'})

            ], justify='start')

        ], fluid=True)
    elif pathname == "/page-1":
        return "Welcome to page2"
    elif pathname == "/page-2":
        return "Welcome to page3"
        # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
