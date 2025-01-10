from dash import Dash, html, dcc, callback, Output, Input, callback_context, State, dash, ctx, register_page, dash_table
import plotly.express as px
import pandas as pd
#import db_main as db
import dash_bootstrap_components as dbc
import plotly.graph_objects as go 



# Crear la aplicación Dash
#FLATLY
register_page(__name__, path="/")

Folder_in='./inputs'
Folder_out='./outputs'

layout = html.Div([
    
])
