
# This is a generated file

"""wind_file_reader - SAM Wind Resource File Reader (SRW)"""

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
        'scan_header_only': float,
        'requested_ht': float,
        'interpolate': float,
        'city': str,
        'state': str,
        'location_id': str,
        'country': str,
        'description': str,
        'year': float,
        'lat': float,
        'lon': float,
        'elev': float,
        'closest_speed_meas_ht': float,
        'closest_dir_meas_ht': float,
        'wind_speed': Array,
        'wind_direction': Array,
        'temperature': Array,
        'pressure': Array
    }, total=False)

class Data(ssc.DataDict):
    file_name: str = INPUT(label='local weather file path', type='STRING', group='Weather Reader', required='*', constraints='LOCAL_FILE')
    scan_header_only: float = INPUT(label='only reader headers', units='0/1', type='NUMBER', group='Weather Reader', required='?=0', constraints='BOOLEAN')
    requested_ht: float = INPUT(label='requested measurement height', units='m', type='NUMBER', group='Weather Reader', required='*')
    interpolate: float = INPUT(label='interpolate to closest height measured?', units='m', type='NUMBER', group='Weather Reader', required='scan_header_only=0', constraints='BOOLEAN')
    city: Final[str] = OUTPUT(label='City', type='STRING', group='Weather Reader', required='*')
    state: Final[str] = OUTPUT(label='State', type='STRING', group='Weather Reader', required='*')
    location_id: Final[str] = OUTPUT(label='Location ID', type='STRING', group='Weather Reader', required='*')
    country: Final[str] = OUTPUT(label='Country', type='STRING', group='Weather Reader', required='*')
    description: Final[str] = OUTPUT(label='Description', type='STRING', group='Weather Reader', required='*')
    year: Final[float] = OUTPUT(label='Calendar year of data', type='NUMBER', group='Weather Reader', required='*', constraints='INTEGER')
    lat: Final[float] = OUTPUT(label='Latitude', units='deg', type='NUMBER', group='Weather Reader', required='*')
    lon: Final[float] = OUTPUT(label='Longitude', units='deg', type='NUMBER', group='Weather Reader', required='*')
    elev: Final[float] = OUTPUT(label='Elevation', units='m', type='NUMBER', group='Weather Reader', required='*')
    closest_speed_meas_ht: Final[float] = OUTPUT(label='Height of closest speed meas in file', units='m', type='NUMBER', group='Weather Reader', required='*')
    closest_dir_meas_ht: Final[float] = OUTPUT(label='Height of closest direction meas in file', units='m', type='NUMBER', group='Weather Reader', required='*')
    wind_speed: Final[Array] = OUTPUT(label='Wind Speed', units='m/s', type='ARRAY', group='Weather Reader', required='*')
    wind_direction: Final[Array] = OUTPUT(label='Wind Direction', units='deg', type='ARRAY', group='Weather Reader', required='*', constraints='LENGTH_EQUAL=wind_speed', meta='0=N,E=90')
    temperature: Final[Array] = OUTPUT(label='Temperature', units="'C", type='ARRAY', group='Weather Reader', required='*', constraints='LENGTH_EQUAL=wind_speed')
    pressure: Final[Array] = OUTPUT(label='Atmospheric Pressure', units='atm', type='ARRAY', group='Weather Reader', required='*', constraints='LENGTH_EQUAL=wind_speed')

    def __init__(self, *args: Mapping[str, Any],
                 file_name: str = ...,
                 scan_header_only: float = ...,
                 requested_ht: float = ...,
                 interpolate: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
