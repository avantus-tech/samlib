
# This is a generated file

"""trough_physical_csp_solver - Physical trough using CSP Solver"""

# VERSION: 1

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
        'file_name': str,
        'track_mode': float,
        'tilt': float,
        'azimuth': float,
        'system_capacity': float,
        'ppa_multiplier_model': float,
        'dispatch_factors_ts': Array,
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
        'V_hdr_max': float,
        'V_hdr_min': float,
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
        'q_pb_design': float,
        'W_pb_design': float,
        'cycle_max_frac': float,
        'cycle_cutoff_frac': float,
        'pb_pump_coef': float,
        'tes_pump_coef': float,
        'pb_fixed_par': float,
        'bop_array': Array,
        'aux_array': Array,
        'fossil_mode': float,
        'q_sby_frac': float,
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
        'time_hr': Array,
        'solzen': Array,
        'beam': Array,
        'eta_map_out': Matrix,
        'flux_maps_out': Matrix,
        'defocus': Array,
        'Q_thermal': Array,
        'm_dot_rec': Array,
        'q_pb': Array,
        'm_dot_pc': Array,
        'q_pc_startup': Array,
        'q_dot_pc_startup': Array,
        'tank_losses': Array,
        'q_heater': Array,
        'T_tes_hot': Array,
        'T_tes_cold': Array,
        'q_dc_tes': Array,
        'q_ch_tes': Array,
        'e_ch_tes': Array,
        'm_dot_tes_dc': Array,
        'm_dot_tes_ch': Array,
        'pparasi': Array,
        'P_tower_pump': Array,
        'htf_pump_power': Array,
        'P_cooling_tower_tot': Array,
        'P_fixed': Array,
        'P_plant_balance_tot': Array,
        'P_out_net': Array,
        'tou_value': Array,
        'pricing_mult': Array,
        'n_op_modes': Array,
        'op_mode_1': Array,
        'op_mode_2': Array,
        'op_mode_3': Array,
        'm_dot_balance': Array,
        'q_balance': Array,
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
        'q_dot_pc_sb': Array,
        'q_dot_pc_min': Array,
        'q_dot_pc_max': Array,
        'q_dot_pc_target': Array,
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
        'gen': Array,
        'annual_energy': float,
        'annual_W_cycle_gross': float,
        'conversion_factor': float,
        'capacity_factor': float,
        'kwh_per_kw': float,
        'annual_total_water_use': float,
        'disp_objective_ann': float,
        'disp_iter_ann': float,
        'disp_presolve_nconstr_ann': float,
        'disp_presolve_nvar_ann': float,
        'disp_solve_time_ann': float,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix
    }, total=False)

