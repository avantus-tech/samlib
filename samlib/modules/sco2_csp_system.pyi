
# This is a generated file

"""sco2_csp_system - ..."""

# VERSION: 0

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'htf': float,
        'htf_props': Matrix,
        'T_htf_hot_des': float,
        'dT_PHX_hot_approach': float,
        'T_amb_des': float,
        'dT_mc_approach': float,
        'site_elevation': float,
        'W_dot_net_des': float,
        'design_method': float,
        'eta_thermal_des': float,
        'UA_recup_tot_des': float,
        'LTR_design_code': float,
        'LTR_UA_des_in': float,
        'LTR_min_dT_des_in': float,
        'LTR_eff_des_in': float,
        'LT_recup_eff_max': float,
        'LTR_LP_deltaP_des_in': float,
        'LTR_HP_deltaP_des_in': float,
        'HTR_design_code': float,
        'HTR_UA_des_in': float,
        'HTR_min_dT_des_in': float,
        'HTR_eff_des_in': float,
        'HT_recup_eff_max': float,
        'HTR_LP_deltaP_des_in': float,
        'HTR_HP_deltaP_des_in': float,
        'cycle_config': float,
        'is_recomp_ok': float,
        'is_P_high_fixed': float,
        'is_PR_fixed': float,
        'is_IP_fixed': float,
        'des_objective': float,
        'min_phx_deltaT': float,
        'rel_tol': float,
        'eta_isen_mc': float,
        'eta_isen_rc': float,
        'eta_isen_pc': float,
        'eta_isen_t': float,
        'PHX_co2_deltaP_des_in': float,
        'deltaP_counterHX_frac': float,
        'P_high_limit': float,
        'dT_PHX_cold_approach': float,
        'is_design_air_cooler': float,
        'fan_power_frac': float,
        'deltaP_cooler_frac': float,
        'T_htf_cold_des': float,
        'm_dot_htf_des': float,
        'eta_thermal_calc': float,
        'm_dot_co2_full': float,
        'recomp_frac': float,
        'cycle_cost': float,
        'cycle_spec_cost': float,
        'cycle_spec_cost_thermal': float,
        'T_comp_in': float,
        'P_comp_in': float,
        'P_comp_out': float,
        'mc_T_out': float,
        'mc_W_dot': float,
        'mc_m_dot_des': float,
        'mc_rho_in': float,
        'mc_ideal_spec_work': float,
        'mc_phi_des': float,
        'mc_psi_des': float,
        'mc_tip_ratio_des': Array,
        'mc_n_stages': float,
        'mc_N_des': float,
        'mc_D': Array,
        'mc_phi_surge': float,
        'mc_psi_max_at_N_des': float,
        'mc_eta_stages_des': Array,
        'mc_cost': float,
        'rc_T_in_des': float,
        'rc_P_in_des': float,
        'rc_T_out_des': float,
        'rc_P_out_des': float,
        'rc_W_dot': float,
        'rc_m_dot_des': float,
        'rc_phi_des': float,
        'rc_psi_des': float,
        'rc_tip_ratio_des': Array,
        'rc_n_stages': float,
        'rc_N_des': float,
        'rc_D': Array,
        'rc_phi_surge': float,
        'rc_psi_max_at_N_des': float,
        'rc_eta_stages_des': Array,
        'rc_cost': float,
        'pc_T_in_des': float,
        'pc_P_in_des': float,
        'pc_W_dot': float,
        'pc_m_dot_des': float,
        'pc_rho_in_des': float,
        'pc_ideal_spec_work_des': float,
        'pc_phi_des': float,
        'pc_tip_ratio_des': Array,
        'pc_n_stages': float,
        'pc_N_des': float,
        'pc_D': Array,
        'pc_phi_surge': float,
        'pc_eta_stages_des': Array,
        'pc_cost': float,
        'c_tot_cost': float,
        'c_tot_W_dot': float,
        't_W_dot': float,
        't_m_dot_des': float,
        'T_turb_in': float,
        't_P_in_des': float,
        't_T_out_des': float,
        't_P_out_des': float,
        't_nu_des': float,
        't_tip_ratio_des': float,
        't_N_des': float,
        't_D': float,
        't_cost': float,
        'recup_total_UA_assigned': float,
        'recup_total_UA_calculated': float,
        'recup_total_cost': float,
        'recup_LTR_UA_frac': float,
        'LTR_HP_T_out_des': float,
        'LTR_UA_assigned': float,
        'LTR_UA_calculated': float,
        'eff_LTR': float,
        'NTU_LTR': float,
        'q_dot_LTR': float,
        'LTR_LP_deltaP_des': float,
        'LTR_HP_deltaP_des': float,
        'LTR_min_dT': float,
        'LTR_cost': float,
        'HTR_LP_T_out_des': float,
        'HTR_HP_T_in_des': float,
        'HTR_UA_assigned': float,
        'HTR_UA_calculated': float,
        'eff_HTR': float,
        'NTU_HTR': float,
        'q_dot_HTR': float,
        'HTR_LP_deltaP_des': float,
        'HTR_HP_deltaP_des': float,
        'HTR_min_dT': float,
        'HTR_cost': float,
        'UA_PHX': float,
        'eff_PHX': float,
        'NTU_PHX': float,
        'T_co2_PHX_in': float,
        'P_co2_PHX_in': float,
        'deltaT_HTF_PHX': float,
        'q_dot_PHX': float,
        'PHX_co2_deltaP_des': float,
        'PHX_cost': float,
        'LP_cooler_T_in': float,
        'LP_cooler_P_in': float,
        'LP_cooler_rho_in': float,
        'LP_cooler_in_isen_deltah_to_P_mc_out': float,
        'LP_cooler_m_dot_co2': float,
        'LP_cooler_UA': float,
        'LP_cooler_q_dot': float,
        'LP_cooler_co2_deltaP_des': float,
        'LP_cooler_W_dot_fan': float,
        'LP_cooler_cost': float,
        'IP_cooler_T_in': float,
        'IP_cooler_P_in': float,
        'IP_cooler_m_dot_co2': float,
        'IP_cooler_UA': float,
        'IP_cooler_q_dot': float,
        'IP_cooler_W_dot_fan': float,
        'IP_cooler_cost': float,
        'cooler_tot_cost': float,
        'cooler_tot_UA': float,
        'cooler_tot_W_dot_fan': float,
        'T_state_points': Array,
        'P_state_points': Array,
        's_state_points': Array,
        'h_state_points': Array,
        'T_LTR_HP_data': Array,
        's_LTR_HP_data': Array,
        'T_HTR_HP_data': Array,
        's_HTR_HP_data': Array,
        'T_PHX_data': Array,
        's_PHX_data': Array,
        'T_HTR_LP_data': Array,
        's_HTR_LP_data': Array,
        'T_LTR_LP_data': Array,
        's_LTR_LP_data': Array,
        'T_main_cooler_data': Array,
        's_main_cooler_data': Array,
        'T_pre_cooler_data': Array,
        's_pre_cooler_data': Array,
        'P_t_data': Array,
        'h_t_data': Array,
        'P_mc_data': Array,
        'h_mc_data': Array,
        'P_rc_data': Array,
        'h_rc_data': Array,
        'P_pc_data': Array,
        'h_pc_data': Array,
        'od_T_t_in_mode': float,
        'od_cases': Matrix,
        'od_P_mc_in_sweep': Array,
        'od_set_control': Matrix,
        'od_generate_udpc': Array,
        'is_gen_od_polynomials': float,
        'm_dot_htf_fracs': Array,
        'T_amb_od': Array,
        'T_htf_hot_od': Array,
        'od_opt_obj_code': Array,
        'od_opt_conv_tol': Array,
        'P_comp_in_od': Array,
        'mc_phi_od': Matrix,
        'recomp_frac_od': Array,
        'sim_time_od': Array,
        'eta_thermal_od': Array,
        'T_mc_in_od': Array,
        'P_mc_out_od': Array,
        'T_htf_cold_od': Array,
        'm_dot_co2_full_od': Array,
        'W_dot_net_od': Array,
        'Q_dot_od': Array,
        'mc_T_out_od': Array,
        'mc_W_dot_od': Array,
        'mc_m_dot_od': Array,
        'mc_rho_in_od': Array,
        'mc_psi_od': Matrix,
        'mc_ideal_spec_work_od': Array,
        'mc_N_od': Array,
        'mc_eta_od': Array,
        'mc_tip_ratio_od': Matrix,
        'mc_eta_stages_od': Matrix,
        'mc_f_bypass_od': Array,
        'rc_T_in_od': Array,
        'rc_P_in_od': Array,
        'rc_T_out_od': Array,
        'rc_P_out_od': Array,
        'rc_W_dot_od': Array,
        'rc_m_dot_od': Array,
        'rc_eta_od': Array,
        'rc_phi_od': Matrix,
        'rc_psi_od': Matrix,
        'rc_N_od': Array,
        'rc_tip_ratio_od': Matrix,
        'rc_eta_stages_od': Matrix,
        'pc_T_in_od': Array,
        'pc_P_in_od': Array,
        'pc_W_dot_od': Array,
        'pc_m_dot_od': Array,
        'pc_rho_in_od': Array,
        'pc_ideal_spec_work_od': Array,
        'pc_eta_od': Array,
        'pc_phi_od': Matrix,
        'pc_N_od': Array,
        'pc_tip_ratio_od': Matrix,
        'pc_eta_stages_od': Matrix,
        'pc_f_bypass_od': Array,
        'c_tot_W_dot_od': Array,
        't_P_in_od': Array,
        't_T_out_od': Array,
        't_P_out_od': Array,
        't_W_dot_od': Array,
        't_m_dot_od': Array,
        't_nu_od': Array,
        't_N_od': Array,
        't_tip_ratio_od': Array,
        't_eta_od': Array,
        'LTR_HP_T_out_od': Array,
        'eff_LTR_od': Array,
        'q_dot_LTR_od': Array,
        'LTR_LP_deltaP_od': Array,
        'LTR_HP_deltaP_od': Array,
        'LTR_min_dT_od': Array,
        'HTR_LP_T_out_od': Array,
        'HTR_HP_T_in_od': Array,
        'eff_HTR_od': Array,
        'q_dot_HTR_od': Array,
        'HTR_LP_deltaP_od': Array,
        'HTR_HP_deltaP_od': Array,
        'HTR_min_dT_od': Array,
        'T_co2_PHX_in_od': Array,
        'P_co2_PHX_in_od': Array,
        'T_co2_PHX_out_od': Array,
        'deltaT_HTF_PHX_od': Array,
        'phx_eff_od': Array,
        'phx_co2_deltaP_od': Array,
        'LP_cooler_T_in_od': Array,
        'LP_cooler_rho_in_od': Array,
        'LP_cooler_in_isen_deltah_to_P_mc_out_od': Array,
        'LP_cooler_co2_deltaP_od': Array,
        'LP_cooler_W_dot_fan_od': Array,
        'IP_cooler_W_dot_fan_od': Array,
        'cooler_tot_W_dot_fan_od': Array,
        'diff_m_dot_od': Array,
        'diff_E_cycle': Array,
        'diff_Q_LTR': Array,
        'diff_Q_HTR': Array,
        'udpc_table': Matrix,
        'udpc_n_T_htf': float,
        'udpc_n_T_amb': float,
        'udpc_n_m_dot_htf': float,
        'od_code': Array
}, total=False)

