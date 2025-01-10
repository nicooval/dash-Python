from dash import Dash, html, dcc, callback, Output, Input, callback_context, State, dash, ctx, register_page, dash_table
import plotly.express as px
import pandas as pd
import db_main_bhp as db
import dash_bootstrap_components as dbc
import plotly.graph_objects as go 
from datetime import datetime, timedelta


# Crear la aplicación Dash
#FLATLY
register_page(__name__, path="/Principales", external_stylesheets=[dbc.themes.BOOTSTRAP,  'assets/custom.css','https://codepen.io/chriddyp/pen/bWLwgP.css'])

Folder_in='./inputs'
Folder_out='./outputs'

tabla_MEL= pd.read_excel(Folder_in+'/'+"excl_ESC.xlsx")
tabla_SPC= pd.read_excel(Folder_in+'/'+"excl_SPC.xlsx")
q2=db.query_drop()
df_cell= db.getdata_recursive(q2,Folder_out+'\\'+ "q2",'update', ' ', 'MySQL', 'DSN=BHP')


cached_data = None
cached_data2 = None
cache_d = None
cached_data3= None


#dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"



# Definir el diseño de la aplicación
layout = html.Div([


        #html.Label('Polígonos:', className='form-label small'),


    html.Div([
        html.Label('Seleccione un rango de fechas: ', className='form-label small'),
        dcc.DatePickerRange(
            id='date-range-picker_PL',
            start_date= (datetime.now() - timedelta(days=10)),
            end_date=(datetime.now() - timedelta(days=5)),
            display_format='YYYY-MM-DD',
            className="dbc",
            style={'width': '100%',
                    'font-size': '6px'},
            #color='#b5111a'
        ),
    ], className='mb-2',style={}),




    
    dbc.Button('Buscar', id='btn-buscarPL', n_clicks=0, className='btn btn-danger btn-sm mb-2 mt-1'),

 

    html.Div([
        dcc.Graph(id='graph-contentKp',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentKp2',
                style={'font-family': 'Calibri'}), 
        dcc.Graph(id='graph-contentKp3',
                style={'font-family': 'Calibri'}), 
        dcc.Graph(id='graph-contentKp4',
                style={'font-family': 'Calibri'}),

    ], style={'display': 'flex', 'flex-wrap': 'wrap','justifyContent': 'center'}),

            html.Label('Celdas excluidas MEL:', className='form-label small'),
            html.Div([
              
              dash_table.DataTable(
                id='tbl1',
                data=tabla_MEL.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in tabla_MEL.columns],
                style_table={ 'overflowY': 'auto','width': '100%'},
                style_cell={
                    'whiteSpace': 'normal',
                    'height': '5px',
                    #'width': 'auto',  # Ajusta la altura de la celda automáticamente
                    'minWidth': '50px',  # Ancho mínimo de la celda
                    'maxWidth': '100px',
                    'font-size': '12px',
                    'fontFamily': 'Calibri, sans-serif',
                     # Ancho máximo de la celda
                },
                editable=True,  # Permitir edición de celdas
                row_selectable='multi',  # Permitir selección múltiple de filas
                selected_rows=[],  # Filas seleccionadas inicialmente
                filter_action='native',  # Habilitar filtros
                sort_action='native',  # Habilitar ordenamiento
                page_action='native',  # Habilitar paginación
                #page_size=20,  # Número de filas por página,
                export_format='csv',
                export_headers='display',
                merge_duplicate_headers=True

    )], style={'display': 'flex', 'flex-wrap': 'wrap'}),
            html.Label('Celdas excluidas SPC:', className='form-label small'),
            html.Div([
              
              dash_table.DataTable(
                id='tbl2',
                data=tabla_SPC.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in tabla_SPC.columns],
                style_table={ 'overflowY': 'auto','width': '100%'},
                style_cell={
                    'whiteSpace': 'normal',
                    'height': '5px',
                    #'width': 'auto',  # Ajusta la altura de la celda automáticamente
                    'minWidth': '50px',  # Ancho mínimo de la celda
                    'maxWidth': '100px',
                    'font-size': '12px',
                    'fontFamily': 'Calibri, sans-serif',
                     # Ancho máximo de la celda
                },
                editable=True,  # Permitir edición de celdas
                row_selectable='multi',  # Permitir selección múltiple de filas
                selected_rows=[],  # Filas seleccionadas inicialmente
                filter_action='native',  # Habilitar filtros
                sort_action='native',  # Habilitar ordenamiento
                page_action='native',  # Habilitar paginación
                #page_size=20,  # Número de filas por página,
                export_format='csv',
                export_headers='display',
                merge_duplicate_headers=True

    )], style={'display': 'flex', 'flex-wrap': 'wrap'}),



 ], style={}, className='bg-light p-4')
