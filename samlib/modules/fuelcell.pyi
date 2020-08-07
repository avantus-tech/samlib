
# This is a generated file

"""fuelcell - Fuel cell model"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'percent_complete': float,
        'system_use_lifetime_output': float,
        'analysis_period': float,
        'gen': Array,
        'load': Array,
        'fuelcell_availability_schedule': Matrix,
        'fuelcell_degradation': float,
        'fuelcell_degradation_restart': float,
        'fuelcell_degradation_restart_schedule': float,
        'fuelcell_degradation_restarts_per_year': float,
        'fuelcell_fixed_pct': float,
        'fuelcell_dynamic_response_up': float,
        'fuelcell_dynamic_response_down': float,
        'fuelcell_efficiency': Matrix,
        'fuelcell_efficiency_choice': float,
        'fuelcell_fuel_available': float,
        'fuelcell_fuel_price': float,
        'fuelcell_fuel_type': float,
        'fuelcell_lhv': float,
        'fuelcell_number_of_units': float,
        'fuelcell_operation_options': float,
        'fuelcell_replacement_option': float,
        'fuelcell_replacement_percent': float,
        'fuelcell_replacement_schedule': Array,
        'fuelcell_shutdown_time': float,
        'fuelcell_startup_time': float,
        'fuelcell_is_started': float,
        'fuelcell_type': float,
        'fuelcell_unit_max_power': float,
        'fuelcell_unit_min_power': float,
        'fuelcell_dispatch': Array,
        'fuelcell_dispatch_choice': float,
        'dispatch_manual_fuelcellcharge': Array,
        'dispatch_manual_fuelcelldischarge': Array,
        'dispatch_manual_percent_fc_discharge': Array,
        'dispatch_manual_units_fc_discharge': Array,
        'dispatch_manual_sched': Matrix,
        'dispatch_manual_sched_weekend': Matrix,
        'capacity_factor': float,
        'annual_energy': float,
        'fuelcell_power': Array,
        'fuelcell_power_max_percent': Array,
        'fuelcell_percent_load': Array,
        'fuelcell_electrical_efficiency': Array,
        'fuelcell_power_thermal': Array,
        'fuelcell_fuel_consumption_mcf': Array,
        'fuelcell_to_load': Array,
        'fuelcell_to_grid': Array,
        'fuelcell_replacement': Array,
        'system_heat_rate': float,
        'annual_fuel_usage': float,
        'annual_fuel_usage_lifetime': Array
}, total=False)

class Data(ssc.DataDict):
    percent_complete: float = INOUT(label='Estimated simulation status', units='%', type='NUMBER')
    system_use_lifetime_output: float = INPUT(label='Lifetime simulation', units='0/1', type='NUMBER', group='Lifetime', required='?=0', constraints='BOOLEAN', meta='0=SingleYearRepeated,1=RunEveryYear')
    analysis_period: float = INPUT(label='Lifetime analysis period', units='years', type='NUMBER', group='Lifetime', required='system_use_lifetime_output=1', meta='The number of years in the simulation')
    gen: Array = INOUT(label='System power generated', units='kW', type='ARRAY', meta='Lifetime system generation')
    load: Array = INPUT(label='Electricity load (year 1)', units='kW', type='ARRAY', group='Load')
    fuelcell_availability_schedule: Matrix = INPUT(label='Fuel cell availability schedule ', units='Column 1: Hour of year start shutdown/Column 2: Hours duration of shutdown ', type='MATRIX', group='Fuel Cell')
    fuelcell_degradation: float = INPUT(label='Fuel cell degradation per hour', units='kW/h', type='NUMBER', group='Fuel Cell')
    fuelcell_degradation_restart: float = INPUT(label='Fuel cell degradation at restart', units='kW', type='NUMBER', group='Fuel Cell')
    fuelcell_degradation_restart_schedule: float = INPUT(label='Fuel cell enable scheduled restarts', units='0/1', type='NUMBER', group='Fuel Cell')
    fuelcell_degradation_restarts_per_year: float = INPUT(label='Fuel cell scheduled restarts per year', type='NUMBER', group='Fuel Cell')
    fuelcell_fixed_pct: float = INPUT(label='Fuel cell fixed operation percent', units='%', type='NUMBER', group='Fuel Cell')
    fuelcell_dynamic_response_up: float = INPUT(label='Fuel cell ramp rate limit up', units='kW/h', type='NUMBER', group='Fuel Cell')
    fuelcell_dynamic_response_down: float = INPUT(label='Fuel cell ramp rate limit down', units='kW/h', type='NUMBER', group='Fuel Cell')
    fuelcell_efficiency: Matrix = INPUT(label='Fuel cell efficiency table ', type='MATRIX', group='Fuel Cell')
    fuelcell_efficiency_choice: float = INPUT(label='Fuel cell efficiency definition choice ', units='0/1', type='NUMBER', group='Fuel Cell', meta='0=OriginalNameplate,1=DegradedNameplate')
    fuelcell_fuel_available: float = INPUT(label='Fuel cell available fuel quantity', units='MCf', type='NUMBER', group='Fuel Cell')
    fuelcell_fuel_price: float = INPUT(label='Fuel cell price', units='$/MCf', type='NUMBER', group='Fuel Cell')
    fuelcell_fuel_type: float = INPUT(label='Fuel cell type', units='0/1', type='NUMBER', group='Fuel Cell')
    fuelcell_lhv: float = INPUT(label='Fuel cell lower heating value', units='Btu/ft3', type='NUMBER', group='Fuel Cell')
    fuelcell_number_of_units: float = INPUT(label='Fuel cell number of units', type='NUMBER', group='Fuel Cell')
    fuelcell_operation_options: float = INPUT(label='Fuel cell turn off options', units='0/1', type='NUMBER', group='Fuel Cell')
    fuelcell_replacement_option: float = INPUT(label='Fuel cell replacement option', units='0/1/2', type='NUMBER', group='Fuel Cell')
    fuelcell_replacement_percent: float = INPUT(label='Fuel cell replace at percentage', type='NUMBER', group='Fuel Cell')
    fuelcell_replacement_schedule: Array = INPUT(label='Fuel cell replace on schedule', type='ARRAY', group='Fuel Cell')
    fuelcell_shutdown_time: float = INPUT(label='Fuel cell shutdown hours', units='hours', type='NUMBER', group='Fuel Cell')
    fuelcell_startup_time: float = INPUT(label='Fuel cell startup hours', units='hours', type='NUMBER', group='Fuel Cell')
    fuelcell_is_started: float = INPUT(label='Fuel cell is started', units='0/1', type='NUMBER', group='Fuel Cell')
    fuelcell_type: float = INPUT(label='Fuel cell type', units='0/1/2', type='NUMBER', group='Fuel Cell')
    fuelcell_unit_max_power: float = INPUT(label='Fuel cell max power per unit', units='kW', type='NUMBER', group='Fuel Cell')
    fuelcell_unit_min_power: float = INPUT(label='Fuel cell min power per unit', units='kW', type='NUMBER', group='Fuel Cell')
    fuelcell_dispatch: Array = INPUT(label='Fuel cell dispatch input per unit', units='kW', type='ARRAY', group='Fuel Cell')
    fuelcell_dispatch_choice: float = INPUT(label='Fuel cell dispatch choice', units='0/1/2', type='NUMBER', group='Fuel Cell')
    dispatch_manual_fuelcellcharge: Array = INPUT(label='Periods 1-6 charging allowed?', type='ARRAY', group='Fuel Cell')
    dispatch_manual_fuelcelldischarge: Array = INPUT(label='Periods 1-6 discharging allowed?', type='ARRAY', group='Fuel Cell')
    dispatch_manual_percent_fc_discharge: Array = INPUT(label='Periods 1-6 percent of max fuelcell output', type='ARRAY', group='Fuel Cell')
    dispatch_manual_units_fc_discharge: Array = INPUT(label='Periods 1-6 number of fuel cell units?', type='ARRAY', group='Fuel Cell')
    dispatch_manual_sched: Matrix = INPUT(label='Dispatch schedule for weekday', type='MATRIX', group='Fuel Cell')
    dispatch_manual_sched_weekend: Matrix = INPUT(label='Dispatch schedule for weekend', type='MATRIX', group='Fuel Cell')
    capacity_factor: float = INOUT(label='Capacity factor', units='%', type='NUMBER', required='?=0')
    annual_energy: float = INOUT(label='Annual Energy', units='kWh', type='NUMBER', required='?=0')
    fuelcell_power: Final[Array] = OUTPUT(label='Electricity from fuel cell', units='kW', type='ARRAY', group='Fuel Cell')
    fuelcell_power_max_percent: Final[Array] = OUTPUT(label='Fuel cell max power percent available', units='%', type='ARRAY', group='Fuel Cell')
    fuelcell_percent_load: Final[Array] = OUTPUT(label='Fuel cell percent load', units='%', type='ARRAY', group='Fuel Cell')
    fuelcell_electrical_efficiency: Final[Array] = OUTPUT(label='Fuel cell electrical efficiency', units='%', type='ARRAY', group='Fuel Cell')
    fuelcell_power_thermal: Final[Array] = OUTPUT(label='Heat from fuel cell', units='kWt', type='ARRAY', group='Fuel Cell')
    fuelcell_fuel_consumption_mcf: Final[Array] = OUTPUT(label='Fuel consumption of fuel cell', units='MCf', type='ARRAY', group='Fuel Cell')
    fuelcell_to_load: Final[Array] = OUTPUT(label='Electricity to load from fuel cell', units='kW', type='ARRAY', group='Fuel Cell')
    fuelcell_to_grid: Final[Array] = OUTPUT(label='Electricity to grid from fuel cell', units='kW', type='ARRAY', group='Fuel Cell')
    fuelcell_replacement: Final[Array] = OUTPUT(label='Fuel cell replacements per year', units='number/year', type='ARRAY', group='Fuel Cell')
    system_heat_rate: Final[float] = OUTPUT(label='Heat rate conversion factor (MMBTUs/MWhe)', units='MMBTUs/MWhe', type='NUMBER', group='Fuel Cell', required='*')
    annual_fuel_usage: Final[float] = OUTPUT(label='Annual Fuel Usage', units='kWht', type='NUMBER', group='Fuel Cell', required='*')
    annual_fuel_usage_lifetime: Final[Array] = OUTPUT(label='Annual Fuel Usage (lifetime)', units='kWht', type='ARRAY', group='Fuel Cell')

    def __init__(self, *args: Mapping[str, Any],
                 percent_complete: float = ...,
                 system_use_lifetime_output: float = ...,
                 analysis_period: float = ...,
                 gen: Array = ...,
                 load: Array = ...,
                 fuelcell_availability_schedule: Matrix = ...,
                 fuelcell_degradation: float = ...,
                 fuelcell_degradation_restart: float = ...,
                 fuelcell_degradation_restart_schedule: float = ...,
                 fuelcell_degradation_restarts_per_year: float = ...,
                 fuelcell_fixed_pct: float = ...,
                 fuelcell_dynamic_response_up: float = ...,
                 fuelcell_dynamic_response_down: float = ...,
                 fuelcell_efficiency: Matrix = ...,
                 fuelcell_efficiency_choice: float = ...,
                 fuelcell_fuel_available: float = ...,
                 fuelcell_fuel_price: float = ...,
                 fuelcell_fuel_type: float = ...,
                 fuelcell_lhv: float = ...,
                 fuelcell_number_of_units: float = ...,
                 fuelcell_operation_options: float = ...,
                 fuelcell_replacement_option: float = ...,
                 fuelcell_replacement_percent: float = ...,
                 fuelcell_replacement_schedule: Array = ...,
                 fuelcell_shutdown_time: float = ...,
                 fuelcell_startup_time: float = ...,
                 fuelcell_is_started: float = ...,
                 fuelcell_type: float = ...,
                 fuelcell_unit_max_power: float = ...,
                 fuelcell_unit_min_power: float = ...,
                 fuelcell_dispatch: Array = ...,
                 fuelcell_dispatch_choice: float = ...,
                 dispatch_manual_fuelcellcharge: Array = ...,
                 dispatch_manual_fuelcelldischarge: Array = ...,
                 dispatch_manual_percent_fc_discharge: Array = ...,
                 dispatch_manual_units_fc_discharge: Array = ...,
                 dispatch_manual_sched: Matrix = ...,
                 dispatch_manual_sched_weekend: Matrix = ...,
                 capacity_factor: float = ...,
                 annual_energy: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
