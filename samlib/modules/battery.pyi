
# This is a generated file

"""battery - Battery storage standalone model ."""

# VERSION: 10

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'en_batt': float,
        'system_use_lifetime_output': float,
        'analysis_period': float,
        'gen': Array,
        'load': Array,
        'batt_replacement_option': float,
        'capacity_factor': float,
        'annual_energy': float,
        'batt_chem': float,
        'inverter_model': float,
        'inverter_count': float,
        'inv_snl_eff_cec': float,
        'inv_snl_paco': float,
        'inv_ds_eff': float,
        'inv_ds_paco': float,
        'inv_pd_eff': float,
        'inv_pd_paco': float,
        'inv_cec_cg_eff_cec': float,
        'inv_cec_cg_paco': float,
        'batt_ac_or_dc': float,
        'batt_dc_dc_efficiency': float,
        'dcoptimizer_loss': float,
        'batt_dc_ac_efficiency': float,
        'batt_ac_dc_efficiency': float,
        'batt_meter_position': float,
        'batt_losses': Array,
        'batt_losses_charging': Array,
        'batt_losses_discharging': Array,
        'batt_losses_idle': Array,
        'batt_loss_choice': float,
        'batt_current_choice': float,
        'batt_computed_strings': float,
        'batt_computed_series': float,
        'batt_computed_bank_capacity': float,
        'batt_current_charge_max': float,
        'batt_current_discharge_max': float,
        'batt_power_charge_max': float,
        'batt_power_discharge_max': float,
        'batt_voltage_choice': float,
        'batt_Vfull': float,
        'batt_Vexp': float,
        'batt_Vnom': float,
        'batt_Vnom_default': float,
        'batt_Qfull': float,
        'batt_Qfull_flow': float,
        'batt_Qexp': float,
        'batt_Qnom': float,
        'batt_C_rate': float,
        'batt_resistance': float,
        'batt_voltage_matrix': Matrix,
        'LeadAcid_q20_computed': float,
        'LeadAcid_q10_computed': float,
        'LeadAcid_qn_computed': float,
        'LeadAcid_tn': float,
        'batt_initial_SOC': float,
        'batt_minimum_SOC': float,
        'batt_maximum_SOC': float,
        'batt_minimum_modetime': float,
        'batt_lifetime_matrix': Matrix,
        'batt_calendar_choice': float,
        'batt_calendar_lifetime_matrix': Matrix,
        'batt_calendar_q0': float,
        'batt_calendar_a': float,
        'batt_calendar_b': float,
        'batt_calendar_c': float,
        'batt_replacement_capacity': float,
        'batt_replacement_schedule': Array,
        'batt_replacement_cost': float,
        'batt_mass': float,
        'batt_length': float,
        'batt_width': float,
        'batt_height': float,
        'batt_Cp': float,
        'batt_h_to_ambient': float,
        'T_room': float,
        'cap_vs_temp': Matrix,
        'dispatch_manual_charge': Array,
        'dispatch_manual_discharge': Array,
        'dispatch_manual_gridcharge': Array,
        'dispatch_manual_percent_discharge': Array,
        'dispatch_manual_percent_gridcharge': Array,
        'dispatch_manual_sched': Matrix,
        'dispatch_manual_sched_weekend': Matrix,
        'batt_target_power': Array,
        'batt_target_power_monthly': Array,
        'batt_target_choice': float,
        'batt_custom_dispatch': Array,
        'batt_dispatch_choice': float,
        'batt_pv_clipping_forecast': Array,
        'batt_pv_dc_forecast': Array,
        'batt_dispatch_auto_can_gridcharge': float,
        'batt_dispatch_auto_can_charge': float,
        'batt_dispatch_auto_can_clipcharge': float,
        'batt_auto_gridcharge_max_daily': float,
        'batt_look_ahead_hours': float,
        'batt_dispatch_update_frequency_hours': float,
        'batt_cycle_cost_choice': float,
        'batt_cycle_cost': float,
        'en_electricity_rates': float,
        'ur_ec_sched_weekday': Matrix,
        'ur_ec_sched_weekend': Matrix,
        'ur_ec_tou_mat': Matrix,
        'ppa_price_input': float,
        'ppa_multiplier_model': float,
        'dispatch_factors_ts': Array,
        'dispatch_tod_factors': Array,
        'dispatch_sched_weekday': Matrix,
        'dispatch_sched_weekend': Matrix,
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
        'batt_dispatch_sched': Matrix
}, total=False)