class Data(ssc.DataDict):
    htf: float = INPUT(label='Integer code for HTF used in PHX', type='NUMBER', group='System Design', required='*')
    htf_props: Matrix = INPUT(label='User defined HTF property data', type='MATRIX', group='System Design', required='?=[[0]]', meta='7 columns (T,Cp,dens,visc,kvisc,cond,h), at least 3 rows')
    T_htf_hot_des: float = INPUT(label='HTF design hot temperature (PHX inlet)', units='C', type='NUMBER', group='System Design', required='*')
    dT_PHX_hot_approach: float = INPUT(label='Temp diff btw hot HTF and turbine inlet', units='C', type='NUMBER', group='System Design', required='*')
    T_amb_des: float = INPUT(label='Ambient temperature', units='C', type='NUMBER', group='System Design', required='*')
    dT_mc_approach: float = INPUT(label='Temp diff btw ambient air and main compressor inlet', units='C', type='NUMBER', group='System Design', required='*')
    site_elevation: float = INPUT(label='Site elevation', units='m', type='NUMBER', group='System Design', required='*')
    W_dot_net_des: float = INPUT(label='Design cycle power output (no cooling parasitics)', units='MWe', type='NUMBER', group='System Design', required='*')
    design_method: float = INPUT(label='1 = Specify efficiency, 2 = Specify total recup UA, 3 = Specify each recup design', type='NUMBER', group='System Design', required='*')
    eta_thermal_des: float = INPUT(label='Power cycle thermal efficiency', type='NUMBER', group='System Design', required='design_method=1')
    UA_recup_tot_des: float = INPUT(label='Total recuperator conductance', units='kW/K', type='NUMBER', group='Heat Exchanger Design', required='design_method=2', meta='Combined recuperator design')
    LTR_design_code: float = INPUT(label='1 = UA, 2 = min dT, 3 = effectiveness', units='-', type='NUMBER', group='Heat Exchanger Design', required='design_method=3', meta='Low temperature recuperator')
    LTR_UA_des_in: float = INPUT(label='Design LTR conductance', units='kW/K', type='NUMBER', group='Heat Exchanger Design', required='design_method=3', meta='Low temperature recuperator')
    LTR_min_dT_des_in: float = INPUT(label='Design minimum allowable temperature difference in LTR', units='C', type='NUMBER', group='Heat Exchanger Design', required='design_method=3', meta='Low temperature recuperator')
    LTR_eff_des_in: float = INPUT(label='Design effectiveness for LTR', units='-', type='NUMBER', group='Heat Exchanger Design', required='design_method=3', meta='Low temperature recuperator')
    LT_recup_eff_max: float = INPUT(label='Maximum allowable effectiveness in LTR', units='-', type='NUMBER', group='Heat Exchanger Design', required='?=1.0', meta='Low temperature recuperator')
    LTR_LP_deltaP_des_in: float = INPUT(label='LTR low pressure side pressure drop as fraction of inlet pressure', units='-', type='NUMBER', group='Heat Exchanger Design', meta='Low temperature recuperator')
    LTR_HP_deltaP_des_in: float = INPUT(label='LTR high pressure side pressure drop as fraction of inlet pressure', units='-', type='NUMBER', group='Heat Exchanger Design', meta='Low temperature recuperator')
    HTR_design_code: float = INPUT(label='1 = UA, 2 = min dT, 3 = effectiveness', units='-', type='NUMBER', group='Heat Exchanger Design', required='design_method=3', meta='High temperature recuperator')
    HTR_UA_des_in: float = INPUT(label='Design HTR conductance', units='kW/K', type='NUMBER', group='Heat Exchanger Design', required='design_method=3', meta='High temperature recuperator')
    HTR_min_dT_des_in: float = INPUT(label='Design minimum allowable temperature difference in HTR', units='C', type='NUMBER', group='Heat Exchanger Design', required='design_method=3', meta='High temperature recuperator')
    HTR_eff_des_in: float = INPUT(label='Design effectiveness for HTR', units='-', type='NUMBER', group='Heat Exchanger Design', required='design_method=3', meta='High temperature recuperator')
    HT_recup_eff_max: float = INPUT(label='Maximum allowable effectiveness in HTR', units='-', type='NUMBER', group='Heat Exchanger Design', required='?=1.0', meta='High temperature recuperator')
    HTR_LP_deltaP_des_in: float = INPUT(label='HTR low pressure side pressure drop as fraction of inlet pressure', units='-', type='NUMBER', group='Heat Exchanger Design', meta='High temperature recuperator')
    HTR_HP_deltaP_des_in: float = INPUT(label='HTR high pressure side pressure drop as fraction of inlet pressure', units='-', type='NUMBER', group='Heat Exchanger Design', meta='High temperature recuperator')
    cycle_config: float = INPUT(label='1 = recompression, 2 = partial cooling', type='NUMBER', group='Heat Exchanger Design', required='?=1', meta='High temperature recuperator')
    is_recomp_ok: float = INPUT(label='1 = Yes, 0 = simple cycle only, < 0 = fix f_recomp to abs(input)', type='NUMBER', group='Heat Exchanger Design', required='?=1', meta='High temperature recuperator')
    is_P_high_fixed: float = INPUT(label='1 = Yes (=P_high_limit), 0 = No, optimized (default)', type='NUMBER', group='Heat Exchanger Design', required='?=0', meta='High temperature recuperator')
    is_PR_fixed: float = INPUT(label='0 = No, >0 = fixed pressure ratio at input <0 = fixed LP at abs(input)', units='High temperature recuperator', type='NUMBER', group='Heat Exchanger Design', required='?=0')
    is_IP_fixed: float = INPUT(label='partial cooling config: 0 = No, >0 = fixed HP-IP pressure ratio at input, <0 = fixed IP at abs(input)', type='NUMBER', group='Heat Exchanger Design', required='?=0', meta='High temperature recuperator')
    des_objective: float = INPUT(label='[2] = hit min phx deltat then max eta, [else] max eta', type='NUMBER', group='Heat Exchanger Design', required='?=0', meta='High temperature recuperator')
    min_phx_deltaT: float = INPUT(label='Minimum design temperature difference across PHX', units='C', type='NUMBER', group='Heat Exchanger Design', required='?=0', meta='High temperature recuperator')
    rel_tol: float = INPUT(label='Baseline solver and optimization relative tolerance exponent (10^-rel_tol)', units='-', type='NUMBER', group='Heat Exchanger Design', required='?=3', meta='High temperature recuperator')
    eta_isen_mc: float = INPUT(label='Design main compressor isentropic efficiency', units='-', type='NUMBER', group='Cycle Design', required='*')
    eta_isen_rc: float = INPUT(label='Design re-compressor isentropic efficiency', units='-', type='NUMBER', group='Cycle Design', required='*')
    eta_isen_pc: float = INPUT(label='Design precompressor isentropic efficiency', units='-', type='NUMBER', group='Cycle Design', required='cycle_config=2')
    eta_isen_t: float = INPUT(label='Design turbine isentropic efficiency', units='-', type='NUMBER', group='Cycle Design', required='*')
    PHX_co2_deltaP_des_in: float = INPUT(label='PHX co2 side pressure drop as fraction of inlet pressure', units='-', type='NUMBER', group='Cycle Design')
    deltaP_counterHX_frac: float = INPUT(label='Fraction of CO2 inlet pressure that is design point counterflow HX (recups & PHX) pressure drop', units='-', type='NUMBER', group='Cycle Design', required='?=0')
    P_high_limit: float = INPUT(label='High pressure limit in cycle', units='MPa', type='NUMBER', group='Cycle Design', required='*')
    dT_PHX_cold_approach: float = INPUT(label='Temp diff btw cold HTF and cold CO2', units='C', type='NUMBER', group='PHX Design', required='*')
    is_design_air_cooler: float = INPUT(label='Defaults to True. False will skip air cooler calcs', type='NUMBER', group='Air Cooler Design', required='?=1.0')
    fan_power_frac: float = INPUT(label='Fraction of net cycle power consumed by air cooler fan', type='NUMBER', group='Air Cooler Design', required='*')
    deltaP_cooler_frac: float = INPUT(label='Fraction of CO2 inlet pressure that is design point cooler CO2 pressure drop', type='NUMBER', group='Air Cooler Design', required='*')
    T_htf_cold_des: Final[float] = OUTPUT(label='HTF design cold temperature (PHX outlet)', units='C', type='NUMBER', required='*', meta='System Design Solution')
    m_dot_htf_des: Final[float] = OUTPUT(label='HTF mass flow rate', units='kg/s', type='NUMBER', required='*', meta='System Design Solution')
    eta_thermal_calc: Final[float] = OUTPUT(label='Calculated cycle thermal efficiency', units='-', type='NUMBER', required='*', meta='System Design Solution')
    m_dot_co2_full: Final[float] = OUTPUT(label='CO2 mass flow rate through HTR, PHX, turbine', units='kg/s', type='NUMBER', required='*', meta='System Design Solution')
    recomp_frac: Final[float] = OUTPUT(label='Recompression fraction', units='-', type='NUMBER', required='*', meta='System Design Solution')
    cycle_cost: Final[float] = OUTPUT(label='Cycle cost', units='M$', type='NUMBER', required='*', meta='System Design Solution')
    cycle_spec_cost: Final[float] = OUTPUT(label='Cycle specific cost', units='$/kWe', type='NUMBER', required='*', meta='System Design Solution')
    cycle_spec_cost_thermal: Final[float] = OUTPUT(label='Cycle specific cost - thermal', units='$/kWt', type='NUMBER', required='*', meta='System Design Solution')
    T_comp_in: Final[float] = OUTPUT(label='Compressor inlet temperature', units='C', type='NUMBER', required='*', meta='Compressor')
    P_comp_in: Final[float] = OUTPUT(label='Compressor inlet pressure', units='MPa', type='NUMBER', required='*', meta='Compressor')
    P_comp_out: Final[float] = OUTPUT(label='Compressor outlet pressure', units='MPa', type='NUMBER', required='*', meta='Compressor')
    mc_T_out: Final[float] = OUTPUT(label='Compressor outlet temperature', units='C', type='NUMBER', required='*', meta='Compressor')
    mc_W_dot: Final[float] = OUTPUT(label='Compressor power', units='MWe', type='NUMBER', required='*', meta='Compressor')
    mc_m_dot_des: Final[float] = OUTPUT(label='Compressor mass flow rate', units='kg/s', type='NUMBER', required='*', meta='Compressor')
    mc_rho_in: Final[float] = OUTPUT(label='Compressor inlet density', units='kg/m3', type='NUMBER', required='*', meta='Compressor')
    mc_ideal_spec_work: Final[float] = OUTPUT(label='Compressor ideal spec work', units='kJ/kg', type='NUMBER', required='*', meta='Compressor')
    mc_phi_des: Final[float] = OUTPUT(label='Compressor design flow coefficient', type='NUMBER', required='*', meta='Compressor')
    mc_psi_des: Final[float] = OUTPUT(label='Compressor design ideal head coefficient', type='NUMBER', required='*', meta='Compressor')
    mc_tip_ratio_des: Final[Array] = OUTPUT(label='Compressor design stage tip speed ratio', type='ARRAY', required='*', meta='Compressor')
    mc_n_stages: Final[float] = OUTPUT(label='Compressor stages', type='NUMBER', required='*', meta='Compressor')
    mc_N_des: Final[float] = OUTPUT(label='Compressor design shaft speed', units='rpm', type='NUMBER', required='*', meta='Compressor')
    mc_D: Final[Array] = OUTPUT(label='Compressor stage diameters', units='m', type='ARRAY', required='*', meta='Compressor')
    mc_phi_surge: Final[float] = OUTPUT(label='Compressor flow coefficient where surge occurs', type='NUMBER', required='*', meta='Compressor')
    mc_psi_max_at_N_des: Final[float] = OUTPUT(label='Compressor max ideal head coefficient at design shaft speed', type='NUMBER', required='*', meta='Compressor')
    mc_eta_stages_des: Final[Array] = OUTPUT(label='Compressor design stage isentropic efficiencies', type='ARRAY', required='*', meta='Compressor')
    mc_cost: Final[float] = OUTPUT(label='Compressor cost', units='M$', type='NUMBER', required='*', meta='Compressor')
    rc_T_in_des: Final[float] = OUTPUT(label='Recompressor inlet temperature', units='C', type='NUMBER', required='*', meta='Recompressor')
    rc_P_in_des: Final[float] = OUTPUT(label='Recompressor inlet pressure', units='MPa', type='NUMBER', required='*', meta='Recompressor')
    rc_T_out_des: Final[float] = OUTPUT(label='Recompressor inlet temperature', units='C', type='NUMBER', required='*', meta='Recompressor')
    rc_P_out_des: Final[float] = OUTPUT(label='Recompressor inlet pressure', units='MPa', type='NUMBER', required='*', meta='Recompressor')
    rc_W_dot: Final[float] = OUTPUT(label='Recompressor power', units='MWe', type='NUMBER', required='*', meta='Recompressor')
    rc_m_dot_des: Final[float] = OUTPUT(label='Recompressor mass flow rate', units='kg/s', type='NUMBER', required='*', meta='Recompressor')
    rc_phi_des: Final[float] = OUTPUT(label='Recompressor design flow coefficient', type='NUMBER', required='*', meta='Recompressor')
    rc_psi_des: Final[float] = OUTPUT(label='Recompressor design ideal head coefficient', type='NUMBER', required='*', meta='Recompressor')
    rc_tip_ratio_des: Final[Array] = OUTPUT(label='Recompressor design stage tip speed ratio', type='ARRAY', required='*', meta='Recompressor')
    rc_n_stages: Final[float] = OUTPUT(label='Recompressor stages', type='NUMBER', required='*', meta='Recompressor')
    rc_N_des: Final[float] = OUTPUT(label='Recompressor design shaft speed', units='rpm', type='NUMBER', required='*', meta='Recompressor')
    rc_D: Final[Array] = OUTPUT(label='Recompressor stage diameters', units='m', type='ARRAY', required='*', meta='Recompressor')
    rc_phi_surge: Final[float] = OUTPUT(label='Recompressor flow coefficient where surge occurs', type='NUMBER', required='*', meta='Recompressor')
    rc_psi_max_at_N_des: Final[float] = OUTPUT(label='Recompressor max ideal head coefficient at design shaft speed', type='NUMBER', required='*', meta='Recompressor')
    rc_eta_stages_des: Final[Array] = OUTPUT(label='Recompressor design stage isenstropic efficiencies', type='ARRAY', required='*', meta='Recompressor')
    rc_cost: Final[float] = OUTPUT(label='Recompressor cost', units='M$', type='NUMBER', required='*', meta='Recompressor')
    pc_T_in_des: Final[float] = OUTPUT(label='Precompressor inlet temperature', units='C', type='NUMBER', required='*', meta='Precompressor')
    pc_P_in_des: Final[float] = OUTPUT(label='Precompressor inlet pressure', units='MPa', type='NUMBER', required='*', meta='Precompressor')
    pc_W_dot: Final[float] = OUTPUT(label='Precompressor power', units='MWe', type='NUMBER', required='*', meta='Precompressor')
    pc_m_dot_des: Final[float] = OUTPUT(label='Precompressor mass flow rate', units='kg/s', type='NUMBER', required='*', meta='Precompressor')
    pc_rho_in_des: Final[float] = OUTPUT(label='Precompressor inlet density', units='kg/m3', type='NUMBER', required='*', meta='Precompressor')
    pc_ideal_spec_work_des: Final[float] = OUTPUT(label='Precompressor ideal spec work', units='kJ/kg', type='NUMBER', required='*', meta='Precompressor')
    pc_phi_des: Final[float] = OUTPUT(label='Precompressor design flow coefficient', type='NUMBER', required='*', meta='Precompressor')
    pc_tip_ratio_des: Final[Array] = OUTPUT(label='Precompressor design stage tip speed ratio', type='ARRAY', required='*', meta='Precompressor')
    pc_n_stages: Final[float] = OUTPUT(label='Precompressor stages', type='NUMBER', required='*', meta='Precompressor')
    pc_N_des: Final[float] = OUTPUT(label='Precompressor design shaft speed', units='rpm', type='NUMBER', required='*', meta='Precompressor')
    pc_D: Final[Array] = OUTPUT(label='Precompressor stage diameters', units='m', type='ARRAY', required='*', meta='Precompressor')
    pc_phi_surge: Final[float] = OUTPUT(label='Precompressor flow coefficient where surge occurs', type='NUMBER', required='*', meta='Precompressor')
    pc_eta_stages_des: Final[Array] = OUTPUT(label='Precompressor design stage isenstropic efficiencies', type='ARRAY', required='*', meta='Precompressor')
    pc_cost: Final[float] = OUTPUT(label='Precompressor cost', units='M$', type='NUMBER', required='*', meta='Precompressor')
    c_tot_cost: Final[float] = OUTPUT(label='Compressor total cost', units='M$', type='NUMBER', required='*', meta='Compressor Totals')
    c_tot_W_dot: Final[float] = OUTPUT(label='Compressor total summed power', units='MWe', type='NUMBER', required='*', meta='Compressor Totals')
    t_W_dot: Final[float] = OUTPUT(label='Turbine power', units='MWe', type='NUMBER', required='*', meta='Turbine')
    t_m_dot_des: Final[float] = OUTPUT(label='Turbine mass flow rate', units='kg/s', type='NUMBER', required='*', meta='Turbine')
    T_turb_in: Final[float] = OUTPUT(label='Turbine inlet temperature', units='C', type='NUMBER', required='*', meta='Turbine')
    t_P_in_des: Final[float] = OUTPUT(label='Turbine design inlet pressure', units='MPa', type='NUMBER', required='*', meta='Turbine')
    t_T_out_des: Final[float] = OUTPUT(label='Turbine outlet temperature', units='C', type='NUMBER', required='*', meta='Turbine')
    t_P_out_des: Final[float] = OUTPUT(label='Turbine design outlet pressure', units='MPa', type='NUMBER', required='*', meta='Turbine')
    t_nu_des: Final[float] = OUTPUT(label='Turbine design velocity ratio', type='NUMBER', required='*', meta='Turbine')
    t_tip_ratio_des: Final[float] = OUTPUT(label='Turbine design tip speed ratio', type='NUMBER', required='*', meta='Turbine')
    t_N_des: Final[float] = OUTPUT(label='Turbine design shaft speed', units='rpm', type='NUMBER', required='*', meta='Turbine')
    t_D: Final[float] = OUTPUT(label='Turbine diameter', units='m', type='NUMBER', required='*', meta='Turbine')
    t_cost: Final[float] = OUTPUT(label='Tubine cost', units='M$', type='NUMBER', required='*', meta='Turbine')
    recup_total_UA_assigned: Final[float] = OUTPUT(label='Total recuperator UA assigned to design routine', units='MW/K', type='NUMBER', required='*', meta='Recuperators')
    recup_total_UA_calculated: Final[float] = OUTPUT(label='Total recuperator UA calculated considering max eff and/or min temp diff parameter', units='MW/K', type='NUMBER', required='*', meta='Recuperators')
    recup_total_cost: Final[float] = OUTPUT(label='Total recuperator cost', units='M$', type='NUMBER', required='*', meta='Recuperators')
    recup_LTR_UA_frac: Final[float] = OUTPUT(label='Fraction of total conductance to LTR', type='NUMBER', required='*', meta='Recuperators')
    LTR_HP_T_out_des: Final[float] = OUTPUT(label='Low temp recuperator HP outlet temperature', units='C', type='NUMBER', required='*', meta='Recuperators')
    LTR_UA_assigned: Final[float] = OUTPUT(label='Low temp recuperator UA assigned from total', units='MW/K', type='NUMBER', required='*', meta='Recuperators')
    LTR_UA_calculated: Final[float] = OUTPUT(label='Low temp recuperator UA calculated considering max eff and/or min temp diff parameter', units='MW/K', type='NUMBER', required='*', meta='Recuperators')
    eff_LTR: Final[float] = OUTPUT(label='Low temp recuperator effectiveness', type='NUMBER', required='*', meta='Recuperators')
    NTU_LTR: Final[float] = OUTPUT(label='Low temp recuperator NTU', type='NUMBER', required='*', meta='Recuperators')
    q_dot_LTR: Final[float] = OUTPUT(label='Low temp recuperator heat transfer', units='MWt', type='NUMBER', required='*', meta='Recuperators')
    LTR_LP_deltaP_des: Final[float] = OUTPUT(label='Low temp recuperator low pressure design pressure drop', units='-', type='NUMBER', required='*', meta='Recuperators')
    LTR_HP_deltaP_des: Final[float] = OUTPUT(label='Low temp recuperator high pressure design pressure drop', units='-', type='NUMBER', required='*', meta='Recuperators')
    LTR_min_dT: Final[float] = OUTPUT(label='Low temp recuperator min temperature difference', units='C', type='NUMBER', required='*', meta='Recuperators')
    LTR_cost: Final[float] = OUTPUT(label='Low temp recuperator cost', units='M$', type='NUMBER', required='*', meta='Recuperators')
    HTR_LP_T_out_des: Final[float] = OUTPUT(label='High temp recuperator LP outlet temperature', units='C', type='NUMBER', required='*', meta='Recuperators')
    HTR_HP_T_in_des: Final[float] = OUTPUT(label='High temp recuperator HP inlet temperature', units='C', type='NUMBER', required='*', meta='Recuperators')
    HTR_UA_assigned: Final[float] = OUTPUT(label='High temp recuperator UA assigned from total', units='MW/K', type='NUMBER', required='*', meta='Recuperators')
    HTR_UA_calculated: Final[float] = OUTPUT(label='High temp recuperator UA calculated considering max eff and/or min temp diff parameter', units='MW/K', type='NUMBER', required='*', meta='Recuperators')
    eff_HTR: Final[float] = OUTPUT(label='High temp recuperator effectiveness', type='NUMBER', required='*', meta='Recuperators')
    NTU_HTR: Final[float] = OUTPUT(label='High temp recuperator NTRU', type='NUMBER', required='*', meta='Recuperators')
    q_dot_HTR: Final[float] = OUTPUT(label='High temp recuperator heat transfer', units='MWt', type='NUMBER', required='*', meta='Recuperators')
    HTR_LP_deltaP_des: Final[float] = OUTPUT(label='High temp recuperator low pressure design pressure drop', units='-', type='NUMBER', required='*', meta='Recuperators')
    HTR_HP_deltaP_des: Final[float] = OUTPUT(label='High temp recuperator high pressure design pressure drop', units='-', type='NUMBER', required='*', meta='Recuperators')
    HTR_min_dT: Final[float] = OUTPUT(label='High temp recuperator min temperature difference', units='C', type='NUMBER', required='*', meta='Recuperators')
    HTR_cost: Final[float] = OUTPUT(label='High temp recuperator cost', units='M$', type='NUMBER', required='*', meta='Recuperators')
    UA_PHX: Final[float] = OUTPUT(label='PHX Conductance', units='MW/K', type='NUMBER', required='*', meta='PHX Design Solution')
    eff_PHX: Final[float] = OUTPUT(label='PHX effectiveness', type='NUMBER', required='*', meta='PHX Design Solution')
    NTU_PHX: Final[float] = OUTPUT(label='PHX NTU', type='NUMBER', required='*', meta='PHX Design Solution')
    T_co2_PHX_in: Final[float] = OUTPUT(label='CO2 temperature at PHX inlet', units='C', type='NUMBER', required='*', meta='PHX Design Solution')
    P_co2_PHX_in: Final[float] = OUTPUT(label='CO2 pressure at PHX inlet', units='MPa', type='NUMBER', required='*', meta='PHX Design Solution')
    deltaT_HTF_PHX: Final[float] = OUTPUT(label='HTF temp difference across PHX', units='C', type='NUMBER', required='*', meta='PHX Design Solution')
    q_dot_PHX: Final[float] = OUTPUT(label='PHX heat transfer', units='MWt', type='NUMBER', required='*', meta='PHX Design Solution')
    PHX_co2_deltaP_des: Final[float] = OUTPUT(label='PHX co2 side design pressure drop', units='-', type='NUMBER', required='*', meta='PHX Design Solution')
    PHX_cost: Final[float] = OUTPUT(label='PHX cost', units='M$', type='NUMBER', required='*', meta='PHX Design Solution')
    LP_cooler_T_in: Final[float] = OUTPUT(label='Low pressure cross flow cooler inlet temperature', units='C', type='NUMBER', required='*', meta='Low Pressure Cooler')
    LP_cooler_P_in: Final[float] = OUTPUT(label='Low pressure cross flow cooler inlet pressure', units='MPa', type='NUMBER', required='*', meta='Low Pressure Cooler')
    LP_cooler_rho_in: Final[float] = OUTPUT(label='Low pressure cross flow cooler inlet density', units='kg/m3', type='NUMBER', required='*', meta='Low Pressure Cooler')
    LP_cooler_in_isen_deltah_to_P_mc_out: Final[float] = OUTPUT(label='Low pressure cross flow cooler inlet isen enthalpy rise to mc outlet pressure', units='kJ/kg', type='NUMBER', required='*', meta='Low Pressure Cooler')
    LP_cooler_m_dot_co2: Final[float] = OUTPUT(label='Low pressure cross flow cooler CO2 mass flow rate', units='kg/s', type='NUMBER', required='*', meta='Low Pressure Cooler')
    LP_cooler_UA: Final[float] = OUTPUT(label='Low pressure cross flow cooler conductance', units='MW/K', type='NUMBER', required='*', meta='Low Pressure Cooler')
    LP_cooler_q_dot: Final[float] = OUTPUT(label='Low pressure cooler heat transfer', units='MWt', type='NUMBER', required='*', meta='Low Pressure Cooler')
    LP_cooler_co2_deltaP_des: Final[float] = OUTPUT(label='Low pressure cooler co2 side design pressure drop', units='-', type='NUMBER', required='*', meta='Low Pressure Cooler')
    LP_cooler_W_dot_fan: Final[float] = OUTPUT(label='Low pressure cooler fan power', units='MWe', type='NUMBER', required='*', meta='Low Pressure Cooler')
    LP_cooler_cost: Final[float] = OUTPUT(label='Low pressure cooler cost', units='M$', type='NUMBER', required='*', meta='Low Pressure Cooler')
    IP_cooler_T_in: Final[float] = OUTPUT(label='Intermediate pressure cross flow cooler inlet temperature', units='C', type='NUMBER', required='*', meta='Intermediate Pressure Cooler')
    IP_cooler_P_in: Final[float] = OUTPUT(label='Intermediate pressure cross flow cooler inlet pressure', units='MPa', type='NUMBER', required='*', meta='Intermediate Pressure Cooler')
    IP_cooler_m_dot_co2: Final[float] = OUTPUT(label='Intermediate pressure cross flow cooler CO2 mass flow rate', units='kg/s', type='NUMBER', required='*', meta='Intermediate Pressure Cooler')
    IP_cooler_UA: Final[float] = OUTPUT(label='Intermediate pressure cross flow cooler conductance', units='MW/K', type='NUMBER', required='*', meta='Intermediate Pressure Cooler')
    IP_cooler_q_dot: Final[float] = OUTPUT(label='Intermediate pressure cooler heat transfer', units='MWt', type='NUMBER', required='*', meta='Intermediate Pressure Cooler')
    IP_cooler_W_dot_fan: Final[float] = OUTPUT(label='Intermediate pressure cooler fan power', units='MWe', type='NUMBER', required='*', meta='Intermediate Pressure Cooler')
    IP_cooler_cost: Final[float] = OUTPUT(label='Intermediate pressure cooler cost', units='M$', type='NUMBER', required='*', meta='Intermediate Pressure Cooler')
    cooler_tot_cost: Final[float] = OUTPUT(label='Total cooler cost', units='M$', type='NUMBER', required='*', meta='Cooler Totals')
    cooler_tot_UA: Final[float] = OUTPUT(label='Total cooler conductance', units='MW/K', type='NUMBER', required='*', meta='Cooler Totals')
    cooler_tot_W_dot_fan: Final[float] = OUTPUT(label='Total cooler fan power', units='MWe', type='NUMBER', required='*', meta='Cooler Totals')
    T_state_points: Final[Array] = OUTPUT(label='Cycle temperature state points', units='C', type='ARRAY', required='*', meta='State Points')
    P_state_points: Final[Array] = OUTPUT(label='Cycle pressure state points', units='MPa', type='ARRAY', required='*', meta='State Points')
    s_state_points: Final[Array] = OUTPUT(label='Cycle entropy state points', units='kJ/kg-K', type='ARRAY', required='*', meta='State Points')
    h_state_points: Final[Array] = OUTPUT(label='Cycle enthalpy state points', units='kJ/kg', type='ARRAY', required='*', meta='State Points')
    T_LTR_HP_data: Final[Array] = OUTPUT(label='Temperature points along LTR HP stream', units='C', type='ARRAY', required='*', meta='T-s plot data')
    s_LTR_HP_data: Final[Array] = OUTPUT(label='Entropy points along LTR HP stream', units='kJ/kg-K', type='ARRAY', required='*', meta='T-s plot data')
    T_HTR_HP_data: Final[Array] = OUTPUT(label='Temperature points along HTR HP stream', units='C', type='ARRAY', required='*', meta='T-s plot data')
    s_HTR_HP_data: Final[Array] = OUTPUT(label='Entropy points along HTR HP stream', units='kJ/kg-K', type='ARRAY', required='*', meta='T-s plot data')
    T_PHX_data: Final[Array] = OUTPUT(label='Temperature points along PHX stream', units='C', type='ARRAY', required='*', meta='T-s plot data')
    s_PHX_data: Final[Array] = OUTPUT(label='Entropy points along PHX stream', units='kJ/kg-K', type='ARRAY', required='*', meta='T-s plot data')
    T_HTR_LP_data: Final[Array] = OUTPUT(label='Temperature points along HTR LP stream', units='C', type='ARRAY', required='*', meta='T-s plot data')
    s_HTR_LP_data: Final[Array] = OUTPUT(label='Entropy points along HTR LP stream', units='kJ/kg-K', type='ARRAY', required='*', meta='T-s plot data')
    T_LTR_LP_data: Final[Array] = OUTPUT(label='Temperature points along LTR LP stream', units='C', type='ARRAY', required='*', meta='T-s plot data')
    s_LTR_LP_data: Final[Array] = OUTPUT(label='Entropy points along LTR LP stream', units='kJ/kg-K', type='ARRAY', required='*', meta='T-s plot data')
    T_main_cooler_data: Final[Array] = OUTPUT(label='Temperature points along main cooler stream', units='C', type='ARRAY', required='*', meta='T-s plot data')
    s_main_cooler_data: Final[Array] = OUTPUT(label='Entropy points along main cooler stream', units='kJ/kg-K', type='ARRAY', required='*', meta='T-s plot data')
    T_pre_cooler_data: Final[Array] = OUTPUT(label='Temperature points along pre cooler stream', units='C', type='ARRAY', required='*', meta='T-s plot data')
    s_pre_cooler_data: Final[Array] = OUTPUT(label='Entropy points along pre cooler stream', units='kJ/kg-K', type='ARRAY', required='*', meta='T-s plot data')
    P_t_data: Final[Array] = OUTPUT(label='Pressure points along turbine expansion', units='MPa', type='ARRAY', required='*', meta='P-h plot data')
    h_t_data: Final[Array] = OUTPUT(label='Enthalpy points along turbine expansion', units='kJ/kg', type='ARRAY', required='*', meta='P-h plot data')
    P_mc_data: Final[Array] = OUTPUT(label='Pressure points along main compression', units='MPa', type='ARRAY', required='*', meta='P-h plot data')
    h_mc_data: Final[Array] = OUTPUT(label='Enthalpy points along main compression', units='kJ/kg', type='ARRAY', required='*', meta='P-h plot data')
    P_rc_data: Final[Array] = OUTPUT(label='Pressure points along re compression', units='MPa', type='ARRAY', required='*', meta='P-h plot data')
    h_rc_data: Final[Array] = OUTPUT(label='Enthalpy points along re compression', units='kJ/kg', type='ARRAY', required='*', meta='P-h plot data')
    P_pc_data: Final[Array] = OUTPUT(label='Pressure points along pre compression', units='MPa', type='ARRAY', required='*', meta='P-h plot data')
    h_pc_data: Final[Array] = OUTPUT(label='Enthalpy points along pre compression', units='kJ/kg', type='ARRAY', required='*', meta='P-h plot data')
    od_T_t_in_mode: float = INPUT(label='0: model solves co2/HTF PHX od model to calculate turbine inlet temp, 1: model sets turbine inlet temp to HTF hot temp', type='NUMBER', required='?=0')
    od_cases: Matrix = INPUT(label='Columns: T_htf_C, m_dot_htf_ND, T_amb_C, f_N_rc (=1 use design, =0 optimize, <0, frac_des = abs(input), f_N_mc (=1 use design, =0 optimize, <0, frac_des = abs(input), PHX_f_dP (=1 use design, <0 = abs(input), Rows: cases', type='MATRIX')
    od_P_mc_in_sweep: Array = INPUT(label='Columns: T_htf_C, m_dot_htf_ND, T_amb_C, f_N_rc (=1 use design, <0, frac_des = abs(input), f_N_mc (=1 use design, <0, frac_des = abs(input), PHX_f_dP (=1 use design, <0 = abs(input)', type='ARRAY')
    od_set_control: Matrix = INPUT(label='Columns: T_htf_C, m_dot_htf_ND, T_amb_C, P_LP_in_MPa, f_N_rc (=1 use design, <0, frac_des = abs(input), f_N_mc (=1 use design, <0, frac_des = abs(input), PHX_f_dP (=1 use design, <0 = abs(input), Rows: cases', type='MATRIX')
    od_generate_udpc: Array = INPUT(label='True/False, f_N_rc (=1 use design, =0 optimize, <0, frac_des = abs(input), f_N_mc (=1 use design, =0 optimize, <0, frac_des = abs(input), PHX_f_dP (=1 use design, <0 = abs(input)', type='ARRAY')
    is_gen_od_polynomials: float = INPUT(label='Generate off-design polynomials for Generic CSP models? 1 = Yes, 0 = No', type='NUMBER', required='?=0')
    m_dot_htf_fracs: Final[Array] = OUTPUT(label='Normalized mass flow rate', type='ARRAY', meta='Off-Design')
    T_amb_od: Final[Array] = OUTPUT(label='Ambient temperatures', units='C', type='ARRAY', meta='Off-Design')
    T_htf_hot_od: Final[Array] = OUTPUT(label='HTF hot temperatures', units='C', type='ARRAY', meta='Off-Design')
    od_opt_obj_code: Final[Array] = OUTPUT(label='1: MAX_ETA, 2: MAX_POWER', type='ARRAY', meta='Off-Design Cycle Control')
    od_opt_conv_tol: Final[Array] = OUTPUT(label='Off design optimizer convergence tolerance', type='ARRAY', meta='Off-Design Cycle Control')
    P_comp_in_od: Final[Array] = OUTPUT(label='Main compressor inlet pressures', units='MPa', type='ARRAY', meta='Off-Design Cycle Control')
    mc_phi_od: Final[Matrix] = OUTPUT(label='Off-design main compressor flow coefficient [od run][stage]', type='MATRIX', meta='Off-Design Cycle Control')
    recomp_frac_od: Final[Array] = OUTPUT(label='Recompression fractions', type='ARRAY', meta='Off-Design Cycle Control')
    sim_time_od: Final[Array] = OUTPUT(label='Simulation time for off design optimization', units='s', type='ARRAY', meta='Off-Design Optimizer')
    eta_thermal_od: Final[Array] = OUTPUT(label='Off-design cycle thermal efficiency', type='ARRAY', meta='Off-Design System Solution')
    T_mc_in_od: Final[Array] = OUTPUT(label='Off-design compressor inlet temperature', units='C', type='ARRAY', meta='Off-Design System Solution')
    P_mc_out_od: Final[Array] = OUTPUT(label='Off-design high side pressure', units='MPa', type='ARRAY', meta='Off-Design System Solution')
    T_htf_cold_od: Final[Array] = OUTPUT(label='Off-design cold return temperature', units='C', type='ARRAY', meta='Off-Design System Solution')
    m_dot_co2_full_od: Final[Array] = OUTPUT(label='Off-design mass flow rate through turbine', units='kg/s', type='ARRAY', meta='Off-Design System Solution')
    W_dot_net_od: Final[Array] = OUTPUT(label='Off-design cycle net output (no cooling pars)', units='MWe', type='ARRAY', meta='Off-Design System Solution')
    Q_dot_od: Final[Array] = OUTPUT(label='Off-design thermal input', units='MWt', type='ARRAY', meta='Off-Design System Solution')
    mc_T_out_od: Final[Array] = OUTPUT(label='Off-design main compressor outlet temperature', units='C', type='ARRAY')
    mc_W_dot_od: Final[Array] = OUTPUT(label='Off-design main compressor power', units='MWe', type='ARRAY')
    mc_m_dot_od: Final[Array] = OUTPUT(label='Off-design main compressor mass flow', units='kg/s', type='ARRAY')
    mc_rho_in_od: Final[Array] = OUTPUT(label='Off-design main compressor inlet density', units='kg/m3', type='ARRAY')
    mc_psi_od: Final[Matrix] = OUTPUT(label='Off-design main compressor ideal head coefficient [od run][stage]', type='MATRIX')
    mc_ideal_spec_work_od: Final[Array] = OUTPUT(label='Off-design main compressor ideal specific work', units='kJ/kg', type='ARRAY')
    mc_N_od: Final[Array] = OUTPUT(label='Off-design main compressor speed', units='rpm', type='ARRAY')
    mc_eta_od: Final[Array] = OUTPUT(label='Off-design main compressor overall isentropic efficiency', type='ARRAY')
    mc_tip_ratio_od: Final[Matrix] = OUTPUT(label='Off-design main compressor tip speed ratio [od run][stage]', type='MATRIX')
    mc_eta_stages_od: Final[Matrix] = OUTPUT(label='Off-design main compressor stages isentropic efficiency [od run][stage]', type='MATRIX')
    mc_f_bypass_od: Final[Array] = OUTPUT(label='Off-design main compressor bypass to cooler inlet', units='-', type='ARRAY')
    rc_T_in_od: Final[Array] = OUTPUT(label='Off-design recompressor inlet temperature', units='C', type='ARRAY')
    rc_P_in_od: Final[Array] = OUTPUT(label='Off-design recompressor inlet pressure', units='MPa', type='ARRAY')
    rc_T_out_od: Final[Array] = OUTPUT(label='Off-design recompressor outlet temperature', units='C', type='ARRAY')
    rc_P_out_od: Final[Array] = OUTPUT(label='Off-design recompressor outlet pressure', units='MPa', type='ARRAY')
    rc_W_dot_od: Final[Array] = OUTPUT(label='Off-design recompressor power', units='MWe', type='ARRAY')
    rc_m_dot_od: Final[Array] = OUTPUT(label='Off-design recompressor mass flow', units='kg/s', type='ARRAY')
    rc_eta_od: Final[Array] = OUTPUT(label='Off-design recompressor overal isentropic efficiency', type='ARRAY')
    rc_phi_od: Final[Matrix] = OUTPUT(label='Off-design recompressor flow coefficients [od run][stage]', units='-', type='MATRIX')
    rc_psi_od: Final[Matrix] = OUTPUT(label='Off-design recompressor ideal head coefficient [od run][stage]', units='-', type='MATRIX')
    rc_N_od: Final[Array] = OUTPUT(label='Off-design recompressor shaft speed', units='rpm', type='ARRAY')
    rc_tip_ratio_od: Final[Matrix] = OUTPUT(label='Off-design recompressor tip speed ratio [od run][stage]', units='-', type='MATRIX')
    rc_eta_stages_od: Final[Matrix] = OUTPUT(label='Off-design recompressor stages isentropic efficiency [od run][stage]', type='MATRIX')
    pc_T_in_od: Final[Array] = OUTPUT(label='Off-design precompressor inlet temperature', units='C', type='ARRAY')
    pc_P_in_od: Final[Array] = OUTPUT(label='Off-design precompressor inlet pressure', units='MPa', type='ARRAY')
    pc_W_dot_od: Final[Array] = OUTPUT(label='Off-design precompressor power', units='MWe', type='ARRAY')
    pc_m_dot_od: Final[Array] = OUTPUT(label='Off-design precompressor mass flow', units='kg/s', type='ARRAY')
    pc_rho_in_od: Final[Array] = OUTPUT(label='Off-design precompressor inlet density', units='kg/m3', type='ARRAY')
    pc_ideal_spec_work_od: Final[Array] = OUTPUT(label='Off-design precompressor ideal spec work', units='kJ/kg', type='ARRAY')
    pc_eta_od: Final[Array] = OUTPUT(label='Off-design precompressor overal isentropic efficiency', type='ARRAY')
    pc_phi_od: Final[Matrix] = OUTPUT(label='Off-design precompressor flow coefficient [od run][stage]', units='-', type='MATRIX')
    pc_N_od: Final[Array] = OUTPUT(label='Off-design precompressor shaft speed', units='rpm', type='ARRAY')
    pc_tip_ratio_od: Final[Matrix] = OUTPUT(label='Off-design precompressor tip speed ratio [od run][stage]', units='-', type='MATRIX')
    pc_eta_stages_od: Final[Matrix] = OUTPUT(label='Off-design precompressor stages isentropic efficiency [od run][stage]', type='MATRIX')
    pc_f_bypass_od: Final[Array] = OUTPUT(label='Off-design precompressor bypass to cooler inlet', units='-', type='ARRAY')
    c_tot_W_dot_od: Final[Array] = OUTPUT(label='Compressor total off-design power', units='MWe', type='ARRAY')
    t_P_in_od: Final[Array] = OUTPUT(label='Off-design turbine inlet pressure', units='MPa', type='ARRAY')
    t_T_out_od: Final[Array] = OUTPUT(label='Off-design turbine outlet temperature', units='C', type='ARRAY')
    t_P_out_od: Final[Array] = OUTPUT(label='Off-design turbine outlet pressure', units='MPa', type='ARRAY')
    t_W_dot_od: Final[Array] = OUTPUT(label='Off-design turbine power', units='MWe', type='ARRAY')
    t_m_dot_od: Final[Array] = OUTPUT(label='Off-design turbine mass flow rate', units='kg/s', type='ARRAY')
    t_nu_od: Final[Array] = OUTPUT(label='Off-design turbine velocity ratio', units='-', type='ARRAY')
    t_N_od: Final[Array] = OUTPUT(label='Off-design turbine shaft speed', units='rpm', type='ARRAY')
    t_tip_ratio_od: Final[Array] = OUTPUT(label='Off-design turbine tip speed ratio', units='-', type='ARRAY')
    t_eta_od: Final[Array] = OUTPUT(label='Off-design turbine efficiency', units='-', type='ARRAY')
    LTR_HP_T_out_od: Final[Array] = OUTPUT(label='Off-design low temp recup HP outlet temperature', units='C', type='ARRAY')
    eff_LTR_od: Final[Array] = OUTPUT(label='Off-design low temp recup effectiveness', type='ARRAY')
    q_dot_LTR_od: Final[Array] = OUTPUT(label='Off-design low temp recup heat transfer', units='MWt', type='ARRAY')
    LTR_LP_deltaP_od: Final[Array] = OUTPUT(label='Off-design low temp recup low pressure side pressure drop', units='-', type='ARRAY')
    LTR_HP_deltaP_od: Final[Array] = OUTPUT(label='Off-design low temp recup high pressure side pressure drop', units='-', type='ARRAY')
    LTR_min_dT_od: Final[Array] = OUTPUT(label='Off-design low temp recup minimum temperature difference', units='C', type='ARRAY')
    HTR_LP_T_out_od: Final[Array] = OUTPUT(label='Off-design high temp recup LP outlet temperature', units='C', type='ARRAY')
    HTR_HP_T_in_od: Final[Array] = OUTPUT(label='Off-design high temp recup HP inlet temperature', units='C', type='ARRAY')
    eff_HTR_od: Final[Array] = OUTPUT(label='Off-design high temp recup effectiveness', type='ARRAY')
    q_dot_HTR_od: Final[Array] = OUTPUT(label='Off-design high temp recup heat transfer', units='MWt', type='ARRAY')
    HTR_LP_deltaP_od: Final[Array] = OUTPUT(label='Off-design high temp recup low pressure side pressure drop', units='-', type='ARRAY')
    HTR_HP_deltaP_od: Final[Array] = OUTPUT(label='Off-design high temp recup high pressure side pressure drop', units='-', type='ARRAY')
    HTR_min_dT_od: Final[Array] = OUTPUT(label='Off-design high temp recup minimum temperature difference', units='C', type='ARRAY')
    T_co2_PHX_in_od: Final[Array] = OUTPUT(label='Off-design PHX co2 inlet temperature', units='C', type='ARRAY')
    P_co2_PHX_in_od: Final[Array] = OUTPUT(label='Off-design PHX co2 inlet pressure', units='MPa', type='ARRAY')
    T_co2_PHX_out_od: Final[Array] = OUTPUT(label='Off-design PHX co2 outlet temperature', units='C', type='ARRAY')
    deltaT_HTF_PHX_od: Final[Array] = OUTPUT(label='Off-design HTF temp difference across PHX', units='C', type='ARRAY')
    phx_eff_od: Final[Array] = OUTPUT(label='Off-design PHX effectiveness', units='-', type='ARRAY')
    phx_co2_deltaP_od: Final[Array] = OUTPUT(label='Off-design PHX co2 side pressure drop', units='-', type='ARRAY')
    LP_cooler_T_in_od: Final[Array] = OUTPUT(label='Off-design Low pressure cooler inlet temperature', units='C', type='ARRAY')
    LP_cooler_rho_in_od: Final[Array] = OUTPUT(label='Off-design Low pressure cooler inlet density', units='kg/m3', type='ARRAY')
    LP_cooler_in_isen_deltah_to_P_mc_out_od: Final[Array] = OUTPUT(label='Off-design Low pressure cooler inlet isen enthalpy rise to mc outlet pressure', units='kJ/kg', type='ARRAY')
    LP_cooler_co2_deltaP_od: Final[Array] = OUTPUT(label='Off-design Off-design low pressure cooler co2 side pressure drop', units='-', type='ARRAY')
    LP_cooler_W_dot_fan_od: Final[Array] = OUTPUT(label='Off-design Low pressure cooler fan power', units='MWe', type='ARRAY')
    IP_cooler_W_dot_fan_od: Final[Array] = OUTPUT(label='Off-design Intermediate pressure cooler fan power', units='MWe', type='ARRAY')
    cooler_tot_W_dot_fan_od: Final[Array] = OUTPUT(label='Intermediate pressure cooler fan power', units='MWe', type='ARRAY')
    diff_m_dot_od: Final[Array] = OUTPUT(label='Off-design mass flow rate balance', units='-', type='ARRAY')
    diff_E_cycle: Final[Array] = OUTPUT(label='Off-design cycle energy balance', units='-', type='ARRAY')
    diff_Q_LTR: Final[Array] = OUTPUT(label='Off-design LTR energy balance', units='-', type='ARRAY')
    diff_Q_HTR: Final[Array] = OUTPUT(label='Off-design HTR energy balance', units='-', type='ARRAY')
    udpc_table: Final[Matrix] = OUTPUT(label='Columns (7): HTF Temp [C], HTF ND mass flow [-], Ambient Temp [C], ND Power, ND Heat In, ND Fan Power, ND Water. Rows = runs', type='MATRIX')
    udpc_n_T_htf: Final[float] = OUTPUT(label='Number of HTF temperature values in udpc parametric', type='NUMBER')
    udpc_n_T_amb: Final[float] = OUTPUT(label='Number of ambient temperature values in udpc parametric', type='NUMBER')
    udpc_n_m_dot_htf: Final[float] = OUTPUT(label='Number of HTF mass flow rate values in udpc parameteric', type='NUMBER')
    od_code: Final[Array] = OUTPUT(label='Diagnostic info', units='-', type='ARRAY')

    def __init__(self, *args: Mapping[str, Any],
                 htf: float = ...,
                 htf_props: Matrix = ...,
                 T_htf_hot_des: float = ...,
                 dT_PHX_hot_approach: float = ...,
                 T_amb_des: float = ...,
                 dT_mc_approach: float = ...,
                 site_elevation: float = ...,
                 W_dot_net_des: float = ...,
                 design_method: float = ...,
                 eta_thermal_des: float = ...,
                 UA_recup_tot_des: float = ...,
                 LTR_design_code: float = ...,
                 LTR_UA_des_in: float = ...,
                 LTR_min_dT_des_in: float = ...,
                 LTR_eff_des_in: float = ...,
                 LT_recup_eff_max: float = ...,
                 LTR_LP_deltaP_des_in: float = ...,
                 LTR_HP_deltaP_des_in: float = ...,
                 HTR_design_code: float = ...,
                 HTR_UA_des_in: float = ...,
                 HTR_min_dT_des_in: float = ...,
                 HTR_eff_des_in: float = ...,
                 HT_recup_eff_max: float = ...,
                 HTR_LP_deltaP_des_in: float = ...,
                 HTR_HP_deltaP_des_in: float = ...,
                 cycle_config: float = ...,
                 is_recomp_ok: float = ...,
                 is_P_high_fixed: float = ...,
                 is_PR_fixed: float = ...,
                 is_IP_fixed: float = ...,
                 des_objective: float = ...,
                 min_phx_deltaT: float = ...,
                 rel_tol: float = ...,
                 eta_isen_mc: float = ...,
                 eta_isen_rc: float = ...,
                 eta_isen_pc: float = ...,
                 eta_isen_t: float = ...,
                 PHX_co2_deltaP_des_in: float = ...,
                 deltaP_counterHX_frac: float = ...,
                 P_high_limit: float = ...,
                 dT_PHX_cold_approach: float = ...,
                 is_design_air_cooler: float = ...,
                 fan_power_frac: float = ...,
                 deltaP_cooler_frac: float = ...,
                 od_T_t_in_mode: float = ...,
                 od_cases: Matrix = ...,
                 od_P_mc_in_sweep: Array = ...,
                 od_set_control: Matrix = ...,
                 od_generate_udpc: Array = ...,
                 is_gen_od_polynomials: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
