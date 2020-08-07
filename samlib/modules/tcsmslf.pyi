
# This is a generated file

"""tcsmslf - CSP model using the molten salt linear fresnel TCS types."""

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
        'weekday_schedule': Matrix,
        'weekend_schedule': Matrix,
        'nMod': float,
        'nRecVar': float,
        'nLoops': float,
        'eta_pump': float,
        'HDR_rough': float,
        'theta_stow': float,
        'theta_dep': float,
        'FieldConfig': float,
        'T_startup': float,
        'pb_rated_cap': float,
        'm_dot_htfmin': float,
        'm_dot_htfmax': float,
        'T_loop_in_des': float,
        'T_loop_out': float,
        'Fluid': float,
        'T_field_ini': float,
        'field_fl_props': Matrix,
        'T_fp': float,
        'I_bn_des': float,
        'V_hdr_max': float,
        'V_hdr_min': float,
        'Pipe_hl_coef': float,
        'SCA_drives_elec': float,
        'fthrok': float,
        'fthrctrl': float,
        'ColAz': float,
        'solar_mult': float,
        'mc_bal_hot': float,
        'mc_bal_cold': float,
        'mc_bal_sca': float,
        'water_per_wash': float,
        'washes_per_year': float,
        'opt_model': float,
        'A_aperture': float,
        'reflectivity': float,
        'TrackingError': float,
        'GeomEffects': float,
        'Dirt_mirror': float,
        'Error': float,
        'L_mod': float,
        'IAM_T_coefs': Array,
        'IAM_L_coefs': Array,
        'OpticalTable': Matrix,
        'rec_model': float,
        'HCE_FieldFrac': Array,
        'D_abs_in': Array,
        'D_abs_out': Array,
        'D_glass_in': Array,
        'D_glass_out': Array,
        'D_plug': Array,
        'Flow_type': Array,
        'Rough': Array,
        'alpha_env': Array,
        'epsilon_abs_1': Matrix,
        'epsilon_abs_2': Matrix,
        'epsilon_abs_3': Matrix,
        'epsilon_abs_4': Matrix,
        'alpha_abs': Array,
        'Tau_envelope': Array,
        'epsilon_glass': Array,
        'GlazingIntactIn': Array,
        'P_a': Array,
        'AnnulusGas': Array,
        'AbsorberMaterial': Array,
        'Shadowing': Array,
        'dirt_env': Array,
        'Design_loss': Array,
        'L_mod_spacing': float,
        'L_crossover': float,
        'HL_T_coefs': Array,
        'HL_w_coefs': Array,
        'DP_nominal': float,
        'DP_coefs': Array,
        'rec_htf_vol': float,
        'T_amb_sf_des': float,
        'V_wind_des': float,
        'I_b': float,
        'T_db': float,
        'V_wind': float,
        'P_amb': float,
        'T_dp': float,
        'T_cold_in': float,
        'defocus': float,
        'field_fluid': float,
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
        'T_tank_hot_ini': float,
        'T_tank_cold_ini': float,
        'vol_tank': float,
        'h_tank': float,
        'h_tank_min': float,
        'u_tank': float,
        'tank_pairs': float,
        'cold_tank_Thtr': float,
        'hot_tank_Thtr': float,
        'tank_max_heat': float,
        'T_field_in_des': float,
        'T_field_out_des': float,
        'q_pb_design': float,
        'W_pb_design': float,
        'cycle_max_frac': float,
        'cycle_cutoff_frac': float,
        'solarm': float,
        'pb_pump_coef': float,
        'tes_pump_coef': float,
        'pb_fixed_par': float,
        'bop_array': Array,
        'aux_array': Array,
        'tes_temp': float,
        'fossil_mode': float,
        'fthr_ok': float,
        'nSCA': float,
        'fc_on': float,
        't_standby_reset': float,
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
        'V_tes_des': float,
        'custom_tes_p_loss': float,
        'k_tes_loss_coeffs': Array,
        'custom_sgs_pipe_sizes': float,
        'sgs_diams': Array,
        'sgs_wallthicks': Array,
        'sgs_lengths': Array,
        'DP_SGS': float,
        'tanks_in_parallel': float,
        'has_hot_tank_bypass': float,
        'T_tank_hot_inlet_min': float,
        'calc_design_pipe_vals': float,
        'pc_config': float,
        'P_ref': float,
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
        'ud_f_W_dot_cool_des': float,
        'ud_m_dot_water_cool_des': float,
        'ud_ind_od': Matrix,
        'eta_lhv': float,
        'eta_tes_htr': float,
        'fp_mode': float,
        'T_htf_hot_ref': float,
        'T_htf_cold_ref': float,
        'month': Array,
        'hour': Array,
        'solazi': Array,
        'solzen': Array,
        'beam': Array,
        'tdry': Array,
        'wspd': Array,
        'twet': Array,
        'pres': Array,
        'tou_value': Array,
        'theta_L': Array,
        'phi_t': Array,
        'eta_optical': Array,
        'EqOptEff': Array,
        'sf_def': Array,
        'q_inc_sf_tot': Array,
        'q_abs_tot': Array,
        'q_dump': Array,
        'q_loss_tot': Array,
        'Pipe_hl': Array,
        'q_avail': Array,
        'q_loss_spec_tot': Array,
        'eta_thermal': Array,
        'E_bal_startup': Array,
        'm_dot_avail': Array,
        'm_dot_htf2': Array,
        'DP_tot': Array,
        'T_sys_c': Array,
        'T_sys_h': Array,
        't_loop_outlet': Array,
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
        'P_cycle': Array,
        'm_dot_pb': Array,
        'T_pb_in': Array,
        'T_pb_out': Array,
        'm_dot_makeup': Array,
        'q_pb': Array,
        'pipe_sgs_diams': Array,
        'pipe_sgs_wallthk': Array,
        'pipe_sgs_mdot_dsn': Array,
        'pipe_sgs_vel_dsn': Array,
        'pipe_sgs_T_dsn': Array,
        'pipe_sgs_P_dsn': Array,
        'q_aux_fuel': Array,
        'W_dot_pump': Array,
        'htf_pump_power': Array,
        'track_par_tot': Array,
        'W_par_BOP': Array,
        'fixed_par': Array,
        'W_par_aux_boiler': Array,
        'W_cool_par': Array,
        'Q_par_sf_fp': Array,
        'Q_par_tes_fp': Array,
        'monthly_energy': Array,
        'annual_energy': float,
        'annual_W_cycle_gross': float,
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
    file_name: str = INPUT(label='local weather file path', type='STRING', group='Weather', required='*', constraints='LOCAL_FILE')
    track_mode: float = INPUT(label='Tracking mode', type='NUMBER', group='Weather', required='*')
    tilt: float = INPUT(label='Tilt angle of surface/axis', type='NUMBER', group='Weather', required='*')
    azimuth: float = INPUT(label='Azimuth angle of surface/axis', type='NUMBER', group='Weather', required='*')
    system_capacity: float = INPUT(label='Nameplate capacity', units='kW', type='NUMBER', group='mslf', required='*')
    weekday_schedule: Matrix = INPUT(label='12x24 Time of Use Values for week days', type='MATRIX', group='tou_translator', required='*')
    weekend_schedule: Matrix = INPUT(label='12x24 Time of Use Values for week end days', type='MATRIX', group='tou_translator', required='*')
    nMod: float = INPUT(label='Number of collector modules in a loop', type='NUMBER', group='controller', required='*', constraints='INTEGER')
    nRecVar: float = INPUT(label='Number of receiver variantions', type='NUMBER', group='controller', required='?=4', constraints='INTEGER')
    nLoops: float = INPUT(label='Number of loops in the field', type='NUMBER', group='controller', required='*')
    eta_pump: float = INPUT(label='HTF pump efficiency', type='NUMBER', group='controller', required='*')
    HDR_rough: float = INPUT(label='Header pipe roughness', units='m', type='NUMBER', group='controller', required='*')
    theta_stow: float = INPUT(label='stow angle', units='deg', type='NUMBER', group='controller', required='*')
    theta_dep: float = INPUT(label='deploy angle', units='deg', type='NUMBER', group='controller', required='*')
    FieldConfig: float = INPUT(label='Number of subfield headers', type='NUMBER', group='controller', required='*')
    T_startup: float = INPUT(label='Power block startup temperature', units='C', type='NUMBER', group='controller', required='*')
    pb_rated_cap: float = INPUT(label='Rated plant capacity', units='MWe', type='NUMBER', group='controller', required='*')
    m_dot_htfmin: float = INPUT(label='Minimum loop HTF flow rate', units='kg/s', type='NUMBER', group='controller', required='*')
    m_dot_htfmax: float = INPUT(label='Maximum loop HTF flow rate', units='kg/s', type='NUMBER', group='controller', required='*')
    T_loop_in_des: float = INPUT(label='Design loop inlet temperature', units='C', type='NUMBER', group='controller', required='*')
    T_loop_out: float = INPUT(label='Target loop outlet temperature', units='C', type='NUMBER', group='controller', required='*')
    Fluid: float = INPUT(label='Field HTF fluid number', type='NUMBER', group='controller', required='*', constraints='INTEGER')
    T_field_ini: float = INPUT(label='Initial field temperature', units='C', type='NUMBER', group='controller', required='*')
    field_fl_props: Matrix = INPUT(label='Fluid property data', type='MATRIX', group='controller', required='*')
    T_fp: float = INPUT(label='Freeze protection temperature (heat trace activation temperature)', units='C', type='NUMBER', group='controller', required='*')
    I_bn_des: float = INPUT(label='Solar irradiation at design', units='W/m2', type='NUMBER', group='controller', required='*')
    V_hdr_max: float = INPUT(label='Maximum HTF velocity in the header at design', units='m/s', type='NUMBER', group='controller', required='*')
    V_hdr_min: float = INPUT(label='Minimum HTF velocity in the header at design', units='m/s', type='NUMBER', group='controller', required='*')
    Pipe_hl_coef: float = INPUT(label='Loss coefficient from the header - runner pipe - and non-HCE piping', units='W/m2-K', type='NUMBER', group='controller', required='*')
    SCA_drives_elec: float = INPUT(label='Tracking power in Watts per SCA drive', units='W/module', type='NUMBER', group='controller', required='*')
    fthrok: float = INPUT(label='Flag to allow partial defocusing of the collectors', type='NUMBER', group='controller', required='*', constraints='INTEGER')
    fthrctrl: float = INPUT(label='Defocusing strategy', type='NUMBER', group='controller', required='*', constraints='INTEGER')
    ColAz: float = INPUT(label='Collector azimuth angle', units='deg', type='NUMBER', group='controller', required='*')
    solar_mult: float = INPUT(label='Solar multiple', type='NUMBER', group='controller', required='*')
    mc_bal_hot: float = INPUT(label='The heat capacity of the balance of plant on the hot side', units='kWht/K-MWt', type='NUMBER', group='controller', required='*')
    mc_bal_cold: float = INPUT(label='The heat capacity of the balance of plant on the cold side', units='kWht/K-MWt', type='NUMBER', group='controller', required='*')
    mc_bal_sca: float = INPUT(label='Non-HTF heat capacity associated with each SCA - per meter basis', units='Wht/K-m', type='NUMBER', group='controller', required='*')
    water_per_wash: float = INPUT(label='Water usage per wash', units='L/m2_aper', type='NUMBER', group='solar_field', required='*')
    washes_per_year: float = INPUT(label='Mirror washing frequency', units='none', type='NUMBER', group='solar_field', required='*')
    opt_model: float = INPUT(label='The optical model', type='NUMBER', group='controller', required='*', constraints='INTEGER')
    A_aperture: float = INPUT(label='Reflective aperture area of the collector', units='m2', type='NUMBER', group='controller', required='*')
    reflectivity: float = INPUT(label='Solar-weighted mirror reflectivity value', type='NUMBER', group='controller', required='*')
    TrackingError: float = INPUT(label='Tracking error derate', type='NUMBER', group='controller', required='*')
    GeomEffects: float = INPUT(label='Geometry effects derate', type='NUMBER', group='controller', required='*')
    Dirt_mirror: float = INPUT(label='User-defined dirt on mirror derate', type='NUMBER', group='controller', required='*')
    Error: float = INPUT(label='User-defined general optical error derate', type='NUMBER', group='controller', required='*')
    L_mod: float = INPUT(label='The length of the collector module', units='m', type='NUMBER', group='controller', required='*')
    IAM_T_coefs: Array = INPUT(label='Incidence angle modifier coefficients - transversal plane', type='ARRAY', group='controller', required='*')
    IAM_L_coefs: Array = INPUT(label='Incidence angle modifier coefficients - longitudinal plane', type='ARRAY', group='controller', required='*')
    OpticalTable: Matrix = INPUT(label='Values of the optical efficiency table', type='MATRIX', group='controller', required='*')
    rec_model: float = INPUT(label='Receiver model type (1=Polynomial ; 2=Evac tube)', type='NUMBER', group='controller', required='*', constraints='INTEGER')
    HCE_FieldFrac: Array = INPUT(label='The fraction of the field occupied by this HCE type', type='ARRAY', group='controller', required='*')
    D_abs_in: Array = INPUT(label='The inner absorber tube diameter', units='m', type='ARRAY', group='controller', required='*')
    D_abs_out: Array = INPUT(label='The outer absorber tube diameter', units='m', type='ARRAY', group='controller', required='*')
    D_glass_in: Array = INPUT(label='The inner glass envelope diameter', units='m', type='ARRAY', group='controller', required='*')
    D_glass_out: Array = INPUT(label='The outer glass envelope diameter', units='m', type='ARRAY', group='controller', required='*')
    D_plug: Array = INPUT(label='The diameter of the absorber flow plug (optional)', units='m', type='ARRAY', group='controller', required='*')
    Flow_type: Array = INPUT(label='The flow type through the absorber', type='ARRAY', group='controller', required='*')
    Rough: Array = INPUT(label='Roughness of the internal surface', units='m', type='ARRAY', group='controller', required='*')
    alpha_env: Array = INPUT(label='Envelope absorptance', type='ARRAY', group='controller', required='*')
    epsilon_abs_1: Matrix = INPUT(label='Absorber emittance - HCE variation 1', type='MATRIX', group='controller', required='*')
    epsilon_abs_2: Matrix = INPUT(label='Absorber emittance - HCE variation 2', type='MATRIX', group='controller', required='*')
    epsilon_abs_3: Matrix = INPUT(label='Absorber emittance - HCE variation 3', type='MATRIX', group='controller', required='*')
    epsilon_abs_4: Matrix = INPUT(label='Absorber emittance - HCE variation 4', type='MATRIX', group='controller', required='*')
    alpha_abs: Array = INPUT(label='Absorber absorptance', type='ARRAY', group='controller', required='*')
    Tau_envelope: Array = INPUT(label='Envelope transmittance', type='ARRAY', group='controller', required='*')
    epsilon_glass: Array = INPUT(label='Glass envelope emissivity', type='ARRAY', group='controller', required='*')
    GlazingIntactIn: Array = INPUT(label='The glazing intact flag', type='ARRAY', group='controller', required='*')
    P_a: Array = INPUT(label='Annulus gas pressure', units='torr', type='ARRAY', group='controller', required='*')
    AnnulusGas: Array = INPUT(label='Annulus gas type (1=air; 26=Ar; 27=H2)', type='ARRAY', group='controller', required='*')
    AbsorberMaterial: Array = INPUT(label='Absorber material type', type='ARRAY', group='controller', required='*')
    Shadowing: Array = INPUT(label='Receiver bellows shadowing loss factor', type='ARRAY', group='controller', required='*')
    dirt_env: Array = INPUT(label='Loss due to dirt on the receiver envelope', type='ARRAY', group='controller', required='*')
    Design_loss: Array = INPUT(label='Receiver heat loss at design', units='W/m', type='ARRAY', group='controller', required='*')
    L_mod_spacing: float = INPUT(label='Piping distance between sequential modules in a loop', units='m', type='NUMBER', group='controller', required='*')
    L_crossover: float = INPUT(label='Length of crossover piping in a loop', units='m', type='NUMBER', group='controller', required='*')
    HL_T_coefs: Array = INPUT(label='HTF temperature-dependent heat loss coefficients', units='W/m-K', type='ARRAY', group='controller', required='*')
    HL_w_coefs: Array = INPUT(label='Wind-speed-dependent heat loss coefficients', units='W/m-(m/s)', type='ARRAY', group='controller', required='*')
    DP_nominal: float = INPUT(label='Pressure drop across a single collector assembly at design', units='bar', type='NUMBER', group='controller', required='*')
    DP_coefs: Array = INPUT(label='Pressure drop mass flow based part-load curve', type='ARRAY', group='controller', required='*')
    rec_htf_vol: float = INPUT(label='Volume of HTF in a single collector unit per unit aperture area', units='L/m2-ap', type='NUMBER', group='controller', required='*')
    T_amb_sf_des: float = INPUT(label='Ambient design-point temperature for the solar field', units='C', type='NUMBER', group='controller', required='*')
    V_wind_des: float = INPUT(label='Design-point wind velocity', units='m/s', type='NUMBER', group='controller', required='*')
    I_b: float = INPUT(label='Direct normal incident solar irradiation', units='kJ/m2-hr', type='NUMBER', group='controller', required='*')
    T_db: float = INPUT(label='Dry bulb air temperature', units='C', type='NUMBER', group='controller', required='*')
    V_wind: float = INPUT(label='Ambient windspeed', units='m/s', type='NUMBER', group='controller', required='*')
    P_amb: float = INPUT(label='Ambient pressure', units='atm', type='NUMBER', group='controller', required='*')
    T_dp: float = INPUT(label='The dewpoint temperature', units='C', type='NUMBER', group='controller', required='*')
    T_cold_in: float = INPUT(label='HTF return temperature', units='C', type='NUMBER', group='controller', required='*')
    defocus: float = INPUT(label='Defocus control', type='NUMBER', group='controller', required='*')
    field_fluid: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    store_fl_props: Matrix = INPUT(label='Label', type='MATRIX', group='controller', required='*')
    store_fluid: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    tshours: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    is_hx: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    dt_hot: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    dt_cold: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    hx_config: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    q_max_aux: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    T_set_aux: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    V_tank_hot_ini: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    T_tank_hot_ini: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    T_tank_cold_ini: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    vol_tank: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    h_tank: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    h_tank_min: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    u_tank: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    tank_pairs: float = INPUT(label='Label', type='NUMBER', group='controller', required='*', constraints='INTEGER')
    cold_tank_Thtr: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    hot_tank_Thtr: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    tank_max_heat: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    T_field_in_des: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    T_field_out_des: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    q_pb_design: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    W_pb_design: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    cycle_max_frac: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    cycle_cutoff_frac: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    solarm: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    pb_pump_coef: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    tes_pump_coef: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    pb_fixed_par: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    bop_array: Array = INPUT(label='Label', type='ARRAY', group='controller', required='*')
    aux_array: Array = INPUT(label='Label', type='ARRAY', group='controller', required='*')
    tes_temp: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    fossil_mode: float = INPUT(label='Label', type='NUMBER', group='controller', required='*', constraints='INTEGER')
    fthr_ok: float = INPUT(label='Label', type='NUMBER', group='controller', required='*', constraints='INTEGER')
    nSCA: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    fc_on: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    t_standby_reset: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    tes_type: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    tslogic_a: Array = INPUT(label='Label', type='ARRAY', group='controller', required='*')
    tslogic_b: Array = INPUT(label='Label', type='ARRAY', group='controller', required='*')
    tslogic_c: Array = INPUT(label='Label', type='ARRAY', group='controller', required='*')
    ffrac: Array = INPUT(label='Label', type='ARRAY', group='controller', required='*')
    tc_fill: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    tc_void: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    t_dis_out_min: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    t_ch_out_max: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    nodes: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    f_tc_cold: float = INPUT(label='Label', type='NUMBER', group='controller', required='*')
    V_tes_des: float = INPUT(label='Design-point velocity to size the TES pipe diameters', units='m/s', type='NUMBER', group='controller', required='*')
    custom_tes_p_loss: float = INPUT(label='TES pipe losses are based on custom lengths and coeffs', units='-', type='NUMBER', group='controller', required='*')
    k_tes_loss_coeffs: Array = INPUT(label='Minor loss coeffs for the coll, gen, and bypass loops', units='-', type='ARRAY', group='controller', required='*')
    custom_sgs_pipe_sizes: float = INPUT(label='Use custom SGS pipe diams, wallthks, and lengths', units='-', type='NUMBER', group='controller', required='*')
    sgs_diams: Array = INPUT(label='Custom SGS diameters', units='m', type='ARRAY', group='controller', required='*')
    sgs_wallthicks: Array = INPUT(label='Custom SGS wall thicknesses', units='m', type='ARRAY', group='controller', required='*')
    sgs_lengths: Array = INPUT(label='Custom SGS lengths', units='m', type='ARRAY', group='controller', required='*')
    DP_SGS: float = INPUT(label='Pressure drop within the steam generator', units='bar', type='NUMBER', group='controller', required='*')
    tanks_in_parallel: float = INPUT(label='Tanks are in parallel, not in series, with solar field', units='-', type='NUMBER', group='controller', required='*')
    has_hot_tank_bypass: float = INPUT(label='Bypass valve connects field outlet to cold tank', units='-', type='NUMBER', group='controller', required='*')
    T_tank_hot_inlet_min: float = INPUT(label='Minimum hot tank htf inlet temperature', units='C', type='NUMBER', group='controller', required='*')
    calc_design_pipe_vals: float = INPUT(label='Calculate temps and pressures at design conditions for runners and headers', units='-', type='NUMBER', group='controller', required='*')
    pc_config: float = INPUT(label='0: Steam Rankine (224), 1: user defined', units='-', type='NUMBER', group='powerblock', required='?=0', constraints='INTEGER')
    P_ref: float = INPUT(label='Label', units='-', type='NUMBER', group='powerblock', required='*')
    eta_ref: float = INPUT(label='Cycle thermal efficiency at design point', units='-', type='NUMBER', group='powerblock', required='*')
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
    ud_f_W_dot_cool_des: float = INPUT(label='Percent of user-defined power cycle design gross output consumed by cooling', units='%', type='NUMBER', group='user_defined_PC', required='pc_config=1')
    ud_m_dot_water_cool_des: float = INPUT(label='Mass flow rate of water required at user-defined power cycle design point', units='kg/s', type='NUMBER', group='user_defined_PC', required='pc_config=1')
    ud_ind_od: Matrix = INPUT(label='Off design user-defined power cycle performance as function of T_htf, m_dot_htf [ND], and T_amb', type='MATRIX', group='user_defined_PC', required='pc_config=1')
    eta_lhv: float = INPUT(label='Label', units='-', type='NUMBER', group='enet', required='*')
    eta_tes_htr: float = INPUT(label='Label', units='-', type='NUMBER', group='enet', required='*')
    fp_mode: float = INPUT(label='Label', units='-', type='NUMBER', group='enet', required='*')
    T_htf_hot_ref: float = INPUT(label='Label', units='-', type='NUMBER', group='powerblock', required='*')
    T_htf_cold_ref: float = INPUT(label='Label', units='-', type='NUMBER', group='powerblock', required='*')
    month: Final[Array] = OUTPUT(label='Resource Month', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    hour: Final[Array] = OUTPUT(label='Resource Hour of Day', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    solazi: Final[Array] = OUTPUT(label='Resource Solar Azimuth', units='deg', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    solzen: Final[Array] = OUTPUT(label='Resource Solar Zenith', units='deg', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    beam: Final[Array] = OUTPUT(label='Resource Beam normal irradiance', units='W/m2', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    tdry: Final[Array] = OUTPUT(label='Resource Dry bulb temperature', units='C', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    wspd: Final[Array] = OUTPUT(label='Resource Wind Speed', units='m/s', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    twet: Final[Array] = OUTPUT(label='Resource Wet bulb temperature', units='C', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    pres: Final[Array] = OUTPUT(label='Resource Pressure', units='mbar', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    tou_value: Final[Array] = OUTPUT(label='Resource Time-of-use value', type='ARRAY', group='tou', required='*', constraints='LENGTH=8760')
    theta_L: Final[Array] = OUTPUT(label='Field collector incidence angle - longitudinal', units='deg', type='ARRAY', group='mslf', required='*', constraints='LENGTH=8760')
    phi_t: Final[Array] = OUTPUT(label='Field collector incidence angle - transversal', units='deg', type='ARRAY', group='mslf', required='*', constraints='LENGTH=8760')
    eta_optical: Final[Array] = OUTPUT(label='Field collector optical efficiency', type='ARRAY', group='mslf', required='*', constraints='LENGTH=8760')
    EqOptEff: Final[Array] = OUTPUT(label='Field collector and receiver optical efficiency', type='ARRAY', group='mslf', required='*', constraints='LENGTH=8760')
    sf_def: Final[Array] = OUTPUT(label='Field collector focus fraction', type='ARRAY', group='mslf', required='*', constraints='LENGTH=8760')
    q_inc_sf_tot: Final[Array] = OUTPUT(label='Field thermal power incident', units='MWt', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    q_abs_tot: Final[Array] = OUTPUT(label='Field thermal power absorbed', units='MWt', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    q_dump: Final[Array] = OUTPUT(label='Field thermal power dumped', units='MWt', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    q_loss_tot: Final[Array] = OUTPUT(label='Field thermal power receiver loss', units='MWt', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    Pipe_hl: Final[Array] = OUTPUT(label='Field thermal power header pipe losses', units='MWt', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    q_avail: Final[Array] = OUTPUT(label='Field thermal power produced', units='MWt', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    q_loss_spec_tot: Final[Array] = OUTPUT(label='Field thermal power avg. receiver loss', units='W/m', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    eta_thermal: Final[Array] = OUTPUT(label='Field thermal efficiency', type='ARRAY', group='mslf', required='*', constraints='LENGTH=8760')
    E_bal_startup: Final[Array] = OUTPUT(label='Field HTF energy inertial (consumed)', units='MWht', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    m_dot_avail: Final[Array] = OUTPUT(label='Field HTF mass flow rate total', units='kg/hr', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    m_dot_htf2: Final[Array] = OUTPUT(label='Field HTF mass flow rate loop', units='kg/s', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    DP_tot: Final[Array] = OUTPUT(label='Field HTF pressure drop total', units='bar', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    T_sys_c: Final[Array] = OUTPUT(label='Field HTF temperature cold header inlet', units='C', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    T_sys_h: Final[Array] = OUTPUT(label='Field HTF temperature hot header outlet', units='C', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    t_loop_outlet: Final[Array] = OUTPUT(label='Field HTF temperature loop outlet', units='C', type='ARRAY', group='mslf', required='*', constraints='LENGTH=8760')
    mass_tank_cold: Final[Array] = OUTPUT(label='TES HTF mass in cold tank', units='kg', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    mass_tank_hot: Final[Array] = OUTPUT(label='TES HTF mass in hot tank', units='kg', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    m_dot_charge_field: Final[Array] = OUTPUT(label='TES HTF mass flow rate - field side of HX', units='kg/hr', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    m_dot_discharge_tank: Final[Array] = OUTPUT(label='TES HTF mass flow rate - storage side of HX', units='kg/hr', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    T_tank_cold_fin: Final[Array] = OUTPUT(label='TES HTF temperature in cold tank', units='C', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    T_tank_hot_fin: Final[Array] = OUTPUT(label='TES HTF temperature in hot tank', units='C', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    Ts_hot: Final[Array] = OUTPUT(label='TES HTF temperature HX field side hot', units='C', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    Ts_cold: Final[Array] = OUTPUT(label='TES HTF temperature HX field side cold', units='C', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    T_tank_hot_in: Final[Array] = OUTPUT(label='TES HTF temperature hot tank inlet', units='C', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    T_tank_cold_in: Final[Array] = OUTPUT(label='TES HTF temperature cold tank inlet', units='C', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    vol_tank_cold_fin: Final[Array] = OUTPUT(label='TES HTF volume in cold tank', units='m3', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    vol_tank_hot_fin: Final[Array] = OUTPUT(label='TES HTF volume in hot tank', units='m3', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    vol_tank_total: Final[Array] = OUTPUT(label='TES HTF volume total', units='m3', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    q_to_tes: Final[Array] = OUTPUT(label='TES thermal energy into storage', units='MWt', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    tank_losses: Final[Array] = OUTPUT(label='TES thermal losses from tank(s)', units='MWt', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    eta: Final[Array] = OUTPUT(label='Cycle efficiency (gross)', type='ARRAY', group='Type224', required='*', constraints='LENGTH=8760')
    W_net: Final[Array] = OUTPUT(label='Cycle electrical power output (net)', units='MWe', type='ARRAY', group='Net_E_Calc', required='*', constraints='LENGTH=8760')
    P_cycle: Final[Array] = OUTPUT(label='Cycle electrical power output (gross)', units='MWe', type='ARRAY', group='Net_E_Calc', required='*', constraints='LENGTH=8760')
    m_dot_pb: Final[Array] = OUTPUT(label='Cycle HTF mass flow rate', units='kg/hr', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    T_pb_in: Final[Array] = OUTPUT(label='Cycle HTF temperature in (hot)', units='C', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    T_pb_out: Final[Array] = OUTPUT(label='Cycle HTF temperature out (cold)', units='C', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    m_dot_makeup: Final[Array] = OUTPUT(label='Cycle cooling water mass flow rate - makeup', units='kg/hr', type='ARRAY', group='Type224', required='*', constraints='LENGTH=8760')
    q_pb: Final[Array] = OUTPUT(label='Cycle thermal power input', units='MWt', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    pipe_sgs_diams: Final[Array] = OUTPUT(label='Pipe diameters in SGS', units='m', type='ARRAY', group='Type251', required='*')
    pipe_sgs_wallthk: Final[Array] = OUTPUT(label='Pipe wall thickness in SGS', units='m', type='ARRAY', group='Type251', required='*')
    pipe_sgs_mdot_dsn: Final[Array] = OUTPUT(label='Mass flow SGS pipes at design conditions', units='kg/s', type='ARRAY', group='Type251', required='*')
    pipe_sgs_vel_dsn: Final[Array] = OUTPUT(label='Velocity in SGS pipes at design conditions', units='m/s', type='ARRAY', group='Type251', required='*')
    pipe_sgs_T_dsn: Final[Array] = OUTPUT(label='Temperature in SGS pipes at design conditions', units='C', type='ARRAY', group='Type251', required='*')
    pipe_sgs_P_dsn: Final[Array] = OUTPUT(label='Pressure in SGS pipes at design conditions', units='bar', type='ARRAY', group='Type251', required='*')
    q_aux_fuel: Final[Array] = OUTPUT(label='Fossil fuel usage (all subsystems)', units='MMBTU', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    W_dot_pump: Final[Array] = OUTPUT(label='Parasitic power solar field HTF pump', units='MWe', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    htf_pump_power: Final[Array] = OUTPUT(label='Parasitic power TES and Cycle HTF pump', units='MWe', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    track_par_tot: Final[Array] = OUTPUT(label='Parasitic power field collector drives', units='MWe', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    W_par_BOP: Final[Array] = OUTPUT(label='Parasitic power generation-dependent load', units='MWe', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    fixed_par: Final[Array] = OUTPUT(label='Parasitic power fixed load', units='MWe', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    W_par_aux_boiler: Final[Array] = OUTPUT(label='Parasitic power auxiliary heater operation', units='MWe', type='ARRAY', group='Type251', required='*', constraints='LENGTH=8760')
    W_cool_par: Final[Array] = OUTPUT(label='Parasitic power condenser operation', units='MWe', type='ARRAY', group='Type224', required='*', constraints='LENGTH=8760')
    Q_par_sf_fp: Final[Array] = OUTPUT(label='Parasitic thermal field freeze protection', units='MWt', type='ARRAY', group='SumCalc', required='*', constraints='LENGTH=8760')
    Q_par_tes_fp: Final[Array] = OUTPUT(label='Parasitic thermal TES freeze protection', units='MWt', type='ARRAY', group='SumCalc', required='*', constraints='LENGTH=8760')
    monthly_energy: Final[Array] = OUTPUT(label='Monthly Energy', units='kWh', type='ARRAY', group='mslf', required='*', constraints='LENGTH=12')
    annual_energy: Final[float] = OUTPUT(label='Annual Energy', units='kWh', type='NUMBER', group='mslf', required='*')
    annual_W_cycle_gross: Final[float] = OUTPUT(label='Electrical source - Power cycle gross output', units='kWh', type='NUMBER', group='mslf', required='*')
    conversion_factor: Final[float] = OUTPUT(label='Gross to Net Conversion Factor', units='%', type='NUMBER', group='Calculated', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', required='*')
    kwh_per_kw: Final[float] = OUTPUT(label='First year kWh/kW', units='kWh/kW', type='NUMBER', required='*')
    system_heat_rate: Final[float] = OUTPUT(label='System heat rate', units='MMBtu/MWh', type='NUMBER', required='*')
    annual_fuel_usage: Final[float] = OUTPUT(label='Annual fuel usage', units='kWh', type='NUMBER', required='*')
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
                 weekday_schedule: Matrix = ...,
                 weekend_schedule: Matrix = ...,
                 nMod: float = ...,
                 nRecVar: float = ...,
                 nLoops: float = ...,
                 eta_pump: float = ...,
                 HDR_rough: float = ...,
                 theta_stow: float = ...,
                 theta_dep: float = ...,
                 FieldConfig: float = ...,
                 T_startup: float = ...,
                 pb_rated_cap: float = ...,
                 m_dot_htfmin: float = ...,
                 m_dot_htfmax: float = ...,
                 T_loop_in_des: float = ...,
                 T_loop_out: float = ...,
                 Fluid: float = ...,
                 T_field_ini: float = ...,
                 field_fl_props: Matrix = ...,
                 T_fp: float = ...,
                 I_bn_des: float = ...,
                 V_hdr_max: float = ...,
                 V_hdr_min: float = ...,
                 Pipe_hl_coef: float = ...,
                 SCA_drives_elec: float = ...,
                 fthrok: float = ...,
                 fthrctrl: float = ...,
                 ColAz: float = ...,
                 solar_mult: float = ...,
                 mc_bal_hot: float = ...,
                 mc_bal_cold: float = ...,
                 mc_bal_sca: float = ...,
                 water_per_wash: float = ...,
                 washes_per_year: float = ...,
                 opt_model: float = ...,
                 A_aperture: float = ...,
                 reflectivity: float = ...,
                 TrackingError: float = ...,
                 GeomEffects: float = ...,
                 Dirt_mirror: float = ...,
                 Error: float = ...,
                 L_mod: float = ...,
                 IAM_T_coefs: Array = ...,
                 IAM_L_coefs: Array = ...,
                 OpticalTable: Matrix = ...,
                 rec_model: float = ...,
                 HCE_FieldFrac: Array = ...,
                 D_abs_in: Array = ...,
                 D_abs_out: Array = ...,
                 D_glass_in: Array = ...,
                 D_glass_out: Array = ...,
                 D_plug: Array = ...,
                 Flow_type: Array = ...,
                 Rough: Array = ...,
                 alpha_env: Array = ...,
                 epsilon_abs_1: Matrix = ...,
                 epsilon_abs_2: Matrix = ...,
                 epsilon_abs_3: Matrix = ...,
                 epsilon_abs_4: Matrix = ...,
                 alpha_abs: Array = ...,
                 Tau_envelope: Array = ...,
                 epsilon_glass: Array = ...,
                 GlazingIntactIn: Array = ...,
                 P_a: Array = ...,
                 AnnulusGas: Array = ...,
                 AbsorberMaterial: Array = ...,
                 Shadowing: Array = ...,
                 dirt_env: Array = ...,
                 Design_loss: Array = ...,
                 L_mod_spacing: float = ...,
                 L_crossover: float = ...,
                 HL_T_coefs: Array = ...,
                 HL_w_coefs: Array = ...,
                 DP_nominal: float = ...,
                 DP_coefs: Array = ...,
                 rec_htf_vol: float = ...,
                 T_amb_sf_des: float = ...,
                 V_wind_des: float = ...,
                 I_b: float = ...,
                 T_db: float = ...,
                 V_wind: float = ...,
                 P_amb: float = ...,
                 T_dp: float = ...,
                 T_cold_in: float = ...,
                 defocus: float = ...,
                 field_fluid: float = ...,
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
                 T_tank_hot_ini: float = ...,
                 T_tank_cold_ini: float = ...,
                 vol_tank: float = ...,
                 h_tank: float = ...,
                 h_tank_min: float = ...,
                 u_tank: float = ...,
                 tank_pairs: float = ...,
                 cold_tank_Thtr: float = ...,
                 hot_tank_Thtr: float = ...,
                 tank_max_heat: float = ...,
                 T_field_in_des: float = ...,
                 T_field_out_des: float = ...,
                 q_pb_design: float = ...,
                 W_pb_design: float = ...,
                 cycle_max_frac: float = ...,
                 cycle_cutoff_frac: float = ...,
                 solarm: float = ...,
                 pb_pump_coef: float = ...,
                 tes_pump_coef: float = ...,
                 pb_fixed_par: float = ...,
                 bop_array: Array = ...,
                 aux_array: Array = ...,
                 tes_temp: float = ...,
                 fossil_mode: float = ...,
                 fthr_ok: float = ...,
                 nSCA: float = ...,
                 fc_on: float = ...,
                 t_standby_reset: float = ...,
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
                 V_tes_des: float = ...,
                 custom_tes_p_loss: float = ...,
                 k_tes_loss_coeffs: Array = ...,
                 custom_sgs_pipe_sizes: float = ...,
                 sgs_diams: Array = ...,
                 sgs_wallthicks: Array = ...,
                 sgs_lengths: Array = ...,
                 DP_SGS: float = ...,
                 tanks_in_parallel: float = ...,
                 has_hot_tank_bypass: float = ...,
                 T_tank_hot_inlet_min: float = ...,
                 calc_design_pipe_vals: float = ...,
                 pc_config: float = ...,
                 P_ref: float = ...,
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
                 ud_f_W_dot_cool_des: float = ...,
                 ud_m_dot_water_cool_des: float = ...,
                 ud_ind_od: Matrix = ...,
                 eta_lhv: float = ...,
                 eta_tes_htr: float = ...,
                 fp_mode: float = ...,
                 T_htf_hot_ref: float = ...,
                 T_htf_cold_ref: float = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
