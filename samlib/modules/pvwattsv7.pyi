
# This is a generated file

"""pvwattsv7 - PVWatts V7 - integrated hourly weather reader and PV system simulator."""

# VERSION: 3

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'solar_resource_file': str,
        'solar_resource_data': Table,
        'albedo': Array,
        'system_use_lifetime_output': float,
        'analysis_period': float,
        'dc_degradation': Array,
        'system_capacity': float,
        'module_type': float,
        'dc_ac_ratio': float,
        'bifaciality': float,
        'ac_plant_max_f': float,
        'array_type': float,
        'tilt': float,
        'azimuth': float,
        'gcr': float,
        'rotlim': float,
        'soiling': Array,
        'losses': float,
        'enable_wind_stow': float,
        'stow_wspd': float,
        'gust_factor': float,
        'wind_stow_angle': float,
        'en_snowloss': float,
        'inv_eff': float,
        'xfmr_nll': float,
        'xfmr_ll': float,
        'shading:timestep': Matrix,
        'shading:mxh': Matrix,
        'shading:azal': Matrix,
        'shading:diff': float,
        'batt_simple_enable': float,
        'gh': Array,
        'dn': Array,
        'df': Array,
        'tamb': Array,
        'wspd': Array,
        'snow': Array,
        'sunup': Array,
        'shad_beam_factor': Array,
        'aoi': Array,
        'poa': Array,
        'tpoa': Array,
        'tcell': Array,
        'dcsnowderate': Array,
        'dc': Array,
        'ac': Array,
        'poa_monthly': Array,
        'solrad_monthly': Array,
        'dc_monthly': Array,
        'ac_monthly': Array,
        'monthly_energy': Array,
        'solrad_annual': float,
        'ac_annual': float,
        'annual_energy': float,
        'capacity_factor': float,
        'kwh_per_kw': float,
        'location': str,
        'city': str,
        'state': str,
        'lat': float,
        'lon': float,
        'tz': float,
        'elev': float,
        'inverter_efficiency': float,
        'estimated_rows': float,
        'ts_shift_hours': float,
        'percent_complete': float,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix,
        'gen': Array
}, total=False)

