
# This is a generated file

"""pvwattsv1_1ts - pvwattsv1_1ts- single timestep calculation of PV system performance."""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'year': float,
        'month': float,
        'day': float,
        'hour': float,
        'minute': float,
        'lat': float,
        'lon': float,
        'tz': float,
        'beam': float,
        'diffuse': float,
        'tamb': float,
        'wspd': float,
        'snow': float,
        'time_step': float,
        'system_size': float,
        'derate': float,
        'track_mode': float,
        'azimuth': float,
        'tilt': float,
        'rotlim': float,
        't_noct': float,
        't_ref': float,
        'gamma': float,
        'inv_eff': float,
        'fd': float,
        'i_ref': float,
        'poa_cutin': float,
        'w_stow': float,
        'tcell': float,
        'poa': float,
        'dc': float,
        'ac': float
}, total=False)

class Data(ssc.DataDict):
    year: float = INPUT(label='Year', units='yr', type='NUMBER', group='PVWatts', required='*')
    month: float = INPUT(label='Month', units='mn', type='NUMBER', group='PVWatts', required='*', meta='1-12')
    day: float = INPUT(label='Day', units='dy', type='NUMBER', group='PVWatts', required='*', meta='1-days in month')
    hour: float = INPUT(label='Hour', units='hr', type='NUMBER', group='PVWatts', required='*', meta='0-23')
    minute: float = INPUT(label='Minute', units='min', type='NUMBER', group='PVWatts', required='*', meta='0-59')
    lat: float = INPUT(label='Latitude', units='deg', type='NUMBER', group='PVWatts', required='*')
    lon: float = INPUT(label='Longitude', units='deg', type='NUMBER', group='PVWatts', required='*')
    tz: float = INPUT(label='Time zone', units='hr', type='NUMBER', group='PVWatts', required='*')
    beam: float = INPUT(label='Beam normal irradiance', units='W/m2', type='NUMBER', group='PVWatts', required='*')
    diffuse: float = INPUT(label='Diffuse irradiance', units='W/m2', type='NUMBER', group='PVWatts', required='*')
    tamb: float = INPUT(label='Ambient temperature', units='C', type='NUMBER', group='PVWatts', required='*')
    wspd: float = INPUT(label='Wind speed', units='m/s', type='NUMBER', group='PVWatts', required='*')
    snow: float = INPUT(label='Snow cover', units='cm', type='NUMBER', group='PVWatts', required='?=0')
    time_step: float = INPUT(label='Time step of input data', units='hr', type='NUMBER', group='PVWatts', required='?=1', constraints='POSITIVE')
    system_size: float = INPUT(label='Nameplate capacity', units='kW', type='NUMBER', group='PVWatts', required='*')
    derate: float = INPUT(label='System derate value', units='frac', type='NUMBER', group='PVWatts', required='*', constraints='MIN=0,MAX=1')
    track_mode: float = INPUT(label='Tracking mode', units='0/1/2/3', type='NUMBER', group='PVWatts', required='*', constraints='MIN=0,MAX=3,INTEGER', meta='Fixed,1Axis,2Axis,AziAxis')
    azimuth: float = INPUT(label='Azimuth angle', units='deg', type='NUMBER', group='PVWatts', required='*', constraints='MIN=0,MAX=360', meta='E=90,S=180,W=270')
    tilt: float = INPUT(label='Tilt angle', units='deg', type='NUMBER', group='PVWatts', required='naof:tilt_eq_lat', constraints='MIN=0,MAX=90', meta='H=0,V=90')
    rotlim: float = INPUT(label='Tracker rotation limit (+/- 1 axis)', units='deg', type='NUMBER', group='PVWatts', required='?=45.0', constraints='MIN=1,MAX=90')
    t_noct: float = INPUT(label='Nominal operating cell temperature', units='C', type='NUMBER', group='PVWatts', required='?=45.0', constraints='POSITIVE')
    t_ref: float = INPUT(label='Reference cell temperature', units='C', type='NUMBER', group='PVWatts', required='?=25.0', constraints='POSITIVE')
    gamma: float = INPUT(label='Max power temperature coefficient', units='%/C', type='NUMBER', group='PVWatts', required='?=-0.5')
    inv_eff: float = INPUT(label='Inverter efficiency at rated power', units='frac', type='NUMBER', group='PVWatts', required='?=0.92', constraints='MIN=0,MAX=1')
    fd: float = INPUT(label='Diffuse fraction', units='0..1', type='NUMBER', group='PVWatts', required='?=1.0', constraints='MIN=0,MAX=1')
    i_ref: float = INPUT(label='Rating condition irradiance', units='W/m2', type='NUMBER', group='PVWatts', required='?=1000', constraints='POSITIVE')
    poa_cutin: float = INPUT(label='Min reqd irradiance for operation', units='W/m2', type='NUMBER', group='PVWatts', required='?=0', constraints='MIN=0')
    w_stow: float = INPUT(label='Wind stow speed', units='m/s', type='NUMBER', group='PVWatts', required='?=0', constraints='MIN=0')
    tcell: float = INOUT(label='Module temperature', units='C', type='NUMBER', group='PVWatts', required='*')
    poa: float = INOUT(label='Plane of array irradiance', units='W/m2', type='NUMBER', group='PVWatts', required='*')
    dc: Final[float] = OUTPUT(label='DC array output', units='Wdc', type='NUMBER', group='PVWatts', required='*')
    ac: Final[float] = OUTPUT(label='AC system output', units='Wac', type='NUMBER', group='PVWatts', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 year: float = ...,
                 month: float = ...,
                 day: float = ...,
                 hour: float = ...,
                 minute: float = ...,
                 lat: float = ...,
                 lon: float = ...,
                 tz: float = ...,
                 beam: float = ...,
                 diffuse: float = ...,
                 tamb: float = ...,
                 wspd: float = ...,
                 snow: float = ...,
                 time_step: float = ...,
                 system_size: float = ...,
                 derate: float = ...,
                 track_mode: float = ...,
                 azimuth: float = ...,
                 tilt: float = ...,
                 rotlim: float = ...,
                 t_noct: float = ...,
                 t_ref: float = ...,
                 gamma: float = ...,
                 inv_eff: float = ...,
                 fd: float = ...,
                 i_ref: float = ...,
                 poa_cutin: float = ...,
                 w_stow: float = ...,
                 tcell: float = ...,
                 poa: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
