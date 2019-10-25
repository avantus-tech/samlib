
# This is a generated file

"""trough_physical_process_heat - Physical trough process heat applications"""

# VERSION: 1

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
        'I_bn_des': float,
        'solar_mult': float,
        'T_loop_in_des': float,
        'T_loop_out': float,
        'q_pb_design': float,
        'tshours': float,
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
        'is_model_heat_sink_piping': float,
        'L_heat_sink_piping': float,
        'm_dot_htfmin': float,
        'm_dot_htfmax': float,
        'Fluid': float,
        'wind_stow_speed': float,
        'field_fl_props': Matrix,
        'T_fp': float,
        'V_hdr_max': float,
        'V_hdr_min': float,
        'Pipe_hl_coef': float,
        'SCA_drives_elec': float,
        'water_usage_per_wash': float,
        'washing_frequency': float,
        'accept_mode': float,
        'accept_init': float,
        'accept_loc': float,
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
        'pb_pump_coef': float,
        'init_hot_htf_percent': float,
        'h_tank': float,
        'cold_tank_max_heat': float,
        'u_tank': float,
        'tank_pairs': float,
        'cold_tank_Thtr': float,
        'h_tank_min': float,
        'hot_tank_Thtr': float,
        'hot_tank_max_heat': float,
        'time_hr': Array,
        'month': Array,
        'hour_day': Array,
        'solazi': Array,
        'solzen': Array,
        'beam': Array,
        'tdry': Array,
        'twet': Array,
        'wspd': Array,
        'pres': Array,
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
        'q_dot_to_heat_sink': Array,
        'W_dot_pc_pump': Array,
        'm_dot_htf_heat_sink': Array,
        'T_heat_sink_in': Array,
        'T_heat_sink_out': Array,
        'tank_losses': Array,
        'q_tes_heater': Array,
        'T_tes_hot': Array,
        'T_tes_cold': Array,
        'q_dc_tes': Array,
        'q_ch_tes': Array,
        'e_ch_tes': Array,
        'm_dot_tes_dc': Array,
        'm_dot_tes_ch': Array,
        'W_dot_parasitic_tot': Array,
        'op_mode_1': Array,
        'op_mode_2': Array,
        'op_mode_3': Array,
        'm_dot_balance': Array,
        'q_balance': Array,
        'annual_energy': float,
        'annual_gross_energy': float,
        'annual_thermal_consumption': float,
        'annual_electricity_consumption': float,
        'annual_total_water_use': float,
        'annual_field_freeze_protection': float,
        'annual_tes_freeze_protection': float,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix
}, total=False)

