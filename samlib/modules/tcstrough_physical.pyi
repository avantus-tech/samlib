
# This is a generated file

"""tcstrough_physical - CSP model using the emperical trough TCS types."""

# VERSION: 4

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'file_name': str,
        'track_mode': float,
        'tilt': float,
        'azimuth': float,
        'system_capacity': float,
        'nSCA': float,
        'nHCEt': float,
        'nColt': float,
        'nHCEVar': float,
        'nLoops': float,
        'eta_pump': float,
        'HDR_rough': float,
        'theta_stow': float,
        'theta_dep': float,
        'Row_Distance': float,
        'FieldConfig': float,
        'T_startup': float,
        'P_ref': float,
        'm_dot_htfmin': float,
        'm_dot_htfmax': float,
        'T_loop_in_des': float,
        'T_loop_out': float,
        'Fluid': float,
        'T_fp': float,
        'I_bn_des': float,
        'calc_design_pipe_vals': float,
        'V_hdr_cold_max': float,
        'V_hdr_cold_min': float,
        'V_hdr_hot_max': float,
        'V_hdr_hot_min': float,
        'N_max_hdr_diams': float,
        'L_rnr_pb': float,
        'L_rnr_per_xpan': float,
        'L_xpan_hdr': float,
        'L_xpan_rnr': float,
        'Min_rnr_xpans': float,
        'northsouth_field_sep': float,
        'N_hdr_per_xpan': float,
        'offset_xpan_hdr': float,
        'Pipe_hl_coef': float,
        'SCA_drives_elec': float,
        'fthrok': float,
        'fthrctrl': float,
        'water_usage_per_wash': float,
        'washing_frequency': float,
        'accept_mode': float,
        'accept_init': float,
        'accept_loc': float,
        'solar_mult': float,
        'mc_bal_hot': float,
        'mc_bal_cold': float,
        'mc_bal_sca': float,
        'W_aperture': Array,
        'A_aperture': Array,
        'TrackingError': Array,
        'GeomEffects': Array,
        'Rho_mirror_clean': Array,
        'Dirt_mirror': Array,
        'Error': Array,
        'Ave_Focal_Length': Array,
        'L_SCA': Array,
        'L_aperture': Array,
        'ColperSCA': Array,
        'Distance_SCA': Array,
        'IAM_matrix': Matrix,
        'HCE_FieldFrac': Matrix,
        'D_2': Matrix,
        'D_3': Matrix,
        'D_4': Matrix,
        'D_5': Matrix,
        'D_p': Matrix,
        'Flow_type': Matrix,
        'Rough': Matrix,
        'alpha_env': Matrix,
        'epsilon_3_11': Matrix,
        'epsilon_3_12': Matrix,
        'epsilon_3_13': Matrix,
        'epsilon_3_14': Matrix,
        'epsilon_3_21': Matrix,
        'epsilon_3_22': Matrix,
        'epsilon_3_23': Matrix,
        'epsilon_3_24': Matrix,
        'epsilon_3_31': Matrix,
        'epsilon_3_32': Matrix,
        'epsilon_3_33': Matrix,
        'epsilon_3_34': Matrix,
        'epsilon_3_41': Matrix,
        'epsilon_3_42': Matrix,
        'epsilon_3_43': Matrix,
        'epsilon_3_44': Matrix,
        'alpha_abs': Matrix,
        'Tau_envelope': Matrix,
        'EPSILON_4': Matrix,
        'EPSILON_5': Matrix,
        'GlazingIntactIn': Matrix,
        'P_a': Matrix,
        'AnnulusGas': Matrix,
        'AbsorberMaterial': Matrix,
        'Shadowing': Matrix,
        'Dirt_HCE': Matrix,
        'Design_loss': Matrix,
        'SCAInfoArray': Matrix,
        'SCADefocusArray': Array,
        'K_cpnt': Matrix,
        'D_cpnt': Matrix,
        'L_cpnt': Matrix,
        'Type_cpnt': Matrix,
        'custom_sf_pipe_sizes': float,
        'sf_rnr_diams': Array,
        'sf_rnr_wallthicks': Array,
        'sf_rnr_lengths': Array,
        'sf_hdr_diams': Array,
        'sf_hdr_wallthicks': Array,
        'sf_hdr_lengths': Array,
        'field_fl_props': Matrix,
        'store_fl_props': Matrix,
        'store_fluid': float,
        'tshours': float,
        'is_hx': float,
        'dt_hot': float,
        'dt_cold': float,
        'hx_config': float,
        'q_max_aux': float,
        'T_set_aux': float,
        'V_tank_hot_ini': float,
        'T_tank_cold_ini': float,
        'vol_tank': float,
        'h_tank': float,
        'h_tank_min': float,
        'u_tank': float,
        'tank_pairs': float,
        'cold_tank_Thtr': float,
        'hot_tank_Thtr': float,
        'tank_max_heat': float,
        'tanks_in_parallel': float,
        'has_hot_tank_bypass': float,
        'T_tank_hot_inlet_min': float,
        'q_pb_design': float,
        'W_pb_design': float,
        'cycle_max_frac': float,
        'cycle_cutoff_frac': float,
        'pb_pump_coef': float,
        'tes_pump_coef': float,
        'V_tes_des': float,
        'custom_tes_p_loss': float,
        'k_tes_loss_coeffs': Array,
        'custom_sgs_pipe_sizes': float,
        'sgs_diams': Array,
        'sgs_wallthicks': Array,
        'sgs_lengths': Array,
        'DP_SGS': float,
        'pb_fixed_par': float,
        'bop_array': Array,
        'aux_array': Array,
        'fossil_mode': float,
        't_standby_reset': float,
        'sf_type': float,
        'tes_type': float,
        'tslogic_a': Array,
        'tslogic_b': Array,
        'tslogic_c': Array,
        'ffrac': Array,
        'tc_fill': float,
        'tc_void': float,
        't_dis_out_min': float,
        't_ch_out_max': float,
        'nodes': float,
        'f_tc_cold': float,
        'weekday_schedule': Matrix,
        'weekend_schedule': Matrix,
        'pc_config': float,
        'eta_ref': float,
        'startup_time': float,
        'startup_frac': float,
        'q_sby_frac': float,
        'dT_cw_ref': float,
        'T_amb_des': float,
        'P_boil': float,
        'CT': float,
        'T_approach': float,
        'T_ITD_des': float,
        'P_cond_ratio': float,
        'pb_bd_frac': float,
        'P_cond_min': float,
        'n_pl_inc': float,
        'F_wc': Array,
        'tech_type': float,
        'ud_T_amb_des': float,
        'ud_f_W_dot_cool_des': float,
        'ud_m_dot_water_cool_des': float,
        'ud_T_htf_low': float,
        'ud_T_htf_high': float,
        'ud_T_amb_low': float,
        'ud_T_amb_high': float,
        'ud_m_dot_htf_low': float,
        'ud_m_dot_htf_high': float,
        'ud_T_htf_ind_od': Matrix,
        'ud_T_amb_ind_od': Matrix,
        'ud_m_dot_htf_ind_od': Matrix,
        'ud_ind_od': Matrix,
        'eta_lhv': float,
        'eta_tes_htr': float,
        'month': Array,
        'hour': Array,
        'solazi': Array,
        'solzen': Array,
        'beam': Array,
        'tdry': Array,
        'twet': Array,
        'wspd': Array,
        'pres': Array,
        'tou_value': Array,
        'recirculating': Array,
        'pipe_header_diams': Array,
        'pipe_header_wallthk': Array,
        'pipe_header_lengths': Array,
        'pipe_header_expansions': Array,
        'pipe_header_mdot_dsn': Array,
        'pipe_header_vel_dsn': Array,
        'pipe_header_T_dsn': Array,
        'pipe_header_P_dsn': Array,
        'pipe_runner_diams': Array,
        'pipe_runner_wallthk': Array,
        'pipe_runner_lengths': Array,
        'pipe_runner_expansions': Array,
        'pipe_runner_mdot_dsn': Array,
        'pipe_runner_vel_dsn': Array,
        'pipe_runner_T_dsn': Array,
        'pipe_runner_P_dsn': Array,
        'pipe_loop_T_dsn': Array,
        'pipe_loop_P_dsn': Array,
        'Theta_ave': Array,
        'CosTh_ave': Array,
        'IAM_ave': Array,
        'RowShadow_ave': Array,
        'EndLoss_ave': Array,
        'dni_costh': Array,
        'SCAs_def': Array,
        'EqOpteff': Array,
        'q_inc_sf_tot': Array,
        'qinc_costh': Array,
        'q_abs_tot': Array,
        'q_dump': Array,
        'q_loss_tot': Array,
        'Pipe_hl': Array,
        'q_avail': Array,
        'q_loss_spec_tot': Array,
        'E_bal_startup': Array,
        'm_dot_avail': Array,
        'm_dot_htf2': Array,
        'DP_tot': Array,
        'T_sys_c': Array,
        'T_sys_h': Array,
        'T_field_in': Array,
        'pipe_sgs_diams': Array,
        'pipe_sgs_wallthk': Array,
        'pipe_sgs_mdot_dsn': Array,
        'pipe_sgs_vel_dsn': Array,
        'pipe_sgs_T_dsn': Array,
        'pipe_sgs_P_dsn': Array,
        'mass_tank_cold': Array,
        'mass_tank_hot': Array,
        'm_dot_charge_field': Array,
        'm_dot_discharge_tank': Array,
        'T_tank_cold_fin': Array,
        'T_tank_hot_fin': Array,
        'Ts_hot': Array,
        'Ts_cold': Array,
        'T_tank_hot_in': Array,
        'T_tank_cold_in': Array,
        'vol_tank_cold_fin': Array,
        'vol_tank_hot_fin': Array,
        'vol_tank_total': Array,
        'q_to_tes': Array,
        'tank_losses': Array,
        'eta': Array,
        'W_net': Array,
        'W_cycle_gross': Array,
        'm_dot_pb': Array,
        'T_pb_in': Array,
        'T_pb_out': Array,
        'm_dot_makeup': Array,
        'q_pb': Array,
        'Q_aux_backup': Array,
        'm_dot_aux': Array,
        'Fuel_usage': Array,
        'W_dot_pump': Array,
        'htf_pump_power': Array,
        'SCA_par_tot': Array,
        'bop_par': Array,
        'fixed_par': Array,
        'aux_par': Array,
        'W_cool_par': Array,
        'Q_par_sf_fp': Array,
        'Q_par_tes_fp': Array,
        'monthly_energy': Array,
        'monthly_W_cycle_gross': Array,
        'monthly_q_inc_sf_tot': Array,
        'monthly_q_abs_tot': Array,
        'monthly_q_avail': Array,
        'monthly_Fuel_usage': Array,
        'monthly_q_dump': Array,
        'monthly_m_dot_makeup': Array,
        'monthly_q_pb': Array,
        'monthly_q_to_tes': Array,
        'annual_energy': float,
        'annual_W_cycle_gross': float,
        'annual_q_inc_sf_tot': float,
        'annual_q_abs_tot': float,
        'annual_q_avail': float,
        'annual_q_aux': float,
        'annual_q_dump': float,
        'annual_q_pb': float,
        'annual_q_to_tes': float,
        'conversion_factor': float,
        'capacity_factor': float,
        'kwh_per_kw': float,
        'system_heat_rate': float,
        'annual_fuel_usage': float,
        'annual_total_water_use': float,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix,
        'gen': Array
}, total=False)

