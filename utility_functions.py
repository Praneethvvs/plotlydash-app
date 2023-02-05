from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import plotly.io as pio

# import geopandas as gpd
from dash.dependencies import Input, Output
from dash import dcc, html, Dash
import dash_bootstrap_components as dbc



def add_subplots():
    df1 = pd.read_csv("data/TopFiveBrands.csv")
    df1 = df1.pivot(index='dateoftransaction', columns='brandname', values='count')
    df1.fillna(0, inplace=True)
    fig = px.area(df1, facet_col="brandname", facet_col_wrap=2)
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)')

    return fig


def add_pie_chart():
    df = pd.read_excel("data/pie_data.xlsx")
    # df = px.data.tips()
    fig = px.pie(df, values='count', names='state')
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)')
    return fig


def line_chart():
    df_month =  pd.read_csv("data/Trends_time_series_linechart.csv")
    fig = go.Figure(data=go.Scatter(x=df_month['month'].astype(dtype=str),
                                    y=df_month['counts'],
                                    marker_color='indianred', text="counts"))
    fig.update_layout({"title": 'Data Year wide Trends',
                       "xaxis": {"title": "Months"},
                       "yaxis": {"title": "Total Transactions"},
                       "showlegend": False})
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)')
    return fig



def bar_plot():
    df1 = pd.read_csv("data/assignedVsUnassignedCount.csv")
    fig=px.bar(data_frame=df1, x="year", y="count",color="SourceQueue", barmode="group")
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)')
    return fig


def bar_graph_rooftop():
    rooftopData = pd.read_csv("data/rooftopData.csv")
    k=rooftopData[rooftopData['GeoLevel']!='other'].groupby(['transcationyear','GeoLevel']).size().reset_index(name='counts')
    fig = px.bar(data_frame=k, x="transcationyear", y="counts", color="GeoLevel", barmode="group")
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)')
    return fig



def unassigned_tgm_distribution():
    df = pd.read_excel("data/unassigned_tgm.xlsx")
    # df = px.data.tips()
    fig = px.pie(df, values='Count', names='Channel')
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)')
    return fig


def barplot_subplots():
    payment_df = pd.read_excel("data/paymentserv_top5.xlsx")
    ota_df = pd.read_excel("data/ota_serv_top5.xlsx")
    otp_df = pd.read_excel("data/otp_serv_top5.xlsx")
    delivery_df = pd.read_excel("data/delivery_serv_top5.xlsx")
    giftcard_df = pd.read_excel("data/gift_card_serv_top5.xlsx")
    fig = make_subplots(rows=3, cols=2,subplot_titles=["paymentservice","ota","otp","delivery","giftcard"])

    fig.add_trace(
        trace=go.Bar(x=payment_df['brandname'], y=payment_df['paymentCount']),
        row=1, col=1
    )

    fig.add_trace(
        trace=go.Bar(x=ota_df['brandname'], y=ota_df['paymentCount']),
        row=1, col=2
    )

    fig.add_trace(
        trace=go.Bar(x=otp_df['brandname'], y=ota_df['paymentCount']),
        row=2, col=1,
    )

    fig.add_trace(
        trace=go.Bar(x=delivery_df['brandname'], y=delivery_df['paymentCount']),
        row=2, col=2
    )

    fig.add_trace(
        trace=go.Bar(x=giftcard_df['brandname'], y=giftcard_df['paymentCount']),
        row=3, col=1
    )

    fig.update_layout(width=800, height=1000)
    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)')
    # fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")
    return fig




# def heatmap_geodata():
#     df = px.data.election()
#     geo_df = gpd.GeoDataFrame.from_features(
#         px.data.election_geojson()["features"]
#     ).merge(df, on="district").set_index("district")
#     fig = px.choropleth_mapbox(geo_df,
#                                geojson=geo_df.geometry,
#                                locations=geo_df.index,
#                                color="Joly",
#                                center={"lat": 45.5517, "lon": -73.7073},
#                                mapbox_style="open-street-map",
#                                zoom=8.5)
#     return fig

