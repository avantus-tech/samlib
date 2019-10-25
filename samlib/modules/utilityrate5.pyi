
# This is a generated file

"""utilityrate5 - Complex utility rate structure net revenue calculator OpenEI Version 4 with net billing"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'en_electricity_rates': float,
        'analysis_period': float,
        'system_use_lifetime_output': float,
        'TOU_demand_single_peak': float,
        'gen': Array,
        'load': Array,
        'bill_load': Array,
        'inflation_rate': float,
        'degradation': Array,
        'load_escalation': Array,
        'rate_escalation': Array,
        'ur_metering_option': float,
        'ur_nm_yearend_sell_rate': float,
        'ur_monthly_fixed_charge': float,
        'ur_sell_eq_buy': float,
        'ur_monthly_min_charge': float,
        'ur_annual_min_charge': float,
        'ur_en_ts_sell_rate': float,
        'ur_ts_sell_rate': Array,
        'ur_ec_sched_weekday': Matrix,
        'ur_ec_sched_weekend': Matrix,
        'ur_ec_tou_mat': Matrix,
        'ur_dc_enable': float,
        'ur_dc_sched_weekday': Matrix,
        'ur_dc_sched_weekend': Matrix,
        'ur_dc_tou_mat': Matrix,
        'ur_dc_flat_mat': Matrix,
        'annual_energy_value': Array,
        'annual_electric_load': Array,
        'elec_cost_with_system': Array,
        'elec_cost_without_system': Array,
        'elec_cost_with_system_year1': float,
        'elec_cost_without_system_year1': float,
        'savings_year1': float,
        'year1_electric_load': float,
        'year1_hourly_e_tofromgrid': Array,
        'year1_hourly_e_togrid': Array,
        'year1_hourly_e_fromgrid': Array,
        'year1_hourly_system_to_load': Array,
        'lifetime_load': Array,
        'year1_hourly_p_tofromgrid': Array,
        'year1_hourly_p_system_to_load': Array,
        'year1_hourly_salespurchases_with_system': Array,
        'year1_hourly_salespurchases_without_system': Array,
        'year1_hourly_ec_with_system': Array,
        'year1_hourly_ec_without_system': Array,
        'year1_hourly_dc_with_system': Array,
        'year1_hourly_dc_without_system': Array,
        'year1_hourly_ec_tou_schedule': Array,
        'year1_hourly_dc_tou_schedule': Array,
        'year1_hourly_dc_peak_per_period': Array,
        'year1_monthly_fixed_with_system': Array,
        'year1_monthly_fixed_without_system': Array,
        'year1_monthly_minimum_with_system': Array,
        'year1_monthly_minimum_without_system': Array,
        'year1_monthly_dc_fixed_with_system': Array,
        'year1_monthly_dc_tou_with_system': Array,
        'year1_monthly_ec_charge_with_system': Array,
        'year1_monthly_dc_fixed_without_system': Array,
        'year1_monthly_dc_tou_without_system': Array,
        'year1_monthly_ec_charge_without_system': Array,
        'year1_monthly_load': Array,
        'year1_monthly_peak_w_system': Array,
        'year1_monthly_peak_wo_system': Array,
        'year1_monthly_use_w_system': Array,
        'year1_monthly_use_wo_system': Array,
        'year1_monthly_electricity_to_grid': Array,
        'year1_monthly_cumulative_excess_generation': Array,
        'year1_monthly_cumulative_excess_dollars': Array,
        'year1_monthly_utility_bill_w_sys': Array,
        'year1_monthly_utility_bill_wo_sys': Array,
        'utility_bill_w_sys_ym': Matrix,
        'utility_bill_wo_sys_ym': Matrix,
        'charge_w_sys_fixed_ym': Matrix,
        'charge_wo_sys_fixed_ym': Matrix,
        'charge_w_sys_minimum_ym': Matrix,
        'charge_wo_sys_minimum_ym': Matrix,
        'charge_w_sys_dc_fixed_ym': Matrix,
        'charge_w_sys_dc_tou_ym': Matrix,
        'charge_wo_sys_dc_fixed_ym': Matrix,
        'charge_wo_sys_dc_tou_ym': Matrix,
        'charge_w_sys_ec_ym': Matrix,
        'charge_wo_sys_ec_ym': Matrix,
        'utility_bill_w_sys': Array,
        'utility_bill_wo_sys': Array,
        'charge_w_sys_fixed': Array,
        'charge_wo_sys_fixed': Array,
        'charge_w_sys_minimum': Array,
        'charge_wo_sys_minimum': Array,
        'charge_w_sys_dc_fixed': Array,
        'charge_w_sys_dc_tou': Array,
        'charge_wo_sys_dc_fixed': Array,
        'charge_wo_sys_dc_tou': Array,
        'charge_w_sys_ec': Array,
        'charge_wo_sys_ec': Array,
        'charge_w_sys_ec_gross_ym': Matrix,
        'excess_dollars_applied_ym': Matrix,
        'excess_dollars_earned_ym': Matrix,
        'excess_kwhs_applied_ym': Matrix,
        'excess_kwhs_earned_ym': Matrix,
        'year1_monthly_ec_charge_gross_with_system': Array,
        'year1_excess_dollars_applied': Array,
        'year1_excess_dollars_earned': Array,
        'year1_excess_kwhs_applied': Array,
        'year1_excess_kwhs_earned': Array,
        'charge_wo_sys_ec_jan_tp': Matrix,
        'charge_wo_sys_ec_feb_tp': Matrix,
        'charge_wo_sys_ec_mar_tp': Matrix,
        'charge_wo_sys_ec_apr_tp': Matrix,
        'charge_wo_sys_ec_may_tp': Matrix,
        'charge_wo_sys_ec_jun_tp': Matrix,
        'charge_wo_sys_ec_jul_tp': Matrix,
        'charge_wo_sys_ec_aug_tp': Matrix,
        'charge_wo_sys_ec_sep_tp': Matrix,
        'charge_wo_sys_ec_oct_tp': Matrix,
        'charge_wo_sys_ec_nov_tp': Matrix,
        'charge_wo_sys_ec_dec_tp': Matrix,
        'energy_wo_sys_ec_jan_tp': Matrix,
        'energy_wo_sys_ec_feb_tp': Matrix,
        'energy_wo_sys_ec_mar_tp': Matrix,
        'energy_wo_sys_ec_apr_tp': Matrix,
        'energy_wo_sys_ec_may_tp': Matrix,
        'energy_wo_sys_ec_jun_tp': Matrix,
        'energy_wo_sys_ec_jul_tp': Matrix,
        'energy_wo_sys_ec_aug_tp': Matrix,
        'energy_wo_sys_ec_sep_tp': Matrix,
        'energy_wo_sys_ec_oct_tp': Matrix,
        'energy_wo_sys_ec_nov_tp': Matrix,
        'energy_wo_sys_ec_dec_tp': Matrix,
        'charge_w_sys_ec_jan_tp': Matrix,
        'charge_w_sys_ec_feb_tp': Matrix,
        'charge_w_sys_ec_mar_tp': Matrix,
        'charge_w_sys_ec_apr_tp': Matrix,
        'charge_w_sys_ec_may_tp': Matrix,
        'charge_w_sys_ec_jun_tp': Matrix,
        'charge_w_sys_ec_jul_tp': Matrix,
        'charge_w_sys_ec_aug_tp': Matrix,
        'charge_w_sys_ec_sep_tp': Matrix,
        'charge_w_sys_ec_oct_tp': Matrix,
        'charge_w_sys_ec_nov_tp': Matrix,
        'charge_w_sys_ec_dec_tp': Matrix,
        'energy_w_sys_ec_jan_tp': Matrix,
        'energy_w_sys_ec_feb_tp': Matrix,
        'energy_w_sys_ec_mar_tp': Matrix,
        'energy_w_sys_ec_apr_tp': Matrix,
        'energy_w_sys_ec_may_tp': Matrix,
        'energy_w_sys_ec_jun_tp': Matrix,
        'energy_w_sys_ec_jul_tp': Matrix,
        'energy_w_sys_ec_aug_tp': Matrix,
        'energy_w_sys_ec_sep_tp': Matrix,
        'energy_w_sys_ec_oct_tp': Matrix,
        'energy_w_sys_ec_nov_tp': Matrix,
        'energy_w_sys_ec_dec_tp': Matrix,
        'surplus_w_sys_ec_jan_tp': Matrix,
        'surplus_w_sys_ec_feb_tp': Matrix,
        'surplus_w_sys_ec_mar_tp': Matrix,
        'surplus_w_sys_ec_apr_tp': Matrix,
        'surplus_w_sys_ec_may_tp': Matrix,
        'surplus_w_sys_ec_jun_tp': Matrix,
        'surplus_w_sys_ec_jul_tp': Matrix,
        'surplus_w_sys_ec_aug_tp': Matrix,
        'surplus_w_sys_ec_sep_tp': Matrix,
        'surplus_w_sys_ec_oct_tp': Matrix,
        'surplus_w_sys_ec_nov_tp': Matrix,
        'surplus_w_sys_ec_dec_tp': Matrix,
        'monthly_tou_demand_peak_w_sys': Matrix,
        'monthly_tou_demand_peak_wo_sys': Matrix,
        'monthly_tou_demand_charge_w_sys': Matrix,
        'monthly_tou_demand_charge_wo_sys': Matrix
}, total=False)

class Data(ssc.DataDict):
    en_electricity_rates: float = INPUT(label='Optionally enable/disable electricity_rate', units='years', type='NUMBER', constraints='INTEGER,MIN=0,MAX=1')
    analysis_period: float = INPUT(label='Number of years in analysis', units='years', type='NUMBER', required='*', constraints='INTEGER,POSITIVE')
    system_use_lifetime_output: float = INPUT(label='Lifetime hourly system outputs', units='0/1', type='NUMBER', required='*', constraints='INTEGER,MIN=0,MAX=1', meta='0=hourly first year,1=hourly lifetime')
    TOU_demand_single_peak: float = INPUT(label='Use single monthly peak for TOU demand charge', units='0/1', type='NUMBER', required='?=0', constraints='INTEGER,MIN=0,MAX=1', meta='0=use TOU peak,1=use flat peak')
    gen: Array = INPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')
    load: Array = INOUT(label='Electricity load (year 1)', units='kW', type='ARRAY', group='Time Series')
    bill_load: Final[Array] = OUTPUT(label='Bill load (year 1)', units='kWh', type='ARRAY', group='Time Series', required='*')
    inflation_rate: float = INPUT(label='Inflation rate', units='%', type='NUMBER', group='Financials', required='*', constraints='MIN=-99')
    degradation: Array = INPUT(label='Annual energy degradation', units='%', type='ARRAY', group='AnnualOutput', required='*')
    load_escalation: Array = INPUT(label='Annual load escalation', units='%/year', type='ARRAY', required='?=0')
    rate_escalation: Array = INPUT(label='Annual electricity rate escalation', units='%/year', type='ARRAY', required='?=0')
    ur_metering_option: float = INPUT(label='Metering options', units='0=Single meter with monthly rollover credits in kWh,1=Single meter with monthly rollover credits in $,2=Single meter with no monthly rollover credits (Net Billing),3=Single meter with monthly rollover credits in $ (Net Billing $),4=Two meters with all generation sold and all load purchased', type='NUMBER', required='?=0', constraints='INTEGER,MIN=0,MAX=4', meta='Net metering monthly excess')
    ur_nm_yearend_sell_rate: float = INPUT(label='Year end sell rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_monthly_fixed_charge: float = INPUT(label='Monthly fixed charge', units='$', type='NUMBER', required='?=0.0')
    ur_sell_eq_buy: float = INPUT(label='Set sell rate equal to buy rate', units='0/1', type='NUMBER', required='?=0', constraints='BOOLEAN', meta='Optional override')
    ur_monthly_min_charge: float = INPUT(label='Monthly minimum charge', units='$', type='NUMBER', required='?=0.0')
    ur_annual_min_charge: float = INPUT(label='Annual minimum charge', units='$', type='NUMBER', required='?=0.0')
    ur_en_ts_sell_rate: float = INPUT(label='Enable time step sell rates', units='0/1', type='NUMBER', required='?=0', constraints='BOOLEAN')
    ur_ts_sell_rate: Array = INPUT(label='Time step sell rates', units='0/1', type='ARRAY')
    ur_ec_sched_weekday: Matrix = INPUT(label='Energy charge weekday schedule', type='MATRIX', required='*', meta='12x24')
    ur_ec_sched_weekend: Matrix = INPUT(label='Energy charge weekend schedule', type='MATRIX', required='*', meta='12x24')
    ur_ec_tou_mat: Matrix = INPUT(label='Energy rates table', type='MATRIX', required='*')
    ur_dc_enable: float = INPUT(label='Enable demand charge', units='0/1', type='NUMBER', required='?=0', constraints='BOOLEAN')
    ur_dc_sched_weekday: Matrix = INPUT(label='Demand charge weekday schedule', type='MATRIX', meta='12x24')
    ur_dc_sched_weekend: Matrix = INPUT(label='Demand charge weekend schedule', type='MATRIX', meta='12x24')
    ur_dc_tou_mat: Matrix = INPUT(label='Demand rates (TOU) table', type='MATRIX', required='ur_dc_enable=1')
    ur_dc_flat_mat: Matrix = INPUT(label='Demand rates (flat) table', type='MATRIX', required='ur_dc_enable=1')
    annual_energy_value: Final[Array] = OUTPUT(label='Energy value in each year', units='$', type='ARRAY', group='Annual', required='*')
    annual_electric_load: Final[Array] = OUTPUT(label='Electricity load total in each year', units='kWh', type='ARRAY', group='Annual', required='*')
    elec_cost_with_system: Final[Array] = OUTPUT(label='Electricity bill with system', units='$/yr', type='ARRAY', group='Annual', required='*')
    elec_cost_without_system: Final[Array] = OUTPUT(label='Electricity bill without system', units='$/yr', type='ARRAY', group='Annual', required='*')
    elec_cost_with_system_year1: Final[float] = OUTPUT(label='Electricity bill with system (year 1)', units='$/yr', type='NUMBER', group='Financial Metrics', required='*')
    elec_cost_without_system_year1: Final[float] = OUTPUT(label='Electricity bill without system (year 1)', units='$/yr', type='NUMBER', group='Financial Metrics', required='*')
    savings_year1: Final[float] = OUTPUT(label='Electricity bill savings with system (year 1)', units='$/yr', type='NUMBER', group='Financial Metrics', required='*')
    year1_electric_load: Final[float] = OUTPUT(label='Electricity load total (year 1)', units='kWh/yr', type='NUMBER', group='Financial Metrics', required='*')
    year1_hourly_e_tofromgrid: Final[Array] = OUTPUT(label='Electricity to/from grid (year 1 hourly)', units='kWh', type='ARRAY', group='Time Series', required='*')
    year1_hourly_e_togrid: Final[Array] = OUTPUT(label='Electricity to grid (year 1 hourly)', units='kWh', type='ARRAY', group='Time Series', required='*')
    year1_hourly_e_fromgrid: Final[Array] = OUTPUT(label='Electricity from grid (year 1 hourly)', units='kWh', type='ARRAY', group='Time Series', required='*')
    year1_hourly_system_to_load: Final[Array] = OUTPUT(label='Electricity from system to load (year 1 hourly)', units='kWh', type='ARRAY', required='*')
    lifetime_load: Final[Array] = OUTPUT(label='Lifetime electricity load', units='kW', type='ARRAY', group='Time Series', required='system_use_lifetime_output=1')
    year1_hourly_p_tofromgrid: Final[Array] = OUTPUT(label='Electricity to/from grid peak (year 1 hourly)', units='kW', type='ARRAY', group='Time Series', required='*')
    year1_hourly_p_system_to_load: Final[Array] = OUTPUT(label='Electricity peak from system to load (year 1 hourly)', units='kW', type='ARRAY', group='Time Series', required='*')
    year1_hourly_salespurchases_with_system: Final[Array] = OUTPUT(label='Electricity sales/purchases with system (year 1 hourly)', units='$', type='ARRAY', group='Time Series', required='*')
    year1_hourly_salespurchases_without_system: Final[Array] = OUTPUT(label='Electricity sales/purchases without system (year 1 hourly)', units='$', type='ARRAY', group='Time Series', required='*')
    year1_hourly_ec_with_system: Final[Array] = OUTPUT(label='Energy charge with system (year 1 hourly)', units='$', type='ARRAY', group='Time Series', required='*')
    year1_hourly_ec_without_system: Final[Array] = OUTPUT(label='Energy charge without system (year 1 hourly)', units='$', type='ARRAY', group='Time Series', required='*')
    year1_hourly_dc_with_system: Final[Array] = OUTPUT(label='Demand charge with system (year 1 hourly)', units='$', type='ARRAY', group='Time Series', required='*')
    year1_hourly_dc_without_system: Final[Array] = OUTPUT(label='Demand charge without system (year 1 hourly)', units='$', type='ARRAY', group='Time Series', required='*')
    year1_hourly_ec_tou_schedule: Final[Array] = OUTPUT(label='TOU period for energy charges (year 1 hourly)', type='ARRAY', group='Time Series', required='*')
    year1_hourly_dc_tou_schedule: Final[Array] = OUTPUT(label='TOU period for demand charges (year 1 hourly)', type='ARRAY', group='Time Series', required='*')
    year1_hourly_dc_peak_per_period: Final[Array] = OUTPUT(label='Electricity peak from grid per TOU period (year 1 hourly)', units='kW', type='ARRAY', group='Time Series', required='*')
    year1_monthly_fixed_with_system: Final[Array] = OUTPUT(label='Fixed monthly charge with system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_fixed_without_system: Final[Array] = OUTPUT(label='Fixed monthly charge without system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_minimum_with_system: Final[Array] = OUTPUT(label='Minimum charge with system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_minimum_without_system: Final[Array] = OUTPUT(label='Minimum charge without system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_dc_fixed_with_system: Final[Array] = OUTPUT(label='Demand charge (flat) with system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_dc_tou_with_system: Final[Array] = OUTPUT(label='Demand charge (TOU) with system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_ec_charge_with_system: Final[Array] = OUTPUT(label='Energy charge with system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_dc_fixed_without_system: Final[Array] = OUTPUT(label='Demand charge (flat) without system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_dc_tou_without_system: Final[Array] = OUTPUT(label='Demand charge (TOU) without system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_ec_charge_without_system: Final[Array] = OUTPUT(label='Energy charge without system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_load: Final[Array] = OUTPUT(label='Electricity load', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_peak_w_system: Final[Array] = OUTPUT(label='Demand peak with system', units='kW/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_peak_wo_system: Final[Array] = OUTPUT(label='Demand peak without system', units='kW/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_use_w_system: Final[Array] = OUTPUT(label='Electricity use with system', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_use_wo_system: Final[Array] = OUTPUT(label='Electricity use without system', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_electricity_to_grid: Final[Array] = OUTPUT(label='Electricity to/from grid', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_cumulative_excess_generation: Final[Array] = OUTPUT(label='Excess generation cumulative kWh credit earned', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_cumulative_excess_dollars: Final[Array] = OUTPUT(label='Excess generation cumulative $ credit earned', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_utility_bill_w_sys: Final[Array] = OUTPUT(label='Electricity bill with system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_utility_bill_wo_sys: Final[Array] = OUTPUT(label='Electricity bill without system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    utility_bill_w_sys_ym: Final[Matrix] = OUTPUT(label='Electricity bill with system', units='$', type='MATRIX', group='Charges by Month', required='*')
    utility_bill_wo_sys_ym: Final[Matrix] = OUTPUT(label='Electricity bill without system', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_fixed_ym: Final[Matrix] = OUTPUT(label='Fixed monthly charge with system', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_wo_sys_fixed_ym: Final[Matrix] = OUTPUT(label='Fixed monthly charge without system', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_minimum_ym: Final[Matrix] = OUTPUT(label='Minimum charge with system', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_wo_sys_minimum_ym: Final[Matrix] = OUTPUT(label='Minimum charge without system', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_dc_fixed_ym: Final[Matrix] = OUTPUT(label='Demand charge with system (flat)', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_dc_tou_ym: Final[Matrix] = OUTPUT(label='Demand charge with system (TOU)', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_wo_sys_dc_fixed_ym: Final[Matrix] = OUTPUT(label='Demand charge without system (flat)', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_wo_sys_dc_tou_ym: Final[Matrix] = OUTPUT(label='Demand charge without system (TOU)', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_ec_ym: Final[Matrix] = OUTPUT(label='Energy charge with system', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_wo_sys_ec_ym: Final[Matrix] = OUTPUT(label='Energy charge without system', units='$', type='MATRIX', group='Charges by Month', required='*')
    utility_bill_w_sys: Final[Array] = OUTPUT(label='Electricity bill with system', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_wo_sys: Final[Array] = OUTPUT(label='Electricity bill without system', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_fixed: Final[Array] = OUTPUT(label='Fixed monthly charge with system', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_fixed: Final[Array] = OUTPUT(label='Fixed monthly charge without system', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_minimum: Final[Array] = OUTPUT(label='Minimum charge with system', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_minimum: Final[Array] = OUTPUT(label='Minimum charge without system', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_fixed: Final[Array] = OUTPUT(label='Demand charge with system (flat)', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_tou: Final[Array] = OUTPUT(label='Demand charge with system (TOU)', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_fixed: Final[Array] = OUTPUT(label='Demand charge without system (flat)', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_tou: Final[Array] = OUTPUT(label='Demand charge without system (TOU)', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec: Final[Array] = OUTPUT(label='Energy charge with system', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec: Final[Array] = OUTPUT(label='Energy charge without system', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_gross_ym: Final[Matrix] = OUTPUT(label='Energy charge with system before credits', units='$', type='MATRIX', group='Charges by Month', required='*')
    excess_dollars_applied_ym: Final[Matrix] = OUTPUT(label='Excess generation $ credit applied', units='$', type='MATRIX', group='Charges by Month', required='*')
    excess_dollars_earned_ym: Final[Matrix] = OUTPUT(label='Excess generation $ credit earned', units='$', type='MATRIX', group='Charges by Month', required='*')
    excess_kwhs_applied_ym: Final[Matrix] = OUTPUT(label='Excess generation kWh credit applied', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    excess_kwhs_earned_ym: Final[Matrix] = OUTPUT(label='Excess generation kWh credit earned', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    year1_monthly_ec_charge_gross_with_system: Final[Array] = OUTPUT(label='Energy charge with system before credits', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_excess_dollars_applied: Final[Array] = OUTPUT(label='Excess generation $ credit applied', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_excess_dollars_earned: Final[Array] = OUTPUT(label='Excess generation $ credit earned', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_excess_kwhs_applied: Final[Array] = OUTPUT(label='Excess generation kWh credit applied', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_excess_kwhs_earned: Final[Array] = OUTPUT(label='Excess generation kWh credit earned', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    charge_wo_sys_ec_jan_tp: Final[Matrix] = OUTPUT(label='Energy charge without system Jan', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_wo_sys_ec_feb_tp: Final[Matrix] = OUTPUT(label='Energy charge without system Feb', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_wo_sys_ec_mar_tp: Final[Matrix] = OUTPUT(label='Energy charge without system Mar', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_wo_sys_ec_apr_tp: Final[Matrix] = OUTPUT(label='Energy charge without system Apr', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_wo_sys_ec_may_tp: Final[Matrix] = OUTPUT(label='Energy charge without system May', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_wo_sys_ec_jun_tp: Final[Matrix] = OUTPUT(label='Energy charge without system Jun', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_wo_sys_ec_jul_tp: Final[Matrix] = OUTPUT(label='Energy charge without system Jul', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_wo_sys_ec_aug_tp: Final[Matrix] = OUTPUT(label='Energy charge without system Aug', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_wo_sys_ec_sep_tp: Final[Matrix] = OUTPUT(label='Energy charge without system Sep', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_wo_sys_ec_oct_tp: Final[Matrix] = OUTPUT(label='Energy charge without system Oct', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_wo_sys_ec_nov_tp: Final[Matrix] = OUTPUT(label='Energy charge without system Nov', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_wo_sys_ec_dec_tp: Final[Matrix] = OUTPUT(label='Energy charge without system Dec', units='$', type='MATRIX', group='Charges by Month', required='*')
    energy_wo_sys_ec_jan_tp: Final[Matrix] = OUTPUT(label='Electricity usage without system Jan', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_wo_sys_ec_feb_tp: Final[Matrix] = OUTPUT(label='Electricity usage without system Feb', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_wo_sys_ec_mar_tp: Final[Matrix] = OUTPUT(label='Electricity usage without system Mar', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_wo_sys_ec_apr_tp: Final[Matrix] = OUTPUT(label='Electricity usage without system Apr', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_wo_sys_ec_may_tp: Final[Matrix] = OUTPUT(label='Electricity usage without system May', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_wo_sys_ec_jun_tp: Final[Matrix] = OUTPUT(label='Electricity usage without system Jun', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_wo_sys_ec_jul_tp: Final[Matrix] = OUTPUT(label='Electricity usage without system Jul', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_wo_sys_ec_aug_tp: Final[Matrix] = OUTPUT(label='Electricity usage without system Aug', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_wo_sys_ec_sep_tp: Final[Matrix] = OUTPUT(label='Electricity usage without system Sep', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_wo_sys_ec_oct_tp: Final[Matrix] = OUTPUT(label='Electricity usage without system Oct', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_wo_sys_ec_nov_tp: Final[Matrix] = OUTPUT(label='Electricity usage without system Nov', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_wo_sys_ec_dec_tp: Final[Matrix] = OUTPUT(label='Electricity usage without system Dec', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_ec_jan_tp: Final[Matrix] = OUTPUT(label='Energy charge with system Jan', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_ec_feb_tp: Final[Matrix] = OUTPUT(label='Energy charge with system Feb', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_ec_mar_tp: Final[Matrix] = OUTPUT(label='Energy charge with system Mar', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_ec_apr_tp: Final[Matrix] = OUTPUT(label='Energy charge with system Apr', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_ec_may_tp: Final[Matrix] = OUTPUT(label='Energy charge with system May', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_ec_jun_tp: Final[Matrix] = OUTPUT(label='Energy charge with system Jun', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_ec_jul_tp: Final[Matrix] = OUTPUT(label='Energy charge with system Jul', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_ec_aug_tp: Final[Matrix] = OUTPUT(label='Energy charge with system Aug', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_ec_sep_tp: Final[Matrix] = OUTPUT(label='Energy charge with system Sep', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_ec_oct_tp: Final[Matrix] = OUTPUT(label='Energy charge with system Oct', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_ec_nov_tp: Final[Matrix] = OUTPUT(label='Energy charge with system Nov', units='$', type='MATRIX', group='Charges by Month', required='*')
    charge_w_sys_ec_dec_tp: Final[Matrix] = OUTPUT(label='Energy charge with system Dec', units='$', type='MATRIX', group='Charges by Month', required='*')
    energy_w_sys_ec_jan_tp: Final[Matrix] = OUTPUT(label='Electricity usage with system Jan', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_w_sys_ec_feb_tp: Final[Matrix] = OUTPUT(label='Electricity usage with system Feb', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_w_sys_ec_mar_tp: Final[Matrix] = OUTPUT(label='Electricity usage with system Mar', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_w_sys_ec_apr_tp: Final[Matrix] = OUTPUT(label='Electricity usage with system Apr', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_w_sys_ec_may_tp: Final[Matrix] = OUTPUT(label='Electricity usage with system May', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_w_sys_ec_jun_tp: Final[Matrix] = OUTPUT(label='Electricity usage with system Jun', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_w_sys_ec_jul_tp: Final[Matrix] = OUTPUT(label='Electricity usage with system Jul', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_w_sys_ec_aug_tp: Final[Matrix] = OUTPUT(label='Electricity usage with system Aug', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_w_sys_ec_sep_tp: Final[Matrix] = OUTPUT(label='Electricity usage with system Sep', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_w_sys_ec_oct_tp: Final[Matrix] = OUTPUT(label='Electricity usage with system Oct', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_w_sys_ec_nov_tp: Final[Matrix] = OUTPUT(label='Electricity usage with system Nov', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    energy_w_sys_ec_dec_tp: Final[Matrix] = OUTPUT(label='Electricity usage with system Dec', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    surplus_w_sys_ec_jan_tp: Final[Matrix] = OUTPUT(label='Electricity exports with system Jan', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    surplus_w_sys_ec_feb_tp: Final[Matrix] = OUTPUT(label='Electricity exports with system Feb', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    surplus_w_sys_ec_mar_tp: Final[Matrix] = OUTPUT(label='Electricity exports with system Mar', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    surplus_w_sys_ec_apr_tp: Final[Matrix] = OUTPUT(label='Electricity exports with system Apr', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    surplus_w_sys_ec_may_tp: Final[Matrix] = OUTPUT(label='Electricity exports with system May', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    surplus_w_sys_ec_jun_tp: Final[Matrix] = OUTPUT(label='Electricity exports with system Jun', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    surplus_w_sys_ec_jul_tp: Final[Matrix] = OUTPUT(label='Electricity exports with system Jul', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    surplus_w_sys_ec_aug_tp: Final[Matrix] = OUTPUT(label='Electricity exports with system Aug', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    surplus_w_sys_ec_sep_tp: Final[Matrix] = OUTPUT(label='Electricity exports with system Sep', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    surplus_w_sys_ec_oct_tp: Final[Matrix] = OUTPUT(label='Electricity exports with system Oct', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    surplus_w_sys_ec_nov_tp: Final[Matrix] = OUTPUT(label='Electricity exports with system Nov', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    surplus_w_sys_ec_dec_tp: Final[Matrix] = OUTPUT(label='Electricity exports with system Dec', units='kWh', type='MATRIX', group='Charges by Month', required='*')
    monthly_tou_demand_peak_w_sys: Final[Matrix] = OUTPUT(label='Demand peak with system', units='kW', type='MATRIX', group='Charges by Month', required='*')
    monthly_tou_demand_peak_wo_sys: Final[Matrix] = OUTPUT(label='Demand peak without system', units='kW', type='MATRIX', group='Charges by Month', required='*')
    monthly_tou_demand_charge_w_sys: Final[Matrix] = OUTPUT(label='Demand peak charge with system', units='$', type='MATRIX', group='Charges by Month', required='*')
    monthly_tou_demand_charge_wo_sys: Final[Matrix] = OUTPUT(label='Demand peak charge without system', units='$', type='MATRIX', group='Charges by Month', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 en_electricity_rates: float = ...,
                 analysis_period: float = ...,
                 system_use_lifetime_output: float = ...,
                 TOU_demand_single_peak: float = ...,
                 gen: Array = ...,
                 load: Array = ...,
                 inflation_rate: float = ...,
                 degradation: Array = ...,
                 load_escalation: Array = ...,
                 rate_escalation: Array = ...,
                 ur_metering_option: float = ...,
                 ur_nm_yearend_sell_rate: float = ...,
                 ur_monthly_fixed_charge: float = ...,
                 ur_sell_eq_buy: float = ...,
                 ur_monthly_min_charge: float = ...,
                 ur_annual_min_charge: float = ...,
                 ur_en_ts_sell_rate: float = ...,
                 ur_ts_sell_rate: Array = ...,
                 ur_ec_sched_weekday: Matrix = ...,
                 ur_ec_sched_weekend: Matrix = ...,
                 ur_ec_tou_mat: Matrix = ...,
                 ur_dc_enable: float = ...,
                 ur_dc_sched_weekday: Matrix = ...,
                 ur_dc_sched_weekend: Matrix = ...,
                 ur_dc_tou_mat: Matrix = ...,
                 ur_dc_flat_mat: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
