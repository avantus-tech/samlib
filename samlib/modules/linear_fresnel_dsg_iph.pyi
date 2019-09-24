
# This is a generated file

"""linear_fresnel_dsg_iph - CSP model using the linear fresnel TCS types."""

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
        'I_bn_des': float,
        'T_cold_ref': float,
        'P_turb_des': float,
        'T_hot': float,
        'x_b_des': float,
        'q_pb_des': float,
        'fP_hdr_c': float,
        'fP_sf_boil': float,
        'fP_hdr_h': float,
        'nModBoil': float,
        'nLoops': float,
        'eta_pump': float,
        'theta_stow': float,
        'theta_dep': float,
        'T_fp': float,
        'Pipe_hl_coef': float,
        'SCA_drives_elec': float,
        'ColAz': float,
        'e_startup': float,
        'T_amb_des_sf': float,
        'V_wind_max': float,
        'csp.lf.sf.water_per_wash': float,
        'csp.lf.sf.washes_per_year': float,
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
        'heat_sink_dP_frac': float,
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
        'theta_traverse': Array,
        'theta_longitudinal': Array,
        'eta_opt_ave': Array,
        'defocus': Array,
        'q_inc_sf_tot': Array,
        'q_dot_rec_inc': Array,
        'q_dot_rec_thermal_loss': Array,
        'q_dot_rec_abs': Array,
        'q_dot_piping_loss': Array,
        'e_dot_field_int_energy': Array,
        'q_dot_sf_out': Array,
        'q_dot_freeze_prot': Array,
        'm_dot_loop': Array,
        'm_dot_field': Array,
        'T_field_cold_in': Array,
        'T_rec_cold_in': Array,
        'T_rec_hot_out': Array,
        'x_rec_hot_out': Array,
        'T_field_hot_out': Array,
        'x_field_hot_out': Array,
        'deltaP_field': Array,
        'W_dot_sca_track': Array,
        'W_dot_field_pump': Array,
        'q_dot_to_heat_sink': Array,
        'W_dot_heat_sink_pump': Array,
        'W_dot_parasitic_tot': Array,
        'op_mode_1': Array,
        'op_mode_2': Array,
        'op_mode_3': Array,
        'annual_energy': float,
        'annual_field_energy': float,
        'annual_thermal_consumption': float,
        'annual_electricity_consumption': float,
        'annual_total_water_use': float,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix,
        'gen': Array
    }, total=False)

