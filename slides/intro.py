# no need to delete this - it won't show up in the presentation unless you add it to presentation.py

# necessary imports - do not change
import dash_html_components as html
from app import app
import dash_core_components as dcc
from dash.dependencies import Output, Input, State





content = html.Div(style=dict(textAlign='center'),children=[

    html.Div(style = {'background-image':'url(assets/Intro.png)','height':'680px'}, children=[ 

      html.Div( children = [
        html.H1('What Data Career is Right For You?', style={'color':'white'}),
        html.H3('Take the quiz everyone is talking about!',style={'color':'white','margin-top': 25}),
        dcc.Input(type='text', placeholder='Full Name',id='name'),
        html.Br(),
        dcc.Input(type='email',placeholder='Email',id='email'),
        html.Br(),
        html.Button('Take Me To The Quiz!',id='start-button',n_clicks=0,
          style = {'margin-top': 25})
      ],style={'margin':'auto','justify':'center','padding': 100})

    ])
    

    

])
