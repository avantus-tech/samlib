
# This is a generated file

"""irradproc - Irradiance Processor"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'irrad_mode': float,
        'beam': Array,
        'diffuse': Array,
        'global': Array,
        'albedo': Array,
        'albedo_const': float,
        'year': Array,
        'month': Array,
        'day': Array,
        'hour': Array,
        'minute': Array,
        'lat': float,
        'lon': float,
        'tz': float,
        'sky_model': float,
        'track_mode': float,
        'azimuth': float,
        'tilt': float,
        'rotlim': float,
        'backtrack': float,
        'gcr': float,
        'poa_beam': Array,
        'poa_skydiff': Array,
        'poa_gnddiff': Array,
        'poa_skydiff_iso': Array,
        'poa_skydiff_cir': Array,
        'poa_skydiff_hor': Array,
        'incidence': Array,
        'surf_tilt': Array,
        'surf_azm': Array,
        'axis_rotation': Array,
        'bt_diff': Array,
        'sun_azm': Array,
        'sun_zen': Array,
        'sun_elv': Array,
        'sun_dec': Array
}, total=False)

class Data(ssc.DataDict):
    irrad_mode: float = INPUT(label='Irradiance input mode', units='0/1/2', type='NUMBER', group='Irradiance Processor', required='?=0', constraints='INTEGER,MIN=0,MAX=2', meta='Beam+Diff,Global+Beam, Global+Diff')
    beam: Array = INPUT(label='Beam normal irradiance', units='W/m2', type='ARRAY', group='Irradiance Processor', required='irrad_mode~2')
    diffuse: Array = INPUT(label='Diffuse horizontal irradiance', units='W/m2', type='ARRAY', group='Irradiance Processor', required='irrad_mode~1', constraints='LENGTH_EQUAL=beam')
    global_: Array = INPUT(name='global', label='Global horizontal irradiance', units='W/m2', type='ARRAY', group='Irradiance Processor', required='irrad_mode~0', constraints='LENGTH_EQUAL=beam')
    albedo: Array = INPUT(label='Ground reflectance (time depend.)', units='frac', type='ARRAY', group='Irradiance Processor', required='?', constraints='LENGTH_EQUAL=beam', meta='0..1')
    albedo_const: float = INPUT(label='Ground reflectance (single value)', units='frac', type='NUMBER', group='Irradiance Processor', required='?=0.2', meta='0..1')
    year: Array = INPUT(label='Year', units='yr', type='ARRAY', group='Irradiance Processor', required='*', constraints='LENGTH_EQUAL=beam')
    month: Array = INPUT(label='Month', units='mn', type='ARRAY', group='Irradiance Processor', required='*', constraints='LENGTH_EQUAL=beam', meta='1-12')
    day: Array = INPUT(label='Day', units='dy', type='ARRAY', group='Irradiance Processor', required='*', constraints='LENGTH_EQUAL=beam', meta='1-days in month')
    hour: Array = INPUT(label='Hour', units='hr', type='ARRAY', group='Irradiance Processor', required='*', constraints='LENGTH_EQUAL=beam', meta='0-23')
    minute: Array = INPUT(label='Minute', units='min', type='ARRAY', group='Irradiance Processor', required='*', constraints='LENGTH_EQUAL=beam', meta='0-59')
    lat: float = INPUT(label='Latitude', units='deg', type='NUMBER', group='Irradiance Processor', required='*')
    lon: float = INPUT(label='Longitude', units='deg', type='NUMBER', group='Irradiance Processor', required='*')
    tz: float = INPUT(label='Time zone', units='hr', type='NUMBER', group='Irradiance Processor', required='*')
    sky_model: float = INPUT(label='Tilted surface irradiance model', units='0/1/2', type='NUMBER', group='Irradiance Processor', required='?=2', constraints='INTEGER,MIN=0,MAX=2', meta='Isotropic,HDKR,Perez')
    track_mode: float = INPUT(label='Tracking mode', units='0/1/2', type='NUMBER', group='Irradiance Processor', required='*', constraints='MIN=0,MAX=2,INTEGER', meta='Fixed,1Axis,2Axis')
    azimuth: float = INPUT(label='Azimuth angle', units='deg', type='NUMBER', group='Irradiance Processor', required='*', constraints='MIN=0,MAX=360', meta='E=90,S=180,W=270')
    tilt: float = INPUT(label='Tilt angle', units='deg', type='NUMBER', group='Irradiance Processor', required='?', constraints='MIN=0,MAX=90', meta='H=0,V=90')
    rotlim: float = INPUT(label='Rotational limit on tracker', units='deg', type='NUMBER', group='Irradiance Processor', required='?=45', constraints='MIN=0,MAX=90')
    backtrack: float = INPUT(label='Enable backtracking', units='0/1', type='NUMBER', group='Irradiance Processor', required='?=0', constraints='BOOLEAN')
    gcr: float = INPUT(label='Ground coverage ratio', units='0..1', type='NUMBER', group='Irradiance Processor', required='backtrack=1', constraints='MIN=0,MAX=1')
    poa_beam: Final[Array] = OUTPUT(label='Incident Beam Irradiance', units='W/m2', type='ARRAY', group='Irradiance Processor', required='*')
    poa_skydiff: Final[Array] = OUTPUT(label='Incident Sky Diffuse', units='W/m2', type='ARRAY', group='Irradiance Processor', required='*')
    poa_gnddiff: Final[Array] = OUTPUT(label='Incident Ground Reflected Diffuse', units='W/m2', type='ARRAY', group='Irradiance Processor', required='*')
    poa_skydiff_iso: Final[Array] = OUTPUT(label='Incident Diffuse Isotropic Component', units='W/m2', type='ARRAY', group='Irradiance Processor', required='*')
    poa_skydiff_cir: Final[Array] = OUTPUT(label='Incident Diffuse Circumsolar Component', units='W/m2', type='ARRAY', group='Irradiance Processor', required='*')
    poa_skydiff_hor: Final[Array] = OUTPUT(label='Incident Diffuse Horizon Brightening Component', units='W/m2', type='ARRAY', group='Irradiance Processor', required='*')
    incidence: Final[Array] = OUTPUT(label='Incidence angle to surface', units='deg', type='ARRAY', group='Irradiance Processor', required='*', constraints='LENGTH_EQUAL=beam')
    surf_tilt: Final[Array] = OUTPUT(label='Surface tilt angle', units='deg', type='ARRAY', group='Irradiance Processor', required='*', constraints='LENGTH_EQUAL=beam')
    surf_azm: Final[Array] = OUTPUT(label='Surface azimuth angle', units='deg', type='ARRAY', group='Irradiance Processor', required='*', constraints='LENGTH_EQUAL=beam')
    axis_rotation: Final[Array] = OUTPUT(label='Tracking axis rotation angle', units='deg', type='ARRAY', group='Irradiance Processor', required='*', constraints='LENGTH_EQUAL=beam')
    bt_diff: Final[Array] = OUTPUT(label='Backtracking difference from ideal rotation', units='deg', type='ARRAY', group='Irradiance Processor', required='*', constraints='LENGTH_EQUAL=beam')
    sun_azm: Final[Array] = OUTPUT(label='Solar azimuth', units='deg', type='ARRAY', group='Irradiance Processor', required='*', constraints='LENGTH_EQUAL=beam')
    sun_zen: Final[Array] = OUTPUT(label='Solar zenith', units='deg', type='ARRAY', group='Irradiance Processor', required='*', constraints='LENGTH_EQUAL=beam')
    sun_elv: Final[Array] = OUTPUT(label='Sun elevation', units='deg', type='ARRAY', group='Irradiance Processor', required='*', constraints='LENGTH_EQUAL=beam')
    sun_dec: Final[Array] = OUTPUT(label='Sun declination', units='deg', type='ARRAY', group='Irradiance Processor', required='*', constraints='LENGTH_EQUAL=beam')

    def __init__(self, *args: Mapping[str, Any],
                 irrad_mode: float = ...,
                 beam: Array = ...,
                 diffuse: Array = ...,
                 global_: Array = ...,
                 albedo: Array = ...,
                 albedo_const: float = ...,
                 year: Array = ...,
                 month: Array = ...,
                 day: Array = ...,
                 hour: Array = ...,
                 minute: Array = ...,
                 lat: float = ...,
                 lon: float = ...,
                 tz: float = ...,
                 sky_model: float = ...,
                 track_mode: float = ...,
                 azimuth: float = ...,
                 tilt: float = ...,
                 rotlim: float = ...,
                 backtrack: float = ...,
                 gcr: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