# Definir la función de actualización del gráfico




def perform_database_queries(start_date, end_date):

    #week_start.astype(str)
    #week_end.astype(str)

    start_date1 = pd.to_datetime(start_date)
    end_date1 = pd.to_datetime(end_date)

# Calcular el número de semana
    week_start = str(start_date1.isocalendar()[1])
    week_end = str(end_date1.isocalendar()[1])
    #week_start.astype(str)
    #week_end.astype(str)

    if start_date is not None:

        q=db.esc_WEEK_PRINCIPAL(week_start, week_end)
        df= db.getdata_recursive(q,Folder_out+'\\'+ "p",'update', ' ', 'MySQL', 'DSN=BHP')

        q2=db.esc_DAY_PRINCIPAL(start_date, end_date)
        df2= db.getdata_recursive(q2,Folder_out+'\\'+ "p2",'update', ' ', 'MySQL', 'DSN=BHP') 
        #df2=df2.drop_duplicates(keep='last')           

        q3=db.spc_WEEK_PRINCIPAL(week_start, week_end)
        df3= db.getdata_recursive(q3,Folder_out+'\\'+ "p3",'update', ' ', 'MySQL', 'DSN=BHP')

        q4=db.spc_DAY_PRINCIPAL(start_date, end_date)
        df4= db.getdata_recursive(q4,Folder_out+'\\'+ "p4",'update', ' ', 'MySQL', 'DSN=BHP')
            #df2=df2.drop_duplicates(keep='last') 



    return df,df2,df3,df4

# Función para calcular la columna 'NUT' y mapear 'Sector'


# def calculate_and_map_columns2(df,fecha):
#     # Calcular la columna 'NUT'
#     #if dias != None:
#     df = df[~df['date_id'].isin(fecha)]


#     return df



