
# This is a generated file

"""belpe - Estimates an electric load profile given basic building characteristics and a weather file"""

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
        'en_belpe': float,
        'load': Array,
        'solar_resource_file': str,
        'floor_area': float,
        'Stories': float,
        'YrBuilt': float,
        'Retrofits': float,
        'Occupants': float,
        'Occ_Schedule': Array,
        'THeat': float,
        'TCool': float,
        'THeatSB': float,
        'TCoolSB': float,
        'T_Sched': Array,
        'en_heat': float,
        'en_cool': float,
        'en_fridge': float,
        'en_range': float,
        'en_dish': float,
        'en_wash': float,
        'en_dry': float,
        'en_mels': float,
        'Monthly_util': Array
    }, total=False)

class Data(ssc.DataDict):
    en_belpe: float = INPUT(label='Enable building load calculator', units='0/1', type='NUMBER', group='Load Profile Estimator', required='*', constraints='BOOLEAN')
    load: Array = INOUT(label='Electricity load (year 1)', units='kW', type='ARRAY', group='Load Profile Estimator', required='en_belpe=0')
    solar_resource_file: str = INPUT(label='Weather Data file', units='n/a', type='STRING', group='Load Profile Estimator', required='en_belpe=1', constraints='LOCAL_FILE')
    floor_area: float = INPUT(label='Building floor area', units='m2', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1')
    Stories: float = INPUT(label='Number of stories', units='#', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1')
    YrBuilt: float = INPUT(label='Year built', units='yr', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1')
    Retrofits: float = INPUT(label='Energy retrofitted', units='0/1', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1', meta='0=No, 1=Yes')
    Occupants: float = INPUT(label='Occupants', units='#', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1')
    Occ_Schedule: Array = INPUT(label='Hourly occupant schedule', units='frac/hr', type='ARRAY', group='Load Profile Estimator', required='en_belpe=1', constraints='LENGTH=24')
    THeat: float = INPUT(label='Heating setpoint', units='degF', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1')
    TCool: float = INPUT(label='Cooling setpoint', units='degF', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1')
    THeatSB: float = INPUT(label='Heating setpoint setback', units='degf', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1')
    TCoolSB: float = INPUT(label='Cooling setpoint setback', units='degF', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1')
    T_Sched: Array = INPUT(label='Temperature schedule', units='0/1', type='ARRAY', group='Load Profile Estimator', required='en_belpe=1', constraints='LENGTH=24')
    en_heat: float = INPUT(label='Enable electric heat', units='0/1', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1', constraints='BOOLEAN')
    en_cool: float = INPUT(label='Enable electric cool', units='0/1', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1', constraints='BOOLEAN')
    en_fridge: float = INPUT(label='Enable electric fridge', units='0/1', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1', constraints='BOOLEAN')
    en_range: float = INPUT(label='Enable electric range', units='0/1', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1', constraints='BOOLEAN')
    en_dish: float = INPUT(label='Enable electric dishwasher', units='0/1', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1', constraints='BOOLEAN')
    en_wash: float = INPUT(label='Enable electric washer', units='0/1', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1', constraints='BOOLEAN')
    en_dry: float = INPUT(label='Enable electric dryer', units='0/1', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1', constraints='BOOLEAN')
    en_mels: float = INPUT(label='Enable misc electric loads', units='0/1', type='NUMBER', group='Load Profile Estimator', required='en_belpe=1', constraints='BOOLEAN')
    Monthly_util: Array = INPUT(label='Monthly consumption from utility bill', units='kWh', type='ARRAY', group='Load Profile Estimator', required='en_belpe=1', constraints='LENGTH=12')

    def __init__(self, *args: Mapping[str, Any],
                 en_belpe: float = ...,
                 load: Array = ...,
                 solar_resource_file: str = ...,
                 floor_area: float = ...,
                 Stories: float = ...,
                 YrBuilt: float = ...,
                 Retrofits: float = ...,
                 Occupants: float = ...,
                 Occ_Schedule: Array = ...,
                 THeat: float = ...,
                 TCool: float = ...,
                 THeatSB: float = ...,
                 TCoolSB: float = ...,
                 T_Sched: Array = ...,
                 en_heat: float = ...,
                 en_cool: float = ...,
                 en_fridge: float = ...,
                 en_range: float = ...,
                 en_dish: float = ...,
                 en_wash: float = ...,
                 en_dry: float = ...,
                 en_mels: float = ...,
                 Monthly_util: Array = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
