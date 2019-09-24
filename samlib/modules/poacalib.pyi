
# This is a generated file

"""poacalib - Calibrates beam and diffuse to give POA input"""

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
        'latitude': float,
        'longitude': float,
        'time_zone': float,
        'array_tilt': float,
        'array_az': float,
        'year': float,
        'albedo': float,
        'poa': Array,
        'beam': Array,
        'diffuse': Array,
        'pcalc': Array
    }, total=False)

class Data(ssc.DataDict):
    latitude: float = INPUT(label='Latitude', units='decimal degrees', type='NUMBER', group='POA Calibrate', required='*', meta='N= positive')
    longitude: float = INPUT(label='Longitude', units='decimal degrees', type='NUMBER', group='POA Calibrate', required='*', meta='E= positive')
    time_zone: float = INPUT(label='Time Zone', type='NUMBER', group='POA Calibrate', required='*', constraints='MIN=-12,MAX=12', meta='-7= Denver')
    array_tilt: float = INPUT(label='Array tilt', units='degrees', type='NUMBER', group='POA Calibrate', required='*', constraints='MIN=0,MAX=90', meta='0-90')
    array_az: float = INPUT(label='Array Azimuth', units='degrees', type='NUMBER', group='POA Calibrate', required='*', constraints='MIN=0,MAX=360', meta='0=N, 90=E, 180=S')
    year: float = INPUT(label='Year', type='NUMBER', group='POA Calibrate', required='*')
    albedo: float = INPUT(label='Albedo', type='NUMBER', group='POA Calibrate', required='*', constraints='MIN=0,MAX=1')
    poa: Array = INPUT(label='Plane of Array', units='W/m^2', type='ARRAY', group='POA Calibrate', required='*', constraints='LENGTH=8760')
    beam: Array = INOUT(label='Beam Irradiation', units='W/m^2', type='ARRAY', group='POA Calibrate', required='*', constraints='LENGTH=8760')
    diffuse: Array = INOUT(label='Diffuse Irradiation', units='W/m^2', type='ARRAY', group='POA Calibrate', required='*', constraints='LENGTH=8760')
    pcalc: Final[Array] = OUTPUT(label='Calculated POA', units='W/m^2', type='ARRAY', group='POA Calibrate', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 latitude: float = ...,
                 longitude: float = ...,
                 time_zone: float = ...,
                 array_tilt: float = ...,
                 array_az: float = ...,
                 year: float = ...,
                 albedo: float = ...,
                 poa: Array = ...,
                 beam: Array = ...,
                 diffuse: Array = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
