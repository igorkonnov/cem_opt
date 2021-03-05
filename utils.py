import dash_html_components as html
import dash_core_components as dcc
import numpy as np
import pandas as pd

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


df2 = pd.read_excel('data.xlsx')

Z1 =df2[['residue', 'dosage']]
Y1 = df2['mill_output']
lm = LinearRegression( normalize=True)
lm.fit(Z1, df2['mill_output'])

color_1 = "#003399"

def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [

            html.Div(
                [
                    html.Div(
                        [html.H5("Оптимизация затрат цементного завода")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/cement/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "5"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/cement/overview",
                className="tab first",
            ),
            dcc.Link(
                "Mashine learning model",
                href="/cement/graths",
                className="tab",
            ),
            dcc.Link(
                "Economics and optimization",
                href="/cement/calculator",
                className="tab",
            ),




        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table

def mill1(dos, res, totpower, enercost,  price_additive, clinkercost,  slag_cost, fil, rm_cost ):
        P1 = np.array([[res,dos]])
        tones = lm.predict(P1)
        cost_energypt = totpower/tones[0]*enercost
        rmcost = rm_cost*58/tones[0]
        add_cost = price_additive/1000000*dos
        composition_cost = (100-fil) *(clinkercost/100)+ (fil * slag_cost/1000)
        total_cost = cost_energypt+add_cost+composition_cost+rmcost
        return total_cost
