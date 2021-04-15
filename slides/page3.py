# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
import dash_html_components as html
from app import app
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
import pandas as pd
from custom_utilities.custom_functions import mqq


df = pd.read_csv('PersonQuestions.csv')

list_of_questions = []

for index, row in df.iterrows():
    print(row)
    list_of_questions.append(mqq(row))




content = html.Div(style=dict(textAlign='center'),children=[
    html.H1('Person Skills'),
    html.Br(),
    html.Div(children=list_of_questions, style={'width':'65%','margin-bottom':15,'margin':'auto','justify':'center'}),


    
])



