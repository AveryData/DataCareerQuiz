import requests
import random
import dash_core_components as dcc
import dash_html_components as html


# file for custom functions

def my_function():
    return 0

def print_lorem_ipsum():
    r = requests.get('https://loripsum.net/api/20/medium/plaintext')
    return r.text

def new_random_colors():
    return dict( background='rgba({},{},{},.9)'.format(*[random.randint(100,255) for x in range(3)]) ,maxWidth='700px',textAlign='center',margin='auto')




def mqq(df_row):



    return html.Div(
    [
        html.H2(df_row['Question']),   
        dcc.Slider(
                min=0,
                max=10,
                step=None,
                marks={
                    0: {'label': df_row['Answer1'], 'style':{'font-size':20}},
                    2.5: {'label': df_row['Answer2'], 'style':{'font-size':20}},
                    5: {'label': df_row['Answer3'], 'style':{'font-size':20}},
                    7.5: {'label': df_row['Answer4'], 'style':{'font-size':20}},
                    10: {'label': df_row['Answer5'], 'style':{'font-size':20}},
                },
                value=5,
                
        ),
        html.Br()   
    ])