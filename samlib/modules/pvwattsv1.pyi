
# This is a generated file

"""pvwattsv1 - PVWatts V.1 - integrated hourly weather reader and PV system simulator."""

# VERSION: 2

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
        'solar_resource_file': str,
        'albedo': float,
        'system_size': float,
        'derate': float,
        'track_mode': float,
        'azimuth': float,
        'tilt': float,
        'tilt_eq_lat': float,
        'shading:timestep': Matrix,
        'shading:mxh': Matrix,
        'shading:azal': Matrix,
        'shading:diff': float,
        'enable_user_poa': float,
        'user_poa': Array,
        'rotlim': float,
        'inoct': float,
        'tref': float,
        'gamma': float,
        'inv_eff': float,
        'fd': float,
        'i_ref': float,
        'poa_cutin': float,
        'w_stow': float,
        'concen': float,
        'fhconv': float,
        'shade_mode_1x': float,
        'gcr': float,
        'ar_glass': float,
        'u0': float,
        'u1': float,
        'gh': Array,
        'dn': Array,
        'df': Array,
        'tamb': Array,
        'tdew': Array,
        'wspd': Array,
        'poa': Array,
        'tpoa': Array,
        'tcell': Array,
        'dc': Array,
        'ac': Array,
        'shad_beam_factor': Array,
        'sunup': Array,
        'poa_monthly': Array,
        'solrad_monthly': Array,
        'dc_monthly': Array,
        'ac_monthly': Array,
        'monthly_energy': Array,
        'solrad_annual': float,
        'ac_annual': float,
        'annual_energy': float,
        'location': str,
        'city': str,
        'state': str,
        'lat': float,
        'lon': float,
        'tz': float,
        'elev': float,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix,
        'gen': Array
    }, total=False)