class Data(ssc.DataDict):
    file_name: str = INPUT(label='Local weather file with path', units='none', type='STRING', group='Weather', required='*', constraints='LOCAL_FILE')
    track_mode: float = INPUT(label='Tracking mode', units='none', type='NUMBER', group='Weather', required='*')
    tilt: float = INPUT(label='Tilt angle of surface/axis', units='none', type='NUMBER', group='Weather', required='*')
    azimuth: float = INPUT(label='Azimuth angle of surface/axis', units='none', type='NUMBER', group='Weather', required='*')
    system_capacity: float = INPUT(label='Nameplate capacity', units='kW', type='NUMBER', group='trough', required='*')
    nSCA: float = INPUT(label='Number of SCAs in a loop', units='none', type='NUMBER', group='solar_field', required='*')
    nHCEt: float = INPUT(label='Number of HCE types', units='none', type='NUMBER', group='solar_field', required='*')
    nColt: float = INPUT(label='Number of collector types', units='none', type='NUMBER', group='solar_field', required='*', meta='constant=4')
    nHCEVar: float = INPUT(label='Number of HCE variants per type', units='none', type='NUMBER', group='solar_field', required='*')
    nLoops: float = INPUT(label='Number of loops in the field', units='none', type='NUMBER', group='solar_field', required='*')
    eta_pump: float = INPUT(label='HTF pump efficiency', units='none', type='NUMBER', group='solar_field', required='*')
    HDR_rough: float = INPUT(label='Header pipe roughness', units='m', type='NUMBER', group='solar_field', required='*')
    theta_stow: float = INPUT(label='Stow angle', units='deg', type='NUMBER', group='solar_field', required='*')
    theta_dep: float = INPUT(label='Deploy angle', units='deg', type='NUMBER', group='solar_field', required='*')
    Row_Distance: float = INPUT(label='Spacing between rows (centerline to centerline)', units='m', type='NUMBER', group='solar_field', required='*')
    FieldConfig: float = INPUT(label='Number of subfield headers', units='none', type='NUMBER', group='solar_field', required='*')
    T_startup: float = INPUT(label='Required temperature of the system before the power block can be switched on', units='C', type='NUMBER', group='solar_field', required='*')
    P_ref: float = INPUT(label='Rated plant capacity', units='MWe', type='NUMBER', group='solar_field', required='*')
    m_dot_htfmin: float = INPUT(label='Minimum loop HTF flow rate', units='kg/s', type='NUMBER', group='solar_field', required='*')
    m_dot_htfmax: float = INPUT(label='Maximum loop HTF flow rate', units='kg/s', type='NUMBER', group='solar_field', required='*')
    T_loop_in_des: float = INPUT(label='Design loop inlet temperature', units='C', type='NUMBER', group='solar_field', required='*')
    T_loop_out: float = INPUT(label='Target loop outlet temperature', units='C', type='NUMBER', group='solar_field', required='*')
    Fluid: float = INPUT(label='Field HTF fluid ID number', units='none', type='NUMBER', group='solar_field', required='*')
    T_fp: float = INPUT(label='Freeze protection temperature (heat trace activation temperature)', units='C', type='NUMBER', group='solar_field', required='*')
    I_bn_des: float = INPUT(label='Solar irradiation at design', units='W/m2', type='NUMBER', group='solar_field', required='*')
    calc_design_pipe_vals: float = INPUT(label='Calculate temps and pressures at design conditions for runners and headers', units='none', type='NUMBER', group='solar_field', required='*')
    V_hdr_cold_max: float = INPUT(label='Maximum HTF velocity in the cold headers at design', units='m/s', type='NUMBER', group='solar_field', required='*')
    V_hdr_cold_min: float = INPUT(label='Minimum HTF velocity in the cold headers at design', units='m/s', type='NUMBER', group='solar_field', required='*')
    V_hdr_hot_max: float = INPUT(label='Maximum HTF velocity in the hot headers at design', units='m/s', type='NUMBER', group='solar_field', required='*')
    V_hdr_hot_min: float = INPUT(label='Minimum HTF velocity in the hot headers at design', units='m/s', type='NUMBER', group='solar_field', required='*')
    N_max_hdr_diams: float = INPUT(label='Maximum number of diameters in each of the hot and cold headers', units='none', type='NUMBER', group='solar_field', required='*')
    L_rnr_pb: float = INPUT(label='Length of runner pipe in power block', units='m', type='NUMBER', group='solar_field', required='*')
    L_rnr_per_xpan: float = INPUT(label='Threshold length of straight runner pipe without an expansion loop', units='m', type='NUMBER', group='solar_field', required='*')
    L_xpan_hdr: float = INPUT(label='Compined perpendicular lengths of each header expansion loop', units='m', type='NUMBER', group='solar_field', required='*')
    L_xpan_rnr: float = INPUT(label='Compined perpendicular lengths of each runner expansion loop', units='m', type='NUMBER', group='solar_field', required='*')
    Min_rnr_xpans: float = INPUT(label='Minimum number of expansion loops per single-diameter runner section', units='none', type='NUMBER', group='solar_field', required='*')
    northsouth_field_sep: float = INPUT(label='North/south separation between subfields. 0 = SCAs are touching', units='m', type='NUMBER', group='solar_field', required='*')
    N_hdr_per_xpan: float = INPUT(label='Number of collector loops per expansion loop', units='none', type='NUMBER', group='solar_field', required='*')
    offset_xpan_hdr: float = INPUT(label='Location of first header expansion loop. 1 = after first collector loop', units='none', type='NUMBER', group='solar_field', required='*')
    Pipe_hl_coef: float = INPUT(label='Loss coefficient from the header, runner pipe, and non-HCE piping', units='W/m2-K', type='NUMBER', group='solar_field', required='*')
    SCA_drives_elec: float = INPUT(label='Tracking power, in Watts per SCA drive', units='W/SCA', type='NUMBER', group='solar_field', required='*')
    fthrok: float = INPUT(label='Flag to allow partial defocusing of the collectors', type='NUMBER', group='solar_field', required='*', constraints='INTEGER')
    fthrctrl: float = INPUT(label='Defocusing strategy', units='none', type='NUMBER', group='solar_field', required='*')
    water_usage_per_wash: float = INPUT(label='Water usage per wash', units='L/m2_aper', type='NUMBER', group='solar_field', required='*')
    washing_frequency: float = INPUT(label='Mirror washing frequency', units='none', type='NUMBER', group='solar_field', required='*')
    accept_mode: float = INPUT(label='Acceptance testing mode?', units='0/1', type='NUMBER', group='solar_field', required='*', meta='no/yes')
    accept_init: float = INPUT(label='In acceptance testing mode - require steady-state startup', units='none', type='NUMBER', group='solar_field', required='*')
    accept_loc: float = INPUT(label='In acceptance testing mode - temperature sensor location', units='1/2', type='NUMBER', group='solar_field', required='*', meta='hx/loop')
    solar_mult: float = INPUT(label='Solar multiple', units='none', type='NUMBER', group='solar_field', required='*')
    mc_bal_hot: float = INPUT(label='Heat capacity of the balance of plant on the hot side', units='kWht/K-MWt', type='NUMBER', group='solar_field', required='*', meta='none')
    mc_bal_cold: float = INPUT(label='Heat capacity of the balance of plant on the cold side', units='kWht/K-MWt', type='NUMBER', group='solar_field', required='*')
    mc_bal_sca: float = INPUT(label='Non-HTF heat capacity associated with each SCA - per meter basis', units='Wht/K-m', type='NUMBER', group='solar_field', required='*')
    W_aperture: Array = INPUT(label='The collector aperture width (Total structural area used for shadowing)', units='m', type='ARRAY', group='solar_field', required='*')
    A_aperture: Array = INPUT(label='Reflective aperture area of the collector', units='m2', type='ARRAY', group='solar_field', required='*')
    TrackingError: Array = INPUT(label='User-defined tracking error derate', units='none', type='ARRAY', group='solar_field', required='*')
    GeomEffects: Array = INPUT(label='User-defined geometry effects derate', units='none', type='ARRAY', group='solar_field', required='*')
    Rho_mirror_clean: Array = INPUT(label='User-defined clean mirror reflectivity', units='none', type='ARRAY', group='solar_field', required='*')
    Dirt_mirror: Array = INPUT(label='User-defined dirt on mirror derate', units='none', type='ARRAY', group='solar_field', required='*')
    Error: Array = INPUT(label='User-defined general optical error derate ', units='none', type='ARRAY', group='solar_field', required='*')
    Ave_Focal_Length: Array = INPUT(label='Average focal length of the collector ', units='m', type='ARRAY', group='solar_field', required='*')
    L_SCA: Array = INPUT(label='Length of the SCA ', units='m', type='ARRAY', group='solar_field', required='*')
    L_aperture: Array = INPUT(label='Length of a single mirror/HCE unit', units='m', type='ARRAY', group='solar_field', required='*')
    ColperSCA: Array = INPUT(label='Number of individual collector sections in an SCA ', units='none', type='ARRAY', group='solar_field', required='*')
    Distance_SCA: Array = INPUT(label="Piping distance between SCA's in the field", units='m', type='ARRAY', group='solar_field', required='*')
    IAM_matrix: Matrix = INPUT(label='IAM coefficients, matrix for 4 collectors', units='none', type='MATRIX', group='solar_field', required='*')
    HCE_FieldFrac: Matrix = INPUT(label='Fraction of the field occupied by this HCE type ', units='none', type='MATRIX', group='solar_field', required='*')
    D_2: Matrix = INPUT(label='Inner absorber tube diameter', units='m', type='MATRIX', group='solar_field', required='*')
    D_3: Matrix = INPUT(label='Outer absorber tube diameter', units='m', type='MATRIX', group='solar_field', required='*')
    D_4: Matrix = INPUT(label='Inner glass envelope diameter ', units='m', type='MATRIX', group='solar_field', required='*')
    D_5: Matrix = INPUT(label='Outer glass envelope diameter ', units='m', type='MATRIX', group='solar_field', required='*')
    D_p: Matrix = INPUT(label='Diameter of the absorber flow plug (optional) ', units='m', type='MATRIX', group='solar_field', required='*')
    Flow_type: Matrix = INPUT(label='Flow type through the absorber', units='none', type='MATRIX', group='solar_field', required='*')
    Rough: Matrix = INPUT(label='Relative roughness of the internal HCE surface ', units='-', type='MATRIX', group='solar_field', required='*')
    alpha_env: Matrix = INPUT(label='Envelope absorptance ', units='none', type='MATRIX', group='solar_field', required='*')
    epsilon_3_11: Matrix = INPUT(label='Absorber emittance for receiver type 1 variation 1', units='none', type='MATRIX', group='solar_field', required='*')
    epsilon_3_12: Matrix = INPUT(label='Absorber emittance for receiver type 1 variation 2', units='none', type='MATRIX', group='solar_field', required='*')
    epsilon_3_13: Matrix = INPUT(label='Absorber emittance for receiver type 1 variation 3', units='none', type='MATRIX', group='solar_field', required='*')
    epsilon_3_14: Matrix = INPUT(label='Absorber emittance for receiver type 1 variation 4', units='none', type='MATRIX', group='solar_field', required='*')
    epsilon_3_21: Matrix = INPUT(label='Absorber emittance for receiver type 2 variation 1', units='none', type='MATRIX', group='solar_field', required='*')
    epsilon_3_22: Matrix = INPUT(label='Absorber emittance for receiver type 2 variation 2', units='none', type='MATRIX', group='solar_field', required='*')
    epsilon_3_23: Matrix = INPUT(label='Absorber emittance for receiver type 2 variation 3', units='none', type='MATRIX', group='solar_field', required='*')
    epsilon_3_24: Matrix = INPUT(label='Absorber emittance for receiver type 2 variation 4', units='none', type='MATRIX', group='solar_field', required='*')
    epsilon_3_31: Matrix = INPUT(label='Absorber emittance for receiver type 3 variation 1', units='none', type='MATRIX', group='solar_field', required='*')
    epsilon_3_32: Matrix = INPUT(label='Absorber emittance for receiver type 3 variation 2', units='none', type='MATRIX', group='solar_field', required='*')
    epsilon_3_33: Matrix = INPUT(label='Absorber emittance for receiver type 3 variation 3', units='none', type='MATRIX', group='solar_field', required='*')
    epsilon_3_34: Matrix = INPUT(label='Absorber emittance for receiver type 3 variation 4', units='none', type='MATRIX', group='solar_field', required='*')
    epsilon_3_41: Matrix = INPUT(label='Absorber emittance for receiver type 4 variation 1', units='none', type='MATRIX', group='solar_field', required='*')
    epsilon_3_42: Matrix = INPUT(label='Absorber emittance for receiver type 4 variation 2', units='none', type='MATRIX', group='solar_field', required='*')
    epsilon_3_43: Matrix = INPUT(label='Absorber emittance for receiver type 4 variation 3', units='none', type='MATRIX', group='solar_field', required='*')
    epsilon_3_44: Matrix = INPUT(label='Absorber emittance for receiver type 4 variation 4', units='none', type='MATRIX', group='solar_field', required='*')
    alpha_abs: Matrix = INPUT(label='Absorber absorptance ', units='none', type='MATRIX', group='solar_field', required='*')
    Tau_envelope: Matrix = INPUT(label='Envelope transmittance', units='none', type='MATRIX', group='solar_field', required='*')
    EPSILON_4: Matrix = INPUT(label='Inner glass envelope emissivities (Pyrex) ', units='none', type='MATRIX', group='solar_field', required='*')
    EPSILON_5: Matrix = INPUT(label='Outer glass envelope emissivities (Pyrex) ', units='none', type='MATRIX', group='solar_field', required='*')
    GlazingIntactIn: Matrix = INPUT(label='Glazing intact (broken glass) flag {1=true, else=false}', units='none', type='MATRIX', group='solar_field', required='*')
    P_a: Matrix = INPUT(label='Annulus gas pressure', units='torr', type='MATRIX', group='solar_field', required='*')
    AnnulusGas: Matrix = INPUT(label='Annulus gas type (1=air, 26=Ar, 27=H2)', units='none', type='MATRIX', group='solar_field', required='*')
    AbsorberMaterial: Matrix = INPUT(label='Absorber material type', units='none', type='MATRIX', group='solar_field', required='*')
    Shadowing: Matrix = INPUT(label='Receiver bellows shadowing loss factor', units='none', type='MATRIX', group='solar_field', required='*')
    Dirt_HCE: Matrix = INPUT(label='Loss due to dirt on the receiver envelope', units='none', type='MATRIX', group='solar_field', required='*')
    Design_loss: Matrix = INPUT(label='Receiver heat loss at design', units='W/m', type='MATRIX', group='solar_field', required='*')
    SCAInfoArray: Matrix = INPUT(label='Receiver (,1) and collector (,2) type for each assembly in loop', units='none', type='MATRIX', group='solar_field', required='*')
    SCADefocusArray: Array = INPUT(label='Collector defocus order', units='none', type='ARRAY', group='solar_field', required='*')
    K_cpnt: Matrix = INPUT(label='Interconnect component minor loss coefficients, row=intc, col=cpnt', units='none', type='MATRIX', group='solar_field', required='*')
    D_cpnt: Matrix = INPUT(label='Interconnect component diameters, row=intc, col=cpnt', units='none', type='MATRIX', group='solar_field', required='*')
    L_cpnt: Matrix = INPUT(label='Interconnect component lengths, row=intc, col=cpnt', units='none', type='MATRIX', group='solar_field', required='*')
    Type_cpnt: Matrix = INPUT(label='Interconnect component type, row=intc, col=cpnt', units='none', type='MATRIX', group='solar_field', required='*')
    custom_sf_pipe_sizes: float = INPUT(label='Use custom solar field pipe diams, wallthks, and lengths', units='none', type='NUMBER', group='solar_field', required='*')
    sf_rnr_diams: Array = INPUT(label='Custom runner diameters', units='m', type='ARRAY', group='solar_field', required='*')
    sf_rnr_wallthicks: Array = INPUT(label='Custom runner wall thicknesses', units='m', type='ARRAY', group='solar_field', required='*')
    sf_rnr_lengths: Array = INPUT(label='Custom runner lengths', units='m', type='ARRAY', group='solar_field', required='*')
    sf_hdr_diams: Array = INPUT(label='Custom header diameters', units='m', type='ARRAY', group='solar_field', required='*')
    sf_hdr_wallthicks: Array = INPUT(label='Custom header wall thicknesses', units='m', type='ARRAY', group='solar_field', required='*')
    sf_hdr_lengths: Array = INPUT(label='Custom header lengths', units='m', type='ARRAY', group='solar_field', required='*')
    field_fl_props: Matrix = INPUT(label='User defined field fluid property data', units='-', type='MATRIX', group='controller', required='*')
    store_fl_props: Matrix = INPUT(label='User defined storage fluid property data', units='-', type='MATRIX', group='controller', required='*')
    store_fluid: float = INPUT(label='Material number for storage fluid', units='-', type='NUMBER', group='controller', required='*')
    tshours: float = INPUT(label='Equivalent full-load thermal storage hours', units='hr', type='NUMBER', group='controller', required='*')
    is_hx: float = INPUT(label='Heat exchanger (HX) exists (1=yes, 0=no)', units='-', type='NUMBER', group='controller', required='*')
    dt_hot: float = INPUT(label='Hot side HX approach temp', units='C', type='NUMBER', group='controller', required='*')
    dt_cold: float = INPUT(label='Cold side HX approach temp', units='C', type='NUMBER', group='controller', required='*')
    hx_config: float = INPUT(label='HX configuration', units='-', type='NUMBER', group='controller', required='*')
    q_max_aux: float = INPUT(label='Max heat rate of auxiliary heater', units='MWt', type='NUMBER', group='controller', required='*')
    T_set_aux: float = INPUT(label='Aux heater outlet temp set point', units='C', type='NUMBER', group='controller', required='*')
    V_tank_hot_ini: float = INPUT(label='Initial hot tank fluid volume', units='m3', type='NUMBER', group='controller', required='*')
    T_tank_cold_ini: float = INPUT(label='Initial cold tank fluid tmeperature', units='C', type='NUMBER', group='controller', required='*')
    vol_tank: float = INPUT(label='Total tank volume, including unusable HTF at bottom', units='m3', type='NUMBER', group='controller', required='*')
    h_tank: float = INPUT(label='Total height of tank (height of HTF when tank is full', units='m', type='NUMBER', group='controller', required='*')
    h_tank_min: float = INPUT(label='Minimum allowable HTF height in storage tank', units='m', type='NUMBER', group='controller', required='*')
    u_tank: float = INPUT(label='Loss coefficient from the tank', units='W/m2-K', type='NUMBER', group='controller', required='*')
    tank_pairs: float = INPUT(label='Number of equivalent tank pairs', units='-', type='NUMBER', group='controller', required='*', constraints='INTEGER')
    cold_tank_Thtr: float = INPUT(label='Minimum allowable cold tank HTF temp', units='C', type='NUMBER', group='controller', required='*')
    hot_tank_Thtr: float = INPUT(label='Minimum allowable hot tank HTF temp', units='C', type='NUMBER', group='controller', required='*')
    tank_max_heat: float = INPUT(label='Rated heater capacity for tank heating', units='MW', type='NUMBER', group='controller', required='*')
    tanks_in_parallel: float = INPUT(label='Tanks are in parallel, not in series, with solar field', units='-', type='NUMBER', group='controller', required='*')
    has_hot_tank_bypass: float = INPUT(label='Bypass valve connects field outlet to cold tank', units='-', type='NUMBER', group='controller', required='*')
    T_tank_hot_inlet_min: float = INPUT(label='Minimum hot tank htf inlet temperature', units='C', type='NUMBER', group='controller', required='*')
    q_pb_design: float = INPUT(label='Design heat input to power block', units='MWt', type='NUMBER', group='controller', required='*')
    W_pb_design: float = INPUT(label='Rated plant capacity', units='MWe', type='NUMBER', group='controller', required='*')
    cycle_max_frac: float = INPUT(label='Maximum turbine over design operation fraction', units='-', type='NUMBER', group='controller', required='*')
    cycle_cutoff_frac: float = INPUT(label='Minimum turbine operation fraction before shutdown', units='-', type='NUMBER', group='controller', required='*')
    pb_pump_coef: float = INPUT(label='Pumping power to move 1kg of HTF through PB loop', units='kW/(kg/s)', type='NUMBER', group='controller', required='*')
    tes_pump_coef: float = INPUT(label='Pumping power to move 1kg of HTF through tes loop', units='kW/(kg/s)', type='NUMBER', group='controller', required='*')
    V_tes_des: float = INPUT(label='Design-point velocity to size the TES pipe diameters', units='m/s', type='NUMBER', group='controller', required='*')
    custom_tes_p_loss: float = INPUT(label='TES pipe losses are based on custom lengths and coeffs', units='-', type='NUMBER', group='controller', required='*')
    k_tes_loss_coeffs: Array = INPUT(label='Minor loss coeffs for the coll, gen, and bypass loops', units='-', type='ARRAY', group='controller', required='*')
    custom_sgs_pipe_sizes: float = INPUT(label='Use custom SGS pipe diams, wallthks, and lengths', units='-', type='NUMBER', group='controller', required='*')
    sgs_diams: Array = INPUT(label='Custom SGS diameters', units='m', type='ARRAY', group='controller', required='*')
    sgs_wallthicks: Array = INPUT(label='Custom SGS wall thicknesses', units='m', type='ARRAY', group='controller', required='*')
    sgs_lengths: Array = INPUT(label='Custom SGS lengths', units='m', type='ARRAY', group='controller', required='*')
    DP_SGS: float = INPUT(label='Pressure drop within the steam generator', units='bar', type='NUMBER', group='controller', required='*')
    pb_fixed_par: float = INPUT(label='Fraction of rated gross power constantly consumed', units='-', type='NUMBER', group='controller', required='*')
    bop_array: Array = INPUT(label='Coefficients for balance of plant parasitics calcs', units='-', type='ARRAY', group='controller', required='*')
    aux_array: Array = INPUT(label='Coefficients for auxiliary heater parasitics calcs', units='-', type='ARRAY', group='controller', required='*')
    fossil_mode: float = INPUT(label='Fossil backup mode 1=Normal 2=Topping', units='-', type='NUMBER', group='controller', required='*', constraints='INTEGER')
    t_standby_reset: float = INPUT(label='Maximum allowable time for PB standby operation', units='hr', type='NUMBER', group='controller', required='*')
    sf_type: float = INPUT(label='Solar field type, 1 = trough, 2 = tower', units='-', type='NUMBER', group='controller', required='*')
    tes_type: float = INPUT(label='1=2-tank, 2=thermocline', units='-', type='NUMBER', group='controller', required='*')
    tslogic_a: Array = INPUT(label='Dispatch logic without solar', units='-', type='ARRAY', group='controller', required='*')
    tslogic_b: Array = INPUT(label='Dispatch logic with solar', units='-', type='ARRAY', group='controller', required='*')
    tslogic_c: Array = INPUT(label='Dispatch logic for turbine load fraction', units='-', type='ARRAY', group='controller', required='*')
    ffrac: Array = INPUT(label='Fossil dispatch logic', units='-', type='ARRAY', group='controller', required='*')
    tc_fill: float = INPUT(label='Thermocline fill material', units='-', type='NUMBER', group='controller', required='*')
    tc_void: float = INPUT(label='Thermocline void fraction', units='-', type='NUMBER', group='controller', required='*')
    t_dis_out_min: float = INPUT(label='Min allowable hot side outlet temp during discharge', units='C', type='NUMBER', group='controller', required='*')
    t_ch_out_max: float = INPUT(label='Max allowable cold side outlet temp during charge', units='C', type='NUMBER', group='controller', required='*')
    nodes: float = INPUT(label='Nodes modeled in the flow path', units='-', type='NUMBER', group='controller', required='*')
    f_tc_cold: float = INPUT(label='0=entire tank is hot, 1=entire tank is cold', units='-', type='NUMBER', group='controller', required='*')
    weekday_schedule: Matrix = INPUT(label='Dispatch 12mx24h schedule for week days', type='MATRIX', group='tou_translator', required='*')
    weekend_schedule: Matrix = INPUT(label='Dispatch 12mx24h schedule for weekends', type='MATRIX', group='tou_translator', required='*')
    pc_config: float = INPUT(label='0: Steam Rankine (224), 1: user defined', units='-', type='NUMBER', group='powerblock', required='?=0', constraints='INTEGER')
    eta_ref: float = INPUT(label='Reference conversion efficiency at design condition', units='none', type='NUMBER', group='powerblock', required='*')
    startup_time: float = INPUT(label='Time needed for power block startup', units='hr', type='NUMBER', group='powerblock', required='*')
    startup_frac: float = INPUT(label='Fraction of design thermal power needed for startup', units='none', type='NUMBER', group='powerblock', required='*')
    q_sby_frac: float = INPUT(label='Fraction of thermal power required for standby mode', units='none', type='NUMBER', group='powerblock', required='*')
    dT_cw_ref: float = INPUT(label='Reference condenser cooling water inlet/outlet T diff', units='C', type='NUMBER', group='powerblock', required='pc_config=0')
    T_amb_des: float = INPUT(label='Reference ambient temperature at design point', units='C', type='NUMBER', group='powerblock', required='pc_config=0')
    P_boil: float = INPUT(label='Boiler operating pressure', units='bar', type='NUMBER', group='powerblock', required='pc_config=0')
    CT: float = INPUT(label='Flag for using dry cooling or wet cooling system', units='none', type='NUMBER', group='powerblock', required='pc_config=0')
    T_approach: float = INPUT(label='Cooling tower approach temperature', units='C', type='NUMBER', group='powerblock', required='pc_config=0')
    T_ITD_des: float = INPUT(label='ITD at design for dry system', units='C', type='NUMBER', group='powerblock', required='pc_config=0')
    P_cond_ratio: float = INPUT(label='Condenser pressure ratio', units='none', type='NUMBER', group='powerblock', required='pc_config=0')
    pb_bd_frac: float = INPUT(label='Power block blowdown steam fraction ', units='none', type='NUMBER', group='powerblock', required='pc_config=0')
    P_cond_min: float = INPUT(label='Minimum condenser pressure', units='inHg', type='NUMBER', group='powerblock', required='pc_config=0')
    n_pl_inc: float = INPUT(label='Number of part-load increments for the heat rejection system', units='none', type='NUMBER', group='powerblock', required='pc_config=0')
    F_wc: Array = INPUT(label='Fraction indicating wet cooling use for hybrid system', units='none', type='ARRAY', group='powerblock', required='pc_config=0', meta='constant=[0,0,0,0,0,0,0,0,0]')
    tech_type: float = INPUT(label='Turbine inlet pressure control flag (sliding=user, fixed=trough)', units='1/2/3', type='NUMBER', group='powerblock', required='pc_config=0', meta='tower/trough/user')
    ud_T_amb_des: float = INPUT(label='Ambient temperature at user-defined power cycle design point', units='C', type='NUMBER', group='user_defined_PC', required='pc_config=1')
    ud_f_W_dot_cool_des: float = INPUT(label='Percent of user-defined power cycle design gross output consumed by cooling', units='%', type='NUMBER', group='user_defined_PC', required='pc_config=1')
    ud_m_dot_water_cool_des: float = INPUT(label='Mass flow rate of water required at user-defined power cycle design point', units='kg/s', type='NUMBER', group='user_defined_PC', required='pc_config=1')
    ud_T_htf_low: float = INPUT(label='Low level HTF inlet temperature for T_amb parametric', units='C', type='NUMBER', group='user_defined_PC', required='pc_config=1')
    ud_T_htf_high: float = INPUT(label='High level HTF inlet temperature for T_amb parametric', units='C', type='NUMBER', group='user_defined_PC', required='pc_config=1')
    ud_T_amb_low: float = INPUT(label='Low level ambient temperature for HTF mass flow rate parametric', units='C', type='NUMBER', group='user_defined_PC', required='pc_config=1')
    ud_T_amb_high: float = INPUT(label='High level ambient temperature for HTF mass flow rate parametric', units='C', type='NUMBER', group='user_defined_PC', required='pc_config=1')
    ud_m_dot_htf_low: float = INPUT(label='Low level normalized HTF mass flow rate for T_HTF parametric', units='-', type='NUMBER', group='user_defined_PC', required='pc_config=1')
    ud_m_dot_htf_high: float = INPUT(label='High level normalized HTF mass flow rate for T_HTF parametric', units='-', type='NUMBER', group='user_defined_PC', required='pc_config=1')
    ud_T_htf_ind_od: Matrix = INPUT(label='Off design table of user-defined power cycle performance formed from parametric on T_htf_hot [C]', type='MATRIX', group='user_defined_PC', required='?=[[0]]')
    ud_T_amb_ind_od: Matrix = INPUT(label='Off design table of user-defined power cycle performance formed from parametric on T_amb [C]', type='MATRIX', group='user_defined_PC', required='?=[[0]]')
    ud_m_dot_htf_ind_od: Matrix = INPUT(label='Off design table of user-defined power cycle performance formed from parametric on m_dot_htf [ND]', type='MATRIX', group='user_defined_PC', required='?=[[0]]')
    ud_ind_od: Matrix = INPUT(label='Off design user-defined power cycle performance as function of T_htf, m_dot_htf [ND], and T_amb', type='MATRIX', group='user_defined_PC', required='?=[[0]]')
    eta_lhv: float = INPUT(label='Fossil fuel lower heating value - Thermal power generated per unit fuel', units='MW/MMBTU', type='NUMBER', group='enet', required='*')
    eta_tes_htr: float = INPUT(label='Thermal storage tank heater efficiency (fp_mode=1 only)', units='none', type='NUMBER', group='enet', required='*')
    month: Final[Array] = OUTPUT(label='Resource Month', type='ARRAY', group='weather', required='*')
    hour: Final[Array] = OUTPUT(label='Resource Hour of Day', type='ARRAY', group='weather', required='*')
    solazi: Final[Array] = OUTPUT(label='Resource Solar Azimuth', units='deg', type='ARRAY', group='weather', required='*')
    solzen: Final[Array] = OUTPUT(label='Resource Solar Zenith', units='deg', type='ARRAY', group='weather', required='*')
    beam: Final[Array] = OUTPUT(label='Resource Beam normal irradiance', units='W/m2', type='ARRAY', group='weather', required='*')
    tdry: Final[Array] = OUTPUT(label='Resource Dry bulb temperature', units='C', type='ARRAY', group='weather', required='*')
    twet: Final[Array] = OUTPUT(label='Resource Wet bulb temperature', units='C', type='ARRAY', group='weather', required='*')
    wspd: Final[Array] = OUTPUT(label='Resource Wind Speed', units='m/s', type='ARRAY', group='weather', required='*')
    pres: Final[Array] = OUTPUT(label='Resource Pressure', units='mbar', type='ARRAY', group='weather', required='*')
    tou_value: Final[Array] = OUTPUT(label='Resource Time-of-use value', type='ARRAY', group='tou', required='*')
    recirculating: Final[Array] = OUTPUT(label='Field recirculating (bypass valve open)', units='-', type='ARRAY', group='Type250', required='*')
    pipe_header_diams: Final[Array] = OUTPUT(label='Field piping header diameters', units='m', type='ARRAY', group='Type250', required='*')
    pipe_header_wallthk: Final[Array] = OUTPUT(label='Field piping header wall thicknesses', units='m', type='ARRAY', group='Type250', required='*')
    pipe_header_lengths: Final[Array] = OUTPUT(label='Field piping header lengths', units='m', type='ARRAY', group='Type250', required='*')
    pipe_header_expansions: Final[Array] = OUTPUT(label='Number of field piping header expansions', units='-', type='ARRAY', group='Type250', required='*')
    pipe_header_mdot_dsn: Final[Array] = OUTPUT(label='Field piping header mass flow at design', units='kg/s', type='ARRAY', group='Type250', required='*')
    pipe_header_vel_dsn: Final[Array] = OUTPUT(label='Field piping header velocity at design', units='m/s', type='ARRAY', group='Type250', required='*')
    pipe_header_T_dsn: Final[Array] = OUTPUT(label='Field piping header temperature at design', units='C', type='ARRAY', group='Type250', required='*')
    pipe_header_P_dsn: Final[Array] = OUTPUT(label='Field piping header pressure at design', units='bar', type='ARRAY', group='Type250', required='*')
    pipe_runner_diams: Final[Array] = OUTPUT(label='Field piping runner diameters', units='m', type='ARRAY', group='Type250', required='*')
    pipe_runner_wallthk: Final[Array] = OUTPUT(label='Field piping runner wall thicknesses', units='m', type='ARRAY', group='Type250', required='*')
    pipe_runner_lengths: Final[Array] = OUTPUT(label='Field piping runner lengths', units='m', type='ARRAY', group='Type250', required='*')
    pipe_runner_expansions: Final[Array] = OUTPUT(label='Number of field piping runner expansions', units='-', type='ARRAY', group='Type250', required='*')
    pipe_runner_mdot_dsn: Final[Array] = OUTPUT(label='Field piping runner mass flow at design', units='kg/s', type='ARRAY', group='Type250', required='*')
    pipe_runner_vel_dsn: Final[Array] = OUTPUT(label='Field piping runner velocity at design', units='m/s', type='ARRAY', group='Type250', required='*')
    pipe_runner_T_dsn: Final[Array] = OUTPUT(label='Field piping runner temperature at design', units='C', type='ARRAY', group='Type250', required='*')
    pipe_runner_P_dsn: Final[Array] = OUTPUT(label='Field piping runner pressure at design', units='bar', type='ARRAY', group='Type250', required='*')
    pipe_loop_T_dsn: Final[Array] = OUTPUT(label='Field piping loop temperature at design', units='C', type='ARRAY', group='Type250', required='*')
    pipe_loop_P_dsn: Final[Array] = OUTPUT(label='Field piping loop pressure at design', units='bar', type='ARRAY', group='Type250', required='*')
    Theta_ave: Final[Array] = OUTPUT(label='Field collector solar incidence angle', units='deg', type='ARRAY', group='Type250', required='*')
    CosTh_ave: Final[Array] = OUTPUT(label='Field collector cosine efficiency', type='ARRAY', group='Type250', required='*')
    IAM_ave: Final[Array] = OUTPUT(label='Field collector incidence angle modifier', type='ARRAY', group='Type250', required='*')
    RowShadow_ave: Final[Array] = OUTPUT(label='Field collector row shadowing loss', type='ARRAY', group='Type250', required='*')
    EndLoss_ave: Final[Array] = OUTPUT(label='Field collector optical end loss', type='ARRAY', group='Type250', required='*')
    dni_costh: Final[Array] = OUTPUT(label='Field collector DNI-cosine product', units='W/m2', type='ARRAY', group='Type250', required='*')
    SCAs_def: Final[Array] = OUTPUT(label="Field collector fraction of focused SCA's", type='ARRAY', group='Type250', required='*')
    EqOpteff: Final[Array] = OUTPUT(label='Field collector optical efficiency', type='ARRAY', group='Type250', required='*')
    q_inc_sf_tot: Final[Array] = OUTPUT(label='Field thermal power incident', units='MWt', type='ARRAY', group='Type250', required='*')
    qinc_costh: Final[Array] = OUTPUT(label='Field thermal power incident after cosine', units='MWt', type='ARRAY', group='Type250', required='*')
    q_abs_tot: Final[Array] = OUTPUT(label='Field thermal power absorbed', units='MWt', type='ARRAY', group='Type250', required='*')
    q_dump: Final[Array] = OUTPUT(label='Field thermal power dumped', units='MWt', type='ARRAY', group='Type250', required='*')
    q_loss_tot: Final[Array] = OUTPUT(label='Field thermal power receiver loss', units='MWt', type='ARRAY', group='Type250', required='*')
    Pipe_hl: Final[Array] = OUTPUT(label='Field thermal power header pipe losses', units='MWt', type='ARRAY', group='Type250', required='*')
    q_avail: Final[Array] = OUTPUT(label='Field thermal power produced', units='MWt', type='ARRAY', group='Type250', required='*')
    q_loss_spec_tot: Final[Array] = OUTPUT(label='Field thermal power avg. receiver loss', units='W/m', type='ARRAY', group='Type250', required='*')
    E_bal_startup: Final[Array] = OUTPUT(label='Field HTF energy inertial (consumed)', units='MWht', type='ARRAY', group='Type250', required='*')
    m_dot_avail: Final[Array] = OUTPUT(label='Field HTF mass flow rate total', units='kg/hr', type='ARRAY', group='Type250', required='*')
    m_dot_htf2: Final[Array] = OUTPUT(label='Field HTF mass flow rate loop', units='kg/s', type='ARRAY', group='Type250', required='*')
    DP_tot: Final[Array] = OUTPUT(label='Field HTF pressure drop total', units='bar', type='ARRAY', group='Type250', required='*')
    T_sys_c: Final[Array] = OUTPUT(label='Field HTF temperature cold header inlet', units='C', type='ARRAY', group='Type250', required='*')
    T_sys_h: Final[Array] = OUTPUT(label='Field HTF temperature hot header outlet', units='C', type='ARRAY', group='Type250', required='*')
    T_field_in: Final[Array] = OUTPUT(label='Field HTF temperature collector inlet', units='C', type='ARRAY', group='Type251', required='*')
    pipe_sgs_diams: Final[Array] = OUTPUT(label='Pipe diameters in SGS', units='m', type='ARRAY', group='Type251', required='*')
    pipe_sgs_wallthk: Final[Array] = OUTPUT(label='Pipe wall thickness in SGS', units='m', type='ARRAY', group='Type251', required='*')
    pipe_sgs_mdot_dsn: Final[Array] = OUTPUT(label='Mass flow SGS pipes at design conditions', units='kg/s', type='ARRAY', group='Type251', required='*')
    pipe_sgs_vel_dsn: Final[Array] = OUTPUT(label='Velocity in SGS pipes at design conditions', units='m/s', type='ARRAY', group='Type251', required='*')
    pipe_sgs_T_dsn: Final[Array] = OUTPUT(label='Temperature in SGS pipes at design conditions', units='C', type='ARRAY', group='Type251', required='*')
    pipe_sgs_P_dsn: Final[Array] = OUTPUT(label='Pressure in SGS pipes at design conditions', units='bar', type='ARRAY', group='Type251', required='*')
    mass_tank_cold: Final[Array] = OUTPUT(label='TES HTF mass in cold tank', units='kg', type='ARRAY', group='Type251', required='*')
    mass_tank_hot: Final[Array] = OUTPUT(label='TES HTF mass in hot tank', units='kg', type='ARRAY', group='Type251', required='*')
    m_dot_charge_field: Final[Array] = OUTPUT(label='TES HTF mass flow rate - field side of HX', units='kg/hr', type='ARRAY', group='Type250', required='*')
    m_dot_discharge_tank: Final[Array] = OUTPUT(label='TES HTF mass flow rate - storage side of HX', units='kg/hr', type='ARRAY', group='Type250', required='*')
    T_tank_cold_fin: Final[Array] = OUTPUT(label='TES HTF temperature in cold tank', units='C', type='ARRAY', group='Type251', required='*')
    T_tank_hot_fin: Final[Array] = OUTPUT(label='TES HTF temperature in hot tank', units='C', type='ARRAY', group='Type251', required='*')
    Ts_hot: Final[Array] = OUTPUT(label='TES HTF temperature HX field side hot', units='C', type='ARRAY', group='Type251', required='*')
    Ts_cold: Final[Array] = OUTPUT(label='TES HTF temperature HX field side cold', units='C', type='ARRAY', group='Type251', required='*')
    T_tank_hot_in: Final[Array] = OUTPUT(label='TES HTF temperature hot tank inlet', units='C', type='ARRAY', group='Type251', required='*')
    T_tank_cold_in: Final[Array] = OUTPUT(label='TES HTF temperature cold tank inlet', units='C', type='ARRAY', group='Type251', required='*')
    vol_tank_cold_fin: Final[Array] = OUTPUT(label='TES HTF volume in cold tank', units='m3', type='ARRAY', group='Type251', required='*')
    vol_tank_hot_fin: Final[Array] = OUTPUT(label='TES HTF volume in hot tank', units='m3', type='ARRAY', group='Type251', required='*')
    vol_tank_total: Final[Array] = OUTPUT(label='TES HTF volume total', units='m3', type='ARRAY', group='Type251', required='*')
    q_to_tes: Final[Array] = OUTPUT(label='TES thermal energy into storage', units='MWt', type='ARRAY', group='Type251', required='*')
    tank_losses: Final[Array] = OUTPUT(label='TES thermal losses from tank(s)', units='MWt', type='ARRAY', group='Type251', required='*')
    eta: Final[Array] = OUTPUT(label='Cycle efficiency (gross)', type='ARRAY', group='Type224', required='*')
    W_net: Final[Array] = OUTPUT(label='Cycle electrical power output (net)', units='MWe', type='ARRAY', group='Net_E_Calc', required='*')
    W_cycle_gross: Final[Array] = OUTPUT(label='Cycle electrical power output (gross)', units='MWe', type='ARRAY', group='Net_E_Calc', required='*')
    m_dot_pb: Final[Array] = OUTPUT(label='Cycle HTF mass flow rate', units='kg/hr', type='ARRAY', group='Type250', required='*')
    T_pb_in: Final[Array] = OUTPUT(label='Cycle HTF temperature in (hot)', units='C', type='ARRAY', group='Type251', required='*')
    T_pb_out: Final[Array] = OUTPUT(label='Cycle HTF temperature out (cold)', units='C', type='ARRAY', group='Type251', required='*')
    m_dot_makeup: Final[Array] = OUTPUT(label='Cycle cooling water mass flow rate - makeup', units='kg/hr', type='ARRAY', group='Type250', required='*')
    q_pb: Final[Array] = OUTPUT(label='Cycle thermal power input', units='MWt', type='ARRAY', group='Type251', required='*')
    Q_aux_backup: Final[Array] = OUTPUT(label='Fossil thermal power produced', units='MWt', type='ARRAY', group='SumCalc', required='*')
    m_dot_aux: Final[Array] = OUTPUT(label='Fossil HTF mass flow rate', units='kg/hr', type='ARRAY', group='Type250', required='*')
    Fuel_usage: Final[Array] = OUTPUT(label='Fossil fuel usage (all subsystems)', units='MMBTU', type='ARRAY', group='SumCalc', required='*')
    W_dot_pump: Final[Array] = OUTPUT(label='Parasitic power solar field HTF pump', units='MWe', type='ARRAY', group='Type250', required='*')
    htf_pump_power: Final[Array] = OUTPUT(label='Parasitic power TES and Cycle HTF pump', units='MWe', type='ARRAY', group='Type251', required='*')
    SCA_par_tot: Final[Array] = OUTPUT(label='Parasitic power field collector drives', units='MWe', type='ARRAY', group='Type250', required='*')
    bop_par: Final[Array] = OUTPUT(label='Parasitic power generation-dependent load', units='MWe', type='ARRAY', group='Type251', required='*')
    fixed_par: Final[Array] = OUTPUT(label='Parasitic power fixed load', units='MWe', type='ARRAY', group='Type251', required='*')
    aux_par: Final[Array] = OUTPUT(label='Parasitic power auxiliary heater operation', units='MWe', type='ARRAY', group='Type251', required='*')
    W_cool_par: Final[Array] = OUTPUT(label='Parasitic power condenser operation', units='MWe', type='ARRAY', group='Type224', required='*')
    Q_par_sf_fp: Final[Array] = OUTPUT(label='Parasitic thermal field freeze protection', units='MWt', type='ARRAY', group='SumCalc', required='*')
    Q_par_tes_fp: Final[Array] = OUTPUT(label='Parasitic thermal TES freeze protection', units='MWt', type='ARRAY', group='SumCalc', required='*')
    monthly_energy: Final[Array] = OUTPUT(label='Monthly Energy', units='kWh', type='ARRAY', group='Net_E_Calc', required='*', constraints='LENGTH=12')
    monthly_W_cycle_gross: Final[Array] = OUTPUT(label='Electrical source - Power cycle gross output', units='MWhe', type='ARRAY', group='Net_E_Calc', required='*', constraints='LENGTH=12')
    monthly_q_inc_sf_tot: Final[Array] = OUTPUT(label='Total power incident on the field', units='MWht', type='ARRAY', group='Type250', required='*', constraints='LENGTH=12')
    monthly_q_abs_tot: Final[Array] = OUTPUT(label='Total absorbed energy', units='MWht', type='ARRAY', group='Type250', required='*', constraints='LENGTH=12')
    monthly_q_avail: Final[Array] = OUTPUT(label='Thermal power produced by the field', units='MWht', type='ARRAY', group='Type250', required='*', constraints='LENGTH=12')
    monthly_Fuel_usage: Final[Array] = OUTPUT(label='Total fossil fuel usage by all plant subsystems', units='MMBTU', type='ARRAY', group='SumCalc', required='*', constraints='LENGTH=12')
    monthly_q_dump: Final[Array] = OUTPUT(label='Dumped thermal energy', units='MWht', type='ARRAY', group='Type250', required='*', constraints='LENGTH=12')
    monthly_m_dot_makeup: Final[Array] = OUTPUT(label='Cooling water makeup flow rate', units='kg/hr', type='ARRAY', group='Type250', required='*', constraints='LENGTH=12')
    monthly_q_pb: Final[Array] = OUTPUT(label='Thermal energy to the power block', units='MWht', type='ARRAY', group='Type251', required='*', constraints='LENGTH=12')
    monthly_q_to_tes: Final[Array] = OUTPUT(label='Thermal energy into storage', units='MWht', type='ARRAY', group='Type251', required='*', constraints='LENGTH=12')
    annual_energy: Final[float] = OUTPUT(label='Annual Energy', units='kWh', type='NUMBER', group='Net_E_Calc', required='*')
    annual_W_cycle_gross: Final[float] = OUTPUT(label='Electrical source - Power cycle gross output', units='MWhe', type='NUMBER', group='Net_E_Calc', required='*')
    annual_q_inc_sf_tot: Final[float] = OUTPUT(label='Total power incident on the field', units='MWht', type='NUMBER', group='Type250', required='*')
    annual_q_abs_tot: Final[float] = OUTPUT(label='Total absorbed energy', units='MWht', type='NUMBER', group='Type250', required='*')
    annual_q_avail: Final[float] = OUTPUT(label='Thermal power produced by the field', units='MWht', type='NUMBER', group='Type250', required='*')
    annual_q_aux: Final[float] = OUTPUT(label='Total fossil fuel usage by all plant subsystems', units='MMBTU', type='NUMBER', group='SumCalc', required='*')
    annual_q_dump: Final[float] = OUTPUT(label='Dumped thermal energy', units='MWht', type='NUMBER', group='Type250', required='*')
    annual_q_pb: Final[float] = OUTPUT(label='Thermal energy to the power block', units='MWht', type='NUMBER', group='Type251', required='*')
    annual_q_to_tes: Final[float] = OUTPUT(label='Thermal energy into storage', units='MWht', type='NUMBER', group='Type251', required='*')
    conversion_factor: Final[float] = OUTPUT(label='Gross to Net Conversion Factor', units='%', type='NUMBER', group='Calculated', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', required='*')
    kwh_per_kw: Final[float] = OUTPUT(label='First year kWh/kW', units='kWh/kW', type='NUMBER', required='*')
    system_heat_rate: Final[float] = OUTPUT(label='System heat rate', units='MMBtu/MWh', type='NUMBER', required='*')
    annual_fuel_usage: Final[float] = OUTPUT(label='Annual fuel usage', units='kWht', type='NUMBER', required='*')
    annual_total_water_use: Final[float] = OUTPUT(label='Total Annual Water Usage: cycle + mirror washing', units='m3', type='NUMBER', group='PostProcess', required='*')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Adjustment Factors', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly Adjustment Factors', units='%', type='ARRAY', group='Adjustment Factors', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based Adjustment Factors', units='%', type='MATRIX', group='Adjustment Factors', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    gen: Final[Array] = OUTPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 file_name: str = ...,
                 track_mode: float = ...,
                 tilt: float = ...,
                 azimuth: float = ...,
                 system_capacity: float = ...,
                 nSCA: float = ...,
                 nHCEt: float = ...,
                 nColt: float = ...,
                 nHCEVar: float = ...,
                 nLoops: float = ...,
                 eta_pump: float = ...,
                 HDR_rough: float = ...,
                 theta_stow: float = ...,
                 theta_dep: float = ...,
                 Row_Distance: float = ...,
                 FieldConfig: float = ...,
                 T_startup: float = ...,
                 P_ref: float = ...,
                 m_dot_htfmin: float = ...,
                 m_dot_htfmax: float = ...,
                 T_loop_in_des: float = ...,
                 T_loop_out: float = ...,
                 Fluid: float = ...,
                 T_fp: float = ...,
                 I_bn_des: float = ...,
                 calc_design_pipe_vals: float = ...,
                 V_hdr_cold_max: float = ...,
                 V_hdr_cold_min: float = ...,
                 V_hdr_hot_max: float = ...,
                 V_hdr_hot_min: float = ...,
                 N_max_hdr_diams: float = ...,
                 L_rnr_pb: float = ...,
                 L_rnr_per_xpan: float = ...,
                 L_xpan_hdr: float = ...,
                 L_xpan_rnr: float = ...,
                 Min_rnr_xpans: float = ...,
                 northsouth_field_sep: float = ...,
                 N_hdr_per_xpan: float = ...,
                 offset_xpan_hdr: float = ...,
                 Pipe_hl_coef: float = ...,
                 SCA_drives_elec: float = ...,
                 fthrok: float = ...,
                 fthrctrl: float = ...,
                 water_usage_per_wash: float = ...,
                 washing_frequency: float = ...,
                 accept_mode: float = ...,
                 accept_init: float = ...,
                 accept_loc: float = ...,
                 solar_mult: float = ...,
                 mc_bal_hot: float = ...,
                 mc_bal_cold: float = ...,
                 mc_bal_sca: float = ...,
                 W_aperture: Array = ...,
                 A_aperture: Array = ...,
                 TrackingError: Array = ...,
                 GeomEffects: Array = ...,
                 Rho_mirror_clean: Array = ...,
                 Dirt_mirror: Array = ...,
                 Error: Array = ...,
                 Ave_Focal_Length: Array = ...,
                 L_SCA: Array = ...,
                 L_aperture: Array = ...,
                 ColperSCA: Array = ...,
                 Distance_SCA: Array = ...,
                 IAM_matrix: Matrix = ...,
                 HCE_FieldFrac: Matrix = ...,
                 D_2: Matrix = ...,
                 D_3: Matrix = ...,
                 D_4: Matrix = ...,
                 D_5: Matrix = ...,
                 D_p: Matrix = ...,
                 Flow_type: Matrix = ...,
                 Rough: Matrix = ...,
                 alpha_env: Matrix = ...,
                 epsilon_3_11: Matrix = ...,
                 epsilon_3_12: Matrix = ...,
                 epsilon_3_13: Matrix = ...,
                 epsilon_3_14: Matrix = ...,
                 epsilon_3_21: Matrix = ...,
                 epsilon_3_22: Matrix = ...,
                 epsilon_3_23: Matrix = ...,
                 epsilon_3_24: Matrix = ...,
                 epsilon_3_31: Matrix = ...,
                 epsilon_3_32: Matrix = ...,
                 epsilon_3_33: Matrix = ...,
                 epsilon_3_34: Matrix = ...,
                 epsilon_3_41: Matrix = ...,
                 epsilon_3_42: Matrix = ...,
                 epsilon_3_43: Matrix = ...,
                 epsilon_3_44: Matrix = ...,
                 alpha_abs: Matrix = ...,
                 Tau_envelope: Matrix = ...,
                 EPSILON_4: Matrix = ...,
                 EPSILON_5: Matrix = ...,
                 GlazingIntactIn: Matrix = ...,
                 P_a: Matrix = ...,
                 AnnulusGas: Matrix = ...,
                 AbsorberMaterial: Matrix = ...,
                 Shadowing: Matrix = ...,
                 Dirt_HCE: Matrix = ...,
                 Design_loss: Matrix = ...,
                 SCAInfoArray: Matrix = ...,
                 SCADefocusArray: Array = ...,
                 K_cpnt: Matrix = ...,
                 D_cpnt: Matrix = ...,
                 L_cpnt: Matrix = ...,
                 Type_cpnt: Matrix = ...,
                 custom_sf_pipe_sizes: float = ...,
                 sf_rnr_diams: Array = ...,
                 sf_rnr_wallthicks: Array = ...,
                 sf_rnr_lengths: Array = ...,
                 sf_hdr_diams: Array = ...,
                 sf_hdr_wallthicks: Array = ...,
                 sf_hdr_lengths: Array = ...,
                 field_fl_props: Matrix = ...,
                 store_fl_props: Matrix = ...,
                 store_fluid: float = ...,
                 tshours: float = ...,
                 is_hx: float = ...,
                 dt_hot: float = ...,
                 dt_cold: float = ...,
                 hx_config: float = ...,
                 q_max_aux: float = ...,
                 T_set_aux: float = ...,
                 V_tank_hot_ini: float = ...,
                 T_tank_cold_ini: float = ...,
                 vol_tank: float = ...,
                 h_tank: float = ...,
                 h_tank_min: float = ...,
                 u_tank: float = ...,
                 tank_pairs: float = ...,
                 cold_tank_Thtr: float = ...,
                 hot_tank_Thtr: float = ...,
                 tank_max_heat: float = ...,
                 tanks_in_parallel: float = ...,
                 has_hot_tank_bypass: float = ...,
                 T_tank_hot_inlet_min: float = ...,
                 q_pb_design: float = ...,
                 W_pb_design: float = ...,
                 cycle_max_frac: float = ...,
                 cycle_cutoff_frac: float = ...,
                 pb_pump_coef: float = ...,
                 tes_pump_coef: float = ...,
                 V_tes_des: float = ...,
                 custom_tes_p_loss: float = ...,
                 k_tes_loss_coeffs: Array = ...,
                 custom_sgs_pipe_sizes: float = ...,
                 sgs_diams: Array = ...,
                 sgs_wallthicks: Array = ...,
                 sgs_lengths: Array = ...,
                 DP_SGS: float = ...,
                 pb_fixed_par: float = ...,
                 bop_array: Array = ...,
                 aux_array: Array = ...,
                 fossil_mode: float = ...,
                 t_standby_reset: float = ...,
                 sf_type: float = ...,
                 tes_type: float = ...,
                 tslogic_a: Array = ...,
                 tslogic_b: Array = ...,
                 tslogic_c: Array = ...,
                 ffrac: Array = ...,
                 tc_fill: float = ...,
                 tc_void: float = ...,
                 t_dis_out_min: float = ...,
                 t_ch_out_max: float = ...,
                 nodes: float = ...,
                 f_tc_cold: float = ...,
                 weekday_schedule: Matrix = ...,
                 weekend_schedule: Matrix = ...,
                 pc_config: float = ...,
                 eta_ref: float = ...,
                 startup_time: float = ...,
                 startup_frac: float = ...,
                 q_sby_frac: float = ...,
                 dT_cw_ref: float = ...,
                 T_amb_des: float = ...,
                 P_boil: float = ...,
                 CT: float = ...,
                 T_approach: float = ...,
                 T_ITD_des: float = ...,
                 P_cond_ratio: float = ...,
                 pb_bd_frac: float = ...,
                 P_cond_min: float = ...,
                 n_pl_inc: float = ...,
                 F_wc: Array = ...,
                 tech_type: float = ...,
                 ud_T_amb_des: float = ...,
                 ud_f_W_dot_cool_des: float = ...,
                 ud_m_dot_water_cool_des: float = ...,
                 ud_T_htf_low: float = ...,
                 ud_T_htf_high: float = ...,
                 ud_T_amb_low: float = ...,
                 ud_T_amb_high: float = ...,
                 ud_m_dot_htf_low: float = ...,
                 ud_m_dot_htf_high: float = ...,
                 ud_T_htf_ind_od: Matrix = ...,
                 ud_T_amb_ind_od: Matrix = ...,
                 ud_m_dot_htf_ind_od: Matrix = ...,
                 ud_ind_od: Matrix = ...,
                 eta_lhv: float = ...,
                 eta_tes_htr: float = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
