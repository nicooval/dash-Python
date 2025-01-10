from dash import Dash, html, dcc, callback, Output, Input, callback_context, State, dash, ctx, register_page, dash_table
import plotly.express as px
import pandas as pd
import db_main_bhp as db
import dash_bootstrap_components as dbc
import plotly.graph_objects as go 
from datetime import datetime, timedelta


# Crear la aplicación Dash
#FLATLY
register_page(__name__, path="/Spence", external_stylesheets=[dbc.themes.BOOTSTRAP,  'assets/custom.css'])

Folder_in='./inputs'
Folder_out='./outputs'
#q_cell = db.query_cell()
#df_cell= pd.read_csv(Folder_in+'\\'+'spence_celldata.csv')
#df_cell=df_cell.dropna()

q2=db.query_drop()
df_cell= db.getdata_recursive(q2,Folder_out+'\\'+ "q2",'update', ' ', 'MySQL', 'DSN=BHP')

dropdown_options2 = [{'label': site, 'value': site} for site in df_cell['lnbts_name'].unique()]
dropdown_options1 = [{'label': site, 'value': site} for site in df_cell['lnbts_name'].unique()]
cached_data = None
cached_data2 = None
cache_d = None
cached_data3= None


#dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"



# Definir el diseño de la aplicación
layout = html.Div([

    html.Div([
        html.Label('Seleccione Sitios o Celdas:', className='form-label small'),
        dbc.RadioItems(
            id='poligonos-sitios-radio1',
            label_checked_style={"color": "#b5111a"},
            input_checked_style={
                "backgroundColor": "#b5111a",
                "borderColor": "#b5111a",
            },
            inline=True,
            options=[
                {'label': 'PLMN', 'value': 'PLMN'},
                {'label': 'Sitios', 'value': 'Sitios'},
                {'label': 'Sitio->Celdas', 'value': 'Celdas'}

        ],
        value='PLMN',
    ),

        #html.Label('Polígonos:', className='form-label small'),

        dcc.Dropdown(
            id='PLMN-dropdown1',
            options=['PLMN Spence'],
            multi=True,
            style={'width': '100%', 'fontSize': '12px'},
        ),


        dcc.Dropdown(
            id='Sitios-dropdown1',
            options=dropdown_options1,
            multi=True,
            style={'width': '100%', 'fontSize': '12px'},
        ),

    #html.Label('Celdas:', className='form-label small'),
        dcc.Dropdown(
            id='Celdas-dropdown1',
            options=dropdown_options2,
            multi=True,
            style={'width': '20%', 'fontSize': '12px'},
        ),    
    ], className='mb-2',style={}),


         dcc.Dropdown(
            id='dropdown-sectorC',
            options=[],
            multi=False,
            style={'display': 'none'}
        ),   



    html.Div([
        html.Label('Rango de fechas: ', className='form-label small'),
        dcc.DatePickerRange(
            id='date-range-picker1',
            start_date= (datetime.now() - timedelta(days=10)),
            end_date=datetime.now(),
            display_format='YYYY-MM-DD',
            className="dbc",
            style={'width': '100%',
                    'font-size': '6px'},
            #color='#b5111a'
        ),
    ], className='mb-2',style={}),

    dbc.RadioItems(
            id='time-radio1',
            label_checked_style={"color": "#b5111a"},
            input_checked_style={
                "backgroundColor": "#b5111a",
                "borderColor": "#b5111a",
            },
            inline=True,
            options=[
                {'label': 'DAY', 'value': 'DAY'},
                {'label': 'HOUR', 'value': 'HOUR'},

        ],
        value='DAY',        
        #labelStyle={'display': 'block'}
    ),
    dbc.Button('Buscar', id='btn-buscar1', n_clicks=0, className='btn btn-danger btn-sm mb-2 mt-1'),

 

    html.Div([
        dcc.Graph(id='graph-contentC',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC2',
                style={'font-family': 'Calibri'}), 
        dcc.Graph(id='graph-contentC3',
                style={'font-family': 'Calibri'}), 
        dcc.Graph(id='graph-contentC4',
                style={'font-family': 'Calibri'}),
        # dcc.Graph(id='graph-contentC5',
        #         style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC8',
                style={'font-family': 'Calibri'}),  
        dcc.Graph(id='graph-contentC6',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC7',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC9',
                style={'font-family': 'Calibri'}),
        # dcc.Graph(id='graph-contentC10',
        #         style={'font-family': 'Calibri'}),  
        dcc.Graph(id='graph-contentC11',
                style={'font-family': 'Calibri'}),
        # dcc.Graph(id='graph-contentC12',
        #         style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC13',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC14',
                style={'font-family': 'Calibri'}), 
        dcc.Graph(id='graph-contentC15',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC16',
                style={'font-family': 'Calibri'}),
        # dcc.Graph(id='graph-contentC17',
        #         style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC18',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC19',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC20',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC21',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC22',
                style={'font-family': 'Calibri'}), 
        dcc.Graph(id='graph-contentC23',
                style={'font-family': 'Calibri'}), 
        dcc.Graph(id='graph-contentC24',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC25',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC26',
                style={'font-family': 'Calibri'}),  
        dcc.Graph(id='graph-contentC27',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC28',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC29',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC30',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC31',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC32',
                style={'font-family': 'Calibri'}), 
        dcc.Graph(id='graph-contentC33',
                style={'font-family': 'Calibri'}), 
        dcc.Graph(id='graph-contentC34',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC35',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC36',
                style={'font-family': 'Calibri'}),  
        dcc.Graph(id='graph-contentC37',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC38',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC39',
                style={'font-family': 'Calibri'}),
        # dcc.Graph(id='graph-contentC40',
        #         style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC41',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC42',
                style={'font-family': 'Calibri'}), 
        dcc.Graph(id='graph-contentC43',
                style={'font-family': 'Calibri'}), 
        dcc.Graph(id='graph-contentC44',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC45',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC46',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC47',
                style={'font-family': 'Calibri'}),
        dcc.Graph(id='graph-contentC48',
                style={'font-family': 'Calibri'}),

   

    ], style={'display': 'flex', 'flex-wrap': 'wrap','justifyContent': 'center'}),



], style={}, className='bg-light p-4')
# Definir la función de actualización del gráfico




def perform_database_queries(start_date, end_date,selected_poligonos,option_selected,datetime_option):



    if ((option_selected == 'PLMN') and (datetime_option == 'DAY')):


        if selected_poligonos is not None:

            q=db.query_PLMN(start_date, end_date)
            df= db.getdata_recursive(q,Folder_out+'\\'+ "q",'update', ' ', 'MySQL', 'DSN=BHP')
    elif ((option_selected == 'PLMN') and (datetime_option == 'HOUR')):


        if selected_poligonos is not None:

            q=db.query_PLMN_H(start_date, end_date)
            df= db.getdata_recursive(q,Folder_out+'\\'+ "q",'update', ' ', 'MySQL', 'DSN=BHP')
            df['date_id'] = pd.to_datetime(df['date_id'], format='%Y-%m-%d')
            df['hour_id'] = pd.to_timedelta(df['hour_id'], unit='h')
            df['date_id'] = df['date_id'] + df['hour_id']


    elif ((option_selected == 'Celdas') and (datetime_option == 'DAY') and (df_cell['lnbts_name'] is not None)):
        df_cell_filtro = df_cell[df_cell['lnbts_name'].isin(selected_poligonos)]

        celdas_filt= df_cell_filtro ['lnbts_name'].unique()

        celdas_filt_ = ', '.join(celdas_filt)


        if selected_poligonos is not None:
            celdas = [celda.strip() for celda in celdas_filt_.split(',')]
            celdas_L = "'" + "','".join(celdas) + "'"
            
            q=db.query_cell(start_date, end_date,celdas_L)
            df= db.getdata_recursive(q,Folder_out+'\\'+ "q",'update', ' ', 'MySQL', 'DSN=BHP')

    elif ((option_selected == 'Celdas') and (datetime_option == 'HOUR')):
        df_cell_filtro = df_cell[df_cell['lnbts_name'].isin(selected_poligonos)]

        celdas_filt= df_cell_filtro ['lnbts_name'].unique()

        celdas_filt_ = ', '.join(celdas_filt)


        if selected_poligonos is not None:
            celdas = [celda.strip() for celda in celdas_filt_.split(',')]
            celdas_L = "'" + "','".join(celdas) + "'"
            
            q=db.query_cell_H(start_date, end_date,celdas_L)
            df= db.getdata_recursive(q,Folder_out+'\\'+ "q",'update', ' ', 'MySQL', 'DSN=BHP')
            df['date_id'] = pd.to_datetime(df['date_id'], format='%Y-%m-%d')
            df['hour_id'] = pd.to_timedelta(df['hour_id'], unit='h')
            df['date_id'] = df['date_id'] + df['hour_id']

            #df = df.drop(['hour_id'], axis=1)

    elif ((option_selected == 'Sitios') and (datetime_option == 'DAY') and (df_cell['lnbts_name'] is not None)):
        df_cell_filtro = df_cell[df_cell['lnbts_name'].isin(selected_poligonos)]

        celdas_filt= df_cell_filtro ['lnbts_name'].unique()

        celdas_filt_ = ', '.join(celdas_filt)


        if selected_poligonos is not None:
            celdas = [celda.strip() for celda in celdas_filt_.split(',')]
            celdas_L = "'" + "','".join(celdas) + "'"
            
            q=db.query_sitio(start_date, end_date,celdas_L)
            df= db.getdata_recursive(q,Folder_out+'\\'+ "q",'update', ' ', 'MySQL', 'DSN=BHP')


    elif ((option_selected == 'Sitios') and (datetime_option == 'HOUR') and (df_cell['lnbts_name'] is not None)):
        df_cell_filtro = df_cell[df_cell['lnbts_name'].isin(selected_poligonos)]

        celdas_filt= df_cell_filtro ['lnbts_name'].unique()

        celdas_filt_ = ', '.join(celdas_filt)


        if selected_poligonos is not None:
            celdas = [celda.strip() for celda in celdas_filt_.split(',')]
            celdas_L = "'" + "','".join(celdas) + "'"
            
            q=db.query_sitio_H(start_date, end_date,celdas_L)
            df= db.getdata_recursive(q,Folder_out+'\\'+ "q",'update', ' ', 'MySQL', 'DSN=BHP')
            df= db.getdata_recursive(q,Folder_out+'\\'+ "q",'update', ' ', 'MySQL', 'DSN=BHP')
            df['date_id'] = pd.to_datetime(df['date_id'], format='%Y-%m-%d')
            df['hour_id'] = pd.to_timedelta(df['hour_id'], unit='h')
            df['date_id'] = df['date_id'] + df['hour_id']




    return df