class Data(ssc.DataDict):
    file_name: str = INPUT(label='Local weather file with path', units='none', type='STRING', group='Weather', required='*', constraints='LOCAL_FILE')
    track_mode: float = INPUT(label='Tracking mode', units='none', type='NUMBER', group='Weather', required='*')
    tilt: float = INPUT(label='Tilt angle of surface/axis', units='none', type='NUMBER', group='Weather', required='*')
    azimuth: float = INPUT(label='Azimuth angle of surface/axis', units='none', type='NUMBER', group='Weather', required='*')
    system_capacity: float = INPUT(label='Nameplate capacity', units='kW', type='NUMBER', group='trough', required='*')
    ppa_multiplier_model: float = INPUT(label='PPA multiplier model', units='0/1', type='NUMBER', group='Time of Delivery', required='?=0', constraints='INTEGER,MIN=0', meta='0=diurnal,1=timestep')
    dispatch_factors_ts: Array = INPUT(label='Dispatch payment factor array', type='ARRAY', group='Time of Delivery', required='ppa_multiplier_model=1')
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
    T_fp: float = INPUT(label='Freeze protection temperature (heat trace activation temperature)', units='none', type='NUMBER', group='solar_field', required='*')
    I_bn_des: float = INPUT(label='Solar irradiation at design', units='C', type='NUMBER', group='solar_field', required='*')
    V_hdr_max: float = INPUT(label='Maximum HTF velocity in the header at design', units='W/m2', type='NUMBER', group='solar_field', required='*')
    V_hdr_min: float = INPUT(label='Minimum HTF velocity in the header at design', units='m/s', type='NUMBER', group='solar_field', required='*')
    Pipe_hl_coef: float = INPUT(label='Loss coefficient from the header, runner pipe, and non-HCE piping', units='m/s', type='NUMBER', group='solar_field', required='*')
    SCA_drives_elec: float = INPUT(label='Tracking power, in Watts per SCA drive', units='W/m2-K', type='NUMBER', group='solar_field', required='*')
    fthrok: float = INPUT(label='Flag to allow partial defocusing of the collectors', units='W/SCA', type='NUMBER', group='solar_field', required='*', constraints='INTEGER')
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
    Rough: Matrix = INPUT(label='Roughness of the internal surface ', units='m', type='MATRIX', group='solar_field', required='*')
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
    q_pb_design: float = INPUT(label='Design heat input to power block', units='MWt', type='NUMBER', group='controller', required='*')
    W_pb_design: float = INPUT(label='Rated plant capacity', units='MWe', type='NUMBER', group='controller', required='*')
    cycle_max_frac: float = INPUT(label='Maximum turbine over design operation fraction', units='-', type='NUMBER', group='controller', required='*')
    cycle_cutoff_frac: float = INPUT(label='Minimum turbine operation fraction before shutdown', units='-', type='NUMBER', group='controller', required='*')
    pb_pump_coef: float = INPUT(label='Pumping power to move 1kg of HTF through PB loop', units='kW/kg', type='NUMBER', group='controller', required='*')
    tes_pump_coef: float = INPUT(label='Pumping power to move 1kg of HTF through tes loop', units='kW/kg', type='NUMBER', group='controller', required='*')
    pb_fixed_par: float = INPUT(label='Fraction of rated gross power constantly consumed', units='-', type='NUMBER', group='controller', required='*')
    bop_array: Array = INPUT(label='Coefficients for balance of plant parasitics calcs', units='-', type='ARRAY', group='controller', required='*')
    aux_array: Array = INPUT(label='Coefficients for auxiliary heater parasitics calcs', units='-', type='ARRAY', group='controller', required='*')
    fossil_mode: float = INPUT(label='Fossil backup mode 1=Normal 2=Topping', units='-', type='NUMBER', group='controller', required='*', constraints='INTEGER')
    q_sby_frac: float = INPUT(label='Fraction of thermal power required for standby', units='-', type='NUMBER', group='controller', required='*')
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
    ud_T_htf_ind_od: Matrix = INPUT(label='Off design table of user-defined power cycle performance formed from parametric on T_htf_hot [C]', type='MATRIX', group='user_defined_PC', required='pc_config=1')
    ud_T_amb_ind_od: Matrix = INPUT(label='Off design table of user-defined power cycle performance formed from parametric on T_amb [C]', type='MATRIX', group='user_defined_PC', required='pc_config=1')
    ud_m_dot_htf_ind_od: Matrix = INPUT(label='Off design table of user-defined power cycle performance formed from parametric on m_dot_htf [ND]', type='MATRIX', group='user_defined_PC', required='pc_config=1')
    ud_ind_od: Matrix = INPUT(label='Off design user-defined power cycle performance as function of T_htf, m_dot_htf [ND], and T_amb', type='MATRIX', group='user_defined_PC', required='pc_config=1')
    eta_lhv: float = INPUT(label='Fossil fuel lower heating value - Thermal power generated per unit fuel', units='MW/MMBTU', type='NUMBER', group='enet', required='*')
    eta_tes_htr: float = INPUT(label='Thermal storage tank heater efficiency (fp_mode=1 only)', units='none', type='NUMBER', group='enet', required='*')
    time_hr: Final[Array] = OUTPUT(label='Time at end of timestep', units='hr', type='ARRAY', group='Solver')
    solzen: Final[Array] = OUTPUT(label='Resource Solar Zenith', units='deg', type='ARRAY', group='weather')
    beam: Final[Array] = OUTPUT(label='Resource Beam normal irradiance', units='W/m2', type='ARRAY', group='weather')
    eta_map_out: Final[Matrix] = OUTPUT(label='Solar field optical efficiencies', type='MATRIX', group='heliostat')
    flux_maps_out: Final[Matrix] = OUTPUT(label='Flux map intensities', type='MATRIX', group='heliostat')
    defocus: Final[Array] = OUTPUT(label='Field optical focus fraction', type='ARRAY', group='Controller')
    Q_thermal: Final[Array] = OUTPUT(label='Rec. thermal power to HTF less piping loss', units='MWt', type='ARRAY', group='CR')
    m_dot_rec: Final[Array] = OUTPUT(label='Rec. mass flow rate', units='kg/hr', type='ARRAY', group='CR')
    q_pb: Final[Array] = OUTPUT(label='PC input energy', units='MWt', type='ARRAY', group='PC')
    m_dot_pc: Final[Array] = OUTPUT(label='PC HTF mass flow rate', units='kg/hr', type='ARRAY', group='PC')
    q_pc_startup: Final[Array] = OUTPUT(label='PC startup thermal energy', units='MWht', type='ARRAY', group='PC')
    q_dot_pc_startup: Final[Array] = OUTPUT(label='PC startup thermal power', units='MWt', type='ARRAY', group='PC')
    tank_losses: Final[Array] = OUTPUT(label='TES thermal losses', units='MWt', type='ARRAY', group='TES')
    q_heater: Final[Array] = OUTPUT(label='TES freeze protection power', units='MWe', type='ARRAY', group='TES')
    T_tes_hot: Final[Array] = OUTPUT(label='TES hot temperature', units='C', type='ARRAY', group='TES')
    T_tes_cold: Final[Array] = OUTPUT(label='TES cold temperature', units='C', type='ARRAY', group='TES')
    q_dc_tes: Final[Array] = OUTPUT(label='TES discharge thermal power', units='MWt', type='ARRAY', group='TES')
    q_ch_tes: Final[Array] = OUTPUT(label='TES charge thermal power', units='MWt', type='ARRAY', group='TES')
    e_ch_tes: Final[Array] = OUTPUT(label='TES charge state', units='MWht', type='ARRAY', group='TES')
    m_dot_tes_dc: Final[Array] = OUTPUT(label='TES discharge mass flow rate', units='kg/hr', type='ARRAY', group='TES')
    m_dot_tes_ch: Final[Array] = OUTPUT(label='TES charge mass flow rate', units='kg/hr', type='ARRAY', group='TES')
    pparasi: Final[Array] = OUTPUT(label='Parasitic power heliostat drives', units='MWe', type='ARRAY', group='CR')
    P_tower_pump: Final[Array] = OUTPUT(label='Parasitic power receiver/tower HTF pump', units='MWe', type='ARRAY', group='CR')
    htf_pump_power: Final[Array] = OUTPUT(label='Parasitic power TES and Cycle HTF pump', units='MWe', type='ARRAY', group='PC-TES')
    P_cooling_tower_tot: Final[Array] = OUTPUT(label='Parasitic power condenser operation', units='MWe', type='ARRAY', group='PC')
    P_fixed: Final[Array] = OUTPUT(label='Parasitic power fixed load', units='MWe', type='ARRAY', group='System')
    P_plant_balance_tot: Final[Array] = OUTPUT(label='Parasitic power generation-dependent load', units='MWe', type='ARRAY', group='System')
    P_out_net: Final[Array] = OUTPUT(label='Total electric power to grid', units='MWe', type='ARRAY', group='System')
    tou_value: Final[Array] = OUTPUT(label='CSP operating Time-of-use value', type='ARRAY', group='Controller')
    pricing_mult: Final[Array] = OUTPUT(label='PPA price multiplier', type='ARRAY', group='Controller')
    n_op_modes: Final[Array] = OUTPUT(label='Operating modes in reporting timestep', type='ARRAY', group='Solver')
    op_mode_1: Final[Array] = OUTPUT(label='1st operating mode', type='ARRAY', group='Solver')
    op_mode_2: Final[Array] = OUTPUT(label='2nd op. mode, if applicable', type='ARRAY', group='Solver')
    op_mode_3: Final[Array] = OUTPUT(label='3rd op. mode, if applicable', type='ARRAY', group='Solver')
    m_dot_balance: Final[Array] = OUTPUT(label='Relative mass flow balance error', type='ARRAY', group='Controller')
    q_balance: Final[Array] = OUTPUT(label='Relative energy balance error', type='ARRAY', group='Controller')
    disp_solve_state: Final[Array] = OUTPUT(label='Dispatch solver state', type='ARRAY', group='tou')
    disp_solve_iter: Final[Array] = OUTPUT(label='Dispatch iterations count', type='ARRAY', group='tou')
    disp_objective: Final[Array] = OUTPUT(label='Dispatch objective function value', type='ARRAY', group='tou')
    disp_obj_relax: Final[Array] = OUTPUT(label='Dispatch objective function - relaxed max', type='ARRAY', group='tou')
    disp_qsf_expected: Final[Array] = OUTPUT(label='Dispatch expected solar field available energy', units='MWt', type='ARRAY', group='tou')
    disp_qsfprod_expected: Final[Array] = OUTPUT(label='Dispatch expected solar field generation', units='MWt', type='ARRAY', group='tou')
    disp_qsfsu_expected: Final[Array] = OUTPUT(label='Dispatch expected solar field startup enegy', units='MWt', type='ARRAY', group='tou')
    disp_tes_expected: Final[Array] = OUTPUT(label='Dispatch expected TES charge level', units='MWht', type='ARRAY', group='tou')
    disp_pceff_expected: Final[Array] = OUTPUT(label='Dispatch expected power cycle efficiency adj.', type='ARRAY', group='tou')
    disp_thermeff_expected: Final[Array] = OUTPUT(label='Dispatch expected SF thermal efficiency adj.', type='ARRAY', group='tou')
    disp_qpbsu_expected: Final[Array] = OUTPUT(label='Dispatch expected power cycle startup energy', units='MWht', type='ARRAY', group='tou')
    disp_wpb_expected: Final[Array] = OUTPUT(label='Dispatch expected power generation', units='MWe', type='ARRAY', group='tou')
    disp_rev_expected: Final[Array] = OUTPUT(label='Dispatch expected revenue factor', type='ARRAY', group='tou')
    disp_presolve_nconstr: Final[Array] = OUTPUT(label='Dispatch number of constraints in problem', type='ARRAY', group='tou')
    disp_presolve_nvar: Final[Array] = OUTPUT(label='Dispatch number of variables in problem', type='ARRAY', group='tou')
    disp_solve_time: Final[Array] = OUTPUT(label='Dispatch solver time', units='sec', type='ARRAY', group='tou')
    q_dot_pc_sb: Final[Array] = OUTPUT(label='Thermal power for PC standby', units='MWt', type='ARRAY', group='Controller')
    q_dot_pc_min: Final[Array] = OUTPUT(label='Thermal power for PC min operation', units='MWt', type='ARRAY', group='Controller')
    q_dot_pc_max: Final[Array] = OUTPUT(label='Max thermal power to PC', units='MWt', type='ARRAY', group='Controller')
    q_dot_pc_target: Final[Array] = OUTPUT(label='Target thermal power to PC', units='MWt', type='ARRAY', group='Controller')
    is_rec_su_allowed: Final[Array] = OUTPUT(label='is receiver startup allowed', type='ARRAY', group='Controller')
    is_pc_su_allowed: Final[Array] = OUTPUT(label='is power cycle startup allowed', type='ARRAY', group='Controller')
    is_pc_sb_allowed: Final[Array] = OUTPUT(label='is power cycle standby allowed', type='ARRAY', group='Controller')
    q_dot_est_cr_su: Final[Array] = OUTPUT(label='Estimate rec. startup thermal power', units='MWt', type='ARRAY', group='Controller')
    q_dot_est_cr_on: Final[Array] = OUTPUT(label='Estimate rec. thermal power TO HTF', units='MWt', type='ARRAY', group='Controller')
    q_dot_est_tes_dc: Final[Array] = OUTPUT(label='Estimate max TES discharge thermal power', units='MWt', type='ARRAY', group='Controller')
    q_dot_est_tes_ch: Final[Array] = OUTPUT(label='Estimate max TES charge thermal power', units='MWt', type='ARRAY', group='Controller')
    operating_modes_a: Final[Array] = OUTPUT(label='First 3 operating modes tried', type='ARRAY', group='Solver')
    operating_modes_b: Final[Array] = OUTPUT(label='Next 3 operating modes tried', type='ARRAY', group='Solver')
    operating_modes_c: Final[Array] = OUTPUT(label='Final 3 operating modes tried', type='ARRAY', group='Solver')
    gen: Final[Array] = OUTPUT(label='Total electric power to grid w/ avail. derate', units='kWe', type='ARRAY', group='System')
    annual_energy: Final[float] = OUTPUT(label='Annual total electric power to grid', units='kWhe', type='NUMBER', group='System')
    annual_W_cycle_gross: Final[float] = OUTPUT(label='Electrical source - Power cycle gross output', units='kWhe', type='NUMBER', group='PC')
    conversion_factor: Final[float] = OUTPUT(label='Gross to Net Conversion Factor', units='%', type='NUMBER', group='PostProcess')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', group='PostProcess')
    kwh_per_kw: Final[float] = OUTPUT(label='First year kWh/kW', units='kWh/kW', type='NUMBER')
    annual_total_water_use: Final[float] = OUTPUT(label='Total Annual Water Usage: cycle + mirror washing', units='m3', type='NUMBER', group='PostProcess')
    disp_objective_ann: Final[float] = OUTPUT(label='Annual sum of dispatch objective func. value', type='NUMBER')
    disp_iter_ann: Final[float] = OUTPUT(label='Annual sum of dispatch solver iterations', type='NUMBER')
    disp_presolve_nconstr_ann: Final[float] = OUTPUT(label='Annual sum of dispatch problem constraint count', type='NUMBER')
    disp_presolve_nvar_ann: Final[float] = OUTPUT(label='Annual sum of dispatch problem variable count', type='NUMBER')
    disp_solve_time_ann: Final[float] = OUTPUT(label='Annual sum of dispatch solver time', type='NUMBER')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')

    def __init__(self, *args: Mapping[str, Any],
                 file_name: str = ...,
                 track_mode: float = ...,
                 tilt: float = ...,
                 azimuth: float = ...,
                 system_capacity: float = ...,
                 ppa_multiplier_model: float = ...,
                 dispatch_factors_ts: Array = ...,
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
                 V_hdr_max: float = ...,
                 V_hdr_min: float = ...,
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
                 q_pb_design: float = ...,
                 W_pb_design: float = ...,
                 cycle_max_frac: float = ...,
                 cycle_cutoff_frac: float = ...,
                 pb_pump_coef: float = ...,
                 tes_pump_coef: float = ...,
                 pb_fixed_par: float = ...,
                 bop_array: Array = ...,
                 aux_array: Array = ...,
                 fossil_mode: float = ...,
                 q_sby_frac: float = ...,
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
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
