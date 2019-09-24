
# This is a generated file

"""sco2_csp_system - ..."""

# VERSION: 0

from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

try:
    from mypy_extensions import TypedDict
except ImportError:
    DataDict = Dict[str, Any]
else:
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
        'cycle_config': float,
        'is_recomp_ok': float,
        'is_P_high_fixed': float,
        'is_PR_fixed': float,
        'des_objective': float,
        'min_phx_deltaT': float,
        'rel_tol': float,
        'eta_isen_mc': float,
        'eta_isen_rc': float,
        'eta_isen_pc': float,
        'eta_isen_t': float,
        'LT_recup_eff_max': float,
        'HT_recup_eff_max': float,
        'deltaP_counterHX_frac': float,
        'P_high_limit': float,
        'dT_PHX_cold_approach': float,
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
        'mc_W_dot': float,
        'mc_m_dot_des': float,
        'mc_phi_des': float,
        'mc_tip_ratio_des': Array,
        'mc_n_stages': float,
        'mc_N_des': float,
        'mc_D': Array,
        'mc_phi_surge': float,
        'mc_eta_stages_des': Array,
        'mc_cost': float,
        'rc_T_in_des': float,
        'rc_W_dot': float,
        'rc_m_dot_des': float,
        'rc_phi_des': float,
        'rc_tip_ratio_des': Array,
        'rc_n_stages': float,
        'rc_N_des': float,
        'rc_D': Array,
        'rc_phi_surge': float,
        'rc_eta_stages_des': Array,
        'rc_cost': float,
        'pc_T_in_des': float,
        'pc_P_in_des': float,
        'pc_W_dot': float,
        'pc_m_dot_des': float,
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
        't_nu_des': float,
        't_tip_ratio_des': float,
        't_N_des': float,
        't_D': float,
        't_cost': float,
        'UA_recup_total': float,
        'recup_total_cost': float,
        'recup_LTR_UA_frac': float,
        'UA_LTR': float,
        'eff_LTR': float,
        'NTU_LTR': float,
        'q_dot_LTR': float,
        'LTR_min_dT': float,
        'LTR_cost': float,
        'UA_HTR': float,
        'eff_HTR': float,
        'NTU_HTR': float,
        'q_dot_HTR': float,
        'HTR_min_dT': float,
        'HTR_cost': float,
        'UA_PHX': float,
        'eff_PHX': float,
        'NTU_PHX': float,
        'T_co2_PHX_in': float,
        'deltaT_HTF_PHX': float,
        'q_dot_PHX': float,
        'PHX_cost': float,
        'LP_cooler_T_in': float,
        'LP_cooler_P_in': float,
        'LP_cooler_m_dot_co2': float,
        'LP_cooler_UA': float,
        'LP_cooler_q_dot': float,
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
        'od_cases': Matrix,
        'od_P_mc_in_sweep': Array,
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
        'mc_W_dot_od': Array,
        'mc_m_dot_od': Array,
        'mc_N_od': Array,
        'mc_eta_od': Array,
        'mc_tip_ratio_od': Matrix,
        'mc_eta_stages_od': Matrix,
        'mc_f_bypass_od': Array,
        'rc_T_in_od': Array,
        'rc_W_dot_od': Array,
        'rc_m_dot_od': Array,
        'rc_eta_od': Array,
        'rc_phi_od': Matrix,
        'rc_N_od': Array,
        'rc_tip_ratio_od': Matrix,
        'rc_eta_stages_od': Matrix,
        'pc_T_in_od': Array,
        'pc_P_in_od': Array,
        'pc_W_dot_od': Array,
        'pc_m_dot_od': Array,
        'pc_eta_od': Array,
        'pc_phi_od': Matrix,
        'pc_N_od': Array,
        'pc_tip_ratio_od': Matrix,
        'pc_eta_stages_od': Matrix,
        'pc_f_bypass_od': Array,
        'c_tot_W_dot_od': Array,
        't_W_dot_od': Array,
        't_m_dot_od': Array,
        't_nu_od': Array,
        't_N_od': Array,
        't_tip_ratio_od': Array,
        't_eta_od': Array,
        'eff_LTR_od': Array,
        'q_dot_LTR_od': Array,
        'eff_HTR_od': Array,
        'q_dot_HTR_od': Array,
        'T_co2_PHX_in_od': Array,
        'T_co2_PHX_out_od': Array,
        'deltaT_HTF_PHX_od': Array,
        'phx_eff_od': Array,
        'LP_cooler_W_dot_fan_od': Array,
        'IP_cooler_W_dot_fan_od': Array,
        'cooler_tot_W_dot_fan_od': Array,
        'od_code': Array
    }, total=False)

