
# This is a generated file

"""battery - Battery storage standalone model ."""

# VERSION: 10

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'percent_complete': float,
        'system_use_lifetime_output': float,
        'analysis_period': float,
        'en_batt': float,
        'gen': Array,
        'load': Array,
        'crit_load': Array,
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
        'batt_inverter_efficiency_cutoff': float,
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
        'batt_power_charge_max_kwdc': float,
        'batt_power_discharge_max_kwdc': float,
        'batt_power_charge_max_kwac': float,
        'batt_power_discharge_max_kwac': float,
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
        'batt_replacement_option': float,
        'batt_replacement_schedule': Array,
        'batt_replacement_schedule_percent': Array,
        'om_replacement_cost1': Array,
        'batt_mass': float,
        'batt_surface_area': float,
        'batt_Cp': float,
        'batt_h_to_ambient': float,
        'batt_room_temperature_celsius': Array,
        'cap_vs_temp': Matrix,
        'dispatch_manual_charge': Array,
        'dispatch_manual_fuelcellcharge': Array,
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
        'batt_dispatch_auto_can_fuelcellcharge': float,
        'batt_dispatch_auto_can_gridcharge': float,
        'batt_dispatch_auto_can_charge': float,
        'batt_dispatch_auto_can_clipcharge': float,
        'batt_auto_gridcharge_max_daily': float,
        'batt_look_ahead_hours': float,
        'batt_dispatch_update_frequency_hours': float,
        'batt_cycle_cost_choice': float,
        'batt_cycle_cost': float,
        'en_electricity_rates': float,
        'ur_en_ts_sell_rate': float,
        'ur_ts_buy_rate': Array,
        'ur_ec_sched_weekday': Matrix,
        'ur_ec_sched_weekend': Matrix,
        'ur_ec_tou_mat': Matrix,
        'fuelcell_power': Array,
        'forecast_price_signal_model': float,
        'ppa_price_input': Array,
        'ppa_multiplier_model': float,
        'dispatch_factors_ts': Array,
        'dispatch_tod_factors': Array,
        'dispatch_sched_weekday': Matrix,
        'dispatch_sched_weekend': Matrix,
        'mp_enable_energy_market_revenue': float,
        'mp_energy_market_revenue': Matrix,
        'mp_enable_ancserv1': float,
        'mp_ancserv1_revenue': Matrix,
        'mp_enable_ancserv2': float,
        'mp_ancserv2_revenue': Matrix,
        'mp_enable_ancserv3': float,
        'mp_ancserv3_revenue': Matrix,
        'mp_enable_ancserv4': float,
        'mp_ancserv4_revenue': Matrix,
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
        'batt_capacity_percent_cycle': Array,
        'batt_capacity_percent_calendar': Array,
        'batt_capacity_thermal_percent': Array,
        'batt_bank_replacement': Array,
        'batt_power': Array,
        'grid_power': Array,
        'pv_to_load': Array,
        'batt_to_load': Array,
        'grid_to_load': Array,
        'pv_to_batt': Array,
        'fuelcell_to_batt': Array,
        'grid_to_batt': Array,
        'pv_to_grid': Array,
        'batt_to_grid': Array,
        'batt_conversion_loss': Array,
        'batt_system_loss': Array,
        'grid_power_target': Array,
        'batt_power_target': Array,
        'batt_cost_to_cycle': Array,
        'market_sell_rate_series_yr1': Array,
        'batt_revenue_gridcharge': Array,
        'batt_revenue_charge': Array,
        'batt_revenue_clipcharge': Array,
        'batt_revenue_discharge': Array,
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
        'resilience_hrs': Array,
        'resilience_hrs_min': float,
        'resilience_hrs_max': float,
        'resilience_hrs_avg': float,
        'outage_durations': Array,
        'pdf_of_surviving': Array,
        'cdf_of_surviving': Array,
        'survival_function': Array,
        'avg_critical_load': float
}, total=False)

