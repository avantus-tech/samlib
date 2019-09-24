
# This is a generated file

"""tcsdish - Dish Stirling model using the TCS types."""

# VERSION: 4

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
        'system_capacity': float,
        'd_ap': float,
        'rho': float,
        'n_ns': float,
        'n_ew': float,
        'ns_dish_sep': float,
        'ew_dish_sep': float,
        'slope_ns': float,
        'slope_ew': float,
        'w_slot_gap': float,
        'h_slot_gap': float,
        'wind_stow_speed': float,
        'A_proj': float,
        'I_cut_in': float,
        'd_ap_test': float,
        'test_if': float,
        'test_L_focal': float,
        'A_total': float,
        'rec_type': float,
        'transmittance_cover': float,
        'alpha_absorber': float,
        'A_absorber': float,
        'alpha_wall': float,
        'A_wall': float,
        'L_insulation': float,
        'k_insulation': float,
        'd_cav': float,
        'P_cav': float,
        'L_cav': float,
        'DELTA_T_DIR': float,
        'DELTA_T_REFLUX': float,
        'T_heater_head_high': float,
        'T_heater_head_low': float,
        'Beale_const_coef': float,
        'Beale_first_coef': float,
        'Beale_square_coef': float,
        'Beale_third_coef': float,
        'Beale_fourth_coef': float,
        'Pressure_coef': float,
        'Pressure_first': float,
        'engine_speed': float,
        'V_displaced': float,
        'T_compression_in': float,
        'cooling_tower_on': float,
        'tower_mode': float,
        'd_pipe_tower': float,
        'tower_m_dot_water': float,
        'tower_m_dot_water_test': float,
        'tower_pipe_material': float,
        'eta_tower_pump': float,
        'fan_control_signal': float,
        'epsilon_power_test': float,
        'system_availability': float,
        'pump_speed': float,
        'fan_speed1': float,
        'fan_speed2': float,
        'fan_speed3': float,
        'T_cool_speed2': float,
        'T_cool_speed3': float,
        'epsilon_cooler_test': float,
        'epsilon_radiator_test': float,
        'cooling_fluid': float,
        'P_controls': float,
        'test_P_pump': float,
        'test_pump_speed': float,
        'test_cooling_fluid': float,
        'test_T_fluid': float,
        'test_V_dot_fluid': float,
        'test_P_fan': float,
        'test_fan_speed': float,
        'test_fan_rho_air': float,
        'test_fan_cfm': float,
        'b_radiator': float,
        'b_cooler': float,
        'Tower_water_outlet_temp': float,
        'ns_dish_separation': float,
        'ew_dish_separation': float,
        'P_tower_fan': float,
        'month': Array,
        'hour': Array,
        'solazi': Array,
        'solzen': Array,
        'beam': Array,
        'tdry': Array,
        'twet': Array,
        'wspd': Array,
        'pres': Array,
        'Phi_shade': Array,
        'Collector_Losses': Array,
        'eta_collector': Array,
        'Power_in_collector': Array,
        'Power_out_col': Array,
        'Power_in_rec': Array,
        'P_out_rec': Array,
        'Q_rec_losses': Array,
        'eta_rec': Array,
        'T_heater_head_operate': Array,
        'net_power': Array,
        'P_out_SE': Array,
        'P_SE_losses': Array,
        'eta_SE': Array,
        'engine_pressure': Array,
        'T_compression': Array,
        'T_tower_out': Array,
        'T_tower_in': Array,
        'P_parasitic': Array,
        'eta_net': Array,
        'hourly_Power_in_collector': Array,
        'hourly_Power_out_col': Array,
        'hourly_Collector_Losses': Array,
        'hourly_Power_in_rec': Array,
        'hourly_Q_rec_losses': Array,
        'hourly_P_out_rec': Array,
        'hourly_P_out_SE': Array,
        'hourly_P_parasitic': Array,
        'annual_energy': float,
        'annual_Power_in_collector': float,
        'annual_Power_out_col': float,
        'annual_Power_in_rec': float,
        'annual_P_out_rec': float,
        'annual_P_out_SE': float,
        'annual_Collector_Losses': float,
        'annual_P_parasitic': float,
        'annual_Q_rec_losses': float,
        'monthly_energy': Array,
        'monthly_Power_in_collector': Array,
        'monthly_Power_out_col': Array,
        'monthly_Power_in_rec': Array,
        'monthly_P_out_rec': Array,
        'monthly_P_out_SE': Array,
        'monthly_Collector_Losses': Array,
        'monthly_P_parasitic': Array,
        'monthly_Q_rec_losses': Array,
        'conversion_factor': float,
        'capacity_factor': float,
        'kwh_per_kw': float,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix,
        'gen': Array
    }, total=False)

