
# This is a generated file

"""snowmodel - Estimates the Detrimental Effects due to Snow Fall"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'subarray1_poa_shaded': Array,
        'wspd': Array,
        'hourly_gen': Array,
        'tdry': Array,
        'subarray1_surf_tilt': Array,
        'sunup': Array,
        'snowdepth': Array,
        'subarray1_nmody': float,
        'subarray1_tilt': float,
        'subarray1_track_mode': float,
        'hourly_energy_before_snow': Array,
        'monthly_energy_before_snow': Array,
        'annual_energy_before_snow': float,
        'monthly_energy': Array,
        'annual_energy': float
}, total=False)

class Data(ssc.DataDict):
    subarray1_poa_shaded: Array = INPUT(label='Plane of Array Incidence', units='W/m^2', type='ARRAY', group='PV Snow Model', required='*', constraints='LENGTH=8760')
    wspd: Array = INPUT(label='Wind Speed', units='m/s', type='ARRAY', group='PV Snow Model', required='*', constraints='LENGTH=8760')
    hourly_gen: Array = INPUT(label='Hourly Energy', units='kwh', type='ARRAY', group='Time Series', required='*', constraints='LENGTH=8760')
    tdry: Array = INPUT(label='Ambient Temperature', units='Degrees Celsius', type='ARRAY', group='PV Snow Model', required='*', constraints='LENGTH=8760')
    subarray1_surf_tilt: Array = INPUT(label='Surface Tilt', units='Degrees', type='ARRAY', group='PV Snow Model', required='*', constraints='LENGTH=8760')
    sunup: Array = INPUT(label='Sun up over horizon', units='0/1', type='ARRAY', group='Time Series', required='*')
    snowdepth: Array = INPUT(label='Snow Depth', units='cm', type='ARRAY', group='PV Snow Model', required='*', constraints='LENGTH=8760')
    subarray1_nmody: float = INPUT(label='Number of Modules in a Row', type='NUMBER', group='PV Snow Model', required='*')
    subarray1_tilt: float = INPUT(label='Base tilt', units='Degrees', type='NUMBER', group='PV Snow Model', required='*')
    subarray1_track_mode: float = INPUT(label='Tracking Mode', type='NUMBER', group='PV Snow Model', required='*')
    hourly_energy_before_snow: Final[Array] = OUTPUT(label='Hourly Energy Without Snow Loss', units='kwh', type='ARRAY', group='Time Series', required='*')
    monthly_energy_before_snow: Final[Array] = OUTPUT(label='Monthly Energy Without Snow Loss', units='kwh', type='ARRAY', group='Monthly', required='*')
    annual_energy_before_snow: Final[float] = OUTPUT(label='Annual Energy Without Snow Losses', units='kwh', type='NUMBER', group='Annual', required='*')
    monthly_energy: Final[Array] = OUTPUT(label='Monthly Energy', units='kwh', type='ARRAY', group='Monthly', required='*')
    annual_energy: Final[float] = OUTPUT(label='Annual Energy', units='kwh', type='NUMBER', group='Annual', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 subarray1_poa_shaded: Array = ...,
                 wspd: Array = ...,
                 hourly_gen: Array = ...,
                 tdry: Array = ...,
                 subarray1_surf_tilt: Array = ...,
                 sunup: Array = ...,
                 snowdepth: Array = ...,
                 subarray1_nmody: float = ...,
                 subarray1_tilt: float = ...,
                 subarray1_track_mode: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
