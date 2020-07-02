
# This is a generated file

"""trough_physical - Physical trough applications"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'file_name': str,
        'nSCA': float,
        'nHCEt': float,
        'nColt': float,
        'nHCEVar': float,
        'nLoops': float,
        'FieldConfig': float,
        'include_fixed_power_block_runner': float,
        'L_power_block_piping': float,
        'eta_pump': float,
        'Fluid': float,
        'accept_loc': float,
        'HDR_rough': float,
        'theta_stow': float,
        'theta_dep': float,
        'Row_Distance': float,
        'T_loop_in_des': float,
        'T_loop_out': float,
        'm_dot_htfmin': float,
        'm_dot_htfmax': float,
        'field_fl_props': Matrix,
        'T_fp': float,
        'I_bn_des': float,
        'Pipe_hl_coef': float,
        'SCA_drives_elec': float,
        'tilt': float,
        'azimuth': float,
        'wind_stow_speed': float,
        'accept_mode': float,
        'accept_init': float,
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
        'rec_su_delay': float,
        'rec_qf_delay': float,
        'p_start': float,
        'pc_config': float,
        'P_ref': float,
        'eta_ref': float,
        'cycle_max_frac': float,
        'cycle_cutoff_frac': float,
        'q_sby_frac': float,
        'startup_time': float,
        'startup_frac': float,
        'pb_pump_coef': float,
        'dT_cw_ref': float,
        'T_amb_des': float,
        'P_boil': float,
        'CT': float,
        'tech_type': float,
        'T_approach': float,
        'T_ITD_des': float,
        'P_cond_ratio': float,
        'pb_bd_frac': float,
        'P_cond_min': float,
        'n_pl_inc': float,
        'F_wc': Array,
        'ud_f_W_dot_cool_des': float,
        'ud_m_dot_water_cool_des': float,
        'ud_ind_od': Matrix,
        'store_fluid': float,
        'store_fl_props': Matrix,
        'is_hx': float,
        'tshours': float,
        'h_tank': float,
        'u_tank': float,
        'tank_pairs': float,
        'hot_tank_Thtr': float,
        'hot_tank_max_heat': float,
        'cold_tank_Thtr': float,
        'cold_tank_max_heat': float,
        'dt_hot': float,
        'h_tank_min': float,
        'init_hot_htf_percent': float,
        'weekday_schedule': Matrix,
        'weekend_schedule': Matrix,
        'dispatch_sched_weekday': Matrix,
        'dispatch_sched_weekend': Matrix,
        'is_tod_pc_target_also_pc_max': float,
        'is_dispatch': float,
        'is_write_ampl_dat': float,
        'is_ampl_engine': float,
        'ampl_data_dir': str,
        'ampl_exec_call': str,
        'disp_frequency': float,
        'disp_steps_per_hour': float,
        'disp_horizon': float,
        'disp_max_iter': float,
        'disp_timeout': float,
        'disp_mip_gap': float,
        'disp_spec_presolve': float,
        'disp_spec_bb': float,
        'disp_reporting': float,
        'disp_spec_scaling': float,
        'disp_time_weighting': float,
        'disp_rsu_cost': float,
        'disp_csu_cost': float,
        'disp_pen_delta_w': float,
        'q_rec_standby': float,
        'q_rec_heattrace': float,
        'is_wlim_series': float,
        'wlim_series': Array,
        'f_turb_tou_periods': Array,
        'ppa_multiplier_model': float,
        'dispatch_factors_ts': Array,
        'dispatch_factor1': float,
        'dispatch_factor2': float,
        'dispatch_factor3': float,
        'dispatch_factor4': float,
        'dispatch_factor5': float,
        'dispatch_factor6': float,
        'dispatch_factor7': float,
        'dispatch_factor8': float,
        'dispatch_factor9': float,
        'is_dispatch_series': float,
        'dispatch_series': Array,
        'pb_fixed_par': float,
        'bop_array': Array,
        'aux_array': Array,
        'gross_net_conversion_factor': float,
        'water_usage_per_wash': float,
        'washing_frequency': float,
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
        'K_cpnt': Matrix,
        'D_cpnt': Matrix,
        'L_cpnt': Matrix,
        'Type_cpnt': Matrix,
        'custom_sf_pipe_sizes': float,
        'sf_rnr_diams': Matrix,
        'sf_rnr_wallthicks': Matrix,
        'sf_rnr_lengths': Matrix,
        'sf_hdr_diams': Matrix,
        'sf_hdr_wallthicks': Matrix,
        'sf_hdr_lengths': Matrix,
        'tanks_in_parallel': float,
        'has_hot_tank_bypass': float,
        'T_tank_hot_inlet_min': float,
        'tes_pump_coef': float,
        'V_tes_des': float,
        'custom_tes_p_loss': float,
        'k_tes_loss_coeffs': Matrix,
        'custom_tes_pipe_sizes': float,
        'tes_diams': Matrix,
        'tes_wallthicks': Matrix,
        'tes_lengths': Matrix,
        'DP_SGS': float,
        'time_hr': Array,
        'month': Array,
        'hour_day': Array,
        'solazi': Array,
        'solzen': Array,
        'beam': Array,
        'tdry': Array,
        'twet': Array,
        'rh': Array,
        'wspd': Array,
        'pres': Array,
        'defocus': Array,
        'Theta_ave': Array,
        'CosTh_ave': Array,
        'IAM_ave': Array,
        'RowShadow_ave': Array,
        'EndLoss_ave': Array,
        'dni_costh': Array,
        'EqOpteff': Array,
        'SCAs_def': Array,
        'q_inc_sf_tot': Array,
        'qinc_costh': Array,
        'q_dot_rec_inc': Array,
        'q_dot_rec_thermal_loss': Array,
        'q_dot_rec_abs': Array,
        'q_dot_piping_loss': Array,
        'e_dot_field_int_energy': Array,
        'q_dot_htf_sf_out': Array,
        'q_dot_freeze_prot': Array,
        'm_dot_loop': Array,
        'm_dot_field_recirc': Array,
        'm_dot_field_delivered': Array,
        'T_field_cold_in': Array,
        'T_rec_cold_in': Array,
        'T_rec_hot_out': Array,
        'T_field_hot_out': Array,
        'deltaP_field': Array,
        'W_dot_sca_track': Array,
        'W_dot_field_pump': Array,
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
        'eta': Array,
        'q_pb': Array,
        'm_dot_pc': Array,
        'q_dot_pc_startup': Array,
        'P_cycle': Array,
        'T_pc_in': Array,
        'T_pc_out': Array,
        'm_dot_water_pc': Array,
        'q_pc_startup': Array,
        'tank_losses': Array,
        'q_tes_heater': Array,
        'T_tes_hot': Array,
        'T_tes_cold': Array,
        'q_dc_tes': Array,
        'q_ch_tes': Array,
        'e_ch_tes': Array,
        'm_dot_tes_dc': Array,
        'm_dot_tes_ch': Array,
        'op_mode_1': Array,
        'op_mode_2': Array,
        'op_mode_3': Array,
        'm_dot_balance': Array,
        'q_balance': Array,
        'monthly_energy': Array,
        'annual_energy': float,
        'annual_thermal_consumption': float,
        'annual_total_water_use': float,
        'annual_field_freeze_protection': float,
        'annual_tes_freeze_protection': float,
        'n_op_modes': Array,
        'tou_value': Array,
        'pricing_mult': Array,
        'q_dot_pc_sb': Array,
        'q_dot_pc_min': Array,
        'q_dot_pc_target': Array,
        'q_dot_pc_max': Array,
        'is_rec_su_allowed': Array,
        'is_pc_su_allowed': Array,
        'is_pc_sb_allowed': Array,
        'q_dot_est_cr_su': Array,
        'q_dot_est_cr_on': Array,
        'q_dot_est_tes_dc': Array,
        'q_dot_est_tes_ch': Array,
        'operating_modes_a': Array,
        'operating_modes_b': Array,
        'operating_modes_c': Array,
        'disp_solve_state': Array,
        'disp_solve_iter': Array,
        'disp_objective': Array,
        'disp_obj_relax': Array,
        'disp_qsf_expected': Array,
        'disp_qsfprod_expected': Array,
        'disp_qsfsu_expected': Array,
        'disp_tes_expected': Array,
        'disp_pceff_expected': Array,
        'disp_thermeff_expected': Array,
        'disp_qpbsu_expected': Array,
        'disp_wpb_expected': Array,
        'disp_rev_expected': Array,
        'disp_presolve_nconstr': Array,
        'disp_presolve_nvar': Array,
        'disp_solve_time': Array,
        'htf_pump_power': Array,
        'P_cooling_tower_tot': Array,
        'P_fixed': Array,
        'P_plant_balance_tot': Array,
        'P_out_net': Array,
        'gen': Array,
        'annual_W_cycle_gross': float,
        'conversion_factor': float,
        'capacity_factor': float,
        'kwh_per_kw': float,
        'recirculating': Array,
        'pipe_tes_diams': Array,
        'pipe_tes_wallthk': Array,
        'pipe_tes_mdot_dsn': Array,
        'pipe_tes_vel_dsn': Array,
        'pipe_tes_T_dsn': Array,
        'pipe_tes_P_dsn': Array,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix
}, total=False)

class Data(ssc.DataDict):
    file_name: str = INPUT(label='Local weather file with path', units='none', type='STRING', group='weather', required='*', constraints='LOCAL_FILE')
    nSCA: float = INPUT(label='Number of SCAs in a loop', units='none', type='NUMBER', group='solar_field', required='*')
    nHCEt: float = INPUT(label='Number of HCE types', units='none', type='NUMBER', group='solar_field', required='*')
    nColt: float = INPUT(label='Number of collector types', units='none', type='NUMBER', group='solar_field', required='*', meta='constant=4')
    nHCEVar: float = INPUT(label='Number of HCE variants per type', units='none', type='NUMBER', group='solar_field', required='*')
    nLoops: float = INPUT(label='Number of loops in the field', units='none', type='NUMBER', group='solar_field', required='*')
    FieldConfig: float = INPUT(label='Number of subfield headers', units='none', type='NUMBER', group='solar_field', required='*')
    include_fixed_power_block_runner: float = INPUT(label='Should model consider piping through power block?', units='none', type='NUMBER', group='solar_field', required='*')
    L_power_block_piping: float = INPUT(label='Length of piping (full mass flow) through heat sink (if applicable)', units='none', type='NUMBER', group='solar_field', required='*')
    eta_pump: float = INPUT(label='HTF pump efficiency', units='none', type='NUMBER', group='solar_field', required='*')
    Fluid: float = INPUT(label='Field HTF fluid ID number', units='none', type='NUMBER', group='solar_field', required='*')
    accept_loc: float = INPUT(label='In acceptance testing mode - temperature sensor location', units='1/2', type='NUMBER', group='solar_field', required='*', meta='hx/loop')
    HDR_rough: float = INPUT(label='Header pipe roughness', units='m', type='NUMBER', group='solar_field', required='*')
    theta_stow: float = INPUT(label='Stow angle', units='deg', type='NUMBER', group='solar_field', required='*')
    theta_dep: float = INPUT(label='Deploy angle', units='deg', type='NUMBER', group='solar_field', required='*')
    Row_Distance: float = INPUT(label='Spacing between rows (centerline to centerline)', units='m', type='NUMBER', group='solar_field', required='*')
    T_loop_in_des: float = INPUT(label='Design loop inlet temperature', units='C', type='NUMBER', group='solar_field', required='*')
    T_loop_out: float = INPUT(label='Target loop outlet temperature', units='C', type='NUMBER', group='solar_field', required='*')
    m_dot_htfmin: float = INPUT(label='Minimum loop HTF flow rate', units='kg/s', type='NUMBER', group='solar_field', required='*')
    m_dot_htfmax: float = INPUT(label='Maximum loop HTF flow rate', units='kg/s', type='NUMBER', group='solar_field', required='*')
    field_fl_props: Matrix = INPUT(label='User defined field fluid property data', units='-', type='MATRIX', group='solar_field', required='*')
    T_fp: float = INPUT(label='Freeze protection temperature (heat trace activation temperature)', units='none', type='NUMBER', group='solar_field', required='*')
    I_bn_des: float = INPUT(label='Solar irradiation at design', units='C', type='NUMBER', group='solar_field', required='*')
    Pipe_hl_coef: float = INPUT(label='Loss coefficient from the header, runner pipe, and non-HCE piping', units='m/s', type='NUMBER', group='solar_field', required='*')
    SCA_drives_elec: float = INPUT(label='Tracking power, in Watts per SCA drive', units='W/m2-K', type='NUMBER', group='solar_field', required='*')
    tilt: float = INPUT(label='Tilt angle of surface/axis', units='none', type='NUMBER', group='solar_field', required='*')
    azimuth: float = INPUT(label='Azimuth angle of surface/axis', units='none', type='NUMBER', group='solar_field', required='*')
    wind_stow_speed: float = INPUT(label='Trough wind stow speed', units='m/s', type='NUMBER', group='solar_field', required='?=50')
    accept_mode: float = INPUT(label='Acceptance testing mode?', units='0/1', type='NUMBER', group='solar_field', required='*', meta='no/yes')
    accept_init: float = INPUT(label='In acceptance testing mode - require steady-state startup', units='none', type='NUMBER', group='solar_field', required='*')
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
    rec_su_delay: float = INPUT(label='Fixed startup delay time for the receiver', units='hr', type='NUMBER', group='solar_field', required='*')
    rec_qf_delay: float = INPUT(label='Energy-based receiver startup delay (fraction of rated thermal power)', units='-', type='NUMBER', group='solar_field', required='*')
    p_start: float = INPUT(label='Collector startup energy, per SCA', units='kWe-hr', type='NUMBER', group='solar_field', required='*')
    pc_config: float = INPUT(label='0: Steam Rankine (224), 1: user defined', units='-', type='NUMBER', group='powerblock', required='?=0', constraints='INTEGER')
    P_ref: float = INPUT(label='Rated plant capacity', units='MWe', type='NUMBER', group='powerblock', required='*')
    eta_ref: float = INPUT(label='Power cycle efficiency at design', units='none', type='NUMBER', group='powerblock', required='*')
    cycle_max_frac: float = INPUT(label='Maximum turbine over design operation fraction', units='-', type='NUMBER', group='powerblock', required='*')
    cycle_cutoff_frac: float = INPUT(label='Minimum turbine operation fraction before shutdown', units='-', type='NUMBER', group='powerblock', required='*')
    q_sby_frac: float = INPUT(label='Fraction of thermal power required for standby mode', units='none', type='NUMBER', group='powerblock', required='*')
    startup_time: float = INPUT(label='Time needed for power block startup', units='hr', type='NUMBER', group='powerblock', required='*')
    startup_frac: float = INPUT(label='Fraction of design thermal power needed for startup', units='none', type='NUMBER', group='powerblock', required='*')
    pb_pump_coef: float = INPUT(label='Pumping power to move 1kg of HTF through PB loop', units='kW/kg', type='NUMBER', group='powerblock', required='*')
    dT_cw_ref: float = INPUT(label='Reference condenser cooling water inlet/outlet T diff', units='C', type='NUMBER', group='powerblock', required='pc_config=0')
    T_amb_des: float = INPUT(label='Reference ambient temperature at design point', units='C', type='NUMBER', group='powerblock', required='pc_config=0')
    P_boil: float = INPUT(label='Boiler operating pressure', units='bar', type='NUMBER', group='powerblock', required='pc_config=0')
    CT: float = INPUT(label='Flag for using dry cooling or wet cooling system', units='none', type='NUMBER', group='powerblock', required='pc_config=0')
    tech_type: float = INPUT(label='Turbine inlet pressure control flag (sliding=user, fixed=trough)', units='1/2/3', type='NUMBER', group='powerblock', required='pc_config=0', meta='tower/trough/user')
    T_approach: float = INPUT(label='Cooling tower approach temperature', units='C', type='NUMBER', group='powerblock', required='pc_config=0')
    T_ITD_des: float = INPUT(label='ITD at design for dry system', units='C', type='NUMBER', group='powerblock', required='pc_config=0')
    P_cond_ratio: float = INPUT(label='Condenser pressure ratio', units='none', type='NUMBER', group='powerblock', required='pc_config=0')
    pb_bd_frac: float = INPUT(label='Power block blowdown steam fraction ', units='none', type='NUMBER', group='powerblock', required='pc_config=0')
    P_cond_min: float = INPUT(label='Minimum condenser pressure', units='inHg', type='NUMBER', group='powerblock', required='pc_config=0')
    n_pl_inc: float = INPUT(label='Number of part-load increments for the heat rejection system', units='none', type='NUMBER', group='powerblock', required='pc_config=0')
    F_wc: Array = INPUT(label='Fraction indicating wet cooling use for hybrid system', units='none', type='ARRAY', group='powerblock', required='pc_config=0', meta='constant=[0,0,0,0,0,0,0,0,0]')
    ud_f_W_dot_cool_des: float = INPUT(label='Percent of user-defined power cycle design gross output consumed by cooling', units='%', type='NUMBER', group='powerblock', required='pc_config=1')
    ud_m_dot_water_cool_des: float = INPUT(label='Mass flow rate of water required at user-defined power cycle design point', units='kg/s', type='NUMBER', group='powerblock', required='pc_config=1')
    ud_ind_od: Matrix = INPUT(label='Off design user-defined power cycle performance as function of T_htf, m_dot_htf [ND], and T_amb', type='MATRIX', group='powerblock', required='pc_config=1')
    store_fluid: float = INPUT(label='Material number for storage fluid', units='-', type='NUMBER', group='TES', required='*')
    store_fl_props: Matrix = INPUT(label='User defined storage fluid property data', units='-', type='MATRIX', group='TES', required='*')
    is_hx: float = INPUT(label='Heat exchanger (HX) exists (1=yes, 0=no)', units='-', type='NUMBER', group='TES', required='*')
    tshours: float = INPUT(label='Equivalent full-load thermal storage hours', units='hr', type='NUMBER', group='TES', required='*')
    h_tank: float = INPUT(label='Total height of tank (height of HTF when tank is full', units='m', type='NUMBER', group='TES', required='*')
    u_tank: float = INPUT(label='Loss coefficient from the tank', units='W/m2-K', type='NUMBER', group='TES', required='*')
    tank_pairs: float = INPUT(label='Number of equivalent tank pairs', units='-', type='NUMBER', group='TES', required='*', constraints='INTEGER')
    hot_tank_Thtr: float = INPUT(label='Minimum allowable hot tank HTF temp', units='C', type='NUMBER', group='TES', required='*')
    hot_tank_max_heat: float = INPUT(label='Rated heater capacity for hot tank heating', units='MWe', type='NUMBER', group='TES', required='*')
    cold_tank_Thtr: float = INPUT(label='Minimum allowable cold tank HTF temp', units='C', type='NUMBER', group='TES', required='*')
    cold_tank_max_heat: float = INPUT(label='Rated heater capacity for cold tank heating', units='MWe', type='NUMBER', group='TES', required='*')
    dt_hot: float = INPUT(label='Hot side HX approach temp', units='C', type='NUMBER', group='TES', required='*')
    h_tank_min: float = INPUT(label='Minimum allowable HTF height in storage tank', units='m', type='NUMBER', group='TES', required='*')
    init_hot_htf_percent: float = INPUT(label='Initial fraction of avail. vol that is hot', units='%', type='NUMBER', group='TES', required='*')
    weekday_schedule: Matrix = INPUT(label='12x24 CSP operation Time-of-Use Weekday schedule', units='-', type='MATRIX', group='tou', required='*')
    weekend_schedule: Matrix = INPUT(label='12x24 CSP operation Time-of-Use Weekend schedule', units='-', type='MATRIX', group='tou', required='*')
    dispatch_sched_weekday: Matrix = INPUT(label='12x24 PPA pricing Weekday schedule', type='MATRIX', group='tou', required='?=1')
    dispatch_sched_weekend: Matrix = INPUT(label='12x24 PPA pricing Weekend schedule', type='MATRIX', group='tou', required='?=1')
    is_tod_pc_target_also_pc_max: float = INPUT(label='Is the TOD target cycle heat input also the max cycle heat input?', type='NUMBER', group='tou', required='?=0')
    is_dispatch: float = INPUT(label='Allow dispatch optimization?', units='-', type='NUMBER', group='tou', required='?=0')
    is_write_ampl_dat: float = INPUT(label='Write AMPL data files for dispatch run', units='-', type='NUMBER', group='tou', required='?=0')
    is_ampl_engine: float = INPUT(label='Run dispatch optimization with external AMPL engine', units='-', type='NUMBER', group='tou', required='?=0')
    ampl_data_dir: str = INPUT(label='AMPL data file directory', units='-', type='STRING', group='tou', required="?=''")
    ampl_exec_call: str = INPUT(label='System command to run AMPL code', units='-', type='STRING', group='tou', required="?='ampl sdk_solution.run'")
    disp_frequency: float = INPUT(label='Frequency for dispatch optimization calculations', units='hour', type='NUMBER', group='tou', required='is_dispatch=1')
    disp_steps_per_hour: float = INPUT(label='Time steps per hour for dispatch optimization calculations', units='-', type='NUMBER', group='tou', required='?=1')
    disp_horizon: float = INPUT(label='Time horizon for dispatch optimization', units='hour', type='NUMBER', group='tou', required='is_dispatch=1')
    disp_max_iter: float = INPUT(label='Max. no. dispatch optimization iterations', units='-', type='NUMBER', group='tou', required='is_dispatch=1')
    disp_timeout: float = INPUT(label='Max. dispatch optimization solve duration', units='s', type='NUMBER', group='tou', required='is_dispatch=1')
    disp_mip_gap: float = INPUT(label='Dispatch optimization solution tolerance', units='-', type='NUMBER', group='tou', required='is_dispatch=1')
    disp_spec_presolve: float = INPUT(label='Dispatch optimization presolve heuristic', units='-', type='NUMBER', group='tou', required='?=-1')
    disp_spec_bb: float = INPUT(label='Dispatch optimization B&B heuristic', units='-', type='NUMBER', group='tou', required='?=-1')
    disp_reporting: float = INPUT(label='Dispatch optimization reporting level', units='-', type='NUMBER', group='tou', required='?=-1')
    disp_spec_scaling: float = INPUT(label='Dispatch optimization scaling heuristic', units='-', type='NUMBER', group='tou', required='?=-1')
    disp_time_weighting: float = INPUT(label='Dispatch optimization future time discounting factor', units='-', type='NUMBER', group='tou', required='?=0.99')
    disp_rsu_cost: float = INPUT(label='Receiver startup cost', units='$', type='NUMBER', group='tou', required='is_dispatch=1')
    disp_csu_cost: float = INPUT(label='Cycle startup cost', units='$', type='NUMBER', group='tou', required='is_dispatch=1')
    disp_pen_delta_w: float = INPUT(label='Dispatch cycle production change penalty', units='$/kWe-change', type='NUMBER', group='tou', required='is_dispatch=1')
    q_rec_standby: float = INPUT(label='Receiver standby energy consumption', units='kWt', type='NUMBER', group='tou', required='?=9e99')
    q_rec_heattrace: float = INPUT(label='Receiver heat trace energy consumption during startup', units='kWe-hr', type='NUMBER', group='tou', required='?=0.0')
    is_wlim_series: float = INPUT(label='Use time-series net electricity generation limits', type='NUMBER', group='tou', required='?=0')
    wlim_series: Array = INPUT(label='Time series net electicity generation limits', units='kWe', type='ARRAY', group='tou', required='is_wlim_series=1')
    f_turb_tou_periods: Array = INPUT(label='Dispatch logic for turbine load fraction', units='-', type='ARRAY', group='tou', required='*')
    ppa_multiplier_model: float = INPUT(label='PPA multiplier model', units='0/1', type='NUMBER', group='tou', required='?=0', constraints='INTEGER,MIN=0', meta='0=diurnal,1=timestep')
    dispatch_factors_ts: Array = INPUT(label='Dispatch payment factor array', type='ARRAY', group='tou', required='ppa_multiplier_model=1')
    dispatch_factor1: float = INPUT(label='Dispatch payment factor 1', type='NUMBER', group='tou', required='?=1')
    dispatch_factor2: float = INPUT(label='Dispatch payment factor 2', type='NUMBER', group='tou', required='?=1')
    dispatch_factor3: float = INPUT(label='Dispatch payment factor 3', type='NUMBER', group='tou', required='?=1')
    dispatch_factor4: float = INPUT(label='Dispatch payment factor 4', type='NUMBER', group='tou', required='?=1')
    dispatch_factor5: float = INPUT(label='Dispatch payment factor 5', type='NUMBER', group='tou', required='?=1')
    dispatch_factor6: float = INPUT(label='Dispatch payment factor 6', type='NUMBER', group='tou', required='?=1')
    dispatch_factor7: float = INPUT(label='Dispatch payment factor 7', type='NUMBER', group='tou', required='?=1')
    dispatch_factor8: float = INPUT(label='Dispatch payment factor 8', type='NUMBER', group='tou', required='?=1')
    dispatch_factor9: float = INPUT(label='Dispatch payment factor 9', type='NUMBER', group='tou', required='?=1')
    is_dispatch_series: float = INPUT(label='Use time-series dispatch factors', type='NUMBER', group='tou', required='?=1')
    dispatch_series: Array = INPUT(label='Time series dispatch factors', type='ARRAY', group='tou')
    pb_fixed_par: float = INPUT(label='Fraction of rated gross power constantly consumed', units='MWe/MWcap', type='NUMBER', group='system', required='*')
    bop_array: Array = INPUT(label='Balance of plant parasitic power fraction, mult frac and const, linear and quad coeff', type='ARRAY', group='system', required='*')
    aux_array: Array = INPUT(label='Auxiliary heater, mult frac and const, linear and quad coeff', type='ARRAY', group='system', required='*')
    gross_net_conversion_factor: float = INPUT(label='Estimated gross to net conversion factor', type='NUMBER', group='system', required='*')
    water_usage_per_wash: float = INPUT(label='Water usage per wash', units='L/m2_aper', type='NUMBER', group='system', required='*')
    washing_frequency: float = INPUT(label='Mirror washing frequency', units='-/year', type='NUMBER', group='system', required='*')
    calc_design_pipe_vals: float = INPUT(label='Calculate temps and pressures at design conditions for runners and headers', units='none', type='NUMBER', group='solar_field', required='*')
    V_hdr_cold_max: float = INPUT(label='Maximum HTF velocity in the cold headers at design', units='m/s', type='NUMBER', group='solar_field', required='*')
    V_hdr_cold_min: float = INPUT(label='Minimum HTF velocity in the cold headers at design', units='m/s', type='NUMBER', group='solar_field', required='*')
    V_hdr_hot_max: float = INPUT(label='Maximum HTF velocity in the hot headers at design', units='m/s', type='NUMBER', group='solar_field', required='*')
    V_hdr_hot_min: float = INPUT(label='Minimum HTF velocity in the hot headers at design', units='m/s', type='NUMBER', group='solar_field', required='*')
    N_max_hdr_diams: float = INPUT(label='Maximum number of diameters in each of the hot and cold headers', units='none', type='NUMBER', group='solar_field', required='*')
    L_rnr_pb: float = INPUT(label='Length of runner pipe in power block', units='m', type='NUMBER', group='powerblock', required='*')
    L_rnr_per_xpan: float = INPUT(label='Threshold length of straight runner pipe without an expansion loop', units='m', type='NUMBER', group='solar_field', required='*')
    L_xpan_hdr: float = INPUT(label='Compined perpendicular lengths of each header expansion loop', units='m', type='NUMBER', group='solar_field', required='*')
    L_xpan_rnr: float = INPUT(label='Compined perpendicular lengths of each runner expansion loop', units='m', type='NUMBER', group='solar_field', required='*')
    Min_rnr_xpans: float = INPUT(label='Minimum number of expansion loops per single-diameter runner section', units='none', type='NUMBER', group='solar_field', required='*')
    northsouth_field_sep: float = INPUT(label='North/south separation between subfields. 0 = SCAs are touching', units='m', type='NUMBER', group='solar_field', required='*')
    N_hdr_per_xpan: float = INPUT(label='Number of collector loops per expansion loop', units='none', type='NUMBER', group='solar_field', required='*')
    offset_xpan_hdr: float = INPUT(label='Location of first header expansion loop. 1 = after first collector loop', units='none', type='NUMBER', group='solar_field', required='*')
    K_cpnt: Matrix = INPUT(label='Interconnect component minor loss coefficients, row=intc, col=cpnt', units='none', type='MATRIX', group='solar_field', required='*')
    D_cpnt: Matrix = INPUT(label='Interconnect component diameters, row=intc, col=cpnt', units='none', type='MATRIX', group='solar_field', required='*')
    L_cpnt: Matrix = INPUT(label='Interconnect component lengths, row=intc, col=cpnt', units='none', type='MATRIX', group='solar_field', required='*')
    Type_cpnt: Matrix = INPUT(label='Interconnect component type, row=intc, col=cpnt', units='none', type='MATRIX', group='solar_field', required='*')
    custom_sf_pipe_sizes: float = INPUT(label='Use custom solar field pipe diams, wallthks, and lengths', units='none', type='NUMBER', group='solar_field', required='*')
    sf_rnr_diams: Matrix = INPUT(label='Custom runner diameters', units='m', type='MATRIX', group='solar_field', required='*')
    sf_rnr_wallthicks: Matrix = INPUT(label='Custom runner wall thicknesses', units='m', type='MATRIX', group='solar_field', required='*')
    sf_rnr_lengths: Matrix = INPUT(label='Custom runner lengths', units='m', type='MATRIX', group='solar_field', required='*')
    sf_hdr_diams: Matrix = INPUT(label='Custom header diameters', units='m', type='MATRIX', group='solar_field', required='*')
    sf_hdr_wallthicks: Matrix = INPUT(label='Custom header wall thicknesses', units='m', type='MATRIX', group='solar_field', required='*')
    sf_hdr_lengths: Matrix = INPUT(label='Custom header lengths', units='m', type='MATRIX', group='solar_field', required='*')
    tanks_in_parallel: float = INPUT(label='Tanks are in parallel, not in series, with solar field', units='-', type='NUMBER', group='controller', required='*')
    has_hot_tank_bypass: float = INPUT(label='Bypass valve connects field outlet to cold tank', units='-', type='NUMBER', group='controller', required='*')
    T_tank_hot_inlet_min: float = INPUT(label='Minimum hot tank htf inlet temperature', units='C', type='NUMBER', group='controller', required='*')
    tes_pump_coef: float = INPUT(label='Pumping power to move 1kg of HTF through tes loop', units='kW/(kg/s)', type='NUMBER', group='controller', required='*')
    V_tes_des: float = INPUT(label='Design-point velocity to size the TES pipe diameters', units='m/s', type='NUMBER', group='controller', required='*')
    custom_tes_p_loss: float = INPUT(label='TES pipe losses are based on custom lengths and coeffs', units='-', type='NUMBER', group='controller', required='*')
    k_tes_loss_coeffs: Matrix = INPUT(label='Minor loss coeffs for the coll, gen, and bypass loops', units='-', type='MATRIX', group='controller', required='*')
    custom_tes_pipe_sizes: float = INPUT(label='Use custom TES pipe diams, wallthks, and lengths', units='-', type='NUMBER', group='controller', required='*')
    tes_diams: Matrix = INPUT(label='Custom TES diameters', units='m', type='MATRIX', group='controller', required='*')
    tes_wallthicks: Matrix = INPUT(label='Custom TES wall thicknesses', units='m', type='MATRIX', group='controller', required='*')
    tes_lengths: Matrix = INPUT(label='Custom TES lengths', units='m', type='MATRIX', group='controller', required='*')
    DP_SGS: float = INPUT(label='Pressure drop within the steam generator', units='bar', type='NUMBER', group='controller', required='*')
    time_hr: Final[Array] = OUTPUT(label='Time at end of timestep', units='hr', type='ARRAY', group='solver', required='*')
    month: Final[Array] = OUTPUT(label='Resource Month', type='ARRAY', group='weather', required='*')
    hour_day: Final[Array] = OUTPUT(label='Resource Hour of Day', type='ARRAY', group='weather', required='*')
    solazi: Final[Array] = OUTPUT(label='Resource Solar Azimuth', units='deg', type='ARRAY', group='weather', required='*')
    solzen: Final[Array] = OUTPUT(label='Resource Solar Zenith', units='deg', type='ARRAY', group='weather', required='*')
    beam: Final[Array] = OUTPUT(label='Resource Beam normal irradiance', units='W/m2', type='ARRAY', group='weather', required='*')
    tdry: Final[Array] = OUTPUT(label='Resource Dry bulb temperature', units='C', type='ARRAY', group='weather', required='*')
    twet: Final[Array] = OUTPUT(label='Resource Wet bulb temperature', units='C', type='ARRAY', group='weather', required='*')
    rh: Final[Array] = OUTPUT(label='Resource Relative Humidity', units='%', type='ARRAY', group='weather', required='*')
    wspd: Final[Array] = OUTPUT(label='Resource Wind Speed', units='m/s', type='ARRAY', group='weather', required='*')
    pres: Final[Array] = OUTPUT(label='Resource Pressure', units='mbar', type='ARRAY', group='weather', required='*')
    defocus: Final[Array] = OUTPUT(label='Field optical focus fraction', type='ARRAY', group='weather', required='*')
    Theta_ave: Final[Array] = OUTPUT(label='Field collector solar incidence angle', units='deg', type='ARRAY', group='solar_field', required='*')
    CosTh_ave: Final[Array] = OUTPUT(label='Field collector cosine efficiency', type='ARRAY', group='solar_field', required='*')
    IAM_ave: Final[Array] = OUTPUT(label='Field collector incidence angle modifier', type='ARRAY', group='solar_field', required='*')
    RowShadow_ave: Final[Array] = OUTPUT(label='Field collector row shadowing loss', type='ARRAY', group='solar_field', required='*')
    EndLoss_ave: Final[Array] = OUTPUT(label='Field collector optical end loss', type='ARRAY', group='solar_field', required='*')
    dni_costh: Final[Array] = OUTPUT(label='Field collector DNI-cosine product', units='W/m2', type='ARRAY', group='solar_field', required='*')
    EqOpteff: Final[Array] = OUTPUT(label='Field optical efficiency before defocus', type='ARRAY', group='solar_field', required='*')
    SCAs_def: Final[Array] = OUTPUT(label='Field fraction of focused SCAs', type='ARRAY', group='solar_field', required='*')
    q_inc_sf_tot: Final[Array] = OUTPUT(label='Field thermal power incident', units='MWt', type='ARRAY', group='solar_field', required='*')
    qinc_costh: Final[Array] = OUTPUT(label='Field thermal power incident after cosine', units='MWt', type='ARRAY', group='solar_field', required='*')
    q_dot_rec_inc: Final[Array] = OUTPUT(label='Receiver thermal power incident', units='MWt', type='ARRAY', group='solar_field', required='*')
    q_dot_rec_thermal_loss: Final[Array] = OUTPUT(label='Receiver thermal losses', units='MWt', type='ARRAY', group='solar_field', required='*')
    q_dot_rec_abs: Final[Array] = OUTPUT(label='Receiver thermal power absorbed', units='MWt', type='ARRAY', group='solar_field', required='*')
    q_dot_piping_loss: Final[Array] = OUTPUT(label='Field piping thermal losses', units='MWt', type='ARRAY', group='solar_field', required='*')
    e_dot_field_int_energy: Final[Array] = OUTPUT(label='Field change in material/htf internal energy', units='MWt', type='ARRAY', group='solar_field', required='*')
    q_dot_htf_sf_out: Final[Array] = OUTPUT(label='Field thermal power leaving in HTF', units='MWt', type='ARRAY', group='solar_field', required='*')
    q_dot_freeze_prot: Final[Array] = OUTPUT(label='Field freeze protection required', units='MWt', type='ARRAY', group='solar_field', required='*')
    m_dot_loop: Final[Array] = OUTPUT(label='Receiver mass flow rate', units='kg/s', type='ARRAY', group='solar_field', required='*')
    m_dot_field_recirc: Final[Array] = OUTPUT(label='Field total mass flow recirculated', units='kg/s', type='ARRAY', group='solar_field', required='*')
    m_dot_field_delivered: Final[Array] = OUTPUT(label='Field total mass flow delivered', units='kg/s', type='ARRAY', group='solar_field', required='*')
    T_field_cold_in: Final[Array] = OUTPUT(label='Field timestep-averaged inlet temperature', units='C', type='ARRAY', group='solar_field', required='*')
    T_rec_cold_in: Final[Array] = OUTPUT(label='Loop timestep-averaged inlet temperature', units='C', type='ARRAY', group='solar_field', required='*')
    T_rec_hot_out: Final[Array] = OUTPUT(label='Loop timestep-averaged outlet temperature', units='C', type='ARRAY', group='solar_field', required='*')
    T_field_hot_out: Final[Array] = OUTPUT(label='Field timestep-averaged outlet temperature', units='C', type='ARRAY', group='solar_field', required='*')
    deltaP_field: Final[Array] = OUTPUT(label='Field pressure drop', units='bar', type='ARRAY', group='solar_field', required='*')
    W_dot_sca_track: Final[Array] = OUTPUT(label='Field collector tracking power', units='MWe', type='ARRAY', group='solar_field', required='*')
    W_dot_field_pump: Final[Array] = OUTPUT(label='Field htf pumping power', units='MWe', type='ARRAY', group='solar_field', required='*')
    pipe_header_diams: Final[Array] = OUTPUT(label='Field piping header diameters', units='m', type='ARRAY', group='solar_field', required='*')
    pipe_header_wallthk: Final[Array] = OUTPUT(label='Field piping header wall thicknesses', units='m', type='ARRAY', group='solar_field', required='*')
    pipe_header_lengths: Final[Array] = OUTPUT(label='Field piping header lengths', units='m', type='ARRAY', group='solar_field', required='*')
    pipe_header_expansions: Final[Array] = OUTPUT(label='Number of field piping header expansions', units='-', type='ARRAY', group='solar_field', required='*')
    pipe_header_mdot_dsn: Final[Array] = OUTPUT(label='Field piping header mass flow at design', units='kg/s', type='ARRAY', group='solar_field', required='*')
    pipe_header_vel_dsn: Final[Array] = OUTPUT(label='Field piping header velocity at design', units='m/s', type='ARRAY', group='solar_field', required='*')
    pipe_header_T_dsn: Final[Array] = OUTPUT(label='Field piping header temperature at design', units='C', type='ARRAY', group='solar_field', required='*')
    pipe_header_P_dsn: Final[Array] = OUTPUT(label='Field piping header pressure at design', units='bar', type='ARRAY', group='solar_field', required='*')
    pipe_runner_diams: Final[Array] = OUTPUT(label='Field piping runner diameters', units='m', type='ARRAY', group='solar_field', required='*')
    pipe_runner_wallthk: Final[Array] = OUTPUT(label='Field piping runner wall thicknesses', units='m', type='ARRAY', group='solar_field', required='*')
    pipe_runner_lengths: Final[Array] = OUTPUT(label='Field piping runner lengths', units='m', type='ARRAY', group='solar_field', required='*')
    pipe_runner_expansions: Final[Array] = OUTPUT(label='Number of field piping runner expansions', units='-', type='ARRAY', group='solar_field', required='*')
    pipe_runner_mdot_dsn: Final[Array] = OUTPUT(label='Field piping runner mass flow at design', units='kg/s', type='ARRAY', group='solar_field', required='*')
    pipe_runner_vel_dsn: Final[Array] = OUTPUT(label='Field piping runner velocity at design', units='m/s', type='ARRAY', group='solar_field', required='*')
    pipe_runner_T_dsn: Final[Array] = OUTPUT(label='Field piping runner temperature at design', units='C', type='ARRAY', group='solar_field', required='*')
    pipe_runner_P_dsn: Final[Array] = OUTPUT(label='Field piping runner pressure at design', units='bar', type='ARRAY', group='solar_field', required='*')
    pipe_loop_T_dsn: Final[Array] = OUTPUT(label='Field piping loop temperature at design', units='C', type='ARRAY', group='solar_field', required='*')
    pipe_loop_P_dsn: Final[Array] = OUTPUT(label='Field piping loop pressure at design', units='bar', type='ARRAY', group='solar_field', required='*')
    eta: Final[Array] = OUTPUT(label='PC efficiency: gross', type='ARRAY', group='powerblock', required='*')
    q_pb: Final[Array] = OUTPUT(label='PC input energy', units='MWt', type='ARRAY', group='powerblock', required='*')
    m_dot_pc: Final[Array] = OUTPUT(label='PC HTF mass flow rate', units='kg/s', type='ARRAY', group='powerblock', required='*')
    q_dot_pc_startup: Final[Array] = OUTPUT(label='PC startup thermal power', units='MWt', type='ARRAY', group='powerblock', required='*')
    P_cycle: Final[Array] = OUTPUT(label='PC electrical power output: gross', units='MWe', type='ARRAY', group='powerblock', required='*')
    T_pc_in: Final[Array] = OUTPUT(label='PC HTF inlet temperature', units='C', type='ARRAY', group='powerblock', required='*')
    T_pc_out: Final[Array] = OUTPUT(label='PC HTF outlet temperature', units='C', type='ARRAY', group='powerblock', required='*')
    m_dot_water_pc: Final[Array] = OUTPUT(label='PC water consumption: makeup + cooling', units='kg/s', type='ARRAY', group='powerblock', required='*')
    q_pc_startup: Final[Array] = OUTPUT(label='PC startup thermal energy', units='MWht', type='ARRAY', group='powerblock', required='*')
    tank_losses: Final[Array] = OUTPUT(label='TES thermal losses', units='MWt', type='ARRAY', group='TES', required='*')
    q_tes_heater: Final[Array] = OUTPUT(label='TES freeze protection power', units='MWe', type='ARRAY', group='TES', required='*')
    T_tes_hot: Final[Array] = OUTPUT(label='TES hot temperature', units='C', type='ARRAY', group='TES', required='*')
    T_tes_cold: Final[Array] = OUTPUT(label='TES cold temperature', units='C', type='ARRAY', group='TES', required='*')
    q_dc_tes: Final[Array] = OUTPUT(label='TES discharge thermal power', units='MWt', type='ARRAY', group='TES', required='*')
    q_ch_tes: Final[Array] = OUTPUT(label='TES charge thermal power', units='MWt', type='ARRAY', group='TES', required='*')
    e_ch_tes: Final[Array] = OUTPUT(label='TES charge state', units='MWht', type='ARRAY', group='TES', required='*')
    m_dot_tes_dc: Final[Array] = OUTPUT(label='TES discharge mass flow rate', units='kg/s', type='ARRAY', group='TES', required='*')
    m_dot_tes_ch: Final[Array] = OUTPUT(label='TES charge mass flow rate', units='kg/s', type='ARRAY', group='TES', required='*')
    op_mode_1: Final[Array] = OUTPUT(label='1st operating mode', type='ARRAY', group='solver', required='*')
    op_mode_2: Final[Array] = OUTPUT(label='2nd op. mode, if applicable', type='ARRAY', group='solver', required='*')
    op_mode_3: Final[Array] = OUTPUT(label='3rd op. mode, if applicable', type='ARRAY', group='solver', required='*')
    m_dot_balance: Final[Array] = OUTPUT(label='Relative mass flow balance error', type='ARRAY', group='solver', required='*')
    q_balance: Final[Array] = OUTPUT(label='Relative energy balance error', type='ARRAY', group='solver', required='*')
    monthly_energy: Final[Array] = OUTPUT(label='Monthly Energy', units='kWh', type='ARRAY', group='Post-process', required='*', constraints='LENGTH=12')
    annual_energy: Final[float] = OUTPUT(label='Annual Net Electrical Energy Production w/ avail derate', units='kWe-hr', type='NUMBER', group='Post-process', required='*')
    annual_thermal_consumption: Final[float] = OUTPUT(label='Annual thermal freeze protection required', units='kWt-hr', type='NUMBER', group='Post-process', required='*')
    annual_total_water_use: Final[float] = OUTPUT(label='Total Annual Water Usage', units='m^3', type='NUMBER', group='Post-process', required='*')
    annual_field_freeze_protection: Final[float] = OUTPUT(label='Annual thermal power for field freeze protection', units='kWt-hr', type='NUMBER', group='Post-process', required='*')
    annual_tes_freeze_protection: Final[float] = OUTPUT(label='Annual thermal power for TES freeze protection', units='kWt-hr', type='NUMBER', group='Post-process', required='*')
    n_op_modes: Final[Array] = OUTPUT(label='Operating modes in reporting timestep', type='ARRAY', group='solver', required='*')
    tou_value: Final[Array] = OUTPUT(label='CSP operating Time-of-use value', type='ARRAY', group='solver', required='*')
    pricing_mult: Final[Array] = OUTPUT(label='PPA price multiplier', type='ARRAY', group='solver', required='*')
    q_dot_pc_sb: Final[Array] = OUTPUT(label='Thermal power for PC standby', units='MWt', type='ARRAY', group='solver', required='*')
    q_dot_pc_min: Final[Array] = OUTPUT(label='Thermal power for PC min operation', units='MWt', type='ARRAY', group='solver', required='*')
    q_dot_pc_target: Final[Array] = OUTPUT(label='Target thermal power to PC', units='MWt', type='ARRAY', group='solver', required='*')
    q_dot_pc_max: Final[Array] = OUTPUT(label='Max thermal power to PC', units='MWt', type='ARRAY', group='solver', required='*')
    is_rec_su_allowed: Final[Array] = OUTPUT(label='is receiver startup allowed', type='ARRAY', group='solver', required='*')
    is_pc_su_allowed: Final[Array] = OUTPUT(label='is power cycle startup allowed', type='ARRAY', group='solver', required='*')
    is_pc_sb_allowed: Final[Array] = OUTPUT(label='is power cycle standby allowed', type='ARRAY', group='solver', required='*')
    q_dot_est_cr_su: Final[Array] = OUTPUT(label='Estimate rec. startup thermal power', units='MWt', type='ARRAY', group='solver', required='*')
    q_dot_est_cr_on: Final[Array] = OUTPUT(label='Estimate rec. thermal power TO HTF', units='MWt', type='ARRAY', group='solver', required='*')
    q_dot_est_tes_dc: Final[Array] = OUTPUT(label='Estimate max TES discharge thermal power', units='MWt', type='ARRAY', group='solver', required='*')
    q_dot_est_tes_ch: Final[Array] = OUTPUT(label='Estimate max TES charge thermal power', units='MWt', type='ARRAY', group='solver', required='*')
    operating_modes_a: Final[Array] = OUTPUT(label='First 3 operating modes tried', type='ARRAY', group='solver', required='*')
    operating_modes_b: Final[Array] = OUTPUT(label='Next 3 operating modes tried', type='ARRAY', group='solver', required='*')
    operating_modes_c: Final[Array] = OUTPUT(label='Final 3 operating modes tried', type='ARRAY', group='solver', required='*')
    disp_solve_state: Final[Array] = OUTPUT(label='Dispatch solver state', type='ARRAY', group='tou', required='*')
    disp_solve_iter: Final[Array] = OUTPUT(label='Dispatch iterations count', type='ARRAY', group='tou', required='*')
    disp_objective: Final[Array] = OUTPUT(label='Dispatch objective function value', type='ARRAY', group='tou', required='*')
    disp_obj_relax: Final[Array] = OUTPUT(label='Dispatch objective function - relaxed max', type='ARRAY', group='tou', required='*')
    disp_qsf_expected: Final[Array] = OUTPUT(label='Dispatch expected solar field available energy', units='MWt', type='ARRAY', group='tou', required='*')
    disp_qsfprod_expected: Final[Array] = OUTPUT(label='Dispatch expected solar field generation', units='MWt', type='ARRAY', group='tou', required='*')
    disp_qsfsu_expected: Final[Array] = OUTPUT(label='Dispatch expected solar field startup enegy', units='MWt', type='ARRAY', group='tou', required='*')
    disp_tes_expected: Final[Array] = OUTPUT(label='Dispatch expected TES charge level', units='MWht', type='ARRAY', group='tou', required='*')
    disp_pceff_expected: Final[Array] = OUTPUT(label='Dispatch expected power cycle efficiency adj.', type='ARRAY', group='tou', required='*')
    disp_thermeff_expected: Final[Array] = OUTPUT(label='Dispatch expected SF thermal efficiency adj.', type='ARRAY', group='tou', required='*')
    disp_qpbsu_expected: Final[Array] = OUTPUT(label='Dispatch expected power cycle startup energy', units='MWht', type='ARRAY', group='tou', required='*')
    disp_wpb_expected: Final[Array] = OUTPUT(label='Dispatch expected power generation', units='MWe', type='ARRAY', group='tou', required='*')
    disp_rev_expected: Final[Array] = OUTPUT(label='Dispatch expected revenue factor', type='ARRAY', group='tou', required='*')
    disp_presolve_nconstr: Final[Array] = OUTPUT(label='Dispatch number of constraints in problem', type='ARRAY', group='tou', required='*')
    disp_presolve_nvar: Final[Array] = OUTPUT(label='Dispatch number of variables in problem', type='ARRAY', group='tou', required='*')
    disp_solve_time: Final[Array] = OUTPUT(label='Dispatch solver time', units='sec', type='ARRAY', group='tou', required='*')
    htf_pump_power: Final[Array] = OUTPUT(label='Parasitic power TES and Cycle HTF pump', units='MWe', type='ARRAY', group='system', required='*')
    P_cooling_tower_tot: Final[Array] = OUTPUT(label='Parasitic power condenser operation', units='MWe', type='ARRAY', group='system', required='*')
    P_fixed: Final[Array] = OUTPUT(label='Parasitic power fixed load', units='MWe', type='ARRAY', group='system', required='*')
    P_plant_balance_tot: Final[Array] = OUTPUT(label='Parasitic power generation-dependent load', units='MWe', type='ARRAY', group='system', required='*')
    P_out_net: Final[Array] = OUTPUT(label='Total electric power to grid', units='MWe', type='ARRAY', group='system', required='*')
    gen: Final[Array] = OUTPUT(label='Total electric power to grid w/ avail. derate', units='kWe', type='ARRAY', group='system', required='*')
    annual_W_cycle_gross: Final[float] = OUTPUT(label='Electrical source - Power cycle gross output', units='kWhe', type='NUMBER', group='system', required='*')
    conversion_factor: Final[float] = OUTPUT(label='Gross to Net Conversion Factor', units='%', type='NUMBER', group='system', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', group='system', required='*')
    kwh_per_kw: Final[float] = OUTPUT(label='First year kWh/kW', units='kWh/kW', type='NUMBER', group='system', required='*')
    recirculating: Final[Array] = OUTPUT(label='Field recirculating (bypass valve open)', units='-', type='ARRAY', group='solar_field', required='*')
    pipe_tes_diams: Final[Array] = OUTPUT(label='Pipe diameters in TES', units='m', type='ARRAY', group='TES', required='*')
    pipe_tes_wallthk: Final[Array] = OUTPUT(label='Pipe wall thickness in TES', units='m', type='ARRAY', group='TES', required='*')
    pipe_tes_mdot_dsn: Final[Array] = OUTPUT(label='Mass flow TES pipes at design conditions', units='kg/s', type='ARRAY', group='TES', required='*')
    pipe_tes_vel_dsn: Final[Array] = OUTPUT(label='Velocity in TES pipes at design conditions', units='m/s', type='ARRAY', group='TES', required='*')
    pipe_tes_T_dsn: Final[Array] = OUTPUT(label='Temperature in TES pipes at design conditions', units='C', type='ARRAY', group='TES', required='*')
    pipe_tes_P_dsn: Final[Array] = OUTPUT(label='Pressure in TES pipes at design conditions', units='bar', type='ARRAY', group='TES', required='*')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Adjustment Factors', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly Adjustment Factors', units='%', type='ARRAY', group='Adjustment Factors', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based Adjustment Factors', units='%', type='MATRIX', group='Adjustment Factors', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')

    def __init__(self, *args: Mapping[str, Any],
                 file_name: str = ...,
                 nSCA: float = ...,
                 nHCEt: float = ...,
                 nColt: float = ...,
                 nHCEVar: float = ...,
                 nLoops: float = ...,
                 FieldConfig: float = ...,
                 include_fixed_power_block_runner: float = ...,
                 L_power_block_piping: float = ...,
                 eta_pump: float = ...,
                 Fluid: float = ...,
                 accept_loc: float = ...,
                 HDR_rough: float = ...,
                 theta_stow: float = ...,
                 theta_dep: float = ...,
                 Row_Distance: float = ...,
                 T_loop_in_des: float = ...,
                 T_loop_out: float = ...,
                 m_dot_htfmin: float = ...,
                 m_dot_htfmax: float = ...,
                 field_fl_props: Matrix = ...,
                 T_fp: float = ...,
                 I_bn_des: float = ...,
                 Pipe_hl_coef: float = ...,
                 SCA_drives_elec: float = ...,
                 tilt: float = ...,
                 azimuth: float = ...,
                 wind_stow_speed: float = ...,
                 accept_mode: float = ...,
                 accept_init: float = ...,
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
                 rec_su_delay: float = ...,
                 rec_qf_delay: float = ...,
                 p_start: float = ...,
                 pc_config: float = ...,
                 P_ref: float = ...,
                 eta_ref: float = ...,
                 cycle_max_frac: float = ...,
                 cycle_cutoff_frac: float = ...,
                 q_sby_frac: float = ...,
                 startup_time: float = ...,
                 startup_frac: float = ...,
                 pb_pump_coef: float = ...,
                 dT_cw_ref: float = ...,
                 T_amb_des: float = ...,
                 P_boil: float = ...,
                 CT: float = ...,
                 tech_type: float = ...,
                 T_approach: float = ...,
                 T_ITD_des: float = ...,
                 P_cond_ratio: float = ...,
                 pb_bd_frac: float = ...,
                 P_cond_min: float = ...,
                 n_pl_inc: float = ...,
                 F_wc: Array = ...,
                 ud_f_W_dot_cool_des: float = ...,
                 ud_m_dot_water_cool_des: float = ...,
                 ud_ind_od: Matrix = ...,
                 store_fluid: float = ...,
                 store_fl_props: Matrix = ...,
                 is_hx: float = ...,
                 tshours: float = ...,
                 h_tank: float = ...,
                 u_tank: float = ...,
                 tank_pairs: float = ...,
                 hot_tank_Thtr: float = ...,
                 hot_tank_max_heat: float = ...,
                 cold_tank_Thtr: float = ...,
                 cold_tank_max_heat: float = ...,
                 dt_hot: float = ...,
                 h_tank_min: float = ...,
                 init_hot_htf_percent: float = ...,
                 weekday_schedule: Matrix = ...,
                 weekend_schedule: Matrix = ...,
                 dispatch_sched_weekday: Matrix = ...,
                 dispatch_sched_weekend: Matrix = ...,
                 is_tod_pc_target_also_pc_max: float = ...,
                 is_dispatch: float = ...,
                 is_write_ampl_dat: float = ...,
                 is_ampl_engine: float = ...,
                 ampl_data_dir: str = ...,
                 ampl_exec_call: str = ...,
                 disp_frequency: float = ...,
                 disp_steps_per_hour: float = ...,
                 disp_horizon: float = ...,
                 disp_max_iter: float = ...,
                 disp_timeout: float = ...,
                 disp_mip_gap: float = ...,
                 disp_spec_presolve: float = ...,
                 disp_spec_bb: float = ...,
                 disp_reporting: float = ...,
                 disp_spec_scaling: float = ...,
                 disp_time_weighting: float = ...,
                 disp_rsu_cost: float = ...,
                 disp_csu_cost: float = ...,
                 disp_pen_delta_w: float = ...,
                 q_rec_standby: float = ...,
                 q_rec_heattrace: float = ...,
                 is_wlim_series: float = ...,
                 wlim_series: Array = ...,
                 f_turb_tou_periods: Array = ...,
                 ppa_multiplier_model: float = ...,
                 dispatch_factors_ts: Array = ...,
                 dispatch_factor1: float = ...,
                 dispatch_factor2: float = ...,
                 dispatch_factor3: float = ...,
                 dispatch_factor4: float = ...,
                 dispatch_factor5: float = ...,
                 dispatch_factor6: float = ...,
                 dispatch_factor7: float = ...,
                 dispatch_factor8: float = ...,
                 dispatch_factor9: float = ...,
                 is_dispatch_series: float = ...,
                 dispatch_series: Array = ...,
                 pb_fixed_par: float = ...,
                 bop_array: Array = ...,
                 aux_array: Array = ...,
                 gross_net_conversion_factor: float = ...,
                 water_usage_per_wash: float = ...,
                 washing_frequency: float = ...,
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
                 K_cpnt: Matrix = ...,
                 D_cpnt: Matrix = ...,
                 L_cpnt: Matrix = ...,
                 Type_cpnt: Matrix = ...,
                 custom_sf_pipe_sizes: float = ...,
                 sf_rnr_diams: Matrix = ...,
                 sf_rnr_wallthicks: Matrix = ...,
                 sf_rnr_lengths: Matrix = ...,
                 sf_hdr_diams: Matrix = ...,
                 sf_hdr_wallthicks: Matrix = ...,
                 sf_hdr_lengths: Matrix = ...,
                 tanks_in_parallel: float = ...,
                 has_hot_tank_bypass: float = ...,
                 T_tank_hot_inlet_min: float = ...,
                 tes_pump_coef: float = ...,
                 V_tes_des: float = ...,
                 custom_tes_p_loss: float = ...,
                 k_tes_loss_coeffs: Matrix = ...,
                 custom_tes_pipe_sizes: float = ...,
                 tes_diams: Matrix = ...,
                 tes_wallthicks: Matrix = ...,
                 tes_lengths: Matrix = ...,
                 DP_SGS: float = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