class Data(ssc.DataDict):
    percent_complete: float = INOUT(label='Estimated simulation status', units='%', type='NUMBER', group='Simulation')
    system_use_lifetime_output: float = INPUT(label='Lifetime simulation', units='0/1', type='NUMBER', group='Lifetime', required='?=0', constraints='BOOLEAN', meta='0=SingleYearRepeated,1=RunEveryYear')
    analysis_period: float = INPUT(label='Lifetime analysis period', units='years', type='NUMBER', group='Lifetime', required='system_use_lifetime_output=1', meta='The number of years in the simulation')
    en_batt: float = INPUT(label='Enable battery storage model', units='0/1', type='NUMBER', group='BatterySystem', required='?=0')
    gen: Array = INOUT(label='System power generated', units='kW', type='ARRAY', group='System Output')
    load: Array = INPUT(label='Electricity load (year 1)', units='kW', type='ARRAY', group='Load')
    crit_load: Array = INPUT(label='Critical electricity load (year 1)', units='kW', type='ARRAY', group='Load')
    capacity_factor: float = INOUT(label='Capacity factor', units='%', type='NUMBER', group='System Output', required='?=0')
    annual_energy: float = INOUT(label='Annual Energy', units='kWh', type='NUMBER', group='System Output', required='?=0')
    batt_chem: float = INPUT(label='Battery chemistry', type='NUMBER', group='BatteryCell', meta='0=LeadAcid,1=LiIon')
    inverter_model: float = INPUT(label='Inverter model specifier', type='NUMBER', group='Inverter', required='?=4', constraints='INTEGER,MIN=0,MAX=4', meta='0=cec,1=datasheet,2=partload,3=coefficientgenerator,4=generic')
    inverter_count: float = INPUT(label='Number of inverters', type='NUMBER', group='Inverter')
    inv_snl_eff_cec: float = INPUT(label='Inverter Sandia CEC Efficiency', units='%', type='NUMBER', group='Inverter')
    inv_snl_paco: float = INPUT(label='Inverter Sandia Maximum AC Power', units='Wac', type='NUMBER', group='Inverter')
    inv_ds_eff: float = INPUT(label='Inverter Datasheet Efficiency', units='%', type='NUMBER', group='Inverter')
    inv_ds_paco: float = INPUT(label='Inverter Datasheet Maximum AC Power', units='Wac', type='NUMBER', group='Inverter')
    inv_pd_eff: float = INPUT(label='Inverter Partload Efficiency', units='%', type='NUMBER', group='Inverter')
    inv_pd_paco: float = INPUT(label='Inverter Partload Maximum AC Power', units='Wac', type='NUMBER', group='Inverter')
    inv_cec_cg_eff_cec: float = INPUT(label='Inverter Coefficient Generator CEC Efficiency', units='%', type='NUMBER', group='Inverter')
    inv_cec_cg_paco: float = INPUT(label='Inverter Coefficient Generator Max AC Power', units='Wac', type='NUMBER', group='Inverter')
    batt_ac_or_dc: float = INPUT(label='Battery interconnection (AC or DC)', type='NUMBER', group='BatterySystem', meta='0=DC_Connected,1=AC_Connected')
    batt_dc_dc_efficiency: float = INPUT(label='System DC to battery DC efficiency', type='NUMBER', group='BatterySystem')
    dcoptimizer_loss: float = INPUT(label='DC optimizer loss', type='NUMBER', group='Losses')
    batt_dc_ac_efficiency: float = INPUT(label='Battery DC to AC efficiency', type='NUMBER', group='BatterySystem')
    batt_ac_dc_efficiency: float = INPUT(label='Inverter AC to battery DC efficiency', type='NUMBER', group='BatterySystem')
    batt_meter_position: float = INPUT(label='Position of battery relative to electric meter', type='NUMBER', group='BatterySystem', meta='0=BehindTheMeter,1=FrontOfMeter')
    batt_inverter_efficiency_cutoff: float = INPUT(label='Inverter efficiency at which to cut battery charge or discharge off', units='%', type='NUMBER', group='BatterySystem')
    batt_losses: Array = INPUT(label='Battery system losses at each timestep', units='kW', type='ARRAY', group='BatterySystem', required='?=0')
    batt_losses_charging: Array = INPUT(label='Battery system losses when charging', units='kW', type='ARRAY', group='BatterySystem', required='?=0')
    batt_losses_discharging: Array = INPUT(label='Battery system losses when discharging', units='kW', type='ARRAY', group='BatterySystem', required='?=0')
    batt_losses_idle: Array = INPUT(label='Battery system losses when idle', units='kW', type='ARRAY', group='BatterySystem', required='?=0')
    batt_loss_choice: float = INPUT(label='Loss power input option', units='0/1', type='NUMBER', group='BatterySystem', required='?=0', meta='0=Monthly,1=TimeSeries')
    batt_current_choice: float = INPUT(label='Limit cells by current or power', type='NUMBER', group='BatterySystem')
    batt_computed_strings: float = INPUT(label='Number of strings of cells', type='NUMBER', group='BatterySystem')
    batt_computed_series: float = INPUT(label='Number of cells in series', type='NUMBER', group='BatterySystem')
    batt_computed_bank_capacity: float = INPUT(label='Computed bank capacity', units='kWh', type='NUMBER', group='BatterySystem')
    batt_current_charge_max: float = INPUT(label='Maximum charge current', units='A', type='NUMBER', group='BatterySystem')
    batt_current_discharge_max: float = INPUT(label='Maximum discharge current', units='A', type='NUMBER', group='BatterySystem')
    batt_power_charge_max_kwdc: float = INPUT(label='Maximum charge power (DC)', units='kWdc', type='NUMBER', group='BatterySystem')
    batt_power_discharge_max_kwdc: float = INPUT(label='Maximum discharge power (DC)', units='kWdc', type='NUMBER', group='BatterySystem')
    batt_power_charge_max_kwac: float = INPUT(label='Maximum charge power (AC)', units='kWac', type='NUMBER', group='BatterySystem')
    batt_power_discharge_max_kwac: float = INPUT(label='Maximum discharge power (AC)', units='kWac', type='NUMBER', group='BatterySystem')
    batt_voltage_choice: float = INPUT(label='Battery voltage input option', units='0/1', type='NUMBER', group='BatteryCell', required='?=0', meta='0=UseVoltageModel,1=InputVoltageTable')
    batt_Vfull: float = INPUT(label='Fully charged cell voltage', units='V', type='NUMBER', group='BatteryCell')
    batt_Vexp: float = INPUT(label='Cell voltage at end of exponential zone', units='V', type='NUMBER', group='BatteryCell')
    batt_Vnom: float = INPUT(label='Cell voltage at end of nominal zone', units='V', type='NUMBER', group='BatteryCell')
    batt_Vnom_default: float = INPUT(label='Default nominal cell voltage', units='V', type='NUMBER', group='BatteryCell')
    batt_Qfull: float = INPUT(label='Fully charged cell capacity', units='Ah', type='NUMBER', group='BatteryCell')
    batt_Qfull_flow: float = INPUT(label='Fully charged flow battery capacity', units='Ah', type='NUMBER', group='BatteryCell')
    batt_Qexp: float = INPUT(label='Cell capacity at end of exponential zone', units='Ah', type='NUMBER', group='BatteryCell')
    batt_Qnom: float = INPUT(label='Cell capacity at end of nominal zone', units='Ah', type='NUMBER', group='BatteryCell')
    batt_C_rate: float = INPUT(label='Rate at which voltage vs. capacity curve input', type='NUMBER', group='BatteryCell')
    batt_resistance: float = INPUT(label='Internal resistance', units='Ohm', type='NUMBER', group='BatteryCell')
    batt_voltage_matrix: Matrix = INPUT(label='Battery voltage vs. depth-of-discharge', type='MATRIX', group='BatteryCell')
    LeadAcid_q20_computed: float = INPUT(label='Capacity at 20-hour discharge rate', units='Ah', type='NUMBER', group='BatteryCell')
    LeadAcid_q10_computed: float = INPUT(label='Capacity at 10-hour discharge rate', units='Ah', type='NUMBER', group='BatteryCell')
    LeadAcid_qn_computed: float = INPUT(label='Capacity at discharge rate for n-hour rate', units='Ah', type='NUMBER', group='BatteryCell')
    LeadAcid_tn: float = INPUT(label='Time to discharge', units='h', type='NUMBER', group='BatteryCell')
    batt_initial_SOC: float = INPUT(label='Initial state-of-charge', units='%', type='NUMBER', group='BatteryCell')
    batt_minimum_SOC: float = INPUT(label='Minimum allowed state-of-charge', units='%', type='NUMBER', group='BatteryCell')
    batt_maximum_SOC: float = INPUT(label='Maximum allowed state-of-charge', units='%', type='NUMBER', group='BatteryCell')
    batt_minimum_modetime: float = INPUT(label='Minimum time at charge state', units='min', type='NUMBER', group='BatteryCell')
    batt_lifetime_matrix: Matrix = INPUT(label='Cycles vs capacity at different depths-of-discharge', type='MATRIX', group='BatteryCell')
    batt_calendar_choice: float = INPUT(label='Calendar life degradation input option', units='0/1/2', type='NUMBER', group='BatteryCell', meta='0=NoCalendarDegradation,1=LithiomIonModel,2=InputLossTable')
    batt_calendar_lifetime_matrix: Matrix = INPUT(label='Days vs capacity', type='MATRIX', group='BatteryCell')
    batt_calendar_q0: float = INPUT(label='Calendar life model initial capacity cofficient', type='NUMBER', group='BatteryCell')
    batt_calendar_a: float = INPUT(label='Calendar life model coefficient', units='1/sqrt(day)', type='NUMBER', group='BatteryCell')
    batt_calendar_b: float = INPUT(label='Calendar life model coefficient', units='K', type='NUMBER', group='BatteryCell')
    batt_calendar_c: float = INPUT(label='Calendar life model coefficient', units='K', type='NUMBER', group='BatteryCell')
    batt_replacement_capacity: float = INPUT(label='Capacity degradation at which to replace battery', units='%', type='NUMBER', group='BatterySystem')
    batt_replacement_option: float = INPUT(label='Enable battery replacement?', units='0=none,1=capacity based,2=user schedule', type='NUMBER', group='BatterySystem', required='?=0', constraints='INTEGER,MIN=0,MAX=2')
    batt_replacement_schedule: Array = INPUT(label='Battery bank number of replacements in each year', units='number/year', type='ARRAY', group='BatterySystem', required='batt_replacement_option=2', meta='length <= analysis_period')
    batt_replacement_schedule_percent: Array = INPUT(label='Percentage of battery capacity to replace in each year', units='%', type='ARRAY', group='BatterySystem', required='batt_replacement_option=2', meta='length <= analysis_period')
    om_replacement_cost1: Array = INPUT(label='Cost to replace battery per kWh', units='$/kWh', type='ARRAY', group='BatterySystem')
    batt_mass: float = INPUT(label='Battery mass', units='kg', type='NUMBER', group='BatterySystem')
    batt_surface_area: float = INPUT(label='Battery surface area', units='m^2', type='NUMBER', group='BatterySystem')
    batt_Cp: float = INPUT(label='Battery specific heat capacity', units='J/KgK', type='NUMBER', group='BatteryCell')
    batt_h_to_ambient: float = INPUT(label='Heat transfer between battery and environment', units='W/m2K', type='NUMBER', group='BatteryCell')
    batt_room_temperature_celsius: Array = INPUT(label='Temperature of storage room', units='C', type='ARRAY', group='BatteryCell')
    cap_vs_temp: Matrix = INPUT(label='Effective capacity as function of temperature', units='C,%', type='MATRIX', group='BatteryCell')
    dispatch_manual_charge: Array = INPUT(label='Periods 1-6 charging from system allowed?', type='ARRAY', group='BatteryDispatch', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_fuelcellcharge: Array = INPUT(label='Periods 1-6 charging from fuel cell allowed?', type='ARRAY', group='BatteryDispatch')
    dispatch_manual_discharge: Array = INPUT(label='Periods 1-6 discharging allowed?', type='ARRAY', group='BatteryDispatch', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_gridcharge: Array = INPUT(label='Periods 1-6 grid charging allowed?', type='ARRAY', group='BatteryDispatch', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_percent_discharge: Array = INPUT(label='Periods 1-6 discharge percent', units='%', type='ARRAY', group='BatteryDispatch', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_percent_gridcharge: Array = INPUT(label='Periods 1-6 gridcharge percent', units='%', type='ARRAY', group='BatteryDispatch', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_sched: Matrix = INPUT(label='Battery dispatch schedule for weekday', type='MATRIX', group='BatteryDispatch', required='en_batt=1&batt_dispatch_choice=4')
    dispatch_manual_sched_weekend: Matrix = INPUT(label='Battery dispatch schedule for weekend', type='MATRIX', group='BatteryDispatch', required='en_batt=1&batt_dispatch_choice=4')
    batt_target_power: Array = INPUT(label='Grid target power for every time step', units='kW', type='ARRAY', group='BatteryDispatch', required='en_batt=1&batt_meter_position=0&batt_dispatch_choice=2')
    batt_target_power_monthly: Array = INPUT(label='Grid target power on monthly basis', units='kW', type='ARRAY', group='BatteryDispatch', required='en_batt=1&batt_meter_position=0&batt_dispatch_choice=2')
    batt_target_choice: float = INPUT(label='Target power input option', units='0/1', type='NUMBER', group='BatteryDispatch', required='en_batt=1&batt_meter_position=0&batt_dispatch_choice=2', meta='0=InputMonthlyTarget,1=InputFullTimeSeries')
    batt_custom_dispatch: Array = INPUT(label='Custom battery power for every time step', units='kW', type='ARRAY', group='BatteryDispatch', required='en_batt=1&batt_dispatch_choice=3', meta='kWAC if AC-connected, else kWDC')
    batt_dispatch_choice: float = INPUT(label='Battery dispatch algorithm', units='0/1/2/3/4', type='NUMBER', group='BatteryDispatch', required='en_batt=1', meta='If behind the meter: 0=PeakShavingLookAhead,1=PeakShavingLookBehind,2=InputGridTarget,3=InputBatteryPower,4=ManualDispatch, if front of meter: 0=AutomatedLookAhead,1=AutomatedLookBehind,2=AutomatedInputForecast,3=InputBatteryPower,4=ManualDispatch')
    batt_pv_clipping_forecast: Array = INPUT(label='Power clipping forecast', units='kW', type='ARRAY', group='BatteryDispatch', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2')
    batt_pv_dc_forecast: Array = INPUT(label='DC power forecast', units='kW', type='ARRAY', group='BatteryDispatch', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2')
    batt_dispatch_auto_can_fuelcellcharge: float = INPUT(label='Charging from fuel cell allowed for automated dispatch?', units='kW', type='NUMBER', group='BatteryDispatch')
    batt_dispatch_auto_can_gridcharge: float = INPUT(label='Grid charging allowed for automated dispatch?', units='kW', type='NUMBER', group='BatteryDispatch')
    batt_dispatch_auto_can_charge: float = INPUT(label='System charging allowed for automated dispatch?', units='kW', type='NUMBER', group='BatteryDispatch')
    batt_dispatch_auto_can_clipcharge: float = INPUT(label='Battery can charge from clipped power for automated dispatch?', units='kW', type='NUMBER', group='BatteryDispatch')
    batt_auto_gridcharge_max_daily: float = INPUT(label='Allowed grid charging percent per day for automated dispatch', units='kW', type='NUMBER', group='BatteryDispatch')
    batt_look_ahead_hours: float = INPUT(label='Hours to look ahead in automated dispatch', units='hours', type='NUMBER', group='BatteryDispatch')
    batt_dispatch_update_frequency_hours: float = INPUT(label='Frequency to update the look-ahead dispatch', units='hours', type='NUMBER', group='BatteryDispatch')
    batt_cycle_cost_choice: float = INPUT(label='Use SAM model for cycle costs or input custom', units='0/1', type='NUMBER', group='BatterySystem', meta='0=UseCostModel,1=InputCost')
    batt_cycle_cost: float = INPUT(label='Input battery cycle costs', units='$/cycle-kWh', type='NUMBER', group='BatterySystem')
    en_electricity_rates: float = INOUT(label='Enable Electricity Rates', units='0/1', type='NUMBER', group='Electricity Rates', meta='0=EnableElectricityRates,1=NoRates')
    ur_en_ts_sell_rate: float = INPUT(label='Enable time step sell rates', units='0/1', type='NUMBER', group='Electricity Rates', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2', constraints='BOOLEAN')
    ur_ts_buy_rate: Array = INPUT(label='Time step buy rates', units='0/1', type='ARRAY', group='Electricity Rates', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2')
    ur_ec_sched_weekday: Matrix = INPUT(label='Energy charge weekday schedule', type='MATRIX', group='Electricity Rates', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2', meta='12 x 24 matrix')
    ur_ec_sched_weekend: Matrix = INPUT(label='Energy charge weekend schedule', type='MATRIX', group='Electricity Rates', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2', meta='12 x 24 matrix')
    ur_ec_tou_mat: Matrix = INPUT(label='Energy rates table', type='MATRIX', group='Electricity Rates', required='en_batt=1&batt_meter_position=1&batt_dispatch_choice=2')
    fuelcell_power: Array = INPUT(label='Electricity from fuel cell', units='kW', type='ARRAY', group='FuelCell')
    forecast_price_signal_model: float = INPUT(label='Forecast price signal model selected', units='0/1', type='NUMBER', group='Price Signal', required='?=0', constraints='INTEGER,MIN=0,MAX=1', meta='0=PPA based,1=Merchant Plant')
    ppa_price_input: Array = INPUT(label='PPA Price Input', type='ARRAY', group='Price Signal', required='forecast_price_signal_model=0&en_batt=1&batt_meter_position=1')
    ppa_multiplier_model: float = INPUT(label='PPA multiplier model', units='0/1', type='NUMBER', group='Price Signal', required='forecast_price_signal_model=0&en_batt=1&batt_meter_position=1', constraints='INTEGER,MIN=0', meta='0=diurnal,1=timestep')
    dispatch_factors_ts: Array = INPUT(label='Dispatch payment factor time step', type='ARRAY', group='Price Signal', required='forecast_price_signal_model=0&en_batt=1&batt_meter_position=1&ppa_multiplier_model=1')
    dispatch_tod_factors: Array = INPUT(label='TOD factors for periods 1-9', type='ARRAY', group='Price Signal', required='en_batt=1&batt_meter_position=1&forecast_price_signal_model=0&ppa_multiplier_model=0')
    dispatch_sched_weekday: Matrix = INPUT(label='Diurnal weekday TOD periods', units='1..9', type='MATRIX', group='Price Signal', required='en_batt=1&batt_meter_position=1&forecast_price_signal_model=0&ppa_multiplier_model=0', meta='12 x 24 matrix')
    dispatch_sched_weekend: Matrix = INPUT(label='Diurnal weekend TOD periods', units='1..9', type='MATRIX', group='Price Signal', required='en_batt=1&batt_meter_position=1&forecast_price_signal_model=0&ppa_multiplier_model=0', meta='12 x 24 matrix')
    mp_enable_energy_market_revenue: float = INPUT(label='Enable energy market revenue', units='0/1', type='NUMBER', group='Price Signal', required='en_batt=1&batt_meter_position=1&forecast_price_signal_model=1', constraints='INTEGER,MIN=0,MAX=1', meta='0=false,1=true')
    mp_energy_market_revenue: Matrix = INPUT(label='Energy market revenue input', units=' [MW, $/MW]', type='MATRIX', group='Price Signal', required='en_batt=1&batt_meter_position=1&forecast_price_signal_model=1')
    mp_enable_ancserv1: float = INPUT(label='Enable ancillary services 1 revenue', units='0/1', type='NUMBER', group='Price Signal', required='forecast_price_signal_model=1', constraints='INTEGER,MIN=0,MAX=1')
    mp_ancserv1_revenue: Matrix = INPUT(label='Ancillary services 1 revenue input', units=' [MW, $/MW]', type='MATRIX', group='Price Signal', required='en_batt=1&batt_meter_position=1&forecast_price_signal_model=1')
    mp_enable_ancserv2: float = INPUT(label='Enable ancillary services 2 revenue', units='0/1', type='NUMBER', group='Price Signal', required='forecast_price_signal_model=1', constraints='INTEGER,MIN=0,MAX=1')
    mp_ancserv2_revenue: Matrix = INPUT(label='Ancillary services 2 revenue input', units=' [MW, $/MW]', type='MATRIX', group='Price Signal', required='en_batt=1&batt_meter_position=1&forecast_price_signal_model=1')
    mp_enable_ancserv3: float = INPUT(label='Enable ancillary services 3 revenue', units='0/1', type='NUMBER', group='Price Signal', required='forecast_price_signal_model=1', constraints='INTEGER,MIN=0,MAX=1')
    mp_ancserv3_revenue: Matrix = INPUT(label='Ancillary services 3 revenue input', units=' [MW, $/MW]', type='MATRIX', group='Price Signal', required='en_batt=1&batt_meter_position=1&forecast_price_signal_model=1')
    mp_enable_ancserv4: float = INPUT(label='Enable ancillary services 4 revenue', units='0/1', type='NUMBER', group='Price Signal', required='forecast_price_signal_model=1', constraints='INTEGER,MIN=0,MAX=1')
    mp_ancserv4_revenue: Matrix = INPUT(label='Ancillary services 4 revenue input', units=' [MW, $/MW]', type='MATRIX', group='Price Signal', required='en_batt=1&batt_meter_position=1&forecast_price_signal_model=1')
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
    batt_capacity_percent: Final[Array] = OUTPUT(label='Battery relative capacity to nameplate', units='%', type='ARRAY', group='Battery')
    batt_capacity_percent_cycle: Final[Array] = OUTPUT(label='Battery relative capacity to nameplate (cycling)', units='%', type='ARRAY', group='Battery')
    batt_capacity_percent_calendar: Final[Array] = OUTPUT(label='Battery relative capacity to nameplate (calendar)', units='%', type='ARRAY', group='Battery')
    batt_capacity_thermal_percent: Final[Array] = OUTPUT(label='Battery capacity percent for temperature', units='%', type='ARRAY', group='Battery')
    batt_bank_replacement: Final[Array] = OUTPUT(label='Battery bank replacements per year', units='number/year', type='ARRAY', group='Battery')
    batt_power: Final[Array] = OUTPUT(label='Electricity to/from battery', units='kW', type='ARRAY', group='Battery')
    grid_power: Final[Array] = OUTPUT(label='Electricity to/from grid', units='kW', type='ARRAY', group='Battery')
    pv_to_load: Final[Array] = OUTPUT(label='Electricity to load from system', units='kW', type='ARRAY', group='Battery')
    batt_to_load: Final[Array] = OUTPUT(label='Electricity to load from battery', units='kW', type='ARRAY', group='Battery')
    grid_to_load: Final[Array] = OUTPUT(label='Electricity to load from grid', units='kW', type='ARRAY', group='Battery')
    pv_to_batt: Final[Array] = OUTPUT(label='Electricity to battery from system', units='kW', type='ARRAY', group='Battery')
    fuelcell_to_batt: Final[Array] = OUTPUT(label='Electricity to battery from fuel cell', units='kW', type='ARRAY', group='Battery')
    grid_to_batt: Final[Array] = OUTPUT(label='Electricity to battery from grid', units='kW', type='ARRAY', group='Battery')
    pv_to_grid: Final[Array] = OUTPUT(label='Electricity to grid from system', units='kW', type='ARRAY', group='Battery')
    batt_to_grid: Final[Array] = OUTPUT(label='Electricity to grid from battery', units='kW', type='ARRAY', group='Battery')
    batt_conversion_loss: Final[Array] = OUTPUT(label='Electricity loss in battery power electronics', units='kW', type='ARRAY', group='Battery')
    batt_system_loss: Final[Array] = OUTPUT(label='Electricity loss from battery ancillary equipment', units='kW', type='ARRAY', group='Battery')
    grid_power_target: Final[Array] = OUTPUT(label='Electricity grid power target for automated dispatch', units='kW', type='ARRAY', group='Battery')
    batt_power_target: Final[Array] = OUTPUT(label='Electricity battery power target for automated dispatch', units='kW', type='ARRAY', group='Battery')
    batt_cost_to_cycle: Final[Array] = OUTPUT(label='Battery computed cost to cycle', units='$/cycle', type='ARRAY', group='Battery')
    market_sell_rate_series_yr1: Final[Array] = OUTPUT(label='Market sell rate (Year 1)', units='$/MWh', type='ARRAY', group='Battery')
    batt_revenue_gridcharge: Final[Array] = OUTPUT(label='Revenue to charge from grid', units='$/kWh', type='ARRAY', group='Battery')
    batt_revenue_charge: Final[Array] = OUTPUT(label='Revenue to charge from system', units='$/kWh', type='ARRAY', group='Battery')
    batt_revenue_clipcharge: Final[Array] = OUTPUT(label='Revenue to charge from clipped', units='$/kWh', type='ARRAY', group='Battery')
    batt_revenue_discharge: Final[Array] = OUTPUT(label='Revenue to discharge', units='$/kWh', type='ARRAY', group='Battery')
    monthly_pv_to_load: Final[Array] = OUTPUT(label='Energy to load from system', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_batt_to_load: Final[Array] = OUTPUT(label='Energy to load from battery', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_grid_to_load: Final[Array] = OUTPUT(label='Energy to load from grid', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_pv_to_grid: Final[Array] = OUTPUT(label='Energy to grid from system', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_batt_to_grid: Final[Array] = OUTPUT(label='Energy to grid from battery', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_pv_to_batt: Final[Array] = OUTPUT(label='Energy to battery from system', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    monthly_grid_to_batt: Final[Array] = OUTPUT(label='Energy to battery from grid', units='kWh', type='ARRAY', group='Battery', constraints='LENGTH=12')
    batt_annual_charge_from_pv: Final[Array] = OUTPUT(label='Battery annual energy charged from system', units='kWh', type='ARRAY', group='Battery')
    batt_annual_charge_from_grid: Final[Array] = OUTPUT(label='Battery annual energy charged from grid', units='kWh', type='ARRAY', group='Battery')
    batt_annual_charge_energy: Final[Array] = OUTPUT(label='Battery annual energy charged', units='kWh', type='ARRAY', group='Battery')
    batt_annual_discharge_energy: Final[Array] = OUTPUT(label='Battery annual energy discharged', units='kWh', type='ARRAY', group='Battery')
    batt_annual_energy_loss: Final[Array] = OUTPUT(label='Battery annual energy loss', units='kWh', type='ARRAY', group='Battery')
    batt_annual_energy_system_loss: Final[Array] = OUTPUT(label='Battery annual system energy loss', units='kWh', type='ARRAY', group='Battery')
    annual_export_to_grid_energy: Final[Array] = OUTPUT(label='Annual energy exported to grid', units='kWh', type='ARRAY', group='Battery')
    annual_import_to_grid_energy: Final[Array] = OUTPUT(label='Annual energy imported from grid', units='kWh', type='ARRAY', group='Battery')
    average_battery_conversion_efficiency: Final[float] = OUTPUT(label='Battery average cycle conversion efficiency', units='%', type='NUMBER', group='Annual')
    average_battery_roundtrip_efficiency: Final[float] = OUTPUT(label='Battery average roundtrip efficiency', units='%', type='NUMBER', group='Annual')
    batt_pv_charge_percent: Final[float] = OUTPUT(label='Battery charge energy charged from system', units='%', type='NUMBER', group='Annual')
    batt_bank_installed_capacity: Final[float] = OUTPUT(label='Battery bank installed capacity', units='kWh', type='NUMBER', group='Annual')
    batt_dispatch_sched: Final[Matrix] = OUTPUT(label='Battery dispatch schedule', type='MATRIX', group='Battery')
    resilience_hrs: Final[Array] = OUTPUT(label='Hours of autonomy during outage at each timestep for resilience', units='hr', type='ARRAY', group='Resilience')
    resilience_hrs_min: Final[float] = OUTPUT(label='Min hours of autonomy for resilience ', units='hr', type='NUMBER', group='Resilience', constraints='MIN=0')
    resilience_hrs_max: Final[float] = OUTPUT(label='Max hours of autonomy for resilience', units='hr', type='NUMBER', group='Resilience', constraints='MIN=0')
    resilience_hrs_avg: Final[float] = OUTPUT(label='Avg hours of autonomy for resilience', units='hr', type='NUMBER', group='Resilience', constraints='MIN=0')
    outage_durations: Final[Array] = OUTPUT(label='List of autonomous hours for resilience from min to max', units='hr', type='ARRAY', group='Resilience', meta='Hours from resilience_hrs_min to resilience_hrs_max')
    pdf_of_surviving: Final[Array] = OUTPUT(label='Probabilities of autonomous hours for resilience ', type='ARRAY', group='Resilience', constraints='MIN=0,MAX=1', meta='Hours from resilience_hrs_min to resilience_hrs_max')
    cdf_of_surviving: Final[Array] = OUTPUT(label='Cumulative probabilities of autonomous hours for resilience', type='ARRAY', group='Resilience', constraints='MIN=0,MAX=1', meta='Prob surviving at least x hrs; hrs from min to max')
    survival_function: Final[Array] = OUTPUT(label='Survival function of autonomous hours for resilience', type='ARRAY', group='Resilience', constraints='MIN=0,MAX=1', meta='Prob surviving greater than x hours; hrs from min to max')
    avg_critical_load: Final[float] = OUTPUT(label='Average critical load met for resilience', units='kWh', type='NUMBER', group='Resilience', constraints='MIN=0')

    def __init__(self, *args: Mapping[str, Any],
                 percent_complete: float = ...,
                 system_use_lifetime_output: float = ...,
                 analysis_period: float = ...,
                 en_batt: float = ...,
                 gen: Array = ...,
                 load: Array = ...,
                 crit_load: Array = ...,
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
                 batt_inverter_efficiency_cutoff: float = ...,
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
                 batt_power_charge_max_kwdc: float = ...,
                 batt_power_discharge_max_kwdc: float = ...,
                 batt_power_charge_max_kwac: float = ...,
                 batt_power_discharge_max_kwac: float = ...,
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
                 batt_replacement_option: float = ...,
                 batt_replacement_schedule: Array = ...,
                 batt_replacement_schedule_percent: Array = ...,
                 om_replacement_cost1: Array = ...,
                 batt_mass: float = ...,
                 batt_surface_area: float = ...,
                 batt_Cp: float = ...,
                 batt_h_to_ambient: float = ...,
                 batt_room_temperature_celsius: Array = ...,
                 cap_vs_temp: Matrix = ...,
                 dispatch_manual_charge: Array = ...,
                 dispatch_manual_fuelcellcharge: Array = ...,
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
                 batt_dispatch_auto_can_fuelcellcharge: float = ...,
                 batt_dispatch_auto_can_gridcharge: float = ...,
                 batt_dispatch_auto_can_charge: float = ...,
                 batt_dispatch_auto_can_clipcharge: float = ...,
                 batt_auto_gridcharge_max_daily: float = ...,
                 batt_look_ahead_hours: float = ...,
                 batt_dispatch_update_frequency_hours: float = ...,
                 batt_cycle_cost_choice: float = ...,
                 batt_cycle_cost: float = ...,
                 en_electricity_rates: float = ...,
                 ur_en_ts_sell_rate: float = ...,
                 ur_ts_buy_rate: Array = ...,
                 ur_ec_sched_weekday: Matrix = ...,
                 ur_ec_sched_weekend: Matrix = ...,
                 ur_ec_tou_mat: Matrix = ...,
                 fuelcell_power: Array = ...,
                 forecast_price_signal_model: float = ...,
                 ppa_price_input: Array = ...,
                 ppa_multiplier_model: float = ...,
                 dispatch_factors_ts: Array = ...,
                 dispatch_tod_factors: Array = ...,
                 dispatch_sched_weekday: Matrix = ...,
                 dispatch_sched_weekend: Matrix = ...,
                 mp_enable_energy_market_revenue: float = ...,
                 mp_energy_market_revenue: Matrix = ...,
                 mp_enable_ancserv1: float = ...,
                 mp_ancserv1_revenue: Matrix = ...,
                 mp_enable_ancserv2: float = ...,
                 mp_ancserv2_revenue: Matrix = ...,
                 mp_enable_ancserv3: float = ...,
                 mp_ancserv3_revenue: Matrix = ...,
                 mp_enable_ancserv4: float = ...,
                 mp_ancserv4_revenue: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