class Data(ssc.DataDict):
    htf: float = INPUT(label='Integer code for HTF used in PHX', type='NUMBER', required='*')
    htf_props: Matrix = INPUT(label='User defined HTF property data', type='MATRIX', required='?=[[0]]', meta='7 columns (T,Cp,dens,visc,kvisc,cond,h), at least 3 rows')
    T_htf_hot_des: float = INPUT(label='HTF design hot temperature (PHX inlet)', units='C', type='NUMBER', required='*')
    dT_PHX_hot_approach: float = INPUT(label='Temp diff btw hot HTF and turbine inlet', units='C', type='NUMBER', required='*')
    T_amb_des: float = INPUT(label='Ambient temperature', units='C', type='NUMBER', required='*')
    dT_mc_approach: float = INPUT(label='Temp diff btw ambient air and main compressor inlet', units='C', type='NUMBER', required='*')
    site_elevation: float = INPUT(label='Site elevation', units='m', type='NUMBER', required='*')
    W_dot_net_des: float = INPUT(label='Design cycle power output (no cooling parasitics)', units='MWe', type='NUMBER', required='*')
    design_method: float = INPUT(label='1 = Specify efficiency, 2 = Specify total recup UA', type='NUMBER', required='*')
    eta_thermal_des: float = INPUT(label='Power cycle thermal efficiency', type='NUMBER', required='?=-1.0')
    UA_recup_tot_des: float = INPUT(label='Total recuperator conductance', units='kW/K', type='NUMBER', required='?=-1.0')
    cycle_config: float = INPUT(label='1 = recompression, 2 = partial cooling', type='NUMBER', required='?=1')
    is_recomp_ok: float = INPUT(label='1 = Yes, 0 = simple cycle only', type='NUMBER', required='?=1')
    is_P_high_fixed: float = INPUT(label='1 = Yes, 0 = No, optimized (default)', type='NUMBER', required='?=0')
    is_PR_fixed: float = INPUT(label='0 = No, >0 = fixed pressure ratio', type='NUMBER', required='?=0')
    des_objective: float = INPUT(label='[2] = hit min phx deltat then max eta, [else] max eta', type='NUMBER', required='?=0')
    min_phx_deltaT: float = INPUT(label='Minimum design temperature difference across PHX', units='C', type='NUMBER', required='?=0')
    rel_tol: float = INPUT(label='Baseline solver and optimization relative tolerance exponent (10^-rel_tol)', units='-', type='NUMBER', required='?=3')
    eta_isen_mc: float = INPUT(label='Design main compressor isentropic efficiency', units='-', type='NUMBER', required='*')
    eta_isen_rc: float = INPUT(label='Design re-compressor isentropic efficiency', units='-', type='NUMBER', required='*')
    eta_isen_pc: float = INPUT(label='Design precompressor isentropic efficiency', units='-', type='NUMBER', required='cycle_config=2')
    eta_isen_t: float = INPUT(label='Design turbine isentropic efficiency', units='-', type='NUMBER', required='*')
    LT_recup_eff_max: float = INPUT(label='Maximum allowable effectiveness in LT recuperator', units='-', type='NUMBER', required='*')
    HT_recup_eff_max: float = INPUT(label='Maximum allowable effectiveness in LT recuperator', units='-', type='NUMBER', required='*')
    deltaP_counterHX_frac: float = INPUT(label='Fraction of CO2 inlet pressure that is design point counterflow HX (recups & PHX) pressure drop', units='-', type='NUMBER', required='?=0')
    P_high_limit: float = INPUT(label='High pressure limit in cycle', units='MPa', type='NUMBER', required='*')
    dT_PHX_cold_approach: float = INPUT(label='Temp diff btw cold HTF and cold CO2', units='C', type='NUMBER', required='*')
    fan_power_frac: float = INPUT(label='Fraction of net cycle power consumed by air cooler fan', type='NUMBER', required='*')
    deltaP_cooler_frac: float = INPUT(label='Fraction of CO2 inlet pressure that is design point cooler CO2 pressure drop', type='NUMBER', required='*')
    T_htf_cold_des: Final[float] = OUTPUT(label='HTF design cold temperature (PHX outlet)', units='C', type='NUMBER', required='*')
    m_dot_htf_des: Final[float] = OUTPUT(label='HTF mass flow rate', units='kg/s', type='NUMBER', required='*')
    eta_thermal_calc: Final[float] = OUTPUT(label='Calculated cycle thermal efficiency', units='-', type='NUMBER', required='*')
    m_dot_co2_full: Final[float] = OUTPUT(label='CO2 mass flow rate through HTR, PHX, turbine', units='kg/s', type='NUMBER', required='*')
    recomp_frac: Final[float] = OUTPUT(label='Recompression fraction', units='-', type='NUMBER', required='*')
    cycle_cost: Final[float] = OUTPUT(label='Cycle cost', units='M$', type='NUMBER', required='*')
    cycle_spec_cost: Final[float] = OUTPUT(label='Cycle specific cost', units='$/kWe', type='NUMBER', required='*')
    cycle_spec_cost_thermal: Final[float] = OUTPUT(label='Cycle specific cost - thermal', units='$/kWt', type='NUMBER', required='*')
    T_comp_in: Final[float] = OUTPUT(label='Compressor inlet temperature', units='C', type='NUMBER', required='*')
    P_comp_in: Final[float] = OUTPUT(label='Compressor inlet pressure', units='MPa', type='NUMBER', required='*')
    P_comp_out: Final[float] = OUTPUT(label='Compressor outlet pressure', units='MPa', type='NUMBER', required='*')
    mc_W_dot: Final[float] = OUTPUT(label='Compressor power', units='MWe', type='NUMBER', required='*')
    mc_m_dot_des: Final[float] = OUTPUT(label='Compressor mass flow rate', units='kg/s', type='NUMBER', required='*')
    mc_phi_des: Final[float] = OUTPUT(label='Compressor design flow coefficient', type='NUMBER', required='*')
    mc_tip_ratio_des: Final[Array] = OUTPUT(label='Compressor design stage tip speed ratio', type='ARRAY', required='*')
    mc_n_stages: Final[float] = OUTPUT(label='Compressor stages', type='NUMBER', required='*')
    mc_N_des: Final[float] = OUTPUT(label='Compressor design shaft speed', units='rpm', type='NUMBER', required='*')
    mc_D: Final[Array] = OUTPUT(label='Compressor stage diameters', units='m', type='ARRAY', required='*')
    mc_phi_surge: Final[float] = OUTPUT(label='Compressor flow coefficient where surge occurs', type='NUMBER', required='*')
    mc_eta_stages_des: Final[Array] = OUTPUT(label='Compressor design stage isentropic efficiencies', type='ARRAY', required='*')
    mc_cost: Final[float] = OUTPUT(label='Compressor cost', units='M$', type='NUMBER', required='*')
    rc_T_in_des: Final[float] = OUTPUT(label='Recompressor inlet temperature', units='C', type='NUMBER', required='*')
    rc_W_dot: Final[float] = OUTPUT(label='Recompressor power', units='MWe', type='NUMBER', required='*')
    rc_m_dot_des: Final[float] = OUTPUT(label='Recompressor mass flow rate', units='kg/s', type='NUMBER', required='*')
    rc_phi_des: Final[float] = OUTPUT(label='Recompressor design flow coefficient', type='NUMBER', required='*')
    rc_tip_ratio_des: Final[Array] = OUTPUT(label='Recompressor design stage tip speed ratio', type='ARRAY', required='*')
    rc_n_stages: Final[float] = OUTPUT(label='Recompressor stages', type='NUMBER', required='*')
    rc_N_des: Final[float] = OUTPUT(label='Recompressor design shaft speed', units='rpm', type='NUMBER', required='*')
    rc_D: Final[Array] = OUTPUT(label='Recompressor stage diameters', units='m', type='ARRAY', required='*')
    rc_phi_surge: Final[float] = OUTPUT(label='Recompressor flow coefficient where surge occurs', type='NUMBER', required='*')
    rc_eta_stages_des: Final[Array] = OUTPUT(label='Recompressor design stage isenstropic efficiencies', type='ARRAY', required='*')
    rc_cost: Final[float] = OUTPUT(label='Recompressor cost', units='M$', type='NUMBER', required='*')
    pc_T_in_des: Final[float] = OUTPUT(label='Precompressor inlet temperature', units='C', type='NUMBER', required='*')
    pc_P_in_des: Final[float] = OUTPUT(label='Precompressor inlet pressure', units='MPa', type='NUMBER', required='*')
    pc_W_dot: Final[float] = OUTPUT(label='Precompressor power', units='MWe', type='NUMBER', required='*')
    pc_m_dot_des: Final[float] = OUTPUT(label='Precompressor mass flow rate', units='kg/s', type='NUMBER', required='*')
    pc_phi_des: Final[float] = OUTPUT(label='Precompressor design flow coefficient', type='NUMBER', required='*')
    pc_tip_ratio_des: Final[Array] = OUTPUT(label='Precompressor design stage tip speed ratio', type='ARRAY', required='*')
    pc_n_stages: Final[float] = OUTPUT(label='Precompressor stages', type='NUMBER', required='*')
    pc_N_des: Final[float] = OUTPUT(label='Precompressor design shaft speed', units='rpm', type='NUMBER', required='*')
    pc_D: Final[Array] = OUTPUT(label='Precompressor stage diameters', units='m', type='ARRAY', required='*')
    pc_phi_surge: Final[float] = OUTPUT(label='Precompressor flow coefficient where surge occurs', type='NUMBER', required='*')
    pc_eta_stages_des: Final[Array] = OUTPUT(label='Precompressor design stage isenstropic efficiencies', type='ARRAY', required='*')
    pc_cost: Final[float] = OUTPUT(label='Precompressor cost', units='M$', type='NUMBER', required='*')
    c_tot_cost: Final[float] = OUTPUT(label='Compressor total cost', units='M$', type='NUMBER', required='*')
    c_tot_W_dot: Final[float] = OUTPUT(label='Compressor total summed power', units='MWe', type='NUMBER', required='*')
    t_W_dot: Final[float] = OUTPUT(label='Turbine power', units='MWe', type='NUMBER', required='*')
    t_m_dot_des: Final[float] = OUTPUT(label='Turbine mass flow rate', units='kg/s', type='NUMBER', required='*')
    T_turb_in: Final[float] = OUTPUT(label='Turbine inlet temperature', units='C', type='NUMBER', required='*')
    t_nu_des: Final[float] = OUTPUT(label='Turbine design velocity ratio', type='NUMBER', required='*')
    t_tip_ratio_des: Final[float] = OUTPUT(label='Turbine design tip speed ratio', type='NUMBER', required='*')
    t_N_des: Final[float] = OUTPUT(label='Turbine design shaft speed', units='rpm', type='NUMBER', required='*')
    t_D: Final[float] = OUTPUT(label='Turbine diameter', units='m', type='NUMBER', required='*')
    t_cost: Final[float] = OUTPUT(label='Tubine cost', units='M$', type='NUMBER', required='*')
    UA_recup_total: Final[float] = OUTPUT(label='Total recuperator UA', units='MW/K', type='NUMBER', required='*')
    recup_total_cost: Final[float] = OUTPUT(label='Total recuperator cost', units='M$', type='NUMBER', required='*')
    recup_LTR_UA_frac: Final[float] = OUTPUT(label='Fraction of total conductance to LTR', type='NUMBER', required='*')
    UA_LTR: Final[float] = OUTPUT(label='Low temp recuperator UA', units='MW/K', type='NUMBER', required='*')
    eff_LTR: Final[float] = OUTPUT(label='Low temp recuperator effectiveness', type='NUMBER', required='*')
    NTU_LTR: Final[float] = OUTPUT(label='Low temp recuperator NTU', type='NUMBER', required='*')
    q_dot_LTR: Final[float] = OUTPUT(label='Low temp recuperator heat transfer', units='MWt', type='NUMBER', required='*')
    LTR_min_dT: Final[float] = OUTPUT(label='Low temp recuperator min temperature difference', units='C', type='NUMBER', required='*')
    LTR_cost: Final[float] = OUTPUT(label='Low temp recuperator cost', units='M$', type='NUMBER', required='*')
    UA_HTR: Final[float] = OUTPUT(label='High temp recuperator UA', units='MW/K', type='NUMBER', required='*')
    eff_HTR: Final[float] = OUTPUT(label='High temp recuperator effectiveness', type='NUMBER', required='*')
    NTU_HTR: Final[float] = OUTPUT(label='High temp recuperator NTRU', type='NUMBER', required='*')
    q_dot_HTR: Final[float] = OUTPUT(label='High temp recuperator heat transfer', units='MWt', type='NUMBER', required='*')
    HTR_min_dT: Final[float] = OUTPUT(label='High temp recuperator min temperature difference', units='C', type='NUMBER', required='*')
    HTR_cost: Final[float] = OUTPUT(label='High temp recuperator cost', units='M$', type='NUMBER', required='*')
    UA_PHX: Final[float] = OUTPUT(label='PHX Conductance', units='MW/K', type='NUMBER', required='*')
    eff_PHX: Final[float] = OUTPUT(label='PHX effectiveness', type='NUMBER', required='*')
    NTU_PHX: Final[float] = OUTPUT(label='PHX NTU', type='NUMBER', required='*')
    T_co2_PHX_in: Final[float] = OUTPUT(label='CO2 temperature at PHX inlet', units='C', type='NUMBER', required='*')
    deltaT_HTF_PHX: Final[float] = OUTPUT(label='HTF temp difference across PHX', units='C', type='NUMBER', required='*')
    q_dot_PHX: Final[float] = OUTPUT(label='PHX heat transfer', units='MWt', type='NUMBER', required='*')
    PHX_cost: Final[float] = OUTPUT(label='PHX cost', units='M$', type='NUMBER', required='*')
    LP_cooler_T_in: Final[float] = OUTPUT(label='Low pressure cross flow cooler inlet temperature', units='C', type='NUMBER', required='*')
    LP_cooler_P_in: Final[float] = OUTPUT(label='Low pressure cross flow cooler inlet pressure', units='MPa', type='NUMBER', required='*')
    LP_cooler_m_dot_co2: Final[float] = OUTPUT(label='Low pressure cross flow cooler CO2 mass flow rate', units='kg/s', type='NUMBER', required='*')
    LP_cooler_UA: Final[float] = OUTPUT(label='Low pressure cross flow cooler conductance', units='MW/K', type='NUMBER', required='*')
    LP_cooler_q_dot: Final[float] = OUTPUT(label='Low pressure cooler heat transfer', units='MWt', type='NUMBER', required='*')
    LP_cooler_W_dot_fan: Final[float] = OUTPUT(label='Low pressure cooler fan power', units='MWe', type='NUMBER', required='*')
    LP_cooler_cost: Final[float] = OUTPUT(label='Low pressure cooler cost', units='M$', type='NUMBER', required='*')
    IP_cooler_T_in: Final[float] = OUTPUT(label='Intermediate pressure cross flow cooler inlet temperature', units='C', type='NUMBER', required='*')
    IP_cooler_P_in: Final[float] = OUTPUT(label='Intermediate pressure cross flow cooler inlet pressure', units='MPa', type='NUMBER', required='*')
    IP_cooler_m_dot_co2: Final[float] = OUTPUT(label='Intermediate pressure cross flow cooler CO2 mass flow rate', units='kg/s', type='NUMBER', required='*')
    IP_cooler_UA: Final[float] = OUTPUT(label='Intermediate pressure cross flow cooler conductance', units='MW/K', type='NUMBER', required='*')
    IP_cooler_q_dot: Final[float] = OUTPUT(label='Intermediate pressure cooler heat transfer', units='MWt', type='NUMBER', required='*')
    IP_cooler_W_dot_fan: Final[float] = OUTPUT(label='Intermediate pressure cooler fan power', units='MWe', type='NUMBER', required='*')
    IP_cooler_cost: Final[float] = OUTPUT(label='Intermediate pressure cooler cost', units='M$', type='NUMBER', required='*')
    cooler_tot_cost: Final[float] = OUTPUT(label='Total cooler cost', units='M$', type='NUMBER', required='*')
    cooler_tot_UA: Final[float] = OUTPUT(label='Total cooler conductance', units='MW/K', type='NUMBER', required='*')
    cooler_tot_W_dot_fan: Final[float] = OUTPUT(label='Total cooler fan power', units='MWe', type='NUMBER', required='*')
    T_state_points: Final[Array] = OUTPUT(label='Cycle temperature state points', units='C', type='ARRAY', required='*')
    P_state_points: Final[Array] = OUTPUT(label='Cycle pressure state points', units='MPa', type='ARRAY', required='*')
    s_state_points: Final[Array] = OUTPUT(label='Cycle entropy state points', units='kJ/kg-K', type='ARRAY', required='*')
    h_state_points: Final[Array] = OUTPUT(label='Cycle enthalpy state points', units='kJ/kg', type='ARRAY', required='*')
    T_LTR_HP_data: Final[Array] = OUTPUT(label='Temperature points along LTR HP stream', units='C', type='ARRAY', required='*')
    s_LTR_HP_data: Final[Array] = OUTPUT(label='Entropy points along LTR HP stream', units='kJ/kg-K', type='ARRAY', required='*')
    T_HTR_HP_data: Final[Array] = OUTPUT(label='Temperature points along HTR HP stream', units='C', type='ARRAY', required='*')
    s_HTR_HP_data: Final[Array] = OUTPUT(label='Entropy points along HTR HP stream', units='kJ/kg-K', type='ARRAY', required='*')
    T_PHX_data: Final[Array] = OUTPUT(label='Temperature points along PHX stream', units='C', type='ARRAY', required='*')
    s_PHX_data: Final[Array] = OUTPUT(label='Entropy points along PHX stream', units='kJ/kg-K', type='ARRAY', required='*')
    T_HTR_LP_data: Final[Array] = OUTPUT(label='Temperature points along HTR LP stream', units='C', type='ARRAY', required='*')
    s_HTR_LP_data: Final[Array] = OUTPUT(label='Entropy points along HTR LP stream', units='kJ/kg-K', type='ARRAY', required='*')
    T_LTR_LP_data: Final[Array] = OUTPUT(label='Temperature points along LTR LP stream', units='C', type='ARRAY', required='*')
    s_LTR_LP_data: Final[Array] = OUTPUT(label='Entropy points along LTR LP stream', units='kJ/kg-K', type='ARRAY', required='*')
    T_main_cooler_data: Final[Array] = OUTPUT(label='Temperature points along main cooler stream', units='C', type='ARRAY', required='*')
    s_main_cooler_data: Final[Array] = OUTPUT(label='Entropy points along main cooler stream', units='kJ/kg-K', type='ARRAY', required='*')
    T_pre_cooler_data: Final[Array] = OUTPUT(label='Temperature points along pre cooler stream', units='C', type='ARRAY', required='*')
    s_pre_cooler_data: Final[Array] = OUTPUT(label='Entropy points along pre cooler stream', units='kJ/kg-K', type='ARRAY', required='*')
    P_t_data: Final[Array] = OUTPUT(label='Pressure points along turbine expansion', units='MPa', type='ARRAY', required='*')
    h_t_data: Final[Array] = OUTPUT(label='Enthalpy points along turbine expansion', units='kJ/kg', type='ARRAY', required='*')
    P_mc_data: Final[Array] = OUTPUT(label='Pressure points along main compression', units='MPa', type='ARRAY', required='*')
    h_mc_data: Final[Array] = OUTPUT(label='Enthalpy points along main compression', units='kJ/kg', type='ARRAY', required='*')
    P_rc_data: Final[Array] = OUTPUT(label='Pressure points along re compression', units='MPa', type='ARRAY', required='*')
    h_rc_data: Final[Array] = OUTPUT(label='Enthalpy points along re compression', units='kJ/kg', type='ARRAY', required='*')
    P_pc_data: Final[Array] = OUTPUT(label='Pressure points along pre compression', units='MPa', type='ARRAY', required='*')
    h_pc_data: Final[Array] = OUTPUT(label='Enthalpy points along pre compression', units='kJ/kg', type='ARRAY', required='*')
    od_cases: Matrix = INPUT(label='Columns: T_htf_C, m_dot_htf_ND, T_amb_C, od_opt_obj (1: MAX_ETA, 2: MAX_POWER), Rows: cases', type='MATRIX')
    od_P_mc_in_sweep: Array = INPUT(label='Columns: T_htf_C, m_dot_htf_ND, T_amb_C, od_opt_obj (1: MAX_ETA, 2: MAX_POWER)', type='ARRAY')
    is_gen_od_polynomials: float = INPUT(label='Generate off-design polynomials for Generic CSP models? 1 = Yes, 0 = No', type='NUMBER', required='?=0')
    m_dot_htf_fracs: Final[Array] = OUTPUT(label='Normalized mass flow rate', type='ARRAY')
    T_amb_od: Final[Array] = OUTPUT(label='Ambient temperatures', units='C', type='ARRAY')
    T_htf_hot_od: Final[Array] = OUTPUT(label='HTF hot temperatures', units='C', type='ARRAY')
    od_opt_obj_code: Final[Array] = OUTPUT(label='1: MAX_ETA, 2: MAX_POWER', type='ARRAY')
    od_opt_conv_tol: Final[Array] = OUTPUT(label='Off design optimizer convergence tolerance', type='ARRAY')
    P_comp_in_od: Final[Array] = OUTPUT(label='Main compressor inlet pressures', units='MPa', type='ARRAY')
    mc_phi_od: Final[Matrix] = OUTPUT(label='Off-design main compressor flow coefficient [od run][stage]', type='MATRIX')
    recomp_frac_od: Final[Array] = OUTPUT(label='Recompression fractions', type='ARRAY')
    sim_time_od: Final[Array] = OUTPUT(label='Simulation time for off design optimization', units='s', type='ARRAY')
    eta_thermal_od: Final[Array] = OUTPUT(label='Off-design cycle thermal efficiency', type='ARRAY')
    T_mc_in_od: Final[Array] = OUTPUT(label='Off-design compressor inlet temperature', units='C', type='ARRAY')
    P_mc_out_od: Final[Array] = OUTPUT(label='Off-design high side pressure', units='MPa', type='ARRAY')
    T_htf_cold_od: Final[Array] = OUTPUT(label='Off-design cold return temperature', units='C', type='ARRAY')
    m_dot_co2_full_od: Final[Array] = OUTPUT(label='Off-design mass flow rate through turbine', units='kg/s', type='ARRAY')
    W_dot_net_od: Final[Array] = OUTPUT(label='Off-design cycle net output (no cooling pars)', units='MWe', type='ARRAY')
    Q_dot_od: Final[Array] = OUTPUT(label='Off-design thermal input', units='MWt', type='ARRAY')
    mc_W_dot_od: Final[Array] = OUTPUT(label='Off-design main compressor power', units='MWe', type='ARRAY')
    mc_m_dot_od: Final[Array] = OUTPUT(label='Off-design main compressor mass flow', units='kg/s', type='ARRAY')
    mc_N_od: Final[Array] = OUTPUT(label='Off-design main compressor speed', units='rpm', type='ARRAY')
    mc_eta_od: Final[Array] = OUTPUT(label='Off-design main compressor overall isentropic efficiency', type='ARRAY')
    mc_tip_ratio_od: Final[Matrix] = OUTPUT(label='Off-design main compressor tip speed ratio [od run][stage]', type='MATRIX')
    mc_eta_stages_od: Final[Matrix] = OUTPUT(label='Off-design main compressor stages isentropic efficiency [od run][stage]', type='MATRIX')
    mc_f_bypass_od: Final[Array] = OUTPUT(label='Off-design main compressor bypass to cooler inlet', units='-', type='ARRAY')
    rc_T_in_od: Final[Array] = OUTPUT(label='Off-design recompressor inlet temperature', units='C', type='ARRAY')
    rc_W_dot_od: Final[Array] = OUTPUT(label='Off-design recompressor power', units='MWe', type='ARRAY')
    rc_m_dot_od: Final[Array] = OUTPUT(label='Off-design recompressor mass flow', units='kg/s', type='ARRAY')
    rc_eta_od: Final[Array] = OUTPUT(label='Off-design recompressor overal isentropic efficiency', type='ARRAY')
    rc_phi_od: Final[Matrix] = OUTPUT(label='Off-design recompressor flow coefficient [od run][stage]', units='-', type='MATRIX')
    rc_N_od: Final[Array] = OUTPUT(label='Off-design recompressor shaft speed', units='rpm', type='ARRAY')
    rc_tip_ratio_od: Final[Matrix] = OUTPUT(label='Off-design recompressor tip speed ratio [od run][stage]', units='-', type='MATRIX')
    rc_eta_stages_od: Final[Matrix] = OUTPUT(label='Off-design recompressor stages isentropic efficiency [od run][stage]', type='MATRIX')
    pc_T_in_od: Final[Array] = OUTPUT(label='Off-design precompressor inlet temperature', units='C', type='ARRAY')
    pc_P_in_od: Final[Array] = OUTPUT(label='Off-design precompressor inlet pressure', units='MPa', type='ARRAY')
    pc_W_dot_od: Final[Array] = OUTPUT(label='Off-design precompressor power', units='MWe', type='ARRAY')
    pc_m_dot_od: Final[Array] = OUTPUT(label='Off-design precompressor mass flow', units='kg/s', type='ARRAY')
    pc_eta_od: Final[Array] = OUTPUT(label='Off-design precompressor overal isentropic efficiency', type='ARRAY')
    pc_phi_od: Final[Matrix] = OUTPUT(label='Off-design precompressor flow coefficient [od run][stage]', units='-', type='MATRIX')
    pc_N_od: Final[Array] = OUTPUT(label='Off-design precompressor shaft speed', units='rpm', type='ARRAY')
    pc_tip_ratio_od: Final[Matrix] = OUTPUT(label='Off-design precompressor tip speed ratio [od run][stage]', units='-', type='MATRIX')
    pc_eta_stages_od: Final[Matrix] = OUTPUT(label='Off-design precompressor stages isentropic efficiency [od run][stage]', type='MATRIX')
    pc_f_bypass_od: Final[Array] = OUTPUT(label='Off-design precompressor bypass to cooler inlet', units='-', type='ARRAY')
    c_tot_W_dot_od: Final[Array] = OUTPUT(label='Compressor total off-design power', units='MWe', type='ARRAY')
    t_W_dot_od: Final[Array] = OUTPUT(label='Off-design turbine power', units='MWe', type='ARRAY')
    t_m_dot_od: Final[Array] = OUTPUT(label='Off-design turbine mass flow rate', units='kg/s', type='ARRAY')
    t_nu_od: Final[Array] = OUTPUT(label='Off-design turbine velocity ratio', units='-', type='ARRAY')
    t_N_od: Final[Array] = OUTPUT(label='Off-design turbine shaft speed', units='rpm', type='ARRAY')
    t_tip_ratio_od: Final[Array] = OUTPUT(label='Off-design turbine tip speed ratio', units='-', type='ARRAY')
    t_eta_od: Final[Array] = OUTPUT(label='Off-design turbine efficiency', units='-', type='ARRAY')
    eff_LTR_od: Final[Array] = OUTPUT(label='Off-design low temp recup effectiveness', type='ARRAY')
    q_dot_LTR_od: Final[Array] = OUTPUT(label='Off-design low temp recup heat transfer', units='MWt', type='ARRAY')
    eff_HTR_od: Final[Array] = OUTPUT(label='Off-design high temp recup effectiveness', type='ARRAY')
    q_dot_HTR_od: Final[Array] = OUTPUT(label='Off-design high temp recup heat transfer', units='MWt', type='ARRAY')
    T_co2_PHX_in_od: Final[Array] = OUTPUT(label='Off-design PHX co2 inlet temperature', units='C', type='ARRAY')
    T_co2_PHX_out_od: Final[Array] = OUTPUT(label='Off-design PHX co2 outlet temperature', units='C', type='ARRAY')
    deltaT_HTF_PHX_od: Final[Array] = OUTPUT(label='Off-design HTF temp difference across PHX', units='C', type='ARRAY')
    phx_eff_od: Final[Array] = OUTPUT(label='Off-design PHX effectiveness', units='-', type='ARRAY')
    LP_cooler_W_dot_fan_od: Final[Array] = OUTPUT(label='Low pressure cooler fan power', units='MWe', type='ARRAY')
    IP_cooler_W_dot_fan_od: Final[Array] = OUTPUT(label='Intermediate pressure cooler fan power', units='MWe', type='ARRAY')
    cooler_tot_W_dot_fan_od: Final[Array] = OUTPUT(label='Intermediate pressure cooler fan power', units='MWe', type='ARRAY')
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
                 cycle_config: float = ...,
                 is_recomp_ok: float = ...,
                 is_P_high_fixed: float = ...,
                 is_PR_fixed: float = ...,
                 des_objective: float = ...,
                 min_phx_deltaT: float = ...,
                 rel_tol: float = ...,
                 eta_isen_mc: float = ...,
                 eta_isen_rc: float = ...,
                 eta_isen_pc: float = ...,
                 eta_isen_t: float = ...,
                 LT_recup_eff_max: float = ...,
                 HT_recup_eff_max: float = ...,
                 deltaP_counterHX_frac: float = ...,
                 P_high_limit: float = ...,
                 dT_PHX_cold_approach: float = ...,
                 fan_power_frac: float = ...,
                 deltaP_cooler_frac: float = ...,
                 od_cases: Matrix = ...,
                 od_P_mc_in_sweep: Array = ...,
                 is_gen_od_polynomials: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