class Data(ssc.DataDict):
    file_name: str = INPUT(label='Local weather file with path', units='none', type='STRING', group='Weather', required='*', constraints='LOCAL_FILE')
    track_mode: float = INPUT(label='Tracking mode', units='none', type='NUMBER', group='Weather', required='*')
    tilt: float = INPUT(label='Tilt angle of surface/axis', units='none', type='NUMBER', group='Weather', required='*')
    azimuth: float = INPUT(label='Azimuth angle of surface/axis', units='none', type='NUMBER', group='Weather', required='*')
    I_bn_des: float = INPUT(label='Solar irradiation at design', units='C', type='NUMBER', group='solar_field', required='*')
    solar_mult: float = INPUT(label='Solar multiple', units='none', type='NUMBER', group='solar_field', required='*')
    T_loop_in_des: float = INPUT(label='Design loop inlet temperature', units='C', type='NUMBER', group='solar_field', required='*')
    T_loop_out: float = INPUT(label='Target loop outlet temperature', units='C', type='NUMBER', group='solar_field', required='*')
    q_pb_design: float = INPUT(label='Design heat input to power block', units='MWt', type='NUMBER', group='controller', required='*')
    tshours: float = INPUT(label='Equivalent full-load thermal storage hours', units='hr', type='NUMBER', group='system_design', required='*')
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
    is_model_heat_sink_piping: float = INPUT(label='Should model consider piping through heat sink?', units='none', type='NUMBER', group='solar_field', required='*')
    L_heat_sink_piping: float = INPUT(label='Length of piping (full mass flow) through heat sink (if applicable)', units='none', type='NUMBER', group='solar_field', required='*')
    m_dot_htfmin: float = INPUT(label='Minimum loop HTF flow rate', units='kg/s', type='NUMBER', group='solar_field', required='*')
    m_dot_htfmax: float = INPUT(label='Maximum loop HTF flow rate', units='kg/s', type='NUMBER', group='solar_field', required='*')
    Fluid: float = INPUT(label='Field HTF fluid ID number', units='none', type='NUMBER', group='solar_field', required='*')
    wind_stow_speed: float = INPUT(label='Trough wind stow speed', units='m/s', type='NUMBER', group='solar_field', required='?=50')
    field_fl_props: Matrix = INPUT(label='User defined field fluid property data', units='-', type='MATRIX', group='controller', required='*')
    T_fp: float = INPUT(label='Freeze protection temperature (heat trace activation temperature)', units='none', type='NUMBER', group='solar_field', required='*')
    V_hdr_max: float = INPUT(label='Maximum HTF velocity in the header at design', units='W/m2', type='NUMBER', group='solar_field', required='*')
    V_hdr_min: float = INPUT(label='Minimum HTF velocity in the header at design', units='m/s', type='NUMBER', group='solar_field', required='*')
    Pipe_hl_coef: float = INPUT(label='Loss coefficient from the header, runner pipe, and non-HCE piping', units='m/s', type='NUMBER', group='solar_field', required='*')
    SCA_drives_elec: float = INPUT(label='Tracking power, in Watts per SCA drive', units='W/m2-K', type='NUMBER', group='solar_field', required='*')
    water_usage_per_wash: float = INPUT(label='Water usage per wash', units='L/m2_aper', type='NUMBER', group='solar_field', required='*')
    washing_frequency: float = INPUT(label='Mirror washing frequency', units='-/year', type='NUMBER', group='solar_field', required='*')
    accept_mode: float = INPUT(label='Acceptance testing mode?', units='0/1', type='NUMBER', group='solar_field', required='*', meta='no/yes')
    accept_init: float = INPUT(label='In acceptance testing mode - require steady-state startup', units='none', type='NUMBER', group='solar_field', required='*')
    accept_loc: float = INPUT(label='In acceptance testing mode - temperature sensor location', units='1/2', type='NUMBER', group='solar_field', required='*', meta='hx/loop')
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
    pb_pump_coef: float = INPUT(label='Pumping power to move 1kg of HTF through PB loop', units='kW/kg', type='NUMBER', group='controller', required='*')
    init_hot_htf_percent: float = INPUT(label='Initial fraction of avail. vol that is hot', units='%', type='NUMBER', group='TES', required='*')
    h_tank: float = INPUT(label='Total height of tank (height of HTF when tank is full', units='m', type='NUMBER', group='TES', required='*')
    cold_tank_max_heat: float = INPUT(label='Rated heater capacity for cold tank heating', units='MW', type='NUMBER', group='TES', required='*')
    u_tank: float = INPUT(label='Loss coefficient from the tank', units='W/m2-K', type='NUMBER', group='TES', required='*')
    tank_pairs: float = INPUT(label='Number of equivalent tank pairs', units='-', type='NUMBER', group='TES', required='*', constraints='INTEGER')
    cold_tank_Thtr: float = INPUT(label='Minimum allowable cold tank HTF temp', units='C', type='NUMBER', group='TES', required='*')
    h_tank_min: float = INPUT(label='Minimum allowable HTF height in storage tank', units='m', type='NUMBER', group='TES_2tank', required='*')
    hot_tank_Thtr: float = INPUT(label='Minimum allowable hot tank HTF temp', units='C', type='NUMBER', group='TES_2tank', required='*')
    hot_tank_max_heat: float = INPUT(label='Rated heater capacity for hot tank heating', units='MW', type='NUMBER', group='TES_2tank', required='*')
    time_hr: Final[Array] = OUTPUT(label='Time at end of timestep', units='hr', type='ARRAY', group='Solver', required='*')
    month: Final[Array] = OUTPUT(label='Resource Month', type='ARRAY', group='weather', required='*')
    hour_day: Final[Array] = OUTPUT(label='Resource Hour of Day', type='ARRAY', group='weather', required='*')
    solazi: Final[Array] = OUTPUT(label='Resource Solar Azimuth', units='deg', type='ARRAY', group='weather', required='*')
    solzen: Final[Array] = OUTPUT(label='Resource Solar Zenith', units='deg', type='ARRAY', group='weather', required='*')
    beam: Final[Array] = OUTPUT(label='Resource Beam normal irradiance', units='W/m2', type='ARRAY', group='weather', required='*')
    tdry: Final[Array] = OUTPUT(label='Resource Dry bulb temperature', units='C', type='ARRAY', group='weather', required='*')
    twet: Final[Array] = OUTPUT(label='Resource Wet bulb temperature', units='C', type='ARRAY', group='weather', required='*')
    wspd: Final[Array] = OUTPUT(label='Resource Wind Speed', units='m/s', type='ARRAY', group='weather', required='*')
    pres: Final[Array] = OUTPUT(label='Resource Pressure', units='mbar', type='ARRAY', group='weather', required='*')
    Theta_ave: Final[Array] = OUTPUT(label='Field collector solar incidence angle', units='deg', type='ARRAY', group='trough_field', required='*')
    CosTh_ave: Final[Array] = OUTPUT(label='Field collector cosine efficiency', type='ARRAY', group='trough_field', required='*')
    IAM_ave: Final[Array] = OUTPUT(label='Field collector incidence angle modifier', type='ARRAY', group='trough_field', required='*')
    RowShadow_ave: Final[Array] = OUTPUT(label='Field collector row shadowing loss', type='ARRAY', group='trough_field', required='*')
    EndLoss_ave: Final[Array] = OUTPUT(label='Field collector optical end loss', type='ARRAY', group='trough_field', required='*')
    dni_costh: Final[Array] = OUTPUT(label='Field collector DNI-cosine product', units='W/m2', type='ARRAY', group='trough_field', required='*')
    EqOpteff: Final[Array] = OUTPUT(label='Field optical efficiency before defocus', type='ARRAY', group='trough_field', required='*')
    SCAs_def: Final[Array] = OUTPUT(label='Field fraction of focused SCAs', type='ARRAY', group='trough_field', required='*')
    q_inc_sf_tot: Final[Array] = OUTPUT(label='Field thermal power incident', units='MWt', type='ARRAY', group='trough_field', required='*')
    qinc_costh: Final[Array] = OUTPUT(label='Field thermal power incident after cosine', units='MWt', type='ARRAY', group='trough_field', required='*')
    q_dot_rec_inc: Final[Array] = OUTPUT(label='Receiver thermal power incident', units='MWt', type='ARRAY', group='trough_field', required='*')
    q_dot_rec_thermal_loss: Final[Array] = OUTPUT(label='Receiver thermal losses', units='MWt', type='ARRAY', group='trough_field', required='*')
    q_dot_rec_abs: Final[Array] = OUTPUT(label='Receiver thermal power absorbed', units='MWt', type='ARRAY', group='trough_field', required='*')
    q_dot_piping_loss: Final[Array] = OUTPUT(label='Field piping thermal losses', units='MWt', type='ARRAY', group='trough_field', required='*')
    e_dot_field_int_energy: Final[Array] = OUTPUT(label='Field change in material/htf internal energy', units='MWt', type='ARRAY', group='trough_field', required='*')
    q_dot_htf_sf_out: Final[Array] = OUTPUT(label='Field thermal power leaving in HTF', units='MWt', type='ARRAY', group='trough_field', required='*')
    q_dot_freeze_prot: Final[Array] = OUTPUT(label='Field freeze protection required', units='MWt', type='ARRAY', group='trough_field', required='*')
    m_dot_loop: Final[Array] = OUTPUT(label='Receiver mass flow rate', units='kg/s', type='ARRAY', group='trough_field', required='*')
    m_dot_field_recirc: Final[Array] = OUTPUT(label='Field total mass flow recirculated', units='kg/s', type='ARRAY', group='trough_field', required='*')
    m_dot_field_delivered: Final[Array] = OUTPUT(label='Field total mass flow delivered', units='kg/s', type='ARRAY', group='trough_field', required='*')
    T_field_cold_in: Final[Array] = OUTPUT(label='Field timestep-averaged inlet temperature', units='C', type='ARRAY', group='trough_field', required='*')
    T_rec_cold_in: Final[Array] = OUTPUT(label='Loop timestep-averaged inlet temperature', units='C', type='ARRAY', group='trough_field', required='*')
    T_rec_hot_out: Final[Array] = OUTPUT(label='Loop timestep-averaged outlet temperature', units='C', type='ARRAY', group='trough_field', required='*')
    T_field_hot_out: Final[Array] = OUTPUT(label='Field timestep-averaged outlet temperature', units='C', type='ARRAY', group='trough_field', required='*')
    deltaP_field: Final[Array] = OUTPUT(label='Field pressure drop', units='bar', type='ARRAY', group='trough_field', required='*')
    W_dot_sca_track: Final[Array] = OUTPUT(label='Field collector tracking power', units='MWe', type='ARRAY', group='trough_field', required='*')
    W_dot_field_pump: Final[Array] = OUTPUT(label='Field htf pumping power', units='MWe', type='ARRAY', group='trough_field', required='*')
    q_dot_to_heat_sink: Final[Array] = OUTPUT(label='Heat sink thermal power', units='MWt', type='ARRAY', group='Heat_Sink', required='*')
    W_dot_pc_pump: Final[Array] = OUTPUT(label='Heat sink pumping power', units='MWe', type='ARRAY', group='Heat_Sink', required='*')
    m_dot_htf_heat_sink: Final[Array] = OUTPUT(label='Heat sink HTF mass flow', units='kg/s', type='ARRAY', group='Heat_Sink', required='*')
    T_heat_sink_in: Final[Array] = OUTPUT(label='Heat sink HTF inlet temp', units='C', type='ARRAY', group='Heat_Sink', required='*')
    T_heat_sink_out: Final[Array] = OUTPUT(label='Heat sink HTF outlet temp', units='C', type='ARRAY', group='Heat_Sink', required='*')
    tank_losses: Final[Array] = OUTPUT(label='TES thermal losses', units='MWt', type='ARRAY', group='TES', required='*')
    q_tes_heater: Final[Array] = OUTPUT(label='TES freeze protection power', units='MWe', type='ARRAY', group='TES', required='*')
    T_tes_hot: Final[Array] = OUTPUT(label='TES hot temperature', units='C', type='ARRAY', group='TES', required='*')
    T_tes_cold: Final[Array] = OUTPUT(label='TES cold temperature', units='C', type='ARRAY', group='TES', required='*')
    q_dc_tes: Final[Array] = OUTPUT(label='TES discharge thermal power', units='MWt', type='ARRAY', group='TES', required='*')
    q_ch_tes: Final[Array] = OUTPUT(label='TES charge thermal power', units='MWt', type='ARRAY', group='TES', required='*')
    e_ch_tes: Final[Array] = OUTPUT(label='TES charge state', units='MWht', type='ARRAY', group='TES', required='*')
    m_dot_tes_dc: Final[Array] = OUTPUT(label='TES discharge mass flow rate', units='kg/s', type='ARRAY', group='TES', required='*')
    m_dot_tes_ch: Final[Array] = OUTPUT(label='TES charge mass flow rate', units='kg/s', type='ARRAY', group='TES', required='*')
    W_dot_parasitic_tot: Final[Array] = OUTPUT(label='System total electrical parasitic', units='MWe', type='ARRAY', group='Heat_Sink', required='*')
    op_mode_1: Final[Array] = OUTPUT(label='1st operating mode', type='ARRAY', group='Solver', required='*')
    op_mode_2: Final[Array] = OUTPUT(label='2nd op. mode, if applicable', type='ARRAY', group='Solver', required='*')
    op_mode_3: Final[Array] = OUTPUT(label='3rd op. mode, if applicable', type='ARRAY', group='Solver', required='*')
    m_dot_balance: Final[Array] = OUTPUT(label='Relative mass flow balance error', type='ARRAY', group='Controller', required='*')
    q_balance: Final[Array] = OUTPUT(label='Relative energy balance error', type='ARRAY', group='Controller', required='*')
    annual_energy: Final[float] = OUTPUT(label='Annual Net Thermal Energy Production w/ avail derate', units='kWt-hr', type='NUMBER', group='Post-process', required='*')
    annual_gross_energy: Final[float] = OUTPUT(label='Annual Gross Thermal Energy Production w/ avail derate', units='kWt-hr', type='NUMBER', group='Post-process', required='*')
    annual_thermal_consumption: Final[float] = OUTPUT(label='Annual thermal freeze protection required', units='kWt-hr', type='NUMBER', group='Post-process', required='*')
    annual_electricity_consumption: Final[float] = OUTPUT(label='Annual electricity consumptoin w/ avail derate', units='kWe-hr', type='NUMBER', group='Post-process', required='*')
    annual_total_water_use: Final[float] = OUTPUT(label='Total Annual Water Usage', units='m^3', type='NUMBER', group='Post-process', required='*')
    annual_field_freeze_protection: Final[float] = OUTPUT(label='Annual thermal power for field freeze protection', units='kWt-hr', type='NUMBER', group='Post-process', required='*')
    annual_tes_freeze_protection: Final[float] = OUTPUT(label='Annual thermal power for TES freeze protection', units='kWt-hr', type='NUMBER', group='Post-process', required='*')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')

    def __init__(self, *args: Mapping[str, Any],
                 file_name: str = ...,
                 track_mode: float = ...,
                 tilt: float = ...,
                 azimuth: float = ...,
                 I_bn_des: float = ...,
                 solar_mult: float = ...,
                 T_loop_in_des: float = ...,
                 T_loop_out: float = ...,
                 q_pb_design: float = ...,
                 tshours: float = ...,
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
                 is_model_heat_sink_piping: float = ...,
                 L_heat_sink_piping: float = ...,
                 m_dot_htfmin: float = ...,
                 m_dot_htfmax: float = ...,
                 Fluid: float = ...,
                 wind_stow_speed: float = ...,
                 field_fl_props: Matrix = ...,
                 T_fp: float = ...,
                 V_hdr_max: float = ...,
                 V_hdr_min: float = ...,
                 Pipe_hl_coef: float = ...,
                 SCA_drives_elec: float = ...,
                 water_usage_per_wash: float = ...,
                 washing_frequency: float = ...,
                 accept_mode: float = ...,
                 accept_init: float = ...,
                 accept_loc: float = ...,
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
                 pb_pump_coef: float = ...,
                 init_hot_htf_percent: float = ...,
                 h_tank: float = ...,
                 cold_tank_max_heat: float = ...,
                 u_tank: float = ...,
                 tank_pairs: float = ...,
                 cold_tank_Thtr: float = ...,
                 h_tank_min: float = ...,
                 hot_tank_Thtr: float = ...,
                 hot_tank_max_heat: float = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
