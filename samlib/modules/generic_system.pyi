
# This is a generated file

"""generic_system - Generic System"""

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
        'spec_mode': float,
        'derate': float,
        'system_capacity': float,
        'user_capacity_factor': float,
        'heat_rate': float,
        'conv_eff': float,
        'energy_output_array': Array,
        'load': Array,
        'system_use_lifetime_output': float,
        'analysis_period': float,
        'generic_degradation': Array,
        'monthly_energy': Array,
        'annual_energy': float,
        'annual_fuel_usage': float,
        'water_usage': float,
        'system_heat_rate': float,
        'capacity_factor': float,
        'kwh_per_kw': float,
        'dc_adjust:constant': float,
        'dc_adjust:hourly': Array,
        'dc_adjust:periods': Matrix,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix,
        'gen': Array
    }, total=False)

class Data(ssc.DataDict):
    spec_mode: float = INPUT(label='Spec mode: 0=constant CF,1=profile', type='NUMBER', group='generic_system', required='*')
    derate: float = INPUT(label='Derate', units='%', type='NUMBER', group='generic_system', required='*')
    system_capacity: float = INOUT(label='Nameplace Capcity', units='kW', type='NUMBER', group='generic_system', required='*')
    user_capacity_factor: float = INPUT(label='Capacity Factor', units='%', type='NUMBER', group='generic_system', required='*')
    heat_rate: float = INPUT(label='Heat Rate', units='MMBTUs/MWhe', type='NUMBER', group='generic_system', required='*')
    conv_eff: float = INPUT(label='Conversion Efficiency', units='%', type='NUMBER', group='generic_system', required='*')
    energy_output_array: Array = INPUT(label='Array of Energy Output Profile', units='kW', type='ARRAY', group='generic_system', required='*')
    load: Array = INPUT(label='Electricity load (year 1)', units='kW', type='ARRAY', group='generic_system')
    system_use_lifetime_output: float = INPUT(label='Generic lifetime simulation', units='0/1', type='NUMBER', group='generic_system', required='?=0', constraints='INTEGER,MIN=0,MAX=1')
    analysis_period: float = INPUT(label='Lifetime analysis period', units='years', type='NUMBER', group='generic_system', required='system_use_lifetime_output=1')
    generic_degradation: Array = INPUT(label='Annual module degradation', units='%/year', type='ARRAY', group='generic_system', required='system_use_lifetime_output=1')
    monthly_energy: Final[Array] = OUTPUT(label='Monthly Energy', units='kWh', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    annual_energy: Final[float] = OUTPUT(label='Annual Energy', units='kWh', type='NUMBER', group='Annual', required='*')
    annual_fuel_usage: Final[float] = OUTPUT(label='Annual Fuel Usage', units='kWht', type='NUMBER', group='Annual', required='*')
    water_usage: Final[float] = OUTPUT(label='Annual Water Usage', type='NUMBER', group='Annual', required='*')
    system_heat_rate: Final[float] = OUTPUT(label='Heat Rate Conversion Factor', units='MMBTUs/MWhe', type='NUMBER', group='Annual', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', group='Annual', required='*')
    kwh_per_kw: Final[float] = OUTPUT(label='First year kWh/kW', units='kWh/kW', type='NUMBER', group='Annual', required='*')
    dc_adjust_constant: float = INPUT(name='dc_adjust:constant', label='DC Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', constraints='MAX=100')
    dc_adjust_hourly: Array = INPUT(name='dc_adjust:hourly', label='DC Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', constraints='LENGTH=8760')
    dc_adjust_periods: Matrix = INPUT(name='dc_adjust:periods', label='DC Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    gen: Final[Array] = OUTPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 spec_mode: float = ...,
                 derate: float = ...,
                 system_capacity: float = ...,
                 user_capacity_factor: float = ...,
                 heat_rate: float = ...,
                 conv_eff: float = ...,
                 energy_output_array: Array = ...,
                 load: Array = ...,
                 system_use_lifetime_output: float = ...,
                 analysis_period: float = ...,
                 generic_degradation: Array = ...,
                 dc_adjust_constant: float = ...,
                 dc_adjust_hourly: Array = ...,
                 dc_adjust_periods: Matrix = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
