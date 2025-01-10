from dash import Dash, html, dcc, callback, Output, Input, callback_context, State, dash, ctx,page_registry, page_container
import plotly.express as px
import pandas as pd
import db_main_bhp as db
import dash_bootstrap_components as dbc
import plotly.graph_objects as go 
#from MainKPI import app1
#from tableKPI import app2
from dash.exceptions import PreventUpdate



#q_LN = db.query_LTEnodos()
#df_LN= db.getdata_recursive(q_LN, "q_LN",'update', ' ', 'MySQL', 'DSN=EMI')
#df_LN=df_LN.dropna()
#dropdown_options = [{'label': polygon, 'value': polygon} for polygon in df_LN['polygon'].unique()]
cached_data = None
cache_d = None

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
# Crear la aplicación principal
app_main = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css, 'assets/custom.css'])


# Definir el layout principal con el menú y el contenedor de la aplicación seleccionada
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href='/')),
        dbc.NavItem(dbc.NavLink("Spence", href='/Spence')),
        dbc.NavItem(dbc.NavLink("Escondida", href='/Escondida')),
        dbc.NavItem(dbc.NavLink("KPIs", href='/KPIs')),
        dbc.NavItem(dbc.NavLink("KPIs Principales", href='/Principales')),
    ],
    brand="BHP KPIs",
    #brand_href='/MainKPI',
    color="#b5111a",
    dark=True,
)

# Crear la aplicación principal
app_main.layout = html.Div(
    [
        navbar,
        page_container
    ],

)

if __name__ == '__main__':
    app_main.run_server(debug=True)