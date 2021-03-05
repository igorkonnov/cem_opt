import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
import pandas as pd
import numpy as np
#import ibm_db
import sqlalchemy
from sqlalchemy import *
#import ibm_db_sa
from dash.dependencies import Input, Output
import plotly.express as px
import pathlib
from utils import Header, make_dash_table

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

#from sqlalchemy import create_engine
#e = create_engine("db2+ibm_db://jpl36331:h28p0+7g67rhlp6h@dashdb-txn-sbox-yp-lon02-07.services.eu-gb.bluemix.net:50000/BLUDB")
#get_table = 'select * from plant_data_example'
#df = pd.read_sql_query(get_table, e)
#df = pd.read_excel('data.xlsx')
#df = df[[ 'dosage', '2 D',  'residue']]
color_1 = "#003399"
color_2 = "#00ffff"
color_3 = "#002277"
color_b = "#F8F8FF"

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 6


 html.Div(
        children=[
        html.Div(
            [
                #html.Div(
                    #[
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Div(
                                                    html.Img(
                                                        src=app.get_asset_url(
                                                            "dash-logo-new.png"
                                                        ),
                                                        className="page-1a",
                                                    )
                                                ),
                                                html.Div(
                                                    [
                                                        html.H6("Проект века"),
                                                        html.H5("Оптимизации затрат на производство цемента на основе AI"),
                                                        html.H6("Все права защищены"),
                                                    ],
                                                    className="page-1b",
                                                ),
                                            ],
                                            className="page-1c",
                                        )
                                    ],
                                    className="page-1d",
                                ),
                                html.Div(
                                    [
                                        html.H1(
                                            [
                                                html.Span("01.", className="page-1e"),
                                                html.Span("20"),
                                            ]
                                        ),
                                        html.H6("Все права защищены"),
                                    ],
                                    className="page-1f",
                                ),
                            ],
                            className="page-1g",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6("Igor Konnov", className="page-1h"),
                                        html.P("453-264-8591"),
                                        html.P("ilq@w.ipq"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6("John Gates", className="page-1h"),
                                        html.P("497-234-2837r"),
                                        html.P("isw@vxogiqyds.umf"),
                                    ],
                                    className="page-1i",
                                ),

                                html.Div(
                                    [
                                        html.H6("Thomas Lemke", className="page-1h"),
                                        html.P("284-671-3721"),
                                        html.P("j@jdvwnqucm.etv"),
                                    ],
                                    className="page-1i",
                                ),
                            ],
                            className="page-1j",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6(
                                            "Краткое описание",
                                            className="page-1h",
                                        ),
                                        html.P("В период 2019 - 2020 года на АО NaN были проведены многочисленные физико-механические испытания цемента (ЦЕМ I 42.5Н), при различных дозировках интенсификаторов помола ( 250-700 г. на тонну), с вводом инертных наполнителей( в пределах ГОСТ), в различных режимах работы помольных агрегатов. В результате были накоплены данные о качественных характеристиках цемента и занесены в базу данных Db2(IBM trademark)  "),
                                    ],
                                    className="page-1k",
                                ),

                                html.Div(
                                    [
                                        html.H6(
                                            "KPI ML модели",
                                            className="page-1h",
                                        ),
                                        html.P("add smthing"),
                                    ],
                                    className="page-1m",
                                ),
                                html.Div(
                                    [
                                        html.H6(
                                            "Цель",
                                            className="page-1h",
                                        ),
                                        html.P("add somthing"),
                                    ],
                                    className="page-1l",
                                ),
                            ],
                            className="page-1n",
                        ),
                    #],
                    #className="subpage",
                #)
            ],
            className="page",
        ) ,


                 ])
],className="page",)