class Data(ssc.DataDict):
    solar_resource_file: str = INPUT(label='local weather file path', type='STRING', group='Weather', required='*', constraints='LOCAL_FILE')
    albedo: float = INPUT(label='Albedo (ground reflectance)', units='frac', type='NUMBER', group='PVWatts', required='?')
    system_size: float = INPUT(label='Nameplate capacity', units='kW', type='NUMBER', group='PVWatts', required='*')
    derate: float = INPUT(label='System derate value', units='frac', type='NUMBER', group='PVWatts', required='*', constraints='MIN=0,MAX=1')
    track_mode: float = INPUT(label='Tracking mode', units='0/1/2/3', type='NUMBER', group='PVWatts', required='*', constraints='MIN=0,MAX=3,INTEGER', meta='Fixed,1Axis,2Axis,AziAxis')
    azimuth: float = INPUT(label='Azimuth angle', units='deg', type='NUMBER', group='PVWatts', required='*', constraints='MIN=0,MAX=360', meta='E=90,S=180,W=270')
    tilt: float = INPUT(label='Tilt angle', units='deg', type='NUMBER', group='PVWatts', required='naof:tilt_eq_lat', constraints='MIN=0,MAX=90', meta='H=0,V=90')
    tilt_eq_lat: float = INPUT(label='Tilt=latitude override', units='0/1', type='NUMBER', group='PVWatts', required='na:tilt', constraints='BOOLEAN')
    shading_timestep: Matrix = INPUT(name='shading:timestep', label='Time step beam shading factors', type='MATRIX', group='PVWatts', required='?')
    shading_mxh: Matrix = INPUT(name='shading:mxh', label='Month x Hour beam shading factors', type='MATRIX', group='PVWatts', required='?')
    shading_azal: Matrix = INPUT(name='shading:azal', label='Azimuth x altitude beam shading factors', type='MATRIX', group='PVWatts', required='?')
    shading_diff: float = INPUT(name='shading:diff', label='Diffuse shading factor', type='NUMBER', group='PVWatts', required='?')
    enable_user_poa: float = INPUT(label='Enable user-defined POA irradiance input', units='0/1', type='NUMBER', group='PVWatts', required='?=0', constraints='BOOLEAN')
    user_poa: Array = INPUT(label='User-defined POA irradiance', units='W/m2', type='ARRAY', group='PVWatts', required='enable_user_poa=1', constraints='LENGTH=8760')
    rotlim: float = INPUT(label='Tracker rotation limit (+/- 1 axis)', units='deg', type='NUMBER', group='PVWatts', required='?=45.0', constraints='MIN=1,MAX=90')
    inoct: float = INPUT(label='Nominal operating cell temperature', units='C', type='NUMBER', group='PVWatts', required='?=45.0', constraints='POSITIVE')
    tref: float = INPUT(label='Reference cell temperature', units='C', type='NUMBER', group='PVWatts', required='?=25.0', constraints='POSITIVE')
    gamma: float = INPUT(label='Max power temperature coefficient', units='%/C', type='NUMBER', group='PVWatts', required='?=-0.5')
    inv_eff: float = INPUT(label='Inverter efficiency at rated power', units='frac', type='NUMBER', group='PVWatts', required='?=0.92', constraints='MIN=0,MAX=1')
    fd: float = INPUT(label='Diffuse fraction', units='0..1', type='NUMBER', group='PVWatts', required='?=1.0', constraints='MIN=0,MAX=1')
    i_ref: float = INPUT(label='Rating condition irradiance', units='W/m2', type='NUMBER', group='PVWatts', required='?=1000', constraints='POSITIVE')
    poa_cutin: float = INPUT(label='Min reqd irradiance for operation', units='W/m2', type='NUMBER', group='PVWatts', required='?=0', constraints='MIN=0')
    w_stow: float = INPUT(label='Wind stow speed', units='m/s', type='NUMBER', group='PVWatts', required='?=0', constraints='MIN=0')
    concen: float = INPUT(label='Concentration ratio', type='NUMBER', group='PVWatts', required='?=1', constraints='MIN=1')
    fhconv: float = INPUT(label='Convective heat transfer factor', type='NUMBER', group='PVWatts', required='?=1', constraints='MIN=0.1')
    shade_mode_1x: float = INPUT(label='Tracker self-shading mode', units='0/1/2', type='NUMBER', group='PVWatts', required='?=2', constraints='INTEGER,MIN=0,MAX=2', meta='0=shading,1=backtrack,2=none')
    gcr: float = INPUT(label='Ground coverage ratio', units='0..1', type='NUMBER', group='PVWatts', required='?=0.3', constraints='MIN=0,MAX=3')
    ar_glass: float = INPUT(label='Enable anti-reflective glass coating (beta)', units='0/1', type='NUMBER', group='PVWatts', required='?=0', constraints='BOOLEAN')
    u0: float = INPUT(label='thermal model coeff U0', type='NUMBER', group='PVWatts', required='?')
    u1: float = INPUT(label='thermal model coeff U0', type='NUMBER', group='PVWatts', required='?')
    gh: Final[Array] = OUTPUT(label='Global horizontal irradiance', units='W/m2', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    dn: Final[Array] = OUTPUT(label='Beam irradiance', units='W/m2', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    df: Final[Array] = OUTPUT(label='Diffuse irradiance', units='W/m2', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    tamb: Final[Array] = OUTPUT(label='Ambient temperature', units='C', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    tdew: Final[Array] = OUTPUT(label='Dew point temperature', units='C', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    wspd: Final[Array] = OUTPUT(label='Wind speed', units='m/s', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    poa: Final[Array] = OUTPUT(label='Plane of array irradiance', units='W/m2', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    tpoa: Final[Array] = OUTPUT(label='Transmitted plane of array irradiance', units='W/m2', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    tcell: Final[Array] = OUTPUT(label='Module temperature', units='C', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    dc: Final[Array] = OUTPUT(label='DC array output', units='Wdc', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    ac: Final[Array] = OUTPUT(label='AC system output', units='Wac', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    shad_beam_factor: Final[Array] = OUTPUT(label='Shading factor for beam radiation', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    sunup: Final[Array] = OUTPUT(label='Sun up over horizon', units='0/1', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    poa_monthly: Final[Array] = OUTPUT(label='Plane of array irradiance', units='kWh/m2', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    solrad_monthly: Final[Array] = OUTPUT(label='Daily average solar irradiance', units='kWh/m2/day', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    dc_monthly: Final[Array] = OUTPUT(label='DC array output', units='kWhdc', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    ac_monthly: Final[Array] = OUTPUT(label='AC system output', units='kWhac', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    monthly_energy: Final[Array] = OUTPUT(label='Monthly energy', units='kWh', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    solrad_annual: Final[float] = OUTPUT(label='Daily average solar irradiance', units='kWh/m2/day', type='NUMBER', group='Annual', required='*')
    ac_annual: Final[float] = OUTPUT(label='Annual AC system output', units='kWhac', type='NUMBER', group='Annual', required='*')
    annual_energy: Final[float] = OUTPUT(label='Annual energy', units='kWh', type='NUMBER', group='Annual', required='*')
    location: Final[str] = OUTPUT(label='Location ID', type='STRING', group='Location', required='*')
    city: Final[str] = OUTPUT(label='City', type='STRING', group='Location', required='*')
    state: Final[str] = OUTPUT(label='State', type='STRING', group='Location', required='*')
    lat: Final[float] = OUTPUT(label='Latitude', units='deg', type='NUMBER', group='Location', required='*')
    lon: Final[float] = OUTPUT(label='Longitude', units='deg', type='NUMBER', group='Location', required='*')
    tz: Final[float] = OUTPUT(label='Time zone', units='hr', type='NUMBER', group='Location', required='*')
    elev: Final[float] = OUTPUT(label='Site elevation', units='m', type='NUMBER', group='Location', required='*')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    gen: Final[Array] = OUTPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 solar_resource_file: str = ...,
                 albedo: float = ...,
                 system_size: float = ...,
                 derate: float = ...,
                 track_mode: float = ...,
                 azimuth: float = ...,
                 tilt: float = ...,
                 tilt_eq_lat: float = ...,
                 shading_timestep: Matrix = ...,
                 shading_mxh: Matrix = ...,
                 shading_azal: Matrix = ...,
                 shading_diff: float = ...,
                 enable_user_poa: float = ...,
                 user_poa: Array = ...,
                 rotlim: float = ...,
                 inoct: float = ...,
                 tref: float = ...,
                 gamma: float = ...,
                 inv_eff: float = ...,
                 fd: float = ...,
                 i_ref: float = ...,
                 poa_cutin: float = ...,
                 w_stow: float = ...,
                 concen: float = ...,
                 fhconv: float = ...,
                 shade_mode_1x: float = ...,
                 gcr: float = ...,
                 ar_glass: float = ...,
                 u0: float = ...,
                 u1: float = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
