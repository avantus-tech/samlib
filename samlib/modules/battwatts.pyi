
# This is a generated file

"""battwatts - simple battery model"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'batt_simple_enable': float,
        'batt_simple_kwh': float,
        'batt_simple_kw': float,
        'batt_simple_chemistry': float,
        'batt_simple_dispatch': float,
        'batt_simple_meter_position': float,
        'dc': Array,
        'ac': Array,
        'load': Array,
        'inverter_model': float,
        'inverter_efficiency': float,
        'batt_q0': Array,
        'batt_q1': Array,
        'batt_q2': Array,
        'batt_SOC': Array,
        'batt_DOD': Array,
        'batt_qmaxI': Array,
        'batt_qmax': Array,
        'batt_qmax_thermal': Array,
        'batt_I': Array,
        'batt_voltage_cell': Array,
        'batt_voltage': Array,
        'batt_DOD_cycle_average': Array,
        'batt_cycles': Array,
        'batt_temperature': Array,
        'batt_capacity_percent': Array,
        'batt_capacity_thermal_percent': Array,
        'batt_bank_replacement': Array,
        'batt_power': Array,
        'grid_power': Array,
        'pv_to_load': Array,
        'batt_to_load': Array,
        'grid_to_load': Array,
        'pv_to_batt': Array,
        'grid_to_batt': Array,
        'pv_to_grid': Array,
        'batt_to_grid': Array,
        'batt_conversion_loss': Array,
        'batt_system_loss': Array,
        'grid_power_target': Array,
        'batt_power_target': Array,
        'batt_cost_to_cycle': Array,
        'market_sell_rate_series_yr1': Array,
        'monthly_pv_to_load': Array,
        'monthly_batt_to_load': Array,
        'monthly_grid_to_load': Array,
        'monthly_pv_to_grid': Array,
        'monthly_batt_to_grid': Array,
        'monthly_pv_to_batt': Array,
        'monthly_grid_to_batt': Array,
        'batt_annual_charge_from_pv': Array,
        'batt_annual_charge_from_grid': Array,
        'batt_annual_charge_energy': Array,
        'batt_annual_discharge_energy': Array,
        'batt_annual_energy_loss': Array,
        'batt_annual_energy_system_loss': Array,
        'annual_export_to_grid_energy': Array,
        'annual_import_to_grid_energy': Array,
        'average_battery_conversion_efficiency': float,
        'average_battery_roundtrip_efficiency': float,
        'batt_pv_charge_percent': float,
        'batt_bank_installed_capacity': float,
        'batt_dispatch_sched': Matrix,
        'gen': Array
}, total=False)

class Data(ssc.DataDict):
    batt_simple_enable: float = INPUT(label='Enable Battery', units='0/1', type='NUMBER', group='battwatts', required='?=0', constraints='BOOLEAN')
    batt_simple_kwh: float = INPUT(label='Battery Capacity', units='kWh', type='NUMBER', group='battwatts', required='?=0')
    batt_simple_kw: float = INPUT(label='Battery Power', units='kW', type='NUMBER', group='battwatts', required='?=0')
    batt_simple_chemistry: float = INPUT(label='Battery Chemistry', units='0=lead acid/1=Li-ion/2', type='NUMBER', group='battwatts', required='?=0')
    batt_simple_dispatch: float = INPUT(label='Battery Dispatch', units='0=peak shaving look ahead/1=peak shaving look behind', type='NUMBER', group='battwatts', required='?=0')
    batt_simple_meter_position: float = INPUT(label='Battery Meter Position', units='0=behind meter/1=front of meter', type='NUMBER', group='battwatts', required='?=0')
    dc: Array = INPUT(label='DC array power', units='W', type='ARRAY')
    ac: Array = INPUT(label='AC inverter power', units='W', type='ARRAY')
    load: Array = INPUT(label='Electricity load (year 1)', units='kW', type='ARRAY')
    inverter_model: float = INPUT(label='Inverter model specifier', type='NUMBER', constraints='INTEGER,MIN=0,MAX=4', meta='0=cec,1=datasheet,2=partload,3=coefficientgenerator,4=generic')
    inverter_efficiency: float = INPUT(label='Inverter Efficiency', units='%', type='NUMBER')
    batt_q0: Final[Array] = OUTPUT(label='Battery total charge', units='Ah', type='ARRAY', group='Battery')
    batt_q1: Final[Array] = OUTPUT(label='Battery available charge', units='Ah', type='ARRAY', group='Battery')
    batt_q2: Final[Array] = OUTPUT(label='Battery bound charge', units='Ah', type='ARRAY', group='Battery')
    batt_SOC: Final[Array] = OUTPUT(label='Battery state of charge', units='%', type='ARRAY', group='Battery')
    batt_DOD: Final[Array] = OUTPUT(label='Battery cycle depth of discharge', units='%', type='ARRAY', group='Battery')
    batt_qmaxI: Final[Array] = OUTPUT(label='Battery maximum capacity at current', units='Ah', type='ARRAY', group='Battery')
    batt_qmax: Final[Array] = OUTPUT(label='Battery maximum charge with degradation', units='Ah', type='ARRAY', group='Battery')
    batt_qmax_thermal: Final[Array] = OUTPUT(label='Battery maximum charge at temperature', units='Ah', type='ARRAY', group='Battery')
    batt_I: Final[Array] = OUTPUT(label='Battery current', units='A', type='ARRAY', group='Battery')
    batt_voltage_cell: Final[Array] = OUTPUT(label='Battery cell voltage', units='V', type='ARRAY', group='Battery')
    batt_voltage: Final[Array] = OUTPUT(label='Battery voltage', units='V', type='ARRAY', group='Battery')
    batt_DOD_cycle_average: Final[Array] = OUTPUT(label='Battery average cycle DOD', type='ARRAY', group='Battery')
    batt_cycles: Final[Array] = OUTPUT(label='Battery number of cycles', type='ARRAY', group='Battery')
    batt_temperature: Final[Array] = OUTPUT(label='Battery temperature', units='C', type='ARRAY', group='Battery')
    batt_capacity_percent: Final[Array] = OUTPUT(label='Battery capacity percent for lifetime', units='%', type='ARRAY', group='Battery')
    batt_capacity_thermal_percent: Final[Array] = OUTPUT(label='Battery capacity percent for temperature', units='%', type='ARRAY', group='Battery')
    batt_bank_replacement: Final[Array] = OUTPUT(label='Battery bank replacements per year', units='number/year', type='ARRAY', group='Battery')
    batt_power: Final[Array] = OUTPUT(label='Electricity to/from battery', units='kW', type='ARRAY', group='Battery')
    grid_power: Final[Array] = OUTPUT(label='Electricity to/from grid', units='kW', type='ARRAY', group='Battery')
    pv_to_load: Final[Array] = OUTPUT(label='Electricity to load from PV', units='kW', type='ARRAY', group='Battery')
    batt_to_load: Final[Array] = OUTPUT(label='Electricity to load from battery', units='kW', type='ARRAY', group='Battery')
    grid_to_load: Final[Array] = OUTPUT(label='Electricity to load from grid', units='kW', type='ARRAY', group='Battery')
    pv_to_batt: Final[Array] = OUTPUT(label='Electricity to battery from PV', units='kW', type='ARRAY', group='Battery')
    grid_to_batt: Final[Array] = OUTPUT(label='Electricity to battery from grid', units='kW', type='ARRAY', group='Battery')
    pv_to_grid: Final[Array] = OUTPUT(label='Electricity to grid from PV', units='kW', type='ARRAY', group='Battery')
    batt_to_grid: Final[Array] = OUTPUT(label='Electricity to grid from battery', units='kW', type='ARRAY', group='Battery')
    batt_conversion_loss: Final[Array] = OUTPUT(label='Electricity loss in battery power electronics', units='kW', type='ARRAY', group='Battery')
    batt_system_loss: Final[Array] = OUTPUT(label='Electricity loss from battery ancillary equipment', units='kW', type='ARRAY', group='Battery')
    grid_power_target: Final[Array] = OUTPUT(label='Electricity grid power target for automated dispatch', units='kW', type='ARRAY', group='Battery')
    batt_power_target: Final[Array] = OUTPUT(label='Electricity battery power target for automated dispatch', units='kW', type='ARRAY', group='Battery')
    batt_cost_to_cycle: Final[Array] = OUTPUT(label='Battery computed cost to cycle', units='$/cycle', type='ARRAY', group='Battery')
    market_sell_rate_series_yr1: Final[Array] = OUTPUT(label='Market sell rate (Year 1)', units='$/MWh', type='ARRAY', group='Battery')
    monthly_pv_to_load: Final[Array] = OUTPUT(label='Energy to load from PV', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_batt_to_load: Final[Array] = OUTPUT(label='Energy to load from battery', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_grid_to_load: Final[Array] = OUTPUT(label='Energy to load from grid', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_pv_to_grid: Final[Array] = OUTPUT(label='Energy to grid from PV', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_batt_to_grid: Final[Array] = OUTPUT(label='Energy to grid from battery', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_pv_to_batt: Final[Array] = OUTPUT(label='Energy to battery from PV', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_grid_to_batt: Final[Array] = OUTPUT(label='Energy to battery from grid', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    batt_annual_charge_from_pv: Final[Array] = OUTPUT(label='Battery annual energy charged from PV', units='kWh', type='ARRAY', group='Battery')
    batt_annual_charge_from_grid: Final[Array] = OUTPUT(label='Battery annual energy charged from grid', units='kWh', type='ARRAY', group='Battery')
    batt_annual_charge_energy: Final[Array] = OUTPUT(label='Battery annual energy charged', units='kWh', type='ARRAY', group='Battery')
    batt_annual_discharge_energy: Final[Array] = OUTPUT(label='Battery annual energy discharged', units='kWh', type='ARRAY', group='Battery')
    batt_annual_energy_loss: Final[Array] = OUTPUT(label='Battery annual energy loss', units='kWh', type='ARRAY', group='Battery')
    batt_annual_energy_system_loss: Final[Array] = OUTPUT(label='Battery annual system energy loss', units='kWh', type='ARRAY', group='Battery')
    annual_export_to_grid_energy: Final[Array] = OUTPUT(label='Annual energy exported to grid', units='kWh', type='ARRAY', group='Battery')
    annual_import_to_grid_energy: Final[Array] = OUTPUT(label='Annual energy imported from grid', units='kWh', type='ARRAY', group='Battery')
    average_battery_conversion_efficiency: Final[float] = OUTPUT(label='Battery average cycle conversion efficiency', units='%', type='NUMBER', group='Annual')
    average_battery_roundtrip_efficiency: Final[float] = OUTPUT(label='Battery average roundtrip efficiency', units='%', type='NUMBER', group='Annual')
    batt_pv_charge_percent: Final[float] = OUTPUT(label='Battery percent energy charged from PV', units='%', type='NUMBER', group='Annual')
    batt_bank_installed_capacity: Final[float] = OUTPUT(label='Battery bank installed capacity', units='kWh', type='NUMBER', group='Annual')
    batt_dispatch_sched: Final[Matrix] = OUTPUT(label='Battery dispatch schedule', type='MATRIX', group='Battery')
    gen: Final[Array] = OUTPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 batt_simple_enable: float = ...,
                 batt_simple_kwh: float = ...,
                 batt_simple_kw: float = ...,
                 batt_simple_chemistry: float = ...,
                 batt_simple_dispatch: float = ...,
                 batt_simple_meter_position: float = ...,
                 dc: Array = ...,
                 ac: Array = ...,
                 load: Array = ...,
                 inverter_model: float = ...,
                 inverter_efficiency: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