class Data(ssc.DataDict):
    en_batt: float = INPUT(label='Enable battery storage model', units='0/1', type='NUMBER', group='Battery', required='?=0')
    system_use_lifetime_output: float = INPUT(label='PV lifetime simulation', units='0/1', type='NUMBER', required='?=0', constraints='BOOLEAN', meta='0=SingleYearRepeated,1=RunEveryYear')
    analysis_period: float = INPUT(label='Lifetime analysis period', units='years', type='NUMBER', required='system_use_lifetime_output=1', meta='The number of years in the simulation')
    gen: Array = INPUT(label='System power generated (lifetime)', units='kW', type='ARRAY')
    load: Array = INPUT(label='Electricity load (year 1)', units='kW', type='ARRAY')
    batt_replacement_option: float = INPUT(label='Enable battery replacement?', units='0=none,1=capacity based,2=user schedule', type='NUMBER', group='Battery', required='?=0', constraints='INTEGER,MIN=0,MAX=2')
    capacity_factor: float = INOUT(label='Capacity factor', units='%', type='NUMBER', required='?=0')
    annual_energy: float = INOUT(label='Annual Energy', units='kWh', type='NUMBER', group='Battery', required='?=0')
    batt_chem: float = INPUT(label='Battery chemistry', type='NUMBER', group='Battery', meta='0=LeadAcid,1=LiIon')
    inverter_model: float = INPUT(label='Inverter model specifier', type='NUMBER', constraints='INTEGER,MIN=0,MAX=4', meta='0=cec,1=datasheet,2=partload,3=coefficientgenerator,4=generic')
    inverter_count: float = INPUT(label='Number of inverters', type='NUMBER', group='pvsamv1')
    inv_snl_eff_cec: float = INPUT(label='Inverter Sandia CEC Efficiency', units='%', type='NUMBER', group='pvsamv1')
    inv_snl_paco: float = INPUT(label='Inverter Sandia Maximum AC Power', units='Wac', type='NUMBER', group='pvsamv1')
    inv_ds_eff: float = INPUT(label='Inverter Datasheet Efficiency', units='%', type='NUMBER', group='pvsamv1')
    inv_ds_paco: float = INPUT(label='Inverter Datasheet Maximum AC Power', units='Wac', type='NUMBER', group='pvsamv1')
    inv_pd_eff: float = INPUT(label='Inverter Partload Efficiency', units='%', type='NUMBER', group='pvsamv1')
    inv_pd_paco: float = INPUT(label='Inverter Partload Maximum AC Power', units='Wac', type='NUMBER', group='pvsamv1')
    inv_cec_cg_eff_cec: float = INPUT(label='Inverter Coefficient Generator CEC Efficiency', units='%', type='NUMBER', group='pvsamv1')
    inv_cec_cg_paco: float = INPUT(label='Inverter Coefficient Generator Max AC Power', units='Wac', type='NUMBER', group='pvsamv1')
    batt_ac_or_dc: float = INPUT(label='Battery interconnection (AC or DC)', type='NUMBER', group='Battery', meta='0=DC_Connected,1=AC_Connected')
    batt_dc_dc_efficiency: float = INPUT(label='PV DC to battery DC efficiency', type='NUMBER', group='Battery')
    dcoptimizer_loss: float = INPUT(label='PV loss in DC/DC w/MPPT conversion', type='NUMBER', group='pvsamv1')
    batt_dc_ac_efficiency: float = INPUT(label='Battery DC to AC efficiency', type='NUMBER', group='Battery')
    batt_ac_dc_efficiency: float = INPUT(label='Inverter AC to battery DC efficiency', type='NUMBER', group='Battery')
    batt_meter_position: float = INPUT(label='Position of battery relative to electric meter', type='NUMBER', group='Battery', meta='0=BehindTheMeter,1=FrontOfMeter')
    batt_losses: Array = INPUT(label='Battery system losses at each timestep', units='kW', type='ARRAY', group='Battery', required='?=0')
    batt_losses_charging: Array = INPUT(label='Battery system losses when charging', units='kW', type='ARRAY', group='Battery', required='?=0')
    batt_losses_discharging: Array = INPUT(label='Battery system losses when discharging', units='kW', type='ARRAY', group='Battery', required='?=0')
    batt_losses_idle: Array = INPUT(label='Battery system losses when idle', units='kW', type='ARRAY', group='Battery', required='?=0')
    batt_loss_choice: float = INPUT(label='Loss power input option', units='0/1', type='NUMBER', group='Battery', required='?=0', meta='0=Monthly,1=TimeSeries')
    batt_current_choice: float = INPUT(label='Limit cells by current or power', type='NUMBER', group='Battery')
    batt_computed_strings: float = INPUT(label='Number of strings of cells', type='NUMBER', group='Battery')
    batt_computed_series: float = INPUT(label='Number of cells in series', type='NUMBER', group='Battery')
    batt_computed_bank_capacity: float = INPUT(label='Computed bank capacity', units='kWh', type='NUMBER', group='Battery')
    batt_current_charge_max: float = INPUT(label='Maximum charge current', units='A', type='NUMBER', group='Battery')
    batt_current_discharge_max: float = INPUT(label='Maximum discharge current', units='A', type='NUMBER', group='Battery')
    batt_power_charge_max: float = INPUT(label='Maximum charge power', units='kW', type='NUMBER', group='Battery')
    batt_power_discharge_max: float = INPUT(label='Maximum discharge power', units='kW', type='NUMBER', group='Battery')
    batt_voltage_choice: float = INPUT(label='Battery voltage input option', units='0/1', type='NUMBER', group='Battery', required='?=0', meta='0=UseVoltageModel,1=InputVoltageTable')
    batt_Vfull: float = INPUT(label='Fully charged cell voltage', units='V', type='NUMBER', group='Battery')
    batt_Vexp: float = INPUT(label='Cell voltage at end of exponential zone', units='V', type='NUMBER', group='Battery')
    batt_Vnom: float = INPUT(label='Cell voltage at end of nominal zone', units='V', type='NUMBER', group='Battery')
    batt_Vnom_default: float = INPUT(label='Default nominal cell voltage', units='V', type='NUMBER', group='Battery')
    batt_Qfull: float = INPUT(label='Fully charged cell capacity', units='Ah', type='NUMBER', group='Battery')
    batt_Qfull_flow: float = INPUT(label='Fully charged flow battery capacity', units='Ah', type='NUMBER', group='Battery')
    batt_Qexp: float = INPUT(label='Cell capacity at end of exponential zone', units='Ah', type='NUMBER', group='Battery')
    batt_Qnom: float = INPUT(label='Cell capacity at end of nominal zone', units='Ah', type='NUMBER', group='Battery')
    batt_C_rate: float = INPUT(label='Rate at which voltage vs. capacity curve input', type='NUMBER', group='Battery')
    batt_resistance: float = INPUT(label='Internal resistance', units='Ohm', type='NUMBER', group='Battery')
    batt_voltage_matrix: Matrix = INPUT(label='Battery voltage vs. depth-of-discharge', type='MATRIX', group='Battery')
    LeadAcid_q20_computed: float = INPUT(label='Capacity at 20-hour discharge rate', units='Ah', type='NUMBER', group='Battery')
    LeadAcid_q10_computed: float = INPUT(label='Capacity at 10-hour discharge rate', units='Ah', type='NUMBER', group='Battery')
    LeadAcid_qn_computed: float = INPUT(label='Capacity at discharge rate for n-hour rate', units='Ah', type='NUMBER', group='Battery')
    LeadAcid_tn: float = INPUT(label='Time to discharge', units='h', type='NUMBER', group='Battery')
    batt_initial_SOC: float = INPUT(label='Initial state-of-charge', units='%', type='NUMBER', group='Battery')
    batt_minimum_SOC: float = INPUT(label='Minimum allowed state-of-charge', units='%', type='NUMBER', group='Battery')
    batt_maximum_SOC: float = INPUT(label='Maximum allowed state-of-charge', units='%', type='NUMBER', group='Battery')
    batt_minimum_modetime: float = INPUT(label='Minimum time at charge state', units='min', type='NUMBER', group='Battery')
    batt_lifetime_matrix: Matrix = INPUT(label='Cycles vs capacity at different depths-of-discharge', type='MATRIX', group='Battery')
    batt_calendar_choice: float = INPUT(label='Calendar life degradation input option', units='0/1/2', type='NUMBER', group='Battery', meta='0=NoCalendarDegradation,1=LithiomIonModel,2=InputLossTable')
    batt_calendar_lifetime_matrix: Matrix = INPUT(label='Days vs capacity', type='MATRIX', group='Battery')
    batt_calendar_q0: float = INPUT(label='Calendar life model initial capacity cofficient', type='NUMBER', group='Battery')
    batt_calendar_a: float = INPUT(label='Calendar life model coefficient', units='1/sqrt(day)', type='NUMBER', group='Battery')
    batt_calendar_b: float = INPUT(label='Calendar life model coefficient', units='K', type='NUMBER', group='Battery')
    batt_calendar_c: float = INPUT(label='Calendar life model coefficient', units='K', type='NUMBER', group='Battery')
    batt_replacement_capacity: float = INPUT(label='Capacity degradation at which to replace battery', units='%', type='NUMBER', group='Battery')
    batt_replacement_schedule: Array = INPUT(label='Battery bank replacements per year (user specified)', units='number/year', type='ARRAY', group='Battery', required='batt_replacement_option=2')
    batt_replacement_cost: float = INPUT(label='Cost to replace battery per kWh', units='$/kWh', type='NUMBER', group='Battery')
    batt_mass: float = INPUT(label='Battery mass', units='kg', type='NUMBER', group='Battery')
    batt_length: float = INPUT(label='Battery length', units='m', type='NUMBER', group='Battery')
    batt_width: float = INPUT(label='Battery width', units='m', type='NUMBER', group='Battery')
    batt_height: float = INPUT(label='Battery height', units='m', type='NUMBER', group='Battery')
    batt_Cp: float = INPUT(label='Battery specific heat capacity', units='J/KgK', type='NUMBER', group='Battery')
    batt_h_to_ambient: float = INPUT(label='Heat transfer between battery and environment', units='W/m2K', type='NUMBER', group='Battery')
    T_room: float = INPUT(label='Temperature of storage room', units='C', type='NUMBER', group='Battery')
    cap_vs_temp: Matrix = INPUT(label='Effective capacity as function of temperature', units='C,%', type='MATRIX', group='Battery')
    dispatch_manual_charge: Array = INPUT(label='Periods 1-6 charging allowed?', type='ARRAY', group='Battery', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_discharge: Array = INPUT(label='Periods 1-6 discharging allowed?', type='ARRAY', group='Battery', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_gridcharge: Array = INPUT(label='Periods 1-6 grid charging allowed?', type='ARRAY', group='Battery', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_percent_discharge: Array = INPUT(label='Periods 1-6 discharge percent', units='%', type='ARRAY', group='Battery', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_percent_gridcharge: Array = INPUT(label='Periods 1-6 gridcharge percent', units='%', type='ARRAY', group='Battery', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_sched: Matrix = INPUT(label='Battery dispatch schedule for weekday', type='MATRIX', group='Battery', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_sched_weekend: Matrix = INPUT(label='Battery dispatch schedule for weekend', type='MATRIX', group='Battery', required='en_batt=1&batt_dispatch_choice=4')
    batt_target_power: Array = INPUT(label='Grid target power (AC) for every time step', units='kWac', type='ARRAY', group='Battery', required='en_batt=1&batt_meter_position=0&batt_dispatch_choice=2')
    batt_target_power_monthly: Array = INPUT(label='Grid target power (AC) on monthly basis', units='kWac', type='ARRAY', group='Battery', required='en_batt=1&batt_meter_position=0&batt_dispatch_choice=2')
    batt_target_choice: float = INPUT(label='Target power input option', units='0/1', type='NUMBER', group='Battery', required='en_batt=1&batt_meter_position=0&batt_dispatch_choice=2', meta='0=InputMonthlyTarget,1=InputFullTimeSeries')
    batt_custom_dispatch: Array = INPUT(label='Custom battery power (DC) for every time step', units='kWdc', type='ARRAY', group='Battery', required='en_batt=1&batt_dispatch_choice=3')
    batt_dispatch_choice: float = INPUT(label='Battery dispatch algorithm', units='0/1/2/3/4', type='NUMBER', group='Battery', required='en_batt=1', meta='If behind the meter: 0=PeakShavingLookAhead,1=PeakShavingLookBehind,2=InputGridTarget,3=InputBatteryPower,4=ManualDispatch, if front of meter: 0=AutomatedLookAhead,1=AutomatedLookBehind,2=AutomatedInputForecast,3=InputBatteryPower,4=ManualDispatch')
    batt_pv_clipping_forecast: Array = INPUT(label='PV clipping forecast', units='kW', type='ARRAY', group='Battery', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2')
    batt_pv_dc_forecast: Array = INPUT(label='PV dc power forecast', units='kW', type='ARRAY', group='Battery', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2')
    batt_dispatch_auto_can_gridcharge: float = INPUT(label='Grid charging allowed for automated dispatch?', units='kW', type='NUMBER', group='Battery')
    batt_dispatch_auto_can_charge: float = INPUT(label='PV charging allowed for automated dispatch?', units='kW', type='NUMBER', group='Battery')
    batt_dispatch_auto_can_clipcharge: float = INPUT(label='Battery can charge from clipped PV for automated dispatch?', units='kW', type='NUMBER', group='Battery')
    batt_auto_gridcharge_max_daily: float = INPUT(label='Allowed grid charging percent per day for automated dispatch', units='kW', type='NUMBER', group='Battery')
    batt_look_ahead_hours: float = INPUT(label='Hours to look ahead in automated dispatch', units='hours', type='NUMBER', group='Battery')
    batt_dispatch_update_frequency_hours: float = INPUT(label='Frequency to update the look-ahead dispatch', units='hours', type='NUMBER', group='Battery')
    batt_cycle_cost_choice: float = INPUT(label='Use SAM model for cycle costs or input custom', units='0/1', type='NUMBER', group='Battery', meta='0=UseCostModel,1=InputCost')
    batt_cycle_cost: float = INPUT(label='Input battery cycle costs', units='$/cycle-kWh', type='NUMBER', group='Battery')
    en_electricity_rates: float = INPUT(label='Enable Electricity Rates', type='NUMBER', group='0=EnableElectricityRates,1=NoRates', meta='0/1')
    ur_ec_sched_weekday: Matrix = INPUT(label='Energy charge weekday schedule', type='MATRIX', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2', meta='12 x 24 matrix')
    ur_ec_sched_weekend: Matrix = INPUT(label='Energy charge weekend schedule', type='MATRIX', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2', meta='12 x 24 matrix')
    ur_ec_tou_mat: Matrix = INPUT(label='Energy rates table', type='MATRIX', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2')
    ppa_price_input: float = INPUT(label='PPA Price Input', type='NUMBER', group='Time of Delivery', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2')
    ppa_multiplier_model: float = INPUT(label='PPA multiplier model', units='0/1', type='NUMBER', group='Time of Delivery', required='?=0', constraints='INTEGER,MIN=0', meta='0=diurnal,1=timestep')
    dispatch_factors_ts: Array = INPUT(label='Dispatch payment factor time step', type='ARRAY', group='Time of Delivery', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2&ppa_multiplier_model=1')
    dispatch_tod_factors: Array = INPUT(label='TOD factors for periods 1-9', type='ARRAY', group='Time of Delivery', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2&ppa_multiplier_model=0')
    dispatch_sched_weekday: Matrix = INPUT(label='Diurnal weekday TOD periods', units='1..9', type='MATRIX', group='Time of Delivery', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2&ppa_multiplier_model=0', meta='12 x 24 matrix')
    dispatch_sched_weekend: Matrix = INPUT(label='Diurnal weekend TOD periods', units='1..9', type='MATRIX', group='Time of Delivery', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2&ppa_multiplier_model=0', meta='12 x 24 matrix')
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

    def __init__(self, *args: Mapping[str, Any],
                 en_batt: float = ...,
                 system_use_lifetime_output: float = ...,
                 analysis_period: float = ...,
                 gen: Array = ...,
                 load: Array = ...,
                 batt_replacement_option: float = ...,
                 capacity_factor: float = ...,
                 annual_energy: float = ...,
                 batt_chem: float = ...,
                 inverter_model: float = ...,
                 inverter_count: float = ...,
                 inv_snl_eff_cec: float = ...,
                 inv_snl_paco: float = ...,
                 inv_ds_eff: float = ...,
                 inv_ds_paco: float = ...,
                 inv_pd_eff: float = ...,
                 inv_pd_paco: float = ...,
                 inv_cec_cg_eff_cec: float = ...,
                 inv_cec_cg_paco: float = ...,
                 batt_ac_or_dc: float = ...,
                 batt_dc_dc_efficiency: float = ...,
                 dcoptimizer_loss: float = ...,
                 batt_dc_ac_efficiency: float = ...,
                 batt_ac_dc_efficiency: float = ...,
                 batt_meter_position: float = ...,
                 batt_losses: Array = ...,
                 batt_losses_charging: Array = ...,
                 batt_losses_discharging: Array = ...,
                 batt_losses_idle: Array = ...,
                 batt_loss_choice: float = ...,
                 batt_current_choice: float = ...,
                 batt_computed_strings: float = ...,
                 batt_computed_series: float = ...,
                 batt_computed_bank_capacity: float = ...,
                 batt_current_charge_max: float = ...,
                 batt_current_discharge_max: float = ...,
                 batt_power_charge_max: float = ...,
                 batt_power_discharge_max: float = ...,
                 batt_voltage_choice: float = ...,
                 batt_Vfull: float = ...,
                 batt_Vexp: float = ...,
                 batt_Vnom: float = ...,
                 batt_Vnom_default: float = ...,
                 batt_Qfull: float = ...,
                 batt_Qfull_flow: float = ...,
                 batt_Qexp: float = ...,
                 batt_Qnom: float = ...,
                 batt_C_rate: float = ...,
                 batt_resistance: float = ...,
                 batt_voltage_matrix: Matrix = ...,
                 LeadAcid_q20_computed: float = ...,
                 LeadAcid_q10_computed: float = ...,
                 LeadAcid_qn_computed: float = ...,
                 LeadAcid_tn: float = ...,
                 batt_initial_SOC: float = ...,
                 batt_minimum_SOC: float = ...,
                 batt_maximum_SOC: float = ...,
                 batt_minimum_modetime: float = ...,
                 batt_lifetime_matrix: Matrix = ...,
                 batt_calendar_choice: float = ...,
                 batt_calendar_lifetime_matrix: Matrix = ...,
                 batt_calendar_q0: float = ...,
                 batt_calendar_a: float = ...,
                 batt_calendar_b: float = ...,
                 batt_calendar_c: float = ...,
                 batt_replacement_capacity: float = ...,
                 batt_replacement_schedule: Array = ...,
                 batt_replacement_cost: float = ...,
                 batt_mass: float = ...,
                 batt_length: float = ...,
                 batt_width: float = ...,
                 batt_height: float = ...,
                 batt_Cp: float = ...,
                 batt_h_to_ambient: float = ...,
                 T_room: float = ...,
                 cap_vs_temp: Matrix = ...,
                 dispatch_manual_charge: Array = ...,
                 dispatch_manual_discharge: Array = ...,
                 dispatch_manual_gridcharge: Array = ...,
                 dispatch_manual_percent_discharge: Array = ...,
                 dispatch_manual_percent_gridcharge: Array = ...,
                 dispatch_manual_sched: Matrix = ...,
                 dispatch_manual_sched_weekend: Matrix = ...,
                 batt_target_power: Array = ...,
                 batt_target_power_monthly: Array = ...,
                 batt_target_choice: float = ...,
                 batt_custom_dispatch: Array = ...,
                 batt_dispatch_choice: float = ...,
                 batt_pv_clipping_forecast: Array = ...,
                 batt_pv_dc_forecast: Array = ...,
                 batt_dispatch_auto_can_gridcharge: float = ...,
                 batt_dispatch_auto_can_charge: float = ...,
                 batt_dispatch_auto_can_clipcharge: float = ...,
                 batt_auto_gridcharge_max_daily: float = ...,
                 batt_look_ahead_hours: float = ...,
                 batt_dispatch_update_frequency_hours: float = ...,
                 batt_cycle_cost_choice: float = ...,
                 batt_cycle_cost: float = ...,
                 en_electricity_rates: float = ...,
                 ur_ec_sched_weekday: Matrix = ...,
                 ur_ec_sched_weekend: Matrix = ...,
                 ur_ec_tou_mat: Matrix = ...,
                 ppa_price_input: float = ...,
                 ppa_multiplier_model: float = ...,
                 dispatch_factors_ts: Array = ...,
                 dispatch_tod_factors: Array = ...,
                 dispatch_sched_weekday: Matrix = ...,
                 dispatch_sched_weekend: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
