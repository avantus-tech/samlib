
# This is a generated file

"""annualoutput - Annual Output_"""

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
        'analysis_period': float,
        'energy_availability': Array,
        'energy_degradation': Array,
        'energy_curtailment': Matrix,
        'system_use_lifetime_output': float,
        'system_hourly_energy': Array,
        'annual_energy': Array,
        'monthly_energy': Array,
        'hourly_energy': Array,
        'annual_availability': Array,
        'annual_degradation': Array
    }, total=False)

class Data(ssc.DataDict):
    analysis_period: float = INPUT(label='Analyis period', units='years', type='NUMBER', group='AnnualOutput', required='?=30', constraints='INTEGER,MIN=0,MAX=50')
    energy_availability: Array = INPUT(label='Annual energy availability', units='%', type='ARRAY', group='AnnualOutput', required='*')
    energy_degradation: Array = INPUT(label='Annual energy degradation', units='%', type='ARRAY', group='AnnualOutput', required='*')
    energy_curtailment: Matrix = INPUT(label='First year energy curtailment', type='MATRIX', group='AnnualOutput', required='*', meta='(0..1)')
    system_use_lifetime_output: float = INPUT(label='Lifetime hourly system outputs', units='0/1', type='NUMBER', group='AnnualOutput', required='*', constraints='INTEGER,MIN=0', meta='0=hourly first year,1=hourly lifetime')
    system_hourly_energy: Array = INPUT(label='Hourly energy produced by the system', units='kW', type='ARRAY', group='AnnualOutput', required='*')
    annual_energy: Final[Array] = OUTPUT(label='Annual energy', units='kWh', type='ARRAY', group='AnnualOutput', required='*')
    monthly_energy: Final[Array] = OUTPUT(label='Monthly energy', units='kWh', type='ARRAY', group='AnnualOutput', required='*')
    hourly_energy: Final[Array] = OUTPUT(label='Hourly energy', units='kWh', type='ARRAY', group='AnnualOutput', required='*')
    annual_availability: Final[Array] = OUTPUT(label='Annual availability', type='ARRAY', group='AnnualOutput', required='*')
    annual_degradation: Final[Array] = OUTPUT(label='Annual degradation', type='ARRAY', group='AnnualOutput', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 analysis_period: float = ...,
                 energy_availability: Array = ...,
                 energy_degradation: Array = ...,
                 energy_curtailment: Matrix = ...,
                 system_use_lifetime_output: float = ...,
                 system_hourly_energy: Array = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
