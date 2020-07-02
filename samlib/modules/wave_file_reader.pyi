
# This is a generated file

"""wave_file_reader - SAM Wave Resource File Reader"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'wave_resource_filename': str,
        'use_specific_wf_wave': float,
        'name': str,
        'city': str,
        'state': str,
        'country': str,
        'lat': float,
        'lon': float,
        'nearby_buoy_number': str,
        'average_power_flux': float,
        'bathymetry': str,
        'sea_bed': str,
        'tz': float,
        'data_source': str,
        'notes': str,
        'wave_resource_matrix': Matrix
}, total=False)

class Data(ssc.DataDict):
    wave_resource_filename: str = INPUT(label='local weather file path', type='STRING', group='Weather Reader', required='*', constraints='LOCAL_FILE')
    use_specific_wf_wave: float = INPUT(label='user specified file', units='0/1', type='NUMBER', group='Weather Reader', required='?=0', constraints='INTEGER,MIN=0,MAX=1')
    name: Final[str] = OUTPUT(label='Name', type='STRING', group='Weather Reader', required='use_specific_wf_wave=0')
    city: Final[str] = OUTPUT(label='City', type='STRING', group='Weather Reader', required='use_specific_wf_wave=0')
    state: Final[str] = OUTPUT(label='State', type='STRING', group='Weather Reader', required='use_specific_wf_wave=0')
    country: Final[str] = OUTPUT(label='Country', type='STRING', group='Weather Reader', required='use_specific_wf_wave=0')
    lat: Final[float] = OUTPUT(label='Latitude', units='deg', type='NUMBER', group='Weather Reader', required='use_specific_wf_wave=0')
    lon: Final[float] = OUTPUT(label='Longitude', units='deg', type='NUMBER', group='Weather Reader', required='use_specific_wf_wave=0')
    nearby_buoy_number: Final[str] = OUTPUT(label='Nearby buoy number', type='STRING', group='Weather Reader', required='use_specific_wf_wave=0')
    average_power_flux: Final[float] = OUTPUT(label='Distance to shore', units='kW/m', type='NUMBER', group='Weather Reader', required='use_specific_wf_wave=0')
    bathymetry: Final[str] = OUTPUT(label='Bathymetry', type='STRING', group='Weather Reader', required='use_specific_wf_wave=0')
    sea_bed: Final[str] = OUTPUT(label='Sea bed', type='STRING', group='Weather Reader', required='use_specific_wf_wave=0')
    tz: Final[float] = OUTPUT(label='Time zone', type='NUMBER', group='Weather Reader', required='use_specific_wf_wave=0')
    data_source: Final[str] = OUTPUT(label='Data source', type='STRING', group='Weather Reader', required='use_specific_wf_wave=0')
    notes: Final[str] = OUTPUT(label='Notes', type='STRING', group='Weather Reader', required='use_specific_wf_wave=0')
    wave_resource_matrix: Final[Matrix] = OUTPUT(label='Frequency distribution of resource', units='m/s', type='MATRIX', group='Weather Reader', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 wave_resource_filename: str = ...,
                 use_specific_wf_wave: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
