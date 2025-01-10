from dash import Dash, html, dcc, callback, Output, Input, callback_context, State, dash, ctx, register_page, dash_table
import plotly.express as px
import pandas as pd
import db_main_bhp as db
import dash_bootstrap_components as dbc
import plotly.graph_objects as go 
from datetime import datetime, timedelta


# Crear la aplicación Dash
#FLATLY
register_page(__name__, path="/KPIs")

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

variable_names = {'pdcp_sdu_delay_ul_dtch_min_m8001c3':'PDCP_SDU_DELAY_UL_DTCH_MIN (M8001C3)',
'pdcp_sdu_delay_dl_dtch_max_m8001c1':'PDCP_SDU_DELAY_DL_DTCH_MAX (M8001C1)',
'pdcp_sdu_delay_dl_dtch_mean_m8001c2':'PDCP_SDU_DELAY_DL_DTCH_MEAN (M8001C2)',
'pdcp_sdu_delay_dl_dtch_min_m8001c0':'PDCP_SDU_DELAY_DL_DTCH_MIN (M8001C0)',
'pdcp_sdu_delay_ul_dtch_max_m8001c4':'PDCP_SDU_DELAY_UL_DTCH_MAX (M8001C4)',
'pdcp_sdu_delay_ul_dtch_mean_m8001c5':'PDCP_SDU_DELAY_UL_DTCH_MEAN (M8001C5)',
'pusch_trans_using_mcs28_m8001c44':'PUSCH_TRANS_USING_MCS28 (M8001C44)',
'pusch_trans_using_mcs0_m8001c16':'PUSCH_TRANS_USING_MCS0 (M8001C16)',
'pusch_trans_using_mcs1_m8001c17':'PUSCH_TRANS_USING_MCS1 (M8001C17)',
'pusch_trans_using_mcs2_m8001c18':'PUSCH_TRANS_USING_MCS2 (M8001C18)',
'pusch_trans_using_mcs3_m8001c19':'PUSCH_TRANS_USING_MCS3 (M8001C19)',
'pusch_trans_using_mcs4_m8001c20':'PUSCH_TRANS_USING_MCS4 (M8001C20)',
'pusch_trans_using_mcs5_m8001c21':'PUSCH_TRANS_USING_MCS5 (M8001C21)',
'pusch_trans_using_mcs6_m8001c22':'PUSCH_TRANS_USING_MCS6 (M8001C22)',
'pusch_trans_using_mcs7_m8001c23':'PUSCH_TRANS_USING_MCS7 (M8001C23)',
'pusch_trans_using_mcs8_m8001c24':'PUSCH_TRANS_USING_MCS8 (M8001C24)',
'pusch_trans_using_mcs9_m8001c25':'PUSCH_TRANS_USING_MCS9 (M8001C25)',
'pusch_trans_using_mcs10_m8001c26':'PUSCH_TRANS_USING_MCS10 (M8001C26)',
'pusch_trans_using_mcs11_m8001c27':'PUSCH_TRANS_USING_MCS11 (M8001C27)',
'pusch_trans_using_mcs12_m8001c28':'PUSCH_TRANS_USING_MCS12 (M8001C28)',
'pusch_trans_using_mcs13_m8001c29':'PUSCH_TRANS_USING_MCS13 (M8001C29)',
'pusch_trans_using_mcs14_m8001c30':'PUSCH_TRANS_USING_MCS14 (M8001C30)',
'pusch_trans_using_mcs15_m8001c31':'PUSCH_TRANS_USING_MCS15 (M8001C31)',
'pusch_trans_using_mcs16_m8001c32':'PUSCH_TRANS_USING_MCS16 (M8001C32)',
'pusch_trans_using_mcs17_m8001c33':'PUSCH_TRANS_USING_MCS17 (M8001C33)',
'pusch_trans_using_mcs18_m8001c34':'PUSCH_TRANS_USING_MCS18 (M8001C34)',
'pusch_trans_using_mcs19_m8001c35':'PUSCH_TRANS_USING_MCS19 (M8001C35)',
'pusch_trans_using_mcs20_m8001c36':'PUSCH_TRANS_USING_MCS20 (M8001C36)',
'pusch_trans_using_mcs21_m8001c37':'PUSCH_TRANS_USING_MCS21 (M8001C37)',
'pusch_trans_using_mcs22_m8001c38':'PUSCH_TRANS_USING_MCS22 (M8001C38)',
'pusch_trans_using_mcs23_m8001c39':'PUSCH_TRANS_USING_MCS23 (M8001C39)',
'pusch_trans_using_mcs24_m8001c40':'PUSCH_TRANS_USING_MCS24 (M8001C40)',
'pusch_trans_using_mcs25_m8001c41':'PUSCH_TRANS_USING_MCS25 (M8001C41)',
'pusch_trans_using_mcs26_m8001c42':'PUSCH_TRANS_USING_MCS26 (M8001C42)',
'pusch_trans_using_mcs27_m8001c43':'PUSCH_TRANS_USING_MCS27 (M8001C43)',
'cell_avail':'Cell Avail',
'cell_avail_excl_blu':'Cell Avail excl BLU',
'rach_stp_completion_sr':'RACH Stp Completion SR',
'rach_stp_att':'RACH stp att',
's1_stp_sr':'S1 stp SR',
'total_e_utran_rrc_conn_stp_sr':'Total E-UTRAN RRC conn stp SR',
'rrc_rel':'RRC Rel',
'n_o_s_c_e_r_r_d_t_mme_o':'Number of Signaling Connection Establishment Requests rejected due to MME overload',
'n_o_s_c_e_r_r_d_t_t_f_t_m_n_o_rrc_c':'Number of Signaling Connection Establishment Requests rejected due to threshold for the maximum number of RRC connections',
'n_o_s_c_e_r_r_d_t_l_o_pucch_r':'Number of Signaling Connection Establishment Requests rejected due to lack of PUCCH resources',
'n_o_s_c_e_r_r_d_t_u_p_o':'Number of Signaling Connection Establishment Requests rejected due to User Plane overload',
'n_o_s_c_e_r_r_d_t_c_p_o':'Number of Signaling Connection Establishment Requests rejected due to Control Plane overload',
's_c_e_f_d_t_rrc_s_c_e':'Signaling Connection Establishment failures due to RRC Setup completions error',
's_c_e_f_d_t_rrc_s_c_m':'Signaling Connection Establishment failures due to RRC Setup completions missing',
's_c_e_f_f_e_c_d_t_m_rb_r':'Signaling Connection Establishment failures for emergency calls due to missing RB resources',
'e_utran_e_rab_dr_ran_view':'E-UTRAN E-RAB DR, RAN View',
'e_utran_e_rab_ret_ran_v_rnl_fail':'E-UTRAN E-RAB ret RAN v, RNL fail',
'enb_initiated_e_rab_releases_due_to_loss_of_connection_to_the_ue':'eNB initiated E-RAB releases due to loss of connection to the UE',
'enb_i_e_rab_r_d_t_i_t_r':'eNB initiated E-RAB releases due to insufficient transport resources',
'e_rab_dr_rnl_unspec_ini_enb':'E-RAB DR, RNL unspec ini eNB',
'enb_initiated_e_rab_releases_due_to_missing_radio_resources':'eNB initiated E-RAB releases due to missing radio resources',
'e_rab_r_d_t_f_h_r_o_t_b_qci':'E-RABs released due to failed Handover regardless of the bearers QCI',
'enb_initiated_e_rab_releases_due_to_e_utran_generated_reason':'eNB initiated E-RAB releases due to E-UTRAN Generated Reason',
'm8006c309':'M8006C309',
'm8006c310':'M8006C310',
'm8006c313':'M8006C313',
'm8006c312':'M8006C312',
'm8006c311':'M8006C311',
'e_rab_r_d_t_p_h_r_o_t_b_qci':'E-RABs released due to partial Handover regardless of the bearers QCI',
'epc_initiated_eps_bearer_release_requests_due_to_other_causes':'EPC initiated EPS Bearer Release requests due to Other causes',
'epc_i_eps_b_r_r_d_t_r_n_l_c':'EPC initiated EPS Bearer Release requests due to Radio Network Layer cause',
'epc_initiated_e_rab_releases_due_to_path_switch':'EPC initiated E-RAB releases due to Path Switch',
'enb_i_e_rab_r_d_t_a_f_h_c_p_a_t_c':'eNB initiated E-RAB releases due to a failed Handover Completion phase at target cell',
'm8006c314':'M8006C314',
'avg_act_connected_ues':'Avg Act connected UEs',
'avg_rrc_conn_ue':'Avg RRC conn UE',
'pdcp_sdu_volume_dl':'PDCP SDU Volume, DL',
'pdcp_sdu_volume_ul':'PDCP SDU Volume, UL',
'avg_pdcp_cell_thp_dl':'Avg PDCP cell thp DL',
'avg_pdcp_cell_thp_ul':'Avg PDCP cell thp UL',
'e_utran_avg_prb_usage_per_tti_dl':'E-UTRAN Avg PRB usage per TTI DL',
'avg_prb_usage_per_tti_ul':'Avg PRB usage per TTI UL',
'dl_spectral_efficiency':'DL Spectral efficiency',
'ul_spectral_efficiency':'UL Spectral efficiency',
'e_rab_stp_att_qci4':'E-RAB Stp Att, QCI4',
'e_rab_stp_sr_qci4':'E-RAB Stp SR, QCI4',
'avg_ip_thp_dl_qci4':'Avg IP thp DL QCI4',
'avg_ip_thp_ul_qci4':'Avg IP thp UL QCI4',
'avg_latency_dl_qci4_drbs':'Avg Latency, DL, QCI4 DRBs',
'avg_pdcp_sdu_delay_dl_qci4':'Avg PDCP SDU Delay DL QCI4',
'e_rab_stp_att_qci9':'E-RAB Stp Att, QCI9',
'e_rab_stp_att_qci5':'E-RAB Stp Att, QCI5',
'avg_ip_thp_dl_qci9':'Avg IP thp DL QCI9',
'avg_ip_thp_dl_qci5':'Avg IP thp DL QCI5',
'avg_ip_thp_ul_qci9':'Avg IP thp UL QCI9',
'avg_ip_thp_ul_qci5':'Avg IP thp UL QCI5',
'avg_pdcp_sdu_delay_dl_qci9':'Avg PDCP SDU Delay DL QCI9',
'avg_pdcp_sdu_delay_dl_qci5':'Avg PDCP SDU Delay DL QCI5',
'intra_enb_ho_prep_sr':'Intra eNB HO prep SR',
'failed_intra_enb_handover_preparations_due_to_other_reasons':'Failed Intra eNB Handover preparations due to other reasons',
'failed_intra_enb_handover_preparations_due_to_admission_control':'Failed Intra eNB Handover preparations due to Admission Control',
'intra_enb_ho_sr':'Intra eNB HO SR',
'total_intra_enb_ho_failures_due_to_timer':'Total intra eNB HO failures due to timer',
'inter_enb_e_utran_ho_prep_sr_x2':'inter eNB E-UTRAN HO prep SR X2',
'f_i_enb_x_h_p_d_t_n_s_qci':'Failed Inter-eNB X2 Handover preparations due to not supported QCI',
'failed_inter_enb_handover_preparations_due_to_other_reason':'Failed Inter eNB Handover preparations due to other reason',
'failed_inter_enb_handover_preparations_due_to_timer':'Failed Inter eNB Handover preparations due to timer',
'f_i_enb_h_p_d_t_t_enb_a_c':'Failed Inter eNB Handover preparations due to target eNB admission control',
'inter_enb_e_utran_ho_sr_x2':'inter eNB E-UTRAN HO SR X2',
'number_of_inter_enb_handover_failures':'Number of Inter eNB Handover failures',
'e_utran_ho_prep_sr_inter_enb_s1':'E-UTRAN HO Prep SR, inter eNB S1',
'f_i_enb_s_h_p_d_t_n_s_qci':'Failed Inter-eNB S1 Handover preparations due to not supported QCI',
'failed_inter_enb_s1_handover_preparations_due_to_other_reason':'Failed Inter eNB S1-Handover preparations due to other reason',
'f_i_enb_s_h_p_d_t_t_enb_a_c':'Failed Inter eNB S1-Handover preparations due to target eNB admission control',
'failed_inter_enb_s1_handover_preparations_due_to_timer':'Failed Inter eNB S1-Handover preparations due to timer',
'e_utran_ho_sr_inter_enb_s1':'E-UTRAN HO SR, inter eNB S1',
'inter_enb_s1_ho_failures_due_to_timer':'Inter eNB S1-HO failures due to timer',
'e_utran_intra_freq_ho_sr':'E-UTRAN Intra-Freq HO SR',
'attempted_intra_enb_ho':'Attempted intra eNB HO',
'attempted_inter_enb_ho':'Attempted inter eNB HO',
'attempted_inter_enb_s1_ho':'Attempted inter eNB S1-HO',
'_ping_pong_ho':'% Ping Pong HO',
'avg_latency_dl':'Avg Latency DL',
'avg_latency_uplink':'Avg Latency Uplink',
'pdcp_sdu_delay_on_dl_dtch_mean':'PDCP SDU delay on DL DTCH Mean',
'pdcp_sdu_delay_on_ul_dtch_mean':'PDCP SDU delay on UL DTCH Mean',
'avg_sinr_for_pucch':'Avg SINR for PUCCH',
'avg_sinr_for_pusch':'Avg SINR for PUSCH',
'avg_rssi_for_pucch':'Avg RSSI for PUCCH',
'avg_rssi_for_pusch':'Avg RSSI for PUSCH',
'bler_dl':'BLER DL',
'bler_ul':'BLER UL',
'average_cqi':'Average CQI',
'_pusch_tx_using_low_mcs':'% PUSCH tx using low MCS',
'_pusch_tx_using_high_mcs':'% PUSCH tx using high MCS',
'_pdsch_tx_using_low_mcs':'% PDSCH tx using low MCS',
'_pdsch_tx_using_high_mcs':'% PDSCH tx using high MCS',
'mimo_cl_single_cw_mode_usage':'MIMO CL Single CW Mode Usage',
'mimo_cl_double_cw_mode_usage':'MIMO CL Double CW Mode Usage',
'_mimo_ri_1':'% MIMO RI 1',
'_mimo_ri_2':'% MIMO RI 2',
'_mimo_ri_3':'% MIMO RI 3',
'_mimo_ri_4':'% MIMO RI 4',
's1_init_ctx_stp_fr_by_no_resp':'S1 init ctx stp FR by NO_RESP',
's1_stp_fr_indicated_by_mme':'S1 stp FR indicated by MME',
'e_utran_s1_stp_att':'E-UTRAN S1 Stp Att',
'e_utran_e_rab_stp_sr':'E-UTRAN E-RAB stp SR',
'e_utran_e_rab_setup_attempts':'E-UTRAN E-RAB Setup Attempts',
'e_rab_sfr_rnl':'E-RAB SFR RNL',
'e_rab_sfr_trport':'E-RAB SFR TRPORT',
'e_rab_sfr_resour':'E-RAB SFR RESOUR',
'e_rab_stp_fr_rnl':'E-RAB stp FR RNL',
'e_rab_stp_fr_misc':'E-RAB stp FR misc',
'e_rab_stp_fr_mobil':'E-RAB stp FR mobil',
'e_rab_sfr_oth':'E-RAB SFR OTH',
'e_rab_stp_fr_miss_ue_cap_lic':'E-RAB stp FR miss UE cap lic',
'avg_nr_simult_e_rabs_qci4':'Avg Nr simult E-RABs QCI4',
'max_nr_simult_e_rabs_qci4':'Max Nr simult E-RABs QCI4',
'e_utran_e_rab_act_time_qci4':'E-UTRAN E-RAB act time QCI4',
'avg_nr_simult_e_rabs_qci9':'Avg Nr simult E-RABs QCI9',
'max_nr_simult_e_rabs_qci9':'Max Nr simult E-RABs QCI9',
'e_rab_stp_sr_qci9':'E-RAB Stp SR, QCI9',
'e_rab_stp_sr_qci5':'E-RAB Stp SR, QCI5',
'released_active_erabs_qci4':'Released active ERABs QCI4',
'released_active_erabs_qci9':'Released active ERABs QCI9',
'released_active_erabs_qci5':'Released active ERABs QCI5',
'cce_block_r':'CCE block R',
'pdcp_sdu_disc_r_dl':'PDCP SDU disc R DL',
'e_utran_pdcp_sdu_disc_r_dl_qci1':'E-UTRAN PDCP SDU disc R DL QCI1',
'e_utran_pdcp_sdu_disc_r_dl_qci2':'E-UTRAN PDCP SDU disc R DL QCI2',
'e_utran_pdcp_sdu_disc_r_dl_qci3':'E-UTRAN PDCP SDU disc R DL QCI3',
'pdcp_sdu_disc_r_dl_qci4':'PDCP SDU disc R DL, QCI4',
'pdcp_sdu_disc_r_dl_non_gbr':'PDCP SDU disc R DL, non GBR',
'e_utran_pdcp_sdu_dl_lr':'E-UTRAN PDCP SDU DL LR',
'e_utran_pdcp_sdu_dl_qci1_lr':'E-UTRAN PDCP SDU DL QCI1 LR',
'e_utran_pdcp_sdu_lr_dl_qci2':'E-UTRAN PDCP SDU LR DL QCI2',
'e_utran_pdcp_sdu_lr_dl_qci3':'E-UTRAN PDCP SDU LR DL QCI3',
'e_utran_pdcp_sdu_dl_lr_qci4':'E-UTRAN PDCP SDU DL LR, QCI4',
'e_utran_pdcp_sdu_dl_lr_qci5':'E-UTRAN PDCP SDU DL LR, QCI5',
'e_utran_pdcp_sdu_dl_lr_qci6':'E-UTRAN PDCP SDU DL LR, QCI6',
'e_utran_pdcp_sdu_dl_lr_qci7':'E-UTRAN PDCP SDU DL LR, QCI7',
'e_utran_pdcp_sdu_dl_lr_qci8':'E-UTRAN PDCP SDU DL LR, QCI8',
'e_utran_pdcp_sdu_dl_lr_qci9':'E-UTRAN PDCP SDU DL LR, QCI9',
'e_utran_pdcp_sdu_lr_ul':'E-UTRAN PDCP SDU LR UL',
'e_utran_pdcp_sdu_lr_ul_qci1':'E-UTRAN PDCP SDU LR UL QCI1',
'e_utran_pdcp_sdu_lr_ul_qci2':'E-UTRAN PDCP SDU LR UL QCI2',
'e_utran_pdcp_sdu_lr_ul_qci3':'E-UTRAN PDCP SDU LR UL QCI3',
'e_utran_pdcp_sdu_lr_ul_qci4':'E-UTRAN PDCP SDU LR UL QCI4',
'e_utran_pdcp_sdu_lr_ul_qci5':'E-UTRAN PDCP SDU LR UL QCI5',
'e_utran_pdcp_sdu_lr_ul_qci6':'E-UTRAN PDCP SDU LR UL QCI6',
'e_utran_pdcp_sdu_lr_ul_qci7':'E-UTRAN PDCP SDU LR UL QCI7',
'e_utran_pdcp_sdu_lr_ul_qci8':'E-UTRAN PDCP SDU LR UL QCI8',
'e_utran_pdcp_sdu_lr_ul_qci9':'E-UTRAN PDCP SDU LR UL QCI9',
'fract_lost_pdcp_sdu_ul_qci1':'Fract lost PDCP SDU UL QCI1',
'fract_lost_pdcp_sdu_ul_qci2':'Fract lost PDCP SDU UL QCI2',
'fract_lost_pdcp_sdu_ul_qci3':'Fract lost PDCP SDU UL QCI3',
'fract_lost_pdcp_sdu_ul_qci4':'Fract lost PDCP SDU UL QCI4',
'fract_lost_pdcp_sdu_ul_qci5':'Fract lost PDCP SDU UL QCI5',
'fract_lost_pdcp_sdu_ul_qci6':'Fract lost PDCP SDU UL QCI6',
'fract_lost_pdcp_sdu_ul_qci7':'Fract lost PDCP SDU UL QCI7',
'fract_lost_pdcp_sdu_ul_qci8':'Fract lost PDCP SDU UL QCI8',
'fract_lost_pdcp_sdu_ul_qci9':'Fract lost PDCP SDU UL QCI9',
'perc_pdcp_sdu_ul_qci_1':'Perc PDCP SDU UL QCI 1',
'perc_pdcp_sdu_ul_qci_2':'Perc PDCP SDU UL QCI 2',
'perc_pdcp_sdu_ul_qci_3':'Perc PDCP SDU UL QCI 3',
'perc_pdcp_sdu_ul_qci_4':'Perc PDCP SDU UL QCI 4',
'pdcp_sdu_ul_qci_1':'PDCP SDU UL QCI 1',
'pdcp_sdu_ul_qci_2':'PDCP SDU UL QCI 2',
'pdcp_sdu_ul_qci_3':'PDCP SDU UL QCI 3',
'pdcp_sdu_ul_qci_4':'PDCP SDU UL QCI 4',
'perc_pdcp_sdu_dl_qci_1':'Perc PDCP SDU DL QCI 1',
'perc_pdcp_sdu_dl_qci_2':'Perc PDCP SDU DL QCI 2',
'perc_pdcp_sdu_dl_qci_3':'Perc PDCP SDU DL QCI 3',
'perc_pdcp_sdu_dl_qci_4':'Perc PDCP SDU DL QCI 4',
'pdcp_sdu_dl_qci_1':'PDCP SDU DL QCI 1',
'pdcp_sdu_dl_qci_2':'PDCP SDU DL QCI 2',
'pdcp_sdu_dl_qci_3':'PDCP SDU DL QCI 3',
'pdcp_sdu_dl_qci_4':'PDCP SDU DL QCI 4',
'rlc_sdu_dv__dl_dcch':'RLC SDU DV DL DCCH',
'rlc_sdu_dv__ul_dcch':'RLC SDU DV UL DCCH',
'avg_rlc_cell_thp_ul':'Avg RLC Cell Thp UL',
'avg_rlc_layer_cell_thp_dl':'Avg RLC Layer cell thp, DL',
'e_utran_rlc_pdu_vol_ul':'E-UTRAN RLC PDU Vol UL',
'rlc_pdu_vol_dl':'RLC PDU Vol DL',
'pdcp_sdu_dv__euu_intf_ul':'PDCP SDU DV eUu Intf UL',
'pdcp_sdu_dv__euu_intf_dl':'PDCP SDU DV eUu Intf DL',
'rrc_ul_traffic_vol__euu':'RRC Ul Traffic Vol eUu',
'rrc_dl_traffic_vol__euu':'RRC Dl Traffic Vol eUu',
'rlc_sdu_ul_dtch_traffic_vol':'RLC SDU UL-DTCH Traffic Vol',
'rlc_sdu_dl_dtch_traffic_vol':'RLC SDU DL-DTCH Traffic Vol',
'perc__retrans_traffic_ul_sch':'Perc ReTrans Traffic UL_SCH',
'perc__retrans_traffic_dl_sch':'Perc ReTrans Traffic DL_SCH',
'mac_sdu_vol__ul_ccch':'MAC SDU Vol UL-CCCH',
'mac_sdu_vol__ul_dcch':'MAC SDU Vol UL-DCCH',
'mac_sdu_vol__ul_dtch':'MAC SDU Vol UL-DTCH',
'mac_sdu_vol__dl_ccch':'MAC SDU Vol DL-CCCH',
'mac_sdu_vol__dl_dcch':'MAC SDU Vol DL-DCCH',
'mac_sdu_vol__dl_dtch':'MAC SDU Vol DL-DTCH',
'rlc_sdus_on_bcch':'RLC SDUs on BCCH',
'rlc_sdus_on_dl_ccch':'RLC SDUs on DL CCCH',
'rlc_sdus_on_pcch':'RLC SDUs on PCCH',
'rlc_sdus_on_ul_ccch':'RLC SDUs on UL CCCH',
'minimum_queue_length_dl_srb':'Minimum queue length DL SRB',
'average_queue_length_dl_srb':'Average queue length DL SRB',
'maximum_queue_length_dl_srb':'Maximum queue length DL SRB',
'minimum_queue_length_dl_drb':'Minimum queue length DL DRB',
'average_queue_length_dl_drb':'Average queue length DL DRB',
'maximum_queue_length_dl_drb':'Maximum queue length DL DRB',
'e_utran_pdcch_order_att_sr':'E-UTRAN PDCCH Order Att SR',
'number_of_pdcch_order_attempts':'Number of PDCCH order attempts',
'number_of_initial_pdcch_order_attempts':'Number of initial PDCCH order attempts',
'unavailability_of_dedicated_preamble':'Unavailability of dedicated preamble',
'unavailability_of_dedicated_preamble_for_pdcch_order_purposes':'Unavailability of dedicated preamble for PDCCH order purposes',
'unavailability_of_dedicated_preamble_for_handover_purposes':'Unavailability of dedicated preamble for handover purposes',
'number_of_ue_state_transitions_from_ul_in_sync_to_ul_out_of_sync':'Number of UE state transitions from UL-In-Sync to UL-Out-Of-Sync',
'avg_nr_ues_ul_sync':'Avg nr UEs UL sync',
'average_number_of_ues_with_unlimited_power_supply_resources':'Average number of UEs with unlimited power supply resources',
'ue_ul_o_o_s_t_t_i_t_r_0_s_<_t_<_0_s':'UE UL-Out-Of-Sync time T in the range 0 seconds < T <= 0.5 seconds',
'ue_ul_o_o_s_t_t_i_t_r_0_s_<_t_<_2_s':'UE UL-Out-Of-Sync time T in the range 0.5 seconds < T <= 2.5 seconds',
'ue_ul_o_o_s_t_t_i_t_r_2_s_<_t_<_1_s':'UE UL-Out-Of-Sync time T in the range 2.5 seconds < T <= 10 seconds',
'ue_ul_o_o_s_t_t_i_t_r_1_s_<_t_<_1_s':'UE UL-Out-Of-Sync time T in the range 10 seconds < T <= 100 seconds',
'ue_ul_out_of_sync_time_t_larger_than_100_seconds':'UE UL-Out-Of-Sync time T larger than 100 seconds',
'perc_time_cell_c_plane_overload':'Perc time cell C-Plane overload',
'_ctrl_pln_overld_1':'% ctrl pln overld 1',
'_ctrl_pln_overld_2':'% ctrl pln overld 2',
'perc_time_cell_u_plane_overload':'Perc time cell U-Plane overload',
'mac_pdu_vol_pdsch_mcs0':'MAC PDU Vol PDSCH MCS0',
'mac_pdu_vol_pdsch_mcs1':'MAC PDU Vol PDSCH MCS1',
'mac_pdu_vol_pdsch_mcs2':'MAC PDU Vol PDSCH MCS2',
'mac_pdu_vol_pdsch_mcs3':'MAC PDU Vol PDSCH MCS3',
'mac_pdu_vol_pdsch_mcs4':'MAC PDU Vol PDSCH MCS4',
'mac_pdu_vol_pdsch_mcs5':'MAC PDU Vol PDSCH MCS5',
'mac_pdu_vol_pdsch_mcs6':'MAC PDU Vol PDSCH MCS6',
'mac_pdu_vol_pdsch_mcs7':'MAC PDU Vol PDSCH MCS7',
'mac_pdu_vol_pdsch_mcs8':'MAC PDU Vol PDSCH MCS8',
'mac_pdu_vol_pdsch_mcs9':'MAC PDU Vol PDSCH MCS9',
'mac_pdu_vol_pdsch_mcs10':'MAC PDU Vol PDSCH MCS10',
'mac_pdu_vol_pdsch_mcs11':'MAC PDU Vol PDSCH MCS11',
'mac_pdu_vol_pdsch_mcs12':'MAC PDU Vol PDSCH MCS12',
'mac_pdu_vol_pdsch_mcs13':'MAC PDU Vol PDSCH MCS13',
'mac_pdu_vol_pdsch_mcs14':'MAC PDU Vol PDSCH MCS14',
'mac_pdu_vol_pdsch_mcs15':'MAC PDU Vol PDSCH MCS15',
'mac_pdu_vol_pdsch_mcs16':'MAC PDU Vol PDSCH MCS16',
'mac_pdu_vol_pdsch_mcs17':'MAC PDU Vol PDSCH MCS17',
'mac_pdu_vol_pdsch_mcs18':'MAC PDU Vol PDSCH MCS18',
'mac_pdu_vol_pdsch_mcs19':'MAC PDU Vol PDSCH MCS19',
'mac_pdu_vol_pdsch_mcs20':'MAC PDU Vol PDSCH MCS20',
'mac_pdu_vol_pdsch_mcs21':'MAC PDU Vol PDSCH MCS21',
'mac_pdu_vol_pdsch_mcs22':'MAC PDU Vol PDSCH MCS22',
'mac_pdu_vol_pdsch_mcs23':'MAC PDU Vol PDSCH MCS23',
'mac_pdu_vol_pdsch_mcs24':'MAC PDU Vol PDSCH MCS24',
'mac_pdu_vol_pdsch_mcs25':'MAC PDU Vol PDSCH MCS25',
'mac_pdu_vol_pdsch_mcs26':'MAC PDU Vol PDSCH MCS26',
'mac_pdu_vol_pdsch_mcs27':'MAC PDU Vol PDSCH MCS27',
'mac_pdu_vol_pdsch_mcs28':'MAC PDU Vol PDSCH MCS28',
'mac_pdu_vol_pdsch_mcs0_1':'MAC PDU Vol PDSCH MCS0.1',
'mac_pdu_vol_pdsch_mcs0_2':'MAC PDU Vol PDSCH MCS0.2',
'mac_pdu_vol_pdsch_mcs0_3':'MAC PDU Vol PDSCH MCS0.3',
'mac_pdu_vol_pusch_mcs0':'MAC PDU Vol PUSCH MCS0',
'mac_pdu_vol_pusch_mcs1':'MAC PDU Vol PUSCH MCS1',
'mac_pdu_vol_pusch_mcs2':'MAC PDU Vol PUSCH MCS2',
'mac_pdu_vol_pusch_mcs3':'MAC PDU Vol PUSCH MCS3',
'mac_pdu_vol_pusch_mcs4':'MAC PDU Vol PUSCH MCS4',
'mac_pdu_vol_pusch_mcs5':'MAC PDU Vol PUSCH MCS5',
'mac_pdu_vol_pusch_mcs6':'MAC PDU Vol PUSCH MCS6',
'mac_pdu_vol_pusch_mcs7':'MAC PDU Vol PUSCH MCS7',
'mac_pdu_vol_pusch_mcs8':'MAC PDU Vol PUSCH MCS8',
'mac_pdu_vol_pusch_mcs9':'MAC PDU Vol PUSCH MCS9',
'mac_pdu_vol_pusch_mcs10':'MAC PDU Vol PUSCH MCS10',
'mac_pdu_vol_pusch_mcs11':'MAC PDU Vol PUSCH MCS11',
'mac_pdu_vol_pusch_mcs12':'MAC PDU Vol PUSCH MCS12',
'mac_pdu_vol_pusch_mcs13':'MAC PDU Vol PUSCH MCS13',
'mac_pdu_vol_pusch_mcs14':'MAC PDU Vol PUSCH MCS14',
'mac_pdu_vol_pusch_mcs15':'MAC PDU Vol PUSCH MCS15',
'mac_pdu_vol_pusch_mcs16':'MAC PDU Vol PUSCH MCS16',
'mac_pdu_vol_pusch_mcs17':'MAC PDU Vol PUSCH MCS17',
'mac_pdu_vol_pusch_mcs18':'MAC PDU Vol PUSCH MCS18',
'mac_pdu_vol_pusch_mcs19':'MAC PDU Vol PUSCH MCS19',
'mac_pdu_vol_pusch_mcs20':'MAC PDU Vol PUSCH MCS20',
'mac_pdu_vol_pusch_mcs21':'MAC PDU Vol PUSCH MCS21',
'mac_pdu_vol_pusch_mcs22':'MAC PDU Vol PUSCH MCS22',
'mac_pdu_vol_pusch_mcs23':'MAC PDU Vol PUSCH MCS23',
'mac_pdu_vol_pusch_mcs24':'MAC PDU Vol PUSCH MCS24',
'mac_pdu_vol_pusch_mcs25':'MAC PDU Vol PUSCH MCS25',
'mac_pdu_vol_pusch_mcs26':'MAC PDU Vol PUSCH MCS26',
'mac_pdu_vol_pusch_mcs27':'MAC PDU Vol PUSCH MCS27',
'mac_pdu_vol_pusch_mcs28':'MAC PDU Vol PUSCH MCS28',
'ue_pwr_headroom__pusch_lev_1':'UE PWR Headroom PUSCH Lev 1',
'ue_pwr_headroom__pusch__lev_2':'UE PWR Headroom PUSCH Lev 2',
'ue_pwr_headroom__pusch__lev_3':'UE PWR Headroom PUSCH Lev 3',
'ue_pwr_headroom__pusch__lev_4':'UE PWR Headroom PUSCH Lev 4',
'ue_pwr_headroom__pusch__lev_5':'UE PWR Headroom PUSCH Lev 5',
'ue_pwr_headroom__pusch__lev_6':'UE PWR Headroom PUSCH Lev 6',
'ue_pwr_headroom__pusch__lev_7':'UE PWR Headroom PUSCH Lev 7',
'ue_pwr_headroom__pusch__lev_8':'UE PWR Headroom PUSCH Lev 8',
'ue_pwr_headroom__pusch__lev_9':'UE PWR Headroom PUSCH Lev 9',
'ue_pwr_headroom__pusch__lev_10':'UE PWR Headroom PUSCH Lev 10',
'ue_pwr_headroom__pusch__lev_11':'UE PWR Headroom PUSCH Lev 11',
'ue_pwr_headroom__pusch__lev_12':'UE PWR Headroom PUSCH Lev 12',
'ue_pwr_headroom__pusch__lev_13':'UE PWR Headroom PUSCH Lev 13',
'ue_pwr_headroom__pusch__lev_14':'UE PWR Headroom PUSCH Lev 14',
'ue_pwr_headroom__pusch__lev_15':'UE PWR Headroom PUSCH Lev 15',
'ue_pwr_headroom__pusch__lev_16':'UE PWR Headroom PUSCH Lev 16',
'ue_pwr_headroom__pusch__lev_17':'UE PWR Headroom PUSCH Lev 17',
'ue_pwr_headroom__pusch__lev_18':'UE PWR Headroom PUSCH Lev 18',
'ue_pwr_headroom__pusch__lev_19':'UE PWR Headroom PUSCH Lev 19',
'ue_pwr_headroom__pusch__lev_20':'UE PWR Headroom PUSCH Lev 20',
'ue_pwr_headroom__pusch__lev_21':'UE PWR Headroom PUSCH Lev 21',
'ue_pwr_headroom__pusch__lev_22':'UE PWR Headroom PUSCH Lev 22',
'ue_pwr_headroom__pusch__lev_23':'UE PWR Headroom PUSCH Lev 23',
'ue_pwr_headroom__pusch__lev_24':'UE PWR Headroom PUSCH Lev 24',
'ue_pwr_headroom__pusch__lev_25':'UE PWR Headroom PUSCH Lev 25',
'ue_pwr_headroom__pusch__lev_26':'UE PWR Headroom PUSCH Lev 26',
'ue_pwr_headroom__pusch__lev_27':'UE PWR Headroom PUSCH Lev 27',
'ue_pwr_headroom__pusch__lev_28':'UE PWR Headroom PUSCH Lev 28',
'ue_pwr_headroom__pusch__lev_29':'UE PWR Headroom PUSCH Lev 29',
'ue_pwr_headroom__pusch__lev_30':'UE PWR Headroom PUSCH Lev 30',
'ue_pwr_headroom__pusch__lev_31':'UE PWR Headroom PUSCH Lev 31',
'ue_pwr_headroom__pusch__lev_32':'UE PWR Headroom PUSCH Lev 32',
'ue_w_d_t_b_s_i_t_r_o_0_4_i_5_c':'% UEs with distance to base station in the range of 0-468m in 5km cells',
'ue_w_d_t_b_s_i_t_r_o_4_1_i_5_c':'% UEs with distance to base station in the range of 468-1014m in 5km cells',
'ue_w_d_t_b_s_i_t_r_o_1_1_i_5_c':'% UEs with distance to base station in the range of 1014-1482m in 5km cells',
'ue_w_d_t_b_s_i_t_r_o_1_2_i_5_c':'% UEs with distance to base station in the range of 1482-2028m in 5km cells',
'ue_w_d_t_b_s_i_t_r_o_2_2_i_5_c':'% UEs with distance to base station in the range of 2028-2656m in 5km cells',
'ue_w_d_t_b_s_i_t_r_o_2_3_i_5_c':'% UEs with distance to base station in the range of 2656-3400m in 5km cells',
'ue_w_d_t_b_s_i_t_r_o_3_4_i_5_c':'% UEs with distance to base station in the range of 3.4-4.1km in 5km cells',
'ue_w_d_t_b_s_i_t_r_o_4_4_i_5_c':'% UEs with distance to base station in the range of 4.1-4.8km in 5km cells',
'ue_w_d_t_b_s_i_t_r_o_4_5_i_5_c':'% UEs with distance to base station in the range of 4.8-5.6km in 5km cells',
'_ues_with_distance_to_base_station_more_than_5_6km_in_5km_cells':'% UEs with distance to base station more than 5.6km in 5km cells',
'expect_cell_size':'Expect cell size',
'avg_ue_distance':'Avg UE distance',
'e_utran_rrc_paging_discard_ratio':'E-UTRAN RRC Paging Discard Ratio',
'rrc_paging_requests':'RRC Paging requests',
'discarded_rrc_paging_requests':'Discarded RRC Paging requests',
'rrc_paging_messages':'RRC Paging messages',
'avg_conn_ues_area':'Avg conn UEs area',
'active_ue_per_cell_average_m8051c57':'Active UE per Cell average (M8051C57)',
'active_ue_per_cell_max_m8051c58':'Active UE per Cell max (M8051C58)',
'rrc_connected_ues_avg_m8051c55':'RRC Connected UEs Avg (M8051C55)',
'rrc_connected_ues_max_m8051c56':'RRC Connected UEs Max (M8051C56)',
'max_act_ues_per_cell_dl':'Max Act UEs per cell DL',
'max_act_ues_per_cell_ul':'Max Act UEs per cell UL',
'avg_act_ues_dl':'Avg act UEs DL',
'avg_act_ues_ul':'Avg act UEs UL',
'rach_stp_att_r':'RACH stp att r',
'rach_setup_attempts_for_small_size_messages':'RACH setup attempts for small size messages',
'rach_setup_attempts_for_large_size_messages':'RACH setup attempts for large size messages',
'rach_setup_attempts_for_dedicated_preambles':'RACH setup attempts for dedicated preambles',
'perc__dl_good_radio_qual':'Perc DL Good Radio QUAL',
'perc__dl_accpt_radio_qual':'Perc DL Accpt Radio QUAL',
'perc__dl_bad_radio_qual':'Perc DL Bad Radio QUAL',
'ue_rep_cqi_lev_00':'UE Rep CQI Lev 00',
'ue_rep_cqi_lev_01':'UE Rep CQI Lev 01',
'ue_rep_cqi_lev_02':'UE Rep CQI Lev 02',
'ue_rep_cqi_lev_03':'UE Rep CQI Lev 03',
'ue_rep_cqi_lev_04':'UE Rep CQI Lev 04',
'ue_rep_cqi_lev_05':'UE Rep CQI Lev 05',
'ue_rep_cqi_lev_06':'UE Rep CQI Lev 06',
'ue_rep_cqi_lev_07':'UE Rep CQI Lev 07',
'ue_rep_cqi_lev_08':'UE Rep CQI Lev 08',
'ue_rep_cqi_lev_09':'UE Rep CQI Lev 09',
'ue_rep_cqi_lev_10':'UE Rep CQI Lev 10',
'ue_rep_cqi_lev_11':'UE Rep CQI Lev 11',
'ue_rep_cqi_lev_12':'UE Rep CQI Lev 12',
'ue_rep_cqi_lev_13':'UE Rep CQI Lev 13',
'ue_rep_cqi_lev_14':'UE Rep CQI Lev 14',
'ue_rep_cqi_lev_15':'UE Rep CQI Lev 15',
'perc__good_sinr_lev__pucch':'Perc Good SINR Lev PUCCH',
'perc__accpt_sinr_lev__pucch':'Perc Accpt SINR Lev PUCCH',
'perc__bad_sinr_lev__pucch':'Perc Bad SINR Lev PUCCH',
'min_sinr__pucch':'Min SINR PUCCH',
'max_sinr__pucch':'Max SINR PUCCH',
'avg_sinr_per_cell_pucch':'Avg SINR per cell PUCCH',
'perc__ul_pucch_good_rssi_lev':'Perc UL PUCCH Good RSSI Lev',
'perc__ul_pucch_accpt_rssi_lev':'Perc UL PUCCH Accpt RSSI Lev',
'perc__ul_pucch_bad_rssi_lev':'Perc UL PUCCH Bad RSSI Lev',
'min_rssi_lev___pucch':'Min RSSI Lev  PUCCH',
'max_rssi_lev___pucch':'Max RSSI Lev  PUCCH',
'avg_rssi_per_cell_pucch':'Avg RSSI per cell PUCCH',
'perc__ul_pusch_good_rssi_lev':'Perc UL PUSCH Good RSSI Lev',
'perc__ul_pusch_accpt_rssi_lev':'Perc UL PUSCH Accpt RSSI Lev',
'perc__ul_pusch_bad_rssi_lev':'Perc UL PUSCH Bad RSSI Lev',
'min_rssi_lev___pusch':'Min RSSI Lev  PUSCH',
'max_rssi_lev___pusch':'Max RSSI Lev  PUSCH',
'avg_rssi_per_cell_pusch':'Avg RSSI per cell PUSCH',
'perc__good_sinr_lev__pusch':'Perc Good SINR Lev PUSCH',
'perc__accpt_sinr_lev__pusch':'Perc Accpt SINR Lev PUSCH',
'perc__bad_sinr_lev__pusch':'Perc Bad SINR Lev PUSCH',
'min_sinr__pusch':'Min SINR PUSCH',
'max_sinr__pusch':'Max SINR PUSCH',
'avg_sinr_per_cell_pusch':'Avg SINR per cell PUSCH',
'e_utran_ini_e_rab_stp_sr':'E-UTRAN Ini E-RAB stp SR',
'data_rb_stp_sr':'Data RB stp SR',
'e_rab_dr_fail_ho_init_enb':'E-RAB DR, fail HO init eNB',
'e_utran_pdcp_sdu_lr_dl':'E-UTRAN PDCP SDU LR DL',
'rlc_pdu_re_transmission_ul':'RLC PDU Re-transmission UL',
'rlc_pdu_re_transmission_dl':'RLC PDU Re-transmission DL',
'e_rab_dr_rnl_ue_loss_enb_init':'E-RAB DR, RNL UE loss eNB init',
'e_rab_dr_tnl_insuf_rsrc_enb_init':'E-RAB DR, TNL insuf rsrc eNB init',
'e_rab_dr_oth_enb_init':'E-RAB DR, OTH eNB init',
'e_rab_dr_partial_ho':'E-RAB DR, partial HO',
'e_rab_dr_fail_ho_init_enb_1':'E-RAB DR, fail HO init eNB.1',
'rrc_stp_att':'RRC STP ATT',
'e_rab_dr_s1_reset_cause_initiated_by_mme':'E-RAB DR, S1 Reset cause initiated by MME',
'e_rab_dr_tnl_unspec_enb_init_enb':'E-RAB DR, TNL unspec eNB init eNB',
'e_rab_dr_eutran_reas_init_enb':'E-RAB DR, EUTRAN reas init eNB',
'e_rab_dr_s1_reset_outage_init_enb':'E-RAB DR, S1 reset outage init eNB',
'avg_pdcp_cell_thp_ul_2':'Avg PDCP Cell Thp UL',
'avg_pdcp_cell_thp_dl_2':'Avg PDCP Cell Thp DL',
'fails_init_e_rab_acc':'Fails Init E-RAB acc',
'tot_rrc_conn_re_estab_att':'Tot RRC conn re-estab att',
'rrc_re_estab_att_reconf_fail':'RRC Re-estab Att, reconf fail',
'total_rrc_conn_re_estab_sr':'Total RRC Conn Re-estab SR',
'intra_ho_att':'Intra HO Att',
'max_nr_active_ues_per_cell':'Max nr active UEs per cell',
'active_ue_per_cell_average':'Active UE per Cell average',
'active_ue_per_cell_max':'Active UE per Cell max',
'data_rb_stp_sr_1':'Data RB stp SR.1',
'data_rb_stp_fails':'Data RB stp fails',
'max_ue_pwr_headroom_pusch':'Max UE PWR Headroom PUSCH',
'avg_ue_pwr_headroom_pusch':'Avg UE PWR Headroom PUSCH',
'agg1_block_r':'AGG1 block R',
'agg4_block_r':'AGG4 block R',
'agg8_block_r':'AGG8 block R',
'agg2_block_r':'AGG2 block R',
'3_ofdm_util_pdcch':'3 OFDM util PDCCH',
'agg_level_block_r':'AGG level block R',
'number_of_subframes_with_1_ofdm_symbol_allocated_to_pdcch':'Number of subframes with 1 OFDM symbol allocated to PDCCH',
'number_of_subframes_with_2_ofdm_symbols_allocated_to_pdcch':'Number of subframes with 2 OFDM symbols allocated to PDCCH',
'number_of_subframes_with_3_ofdm_symbols_allocated_to_pdcch':'Number of subframes with 3 OFDM symbols allocated to PDCCH',
'agg1_blocked_pdcch':'AGG1 blocked PDCCH',
'agg2_blocked_pdcch':'AGG2 blocked PDCCH',
'agg4_blocked_pdcch':'AGG4 blocked PDCCH',
'agg8_blocked_pdcch':'AGG8 blocked PDCCH',
'agg1_used_pdcch':'AGG1 used PDCCH',
'agg2_used_pdcch':'AGG2 used PDCCH',
'agg4_used_pdcch':'AGG4 used PDCCH',
'agg8_used_pdcch':'AGG8 used PDCCH',
'avg_pdcch_pwr':'Avg PDCCH pwr',
'perc_dl_prb_util':'Perc DL PRB Util',
'perc_ul_prb_util':'Perc UL PRB Util',
'max_util_dl_prb_p_tti':'Max util DL PRB p TTI',
'dl_prb_util_p_tti_lev_10':'DL PRB Util p TTI Lev_10',
'dl_prb_util_p_tti_lev_1':'DL PRB Util p TTI Lev_1',
'dl_prb_util_p_tti_lev_2':'DL PRB Util p TTI Lev_2',
'dl_prb_util_p_tti_lev_3':'DL PRB Util p TTI Lev_3',
'dl_prb_util_p_tti_lev_4':'DL PRB Util p TTI Lev_4',
'dl_prb_util_p_tti_lev_5':'DL PRB Util p TTI Lev_5',
'dl_prb_util_p_tti_lev_6':'DL PRB Util p TTI Lev_6',
'dl_prb_util_p_tti_lev_7':'DL PRB Util p TTI Lev_7',
'dl_prb_util_p_tti_lev_8':'DL PRB Util p TTI Lev_8',
'dl_prb_util_p_tti_lev_9':'DL PRB Util p TTI Lev_9',
'number_of_available_ttis_for_pusch':'Number of available TTIs for PUSCH',
'number_of_available_ttis_for_pdsch':'Number of available TTIs for PDSCH',
'ttis_used_in_dl_by_cell_resource_group_4':'TTIs used in DL by cell resource group 4',
'ttis_used_in_ul_by_cell_resource_group_1':'TTIs used in UL by cell resource group 1',
'ttis_used_in_ul_by_cell_resource_group_2':'TTIs used in UL by cell resource group 2',
'ttis_used_in_ul_by_cell_resource_group_3':'TTIs used in UL by cell resource group 3',
'ttis_used_in_ul_by_cell_resource_group_4':'TTIs used in UL by cell resource group 4',
'ttis_used_in_dl_by_cell_resource_group_1':'TTIs used in DL by cell resource group 1',
'ttis_used_in_dl_by_cell_resource_group_2':'TTIs used in DL by cell resource group 2',
'ttis_used_in_dl_by_cell_resource_group_3':'TTIs used in DL by cell resource group 3',
'sig_conn_rej_r_emgrb_rsrc':'Sig conn rej R emg,RB rsrc',
'sig_con_fr_due_user_plane_ovl':'Sig con FR due User Plane OVL',
'sig_con_fr_due_ctrl_plane_ovl':'Sig con FR due Ctrl Plane OVL',
'sig_con_fr_due_pucch':'Sig con FR due PUCCH',
'sig_con_fr_due_maxrrc':'Sig con FR due MAXRRC',
'sig_con_fr_due_mme_ovl':'Sig con FR due MME OVL',
'perc__ue_lack__ul_pwr_pusch':'Perc UE Lack UL PWR (PUSCH)',
'ul_prb_util_p_tti_lev_10':'UL PRB Util p TTI Lev_10',
'ul_prb_util_p_tti_lev_1':'UL PRB Util p TTI Lev_1',
'ul_prb_util_p_tti_lev_2':'UL PRB Util p TTI Lev_2',
'ul_prb_util_p_tti_lev_3':'UL PRB Util p TTI Lev_3',
'ul_prb_util_p_tti_lev_4':'UL PRB Util p TTI Lev_4',
'ul_prb_util_p_tti_lev_5':'UL PRB Util p TTI Lev_5',
'ul_prb_util_p_tti_lev_6':'UL PRB Util p TTI Lev_6',
'ul_prb_util_p_tti_lev_7':'UL PRB Util p TTI Lev_7',
'ul_prb_util_p_tti_lev_8':'UL PRB Util p TTI Lev_8',
'ul_prb_util_p_tti_lev_9':'UL PRB Util p TTI Lev_9',
'rrc_connected_ues_max':'RRC Connected UEs Max',
'rrc_connected_ues_avg':'RRC Connected UEs Avg',
'avg_act_ues_sched_data_ul':'Avg act UEs sched data UL',
'avg_act_ues_sched_data_dl':'Avg act UEs sched data DL',
'avg_act_ues_data_buff_ul_plmn':'Avg act UEs data buff UL PLMN',
'avg_act_ues_data_buff_dl_plmn':'Avg act UEs data buff DL PLMN',
'disc_rrc_paging_reqs':'DISC RRC Paging REQs',
'rrc_paging_reqs':'RRC Paging REQs',
'max_pdcp_thr_dl':'Max PDCP Thr DL',
'max_pdcp_thr_ul':'Max PDCP Thr UL',
'pdcp_sdu_vol_dl_cat_m':'PDCP SDU vol DL Cat-M',
'prb_pdsch_usgr':'PRB PDSCH UsgR',
'prb_pusch_usgr':'PRB PUSCH UsgR',
'ue_transact_ecm_idle_sr':'UE Transact ECM-IDLE SR',
'dl_user_thp':'DL_USER_THP',
'ul_user_thp':'UL_USER_THP',
'perc_ul_prb_util_1':'Perc UL PRB Util.1',
'perc_dl_prb_util_1':'Perc DL PRB Util.1'}
df_kpi = pd.DataFrame(variable_names.items(), columns=['A', 'B'])


#dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"



# Definir el diseño de la aplicación
layout = html.Div([

    html.Div([
        html.Label('Seleccione Minera:', className='form-label small'),
        dbc.RadioItems(
            id='Minera-radio1',
            label_checked_style={"color": "#b5111a"},
            input_checked_style={
                "backgroundColor": "#b5111a",
                "borderColor": "#b5111a",
            },
            inline=True,
            options=[
                {'label': 'Escondida', 'value': 'Escondida'},
                {'label': 'Spence', 'value': 'Spence'}


        ],
        value='Escondida',
    ),

        #html.Label('Polígonos:', className='form-label small'),

        html.Label('Seleccione KPI:', className='form-label small'),
        dcc.Dropdown(
            id='KPI-dropdown1',
            options=['Total E-UTRAN RRC conn stp SR','RRC Rel','RACH Stp Completion SR','E-UTRAN E-RAB stp SR','E-UTRAN E-RAB Setup Attempts','Cell Avail','RACH stp att','Number of Signaling Connection Establishment Requests rejected due to MME overload','Number of Signaling Connection Establishment Requests rejected due to threshold for the maximum number of RRC connections','Number of Signaling Connection Establishment Requests rejected due to lack of PUCCH resources','Number of Signaling Connection Establishment Requests rejected due to User Plane overload','Number of Signaling Connection Establishment Requests rejected due to Control Plane overload','Signaling Connection Establishment failures due to RRC Setup completions error','Signaling Connection Establishment failures due to RRC Setup completions missing','Signaling Connection Establishment failures for emergency calls due to missing RB resources','E-RAB DR, RNL unspec ini eNB','eNB initiated E-RAB releases due to loss of connection to the UE','eNB initiated E-RAB releases due to insufficient transport resources','eNB initiated E-RAB releases due to missing radio resources','eNB initiated E-RAB releases due to E-UTRAN Generated Reason','E-RABs released due to failed Handover regardless of the bearers QCI','E-RABs released due to partial Handover regardless of the bearers QCI','EPC initiated EPS Bearer Release requests due to Other causes','M8006C309','M8006C310','M8006C313','M8006C312','M8006C311','Avg Act connected UEs','Avg RRC conn UE','PDCP SDU Volume, DL','PDCP SDU Volume, UL','Avg PDCP cell thp DL','Avg PDCP cell thp UL','E-UTRAN Avg PRB usage per TTI DL','Avg PRB usage per TTI UL','DL Spectral efficiency','UL Spectral efficiency','E-RAB Stp Att, QCI9','Avg IP thp DL QCI9','Avg IP thp UL QCI9','Avg PDCP SDU Delay DL QCI9','Intra eNB HO prep SR','Failed Intra eNB Handover preparations due to other reasons','Failed Intra eNB Handover preparations due to Admission Control','Intra eNB HO SR','Total intra eNB HO failures due to timer','inter eNB E-UTRAN HO prep SR X2','Failed Inter-eNB X2 Handover preparations due to not supported QCI','Failed Inter eNB Handover preparations due to other reason','Failed Inter eNB Handover preparations due to timer','Failed Inter eNB Handover preparations due to target eNB admission control','inter eNB E-UTRAN HO SR X2','Number of Inter eNB Handover failures','E-UTRAN HO Prep SR, inter eNB S1','Failed Inter-eNB S1 Handover preparations due to not supported QCI','Failed Inter eNB S1-Handover preparations due to other reason','Failed Inter eNB S1-Handover preparations due to target eNB admission control','Failed Inter eNB S1-Handover preparations due to timer','E-UTRAN HO SR, inter eNB S1','Inter eNB S1-HO failures due to timer','E-UTRAN Intra-Freq HO SR','Attempted intra eNB HO','Attempted inter eNB HO','Attempted inter eNB S1-HO','% Ping Pong HO','Avg Latency DL','Avg Latency Uplink','PDCP SDU delay on DL DTCH Mean','PDCP SDU delay on UL DTCH Mean','Avg SINR for PUCCH','Avg SINR for PUSCH','Avg RSSI for PUCCH','Avg RSSI for PUSCH','BLER DL','BLER UL','Average CQI','% PUSCH tx using low MCS','% PUSCH tx using high MCS','% PDSCH tx using low MCS','% PDSCH tx using high MCS','MIMO CL Single CW Mode Usage', 'MIMO CL Double CW Mode Usage','% MIMO RI 1', '% MIMO RI 2', '% MIMO RI 3', '% MIMO RI 4','E-UTRAN S1 Stp Att','S1 init ctx stp FR by NO_RESP', 'S1 stp FR indicated by MME','E-RAB SFR RNL', 'E-RAB SFR TRPORT', 'E-RAB SFR RESOUR',  'E-RAB stp FR RNL', 'E-RAB stp FR misc', 'E-RAB stp FR mobil', 'E-RAB SFR OTH', 'E-RAB stp FR miss UE cap lic','Avg Nr simult E-RABs QCI9', 'Max Nr simult E-RABs QCI9','E-RAB Stp SR, QCI9','Released active ERABs QCI9','E-UTRAN E-RAB ret RAN v, RNL fail','E-UTRAN E-RAB DR, RAN View', 'E-RAB DR, fail HO init eNB','Avg UE distance', 'S1 stp SR'],
            multi=False,
            style={'width': '100%', 'fontSize': '12px'},
        ),  
    ], className='mb-2',style={}),





    html.Div([
        html.Label('Rango de fechas: ', className='form-label small'),
        dcc.DatePickerRange(
            id='date-range-KPI',
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
            id='time-radio-KPI',
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
    dbc.Button('Buscar', id='btn-buscar-KPI', n_clicks=0, className='btn btn-danger btn-sm mb-2 mt-1'),

 

    html.Div([
        dcc.Graph(id='graph-content-KPI',
                style={'font-family': 'Calibri'}),
   

    ], style={'display': 'flex', 'flex-wrap': 'wrap','justifyContent': 'center'}),



], style={}, className='bg-light p-4')
# Definir la función de actualización del gráfico




def perform_database_queries(start_date, end_date,Minera_selected,datetime_option,KPI_selected):


    kpi_filter= df_kpi[df_kpi['B'] == KPI_selected]
    columnA = kpi_filter['A'].values[0]
    columnB = kpi_filter['B'].values[0]
    print(columnA)
    print(kpi_filter)

    if ((Minera_selected == 'Escondida') and (datetime_option == 'DAY')):


        if Minera_selected is not None:

            q=db.query_S_2(start_date, end_date,columnA,columnB)
            df= db.getdata_recursive(q,Folder_out+'\\'+ "q",'update', ' ', 'MySQL', 'DSN=BHP')
            df['date_id'] = pd.to_datetime(df['date_id'], format='%Y-%m-%d')

    elif ((Minera_selected == 'Escondida') and (datetime_option == 'HOUR')):


        if Minera_selected is not None:

            q=db.query_S_H_2(start_date, end_date,columnA,columnB)
            df= db.getdata_recursive(q,Folder_out+'\\'+ "q",'update', ' ', 'MySQL', 'DSN=BHP')
            df['date_id'] = pd.to_datetime(df['date_id'], format='%Y-%m-%d')
            df['hour_id'] = pd.to_timedelta(df['hour_id'], unit='h')
            df['date_id'] = df['date_id'] + df['hour_id']

    elif ((Minera_selected == 'Spence') and (datetime_option == 'DAY')):


        if Minera_selected is not None:

            q=db.query_S(start_date, end_date,columnA,columnB)
            df= db.getdata_recursive(q,Folder_out+'\\'+ "q",'update', ' ', 'MySQL', 'DSN=BHP')

    elif ((Minera_selected == 'Spence') and (datetime_option == 'HOUR')):


        if Minera_selected is not None:

            q=db.query_S_H(start_date, end_date,columnA,columnB)
            df= db.getdata_recursive(q,Folder_out+'\\'+ "q",'update', ' ', 'MySQL', 'DSN=BHP')
            df['date_id'] = pd.to_datetime(df['date_id'], format='%Y-%m-%d')
            df['hour_id'] = pd.to_timedelta(df['hour_id'], unit='h')
            df['date_id'] = df['date_id'] + df['hour_id']




    return df


def generate_graph2(df,y_columns):
    #sector_selected = [sector_selected] if not isinstance(sector_selected, list) else sector_selected

 
    def create_figure(df, x_col, y1_cols):

        fig = go.Figure()
        for sitio in df['lnbts_name'].unique():

            df_sitio = df[df['lnbts_name'] == sitio]

            fig.add_trace(go.Scatter(x=df_sitio[x_col], y=df_sitio[y1_cols],name=sitio,line=dict(width=2)))


        fig.update_layout(
            width=6.5 * 96 * 2.5,  # 6.5 pulgadas convertidas a píxeles (aproximadamente 96 píxeles por pulgada)
            height=3 * 96 *2.5,   # 3 pulgadas convertidas a píxeles
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            title=dict(text=y1_cols,x=0.5),
            yaxis=dict(
                title=f'{y1_cols}',
                side='left',
                showgrid=True,
                gridcolor='lightgray',
                gridwidth=1,
                #dtick=2, 
                #range=rang
                ),
            xaxis=dict(
                    showgrid=False,
                ))
        #fig.update_xaxes(rangeslider_visible=True)


        return fig

     
    fig1 = create_figure(df, 'date_id', y_columns)


    layout_style = dict(
        font=dict(family='Calibri', size=13),
        xaxis=dict(title=dict( font=dict(family='Calibri black', size=15, color='black'))),
        yaxis=dict(title=dict(font=dict(family='Calibri black', size=15, color='black'))),
        title=dict(font=dict(family='Calibri black', size=24, color='black')),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1, font=dict(family='Calibri', size=11, color='black')),

    )

    
    fig1.update_layout(**layout_style)



    return fig1


# Definir el callback





# Definir la función de actualización del gráfico
@callback(
    Output('graph-content-KPI', 'figure'),
    [Input('btn-buscar-KPI', 'n_clicks')],
    [State('date-range-KPI', 'start_date'),
     State('date-range-KPI', 'end_date'),
     State('Minera-radio1', 'value'),
     State('time-radio-KPI', 'value'),
     State('KPI-dropdown1', 'value')]
)
def update_graph(n_clicks, start_date, end_date,Minera_selected,datetime_option,KPI_selected):
      # Asegurar que cached_data sea global

    global cached_data
    global cached_data2
    global cached_data3

    dropdown_fecha = pd.date_range(start=start_date, end=end_date, freq='D').strftime('%d-%m-%Y')
    # Verificar qué componente ha desencadenado la actualización
    triggered_component_id = ctx.triggered_id
    #print(triggered_component_id)
    #print(triggered_component_id )
    #print(KPI_selected)
    #print(Minera_selected)
    if  (triggered_component_id == 'btn-buscar-KPI'):

       # print(KPI_selected)
            # Realizar consultas a la base de datos solo si el botón "Buscar" o algún dropdown ha desencadenado la actualización
        df = perform_database_queries(start_date, end_date, Minera_selected,datetime_option,KPI_selected)


        cached_data3 = {'df': df}

        fig1 = generate_graph2(cached_data3['df'],KPI_selected) 

           


    else:

        
        fig1 = go.Figure()


        
        #config = {'sort_action':'native'}
    # Generar opciones para Dropdown
    return fig1

# Iniciar la aplicación si se ejecuta el script