class Data(ssc.DataDict):
    solar_resource_file: str = INPUT(label='Weather file path', type='STRING', group='Solar Resource', required='?')
    solar_resource_data: Table = INPUT(label='Weather data', type='TABLE', group='Solar Resource', required='?', meta='dn,df,tdry,wspd,lat,lon,tz,elev')
    albedo: Array = INPUT(label='Albedo', units='frac', type='ARRAY', group='Solar Resource', meta='if provided, will overwrite weather file albedo')
    system_use_lifetime_output: float = INOUT(label='Run lifetime simulation', units='0/1', type='NUMBER', group='Lifetime', required='?=0')
    analysis_period: float = INPUT(label='Analysis period', units='years', type='NUMBER', group='Lifetime', required='system_use_lifetime_output=1')
    dc_degradation: Array = INPUT(label='Annual DC degradation for lifetime simulations', units='%/year', type='ARRAY', group='Lifetime', required='system_use_lifetime_output=1')
    system_capacity: float = INPUT(label='System size (DC nameplate)', units='kW', type='NUMBER', group='System Design', required='*')
    module_type: float = INPUT(label='Module type', units='0/1/2', type='NUMBER', group='System Design', required='?=0', constraints='MIN=0,MAX=2,INTEGER', meta='Standard,Premium,Thin film')
    dc_ac_ratio: float = INPUT(label='DC to AC ratio', units='ratio', type='NUMBER', group='System Design', required='?=1.1', constraints='POSITIVE')
    bifaciality: float = INPUT(label='Module bifaciality factor', units='0 or ~0.65', type='NUMBER', group='System Design', required='?=0')
    ac_plant_max_f: float = INPUT(label='Plant controller max output (as f(ac_size))', units='ratio', type='NUMBER', group='System Design', required='?=1.0')
    array_type: float = INPUT(label='Array type', units='0/1/2/3/4', type='NUMBER', group='System Design', required='*', constraints='MIN=0,MAX=4,INTEGER', meta='Fixed Rack,Fixed Roof,1Axis,Backtracked,2Axis')
    tilt: float = INPUT(label='Tilt angle', units='deg', type='NUMBER', group='System Design', required='array_type<4', constraints='MIN=0,MAX=90', meta='H=0,V=90')
    azimuth: float = INPUT(label='Azimuth angle', units='deg', type='NUMBER', group='System Design', required='array_type<4', constraints='MIN=0,MAX=360', meta='E=90,S=180,W=270')
    gcr: float = INPUT(label='Ground coverage ratio', units='0..1', type='NUMBER', group='System Design', required='?=0.4', constraints='MIN=0.01,MAX=0.99')
    rotlim: float = INPUT(label='Tracker rotation angle limit', units='deg', type='NUMBER', group='System Design', required='?=45.0')
    soiling: Array = INPUT(label='Soiling loss', units='%', type='ARRAY', group='System Design', required='?')
    losses: float = INPUT(label='Other DC losses', units='%', type='NUMBER', group='System Design', required='*', constraints='MIN=-5,MAX=99', meta='Total system losses')
    enable_wind_stow: float = INPUT(label='Enable tracker stow at high wind speeds', units='0/1', type='NUMBER', group='System Design', required='?=0')
    stow_wspd: float = INPUT(label='Tracker stow wind speed threshold', units='m/s', type='NUMBER', group='System Design', required='?=10')
    gust_factor: float = INPUT(label='Wind gust estimation factor', type='NUMBER', group='System Design', required='?')
    wind_stow_angle: float = INPUT(label='Tracker angle for wind stow', units='deg', type='NUMBER', group='System Design', required='?=30.0')
    en_snowloss: float = INPUT(label='Enable snow loss model', units='0/1', type='NUMBER', group='System Design', required='?=0', constraints='BOOLEAN')
    inv_eff: float = INPUT(label='Inverter efficiency at rated power', units='%', type='NUMBER', group='System Design', required='?=96', constraints='MIN=90,MAX=99.5')
    xfmr_nll: float = INPUT(label='GSU transformer no load loss (iron core)', units='%(ac)', type='NUMBER', group='System Design', required='?=0.0')
    xfmr_ll: float = INPUT(label='GSU transformer load loss (resistive)', units='%(ac)', type='NUMBER', group='System Design', required='?=0.0')
    shading_timestep: Matrix = INPUT(name='shading:timestep', label='Time step beam shading loss', units='%', type='MATRIX', group='System Design', required='?')
    shading_mxh: Matrix = INPUT(name='shading:mxh', label='Month x Hour beam shading loss', units='%', type='MATRIX', group='System Design', required='?')
    shading_azal: Matrix = INPUT(name='shading:azal', label='Azimuth x altitude beam shading loss', units='%', type='MATRIX', group='System Design', required='?')
    shading_diff: float = INPUT(name='shading:diff', label='Diffuse shading loss', units='%', type='NUMBER', group='System Design', required='?')
    batt_simple_enable: float = INPUT(label='Enable Battery', units='0/1', type='NUMBER', group='System Design', required='?=0', constraints='BOOLEAN')
    gh: Final[Array] = OUTPUT(label='Weather file global horizontal irradiance', units='W/m2', type='ARRAY', group='Time Series', required='*')
    dn: Final[Array] = OUTPUT(label='Weather file beam irradiance', units='W/m2', type='ARRAY', group='Time Series', required='*')
    df: Final[Array] = OUTPUT(label='Weather file diffuse irradiance', units='W/m2', type='ARRAY', group='Time Series', required='*')
    tamb: Final[Array] = OUTPUT(label='Weather file ambient temperature', units='C', type='ARRAY', group='Time Series', required='*')
    wspd: Final[Array] = OUTPUT(label='Weather file wind speed', units='m/s', type='ARRAY', group='Time Series', required='*')
    snow: Final[Array] = OUTPUT(label='Weather file snow depth', units='cm', type='ARRAY', group='Time Series')
    sunup: Final[Array] = OUTPUT(label='Sun up over horizon', units='0/1', type='ARRAY', group='Time Series', required='*')
    shad_beam_factor: Final[Array] = OUTPUT(label='Shading factor for beam radiation', type='ARRAY', group='Time Series', required='*')
    aoi: Final[Array] = OUTPUT(label='Angle of incidence', units='deg', type='ARRAY', group='Time Series', required='*')
    poa: Final[Array] = OUTPUT(label='Plane of array irradiance', units='W/m2', type='ARRAY', group='Time Series', required='*')
    tpoa: Final[Array] = OUTPUT(label='Transmitted plane of array irradiance', units='W/m2', type='ARRAY', group='Time Series', required='*')
    tcell: Final[Array] = OUTPUT(label='Module temperature', units='C', type='ARRAY', group='Time Series', required='*')
    dcsnowderate: Final[Array] = OUTPUT(label='Array DC power loss due to snow', units='%', type='ARRAY', group='Time Series', required='*')
    dc: Final[Array] = OUTPUT(label='DC array power', units='W', type='ARRAY', group='Time Series', required='*')
    ac: Final[Array] = OUTPUT(label='AC inverter power', units='W', type='ARRAY', group='Time Series', required='*')
    poa_monthly: Final[Array] = OUTPUT(label='Plane of array irradiance', units='kWh/m2', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    solrad_monthly: Final[Array] = OUTPUT(label='Daily average solar irradiance', units='kWh/m2/day', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    dc_monthly: Final[Array] = OUTPUT(label='DC array output', units='kWh', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    ac_monthly: Final[Array] = OUTPUT(label='AC system output', units='kWh', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    monthly_energy: Final[Array] = OUTPUT(label='Monthly energy', units='kWh', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    solrad_annual: Final[float] = OUTPUT(label='Daily average solar irradiance', units='kWh/m2/day', type='NUMBER', group='Annual', required='*')
    ac_annual: Final[float] = OUTPUT(label='Annual AC system output', units='kWh', type='NUMBER', group='Annual', required='*')
    annual_energy: Final[float] = OUTPUT(label='Annual energy', units='kWh', type='NUMBER', group='Annual', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', group='Annual', required='*')
    kwh_per_kw: Final[float] = OUTPUT(label='Energy yield', units='kWh/kW', type='NUMBER', group='Annual', required='*')
    location: Final[str] = OUTPUT(label='Location ID', type='STRING', group='Location', required='*')
    city: Final[str] = OUTPUT(label='City', type='STRING', group='Location', required='*')
    state: Final[str] = OUTPUT(label='State', type='STRING', group='Location', required='*')
    lat: Final[float] = OUTPUT(label='Latitude', units='deg', type='NUMBER', group='Location', required='*')
    lon: Final[float] = OUTPUT(label='Longitude', units='deg', type='NUMBER', group='Location', required='*')
    tz: Final[float] = OUTPUT(label='Time zone', units='hr', type='NUMBER', group='Location', required='*')
    elev: Final[float] = OUTPUT(label='Site elevation', units='m', type='NUMBER', group='Location', required='*')
    inverter_efficiency: Final[float] = OUTPUT(label='Inverter efficiency at rated power', units='%', type='NUMBER', group='PVWatts')
    estimated_rows: Final[float] = OUTPUT(label='Estimated number of rows in the system', type='NUMBER', group='PVWatts')
    ts_shift_hours: Final[float] = OUTPUT(label='Time offset for interpreting time series outputs', units='hours', type='NUMBER', group='Miscellaneous', required='*')
    percent_complete: Final[float] = OUTPUT(label='Estimated percent of total completed simulation', units='%', type='NUMBER', group='Miscellaneous')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Adjustment Factors', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly Adjustment Factors', units='%', type='ARRAY', group='Adjustment Factors', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based Adjustment Factors', units='%', type='MATRIX', group='Adjustment Factors', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    gen: Final[Array] = OUTPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 solar_resource_file: str = ...,
                 solar_resource_data: Table = ...,
                 albedo: Array = ...,
                 system_use_lifetime_output: float = ...,
                 analysis_period: float = ...,
                 dc_degradation: Array = ...,
                 system_capacity: float = ...,
                 module_type: float = ...,
                 dc_ac_ratio: float = ...,
                 bifaciality: float = ...,
                 ac_plant_max_f: float = ...,
                 array_type: float = ...,
                 tilt: float = ...,
                 azimuth: float = ...,
                 gcr: float = ...,
                 rotlim: float = ...,
                 soiling: Array = ...,
                 losses: float = ...,
                 enable_wind_stow: float = ...,
                 stow_wspd: float = ...,
                 gust_factor: float = ...,
                 wind_stow_angle: float = ...,
                 en_snowloss: float = ...,
                 inv_eff: float = ...,
                 xfmr_nll: float = ...,
                 xfmr_ll: float = ...,
                 shading_timestep: Matrix = ...,
                 shading_mxh: Matrix = ...,
                 shading_azal: Matrix = ...,
                 shading_diff: float = ...,
                 batt_simple_enable: float = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