# Función para calcular la columna 'NUT' y mapear 'Sector'


# def calculate_and_map_columns2(df,fecha):
#     # Calcular la columna 'NUT'
#     #if dias != None:
#     df = df[~df['date_id'].isin(fecha)]


#     return df



def generate_graph(df,sector_selected):
    sector_selected = [sector_selected] if not isinstance(sector_selected, list) else sector_selected
    dff= df[df['lncel_name'].isin(sector_selected)]
    #dff = df[(df['lncel_name'] == sector_selected)]
    y1_columns=['Total E-UTRAN RRC conn stp SR']
    y1_columns_=['RRC Rel']
    y2_columns = ['RACH Stp Completion SR']
    y2_columns_=['RACH stp att']
    y3_columns=['E-UTRAN E-RAB stp SR']
    y3_columns_=['E-UTRAN E-RAB Setup Attempts']
    y4_columns=['Cell Avail','Cell Avail excl BLU']
    y5_columns=['RACH stp att']
    y6_columns=['Number of Signaling Connection Establishment Requests rejected due to MME overload','Number of Signaling Connection Establishment Requests rejected due to threshold for the maximum number of RRC connections','Number of Signaling Connection Establishment Requests rejected due to lack of PUCCH resources','Number of Signaling Connection Establishment Requests rejected due to User Plane overload','Number of Signaling Connection Establishment Requests rejected due to Control Plane overload','Signaling Connection Establishment failures due to RRC Setup completions error','Signaling Connection Establishment failures due to RRC Setup completions missing','Signaling Connection Establishment failures for emergency calls due to missing RB resources']
    y7_columns=['E-RAB DR, RNL unspec ini eNB']
    y7_columns_=['eNB initiated E-RAB releases due to loss of connection to the UE','eNB initiated E-RAB releases due to insufficient transport resources','eNB initiated E-RAB releases due to missing radio resources','eNB initiated E-RAB releases due to E-UTRAN Generated Reason','E-RABs released due to failed Handover regardless of the bearers QCI','E-RABs released due to partial Handover regardless of the bearers QCI','EPC initiated EPS Bearer Release requests due to Other causes','M8006C309','M8006C310','M8006C313','M8006C312','M8006C311']
    #y8_columns=['Avg RRC conn UE']
    y9_columns=['PDCP SDU Volume, DL','PDCP SDU Volume, UL']
    y10_columns=['PDCP SDU Volume, DL','PDCP SDU Volume, UL']
    y11_columns=['Avg PDCP cell thp DL','Avg PDCP cell thp UL']
    y12_columns=['Avg PDCP cell thp UL']
    y13_columns=['E-UTRAN Avg PRB usage per TTI DL','Avg PRB usage per TTI UL']
    y14_columns=['DL Spectral efficiency','UL Spectral efficiency']
    y15_columns=['E-RAB Stp SR, QCI9']
    y15_columns_=['E-RAB Stp Att, QCI9']
    y16_columns=['Avg IP thp DL QCI9','Avg IP thp UL QCI9']
    y17_columns=['Avg IP thp UL QCI9']
    y18_columns=['Avg PDCP SDU Delay DL QCI9']
    y19_columns=['Intra eNB HO prep SR']
    y19_columns_=['Failed Intra eNB Handover preparations due to other reasons','Failed Intra eNB Handover preparations due to Admission Control']
    y20_columns=['Intra eNB HO SR']
    y20_columns_=['Total intra eNB HO failures due to timer']
    y21_columns=['inter eNB E-UTRAN HO prep SR X2']
    y21_columns_=['Failed Inter-eNB X2 Handover preparations due to not supported QCI','Failed Inter eNB Handover preparations due to other reason','Failed Inter eNB Handover preparations due to timer','Failed Inter eNB Handover preparations due to target eNB admission control']
    y22_columns=['inter eNB E-UTRAN HO SR X2']
    y22_columns_=['Number of Inter eNB Handover failures']
    y23_columns=['E-UTRAN HO Prep SR, inter eNB S1']
    y23_columns_=['Failed Inter-eNB S1 Handover preparations due to not supported QCI','Failed Inter eNB S1-Handover preparations due to other reason','Failed Inter eNB S1-Handover preparations due to target eNB admission control','Failed Inter eNB S1-Handover preparations due to timer']
    y24_columns=['E-UTRAN HO SR, inter eNB S1']
    y24_columns_=['Inter eNB S1-HO failures due to timer']
    y25_columns=['E-UTRAN Intra-Freq HO SR']
    y26_columns=['Attempted intra eNB HO','Attempted inter eNB HO','Attempted inter eNB S1-HO']
    y27_columns=['% Ping Pong HO']
    y28_columns=['Avg Latency DL','Avg Latency Uplink']
    y29_columns=['PDCP SDU delay on DL DTCH Mean','PDCP SDU delay on UL DTCH Mean']
    y30_columns=['Avg SINR for PUCCH','Avg SINR for PUSCH']
    y31_columns=['Avg RSSI for PUCCH','Avg RSSI for PUSCH']
    y32_columns=['BLER DL','BLER UL']
    y33_columns=['Average CQI']
    y34_columns=['% PUSCH tx using low MCS','% PUSCH tx using high MCS','% PDSCH tx using low MCS','% PDSCH tx using high MCS']
    y35_columns=['MIMO CL Single CW Mode Usage','MIMO CL Double CW Mode Usage']
    y36_columns=['% MIMO RI 1','% MIMO RI 2','% MIMO RI 3','% MIMO RI 4']
    #y37_columns=['E-UTRAN S1 Stp Att']
    #y37_columns_=['S1 init ctx stp FR by NO_RESP','S1 stp FR indicated by MME']
    y38_columns=['E-RAB SFR RNL','E-RAB SFR TRPORT','E-RAB SFR RESOUR','E-RAB stp FR RNL','E-RAB stp FR misc','E-RAB stp FR mobil','E-RAB SFR OTH','E-RAB stp FR miss UE cap lic']
    y39_columns=['Avg Nr simult E-RABs QCI9','Max Nr simult E-RABs QCI9']
    #y39_columns_=['Max Nr simult E-RABs QCI9']
    y40_columns=['E-RAB Stp SR, QCI9']
    y41_columns=['Released active ERABs QCI9']
    y42_columns=['E-UTRAN E-RAB ret RAN v, RNL fail']
    y42_columns_=['E-UTRAN E-RAB DR, RAN View']
    y43_columns=['E-RAB DR, fail HO init eNB']
    y44_columns=['Avg UE distance']
    #y45_columns=['ERAB_REL_ENB_RNL_INA']
    #y46_columns=['E-RAB Stp SR, QCI9']
    #y47_columns=['E-RAB Stp SR, QCI9']
    y47_columns=['AGG1 used PDCCH','AGG2 used PDCCH','AGG4 used PDCCH','AGG8 used PDCCH']
    y48_columns=['CCE block R']
    y48_columns_=['AGG1 blocked PDCCH','AGG2 blocked PDCCH','AGG4 blocked PDCCH','AGG8 blocked PDCCH']


    def create_figure(df, x_col, y1_cols, y2_cols, y1_name, y2_name, titleg):

        fig = go.Figure()
  

        for y1_col in y1_cols:
            fig.add_trace(go.Scatter(x=df[x_col], y=df[y1_col], name=y1_col,line=dict(width=2),yaxis='y2'))
        for y2_col in y2_cols:
            fig.add_trace(go.Bar(x=df[x_col], y=df[y2_col], name=y2_col,yaxis='y'))



        fig.update_layout(
            barmode='stack',
            width=6.5 * 96 * 1.5,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
            height=3 * 96 *1.5,   # 3 pulgadas convertidas a píxeles
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title=dict(text=titleg, x=0.5, y=0.9),
            yaxis=dict(
                title=f'{y2_name}',
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
                title=f'{y1_name}',
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


    def create_figure2(df, x_col, y1_cols, y1_name, titleg, caso):

        fig = go.Figure()

        for y1_col in y1_cols:
            fig.add_trace(go.Scatter(x=df[x_col], y=df[y1_col], name=y1_col,line=dict(width=2)))

        if caso == 0:
            fig.update_layout(
                width=6.5 * 96 * 1.5,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
                height=3 * 96 * 1.5,   # 3 pulgadas convertidas a píxeles
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                title=dict(text=titleg,x=0.5),
                yaxis=dict(
                    title=f'{y1_name}',
                    side='left',
                    showgrid=True,
                    gridcolor='lightgray',
                    gridwidth=1,
                    #dtick=0.2 
                    #range=[None, 100.5],
                    autorange = True,
                    fixedrange= False
                    ),
                xaxis=dict(
                        showgrid=False,
                    ))

        elif caso == 1:
            fig.update_layout(
                width=6.5 * 96 * 1.5,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
                height=3 * 96 * 1.5,   # 3 pulgadas convertidas a píxeles
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                title=dict(text=titleg,x=0.5),
                yaxis=dict(
                    title=f'{y1_name}',
                    side='left',
                    showgrid=True,
                    gridcolor='lightgray',
                    gridwidth=1,
                    #dtick=0.2 
                    #range=[None, 100.5],
                    autorange = True,
                    fixedrange= False
                    ),
                xaxis=dict(
                        showgrid=False,
                    ))   


        return fig

    def create_figure3(df, x_col, y1_cols, y1_name, titleg):

        fig = go.Figure()

        for y1_col in y1_cols:
            fig.add_trace(go.Bar(x=df[x_col], y=df[y1_col], name=y1_col))


        fig.update_layout(
            barmode='stack',
            width=6.5 * 96 * 1.5,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
            height=3 * 96 * 1.5,   # 3 pulgadas convertidas a píxeles
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title=dict(text=titleg,x=0.5),
            yaxis=dict(
                title=f'{y1_name}',
                side='left',
                showgrid=True,
                gridcolor='lightgray',
                gridwidth=1,
                #dtick=0.2 
                autorange = True,
                fixedrange= False
                ),
            xaxis=dict(
                    showgrid=False,
                ))
        return fig    

    def create_figure4(df, x_col, y1_cols, y1_name, titleg):

        fig = go.Figure()

        for y1_col in y1_cols:
            fig.add_trace(go.Bar(x=df[x_col], y=df[y1_col], name=y1_col))


        fig.update_layout(
            barmode='stack',
            width=6.5 * 96 * 2.2,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
            height=3 * 96 * 2.2,   # 3 pulgadas convertidas a píxeles
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title=dict(text=titleg,x=0.5),
            yaxis=dict(
                title=f'{y1_name}',
                side='left',
                showgrid=True,
                gridcolor='lightgray',
                gridwidth=1,
                #dtick=0.2 
                autorange = True,
                fixedrange= False
                ),
            xaxis=dict(
                    showgrid=False,
                ))
        return fig 

    def create_figure5(df, x_col, y1_cols, y2_cols, y1_name, y2_name, titleg):

        fig = go.Figure()

        for y1_col in y1_cols:
            fig.add_trace(go.Scatter(x=df[x_col], y=df[y1_col], name=y1_col,yaxis='y2'))
        for y2_col in y2_cols:
            fig.add_trace(go.Bar(x=df[x_col], y=df[y2_col], name=y2_col,yaxis='y'))


        fig.update_layout(
            barmode='stack',
            width=6.5 * 96 * 2.2,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
            height=3 * 96 * 2.2,   # 3 pulgadas convertidas a píxeles
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title=dict(text=titleg,x=0.5),
            yaxis=dict(
                title=f'{y2_name}',
                side='left',
                showgrid=True,
                gridcolor='lightgray',
                #gridwidth=1,
                #dtick=0.2 
                #range=[0, 120]
                autorange = True,
                fixedrange= True
            ),
            yaxis2=dict(
                title=f'{y1_name}',
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

    def create_figure6(df, x_col, y1_cols, y1_name, titleg):

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=df[x_col], y=df[y1_cols[0]], name=y1_cols[0],stackgroup='one',fillcolor='rgba (239, 85,59, 1)',line=dict(width=1, color='rgba (239, 85,59, 1)')))
        fig.add_trace(go.Scatter(x=df[x_col], y=df[y1_cols[1]], name=y1_cols[1], fill='tonexty',stackgroup='one',fillcolor='rgba(99, 110, 250, 1)',line=dict(width=1, color='rgba (99, 110,250, 1)')))


        fig.update_layout(
            width=6.5 * 96 * 1.5,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
            height=3 * 96 * 1.5,   # 3 pulgadas convertidas a píxeles
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title=dict(text=titleg,x=0.5),
            yaxis=dict(
                title=f'{y1_name}',
                side='left',
                showgrid=True,
                gridcolor='lightgray',
                gridwidth=1,
                #dtick=0.2 
                #autorange = True,
                fixedrange= False
                ),
            xaxis=dict(
                    showgrid=False,
                ))
        return fig  

    def create_figure7(df, x_col, y1_cols, y1_name, titleg):

        fig = go.Figure()

        for y1_col in y1_cols:
            fig.add_trace(go.Scatter(x=df[x_col], y=df[y1_col], name=y1_col,line=dict(width=2)))

        rang=[0,None]


        fig.update_layout(
            width=6.5 * 96 * 1.5,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
            height=3 * 96 * 1.5,   # 3 pulgadas convertidas a píxeles
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title=dict(text=titleg,x=0.5),
            yaxis=dict(
                title=f'{y1_name}',
                side='left',
                showgrid=True,
                gridcolor='lightgray',
                gridwidth=1,
                #dtick=0.2 
                range = rang,
                fixedrange= False
                ),
            xaxis=dict(
                    showgrid=False,
                ))
        return fig 

    def create_figure8(df, x_col, y1_cols, y2_cols, y1_name, y2_name, titleg):

        fig = go.Figure()
  

        for y1_col in y1_cols:
            fig.add_trace(go.Bar(x=df[x_col], y=df[y1_col], name=y1_col,yaxis='y'))
        for y2_col in y2_cols:
            fig.add_trace(go.Scatter(x=df[x_col], y=df[y2_col], name=y2_col,line=dict(width=2),yaxis='y2'))



        fig.update_layout(
            barmode='stack',
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


    def create_figure9(df, x_col, y1_cols, y2_cols, y1_name, y2_name, titleg):

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


     
    fig1 = create_figure(dff, 'date_id', y1_columns,y1_columns_, '%','#','Total E-UTRAN RRC conn stp SR')
    fig2 = create_figure(dff, 'date_id', y2_columns,y2_columns_,  '%','#','RACH Stp Completion')
    fig3 = create_figure(dff, 'date_id', y3_columns,y3_columns_, '%','#','E-UTRAN E-RAB stp SR')
    fig4 = create_figure2(dff, 'date_id', y4_columns, '%','Cell Avail',0)
    #fig5 = create_figure3(dff, 'date_id', y5_columns, '#','RACH stp att')
    fig6 = create_figure4(dff, 'date_id', y6_columns, '#','RCC Failures')
    fig7 = create_figure5(dff, 'date_id', y7_columns,y7_columns_, '%','#','Causas Drop PS')
    #fig8 = create_figure2(dff, 'date_id', y8_columns, '#','Avg UEs Connected y Act',1)
    fig8 =go.Figure()
    fig9 = create_figure6(dff, 'date_id', y9_columns, '[MB]','PDCP SDU Volume')
    #fig10 = create_figure6(dff, 'date_id', y10_columns, '[MB]','PDCP SDU Volume, UL')
    fig11 = create_figure2(dff, 'date_id', y11_columns, '[kbps]','Avg PDCP cell thp',0)
    #fig12 = create_figure7(dff, 'date_id', y12_columns, '[kbps]','Avg PDCP cell thp UL')
    fig13 = create_figure2(dff, 'date_id', y13_columns, '%','E-UTRAN Avg PRB usage per TTI',1)
    fig14 = create_figure2(dff, 'date_id', y14_columns, '[bits/s]','Spectral efficiency',1)
    fig15 = create_figure(dff, 'date_id', y15_columns, y15_columns_, '%','#','E-RAB Stp QCI9')
    fig16 = create_figure2(dff, 'date_id', y16_columns, '%','Avg IP thp QCI9',0)
    #fig17 = create_figure7(dff, 'date_id', y17_columns, '%','Avg IP thp UL QCI9')
    fig18 = create_figure7(dff, 'date_id', y18_columns, 'ms','Avg PDCP SDU Delay DL QCI9')
    fig19 = create_figure(dff, 'date_id', y19_columns,y19_columns_, '%','#','Intra eNB HO prep SR')
    fig20 = create_figure(dff, 'date_id', y20_columns,y20_columns_, '%','#','Intra eNB HO SR')
    fig21 = create_figure(dff, 'date_id', y21_columns,y21_columns_, '%','#','inter eNB E-UTRAN HO prep SR X2')
    fig22 = create_figure(dff, 'date_id', y22_columns,y22_columns_, '%','#','inter eNB E-UTRAN HO SR X2')
    fig23 = create_figure5(dff, 'date_id', y23_columns,y23_columns_, '%','#','E-UTRAN HO Prep SR, inter eNB S1')
    fig24 = create_figure(dff, 'date_id', y24_columns,y24_columns_, '%','#','E-UTRAN HO SR, inter eNB S1')
    fig25 = create_figure2(dff, 'date_id', y25_columns, '%','E-UTRAN Intra-Freq HO SR',0)
    fig26 = create_figure3(dff, 'date_id', y26_columns, '#','Attempted HO')
    fig27 = create_figure2(dff, 'date_id', y27_columns, '%','% Ping Pong HO',0)
    fig28 = create_figure2(dff, 'date_id', y28_columns, '[ms]','Avg Latency',0)
    fig29 = create_figure2(dff, 'date_id', y29_columns, '[ms]','PDCP SDU delay',0)
    fig30 = create_figure2(dff, 'date_id', y30_columns, '[dB]','Avg SINR',0)
    fig31 = create_figure2(dff, 'date_id', y31_columns, '[dBm]','Avg RSSI',0)
    fig32 = create_figure2(dff, 'date_id', y32_columns, '%','BLER',0)
    fig33 = create_figure3(dff, 'date_id', y33_columns, '#','Average CQI')
    fig34 = create_figure2(dff, 'date_id', y34_columns, '%','MCS',0)
    fig35 = create_figure2(dff, 'date_id', y35_columns, '%','MIMO',0)
    fig36 = create_figure2(dff, 'date_id', y36_columns, '%','Rank Indicator',0)
    #fig37 = create_figure8(dff, 'date_id', y37_columns,y37_columns_, '#','%','S1 Attempts _ Setup Failure')
    fig37 =go.Figure()
    fig38 = create_figure2(dff, 'date_id', y38_columns, '%','E-RAB Failures',0)
    fig39 = create_figure3(dff, 'date_id', y39_columns, '#','Avg - Max Nr simult E-RABs QCI9')
    #fig39 = create_figure9(dff, 'date_id', y39_columns,y39_columns_, '#','#','Avg - Max Nr simult E-RABs QCI9')
    #fig40 = create_figure2(dff, 'date_id', y40_columns, '%','E-RAB Stp SR, QCI9',0)
    fig41 = create_figure2(dff, 'date_id', y41_columns, '%','Released active ERABs QCI9',0)
    fig42 = create_figure9(dff, 'date_id', y42_columns,y42_columns_, '#/h','%','E-UTRAN E-RAB ret RAN v, RNL fail')
    fig43 = create_figure2(dff, 'date_id', y43_columns, '%','E-RAB DR, fail HO init eNB',0)
    fig44 = create_figure2(dff, 'date_id', y44_columns, '[km]','Avg UE distance',0)
    #fig45 = create_figure3(dff, 'date_id', y45_columns, '#','ERAB_REL_ENB_RNL_INA (M8006C255)')
    fig45 =go.Figure()
    #'eNB initiated E-RAB releases due to loss of connection to the UE','eNB initiated E-RAB releases due to insufficient transport resources','eNB initiated E-RAB releases due to missing radio resources','eNB initiated E-RAB releases due to E-UTRAN Generated Reason','E-RAB DR, RNL unspec ini eNB','E-RABs released due to failed Handover regardless of the bearers QCI','E-RABs released due to partial  Handover regardless of the bearers QCI','EPC initiated EPS Bearer Release requests due to Other causes','M8006C309','M8006C310','M8006C313','M8006C312','M8006C311'
    fig47 = create_figure3(dff, 'date_id', y47_columns, '#','Nivel de agregación PDCCH')
    fig48 = create_figure(dff, 'date_id', y48_columns,y48_columns_, '%','#','Bloqueos PDCCH')


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
    #fig5.update_layout(**layout_style)
    fig6.update_layout(**layout_style2)
    fig7.update_layout(**layout_style3)
    fig8.update_layout(**layout_style)
    fig9.update_layout(**layout_style)
    #fig10.update_layout(**layout_style)
    fig11.update_layout(**layout_style)
    #fig12.update_layout(**layout_style)
    fig13.update_layout(**layout_style)
    fig14.update_layout(**layout_style)
    fig15.update_layout(**layout_style)
    fig16.update_layout(**layout_style)
    #fig17.update_layout(**layout_style)
    fig18.update_layout(**layout_style)
    fig19.update_layout(**layout_style4)
    fig20.update_layout(**layout_style)
    fig21.update_layout(**layout_style4)
    fig22.update_layout(**layout_style)
    fig23.update_layout(**layout_style)
    fig24.update_layout(**layout_style)
    fig25.update_layout(**layout_style)
    fig26.update_layout(**layout_style)
    fig27.update_layout(**layout_style)
    fig28.update_layout(**layout_style)
    fig29.update_layout(**layout_style)
    fig30.update_layout(**layout_style)
    fig31.update_layout(**layout_style)
    fig32.update_layout(**layout_style)
    fig33.update_layout(**layout_style)
    fig34.update_layout(**layout_style)
    fig35.update_layout(**layout_style)
    fig36.update_layout(**layout_style)
    fig37.update_layout(**layout_style)
    fig38.update_layout(**layout_style)
    fig39.update_layout(**layout_style)
    #fig40.update_layout(**layout_style)
    fig41.update_layout(**layout_style)
    fig42.update_layout(**layout_style)
    fig43.update_layout(**layout_style)
    fig44.update_layout(**layout_style)
    fig45.update_layout(**layout_style)
    fig47.update_layout(**layout_style)
    fig48.update_layout(**layout_style)



    return fig1,fig2,fig3,fig4,fig6,fig7,fig8,fig9,fig11,fig13,fig14,fig15,fig16,fig18,fig19,fig20,fig21,fig22,fig23,fig24,fig25,fig26,fig27,fig28,fig29,fig30,fig31,fig32,fig33,fig34,fig35,fig36,fig37,fig38,fig39,fig41,fig42,fig43,fig44,fig45,fig47,fig48

def generate_graph2(df):
    #sector_selected = [sector_selected] if not isinstance(sector_selected, list) else sector_selected
    dff= df
    #dff = df[(df['lncel_name'] == sector_selected)]
    y1_columns=['Total E-UTRAN RRC conn stp SR']
    y1_columns_=['RRC Rel']
    y2_columns = ['RACH Stp Completion SR']
    y2_columns_=['RACH stp att']
    y3_columns=['E-UTRAN E-RAB stp SR']
    y3_columns_=['E-UTRAN E-RAB Setup Attempts']
    y4_columns=['Cell Avail','Cell Avail excl BLU']
    y5_columns=['RACH stp att']
    y6_columns=['Number of Signaling Connection Establishment Requests rejected due to MME overload','Number of Signaling Connection Establishment Requests rejected due to threshold for the maximum number of RRC connections','Number of Signaling Connection Establishment Requests rejected due to lack of PUCCH resources','Number of Signaling Connection Establishment Requests rejected due to User Plane overload','Number of Signaling Connection Establishment Requests rejected due to Control Plane overload','Signaling Connection Establishment failures due to RRC Setup completions error','Signaling Connection Establishment failures due to RRC Setup completions missing','Signaling Connection Establishment failures for emergency calls due to missing RB resources']
    y7_columns=['E-RAB DR, RNL unspec ini eNB']
    y7_columns_=['eNB initiated E-RAB releases due to loss of connection to the UE','eNB initiated E-RAB releases due to insufficient transport resources','eNB initiated E-RAB releases due to missing radio resources','eNB initiated E-RAB releases due to E-UTRAN Generated Reason','E-RABs released due to failed Handover regardless of the bearers QCI','E-RABs released due to partial Handover regardless of the bearers QCI','EPC initiated EPS Bearer Release requests due to Other causes','M8006C309','M8006C310','M8006C313','M8006C312','M8006C311']
    y8_columns=['Avg Act connected UEs','Avg RRC conn UE']
    y9_columns=['PDCP SDU Volume, DL','PDCP SDU Volume, UL']
    y10_columns=['PDCP SDU Volume, DL','PDCP SDU Volume, UL']
    y11_columns=['Avg PDCP cell thp DL','Avg PDCP cell thp UL']
    y12_columns=['Avg PDCP cell thp UL']
    y13_columns=['E-UTRAN Avg PRB usage per TTI DL','Avg PRB usage per TTI UL']
    y14_columns=['DL Spectral efficiency','UL Spectral efficiency']
    y15_columns=['E-RAB Stp SR, QCI9']
    y15_columns_=['E-RAB Stp Att, QCI9']
    y16_columns=['Avg IP thp DL QCI9','Avg IP thp UL QCI9']
    y17_columns=['Avg IP thp UL QCI9']
    y18_columns=['Avg PDCP SDU Delay DL QCI9']
    y19_columns=['Intra eNB HO prep SR']
    y19_columns_=['Failed Intra eNB Handover preparations due to other reasons','Failed Intra eNB Handover preparations due to Admission Control']
    y20_columns=['Intra eNB HO SR']
    y20_columns_=['Total intra eNB HO failures due to timer']
    y21_columns=['inter eNB E-UTRAN HO prep SR X2']
    y21_columns_=['Failed Inter-eNB X2 Handover preparations due to not supported QCI','Failed Inter eNB Handover preparations due to other reason','Failed Inter eNB Handover preparations due to timer','Failed Inter eNB Handover preparations due to target eNB admission control']
    y22_columns=['inter eNB E-UTRAN HO SR X2']
    y22_columns_=['Number of Inter eNB Handover failures']
    y23_columns=['E-UTRAN HO Prep SR, inter eNB S1']
    y23_columns_=['Failed Inter-eNB S1 Handover preparations due to not supported QCI','Failed Inter eNB S1-Handover preparations due to other reason','Failed Inter eNB S1-Handover preparations due to target eNB admission control','Failed Inter eNB S1-Handover preparations due to timer']
    y24_columns=['E-UTRAN HO SR, inter eNB S1']
    y24_columns_=['Inter eNB S1-HO failures due to timer']
    y25_columns=['E-UTRAN Intra-Freq HO SR']
    y26_columns=['Attempted intra eNB HO','Attempted inter eNB HO','Attempted inter eNB S1-HO']
    y27_columns=['% Ping Pong HO']
    y28_columns=['Avg Latency DL','Avg Latency Uplink']
    y29_columns=['PDCP SDU delay on DL DTCH Mean','PDCP SDU delay on UL DTCH Mean']
    y30_columns=['Avg SINR for PUCCH','Avg SINR for PUSCH']
    y31_columns=['Avg RSSI for PUCCH','Avg RSSI for PUSCH']
    y32_columns=['BLER DL','BLER UL']
    y33_columns=['Average CQI']
    y34_columns=['% PUSCH tx using low MCS','% PUSCH tx using high MCS','% PDSCH tx using low MCS','% PDSCH tx using high MCS']
    y35_columns=['MIMO CL Single CW Mode Usage','MIMO CL Double CW Mode Usage']
    y36_columns=['% MIMO RI 1','% MIMO RI 2','% MIMO RI 3','% MIMO RI 4']
    y37_columns=['E-UTRAN S1 Stp Att']
    y37_columns_=['S1 init ctx stp FR by NO_RESP','S1 stp FR indicated by MME']
    y38_columns=['E-RAB SFR RNL','E-RAB SFR TRPORT','E-RAB SFR RESOUR','E-RAB stp FR RNL','E-RAB stp FR misc','E-RAB stp FR mobil','E-RAB SFR OTH','E-RAB stp FR miss UE cap lic']
    y39_columns=['Avg Nr simult E-RABs QCI9','Max Nr simult E-RABs QCI9']
    #y39_columns_=['Max Nr simult E-RABs QCI9']
    y40_columns=['E-RAB Stp SR, QCI9']
    y41_columns=['Released active ERABs QCI9']
    y42_columns=['E-UTRAN E-RAB ret RAN v, RNL fail']
    y42_columns_=['E-UTRAN E-RAB DR, RAN View']
    y43_columns=['E-RAB DR, fail HO init eNB']
    y44_columns=['Avg UE distance']
    y46_columns=['S1 stp SR']
    y47_columns=['AGG1 used PDCCH','AGG2 used PDCCH','AGG4 used PDCCH','AGG8 used PDCCH']
    y48_columns=['CCE block R']
    y48_columns_=['AGG1 blocked PDCCH','AGG2 blocked PDCCH','AGG4 blocked PDCCH','AGG8 blocked PDCCH']

    #y45_columns=['ERAB_REL_ENB_RNL_INA']
    #y46_columns=['E-RAB Stp SR, QCI9']
    #y47_columns=['E-RAB Stp SR, QCI9']


    def create_figure(df, x_col, y1_cols, y2_cols, y1_name, y2_name, titleg):

        fig = go.Figure()
  

        for y1_col in y1_cols:
            fig.add_trace(go.Scatter(x=df[x_col], y=df[y1_col], name=y1_col,line=dict(width=2),yaxis='y2'))
        for y2_col in y2_cols:
            fig.add_trace(go.Bar(x=df[x_col], y=df[y2_col], name=y2_col,yaxis='y'))



        fig.update_layout(
            barmode='stack',
            width=6.5 * 96 * 1.5,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
            height=3 * 96 *1.5,   # 3 pulgadas convertidas a píxeles
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title=dict(text=titleg, x=0.5, y=0.9),
            yaxis=dict(
                title=f'{y2_name}',
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
                title=f'{y1_name}',
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


    def create_figure2(df, x_col, y1_cols, y1_name, titleg, caso):

        fig = go.Figure()

        for y1_col in y1_cols:
            fig.add_trace(go.Scatter(x=df[x_col], y=df[y1_col], name=y1_col,line=dict(width=2)))

        if caso == 0:
            fig.update_layout(
                width=6.5 * 96 * 1.5,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
                height=3 * 96 * 1.5,   # 3 pulgadas convertidas a píxeles
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                title=dict(text=titleg,x=0.5),
                yaxis=dict(
                    title=f'{y1_name}',
                    side='left',
                    showgrid=True,
                    gridcolor='lightgray',
                    gridwidth=1,
                    #dtick=0.2 
                    #range=[None, 100.5],
                    autorange = True,
                    fixedrange= False
                    ),
                xaxis=dict(
                        showgrid=False,
                    ))

        elif caso == 1:
            fig.update_layout(
                width=6.5 * 96 * 1.5,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
                height=3 * 96 * 1.5,   # 3 pulgadas convertidas a píxeles
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                title=dict(text=titleg,x=0.5),
                yaxis=dict(
                    title=f'{y1_name}',
                    side='left',
                    showgrid=True,
                    gridcolor='lightgray',
                    gridwidth=1,
                    #dtick=0.2 
                    #range=[None, 100.5],
                    autorange = True,
                    fixedrange= False
                    ),
                xaxis=dict(
                        showgrid=False,
                    ))   


        return fig

    def create_figure3(df, x_col, y1_cols, y1_name, titleg):

        fig = go.Figure()

        for y1_col in y1_cols:
            fig.add_trace(go.Bar(x=df[x_col], y=df[y1_col], name=y1_col))


        fig.update_layout(
            barmode='stack',
            width=6.5 * 96 * 1.5,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
            height=3 * 96 * 1.5,   # 3 pulgadas convertidas a píxeles
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title=dict(text=titleg,x=0.5),
            yaxis=dict(
                title=f'{y1_name}',
                side='left',
                showgrid=True,
                gridcolor='lightgray',
                gridwidth=1,
                #dtick=0.2 
                autorange = True,
                fixedrange= False
                ),
            xaxis=dict(
                    showgrid=False,
                ))
        return fig    

    def create_figure4(df, x_col, y1_cols, y1_name, titleg):

        fig = go.Figure()

        for y1_col in y1_cols:
            fig.add_trace(go.Bar(x=df[x_col], y=df[y1_col], name=y1_col))


        fig.update_layout(
            barmode='stack',
            width=6.5 * 96 * 2.2,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
            height=3 * 96 * 2.2,   # 3 pulgadas convertidas a píxeles
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title=dict(text=titleg,x=0.5),
            yaxis=dict(
                title=f'{y1_name}',
                side='left',
                showgrid=True,
                gridcolor='lightgray',
                gridwidth=1,
                #dtick=0.2 
                autorange = True,
                fixedrange= False
                ),
            xaxis=dict(
                    showgrid=False,
                ))
        return fig 

    def create_figure5(df, x_col, y1_cols, y2_cols, y1_name, y2_name, titleg):

        fig = go.Figure()

        for y1_col in y1_cols:
            fig.add_trace(go.Scatter(x=df[x_col], y=df[y1_col], name=y1_col,yaxis='y2'))
        for y2_col in y2_cols:
            fig.add_trace(go.Bar(x=df[x_col], y=df[y2_col], name=y2_col,yaxis='y'))


        fig.update_layout(
            barmode='stack',
            width=6.5 * 96 * 2.2,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
            height=3 * 96 * 2.2,   # 3 pulgadas convertidas a píxeles
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title=dict(text=titleg,x=0.5),
            yaxis=dict(
                title=f'{y2_name}',
                side='left',
                showgrid=True,
                gridcolor='lightgray',
                #gridwidth=1,
                #dtick=0.2 
                #range=[0, 120]
                autorange = True,
                fixedrange= True
            ),
            yaxis2=dict(
                title=f'{y1_name}',
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

    def create_figure6(df, x_col, y1_cols, y1_name, titleg):

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=df[x_col], y=df[y1_cols[0]], name=y1_cols[0],stackgroup='one',fillcolor='rgba (239, 85,59, 1)',line=dict(width=1, color='rgba (239, 85,59, 1)')))
        fig.add_trace(go.Scatter(x=df[x_col], y=df[y1_cols[1]], name=y1_cols[1], fill='tonexty',stackgroup='one',fillcolor='rgba(99, 110, 250, 1)',line=dict(width=1, color='rgba(99, 110, 250, 1)')))


        fig.update_layout(
            width=6.5 * 96 * 1.5,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
            height=3 * 96 * 1.5,   # 3 pulgadas convertidas a píxeles
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title=dict(text=titleg,x=0.5),
            yaxis=dict(
                title=f'{y1_name}',
                side='left',
                showgrid=True,
                gridcolor='lightgray',
                gridwidth=1,
                #dtick=0.2 
                #autorange = True,
                fixedrange= False
                ),
            xaxis=dict(
                    showgrid=False,
                ))
        return fig  

    def create_figure7(df, x_col, y1_cols, y1_name, titleg):

        fig = go.Figure()

        for y1_col in y1_cols:
            fig.add_trace(go.Scatter(x=df[x_col], y=df[y1_col], name=y1_col,line=dict(width=2)))

        rang=[0,None]


        fig.update_layout(
            width=6.5 * 96 * 1.5,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
            height=3 * 96 * 1.5,   # 3 pulgadas convertidas a píxeles
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title=dict(text=titleg,x=0.5),
            yaxis=dict(
                title=f'{y1_name}',
                side='left',
                showgrid=True,
                gridcolor='lightgray',
                gridwidth=1,
                #dtick=0.2 
                range = rang,
                fixedrange= False
                ),
            xaxis=dict(
                    showgrid=False,
                ))
        return fig 

    def create_figure8(df, x_col, y1_cols, y2_cols, y1_name, y2_name, titleg):

        fig = go.Figure()
  

        for y1_col in y1_cols:
            fig.add_trace(go.Bar(x=df[x_col], y=df[y1_col], name=y1_col,yaxis='y'))
        for y2_col in y2_cols:
            fig.add_trace(go.Scatter(x=df[x_col], y=df[y2_col], name=y2_col,line=dict(width=2),yaxis='y2'))



        fig.update_layout(
            barmode='stack',
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


    def create_figure9(df, x_col, y1_cols, y2_cols, y1_name, y2_name, titleg):

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


     
    fig1 = create_figure(dff, 'date_id', y1_columns,y1_columns_, '%','#','Total E-UTRAN RRC conn stp SR')
    fig2 = create_figure(dff, 'date_id', y2_columns,y2_columns_,  '%','#','RACH Stp Completion')
    fig3 = create_figure(dff, 'date_id', y3_columns,y3_columns_, '%','#','E-UTRAN E-RAB stp SR')
    fig4 = create_figure2(dff, 'date_id', y4_columns, '%','Cell Avail',0)
    #fig5 = create_figure3(dff, 'date_id', y5_columns, '#','RACH stp att')
    fig6 = create_figure4(dff, 'date_id', y6_columns, '#','RCC Failures')
    fig7 = create_figure5(dff, 'date_id', y7_columns,y7_columns_, '%','#','Causas Drop PS')
    fig8 = create_figure2(dff, 'date_id', y8_columns, '#','Avg UEs Connected y Act',1)
    #fig8 =go.Figure()
    fig9 = create_figure6(dff, 'date_id', y9_columns, '[MB]','PDCP SDU Volume')
    #fig10 = create_figure6(dff, 'date_id', y10_columns, '[MB]','PDCP SDU Volume, UL')
    fig11 = create_figure2(dff, 'date_id', y11_columns, '[kbps]','Avg PDCP cell thp',0)
    #fig12 = create_figure7(dff, 'date_id', y12_columns, '[kbps]','Avg PDCP cell thp UL')
    fig13 = create_figure2(dff, 'date_id', y13_columns, '%','E-UTRAN Avg PRB usage per TTI',1)
    fig14 = create_figure2(dff, 'date_id', y14_columns, '[bits/s]','Spectral efficiency',1)
    fig15 = create_figure(dff, 'date_id', y15_columns, y15_columns_, '%','#','E-RAB Stp QCI9')
    fig16 = create_figure2(dff, 'date_id', y16_columns, '%','Avg IP thp QCI9',0)
    #fig17 = create_figure7(dff, 'date_id', y17_columns, '%','Avg IP thp UL QCI9')
    fig18 = create_figure7(dff, 'date_id', y18_columns, 'ms','Avg PDCP SDU Delay DL QCI9')
    fig19 = create_figure(dff, 'date_id', y19_columns,y19_columns_, '%','#','Intra eNB HO prep SR')
    fig20 = create_figure(dff, 'date_id', y20_columns,y20_columns_, '%','#','Intra eNB HO SR')
    fig21 = create_figure(dff, 'date_id', y21_columns,y21_columns_, '%','#','inter eNB E-UTRAN HO prep SR X2')
    fig22 = create_figure(dff, 'date_id', y22_columns,y22_columns_, '%','#','inter eNB E-UTRAN HO SR X2')
    fig23 = create_figure5(dff, 'date_id', y23_columns,y23_columns_, '%','#','E-UTRAN HO Prep SR, inter eNB S1')
    fig24 = create_figure(dff, 'date_id', y24_columns,y24_columns_, '%','#','E-UTRAN HO SR, inter eNB S1')
    fig25 = create_figure2(dff, 'date_id', y25_columns, '%','E-UTRAN Intra-Freq HO SR',0)
    fig26 = create_figure3(dff, 'date_id', y26_columns, '#','Attempted HO')
    fig27 = create_figure2(dff, 'date_id', y27_columns, '%','% Ping Pong HO',0)
    fig28 = create_figure2(dff, 'date_id', y28_columns, '[ms]','Avg Latency',0)
    fig29 = create_figure2(dff, 'date_id', y29_columns, '[ms]','PDCP SDU delay',0)
    fig30 = create_figure2(dff, 'date_id', y30_columns, '[dB]','Avg SINR',0)
    fig31 = create_figure2(dff, 'date_id', y31_columns, '[dBm]','Avg RSSI',0)
    fig32 = create_figure2(dff, 'date_id', y32_columns, '%','BLER',0)
    fig33 = create_figure3(dff, 'date_id', y33_columns, '#','Average CQI')
    fig34 = create_figure2(dff, 'date_id', y34_columns, '%','MCS',0)
    fig35 = create_figure2(dff, 'date_id', y35_columns, '%','MIMO',0)
    fig36 = create_figure2(dff, 'date_id', y36_columns, '%','Rank Indicator',0)
    fig37 = create_figure8(dff, 'date_id', y37_columns,y37_columns_, '#','%','S1 Attempts _ Setup Failure')
    #fig37 =go.Figure()
    fig38 = create_figure2(dff, 'date_id', y38_columns, '%','E-RAB Failures',0)
    fig39 = create_figure3(dff, 'date_id', y39_columns, '#','Avg - Max Nr simult E-RABs QCI9')
    #fig39 = create_figure9(dff, 'date_id', y39_columns,y39_columns_, '#','#','Avg - Max Nr simult E-RABs QCI9')
    #fig40 = create_figure2(dff, 'date_id', y40_columns, '%','E-RAB Stp SR, QCI9',0)
    fig41 = create_figure2(dff, 'date_id', y41_columns, '%','Released active ERABs QCI9',0)
    fig42 = create_figure9(dff, 'date_id', y42_columns,y42_columns_, '#/h','%','E-UTRAN E-RAB ret RAN v, RNL fail')
    fig43 = create_figure2(dff, 'date_id', y43_columns, '%','E-RAB DR, fail HO init eNB',0)
    fig44 = create_figure2(dff, 'date_id', y44_columns, '[km]','Avg UE distance',0)
    fig46 = create_figure2(dff, 'date_id', y46_columns, '%','S1 stp SR',0)
    #fig45 = create_figure3(dff, 'date_id', y45_columns, '#','ERAB_REL_ENB_RNL_INA (M8006C255)')
    fig45 =go.Figure()
    #'eNB initiated E-RAB releases due to loss of connection to the UE','eNB initiated E-RAB releases due to insufficient transport resources','eNB initiated E-RAB releases due to missing radio resources','eNB initiated E-RAB releases due to E-UTRAN Generated Reason','E-RAB DR, RNL unspec ini eNB','E-RABs released due to failed Handover regardless of the bearers QCI','E-RABs released due to partial  Handover regardless of the bearers QCI','EPC initiated EPS Bearer Release requests due to Other causes','M8006C309','M8006C310','M8006C313','M8006C312','M8006C311'
    fig47 = create_figure3(dff, 'date_id', y47_columns, '#','Nivel de agregación PDCCH')
    fig48 = create_figure(dff, 'date_id', y48_columns,y48_columns_, '%','#','Bloqueos PDCCH')


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
    #fig5.update_layout(**layout_style)
    fig6.update_layout(**layout_style2)
    fig7.update_layout(**layout_style3)
    fig8.update_layout(**layout_style)
    fig9.update_layout(**layout_style)
    #fig10.update_layout(**layout_style)
    fig11.update_layout(**layout_style)
    #fig12.update_layout(**layout_style)
    fig13.update_layout(**layout_style)
    fig14.update_layout(**layout_style)
    fig15.update_layout(**layout_style)
    fig16.update_layout(**layout_style)
    #fig17.update_layout(**layout_style)
    fig18.update_layout(**layout_style)
    fig19.update_layout(**layout_style4)
    fig20.update_layout(**layout_style)
    fig21.update_layout(**layout_style4)
    fig22.update_layout(**layout_style)
    fig23.update_layout(**layout_style)
    fig24.update_layout(**layout_style)
    fig25.update_layout(**layout_style)
    fig26.update_layout(**layout_style)
    fig27.update_layout(**layout_style)
    fig28.update_layout(**layout_style)
    fig29.update_layout(**layout_style)
    fig30.update_layout(**layout_style)
    fig31.update_layout(**layout_style)
    fig32.update_layout(**layout_style)
    fig33.update_layout(**layout_style)
    fig34.update_layout(**layout_style)
    fig35.update_layout(**layout_style)
    fig36.update_layout(**layout_style)
    fig37.update_layout(**layout_style)
    fig38.update_layout(**layout_style)
    fig39.update_layout(**layout_style)
    #fig40.update_layout(**layout_style)
    fig41.update_layout(**layout_style)
    fig42.update_layout(**layout_style)
    fig43.update_layout(**layout_style)
    fig44.update_layout(**layout_style)
    fig45.update_layout(**layout_style)
    fig46.update_layout(**layout_style)
    fig47.update_layout(**layout_style)
    fig48.update_layout(**layout_style)  



    return fig1,fig2,fig3,fig4,fig6,fig7,fig8,fig9,fig11,fig13,fig14,fig15,fig16,fig18,fig19,fig20,fig21,fig22,fig23,fig24,fig25,fig26,fig27,fig28,fig29,fig30,fig31,fig32,fig33,fig34,fig35,fig36,fig37,fig38,fig39,fig41,fig42,fig43,fig44,fig45,fig46,fig47,fig48

# Definir el callback

@callback(
    [Output('PLMN-dropdown1', 'style'),
     Output('Sitios-dropdown1', 'style'),
     Output('Celdas-dropdown1', 'style'),
     Output('dropdown-sectorC', 'style')],
    [Input('poligonos-sitios-radio1', 'value')]
)
def update_input_visibility(option_selected,):

    if option_selected == 'PLMN':
        dropdown_style = {'display': 'block','width': '60%', 'fontSize': '12px'}
        input_style = {'display': 'none'}
        input_style_celdas = {'display': 'none'}
        dropdown_celda_style={'display': 'none'}
    if option_selected == 'Sitios':
        dropdown_style = {'display': 'none'}
        input_style = {'display': 'block','width': '60%', 'fontSize': '12px'}
        input_style_celdas = {'display': 'none'}
        dropdown_celda_style={'display': 'none'}
    elif option_selected == 'Celdas':
        # Puedes manejar 'celdas' de manera similar si es necesario
        dropdown_style = {'display': 'none'}
        input_style = {'display': 'none'}
        input_style_celdas = {'display': 'block','width': '60%', 'fontSize': '12px'}
        dropdown_celda_style={'display': 'block','width': '40%', 'fontSize': '12px'}

    return dropdown_style,input_style, input_style_celdas, dropdown_celda_style





# Definir la función de actualización del gráfico
@callback(
    [Output('graph-contentC', 'figure'),
     Output('graph-contentC2','figure'),
     Output('graph-contentC3','figure'),
     Output('graph-contentC4','figure'),
     #Output('graph-contentC5','figure'),
     Output('graph-contentC6','figure'),
     Output('graph-contentC7','figure'),
     Output('graph-contentC8','figure'),
     Output('graph-contentC9','figure'),
     #Output('graph-contentC10','figure'),
     Output('graph-contentC11','figure'),
     #Output('graph-contentC12','figure'),
     Output('graph-contentC13','figure'),
     Output('graph-contentC14','figure'),
     Output('graph-contentC15','figure'),
     Output('graph-contentC16','figure'),
     #Output('graph-contentC17','figure'),
     Output('graph-contentC18','figure'),
     Output('graph-contentC19','figure'),
     Output('graph-contentC20','figure'),
     Output('graph-contentC21','figure'),
     Output('graph-contentC22','figure'),
     Output('graph-contentC23','figure'),
     Output('graph-contentC24','figure'),
     Output('graph-contentC25','figure'),
     Output('graph-contentC26','figure'),
     Output('graph-contentC27','figure'),
     Output('graph-contentC28','figure'),
     Output('graph-contentC29','figure'),
     Output('graph-contentC30','figure'),
     Output('graph-contentC31','figure'),
     Output('graph-contentC32','figure'),
     Output('graph-contentC33','figure'),
     Output('graph-contentC34','figure'),
     Output('graph-contentC35','figure'),
     Output('graph-contentC36','figure'),
     Output('graph-contentC37','figure'),
     Output('graph-contentC38','figure'),
     Output('graph-contentC39','figure'),
     #Output('graph-contentC40','figure'),
     Output('graph-contentC41','figure'),
     Output('graph-contentC42','figure'),
     Output('graph-contentC43','figure'),
     Output('graph-contentC44','figure'),
     Output('graph-contentC45','figure'),
     Output('graph-contentC46','figure'),
     Output('graph-contentC47','figure'),
     Output('graph-contentC48','figure'),
     Output('dropdown-sectorC', 'options'),
     Output('dropdown-sectorC', 'value'),
     #Output('dropdown-sectorC', 'style'),
     Output('graph-contentC11','style'),
     Output('graph-contentC37','style'),
     Output('graph-contentC46','style'),
     Output('graph-contentC36','style')],
    [Input('btn-buscar1', 'n_clicks')],
    [State('date-range-picker1', 'start_date'),
     State('date-range-picker1', 'end_date'),
     State('PLMN-dropdown1', 'value'),
     State('Sitios-dropdown1', 'value'),
     State('Celdas-dropdown1', 'value'),  # Nuevo input para sitios
     State('poligonos-sitios-radio1', 'value'),
     State('time-radio1', 'value'),
     State('dropdown-sectorC', 'value'),  # Nuevo input para el dropdown
     Input('dropdown-sectorC', 'value')]
)
def update_graph(n_clicks, start_date, end_date,selected_poligonos_dropdown, selected_sitios_input,selected_celdas_input, option_selected,datetime_option,selected_cell,select_cell_value):
      # Asegurar que cached_data sea global

    global cached_data
    global cached_data2
    global cached_data3

    dropdown_fecha = pd.date_range(start=start_date, end=end_date, freq='D').strftime('%d-%m-%Y')
    # Verificar qué componente ha desencadenado la actualización
    triggered_component_id = ctx.triggered_id
    #print(triggered_component_id )
    if  (triggered_component_id == 'btn-buscar1' and selected_poligonos_dropdown) or (triggered_component_id == 'btn-buscar1' and selected_sitios_input) or (triggered_component_id == 'btn-buscar1' and selected_celdas_input):
        
        print('Spence:',datetime.now())

        if option_selected == 'PLMN':

            # Realizar consultas a la base de datos solo si el botón "Buscar" o algún dropdown ha desencadenado la actualización
            df = perform_database_queries(start_date, end_date, selected_poligonos_dropdown,option_selected,datetime_option)


            cached_data3 = {'df': df}


        elif option_selected == 'Sitios':
            
            # Realizar consultas a la base de datos solo si el botón "Buscar" o algún dropdown ha desencadenado la actualización

            df = perform_database_queries(start_date, end_date, selected_sitios_input,option_selected,datetime_option)
            cached_data = {'df': df}


        elif option_selected == 'Celdas':
            
            # Realizar consultas a la base de datos solo si el botón "Buscar" o algún dropdown ha desencadenado la actualización
            df = perform_database_queries(start_date, end_date, selected_celdas_input,option_selected,datetime_option)

            cached_data2 = {'df': df}



    if ((option_selected == 'PLMN') and (cached_data3 is not None)): 
        dropdown_celda_style={'display': 'none'}
        fig8_style={'display': 'flex', 'flex-wrap': 'wrap','justifyContent': 'center'}
        fig37_style={'display': 'flex', 'flex-wrap': 'wrap','justifyContent': 'center'}
        fig45_style={'display': 'none'}
        fig46_style={'display': 'flex', 'flex-wrap': 'wrap','justifyContent': 'center'}

        fig1,fig2,fig3,fig4,fig6,fig7,fig8,fig9,fig11,fig13,fig14,fig15,fig16,fig18,fig19,fig20,fig21,fig22,fig23,fig24,fig25,fig26,fig27,fig28,fig29,fig30,fig31,fig32,fig33,fig34,fig35,fig36,fig37,fig38,fig39,fig41,fig42,fig43,fig44,fig45,fig46,fig47,fig48 = generate_graph2(cached_data3['df']) 
        dropdown_sector_options=[]
           

    elif ((option_selected == 'Sitios') and (cached_data is not None)): 
        dropdown_celda_style={'display': 'none'}
        fig8_style={'display': 'flex', 'flex-wrap': 'wrap','justifyContent': 'center'}
        fig37_style={'display': 'flex', 'flex-wrap': 'wrap','justifyContent': 'center'}
        fig45_style={'display': 'none'}
        fig46_style={'display': 'flex', 'flex-wrap': 'wrap','justifyContent': 'center'}

        fig1,fig2,fig3,fig4,fig6,fig7,fig8,fig9,fig11,fig13,fig14,fig15,fig16,fig18,fig19,fig20,fig21,fig22,fig23,fig24,fig25,fig26,fig27,fig28,fig29,fig30,fig31,fig32,fig33,fig34,fig35,fig36,fig37,fig38,fig39,fig41,fig42,fig43,fig44,fig45,fig46,fig47,fig48 = generate_graph2(cached_data['df']) 
        dropdown_sector_options=[]
           

    elif ((option_selected == 'Celdas') and (cached_data2 is not None)):
        fig8_style={'display': 'none'}
        fig37_style={'display': 'none'} 
        fig45_style={'display': 'none'} 


        selected_cell = selected_cell or cached_data2['df']['lncel_name'].iloc[0]
        
        fig1,fig2,fig3,fig4,fig6,fig7,fig8,fig9,fig11,fig13,fig14,fig15,fig16,fig18,fig19,fig20,fig21,fig22,fig23,fig24,fig25,fig26,fig27,fig28,fig29,fig30,fig31,fig32,fig33,fig34,fig35,fig36,fig37,fig38,fig39,fig41,fig42,fig43,fig44,fig45,fig47,fig48 = generate_graph(cached_data2['df'],selected_cell)
        dropdown_sector_options = [{'label': cell, 'value': cell} for cell in cached_data2['df']['lncel_name'].unique()]
        
        fig46 = go.Figure()
        fig46_style={'display': 'none'} 

            #fig1 = generate_graphs(df)
    # elif triggered_component_id =='checklist1' or triggered_component_id == 'dropdown-Fecha1':
    #     #print(triggered_component_id)

    #     if cached_data is not None:
    #         df = cached_data['df']
    #         df = calculate_and_map_columns(df, dias, fecha)
    #         fig10 = generate_table(df)

            
    #     else:
    #         fig10 = None
    #         fig1 = go.Figure()


    else:

        
        fig1 = go.Figure()
        fig2 = go.Figure()
        fig3 = go.Figure()
        fig4 = go.Figure()
        #fig5 = go.Figure()
        fig6 = go.Figure()
        fig7 = go.Figure()
        fig8 = go.Figure()
        fig9 = go.Figure()
        #fig10 = go.Figure()
        fig11 = go.Figure()
        #fig12 = go.Figure()
        fig13 = go.Figure()
        fig14 = go.Figure()
        fig15 = go.Figure()
        fig16 = go.Figure()
        #fig17 = go.Figure()
        fig18 = go.Figure()
        fig19 = go.Figure()
        fig20 = go.Figure()
        fig21 = go.Figure()
        fig22 = go.Figure()
        fig23 = go.Figure()
        fig24 = go.Figure()
        fig25 = go.Figure()
        fig26 = go.Figure()
        fig27 = go.Figure()
        fig28 = go.Figure()
        fig29 = go.Figure()
        fig30 = go.Figure()
        fig31 = go.Figure()
        fig32 = go.Figure()
        fig33 = go.Figure()
        fig34 = go.Figure()
        fig35 = go.Figure()
        fig36 = go.Figure()
        fig37 = go.Figure()
        fig38 = go.Figure()
        fig39 = go.Figure()
        #fig40 = go.Figure()
        fig41 = go.Figure()
        fig42 = go.Figure()
        fig43 = go.Figure()
        fig44 = go.Figure()
        fig45 = go.Figure()
        fig46 = go.Figure()
        fig47 = go.Figure()
        fig48 = go.Figure()
        dropdown_sector_options=[]
        dropdown_celda_style={'display': 'none'}
        fig8_style={'display': 'none'}
        fig37_style={'display': 'none'} 
        fig45_style={'display': 'none'}
        fig46_style={'display': 'none'} 

        #dropdown_fecha=[]

        
        #config = {'sort_action':'native'}
    # Generar opciones para Dropdown
    return fig4,fig2,fig1,fig6,fig3,fig38,fig42,fig7,fig8,fig9,fig11,fig13,fig14,fig19,fig20,fig21,fig22,fig23,fig24,fig25,fig26,fig27,fig28,fig29,fig30,fig31,fig32,fig33,fig34,fig35,fig36,fig46,fig37,fig15,fig16,fig41,fig39,fig18,fig43,fig44,fig45,fig47,fig48, dropdown_sector_options, selected_cell,fig8_style,fig37_style,fig45_style,fig46_style

# Iniciar la aplicación si se ejecuta el script











