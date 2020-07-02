
# This is a generated file

"""thermalrate - Thermal flat rate structure net revenue calculator"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'en_thermal_rates': float,
        'analysis_period': float,
        'system_use_lifetime_output': float,
        'fuelcell_power_thermal': Array,
        'thermal_load': Array,
        'inflation_rate': float,
        'thermal_degradation': Array,
        'thermal_load_escalation': Array,
        'thermal_rate_escalation': Array,
        'thermal_buy_rate_option': float,
        'thermal_buy_rate': Array,
        'thermal_buy_rate_flat': float,
        'thermal_sell_rate_option': float,
        'thermal_sell_rate': Array,
        'thermal_sell_rate_flat': float,
        'thermal_revenue_with_system': Array,
        'thermal_revenue_without_system': Array,
        'thermal_load_year1': float,
        'thermal_savings_year1': float,
        'thermal_cost_with_system_year1': float,
        'thermal_cost_without_system_year1': float
}, total=False)

class Data(ssc.DataDict):
    en_thermal_rates: float = INPUT(label='Optionally enable/disable thermal_rate', units='years', type='NUMBER', group='Thermal Rate', constraints='INTEGER,MIN=0,MAX=1')
    analysis_period: float = INPUT(label='Number of years in analysis', units='years', type='NUMBER', group='Lifetime', required='*', constraints='INTEGER,POSITIVE')
    system_use_lifetime_output: float = INPUT(label='Lifetime hourly system outputs', units='0/1', type='NUMBER', group='Lifetime', required='*', constraints='INTEGER,MIN=0,MAX=1', meta='0=hourly first year,1=hourly lifetime')
    fuelcell_power_thermal: Array = INPUT(label='Fuel cell power generated', units='kW-t', type='ARRAY', group='Thermal Rate', required='*')
    thermal_load: Array = INOUT(label='Thermal load (year 1)', units='kW-t', type='ARRAY', group='Thermal Rate')
    inflation_rate: float = INPUT(label='Inflation rate', units='%', type='NUMBER', group='Lifetime', required='*', constraints='MIN=-99')
    thermal_degradation: Array = INPUT(label='Annual energy degradation', units='%', type='ARRAY', group='Thermal Rate', required='?=0')
    thermal_load_escalation: Array = INPUT(label='Annual load escalation', units='%/year', type='ARRAY', group='Thermal Rate', required='?=0')
    thermal_rate_escalation: Array = INPUT(label='Annual thermal rate escalation', units='%/year', type='ARRAY', group='Thermal Rate', required='?=0')
    thermal_buy_rate_option: float = INPUT(label='Thermal buy rate option', units='0/1', type='NUMBER', group='Thermal Rate', required='?=0', constraints='INTEGER,MIN=0,MAX=1', meta='0=flat,1=timestep')
    thermal_buy_rate: Array = INPUT(label='Thermal buy rate', units='$/kW-t', type='ARRAY', group='Thermal Rate', required='?=0')
    thermal_buy_rate_flat: float = INPUT(label='Thermal buy rate flat', units='$/kW-t', type='NUMBER', group='Thermal Rate', required='?=0')
    thermal_sell_rate_option: float = INPUT(label='Thermal sell rate option', units='0/1', type='NUMBER', group='Thermal Rate', required='?=0', constraints='INTEGER,MIN=0,MAX=1', meta='0=flat,1=timestep')
    thermal_sell_rate: Array = INPUT(label='Thermal sell rate', units='$/kW-t', type='ARRAY', group='Thermal Rate', required='?=0')
    thermal_sell_rate_flat: float = INPUT(label='Thermal sell rate flat', units='$/kW-t', type='NUMBER', group='Thermal Rate', required='?=0')
    thermal_revenue_with_system: Final[Array] = OUTPUT(label='Thermal revenue with system', units='$', type='ARRAY', group='Time Series', required='*')
    thermal_revenue_without_system: Final[Array] = OUTPUT(label='Thermal revenue without system', units='$', type='ARRAY', group='Time Series', required='*')
    thermal_load_year1: Final[float] = OUTPUT(label='Thermal load (year 1)', units='$', type='NUMBER', required='*')
    thermal_savings_year1: Final[float] = OUTPUT(label='Thermal savings (year 1)', units='$', type='NUMBER', required='*')
    thermal_cost_with_system_year1: Final[float] = OUTPUT(label='Thermal cost with sytem (year 1)', units='$', type='NUMBER', required='*')
    thermal_cost_without_system_year1: Final[float] = OUTPUT(label='Thermal cost without system (year 1)', units='$', type='NUMBER', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 en_thermal_rates: float = ...,
                 analysis_period: float = ...,
                 system_use_lifetime_output: float = ...,
                 fuelcell_power_thermal: Array = ...,
                 thermal_load: Array = ...,
                 inflation_rate: float = ...,
                 thermal_degradation: Array = ...,
                 thermal_load_escalation: Array = ...,
                 thermal_rate_escalation: Array = ...,
                 thermal_buy_rate_option: float = ...,
                 thermal_buy_rate: Array = ...,
                 thermal_buy_rate_flat: float = ...,
                 thermal_sell_rate_option: float = ...,
                 thermal_sell_rate: Array = ...,
                 thermal_sell_rate_flat: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