def generate_graph(df,df2,df3,df4):


    def create_figure(df, x_col, y1_cols, y2_cols, y1_name, y2_name, titleg):

        fig = go.Figure()
  

        for y1_col in y1_cols:
            fig.add_trace(go.Scatter(x=df[x_col], y=df[y1_col], name=y1_col,line=dict(width=2),yaxis='y'))
        for y2_col in y2_cols:
            fig.add_trace(go.Scatter(x=df[x_col], y=df[y2_col], name=y2_col,line=dict(width=2),yaxis='y2'))



        fig.update_layout(
            #barmode='stack',
            width=6.5 * 96 * 1.5,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
            height=3 * 96 *1.5,   # 3 pulgadas convertidas a píxeles
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title=dict(text=titleg, x=0.5, y=0.9),
            yaxis=dict(
                title=f'{y1_name}',
                side='left',
                showgrid=True,
                gridcolor='lightgray',
                #gridwidth=1,
                #dtick=0.2 
                #range=[0, 120],
                autorange = True,
                fixedrange= False
            ),
            yaxis2=dict(
                title=f'{y2_name}',
                side='right',
                showgrid=False,
                overlaying='y',
                gridcolor='lightgray',
                gridwidth=1,
                #dtick=0.2 
                #range=[0, max_value_y1]
                autorange = True,
                fixedrange= False
            ),
            xaxis=dict(
                showgrid=False,
            ))
        return fig



     
    fig1 = create_figure(df, 'week', ['Disponibilidad', 'Accesibilidad', 'Movilidad'],['Drop'], '%','%','KPIs WEEK MEL')
    fig2 = create_figure(df2, 'date_id', ['Disponibilidad', 'Accesibilidad', 'Movilidad'],['Drop'], '%','%','KPIs DAY MEL')
    fig3 = create_figure(df3, 'week', ['Disponibilidad', 'Accesibilidad', 'Movilidad'],['Drop'], '%','%','KPIs WEEK SPC')
    fig4 = create_figure(df4, 'date_id', ['Disponibilidad', 'Accesibilidad', 'Movilidad'],['Drop'], '%','%','KPIs DAY SPC')






    layout_style = dict(
        font=dict(family='Calibri', size=13),
        xaxis=dict(title=dict( font=dict(family='Calibri black', size=15, color='black'))),
        yaxis=dict(title=dict(font=dict(family='Calibri black', size=15, color='black'))),
        title=dict(font=dict(family='Calibri black', size=24, color='black')),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1, font=dict(family='Calibri', size=11, color='black')),

    )

    layout_style2 = dict(
        font=dict(family='Calibri', size=13),
        xaxis=dict(title=dict( font=dict(family='Calibri black', size=15, color='black'))),
        yaxis=dict(title=dict(font=dict(family='Calibri black', size=15, color='black'))),
        title=dict(font=dict(family='Calibri black', size=24, color='black')),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1, font=dict(family='Calibri', size=11, color='black')),
        margin=dict(
        l=50,  # Ajusta el margen izquierdo según sea necesario
        r=50,  # Ajusta el margen derecho según sea necesario
        t=250,  # Ajusta el margen superior según sea necesario
        b=50  # Ajusta el margen inferior según sea necesario
    ))

    layout_style3 = dict(
        font=dict(family='Calibri', size=13),
        xaxis=dict(title=dict( font=dict(family='Calibri black', size=15, color='black'))),
        yaxis=dict(title=dict(font=dict(family='Calibri black', size=15, color='black'))),
        title=dict(font=dict(family='Calibri black', size=24, color='black')),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1, font=dict(family='Calibri', size=11, color='black')),
        margin=dict(
        l=50,  # Ajusta el margen izquierdo según sea necesario
        r=50,  # Ajusta el margen derecho según sea necesario
        t=250,  # Ajusta el margen superior según sea necesario
        b=50  # Ajusta el margen inferior según sea necesario
    ))

    layout_style4 = dict(
        font=dict(family='Calibri', size=13),
        xaxis=dict(title=dict( font=dict(family='Calibri black', size=15, color='black'))),
        yaxis=dict(title=dict(font=dict(family='Calibri black', size=15, color='black'))),
        title=dict(font=dict(family='Calibri black', size=24, color='black')),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1, font=dict(family='Calibri', size=11, color='black')),
        margin=dict(
        #l=50,  # Ajusta el margen izquierdo según sea necesario
        #r=50,  # Ajusta el margen derecho según sea necesario
        #t=250,  # Ajusta el margen superior según sea necesario
        t=150  # Ajusta el margen inferior según sea necesario
    ))

    
    
    fig1.update_layout(**layout_style)
    fig2.update_layout(**layout_style)
    fig3.update_layout(**layout_style)
    fig4.update_layout(**layout_style)

    fig1.update_layout(xaxis={'type':'category'})
    #fig2.update_layout(xaxis={'type':'category'})
    fig3.update_layout(xaxis={'type':'category'})
    #fig4.update_layout(xaxis={'type':'category'})



    return fig1,fig2,fig3,fig4


# Definir el callback



# Definir la función de actualización del gráfico
@callback(
    [Output('graph-contentKp', 'figure'),
     Output('graph-contentKp2','figure'),
     Output('graph-contentKp3','figure'),
     Output('graph-contentKp4','figure')],
    [Input('btn-buscarPL', 'n_clicks')],
    [State('date-range-picker_PL', 'start_date'),
     State('date-range-picker_PL', 'end_date')]
)
def update_graph(n_clicks, start_date, end_date):
      # Asegurar que cached_data sea global

    global cached_data
    global cached_data2
    global cached_data3


    # Verificar qué componente ha desencadenado la actualización
    triggered_component_id = ctx.triggered_id
    #print(triggered_component_id )
    if  (triggered_component_id == 'btn-buscarPL'):
        


        # Realizar consultas a la base de datos solo si el botón "Buscar" o algún dropdown ha desencadenado la actualización
        df,df2,df3,df4 = perform_database_queries(start_date, end_date)

        fig1,fig2,fig3,fig4 = generate_graph(df,df2,df3,df4) 


    else:

        
        fig1 = go.Figure()
        fig2 = go.Figure()
        fig3 = go.Figure()
        fig4 = go.Figure()


        #dropdown_fecha=[]

        
        #config = {'sort_action':'native'}
    # Generar opciones para Dropdown
    return fig1,fig2,fig3,fig4
layout.children.append(dcc.Interval(id='interval-component', interval=86400000, n_intervals=0))

# Iniciar la aplicación si se ejecuta el script

# Iniciar la aplicación si se ejecuta el script











