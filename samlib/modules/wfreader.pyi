
# This is a generated file

"""wfreader - Standard Weather File Format Reader (TMY2, TMY3, EPW, SMW, WFCSV)"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'file_name': str,
        'header_only': float,
        'lat': float,
        'lon': float,
        'tz': float,
        'elev': float,
        'location': str,
        'city': str,
        'state': str,
        'country': str,
        'description': str,
        'source': str,
        'url': str,
        'format': str,
        'start': float,
        'step': float,
        'nrecords': float,
        'year': Array,
        'month': Array,
        'day': Array,
        'hour': Array,
        'minute': Array,
        'global': Array,
        'beam': Array,
        'diffuse': Array,
        'poa': Array,
        'wspd': Array,
        'wdir': Array,
        'tdry': Array,
        'twet': Array,
        'tdew': Array,
        'rhum': Array,
        'pres': Array,
        'snow': Array,
        'albedo': Array,
        'annual_global': float,
        'annual_beam': float,
        'annual_diffuse': float,
        'annual_tdry': float,
        'annual_wspd': float,
        'annual_snow': float,
        'annual_albedo': float
}, total=False)

class Data(ssc.DataDict):
    file_name: str = INPUT(label='local weather file path', type='STRING', group='Weather Reader', required='*', constraints='LOCAL_FILE')
    header_only: float = INPUT(label='read header only', units='0/1', type='NUMBER', group='Weather Reader', required='?=0', constraints='BOOLEAN')
    lat: Final[float] = OUTPUT(label='Latitude', units='deg', type='NUMBER', group='Weather Reader', required='*')
    lon: Final[float] = OUTPUT(label='Longitude', units='deg', type='NUMBER', group='Weather Reader', required='*')
    tz: Final[float] = OUTPUT(label='Time zone', units='hr', type='NUMBER', group='Weather Reader', required='*')
    elev: Final[float] = OUTPUT(label='Elevation', units='m', type='NUMBER', group='Weather Reader', required='*')
    location: Final[str] = OUTPUT(label='Location ID', type='STRING', group='Weather Reader', required='*')
    city: Final[str] = OUTPUT(label='City', type='STRING', group='Weather Reader', required='*')
    state: Final[str] = OUTPUT(label='State', type='STRING', group='Weather Reader', required='*')
    country: Final[str] = OUTPUT(label='Country', type='STRING', group='Weather Reader', required='*')
    description: Final[str] = OUTPUT(label='Description', type='STRING', group='Weather Reader', required='*')
    source: Final[str] = OUTPUT(label='Source', type='STRING', group='Weather Reader', required='*')
    url: Final[str] = OUTPUT(label='URL', type='STRING', group='Weather Reader', required='*')
    format: Final[str] = OUTPUT(label='File format', type='STRING', group='Weather Reader', required='*', meta='tmy2,tmy3,epw,smw,wfcsv')
    start: Final[float] = OUTPUT(label='Start', units='sec', type='NUMBER', group='Weather Reader', required='*')
    step: Final[float] = OUTPUT(label='Step', units='sec', type='NUMBER', group='Weather Reader', required='*')
    nrecords: Final[float] = OUTPUT(label='Number of records', type='NUMBER', group='Weather Reader', required='*')
    year: Final[Array] = OUTPUT(label='Year', units='yr', type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year')
    month: Final[Array] = OUTPUT(label='Month', units='mn', type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year', meta='1-12')
    day: Final[Array] = OUTPUT(label='Day', units='dy', type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year', meta='1-365')
    hour: Final[Array] = OUTPUT(label='Hour', units='hr', type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year', meta='0-23')
    minute: Final[Array] = OUTPUT(label='Minute', units='min', type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year', meta='0-59')
    global_: Final[Array] = OUTPUT(name='global', label='Global Horizontal Irradiance', units='W/m2', type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year')
    beam: Final[Array] = OUTPUT(label='Beam Normal Irradiance', units='W/m2', type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year')
    diffuse: Final[Array] = OUTPUT(label='Diffuse Horizontal Irradiance', units='W/m2', type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year')
    poa: Final[Array] = OUTPUT(label='Plane of Array Irradiance', units='W/m2', type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year')
    wspd: Final[Array] = OUTPUT(label='Wind Speed', units='m/s', type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year')
    wdir: Final[Array] = OUTPUT(label='Wind Direction', units='deg', type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year', meta='0=N,E=90')
    tdry: Final[Array] = OUTPUT(label='Temperature Dry Bulb', units="'C", type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year')
    twet: Final[Array] = OUTPUT(label='Temperature Wet Bulb', units="'C", type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year')
    tdew: Final[Array] = OUTPUT(label='Temperature Dew Point', units="'C", type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year')
    rhum: Final[Array] = OUTPUT(label='Relative Humidity', units='%', type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year')
    pres: Final[Array] = OUTPUT(label='Atmospheric Pressure', units='millibar', type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year')
    snow: Final[Array] = OUTPUT(label='Snow Depth', units='cm', type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year')
    albedo: Final[Array] = OUTPUT(label='Ground Reflectance', units='frac', type='ARRAY', group='Weather Reader', required='header_only=0', constraints='LENGTH_EQUAL=year', meta='0..1')
    annual_global: Final[float] = OUTPUT(label='Average daily global horizontal', units='kWh/m2/day', type='NUMBER', group='Weather Reader', required='header_only=0')
    annual_beam: Final[float] = OUTPUT(label='Average daily beam normal', units='kWh/m2/day', type='NUMBER', group='Weather Reader', required='header_only=0')
    annual_diffuse: Final[float] = OUTPUT(label='Average daily diffuse', units='kWh/m2/day', type='NUMBER', group='Weather Reader', required='header_only=0')
    annual_tdry: Final[float] = OUTPUT(label='Average dry bulb temperature', units="'C", type='NUMBER', group='Weather Reader', required='header_only=0')
    annual_wspd: Final[float] = OUTPUT(label='Average wind speed', units='m/s', type='NUMBER', group='Weather Reader', required='header_only=0')
    annual_snow: Final[float] = OUTPUT(label='Maximum snow depth', units='cm', type='NUMBER', group='Weather Reader', required='header_only=0')
    annual_albedo: Final[float] = OUTPUT(label='Average albedo', type='NUMBER', group='Weather Reader', required='header_only=0')

    def __init__(self, *args: Mapping[str, Any],
                 file_name: str = ...,
                 header_only: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
