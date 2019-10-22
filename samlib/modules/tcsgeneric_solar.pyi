
# This is a generated file

"""tcsgeneric_solar - Generic CSP model using the generic solar TCS types."""

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
        'latitude': float,
        'longitude': float,
        'timezone': float,
        'theta_stow': float,
        'theta_dep': float,
        'interp_arr': float,
        'rad_type': float,
        'solarm': float,
        'T_sfdes': float,
        'irr_des': float,
        'eta_opt_soil': float,
        'eta_opt_gen': float,
        'f_sfhl_ref': float,
        'sfhlQ_coefs': Array,
        'sfhlT_coefs': Array,
        'sfhlV_coefs': Array,
        'qsf_des': float,
        'w_des': float,
        'eta_des': float,
        'f_wmax': float,
        'f_wmin': float,
        'f_startup': float,
        'eta_lhv': float,
        'etaQ_coefs': Array,
        'etaT_coefs': Array,
        'T_pcdes': float,
        'PC_T_corr': float,
        'f_Wpar_fixed': float,
        'f_Wpar_prod': float,
        'Wpar_prodQ_coefs': Array,
        'Wpar_prodT_coefs': Array,
        'Wpar_prodD_coefs': Array,
        'hrs_tes': float,
        'f_charge': float,
        'f_disch': float,
        'f_etes_0': float,
        'f_teshl_ref': float,
        'teshlX_coefs': Array,
        'teshlT_coefs': Array,
        'ntod': float,
        'disws': Array,
        'diswos': Array,
        'qdisp': Array,
        'fdisp': Array,
        'istableunsorted': float,
        'OpticalTable': Matrix,
        'exergy_table': Matrix,
        'storage_config': float,
        'ibn': float,
        'ibh': float,
        'itoth': float,
        'tdb': float,
        'twb': float,
        'vwind': float,
        'month': Array,
        'hour': Array,
        'solazi': Array,
        'solzen': Array,
        'beam': Array,
        'global': Array,
        'diff': Array,
        'tdry': Array,
        'twet': Array,
        'wspd': Array,
        'pres': Array,
        'eta_opt_sf': Array,
        'q_inc': Array,
        'f_sfhl_qdni': Array,
        'f_sfhl_tamb': Array,
        'f_sfhl_vwind': Array,
        'q_hl_sf': Array,
        'q_sf': Array,
        'q_to_tes': Array,
        'q_from_tes': Array,
        'e_in_tes': Array,
        'q_hl_tes': Array,
        'eta_cycle': Array,
        'f_effpc_qtpb': Array,
        'f_effpc_tamb': Array,
        'enet': Array,
        'w_gr': Array,
        'w_gr_solar': Array,
        'w_gr_fossil': Array,
        'q_to_pb': Array,
        'q_startup': Array,
        'q_dump_tesfull': Array,
        'q_dump_umin': Array,
        'q_dump_teschg': Array,
        'q_dump_tot': Array,
        'q_fossil': Array,
        'q_gas': Array,
        'w_par_fixed': Array,
        'w_par_prod': Array,
        'w_par_tot': Array,
        'w_par_online': Array,
        'w_par_offline': Array,
        'monthly_energy': Array,
        'monthly_w_gr': Array,
        'monthly_q_sf': Array,
        'monthly_q_to_pb': Array,
        'monthly_q_to_tes': Array,
        'monthly_q_from_tes': Array,
        'monthly_q_hl_sf': Array,
        'monthly_q_hl_tes': Array,
        'monthly_q_dump_tot': Array,
        'monthly_q_startup': Array,
        'monthly_q_fossil': Array,
        'annual_energy': float,
        'annual_w_gr': float,
        'annual_q_sf': float,
        'annual_q_to_pb': float,
        'annual_q_to_tes': float,
        'annual_q_from_tes': float,
        'annual_q_hl_sf': float,
        'annual_q_hl_tes': float,
        'annual_q_dump_tot': float,
        'annual_q_startup': float,
        'annual_q_fossil': float,
        'conversion_factor': float,
        'capacity_factor': float,
        'kwh_per_kw': float,
        'system_heat_rate': float,
        'annual_fuel_usage': float,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix,
        'sf_adjust:constant': float,
        'sf_adjust:hourly': Array,
        'sf_adjust:periods': Matrix,
        'gen': Array
}, total=False)

