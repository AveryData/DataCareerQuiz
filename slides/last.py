# necessary imports - do not change, and include on every slide
import dash_html_components as html
from app import app
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
###







content = html.H1(style=dict(textAlign='center'), children = [

    
    html.H3('Congrats! You matched with...'),
    html.H1('Data Scientist!'),

    html.Div(
        html.Img(
            src='assets/dfj-owl.gif',
            style=dict(height='600px')
        )
    ),

    html.Br(),

    html.Div(
    [
        html.H5('Data Scientits are...'),
        html.P('Really cool, relaly fun, and get paid a lot'),


        #html.Button('Download the full PDF summary!'),
        html.Br(),
        html.Div(
            html.Iframe(id="embedded-pdf", width="600px", height="776px",src="assets/Breaking Into Data Science.pdf")
        )
    ])



]


)