class Data(ssc.DataDict):
    file_name: str = INPUT(label='local weather file path', type='STRING', group='Weather', required='*', constraints='LOCAL_FILE')
    system_capacity: float = INPUT(label='Nameplate capacity', units='kW', type='NUMBER', group='dish', required='*')
    d_ap: float = INPUT(label='Dish aperture diameter', units='m', type='NUMBER', group='type295', required='*')
    rho: float = INPUT(label='Mirror surface reflectivity', units='-', type='NUMBER', group='type295', required='*')
    n_ns: float = INPUT(label='Number of collectors North-South', units='-', type='NUMBER', group='type295', required='*', constraints='INTEGER')
    n_ew: float = INPUT(label='Number of collectors East-West', units='-', type='NUMBER', group='type295', required='*', constraints='INTEGER')
    ns_dish_sep: float = INPUT(label='Collector separation North-South', units='m', type='NUMBER', group='type295', required='*')
    ew_dish_sep: float = INPUT(label='Collector separation East-West', units='m', type='NUMBER', group='type295', required='*')
    slope_ns: float = INPUT(label='North-South ground slope', units='%', type='NUMBER', group='type295', required='*')
    slope_ew: float = INPUT(label='East-West ground slope', units='%', type='NUMBER', group='type295', required='*')
    w_slot_gap: float = INPUT(label='Slot gap width', units='m', type='NUMBER', group='type295', required='*')
    h_slot_gap: float = INPUT(label='Slot gap height', units='m', type='NUMBER', group='type295', required='*')
    wind_stow_speed: float = INPUT(label='Wind stow speed', units='m/s', type='NUMBER', group='type295', required='*')
    A_proj: float = INPUT(label='Projected mirror area', units='m^2', type='NUMBER', group='type295', required='*')
    I_cut_in: float = INPUT(label='Insolation cut in value', units='W/m^2', type='NUMBER', group='type295', required='*')
    d_ap_test: float = INPUT(label='Receiver aperture diameter during test', units='m', type='NUMBER', group='type295', required='*')
    test_if: float = INPUT(label='Test intercept factor', units='-', type='NUMBER', group='type295', required='*')
    test_L_focal: float = INPUT(label='Focal length of mirror system', units='m', type='NUMBER', group='type295', required='*')
    A_total: float = INPUT(label='Total Area', units='m^2', type='NUMBER', group='type295', required='*')
    rec_type: float = INPUT(label='Receiver type (always = 1)', units='-', type='NUMBER', group='type296', required='*')
    transmittance_cover: float = INPUT(label='Transmittance cover (always = 1)', units='-', type='NUMBER', group='type296', required='*')
    alpha_absorber: float = INPUT(label='Absorber absorptance', units='-', type='NUMBER', group='type296', required='*')
    A_absorber: float = INPUT(label='Absorber surface area', units='m^2', type='NUMBER', group='type296', required='*')
    alpha_wall: float = INPUT(label='Cavity absorptance', units='-', type='NUMBER', group='type296', required='*')
    A_wall: float = INPUT(label='Cavity surface area', units='m^2', type='NUMBER', group='type296', required='*')
    L_insulation: float = INPUT(label='Insulation thickness', units='m', type='NUMBER', group='type296', required='*')
    k_insulation: float = INPUT(label='Insulation thermal conductivity', units='W/m-K', type='NUMBER', group='type296', required='*')
    d_cav: float = INPUT(label='Internal diameter of cavity perp to aperture', units='m', type='NUMBER', group='type296', required='*')
    P_cav: float = INPUT(label='Internal cavity pressure with aperture covered', units='kPa', type='NUMBER', group='type296', required='*')
    L_cav: float = INPUT(label='Internal depth of cavity perp to aperture', units='m', type='NUMBER', group='type296', required='*')
    DELTA_T_DIR: float = INPUT(label='Delta temperature for DIR receiver', units='K', type='NUMBER', group='type296', required='*')
    DELTA_T_REFLUX: float = INPUT(label='Delta temp for REFLUX receiver (always = 40)', units='K', type='NUMBER', group='type296', required='*')
    T_heater_head_high: float = INPUT(label='Heater Head Set Temperature', units='K', type='NUMBER', group='type296', required='*')
    T_heater_head_low: float = INPUT(label='Header Head Lowest Temperature', units='K', type='NUMBER', group='type296', required='*')
    Beale_const_coef: float = INPUT(label='Beale Constant Coefficient', units='-', type='NUMBER', group='type297', required='*')
    Beale_first_coef: float = INPUT(label='Beale first-order coefficient', units='1/W', type='NUMBER', group='type297', required='*')
    Beale_square_coef: float = INPUT(label='Beale second-order coefficient', units='1/W^2', type='NUMBER', group='type297', required='*')
    Beale_third_coef: float = INPUT(label='Beale third-order coefficient', units='1/W^3', type='NUMBER', group='type297', required='*')
    Beale_fourth_coef: float = INPUT(label='Beale fourth-order coefficient', units='1/W^4', type='NUMBER', group='type297', required='*')
    Pressure_coef: float = INPUT(label='Pressure constant coefficient', units='MPa', type='NUMBER', group='type297', required='*')
    Pressure_first: float = INPUT(label='Pressure first-order coefficient', units='MPa/W', type='NUMBER', group='type297', required='*')
    engine_speed: float = INPUT(label='Engine operating speed', units='rpm', type='NUMBER', group='type297', required='*')
    V_displaced: float = INPUT(label='Displaced engine volume', units='m3', type='NUMBER', group='type297', required='*')
    T_compression_in: float = INPUT(label='Receiver efficiency', units='C', type='NUMBER', group='type297', required='*')
    cooling_tower_on: float = INPUT(label='Option to use a cooling tower (set to 0=off)', units='-', type='NUMBER', group='type298', required='*')
    tower_mode: float = INPUT(label='Cooling tower type (natural or forced draft)', units='-', type='NUMBER', group='type298', required='*')
    d_pipe_tower: float = INPUT(label='Runner pipe diameter to the cooling tower (set to 0.4m)', units='m', type='NUMBER', group='type298', required='*')
    tower_m_dot_water: float = INPUT(label='Tower cooling water flow rate (set to 134,000 kg/hr)', units='kg/s', type='NUMBER', group='type298', required='*')
    tower_m_dot_water_test: float = INPUT(label='Test value for the cooling water flow rate (set to 134,000 kg/hr)', units='kg/s', type='NUMBER', group='type298', required='*')
    tower_pipe_material: float = INPUT(label='Tower pipe material (1=plastic, 2=new cast iron, 3=riveted steel)', units='-', type='NUMBER', group='type298', required='*')
    eta_tower_pump: float = INPUT(label='Tower pump efficiency (set to 0.6)', units='-', type='NUMBER', group='type298', required='*')
    fan_control_signal: float = INPUT(label='Fan control signal (set to 1, not used in this model)', units='-', type='NUMBER', group='type298', required='*')
    epsilon_power_test: float = INPUT(label='Test value for cooling tower effectiveness (set to 0.7)', units='-', type='NUMBER', group='type298', required='*')
    system_availability: float = INPUT(label='System availability (set to 1.0)', units='-', type='NUMBER', group='type298', required='*')
    pump_speed: float = INPUT(label='Reference Condition Pump Speed', units='rpm', type='NUMBER', group='type298', required='*')
    fan_speed1: float = INPUT(label='Cooling system fan speed 1', units='rpm', type='NUMBER', group='type298', required='*')
    fan_speed2: float = INPUT(label='Cooling system fan speed 2', units='rpm', type='NUMBER', group='type298', required='*')
    fan_speed3: float = INPUT(label='Cooling system fan speed 3', units='rpm', type='NUMBER', group='type298', required='*')
    T_cool_speed2: float = INPUT(label='Cooling Fluid Temp. For Fan Speed 2 Cut-In', units='C', type='NUMBER', group='type298', required='*')
    T_cool_speed3: float = INPUT(label='Cooling Fluid Temp. For Fan Speed 3 Cut-In', units='C', type='NUMBER', group='type298', required='*')
    epsilon_cooler_test: float = INPUT(label='Cooler effectiveness', units='-', type='NUMBER', group='type298', required='*')
    epsilon_radiator_test: float = INPUT(label='Radiator effectiveness', units='-', type='NUMBER', group='type298', required='*')
    cooling_fluid: float = INPUT(label='Reference Condition Cooling Fluid: 1=Water,2=V50%EG,3=V25%EG,4=V40%PG,5=V25%PG', units='-', type='NUMBER', group='type298', required='*', constraints='INTEGER')
    P_controls: float = INPUT(label='Control System Parasitic Power, Avg.', units='W', type='NUMBER', group='type298', required='*')
    test_P_pump: float = INPUT(label='Reference Condition Pump Parasitic Power', units='W', type='NUMBER', group='type298', required='*')
    test_pump_speed: float = INPUT(label='Reference Condition Pump Speed', units='rpm', type='NUMBER', group='type298', required='*')
    test_cooling_fluid: float = INPUT(label='Reference Condition Cooling Fluid', units='-', type='NUMBER', group='type298', required='*', constraints='INTEGER')
    test_T_fluid: float = INPUT(label='Reference Condition Cooling Fluid Temperature', units='K', type='NUMBER', group='type298', required='*')
    test_V_dot_fluid: float = INPUT(label='Reference Condition Cooling Fluid Volumetric Flow Rate', units='gpm', type='NUMBER', group='type298', required='*')
    test_P_fan: float = INPUT(label='Reference Condition Cooling System Fan Power', units='W', type='NUMBER', group='type298', required='*')
    test_fan_speed: float = INPUT(label='Reference Condition Cooling System Fan Speed', units='rpm', type='NUMBER', group='type298', required='*')
    test_fan_rho_air: float = INPUT(label='Reference condition fan air density', units='kg/m^3', type='NUMBER', group='type298', required='*')
    test_fan_cfm: float = INPUT(label='Reference condition van volumentric flow rate', units='cfm', type='NUMBER', group='type298', required='*')
    b_radiator: float = INPUT(label='b_radiator parameter', units='-', type='NUMBER', group='type298', required='*')
    b_cooler: float = INPUT(label='b_cooler parameter', units='-', type='NUMBER', group='type298', required='*')
    Tower_water_outlet_temp: float = INPUT(label='Tower water outlet temperature (set to 20)', units='C', type='NUMBER', group='type298', required='*')
    ns_dish_separation: float = INPUT(label='North-South dish separation used in the simulation', units='m', type='NUMBER', group='type298', required='*')
    ew_dish_separation: float = INPUT(label='East-West dish separation used in the simulation', units='m', type='NUMBER', group='type298', required='*')
    P_tower_fan: float = INPUT(label='Tower fan power (set to 0)', units='kJ/hr', type='NUMBER', group='type298', required='*')
    month: Final[Array] = OUTPUT(label='Resource Month', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    hour: Final[Array] = OUTPUT(label='Resource Hour of Day', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    solazi: Final[Array] = OUTPUT(label='Resource Solar Azimuth', units='deg', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    solzen: Final[Array] = OUTPUT(label='Resource Solar Zenith', units='deg', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    beam: Final[Array] = OUTPUT(label='Resource Beam normal irradiance', units='W/m2', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    tdry: Final[Array] = OUTPUT(label='Resource Dry bulb temperature', units='C', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    twet: Final[Array] = OUTPUT(label='Resource Wet bulb temperature', units='C', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    wspd: Final[Array] = OUTPUT(label='Resource Wind Speed', units='m/s', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    pres: Final[Array] = OUTPUT(label='Resource Pressure', units='mbar', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    Phi_shade: Final[Array] = OUTPUT(label='Collector shading efficiency', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    Collector_Losses: Final[Array] = OUTPUT(label='Collector loss total', units='kWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    eta_collector: Final[Array] = OUTPUT(label='Collector efficiency', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    Power_in_collector: Final[Array] = OUTPUT(label='Collector thermal power incident', units='kWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    Power_out_col: Final[Array] = OUTPUT(label='Collector thermal power produced', units='kWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    Power_in_rec: Final[Array] = OUTPUT(label='Receiver thermal power input', units='kWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_out_rec: Final[Array] = OUTPUT(label='Receiver thermal power output', units='kWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    Q_rec_losses: Final[Array] = OUTPUT(label='Receiver thermal power loss', units='kWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    eta_rec: Final[Array] = OUTPUT(label='Receiver efficiency', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    T_heater_head_operate: Final[Array] = OUTPUT(label='Receiver temperature - head operating', units='K', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    net_power: Final[Array] = OUTPUT(label='Engine power output (net)', units='kWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_out_SE: Final[Array] = OUTPUT(label='Engine power output (gross)', units='kWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_SE_losses: Final[Array] = OUTPUT(label='Engine power loss', units='kWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    eta_SE: Final[Array] = OUTPUT(label='Engine efficiency', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    engine_pressure: Final[Array] = OUTPUT(label='Engine pressure', units='Pa', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    T_compression: Final[Array] = OUTPUT(label='Engine compression temperature', units='K', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    T_tower_out: Final[Array] = OUTPUT(label='Cooling fluid temperature - cooler in/tower out', units='C', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    T_tower_in: Final[Array] = OUTPUT(label='Cooling fluid temperature - cooler out/tower in', units='C', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_parasitic: Final[Array] = OUTPUT(label='Parasitic power', units='We', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    eta_net: Final[Array] = OUTPUT(label='System total: Net efficiency', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    hourly_Power_in_collector: Final[Array] = OUTPUT(label='System total: Collector thermal power incident', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    hourly_Power_out_col: Final[Array] = OUTPUT(label='System total: Collector thermal power produced', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    hourly_Collector_Losses: Final[Array] = OUTPUT(label='System total: Collector loss total', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    hourly_Power_in_rec: Final[Array] = OUTPUT(label='System total: Receiver thermal power input', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    hourly_Q_rec_losses: Final[Array] = OUTPUT(label='System total: Receiver thermal loss', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    hourly_P_out_rec: Final[Array] = OUTPUT(label='System total: Receiver thermal power output', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    hourly_P_out_SE: Final[Array] = OUTPUT(label='System total: Engine power output (gross)', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    hourly_P_parasitic: Final[Array] = OUTPUT(label='System total: Parasitic power', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    annual_energy: Final[float] = OUTPUT(label='Annual Energy', units='kWh', type='NUMBER', group='Outputs', required='*')
    annual_Power_in_collector: Final[float] = OUTPUT(label='Power incident on the collector', units='MWh', type='NUMBER', group='Outputs', required='*')
    annual_Power_out_col: Final[float] = OUTPUT(label='Total power from the collector dish', units='MWh', type='NUMBER', group='Outputs', required='*')
    annual_Power_in_rec: Final[float] = OUTPUT(label='Power entering the receiver from the collector', units='MWh', type='NUMBER', group='Outputs', required='*')
    annual_P_out_rec: Final[float] = OUTPUT(label='Receiver output power', units='MWh', type='NUMBER', group='Outputs', required='*')
    annual_P_out_SE: Final[float] = OUTPUT(label='Stirling engine gross output', units='MWh', type='NUMBER', group='Outputs', required='*')
    annual_Collector_Losses: Final[float] = OUTPUT(label='Total collector losses (Incident - P_out)', units='MWh', type='NUMBER', group='Outputs', required='*')
    annual_P_parasitic: Final[float] = OUTPUT(label='Total parasitic power load', units='MWh', type='NUMBER', group='Outputs', required='*')
    annual_Q_rec_losses: Final[float] = OUTPUT(label='Receiver thermal losses', units='MWh', type='NUMBER', group='Outputs', required='*')
    monthly_energy: Final[Array] = OUTPUT(label='Monthly Energy', units='kWh', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=12')
    monthly_Power_in_collector: Final[Array] = OUTPUT(label='Power incident on the collector', units='MWh', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=12')
    monthly_Power_out_col: Final[Array] = OUTPUT(label='Total power from the collector dish', units='MWh', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=12')
    monthly_Power_in_rec: Final[Array] = OUTPUT(label='Power entering the receiver from the collector', units='MWh', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=12')
    monthly_P_out_rec: Final[Array] = OUTPUT(label='Receiver output power', units='MWh', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=12')
    monthly_P_out_SE: Final[Array] = OUTPUT(label='Stirling engine gross output', units='MWh', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=12')
    monthly_Collector_Losses: Final[Array] = OUTPUT(label='Total collector losses (Incident - P_out)', units='MWh', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=12')
    monthly_P_parasitic: Final[Array] = OUTPUT(label='Total parasitic power load', units='MWh', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=12')
    monthly_Q_rec_losses: Final[Array] = OUTPUT(label='Receiver thermal losses', units='MWh', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=12')
    conversion_factor: Final[float] = OUTPUT(label='Gross to Net Conversion Factor', units='%', type='NUMBER', group='Calculated', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', required='*')
    kwh_per_kw: Final[float] = OUTPUT(label='First year kWh/kW', units='kWh/kW', type='NUMBER', required='*')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    gen: Final[Array] = OUTPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 file_name: str = ...,
                 system_capacity: float = ...,
                 d_ap: float = ...,
                 rho: float = ...,
                 n_ns: float = ...,
                 n_ew: float = ...,
                 ns_dish_sep: float = ...,
                 ew_dish_sep: float = ...,
                 slope_ns: float = ...,
                 slope_ew: float = ...,
                 w_slot_gap: float = ...,
                 h_slot_gap: float = ...,
                 wind_stow_speed: float = ...,
                 A_proj: float = ...,
                 I_cut_in: float = ...,
                 d_ap_test: float = ...,
                 test_if: float = ...,
                 test_L_focal: float = ...,
                 A_total: float = ...,
                 rec_type: float = ...,
                 transmittance_cover: float = ...,
                 alpha_absorber: float = ...,
                 A_absorber: float = ...,
                 alpha_wall: float = ...,
                 A_wall: float = ...,
                 L_insulation: float = ...,
                 k_insulation: float = ...,
                 d_cav: float = ...,
                 P_cav: float = ...,
                 L_cav: float = ...,
                 DELTA_T_DIR: float = ...,
                 DELTA_T_REFLUX: float = ...,
                 T_heater_head_high: float = ...,
                 T_heater_head_low: float = ...,
                 Beale_const_coef: float = ...,
                 Beale_first_coef: float = ...,
                 Beale_square_coef: float = ...,
                 Beale_third_coef: float = ...,
                 Beale_fourth_coef: float = ...,
                 Pressure_coef: float = ...,
                 Pressure_first: float = ...,
                 engine_speed: float = ...,
                 V_displaced: float = ...,
                 T_compression_in: float = ...,
                 cooling_tower_on: float = ...,
                 tower_mode: float = ...,
                 d_pipe_tower: float = ...,
                 tower_m_dot_water: float = ...,
                 tower_m_dot_water_test: float = ...,
                 tower_pipe_material: float = ...,
                 eta_tower_pump: float = ...,
                 fan_control_signal: float = ...,
                 epsilon_power_test: float = ...,
                 system_availability: float = ...,
                 pump_speed: float = ...,
                 fan_speed1: float = ...,
                 fan_speed2: float = ...,
                 fan_speed3: float = ...,
                 T_cool_speed2: float = ...,
                 T_cool_speed3: float = ...,
                 epsilon_cooler_test: float = ...,
                 epsilon_radiator_test: float = ...,
                 cooling_fluid: float = ...,
                 P_controls: float = ...,
                 test_P_pump: float = ...,
                 test_pump_speed: float = ...,
                 test_cooling_fluid: float = ...,
                 test_T_fluid: float = ...,
                 test_V_dot_fluid: float = ...,
                 test_P_fan: float = ...,
                 test_fan_speed: float = ...,
                 test_fan_rho_air: float = ...,
                 test_fan_cfm: float = ...,
                 b_radiator: float = ...,
                 b_cooler: float = ...,
                 Tower_water_outlet_temp: float = ...,
                 ns_dish_separation: float = ...,
                 ew_dish_separation: float = ...,
                 P_tower_fan: float = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