class Data(ssc.DataDict):
    file_name: str = INPUT(label='local weather file path', type='STRING', group='Weather', required='*', constraints='LOCAL_FILE')
    track_mode: float = INPUT(label='Tracking mode', type='NUMBER', group='Weather', required='*')
    tilt: float = INPUT(label='Tilt angle of surface/axis', type='NUMBER', group='Weather', required='*')
    azimuth: float = INPUT(label='Azimuth angle of surface/axis', type='NUMBER', group='Weather', required='*')
    system_capacity: float = INPUT(label='Nameplate capacity', units='kW', type='NUMBER', group='generic solar', required='*')
    weekday_schedule: Matrix = INPUT(label='12x24 Time of Use Values for week days', type='MATRIX', group='tou_translator', required='*')
    weekend_schedule: Matrix = INPUT(label='12x24 Time of Use Values for week end days', type='MATRIX', group='tou_translator', required='*')
    latitude: float = INPUT(label='Site latitude', type='NUMBER', group='type_260', required='*')
    longitude: float = INPUT(label='Site longitude', type='NUMBER', group='type_260', required='*')
    timezone: float = INPUT(label='Site timezone', units='hr', type='NUMBER', group='type_260', required='*')
    theta_stow: float = INPUT(label='Solar elevation angle at which the solar field stops operating', units='deg', type='NUMBER', group='type_260', required='*')
    theta_dep: float = INPUT(label='Solar elevation angle at which the solar field begins operating', units='deg', type='NUMBER', group='type_260', required='*')
    interp_arr: float = INPUT(label='Interpolate the array or find nearest neighbor? (1=interp,2=no)', units='none', type='NUMBER', group='type_260', required='*', constraints='INTEGER')
    rad_type: float = INPUT(label='Solar resource radiation type (1=DNI,2=horiz.beam,3=tot.horiz)', units='none', type='NUMBER', group='type_260', required='*', constraints='INTEGER')
    solarm: float = INPUT(label='Solar multiple', units='none', type='NUMBER', group='type_260', required='*')
    T_sfdes: float = INPUT(label='Solar field design point temperature (dry bulb)', units='C', type='NUMBER', group='type_260', required='*')
    irr_des: float = INPUT(label='Irradiation design point', units='W/m2', type='NUMBER', group='type_260', required='*')
    eta_opt_soil: float = INPUT(label='Soiling optical derate factor', units='none', type='NUMBER', group='type_260', required='*')
    eta_opt_gen: float = INPUT(label='General/other optical derate', units='none', type='NUMBER', group='type_260', required='*')
    f_sfhl_ref: float = INPUT(label='Reference solar field thermal loss fraction', units='MW/MWcap', type='NUMBER', group='type_260', required='*')
    sfhlQ_coefs: Array = INPUT(label='Irr-based solar field thermal loss adjustment coefficients', units='1/MWt', type='ARRAY', group='type_260', required='*')
    sfhlT_coefs: Array = INPUT(label='Temp.-based solar field thermal loss adjustment coefficients', units='1/C', type='ARRAY', group='type_260', required='*')
    sfhlV_coefs: Array = INPUT(label='Wind-based solar field thermal loss adjustment coefficients', units='1/(m/s)', type='ARRAY', group='type_260', required='*')
    qsf_des: float = INPUT(label='Solar field thermal production at design', units='MWt', type='NUMBER', group='type_260', required='*')
    w_des: float = INPUT(label='Design power cycle gross output', units='MWe', type='NUMBER', group='type_260', required='*')
    eta_des: float = INPUT(label='Design power cycle gross efficiency', units='none', type='NUMBER', group='type_260', required='*')
    f_wmax: float = INPUT(label='Maximum over-design power cycle operation fraction', units='none', type='NUMBER', group='type_260', required='*')
    f_wmin: float = INPUT(label='Minimum part-load power cycle operation fraction', units='none', type='NUMBER', group='type_260', required='*')
    f_startup: float = INPUT(label='Equivalent full-load hours required for power system startup', units='hours', type='NUMBER', group='type_260', required='*')
    eta_lhv: float = INPUT(label='Fossil backup lower heating value efficiency', units='none', type='NUMBER', group='type_260', required='*')
    etaQ_coefs: Array = INPUT(label='Part-load power conversion efficiency adjustment coefficients', units='1/MWt', type='ARRAY', group='type_260', required='*')
    etaT_coefs: Array = INPUT(label='Temp.-based power conversion efficiency adjustment coefs.', units='1/C', type='ARRAY', group='type_260', required='*')
    T_pcdes: float = INPUT(label='Power conversion reference temperature', units='C', type='NUMBER', group='type_260', required='*')
    PC_T_corr: float = INPUT(label='Power conversion temperature correction mode (1=wetb, 2=dryb)', units='none', type='NUMBER', group='type_260', required='*', constraints='INTEGER')
    f_Wpar_fixed: float = INPUT(label='Fixed capacity-based parasitic loss fraction', units='MWe/MWcap', type='NUMBER', group='type_260', required='*')
    f_Wpar_prod: float = INPUT(label='Production-based parasitic loss fraction', units='MWe/MWe', type='NUMBER', group='type_260', required='*')
    Wpar_prodQ_coefs: Array = INPUT(label='Part-load production parasitic adjustment coefs.', units='1/MWe', type='ARRAY', group='type_260', required='*')
    Wpar_prodT_coefs: Array = INPUT(label='Temp.-based production parasitic adjustment coefs.', units='1/C', type='ARRAY', group='type_260', required='*')
    Wpar_prodD_coefs: Array = INPUT(label='DNI-based production parasitic adjustment coefs.', units='m2/W', type='ARRAY', group='type_260', required='*')
    hrs_tes: float = INPUT(label='Equivalent full-load hours of storage', units='hours', type='NUMBER', group='type_260', required='*')
    f_charge: float = INPUT(label='Storage charging energy derate', units='none', type='NUMBER', group='type_260', required='*')
    f_disch: float = INPUT(label='Storage discharging energy derate', units='none', type='NUMBER', group='type_260', required='*')
    f_etes_0: float = INPUT(label='Initial fractional charge level of thermal storage (0..1)', units='none', type='NUMBER', group='type_260', required='*')
    f_teshl_ref: float = INPUT(label='Reference heat loss from storage per max stored capacity', units='kWt/MWhr-stored', type='NUMBER', group='type_260', required='*')
    teshlX_coefs: Array = INPUT(label='Charge-based thermal loss adjustment - constant coef.', units='1/MWhr-stored', type='ARRAY', group='type_260', required='*')
    teshlT_coefs: Array = INPUT(label='Temp.-based thermal loss adjustment - constant coef.', units='1/C', type='ARRAY', group='type_260', required='*')
    ntod: float = INPUT(label='Number of time-of-dispatch periods in the dispatch schedule', units='none', type='NUMBER', group='type_260', required='*')
    disws: Array = INPUT(label='Time-of-dispatch control for with-solar conditions', units='none', type='ARRAY', group='type_260', required='*')
    diswos: Array = INPUT(label='Time-of-dispatch control for without-solar conditions', units='none', type='ARRAY', group='type_260', required='*')
    qdisp: Array = INPUT(label='TOD power output control factors', units='none', type='ARRAY', group='type_260', required='*')
    fdisp: Array = INPUT(label='Fossil backup output control factors', units='none', type='ARRAY', group='type_260', required='*')
    istableunsorted: float = INPUT(label='Is optical table unsorted format?none', type='NUMBER', group='*', meta='type_260')
    OpticalTable: Matrix = INPUT(label='Optical table', units='none', type='MATRIX', group='type_260', required='*')
    exergy_table: Matrix = INPUT(label='Exergy table', units='none', type='MATRIX', group='type_260', required='*')
    storage_config: float = INPUT(label='Thermal storage configuration', units='none', type='NUMBER', group='type_260', required='*')
    ibn: float = INPUT(label='Beam-normal (DNI) irradiation', units='kJ/hr-m^2', type='NUMBER', group='type_260', required='*')
    ibh: float = INPUT(label='Beam-horizontal irradiation', units='kJ/hr-m^2', type='NUMBER', group='type_260', required='*')
    itoth: float = INPUT(label='Total horizontal irradiation', units='kJ/hr-m^2', type='NUMBER', group='type_260', required='*')
    tdb: float = INPUT(label='Ambient dry-bulb temperature', units='C', type='NUMBER', group='type_260', required='*')
    twb: float = INPUT(label='Ambient wet-bulb temperature', units='C', type='NUMBER', group='type_260', required='*')
    vwind: float = INPUT(label='Wind velocity', units='m/s', type='NUMBER', group='type_260', required='*')
    month: Final[Array] = OUTPUT(label='Resource Month', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    hour: Final[Array] = OUTPUT(label='Resource Hour of Day', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    solazi: Final[Array] = OUTPUT(label='Resource Solar Azimuth', units='deg', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    solzen: Final[Array] = OUTPUT(label='Resource Solar Zenith', units='deg', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    beam: Final[Array] = OUTPUT(label='Resource Beam normal irradiance', units='W/m2', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    global_: Final[Array] = OUTPUT(name='global', label='Resource Global horizontal irradiance', units='W/m2', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    diff: Final[Array] = OUTPUT(label='Resource Diffuse horizontal irradiance', units='W/m2', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    tdry: Final[Array] = OUTPUT(label='Resource Dry bulb temperature', units='C', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    twet: Final[Array] = OUTPUT(label='Resource Wet bulb temperature', units='C', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    wspd: Final[Array] = OUTPUT(label='Resource Wind Speed', units='m/s', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    pres: Final[Array] = OUTPUT(label='Resource Pressure', units='mbar', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    eta_opt_sf: Final[Array] = OUTPUT(label='Field collector optical efficiency', units='none', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_inc: Final[Array] = OUTPUT(label='Field thermal power incident', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    f_sfhl_qdni: Final[Array] = OUTPUT(label='Field thermal power load-based loss correction', units='none', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    f_sfhl_tamb: Final[Array] = OUTPUT(label='Field thermal power temp.-based loss correction', units='none', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    f_sfhl_vwind: Final[Array] = OUTPUT(label='Field thermal power wind-based loss correction', units='none', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_hl_sf: Final[Array] = OUTPUT(label='Field thermal power loss total', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_sf: Final[Array] = OUTPUT(label='Field thermal power total produced', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_to_tes: Final[Array] = OUTPUT(label='TES thermal energy into storage', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_from_tes: Final[Array] = OUTPUT(label='TES thermal energy from storage', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    e_in_tes: Final[Array] = OUTPUT(label='TES thermal energy available', units='MWht', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_hl_tes: Final[Array] = OUTPUT(label='TES thermal losses from tank(s)', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    eta_cycle: Final[Array] = OUTPUT(label='Cycle efficiency (gross)', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    f_effpc_qtpb: Final[Array] = OUTPUT(label='Cycle efficiency load-based correction', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    f_effpc_tamb: Final[Array] = OUTPUT(label='Cycle efficiency temperature-based correction', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    enet: Final[Array] = OUTPUT(label='Cycle electrical power output (net)', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    w_gr: Final[Array] = OUTPUT(label='Cycle electrical power output (gross)', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    w_gr_solar: Final[Array] = OUTPUT(label='Cycle electrical power output (gross, solar share)', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    w_gr_fossil: Final[Array] = OUTPUT(label='Cycle electrical power output (gross, fossil share)', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_to_pb: Final[Array] = OUTPUT(label='Cycle thermal power input', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_startup: Final[Array] = OUTPUT(label='Cycle thermal startup energy', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_dump_tesfull: Final[Array] = OUTPUT(label='Cycle thermal energy dumped - TES is full', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_dump_umin: Final[Array] = OUTPUT(label='Cycle thermal energy dumped - min. load requirement', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_dump_teschg: Final[Array] = OUTPUT(label='Cycle thermal energy dumped - solar field', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_dump_tot: Final[Array] = OUTPUT(label='Cycle thermal energy dumped total', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_fossil: Final[Array] = OUTPUT(label='Fossil thermal power produced', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_gas: Final[Array] = OUTPUT(label='Fossil fuel used', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    w_par_fixed: Final[Array] = OUTPUT(label='Fixed parasitic losses', units='MWh', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    w_par_prod: Final[Array] = OUTPUT(label='Production-based parasitic losses', units='MWh', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    w_par_tot: Final[Array] = OUTPUT(label='Total parasitic losses', units='MWh', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    w_par_online: Final[Array] = OUTPUT(label='Online parasitics', units='MWh', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    w_par_offline: Final[Array] = OUTPUT(label='Offline parasitics', units='MWh', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    monthly_energy: Final[Array] = OUTPUT(label='Monthly Energy', units='kWh', type='ARRAY', group='Generic CSP', required='*', constraints='LENGTH=12')
    monthly_w_gr: Final[Array] = OUTPUT(label='Total gross power production', units='kWh', type='ARRAY', group='Generic CSP', required='*', constraints='LENGTH=12')
    monthly_q_sf: Final[Array] = OUTPUT(label='Solar field delivered thermal power', units='MWt', type='ARRAY', group='Generic CSP', required='*', constraints='LENGTH=12')
    monthly_q_to_pb: Final[Array] = OUTPUT(label='Thermal energy to the power conversion system', units='MWt', type='ARRAY', group='Generic CSP', required='*', constraints='LENGTH=12')
    monthly_q_to_tes: Final[Array] = OUTPUT(label='Thermal energy into storage', units='MWt', type='ARRAY', group='Generic CSP', required='*', constraints='LENGTH=12')
    monthly_q_from_tes: Final[Array] = OUTPUT(label='Thermal energy from storage', units='MWt', type='ARRAY', group='Generic CSP', required='*', constraints='LENGTH=12')
    monthly_q_hl_sf: Final[Array] = OUTPUT(label='Solar field thermal losses', units='MWt', type='ARRAY', group='Generic CSP', required='*', constraints='LENGTH=12')
    monthly_q_hl_tes: Final[Array] = OUTPUT(label='Thermal losses from storage', units='MWt', type='ARRAY', group='Generic CSP', required='*', constraints='LENGTH=12')
    monthly_q_dump_tot: Final[Array] = OUTPUT(label='Total dumped energy', units='MWt', type='ARRAY', group='Generic CSP', required='*', constraints='LENGTH=12')
    monthly_q_startup: Final[Array] = OUTPUT(label='Power conversion startup energy', units='MWt', type='ARRAY', group='Generic CSP', required='*', constraints='LENGTH=12')
    monthly_q_fossil: Final[Array] = OUTPUT(label='Thermal energy supplied from aux firing', units='MWt', type='ARRAY', group='Generic CSP', required='*', constraints='LENGTH=12')
    annual_energy: Final[float] = OUTPUT(label='Annual Energy', units='kWh', type='NUMBER', group='Generic CSP', required='*')
    annual_w_gr: Final[float] = OUTPUT(label='Total gross power production', units='kWh', type='NUMBER', group='Generic CSP', required='*')
    annual_q_sf: Final[float] = OUTPUT(label='Solar field delivered thermal power', units='MWht', type='NUMBER', group='Generic CSP', required='*')
    annual_q_to_pb: Final[float] = OUTPUT(label='Thermal energy to the power conversion system', units='MWht', type='NUMBER', group='Generic CSP', required='*')
    annual_q_to_tes: Final[float] = OUTPUT(label='Thermal energy into storage', units='MWht', type='NUMBER', group='Generic CSP', required='*')
    annual_q_from_tes: Final[float] = OUTPUT(label='Thermal energy from storage', units='MWht', type='NUMBER', group='Generic CSP', required='*')
    annual_q_hl_sf: Final[float] = OUTPUT(label='Solar field thermal losses', units='MWht', type='NUMBER', group='Generic CSP', required='*')
    annual_q_hl_tes: Final[float] = OUTPUT(label='Thermal losses from storage', units='MWht', type='NUMBER', group='Generic CSP', required='*')
    annual_q_dump_tot: Final[float] = OUTPUT(label='Total dumped energy', units='MWht', type='NUMBER', group='Generic CSP', required='*')
    annual_q_startup: Final[float] = OUTPUT(label='Power conversion startup energy', units='MWht', type='NUMBER', group='Generic CSP', required='*')
    annual_q_fossil: Final[float] = OUTPUT(label='Thermal energy supplied from aux firing', units='MWht', type='NUMBER', group='Generic CSP', required='*')
    conversion_factor: Final[float] = OUTPUT(label='Gross to Net Conversion Factor', units='%', type='NUMBER', group='Calculated', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', required='*')
    kwh_per_kw: Final[float] = OUTPUT(label='First year kWh/kW', units='kWh/kW', type='NUMBER', required='*')
    system_heat_rate: Final[float] = OUTPUT(label='System heat rate', units='MMBtu/MWh', type='NUMBER', required='*')
    annual_fuel_usage: Final[float] = OUTPUT(label='Annual fuel usage', units='kWh', type='NUMBER', required='*')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    sf_adjust_constant: float = INPUT(name='sf_adjust:constant', label='SF Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    sf_adjust_hourly: Array = INPUT(name='sf_adjust:hourly', label='SF Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    sf_adjust_periods: Matrix = INPUT(name='sf_adjust:periods', label='SF Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    gen: Final[Array] = OUTPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 file_name: str = ...,
                 track_mode: float = ...,
                 tilt: float = ...,
                 azimuth: float = ...,
                 system_capacity: float = ...,
                 weekday_schedule: Matrix = ...,
                 weekend_schedule: Matrix = ...,
                 latitude: float = ...,
                 longitude: float = ...,
                 timezone: float = ...,
                 theta_stow: float = ...,
                 theta_dep: float = ...,
                 interp_arr: float = ...,
                 rad_type: float = ...,
                 solarm: float = ...,
                 T_sfdes: float = ...,
                 irr_des: float = ...,
                 eta_opt_soil: float = ...,
                 eta_opt_gen: float = ...,
                 f_sfhl_ref: float = ...,
                 sfhlQ_coefs: Array = ...,
                 sfhlT_coefs: Array = ...,
                 sfhlV_coefs: Array = ...,
                 qsf_des: float = ...,
                 w_des: float = ...,
                 eta_des: float = ...,
                 f_wmax: float = ...,
                 f_wmin: float = ...,
                 f_startup: float = ...,
                 eta_lhv: float = ...,
                 etaQ_coefs: Array = ...,
                 etaT_coefs: Array = ...,
                 T_pcdes: float = ...,
                 PC_T_corr: float = ...,
                 f_Wpar_fixed: float = ...,
                 f_Wpar_prod: float = ...,
                 Wpar_prodQ_coefs: Array = ...,
                 Wpar_prodT_coefs: Array = ...,
                 Wpar_prodD_coefs: Array = ...,
                 hrs_tes: float = ...,
                 f_charge: float = ...,
                 f_disch: float = ...,
                 f_etes_0: float = ...,
                 f_teshl_ref: float = ...,
                 teshlX_coefs: Array = ...,
                 teshlT_coefs: Array = ...,
                 ntod: float = ...,
                 disws: Array = ...,
                 diswos: Array = ...,
                 qdisp: Array = ...,
                 fdisp: Array = ...,
                 istableunsorted: float = ...,
                 OpticalTable: Matrix = ...,
                 exergy_table: Matrix = ...,
                 storage_config: float = ...,
                 ibn: float = ...,
                 ibh: float = ...,
                 itoth: float = ...,
                 tdb: float = ...,
                 twb: float = ...,
                 vwind: float = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...,
                 sf_adjust_constant: float = ...,
                 sf_adjust_hourly: Array = ...,
                 sf_adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
