import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
import pandas as pd
import numpy as np
from utils import mill1
#import ibm_db
#import sqlalchemy
#from sqlalchemy import *
#import ibm_db_sa
from dash.dependencies import Input, Output,  State

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

from pages import (
    overview,
    graths,
    calculator,
)



app = dash.Dash(
    __name__, suppress_callback_exceptions=True, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


df2 = pd.read_excel('data.xlsx')
Z= df2[['dosage', 'residue', 'filler%']]
pr=PolynomialFeatures(degree=3)
Z_pr=pr.fit_transform(Z)
Inputm=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression(normalize=True))]
pipe=Pipeline(Inputm)
y = df2['2 D']
pipe.fit(Z,y)

Z1 =df2[['residue', 'dosage']]
Y1 = df2['mill_output']
lm = LinearRegression( normalize=True)
lm.fit(Z1, df2['mill_output'])


df_opt = pd.DataFrame({'dos': [],  'fil': [], 'res': [], 'sum': [], 'str':[]})



# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")] )



def display_page(pathname):
    if pathname == "/cement/overview":
        return overview.create_layout(app)
    elif pathname == "/cement/graths":
        return graths.create_layout(app)
    elif pathname == "/cement/calculator":
        return calculator.create_layout(app)

    elif pathname == "/cement/full-view":
        return (
            overview.create_layout(app),
            graths.create_layout(app),
            calculator.create_layout(app),
                )

    else:
        return overview.create_layout(app)

@app.callback([Output('output-state', 'children'),
              Output('output-state2', 'children'),
              Output('tones', 'children'),
              Output('cost_energypt','children' ),
              Output('rmcost','children' ),
              Output('add_cost','children' ),
              Output('composition_cost','children' ),
              Output('total_cost','children' ),


              ],


            [Input('dosage', 'value'),
            Input('residue', 'value'),
            Input('filler', 'value'),
            Input ('totpower','value' ),
            Input ('enercost','value' ),
            Input ('rm_cost','value' ),
            Input ('price_additive','value' ),
            Input ('clinkercost','value' ),
            Input ('slag_cost','value' ),





              ])

def strength(dosage,residue,filler,totpower,enercost, rm_cost, price_additive, clinkercost, slag_cost):
              P = np.array([[dosage, residue, filler]])
              outputj = pipe.predict(P)
              early = outputj[0]
              late = (47.03+0.27 * early)
              P1 = np.array([[residue,dosage]])
              tones = lm.predict(P1)
              tones_z = tones[0]
              cost_energypt =( totpower/tones_z*enercost)
              rmcost = (rm_cost*58/tones_z)
              add_cost = price_additive/1000000*dosage
              composition_cost = (100-filler) *(clinkercost/100)+ (filler * slag_cost/1000)
              total_cost = ( cost_energypt+add_cost+composition_cost+rmcost)


              return  '''2 суток = {} МПа'''.format(round(early),1) , '''28 суток = {} МПа'''.format(round(late),1), round(tones_z), round(cost_energypt), round (rmcost), round(add_cost),round (composition_cost),round (total_cost)


@app.callback([Output('optim_cost', 'children'),
                        Output('opt_res', 'children'),
                        Output('opt_dos', 'children'),
                        Output('opt_fil', 'children')
                        ],



                        [Input('submit-button-state', 'n_clicks')],
                        [State('target_str','value' ),
                         State('totpower','value' ),
                         State('enercost','value' ),
                         State('rm_cost','value' ),
                         State('price_additive','value' ),
                         State('clinkercost','value' ),
                         State('slag_cost','value' )],







             )
def zalupa (n_clicks,target_str,totpower, enercost,rm_cost,price_additive,clinkercost,slag_cost ):
            global df_opt
            for dos in range (0, 1000,20):
                for res in range (0,11):
                    for  fil in range (1,6):
                         P = np.array([[dos,res, fil]])
                         output = pipe.predict(P)
                         got =  output[0]
                         if got >= target_str -0.5 and got <= target_str+0.4:
                             s = mill1(dos, res, totpower, enercost,  price_additive, clinkercost,  slag_cost, fil, rm_cost)
                             raw500 = {'dos': dos,  'fil': fil, 'res': res, 'sum': s, 'str':got }
                             df_opt = df_opt.append(raw500, ignore_index=True)

            k = round( df_opt['sum'].min())
            #lopi =2
            mindf = df_opt['sum'].idxmin()
            res1 = df_opt['res'][mindf]
            dos1 = df_opt['dos'][mindf]
            fil1 = df_opt['fil'][mindf]

            df_opt.to_excel('opt.xlsx')
            df_opt = pd.DataFrame({'dos': [],  'fil': [], 'res': [], 'sum': [], 'str':[]})



            return k, res1, dos1,fil1



if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_ui=False,dev_tools_props_check=False)
