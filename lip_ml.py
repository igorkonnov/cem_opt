import pandas as pd
import pathlib
from utils import Header
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px
import pathlib
import dash_daq as daq
from dash.dependencies import Input, Output
# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve




controls = html.Div([

                  dbc.FormGroup(
            [
                dbc.Label("Цена интенсификатора, руб.тонна"),
                dbc.Input(id="price_additive", type="number", value=150000),
                dbc.Label("Мощность главного привода, кВт"),
                dcc.Input(id="totpower", type="number", value=2200),
                dbc.Label("Цена электроэнергии, руб. за кВт/ч"),
                dbc.Input(id="enercost", type="number", value=3.1),
                dbc.Label("Затраты на ремонт и обслуживание, руб.на тонну цемента"),
                dbc.Input(id="rm_cost", type="number", value=20),
                dbc.Label("Себестоимость пр-ва клинкера, руб. за тонну"),
                dbc.Input(id="clinkercost", type="number", value=1800),
                dbc.Label("Цена минеральных добавок (известняк), руб. за тонну"),
                dbc.Input(id="slag_cost", type="number", value=150),
                dbc.Label("Цена гипса, руб. за тонну"),
                dbc.Input(id="gypsum", type="number", value=500)


            ]
                            )

                   ],
                   )
input_var = dbc.Card ([

                  dbc.FormGroup([

                  daq.Slider(value=8, min=1,max=10,step=1,id ='residue', handleLabel={"showCurrentValue": True,"label": "VALUE"} , ),
                  dbc.Label("Тонкость помола  R 0045", className="slider" ),

                  daq.Slider(value=600, min=0,max=1000,step=1,id ='dosage', handleLabel={"showCurrentValue": True, "label": "value"}),
                  dbc.Label("Дозировка интенсификатора, г/т",  className="slider" ),

                  daq.Slider(value=5, min=0,max=5,step=0.5,id ='filler', handleLabel={"showCurrentValue": True, "label": "value"} ),
                  dbc.Label("% ввода известняка",  className="slider"),

                  daq.Slider(value=4, min=0,max=5,step=0.5,id ='gypsum', handleLabel={"showCurrentValue": True,"label": "value"}),
                  dbc.Label("% ввод гипса")


])
                     ])


y_days =   html.Div(
[html.Output(id='output-state',  style={'width': '40%', 'height': 10, 'font-size':20, 'margin-bottom':100, 'color':"red" }, ) ],className="slider"
        )
l_days =   html.Div(
[html.Output(id='output-state2',  style={'width': '40%', 'height': 10, 'font-size':20, 'margin-bottom':100, 'color':"blue" }, ) ],className="slider"
      )
cost_out= html.Div (
[dbc.Label("Суммарные переменные затраты руб/тонну"),
html.Output(id="total_cost",className ='output2', style={'width': '40%', 'height': 30, 'font-size':20,'margin-bottom':0,'text-align': 'center', 'color':"blue" },)
]
)
target =html.Div ([ dbc.Label("Целевая прочность,2 сут МПа"),
                  dbc.Input(id="target_str", type="number", value=26, style={'width': '40%', 'height': 30, 'font-size':20,'margin-bottom':10,'text-align': 'center', 'color':"blue" }),
])

optim= html.Div ([dbc.Label("Оптимальные затраты"),
html.Output(id="optim_cost",className ='output2', style={'width': '40%', 'height': 30, 'font-size':20,'margin-bottom':10,'text-align': 'center', 'color':"blue" },)
]
)

opt_res= html.Div ([dbc.Label("Оптимальньный остаток на сите R0045"),
html.Output(id="opt_res",className ='output2', style={'width': '40%', 'height': 30, 'font-size':20,'margin-bottom':10,'text-align': 'center', 'color':"blue" },)
]
)

opt_dos= html.Div ([dbc.Label("Оптимальная дозировка"),
html.Output(id="opt_dos",className ='output2', style={'width': '40%', 'height': 30, 'font-size':20,'margin-bottom':10,'text-align': 'center', 'color':"blue" },)
]
)

opt_fil= html.Div ([dbc.Label("Оптимальный % известняка"),
html.Output(id="opt_fil",className ='output2', style={'width': '40%', 'height': 30, 'font-size':20,'margin-bottom':10,'text-align': 'center', 'color':"blue" },)
]
)

button1 = html.Div ([html.Button(id='submit-button-state',n_clicks=0, children='Оптимизировать')])




optimisation = html.Div([

                  dbc.FormGroup(
            [

                dbc.Label("Производительность, т/ч"),
                html.Output(id="tones", className ='output2' ),
                dbc.Label("Стоимость электроэнергии на тонну цемента, руб"),
                html.Output(id="cost_energypt",className= 'output2' ),
                dbc.Label("Затраты на ремонт и обслуживание, руб. за тонну"),
                html.Output(id="rmcost",className= 'output2' ),
                dbc.Label("Затраты на интенсификатор, руб. за тонну"),
                html.Output(id="add_cost", className= 'output2'),
                dbc.Label("Затраты на материалы(композиция), руб. за тонну"),
                html.Output(id="composition_cost", className= 'output3' )



            ]
                            )

                   ],
                   )



def create_layout(app, external_stylesheets=[dbc.themes.BOOTSTRAP]):
    return html.Div(
                [
                Header(app),html.Hr(),



html.Div(
         [html.H4(["Вводные данные"],className="subtitle padded" ),

         controls], className= "four columns", style={"padding-left": "10"} ),
html.Div(
         [html.H4(["Целевые показатели"],className="subtitle padded" ),



         y_days,l_days,cost_out, target, optim, opt_res,opt_dos, opt_fil, button1 ], className= "three columns"),


html.Div(
         [html.H4(["Затраты, расчетные"],className="subtitle padded" ),

         optimisation,  input_var

         ], className= "three columns", style={"padding-left": "0"} ),





])
