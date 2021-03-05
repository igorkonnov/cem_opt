#from utils import Header, make_dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
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
df = pd.read_excel('data.xlsx')
df = df[[ 'dosage', '2 D',  'residue', 'filler%', 'mill_output']]
color_1 = "#003399"
color_2 = "#00ffff"
color_3 = "#002277"
color_b = "#F8F8FF"

# m model
df2 = df
Z= df2[['dosage', 'residue', 'filler%']]

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

pr=PolynomialFeatures(degree=3)

Z_pr=pr.fit_transform(Z)


Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression(normalize=True))]

pipe=Pipeline(Input)


y = df2['2 D']

pipe.fit(Z,y)

df2['2D_predicted'] = pipe.predict(Z)
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(df2['2 D'], df2['2D_predicted'])
R2 = pipe.score(Z,y)
# end model

def create_layout(app):
    return html.Div(
        [
            Header(app),

        html.Div (

         [dcc.Graph

         (figure = (px.scatter(df,  x= 'residue', y= '2 D' , color = '2 D', title ="Двухсуточная прочность и тонкость помола R0045"  ) .update_traces(marker=dict(size=5,line=dict(width=0.5, color='white')), selector=dict(mode='markers')     ))),


                  ] ),

        html.Div (

         [dcc.Graph

         (figure = (px.box(df,  x= 'dosage', y= '2 D' ,  title ="Двухсуточная прочность и дозировка интенсификатора"  )      )),


                  ] ),


            html.Div (

             [dcc.Graph

            (figure = px.scatter_3d(df, x='dosage', z='2 D', y='residue',  color='dosage', title = '4D график, 2-х суточная прочность и основные предикторы',  width=1000, height=700).update_traces(marker=dict(size=3, line=dict(width=2, color='DarkSlateGrey')), selector=dict(mode='markers'))),


                      ] ),

            html.Div(
                [
                    html.H5(
                        "Характеристики модели машинного обучения : MSE = 0,48 , R2 score = 0,92",

                        className="page-9h"),


                    ]),






                    ], className = 'page_l'#end of line plot
)

 #end of page 1