class Data(ssc.DataDict):
    file_name: str = INPUT(label='local weather file path', type='STRING', group='Weather', required='*', constraints='LOCAL_FILE')
    I_bn_des: float = INPUT(label='Design point irradiation value', units='W/m2', type='NUMBER', group='solarfield', required='*')
    T_cold_ref: float = INPUT(label='Reference HTF outlet temperature at design', units='C', type='NUMBER', group='powerblock', required='*')
    P_turb_des: float = INPUT(label='Design-point turbine inlet pressure', units='bar', type='NUMBER', group='solarfield', required='*')
    T_hot: float = INPUT(label='Hot HTF inlet temperature, from storage tank', units='C', type='NUMBER', group='powerblock', required='*')
    x_b_des: float = INPUT(label='Design point boiler outlet steam quality', units='none', type='NUMBER', group='solarfield', required='*')
    q_pb_des: float = INPUT(label='Design heat input to the power block', units='MW', type='NUMBER', group='solarfield', required='*')
    fP_hdr_c: float = INPUT(label='Average design-point cold header pressure drop fraction', units='none', type='NUMBER', group='solarfield', required='*')
    fP_sf_boil: float = INPUT(label='Design-point pressure drop across the solar field boiler fraction', units='none', type='NUMBER', group='solarfield', required='*')
    fP_hdr_h: float = INPUT(label='Average design-point hot header pressure drop fraction', units='none', type='NUMBER', group='solarfield', required='*')
    nModBoil: float = INPUT(label='Number of modules in the boiler section', units='none', type='NUMBER', group='solarfield', required='*', constraints='INTEGER')
    nLoops: float = INPUT(label='Number of loops', units='none', type='NUMBER', group='solarfield', required='*')
    eta_pump: float = INPUT(label='Feedwater pump efficiency', units='none', type='NUMBER', group='solarfield', required='*')
    theta_stow: float = INPUT(label='stow angle', units='deg', type='NUMBER', group='solarfield', required='*')
    theta_dep: float = INPUT(label='deploy angle', units='deg', type='NUMBER', group='solarfield', required='*')
    T_fp: float = INPUT(label='Freeze protection temperature (heat trace activation temperature)', units='C', type='NUMBER', group='solarfield', required='*')
    Pipe_hl_coef: float = INPUT(label='Loss coefficient from the header.. runner pipe.. and non-HCE pipin', units='W/m2-K', type='NUMBER', group='solarfield', required='*')
    SCA_drives_elec: float = INPUT(label='Tracking power.. in Watts per m2', units='W/m2', type='NUMBER', group='solarfield', required='*')
    ColAz: float = INPUT(label='Collector azimuth angle', units='deg', type='NUMBER', group='solarfield', required='*')
    e_startup: float = INPUT(label='Thermal inertia contribution per sq meter of solar field', units='kJ/K-m2', type='NUMBER', group='solarfield', required='*')
    T_amb_des_sf: float = INPUT(label='Design-point ambient temperature', units='C', type='NUMBER', group='solarfield', required='*')
    V_wind_max: float = INPUT(label='Maximum allowable wind velocity before safety stow', units='m/s', type='NUMBER', group='solarfield', required='*')
    csp_lf_sf_water_per_wash: float = INPUT(name='csp.lf.sf.water_per_wash', label='Water usage per wash', units='L/m2_aper', type='NUMBER', group='heliostat', required='*')
    csp_lf_sf_washes_per_year: float = INPUT(name='csp.lf.sf.washes_per_year', label='Mirror washing frequency', units='-/year', type='NUMBER', group='heliostat', required='*')
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
    heat_sink_dP_frac: float = INPUT(label='Fractional pressure drop through heat sink', type='NUMBER', group='heat_sink', required='*')
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
    theta_traverse: Final[Array] = OUTPUT(label='Field traverse incidence angle', units='deg', type='ARRAY', group='dsg_field', required='*')
    theta_longitudinal: Final[Array] = OUTPUT(label='Field traverse incidence angle', units='deg', type='ARRAY', group='dsg_field', required='*')
    eta_opt_ave: Final[Array] = OUTPUT(label='Field optical efficiency before defocus', units='deg', type='ARRAY', group='dsg_field', required='*')
    defocus: Final[Array] = OUTPUT(label='Field collector focus fraction', type='ARRAY', group='dsg_field', required='*')
    q_inc_sf_tot: Final[Array] = OUTPUT(label='Field thermal power incident', units='MWt', type='ARRAY', group='dsg_field', required='*')
    q_dot_rec_inc: Final[Array] = OUTPUT(label='Receiver thermal power incident', units='MWt', type='ARRAY', group='dsg_field', required='*')
    q_dot_rec_thermal_loss: Final[Array] = OUTPUT(label='Receiver thermal losses', units='MWt', type='ARRAY', group='dsg_field', required='*')
    q_dot_rec_abs: Final[Array] = OUTPUT(label='Receiver thermal power absorbed', units='MWt', type='ARRAY', group='dsg_field', required='*')
    q_dot_piping_loss: Final[Array] = OUTPUT(label='Field piping thermal losses', units='MWt', type='ARRAY', group='dsg_field', required='*')
    e_dot_field_int_energy: Final[Array] = OUTPUT(label='Field change in material/htf internal energy', units='MWt', type='ARRAY', group='dsg_field', required='*')
    q_dot_sf_out: Final[Array] = OUTPUT(label='Field thermal power leaving in steam', units='MWt', type='ARRAY', group='dsg_field', required='*')
    q_dot_freeze_prot: Final[Array] = OUTPUT(label='Field freeze protection required', units='MWt', type='ARRAY', group='dsg_field', required='*')
    m_dot_loop: Final[Array] = OUTPUT(label='Receiver mass flow rate', units='kg/s', type='ARRAY', group='dsg_field', required='*')
    m_dot_field: Final[Array] = OUTPUT(label='Field total mass flow rate', units='kg/s', type='ARRAY', group='dsg_field', required='*')
    T_field_cold_in: Final[Array] = OUTPUT(label='Field timestep-averaged inlet temperature', units='C', type='ARRAY', group='dsg_field', required='*')
    T_rec_cold_in: Final[Array] = OUTPUT(label='Loop timestep-averaged inlet temperature', units='C', type='ARRAY', group='dsg_field', required='*')
    T_rec_hot_out: Final[Array] = OUTPUT(label='Loop timestep-averaged outlet temperature', units='C', type='ARRAY', group='dsg_field', required='*')
    x_rec_hot_out: Final[Array] = OUTPUT(label='Loop timestep-averaged outlet quality', type='ARRAY', group='dsg_field', required='*')
    T_field_hot_out: Final[Array] = OUTPUT(label='Field timestep-averaged outlet temperature', units='C', type='ARRAY', group='dsg_field', required='*')
    x_field_hot_out: Final[Array] = OUTPUT(label='Field timestep-averaged outlet quality', type='ARRAY', group='dsg_field', required='*')
    deltaP_field: Final[Array] = OUTPUT(label='Field pressure drop', units='bar', type='ARRAY', group='dsg_field', required='*')
    W_dot_sca_track: Final[Array] = OUTPUT(label='Field collector tracking power', units='MWe', type='ARRAY', group='dsg_field', required='*')
    W_dot_field_pump: Final[Array] = OUTPUT(label='Field htf pumping power', units='MWe', type='ARRAY', group='dsg_field', required='*')
    q_dot_to_heat_sink: Final[Array] = OUTPUT(label='Heat sink thermal power', units='MWt', type='ARRAY', group='Heat_Sink', required='*')
    W_dot_heat_sink_pump: Final[Array] = OUTPUT(label='Heat sink pumping power', units='MWe', type='ARRAY', group='Heat_Sink', required='*')
    W_dot_parasitic_tot: Final[Array] = OUTPUT(label='System total electrical parasitic', units='MWe', type='ARRAY', group='Controller', required='*')
    op_mode_1: Final[Array] = OUTPUT(label='1st operating mode', type='ARRAY', group='Controller', required='*')
    op_mode_2: Final[Array] = OUTPUT(label='2nd op. mode, if applicable', type='ARRAY', group='Controller', required='*')
    op_mode_3: Final[Array] = OUTPUT(label='3rd op. mode, if applicable', type='ARRAY', group='Controller', required='*')
    annual_energy: Final[float] = OUTPUT(label='Annual Net Thermal Energy Production w/ avail derate', units='kWt-hr', type='NUMBER', group='Post-process', required='*')
    annual_field_energy: Final[float] = OUTPUT(label='Annual Gross Thermal Energy Production w/ avail derate', units='kWt-hr', type='NUMBER', group='Post-process', required='*')
    annual_thermal_consumption: Final[float] = OUTPUT(label='Annual thermal freeze protection required', units='kWt-hr', type='NUMBER', group='Post-process', required='*')
    annual_electricity_consumption: Final[float] = OUTPUT(label='Annual electricity consumptoin w/ avail derate', units='kWe-hr', type='NUMBER', group='Post-process', required='*')
    annual_total_water_use: Final[float] = OUTPUT(label='Total Annual Water Usage', units='m^3', type='NUMBER', group='Post-process', required='*')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    gen: Final[Array] = OUTPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 file_name: str = ...,
                 I_bn_des: float = ...,
                 T_cold_ref: float = ...,
                 P_turb_des: float = ...,
                 T_hot: float = ...,
                 x_b_des: float = ...,
                 q_pb_des: float = ...,
                 fP_hdr_c: float = ...,
                 fP_sf_boil: float = ...,
                 fP_hdr_h: float = ...,
                 nModBoil: float = ...,
                 nLoops: float = ...,
                 eta_pump: float = ...,
                 theta_stow: float = ...,
                 theta_dep: float = ...,
                 T_fp: float = ...,
                 Pipe_hl_coef: float = ...,
                 SCA_drives_elec: float = ...,
                 ColAz: float = ...,
                 e_startup: float = ...,
                 T_amb_des_sf: float = ...,
                 V_wind_max: float = ...,
                 csp_lf_sf_water_per_wash: float = ...,
                 csp_lf_sf_washes_per_year: float = ...,
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
                 heat_sink_dP_frac: float = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
