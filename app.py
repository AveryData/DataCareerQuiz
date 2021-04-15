from presentation import presentation_title
import dash
import dash_bootstrap_components as dbc

css_style = ['https://codepen.io/chriddyp/pen/dZVMbK.css']

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)
app.config.suppress_callback_exceptions = True
app.title = presentation_title
server = app.server