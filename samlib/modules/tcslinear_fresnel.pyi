
# This is a generated file

"""tcslinear_fresnel - CSP model using the linear fresnel TCS types."""

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
        'tes_hours': float,
        'q_max_aux': float,
        'LHV_eff': float,
        'x_b_des': float,
        'P_turb_des': float,
        'fP_hdr_c': float,
        'fP_sf_boil': float,
        'fP_boil_to_sh': float,
        'fP_sf_sh': float,
        'fP_hdr_h': float,
        'q_pb_des': float,
        'cycle_max_fraction': float,
        'cycle_cutoff_frac': float,
        't_sby': float,
        'q_sby_frac': float,
        'solarm': float,
        'PB_pump_coef': float,
        'PB_fixed_par': float,
        'bop_array': Array,
        'aux_array': Array,
        'fossil_mode': float,
        'I_bn_des': float,
        'is_sh': float,
        'is_oncethru': float,
        'is_multgeom': float,
        'nModBoil': float,
        'nModSH': float,
        'nLoops': float,
        'eta_pump': float,
        'latitude': float,
        'theta_stow': float,
        'theta_dep': float,
        'm_dot_min': float,
        'T_fp': float,
        'Pipe_hl_coef': float,
        'SCA_drives_elec': float,
        'ColAz': float,
        'e_startup': float,
        'T_amb_des_sf': float,
        'V_wind_max': float,
        'csp.lf.sf.water_per_wash': float,
        'csp.lf.sf.washes_per_year': float,
        'ffrac': Array,
        'A_aperture': Matrix,
        'L_col': Matrix,
        'OptCharType': Matrix,
        'IAM_T': Matrix,
        'IAM_L': Matrix,
        'TrackingError': Matrix,
        'GeomEffects': Matrix,
        'rho_mirror_clean': Matrix,
        'dirt_mirror': Matrix,
        'error': Matrix,
        'HLCharType': Matrix,
        'HL_dT': Matrix,
        'HL_W': Matrix,
        'D_2': Matrix,
        'D_3': Matrix,
        'D_4': Matrix,
        'D_5': Matrix,
        'D_p': Matrix,
        'Rough': Matrix,
        'Flow_type': Matrix,
        'AbsorberMaterial': Matrix,
        'HCE_FieldFrac': Matrix,
        'alpha_abs': Matrix,
        'b_eps_HCE1': Matrix,
        'b_eps_HCE2': Matrix,
        'b_eps_HCE3': Matrix,
        'b_eps_HCE4': Matrix,
        'sh_eps_HCE1': Matrix,
        'sh_eps_HCE2': Matrix,
        'sh_eps_HCE3': Matrix,
        'sh_eps_HCE4': Matrix,
        'alpha_env': Matrix,
        'EPSILON_4': Matrix,
        'Tau_envelope': Matrix,
        'GlazingIntactIn': Matrix,
        'AnnulusGas': Matrix,
        'P_a': Matrix,
        'Design_loss': Matrix,
        'Shadowing': Matrix,
        'Dirt_HCE': Matrix,
        'b_OpticalTable': Matrix,
        'sh_OpticalTable': Matrix,
        'dnifc': float,
        'I_bn': float,
        'T_db': float,
        'T_dp': float,
        'P_amb': float,
        'V_wind': float,
        'm_dot_htf_ref': float,
        'm_pb_demand': float,
        'shift': float,
        'SolarAz_init': float,
        'SolarZen': float,
        'T_pb_out_init': float,
        'eta_ref': float,
        'T_cold_ref': float,
        'dT_cw_ref': float,
        'T_amb_des': float,
        'P_boil_des': float,
        'P_rh_ref': float,
        'rh_frac_ref': float,
        'CT': float,
        'startup_time': float,
        'startup_frac': float,
        'T_approach': float,
        'T_ITD_des': float,
        'P_cond_ratio': float,
        'pb_bd_frac': float,
        'P_cond_min': float,
        'n_pl_inc': float,
        'F_wc': Array,
        'pc_mode': float,
        'T_hot': float,
        'm_dot_st': float,
        'T_wb': float,
        'demand_var': float,
        'standby_control': float,
        'T_db_pwb': float,
        'P_amb_pwb': float,
        'relhum': float,
        'f_recSU': float,
        'dp_b': float,
        'dp_sh': float,
        'dp_rh': float,
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
        'defocus': Array,
        'eta_opt_ave': Array,
        'eta_thermal': Array,
        'eta_sf': Array,
        'q_inc_tot': Array,
        'q_loss_rec': Array,
        'q_loss_piping': Array,
        'q_loss_sf': Array,
        'q_field_delivered': Array,
        'm_dot_field': Array,
        'm_dot_b_tot': Array,
        'm_dot': Array,
        'P_sf_in': Array,
        'dP_tot': Array,
        'T_field_in': Array,
        'T_loop_out': Array,
        'T_field_out': Array,
        'eta': Array,
        'W_net': Array,
        'W_cycle_gross': Array,
        'm_dot_to_pb': Array,
        'P_turb_in': Array,
        'T_pb_in': Array,
        'T_pb_out': Array,
        'E_bal_startup': Array,
        'q_dump': Array,
        'q_to_pb': Array,
        'm_dot_makeup': Array,
        'P_cond': Array,
        'f_bays': Array,
        'q_aux_fluid': Array,
        'm_dot_aux': Array,
        'q_aux_fuel': Array,
        'W_dot_pump': Array,
        'W_dot_col': Array,
        'W_dot_bop': Array,
        'W_dot_fixed': Array,
        'W_dot_aux': Array,
        'W_cool_par': Array,
        'monthly_energy': Array,
        'annual_energy': float,
        'annual_W_cycle_gross': float,
        'conversion_factor': float,
        'capacity_factor': float,
        'annual_total_water_use': float,
        'kwh_per_kw': float,
        'system_heat_rate': float,
        'annual_fuel_usage': float,
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
    system_capacity: float = INPUT(label='Nameplate capacity', units='kW', type='NUMBER', group='linear fresnelr', required='*')
    weekday_schedule: Matrix = INPUT(label='12x24 Time of Use Values for week days', type='MATRIX', group='tou_translator', required='*')
    weekend_schedule: Matrix = INPUT(label='12x24 Time of Use Values for week end days', type='MATRIX', group='tou_translator', required='*')
    tes_hours: float = INPUT(label='Equivalent full-load thermal storage hours', units='hr', type='NUMBER', group='solarfield', required='*')
    q_max_aux: float = INPUT(label='Maximum heat rate of the auxiliary heater', units='MW', type='NUMBER', group='solarfield', required='*')
    LHV_eff: float = INPUT(label='Fuel LHV efficiency (0..1)', units='none', type='NUMBER', group='solarfield', required='*')
    x_b_des: float = INPUT(label='Design point boiler outlet steam quality', units='none', type='NUMBER', group='solarfield', required='*')
    P_turb_des: float = INPUT(label='Design-point turbine inlet pressure', units='bar', type='NUMBER', group='solarfield', required='*')
    fP_hdr_c: float = INPUT(label='Average design-point cold header pressure drop fraction', units='none', type='NUMBER', group='solarfield', required='*')
    fP_sf_boil: float = INPUT(label='Design-point pressure drop across the solar field boiler fraction', units='none', type='NUMBER', group='solarfield', required='*')
    fP_boil_to_sh: float = INPUT(label='Design-point pressure drop between the boiler and superheater frac', units='none', type='NUMBER', group='solarfield', required='*')
    fP_sf_sh: float = INPUT(label='Design-point pressure drop across the solar field superheater frac', units='none', type='NUMBER', group='solarfield', required='*')
    fP_hdr_h: float = INPUT(label='Average design-point hot header pressure drop fraction', units='none', type='NUMBER', group='solarfield', required='*')
    q_pb_des: float = INPUT(label='Design heat input to the power block', units='MW', type='NUMBER', group='solarfield', required='*')
    cycle_max_fraction: float = INPUT(label='Maximum turbine over design operation fraction', units='none', type='NUMBER', group='solarfield', required='*')
    cycle_cutoff_frac: float = INPUT(label='Minimum turbine operation fraction before shutdown', units='none', type='NUMBER', group='solarfield', required='*')
    t_sby: float = INPUT(label='Low resource standby period', units='hr', type='NUMBER', group='solarfield', required='*')
    q_sby_frac: float = INPUT(label='Fraction of thermal power required for standby', units='none', type='NUMBER', group='solarfield', required='*')
    solarm: float = INPUT(label='Solar multiple', units='none', type='NUMBER', group='solarfield', required='*')
    PB_pump_coef: float = INPUT(label='Pumping power required to move 1kg of HTF through power block flow', units='kW/kg', type='NUMBER', group='solarfield', required='*')
    PB_fixed_par: float = INPUT(label='fraction of rated gross power consumed at all hours of the year', units='none', type='NUMBER', group='solarfield', required='*')
    bop_array: Array = INPUT(label='BOP_parVal, BOP_parPF, BOP_par0, BOP_par1, BOP_par2', units='-', type='ARRAY', group='solarfield', required='*')
    aux_array: Array = INPUT(label='Aux_parVal, Aux_parPF, Aux_par0, Aux_par1, Aux_par2', units='-', type='ARRAY', group='solarfield', required='*')
    fossil_mode: float = INPUT(label='Operation mode for the fossil backup {1=Normal,2=supp,3=toppin}', units='none', type='NUMBER', group='solarfield', required='*', constraints='INTEGER')
    I_bn_des: float = INPUT(label='Design point irradiation value', units='W/m2', type='NUMBER', group='solarfield', required='*')
    is_sh: float = INPUT(label='Does the solar field include a superheating section', units='none', type='NUMBER', group='solarfield', required='*', constraints='INTEGER')
    is_oncethru: float = INPUT(label='Flag indicating whether flow is once through with superheat', units='none', type='NUMBER', group='solarfield', required='*', constraints='INTEGER')
    is_multgeom: float = INPUT(label='Does the superheater have a different geometry from the boiler {1=yes}', units='none', type='NUMBER', group='solarfield', required='*', constraints='INTEGER')
    nModBoil: float = INPUT(label='Number of modules in the boiler section', units='none', type='NUMBER', group='solarfield', required='*', constraints='INTEGER')
    nModSH: float = INPUT(label='Number of modules in the superheater section', units='none', type='NUMBER', group='solarfield', required='*', constraints='INTEGER')
    nLoops: float = INPUT(label='Number of loops', units='none', type='NUMBER', group='solarfield', required='*')
    eta_pump: float = INPUT(label='Feedwater pump efficiency', units='none', type='NUMBER', group='solarfield', required='*')
    latitude: float = INPUT(label='Site latitude resource page', units='deg', type='NUMBER', group='solarfield', required='*')
    theta_stow: float = INPUT(label='stow angle', units='deg', type='NUMBER', group='solarfield', required='*')
    theta_dep: float = INPUT(label='deploy angle', units='deg', type='NUMBER', group='solarfield', required='*')
    m_dot_min: float = INPUT(label='Minimum loop flow rate', units='kg/s', type='NUMBER', group='solarfield', required='*')
    T_fp: float = INPUT(label='Freeze protection temperature (heat trace activation temperature)', units='C', type='NUMBER', group='solarfield', required='*')
    Pipe_hl_coef: float = INPUT(label='Loss coefficient from the header.. runner pipe.. and non-HCE pipin', units='W/m2-K', type='NUMBER', group='solarfield', required='*')
    SCA_drives_elec: float = INPUT(label='Tracking power.. in Watts per SCA drive', units='W/m2', type='NUMBER', group='solarfield', required='*')
    ColAz: float = INPUT(label='Collector azimuth angle', units='deg', type='NUMBER', group='solarfield', required='*')
    e_startup: float = INPUT(label='Thermal inertia contribution per sq meter of solar field', units='kJ/K-m2', type='NUMBER', group='solarfield', required='*')
    T_amb_des_sf: float = INPUT(label='Design-point ambient temperature', units='C', type='NUMBER', group='solarfield', required='*')
    V_wind_max: float = INPUT(label='Maximum allowable wind velocity before safety stow', units='m/s', type='NUMBER', group='solarfield', required='*')
    csp_lf_sf_water_per_wash: float = INPUT(name='csp.lf.sf.water_per_wash', label='Water usage per wash', units='L/m2_aper', type='NUMBER', group='heliostat', required='*')
    csp_lf_sf_washes_per_year: float = INPUT(name='csp.lf.sf.washes_per_year', label='Mirror washing frequency', type='NUMBER', group='heliostat', required='*')
    ffrac: Array = INPUT(label='Fossil dispatch logic - TOU periods', units='none', type='ARRAY', group='solarfield', required='*')
    A_aperture: Matrix = INPUT(label='(boiler, SH) Reflective aperture area of the collector module', units='m^2', type='MATRIX', group='solarfield', required='*')
    L_col: Matrix = INPUT(label='(boiler, SH) Active length of the superheater section collector module', units='m', type='MATRIX', group='solarfield', required='*')
    OptCharType: Matrix = INPUT(label='(boiler, SH) The optical characterization method', units='none', type='MATRIX', group='solarfield', required='*')
    IAM_T: Matrix = INPUT(label='(boiler, SH) Transverse Incident angle modifiers (0,1,2,3,4 order terms)', units='none', type='MATRIX', group='solarfield', required='*')
    IAM_L: Matrix = INPUT(label='(boiler, SH) Longitudinal Incident angle modifiers (0,1,2,3,4 order terms)', units='none', type='MATRIX', group='solarfield', required='*')
    TrackingError: Matrix = INPUT(label='(boiler, SH) User-defined tracking error derate', units='none', type='MATRIX', group='solarfield', required='*')
    GeomEffects: Matrix = INPUT(label='(boiler, SH) User-defined geometry effects derate', units='none', type='MATRIX', group='solarfield', required='*')
    rho_mirror_clean: Matrix = INPUT(label='(boiler, SH) User-defined clean mirror reflectivity', units='none', type='MATRIX', group='solarfield', required='*')
    dirt_mirror: Matrix = INPUT(label='(boiler, SH) User-defined dirt on mirror derate', units='none', type='MATRIX', group='solarfield', required='*')
    error: Matrix = INPUT(label='(boiler, SH) User-defined general optical error derate', units='none', type='MATRIX', group='solarfield', required='*')
    HLCharType: Matrix = INPUT(label='(boiler, SH) Flag indicating the heat loss model type {1=poly.; 2=Forristall}', units='none', type='MATRIX', group='solarfield', required='*')
    HL_dT: Matrix = INPUT(label='(boiler, SH) Heat loss coefficient - HTF temperature (0,1,2,3,4 order terms)', units='W/m-K^order', type='MATRIX', group='solarfield', required='*')
    HL_W: Matrix = INPUT(label='(boiler, SH) Heat loss coef adj wind velocity (0,1,2,3,4 order terms)', units='1/(m/s)^order', type='MATRIX', group='solarfield', required='*')
    D_2: Matrix = INPUT(label='(boiler, SH) The inner absorber tube diameter', units='m', type='MATRIX', group='solarfield', required='*')
    D_3: Matrix = INPUT(label='(boiler, SH) The outer absorber tube diameter', units='m', type='MATRIX', group='solarfield', required='*')
    D_4: Matrix = INPUT(label='(boiler, SH) The inner glass envelope diameter', units='m', type='MATRIX', group='solarfield', required='*')
    D_5: Matrix = INPUT(label='(boiler, SH) The outer glass envelope diameter', units='m', type='MATRIX', group='solarfield', required='*')
    D_p: Matrix = INPUT(label='(boiler, SH) The diameter of the absorber flow plug (optional)', units='m', type='MATRIX', group='solarfield', required='*')
    Rough: Matrix = INPUT(label='(boiler, SH) Roughness of the internal surface', units='m', type='MATRIX', group='solarfield', required='*')
    Flow_type: Matrix = INPUT(label='(boiler, SH) The flow type through the absorber', units='none', type='MATRIX', group='solarfield', required='*')
    AbsorberMaterial: Matrix = INPUT(label='(boiler, SH) Absorber material type', units='none', type='MATRIX', group='solarfield', required='*')
    HCE_FieldFrac: Matrix = INPUT(label='(boiler, SH) The fraction of the field occupied by this HCE type (4: # field fracs)', units='none', type='MATRIX', group='solarfield', required='*')
    alpha_abs: Matrix = INPUT(label='(boiler, SH) Absorber absorptance (4: # field fracs)', units='none', type='MATRIX', group='solarfield', required='*')
    b_eps_HCE1: Matrix = INPUT(label='(temperature) Absorber emittance (eps)', units='none', type='MATRIX', group='solarfield', required='*')
    b_eps_HCE2: Matrix = INPUT(label='(temperature) Absorber emittance (eps)', units='none', type='MATRIX', group='solarfield', required='*')
    b_eps_HCE3: Matrix = INPUT(label='(temperature) Absorber emittance (eps)', units='none', type='MATRIX', group='solarfield', required='*')
    b_eps_HCE4: Matrix = INPUT(label='(temperature) Absorber emittance (eps)', units='none', type='MATRIX', group='solarfield', required='*')
    sh_eps_HCE1: Matrix = INPUT(label='(temperature) Absorber emittance (eps)', units='none', type='MATRIX', group='solarfield', required='*')
    sh_eps_HCE2: Matrix = INPUT(label='(temperature) Absorber emittance (eps)', units='none', type='MATRIX', group='solarfield', required='*')
    sh_eps_HCE3: Matrix = INPUT(label='(temperature) Absorber emittance (eps)', units='none', type='MATRIX', group='solarfield', required='*')
    sh_eps_HCE4: Matrix = INPUT(label='(temperature) Absorber emittance (eps)', units='none', type='MATRIX', group='solarfield', required='*')
    alpha_env: Matrix = INPUT(label='(boiler, SH) Envelope absorptance (4: # field fracs)', units='none', type='MATRIX', group='solarfield', required='*')
    EPSILON_4: Matrix = INPUT(label='(boiler, SH) Inner glass envelope emissivities (Pyrex) (4: # field fracs)', units='none', type='MATRIX', group='solarfield', required='*')
    Tau_envelope: Matrix = INPUT(label='(boiler, SH) Envelope transmittance (4: # field fracs)', units='none', type='MATRIX', group='solarfield', required='*')
    GlazingIntactIn: Matrix = INPUT(label='(boiler, SH) The glazing intact flag {true=0; false=1} (4: # field fracs)', units='none', type='MATRIX', group='solarfield', required='*')
    AnnulusGas: Matrix = INPUT(label='(boiler, SH) Annulus gas type {1=air; 26=Ar; 27=H2} (4: # field fracs)', units='none', type='MATRIX', group='solarfield', required='*')
    P_a: Matrix = INPUT(label='(boiler, SH) Annulus gas pressure (4: # field fracs)', units='torr', type='MATRIX', group='solarfield', required='*')
    Design_loss: Matrix = INPUT(label='(boiler, SH) Receiver heat loss at design (4: # field fracs)', units='W/m', type='MATRIX', group='solarfield', required='*')
    Shadowing: Matrix = INPUT(label='(boiler, SH) Receiver bellows shadowing loss factor (4: # field fracs)', units='none', type='MATRIX', group='solarfield', required='*')
    Dirt_HCE: Matrix = INPUT(label='(boiler, SH) Loss due to dirt on the receiver envelope (4: # field fracs)', units='none', type='MATRIX', group='solarfield', required='*')
    b_OpticalTable: Matrix = INPUT(label='Values of the optical efficiency table', units='none', type='MATRIX', group='solarfield', required='*')
    sh_OpticalTable: Matrix = INPUT(label='Values of the optical efficiency table', units='none', type='MATRIX', group='solarfield', required='*')
    dnifc: float = INPUT(label='Forecast DNI', units='W/m2', type='NUMBER', group='solarfield', required='*')
    I_bn: float = INPUT(label='Beam normal radiation (input kJ/m2-hr)', units='W/m2', type='NUMBER', group='solarfield', required='*')
    T_db: float = INPUT(label='Dry bulb air temperature', units='C', type='NUMBER', group='solarfield', required='*')
    T_dp: float = INPUT(label='The dewpoint temperature', units='C', type='NUMBER', group='solarfield', required='*')
    P_amb: float = INPUT(label='Ambient pressure', units='atm', type='NUMBER', group='solarfield', required='*')
    V_wind: float = INPUT(label='Ambient windspeed', units='m/s', type='NUMBER', group='solarfield', required='*')
    m_dot_htf_ref: float = INPUT(label='Reference HTF flow rate at design conditions', units='kg/hr', type='NUMBER', group='solarfield', required='*')
    m_pb_demand: float = INPUT(label='Demand htf flow from the power block', units='kg/hr', type='NUMBER', group='solarfield', required='*')
    shift: float = INPUT(label='Shift in longitude from local standard meridian', units='deg', type='NUMBER', group='solarfield', required='*')
    SolarAz_init: float = INPUT(label='Solar azimuth angle', units='deg', type='NUMBER', group='solarfield', required='*')
    SolarZen: float = INPUT(label='Solar zenith angle', units='deg', type='NUMBER', group='solarfield', required='*')
    T_pb_out_init: float = INPUT(label='Fluid temperature from the power block', units='C', type='NUMBER', group='solarfield', required='*')
    eta_ref: float = INPUT(label='Reference conversion efficiency at design condition', units='none', type='NUMBER', group='powerblock', required='*')
    T_cold_ref: float = INPUT(label='Reference HTF outlet temperature at design', units='C', type='NUMBER', group='powerblock', required='*')
    dT_cw_ref: float = INPUT(label='Reference condenser cooling water inlet/outlet T diff', units='C', type='NUMBER', group='powerblock', required='*')
    T_amb_des: float = INPUT(label='Reference ambient temperature at design point', units='C', type='NUMBER', group='powerblock', required='*')
    P_boil_des: float = INPUT(label='Boiler operating pressure @ design', units='bar', type='NUMBER', group='powerblock', required='*')
    P_rh_ref: float = INPUT(label='Reheater operating pressure at design', units='bar', type='NUMBER', group='powerblock', required='*')
    rh_frac_ref: float = INPUT(label='Reheater flow fraction at design', units='none', type='NUMBER', group='powerblock', required='*')
    CT: float = INPUT(label='Flag for using dry cooling or wet cooling system', units='none', type='NUMBER', group='powerblock', required='*', constraints='INTEGER')
    startup_time: float = INPUT(label='Time needed for power block startup', units='hr', type='NUMBER', group='powerblock', required='*')
    startup_frac: float = INPUT(label='Fraction of design thermal power needed for startup', units='none', type='NUMBER', group='powerblock', required='*')
    T_approach: float = INPUT(label='Cooling tower approach temperature', units='C', type='NUMBER', group='powerblock', required='*')
    T_ITD_des: float = INPUT(label='ITD at design for dry system', units='C', type='NUMBER', group='powerblock', required='*')
    P_cond_ratio: float = INPUT(label='Condenser pressure ratio', units='none', type='NUMBER', group='powerblock', required='*')
    pb_bd_frac: float = INPUT(label='Power block blowdown steam fraction ', units='none', type='NUMBER', group='powerblock', required='*')
    P_cond_min: float = INPUT(label='Minimum condenser pressure', units='inHg', type='NUMBER', group='powerblock', required='*')
    n_pl_inc: float = INPUT(label='Number of part-load increments for the heat rejection system', units='none', type='NUMBER', group='powerblock', required='*', constraints='INTEGER')
    F_wc: Array = INPUT(label='Fraction indicating wet cooling use for hybrid system', units='none', type='ARRAY', group='powerblock', required='*')
    pc_mode: float = INPUT(label='Cycle part load control, from plant controller', units='none', type='NUMBER', group='powerblock', required='*')
    T_hot: float = INPUT(label='Hot HTF inlet temperature, from storage tank', units='C', type='NUMBER', group='powerblock', required='*')
    m_dot_st: float = INPUT(label='HTF mass flow rate', units='kg/hr', type='NUMBER', group='powerblock', required='*')
    T_wb: float = INPUT(label='Ambient wet bulb temperature', units='C', type='NUMBER', group='powerblock', required='*')
    demand_var: float = INPUT(label='Control signal indicating operational mode', units='none', type='NUMBER', group='powerblock', required='*')
    standby_control: float = INPUT(label='Control signal indicating standby mode', units='none', type='NUMBER', group='powerblock', required='*')
    T_db_pwb: float = INPUT(label='Ambient dry bulb temperature', units='C', type='NUMBER', group='powerblock', required='*')
    P_amb_pwb: float = INPUT(label='Ambient pressure', units='atm', type='NUMBER', group='powerblock', required='*')
    relhum: float = INPUT(label='Relative humidity of the ambient air', units='none', type='NUMBER', group='powerblock', required='*')
    f_recSU: float = INPUT(label='Fraction powerblock can run due to receiver startup', units='none', type='NUMBER', group='powerblock', required='*')
    dp_b: float = INPUT(label='Pressure drop in boiler', units='Pa', type='NUMBER', group='powerblock', required='*')
    dp_sh: float = INPUT(label='Pressure drop in superheater', units='Pa', type='NUMBER', group='powerblock', required='*')
    dp_rh: float = INPUT(label='Pressure drop in reheater', units='Pa', type='NUMBER', group='powerblock', required='*')
    month: Final[Array] = OUTPUT(label='Resource Month', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    hour: Final[Array] = OUTPUT(label='Resource Hour of Day', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    solazi: Final[Array] = OUTPUT(label='Resource Solar Azimuth', units='deg', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    solzen: Final[Array] = OUTPUT(label='Resource Solar Zenith', units='deg', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    beam: Final[Array] = OUTPUT(label='Resource Beam normal irradiance', units='W/m2', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    tdry: Final[Array] = OUTPUT(label='Resource Dry bulb temperature', units='C', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    twet: Final[Array] = OUTPUT(label='Resource Wet bulb temperature', units='C', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    wspd: Final[Array] = OUTPUT(label='Resource Wind Speed', units='m/s', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    pres: Final[Array] = OUTPUT(label='Resource Pressure', units='mbar', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    tou_value: Final[Array] = OUTPUT(label='Resource Time-of-use value', type='ARRAY', group='tou', required='*', constraints='LENGTH=8760')
    defocus: Final[Array] = OUTPUT(label='Field collector focus fraction', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    eta_opt_ave: Final[Array] = OUTPUT(label='Field collector optical efficiency', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    eta_thermal: Final[Array] = OUTPUT(label='Field thermal efficiency', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    eta_sf: Final[Array] = OUTPUT(label='Field efficiency total', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_inc_tot: Final[Array] = OUTPUT(label='Field thermal power incident', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_loss_rec: Final[Array] = OUTPUT(label='Field thermal power receiver loss', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_loss_piping: Final[Array] = OUTPUT(label='Field thermal power header pipe loss', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_loss_sf: Final[Array] = OUTPUT(label='Field thermal power loss', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_field_delivered: Final[Array] = OUTPUT(label='Field thermal power produced', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    m_dot_field: Final[Array] = OUTPUT(label='Field steam mass flow rate', units='kg/hr', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    m_dot_b_tot: Final[Array] = OUTPUT(label='Field steam mass flow rate - boiler', units='kg/hr', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    m_dot: Final[Array] = OUTPUT(label='Field steam mass flow rate - loop', units='kg/s', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_sf_in: Final[Array] = OUTPUT(label='Field steam pressure at inlet', units='bar', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    dP_tot: Final[Array] = OUTPUT(label='Field steam pressure loss', units='bar', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    T_field_in: Final[Array] = OUTPUT(label='Field steam temperature at header inlet', units='C', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    T_loop_out: Final[Array] = OUTPUT(label='Field steam temperature at collector outlet', units='C', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    T_field_out: Final[Array] = OUTPUT(label='Field steam temperature at header outlet', units='C', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    eta: Final[Array] = OUTPUT(label='Cycle efficiency (gross)', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    W_net: Final[Array] = OUTPUT(label='Cycle electrical power output (net)', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    W_cycle_gross: Final[Array] = OUTPUT(label='Cycle electrical power output (gross)', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    m_dot_to_pb: Final[Array] = OUTPUT(label='Cycle steam mass flow rate', units='kg/hr', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_turb_in: Final[Array] = OUTPUT(label='Cycle steam pressure at inlet', units='bar', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    T_pb_in: Final[Array] = OUTPUT(label='Cycle steam temperature at inlet', units='C', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    T_pb_out: Final[Array] = OUTPUT(label='Cycle steam temperature at outlet', units='C', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    E_bal_startup: Final[Array] = OUTPUT(label='Cycle thermal energy startup', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_dump: Final[Array] = OUTPUT(label='Cycle thermal energy dumped', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_to_pb: Final[Array] = OUTPUT(label='Cycle thermal power input', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    m_dot_makeup: Final[Array] = OUTPUT(label='Cycle cooling water mass flow rate - makeup', units='kg/hr', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_cond: Final[Array] = OUTPUT(label='Condenser pressure', units='Pa', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    f_bays: Final[Array] = OUTPUT(label='Condenser fraction of operating bays', units='none', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_aux_fluid: Final[Array] = OUTPUT(label='Fossil thermal power produced', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    m_dot_aux: Final[Array] = OUTPUT(label='Fossil steam mass flow rate', units='kg/hr', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_aux_fuel: Final[Array] = OUTPUT(label='Fossil fuel usage', units='MMBTU', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    W_dot_pump: Final[Array] = OUTPUT(label='Parasitic power solar field pump', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    W_dot_col: Final[Array] = OUTPUT(label='Parasitic power field collector drives', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    W_dot_bop: Final[Array] = OUTPUT(label='Parasitic power generation-dependent load', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    W_dot_fixed: Final[Array] = OUTPUT(label='Parasitic power fixed load', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    W_dot_aux: Final[Array] = OUTPUT(label='Parasitic power auxiliary heater operation', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    W_cool_par: Final[Array] = OUTPUT(label='Parasitic power condenser operation', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    monthly_energy: Final[Array] = OUTPUT(label='Monthly Energy', units='kWh', type='ARRAY', group='Linear Fresnel', required='*', constraints='LENGTH=12')
    annual_energy: Final[float] = OUTPUT(label='Annual Energy', units='kWh', type='NUMBER', group='Linear Fresnel', required='*')
    annual_W_cycle_gross: Final[float] = OUTPUT(label='Electrical source - Power cycle gross output', units='kWh', type='NUMBER', group='Linear Fresnel', required='*')
    conversion_factor: Final[float] = OUTPUT(label='Gross to Net Conversion Factor', units='%', type='NUMBER', group='Calculated', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', required='*')
    annual_total_water_use: Final[float] = OUTPUT(label='Total Annual Water Usage: cycle + mirror washing', units='m3', type='NUMBER', group='PostProcess', required='*')
    kwh_per_kw: Final[float] = OUTPUT(label='First year kWh/kW', units='kWh/kW', type='NUMBER', required='*')
    system_heat_rate: Final[float] = OUTPUT(label='System heat rate', units='MMBtu/MWh', type='NUMBER', required='*')
    annual_fuel_usage: Final[float] = OUTPUT(label='Annual fuel usage', units='kWh', type='NUMBER', required='*')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    gen: Final[Array] = OUTPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 file_name: str = ...,
                 track_mode: float = ...,
                 tilt: float = ...,
                 azimuth: float = ...,
                 system_capacity: float = ...,
                 weekday_schedule: Matrix = ...,
                 weekend_schedule: Matrix = ...,
                 tes_hours: float = ...,
                 q_max_aux: float = ...,
                 LHV_eff: float = ...,
                 x_b_des: float = ...,
                 P_turb_des: float = ...,
                 fP_hdr_c: float = ...,
                 fP_sf_boil: float = ...,
                 fP_boil_to_sh: float = ...,
                 fP_sf_sh: float = ...,
                 fP_hdr_h: float = ...,
                 q_pb_des: float = ...,
                 cycle_max_fraction: float = ...,
                 cycle_cutoff_frac: float = ...,
                 t_sby: float = ...,
                 q_sby_frac: float = ...,
                 solarm: float = ...,
                 PB_pump_coef: float = ...,
                 PB_fixed_par: float = ...,
                 bop_array: Array = ...,
                 aux_array: Array = ...,
                 fossil_mode: float = ...,
                 I_bn_des: float = ...,
                 is_sh: float = ...,
                 is_oncethru: float = ...,
                 is_multgeom: float = ...,
                 nModBoil: float = ...,
                 nModSH: float = ...,
                 nLoops: float = ...,
                 eta_pump: float = ...,
                 latitude: float = ...,
                 theta_stow: float = ...,
                 theta_dep: float = ...,
                 m_dot_min: float = ...,
                 T_fp: float = ...,
                 Pipe_hl_coef: float = ...,
                 SCA_drives_elec: float = ...,
                 ColAz: float = ...,
                 e_startup: float = ...,
                 T_amb_des_sf: float = ...,
                 V_wind_max: float = ...,
                 csp_lf_sf_water_per_wash: float = ...,
                 csp_lf_sf_washes_per_year: float = ...,
                 ffrac: Array = ...,
                 A_aperture: Matrix = ...,
                 L_col: Matrix = ...,
                 OptCharType: Matrix = ...,
                 IAM_T: Matrix = ...,
                 IAM_L: Matrix = ...,
                 TrackingError: Matrix = ...,
                 GeomEffects: Matrix = ...,
                 rho_mirror_clean: Matrix = ...,
                 dirt_mirror: Matrix = ...,
                 error: Matrix = ...,
                 HLCharType: Matrix = ...,
                 HL_dT: Matrix = ...,
                 HL_W: Matrix = ...,
                 D_2: Matrix = ...,
                 D_3: Matrix = ...,
                 D_4: Matrix = ...,
                 D_5: Matrix = ...,
                 D_p: Matrix = ...,
                 Rough: Matrix = ...,
                 Flow_type: Matrix = ...,
                 AbsorberMaterial: Matrix = ...,
                 HCE_FieldFrac: Matrix = ...,
                 alpha_abs: Matrix = ...,
                 b_eps_HCE1: Matrix = ...,
                 b_eps_HCE2: Matrix = ...,
                 b_eps_HCE3: Matrix = ...,
                 b_eps_HCE4: Matrix = ...,
                 sh_eps_HCE1: Matrix = ...,
                 sh_eps_HCE2: Matrix = ...,
                 sh_eps_HCE3: Matrix = ...,
                 sh_eps_HCE4: Matrix = ...,
                 alpha_env: Matrix = ...,
                 EPSILON_4: Matrix = ...,
                 Tau_envelope: Matrix = ...,
                 GlazingIntactIn: Matrix = ...,
                 AnnulusGas: Matrix = ...,
                 P_a: Matrix = ...,
                 Design_loss: Matrix = ...,
                 Shadowing: Matrix = ...,
                 Dirt_HCE: Matrix = ...,
                 b_OpticalTable: Matrix = ...,
                 sh_OpticalTable: Matrix = ...,
                 dnifc: float = ...,
                 I_bn: float = ...,
                 T_db: float = ...,
                 T_dp: float = ...,
                 P_amb: float = ...,
                 V_wind: float = ...,
                 m_dot_htf_ref: float = ...,
                 m_pb_demand: float = ...,
                 shift: float = ...,
                 SolarAz_init: float = ...,
                 SolarZen: float = ...,
                 T_pb_out_init: float = ...,
                 eta_ref: float = ...,
                 T_cold_ref: float = ...,
                 dT_cw_ref: float = ...,
                 T_amb_des: float = ...,
                 P_boil_des: float = ...,
                 P_rh_ref: float = ...,
                 rh_frac_ref: float = ...,
                 CT: float = ...,
                 startup_time: float = ...,
                 startup_frac: float = ...,
                 T_approach: float = ...,
                 T_ITD_des: float = ...,
                 P_cond_ratio: float = ...,
                 pb_bd_frac: float = ...,
                 P_cond_min: float = ...,
                 n_pl_inc: float = ...,
                 F_wc: Array = ...,
                 pc_mode: float = ...,
                 T_hot: float = ...,
                 m_dot_st: float = ...,
                 T_wb: float = ...,
                 demand_var: float = ...,
                 standby_control: float = ...,
                 T_db_pwb: float = ...,
                 P_amb_pwb: float = ...,
                 relhum: float = ...,
                 f_recSU: float = ...,
                 dp_b: float = ...,
                 dp_sh: float = ...,
                 dp_rh: float = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
