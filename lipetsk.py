import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
import pandas as pd
import numpy as np

#import ibm_db
#import sqlalchemy
#from sqlalchemy import *
#import ibm_db_sa
from dash.dependencies import Input, Output,  State

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

app = dash.Dash(__name__ )



temper = pd.read_excel(r'C:\Users\IKonnov\OneDrive - GCPAT\AAA\2021\Eurocement\lipetsk\temperature.xlsx')
temper = temper[['Местное время в Липецке', 'T']]
temperm = df3.merge(temper,  how = 'left', left_on='Дата изготовления образцов', right_on='Местное время в Липецке', left_index=False)
Z =temperm[['Содерж. SO₃, %', 'XS 148', 'Дозировка клинкера с запаса, %', 'R 008, %', 't цемента, ° С', 'W цемента. %','T' ]]
Y = temperm['Прочность сжатие 2 сут, МПа']


from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

Input=[('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression(normalize=True))]


pipe=Pipeline(Input)
pipe.fit(Z,Y)



from sklearn.linear_model import Ridge
RigeModel=Ridge(alpha=0.1,normalize=True )
RigeModel.fit(Z, Y)



# In[49]:


from sklearn.experimental import enable_hist_gradient_boosting  # noqa
from sklearn.ensemble import HistGradientBoostingRegressor

p

est = HistGradientBoostingRegressor()
est.fit(Z, Y)


if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_ui=False,dev_tools_props_check=False)
