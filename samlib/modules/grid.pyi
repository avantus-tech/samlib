
# This is a generated file

"""grid - Grid model"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'system_use_lifetime_output': float,
        'analysis_period': float,
        'enable_interconnection_limit': float,
        'grid_interconnection_limit_kwac': float,
        'gen': Array,
        'load': Array,
        'system_pre_interconnect_kwac': Array,
        'capacity_factor_interconnect_ac': float,
        'annual_energy_pre_interconnect_ac': float,
        'annual_energy': float,
        'annual_ac_interconnect_loss_percent': float,
        'annual_ac_interconnect_loss_kwh': float,
        'system_pre_curtailment_kwac': Array,
        'capacity_factor_curtailment_ac': float,
        'annual_energy_pre_curtailment_ac': float,
        'annual_ac_curtailment_loss_percent': float,
        'annual_ac_curtailment_loss_kwh': float,
        'grid_curtailment': Array
}, total=False)

class Data(ssc.DataDict):
    system_use_lifetime_output: float = INPUT(label='Lifetime simulation', units='0/1', type='NUMBER', group='Lifetime', required='?=0', constraints='BOOLEAN', meta='0=SingleYearRepeated,1=RunEveryYear')
    analysis_period: float = INPUT(label='Lifetime analysis period', units='years', type='NUMBER', group='Lifetime', required='system_use_lifetime_output=1', meta='The number of years in the simulation')
    enable_interconnection_limit: float = INPUT(label='Enable grid interconnection limit', units='0/1', type='NUMBER', group='GridLimits', meta='Enable a grid interconnection limit')
    grid_interconnection_limit_kwac: float = INPUT(label='Grid interconnection limit', units='kWac', type='NUMBER', group='GridLimits')
    gen: Array = INOUT(label='System power generated', units='kW', type='ARRAY', group='System Output', meta='Lifetime system generation')
    load: Array = INPUT(label='Electricity load (year 1)', units='kW', type='ARRAY', group='Load')
    system_pre_interconnect_kwac: Final[Array] = OUTPUT(label='System power before grid interconnect', units='kW', type='ARRAY', meta='Lifetime system generation')
    capacity_factor_interconnect_ac: Final[float] = OUTPUT(label='Capacity factor of the interconnection (year 1)', units='%', type='NUMBER')
    annual_energy_pre_interconnect_ac: Final[float] = OUTPUT(label='Annual Energy AC pre-interconnection (year 1)', units='kWh', type='NUMBER')
    annual_energy: float = INOUT(label='Annual Energy AC (year 1)', units='kWh', type='NUMBER', group='System Output')
    annual_ac_interconnect_loss_percent: Final[float] = OUTPUT(label='Annual Energy loss from interconnection limit (year 1)', units='%', type='NUMBER')
    annual_ac_interconnect_loss_kwh: Final[float] = OUTPUT(label='Annual Energy loss from interconnection limit (year 1)', units='kWh', type='NUMBER')
    system_pre_curtailment_kwac: Final[Array] = OUTPUT(label='System power before grid curtailment', units='kW', type='ARRAY', meta='Lifetime system generation')
    capacity_factor_curtailment_ac: Final[float] = OUTPUT(label='Capacity factor of the curtailment (year 1)', units='%', type='NUMBER')
    annual_energy_pre_curtailment_ac: Final[float] = OUTPUT(label='Annual Energy AC pre-curtailment (year 1)', units='kWh', type='NUMBER')
    annual_ac_curtailment_loss_percent: Final[float] = OUTPUT(label='Annual Energy loss from curtailment (year 1)', units='%', type='NUMBER')
    annual_ac_curtailment_loss_kwh: Final[float] = OUTPUT(label='Annual Energy loss from curtailment (year 1)', units='kWh', type='NUMBER')
    grid_curtailment: Array = INPUT(label='Grid curtailment as energy delivery limit (first year)', units='MW', type='ARRAY', group='GridLimits', required='?')

    def __init__(self, *args: Mapping[str, Any],
                 system_use_lifetime_output: float = ...,
                 analysis_period: float = ...,
                 enable_interconnection_limit: float = ...,
                 grid_interconnection_limit_kwac: float = ...,
                 gen: Array = ...,
                 load: Array = ...,
                 annual_energy: float = ...,
                 grid_curtailment: Array = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
