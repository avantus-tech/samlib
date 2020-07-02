
# This is a generated file

"""pvwattsv5_1ts - pvwattsv5_1ts- single timestep calculation of PV system performance."""

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
        'alb': float,
        'time_step': float,
        'system_capacity': float,
        'module_type': float,
        'dc_ac_ratio': float,
        'inv_eff': float,
        'losses': float,
        'array_type': float,
        'tilt': float,
        'azimuth': float,
        'gcr': float,
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
    alb: float = INPUT(label='Albedo', units='frac', type='NUMBER', group='PVWatts', required='?=0.2')
    time_step: float = INPUT(label='Time step of input data', units='hr', type='NUMBER', group='PVWatts', required='?=1', constraints='POSITIVE')
    system_capacity: float = INPUT(label='System size (DC nameplate)', units='kW', type='NUMBER', group='System Design', required='*')
    module_type: float = INPUT(label='Module type', units='0/1/2', type='NUMBER', group='System Design', required='?=0', constraints='MIN=0,MAX=2,INTEGER', meta='Standard,Premium,Thin film')
    dc_ac_ratio: float = INPUT(label='DC to AC ratio', units='ratio', type='NUMBER', group='System Design', required='?=1.1', constraints='POSITIVE')
    inv_eff: float = INPUT(label='Inverter efficiency at rated power', units='%', type='NUMBER', group='System Design', required='?=96', constraints='MIN=90,MAX=99.5')
    losses: float = INPUT(label='System losses', units='%', type='NUMBER', group='System Design', required='*', constraints='MIN=-5,MAX=99', meta='Total system losses')
    array_type: float = INPUT(label='Array type', units='0/1/2/3/4', type='NUMBER', group='System Design', required='*', constraints='MIN=0,MAX=4,INTEGER', meta='Fixed OR,Fixed Roof,1Axis,Backtracked,2Axis')
    tilt: float = INPUT(label='Tilt angle', units='deg', type='NUMBER', group='System Design', required='array_type<4', constraints='MIN=0,MAX=90', meta='H=0,V=90')
    azimuth: float = INPUT(label='Azimuth angle', units='deg', type='NUMBER', group='System Design', required='array_type<4', constraints='MIN=0,MAX=360', meta='E=90,S=180,W=270')
    gcr: float = INPUT(label='Ground coverage ratio', units='0..1', type='NUMBER', group='System Design', required='?=0.4', constraints='MIN=0.01,MAX=0.99')
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
                 alb: float = ...,
                 time_step: float = ...,
                 system_capacity: float = ...,
                 module_type: float = ...,
                 dc_ac_ratio: float = ...,
                 inv_eff: float = ...,
                 losses: float = ...,
                 array_type: float = ...,
                 tilt: float = ...,
                 azimuth: float = ...,
                 gcr: float = ...,
                 tcell: float = ...,
                 poa: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
