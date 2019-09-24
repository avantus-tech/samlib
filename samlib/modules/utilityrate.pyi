
# This is a generated file

"""utilityrate - Complex utility rate structure net revenue calculator"""

# VERSION: 3

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
        'e_with_system': Array,
        'p_with_system': Array,
        'e_without_system': Array,
        'p_without_system': Array,
        'system_availability': Array,
        'system_degradation': Array,
        'load_escalation': Array,
        'rate_escalation': Array,
        'ur_sell_eq_buy': float,
        'ur_monthly_fixed_charge': float,
        'ur_flat_buy_rate': float,
        'ur_flat_sell_rate': float,
        'ur_tou_enable': float,
        'ur_tou_p1_buy_rate': float,
        'ur_tou_p1_sell_rate': float,
        'ur_tou_p2_buy_rate': float,
        'ur_tou_p2_sell_rate': float,
        'ur_tou_p3_buy_rate': float,
        'ur_tou_p3_sell_rate': float,
        'ur_tou_p4_buy_rate': float,
        'ur_tou_p4_sell_rate': float,
        'ur_tou_p5_buy_rate': float,
        'ur_tou_p5_sell_rate': float,
        'ur_tou_p6_buy_rate': float,
        'ur_tou_p6_sell_rate': float,
        'ur_tou_p7_buy_rate': float,
        'ur_tou_p7_sell_rate': float,
        'ur_tou_p8_buy_rate': float,
        'ur_tou_p8_sell_rate': float,
        'ur_tou_p9_buy_rate': float,
        'ur_tou_p9_sell_rate': float,
        'ur_tou_sched_weekday': str,
        'ur_tou_sched_weekend': str,
        'ur_dc_enable': float,
        'ur_dc_fixed_m1': float,
        'ur_dc_fixed_m2': float,
        'ur_dc_fixed_m3': float,
        'ur_dc_fixed_m4': float,
        'ur_dc_fixed_m5': float,
        'ur_dc_fixed_m6': float,
        'ur_dc_fixed_m7': float,
        'ur_dc_fixed_m8': float,
        'ur_dc_fixed_m9': float,
        'ur_dc_fixed_m10': float,
        'ur_dc_fixed_m11': float,
        'ur_dc_fixed_m12': float,
        'ur_dc_p1': float,
        'ur_dc_p2': float,
        'ur_dc_p3': float,
        'ur_dc_p4': float,
        'ur_dc_p5': float,
        'ur_dc_p6': float,
        'ur_dc_p7': float,
        'ur_dc_p8': float,
        'ur_dc_p9': float,
        'ur_dc_sched_weekday': str,
        'ur_dc_sched_weekend': str,
        'ur_tr_enable': float,
        'ur_tr_sell_mode': float,
        'ur_tr_sell_rate': float,
        'ur_tr_s1_energy_ub1': float,
        'ur_tr_s1_energy_ub2': float,
        'ur_tr_s1_energy_ub3': float,
        'ur_tr_s1_energy_ub4': float,
        'ur_tr_s1_energy_ub5': float,
        'ur_tr_s1_energy_ub6': float,
        'ur_tr_s1_rate1': float,
        'ur_tr_s1_rate2': float,
        'ur_tr_s1_rate3': float,
        'ur_tr_s1_rate4': float,
        'ur_tr_s1_rate5': float,
        'ur_tr_s1_rate6': float,
        'ur_tr_s2_energy_ub1': float,
        'ur_tr_s2_energy_ub2': float,
        'ur_tr_s2_energy_ub3': float,
        'ur_tr_s2_energy_ub4': float,
        'ur_tr_s2_energy_ub5': float,
        'ur_tr_s2_energy_ub6': float,
        'ur_tr_s2_rate1': float,
        'ur_tr_s2_rate2': float,
        'ur_tr_s2_rate3': float,
        'ur_tr_s2_rate4': float,
        'ur_tr_s2_rate5': float,
        'ur_tr_s2_rate6': float,
        'ur_tr_s3_energy_ub1': float,
        'ur_tr_s3_energy_ub2': float,
        'ur_tr_s3_energy_ub3': float,
        'ur_tr_s3_energy_ub4': float,
        'ur_tr_s3_energy_ub5': float,
        'ur_tr_s3_energy_ub6': float,
        'ur_tr_s3_rate1': float,
        'ur_tr_s3_rate2': float,
        'ur_tr_s3_rate3': float,
        'ur_tr_s3_rate4': float,
        'ur_tr_s3_rate5': float,
        'ur_tr_s3_rate6': float,
        'ur_tr_s4_energy_ub1': float,
        'ur_tr_s4_energy_ub2': float,
        'ur_tr_s4_energy_ub3': float,
        'ur_tr_s4_energy_ub4': float,
        'ur_tr_s4_energy_ub5': float,
        'ur_tr_s4_energy_ub6': float,
        'ur_tr_s4_rate1': float,
        'ur_tr_s4_rate2': float,
        'ur_tr_s4_rate3': float,
        'ur_tr_s4_rate4': float,
        'ur_tr_s4_rate5': float,
        'ur_tr_s4_rate6': float,
        'ur_tr_s5_energy_ub1': float,
        'ur_tr_s5_energy_ub2': float,
        'ur_tr_s5_energy_ub3': float,
        'ur_tr_s5_energy_ub4': float,
        'ur_tr_s5_energy_ub5': float,
        'ur_tr_s5_energy_ub6': float,
        'ur_tr_s5_rate1': float,
        'ur_tr_s5_rate2': float,
        'ur_tr_s5_rate3': float,
        'ur_tr_s5_rate4': float,
        'ur_tr_s5_rate5': float,
        'ur_tr_s5_rate6': float,
        'ur_tr_s6_energy_ub1': float,
        'ur_tr_s6_energy_ub2': float,
        'ur_tr_s6_energy_ub3': float,
        'ur_tr_s6_energy_ub4': float,
        'ur_tr_s6_energy_ub5': float,
        'ur_tr_s6_energy_ub6': float,
        'ur_tr_s6_rate1': float,
        'ur_tr_s6_rate2': float,
        'ur_tr_s6_rate3': float,
        'ur_tr_s6_rate4': float,
        'ur_tr_s6_rate5': float,
        'ur_tr_s6_rate6': float,
        'ur_tr_sched_m1': float,
        'ur_tr_sched_m2': float,
        'ur_tr_sched_m3': float,
        'ur_tr_sched_m4': float,
        'ur_tr_sched_m5': float,
        'ur_tr_sched_m6': float,
        'ur_tr_sched_m7': float,
        'ur_tr_sched_m8': float,
        'ur_tr_sched_m9': float,
        'ur_tr_sched_m10': float,
        'ur_tr_sched_m11': float,
        'ur_tr_sched_m12': float,
        'energy_value': Array,
        'energy_net': Array,
        'revenue_with_system': Array,
        'revenue_without_system': Array,
        'elec_cost_with_system': Array,
        'elec_cost_without_system': Array,
        'year1_hourly_e_grid': Array,
        'year1_hourly_system_output': Array,
        'year1_hourly_e_demand': Array,
        'year1_hourly_system_to_grid': Array,
        'year1_hourly_system_to_load': Array,
        'year1_hourly_p_grid': Array,
        'year1_hourly_p_demand': Array,
        'year1_hourly_p_system_to_load': Array,
        'year1_hourly_revenue_with_system': Array,
        'year1_hourly_payment_with_system': Array,
        'year1_hourly_income_with_system': Array,
        'year1_hourly_price_with_system': Array,
        'year1_hourly_revenue_without_system': Array,
        'year1_hourly_payment_without_system': Array,
        'year1_hourly_income_without_system': Array,
        'year1_hourly_price_without_system': Array,
        'year1_monthly_dc_fixed_with_system': Array,
        'year1_monthly_dc_tou_with_system': Array,
        'year1_monthly_tr_charge_with_system': Array,
        'year1_monthly_tr_rate_with_system': Array,
        'year1_monthly_dc_fixed_without_system': Array,
        'year1_monthly_dc_tou_without_system': Array,
        'year1_monthly_tr_charge_without_system': Array,
        'year1_monthly_tr_rate_without_system': Array,
        'charge_dc_fixed_jan': Array,
        'charge_dc_fixed_feb': Array,
        'charge_dc_fixed_mar': Array,
        'charge_dc_fixed_apr': Array,
        'charge_dc_fixed_may': Array,
        'charge_dc_fixed_jun': Array,
        'charge_dc_fixed_jul': Array,
        'charge_dc_fixed_aug': Array,
        'charge_dc_fixed_sep': Array,
        'charge_dc_fixed_oct': Array,
        'charge_dc_fixed_nov': Array,
        'charge_dc_fixed_dec': Array,
        'charge_dc_tou_jan': Array,
        'charge_dc_tou_feb': Array,
        'charge_dc_tou_mar': Array,
        'charge_dc_tou_apr': Array,
        'charge_dc_tou_may': Array,
        'charge_dc_tou_jun': Array,
        'charge_dc_tou_jul': Array,
        'charge_dc_tou_aug': Array,
        'charge_dc_tou_sep': Array,
        'charge_dc_tou_oct': Array,
        'charge_dc_tou_nov': Array,
        'charge_dc_tou_dec': Array,
        'charge_tr_jan': Array,
        'charge_tr_feb': Array,
        'charge_tr_mar': Array,
        'charge_tr_apr': Array,
        'charge_tr_may': Array,
        'charge_tr_jun': Array,
        'charge_tr_jul': Array,
        'charge_tr_aug': Array,
        'charge_tr_sep': Array,
        'charge_tr_oct': Array,
        'charge_tr_nov': Array,
        'charge_tr_dec': Array
    }, total=False)

class Data(ssc.DataDict):
    analysis_period: float = INPUT(label='Number of years in analysis', units='years', type='NUMBER', required='*', constraints='INTEGER,POSITIVE')
    e_with_system: Array = INPUT(label='Energy at grid with system', units='kWh', type='ARRAY', required='*', constraints='LENGTH=8760')
    p_with_system: Array = INPUT(label='Max power at grid with system', units='kW', type='ARRAY', required='?', constraints='LENGTH=8760')
    e_without_system: Array = INPUT(label='Energy at grid without system (load only)', units='kWh', type='ARRAY', required='?', constraints='LENGTH=8760')
    p_without_system: Array = INPUT(label='Max power at grid without system (load only)', units='kW', type='ARRAY', required='?', constraints='LENGTH=8760')
    system_availability: Array = INPUT(label='Annual availability of system', units='%/year', type='ARRAY', required='?=100')
    system_degradation: Array = INPUT(label='Annual degradation of system', units='%/year', type='ARRAY', required='?=0')
    load_escalation: Array = INPUT(label='Annual load escalation', units='%/year', type='ARRAY', required='?=0')
    rate_escalation: Array = INPUT(label='Annual utility rate escalation', units='%/year', type='ARRAY', required='?=0')
    ur_sell_eq_buy: float = INPUT(label='Force sell rate equal to buy', units='0/1', type='NUMBER', required='?=1', constraints='BOOLEAN', meta='Enforce net metering')
    ur_monthly_fixed_charge: float = INPUT(label='Monthly fixed charge', units='$', type='NUMBER', required='?=0.0')
    ur_flat_buy_rate: float = INPUT(label='Flat rate (buy)', units='$/kWh', type='NUMBER', required='*')
    ur_flat_sell_rate: float = INPUT(label='Flat rate (sell)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_enable: float = INPUT(label='Enable time-of-use rates', units='0/1', type='NUMBER', required='?=0', constraints='BOOLEAN')
    ur_tou_p1_buy_rate: float = INPUT(label='TOU period 1 rate (buy)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p1_sell_rate: float = INPUT(label='TOU period 1 rate (sell)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p2_buy_rate: float = INPUT(label='TOU period 2 rate (buy)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p2_sell_rate: float = INPUT(label='TOU period 2 rate (sell)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p3_buy_rate: float = INPUT(label='TOU period 3 rate (buy)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p3_sell_rate: float = INPUT(label='TOU period 3 rate (sell)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p4_buy_rate: float = INPUT(label='TOU period 4 rate (buy)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p4_sell_rate: float = INPUT(label='TOU period 4 rate (sell)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p5_buy_rate: float = INPUT(label='TOU period 5 rate (buy)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p5_sell_rate: float = INPUT(label='TOU period 5 rate (sell)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p6_buy_rate: float = INPUT(label='TOU period 6 rate (buy)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p6_sell_rate: float = INPUT(label='TOU period 6 rate (sell)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p7_buy_rate: float = INPUT(label='TOU period 7 rate (buy)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p7_sell_rate: float = INPUT(label='TOU period 7 rate (sell)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p8_buy_rate: float = INPUT(label='TOU period 8 rate (buy)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p8_sell_rate: float = INPUT(label='TOU period 8 rate (sell)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p9_buy_rate: float = INPUT(label='TOU period 9 rate (buy)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_p9_sell_rate: float = INPUT(label='TOU period 9 rate (sell)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tou_sched_weekday: str = INPUT(label='TOU weekday schedule', type='STRING', required='ur_tou_enable=1', constraints='TOUSCHED', meta='288 digits 0-9, 24x12')
    ur_tou_sched_weekend: str = INPUT(label='TOU weekend schedule', type='STRING', required='ur_tou_enable=1', constraints='TOUSCHED', meta='288 digits 0-9, 24x12')
    ur_dc_enable: float = INPUT(label='Enable demand charges', units='0/1', type='NUMBER', required='?=0', constraints='BOOLEAN')
    ur_dc_fixed_m1: float = INPUT(label='DC fixed rate January', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_fixed_m2: float = INPUT(label='DC fixed rate February', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_fixed_m3: float = INPUT(label='DC fixed rate March', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_fixed_m4: float = INPUT(label='DC fixed rate April', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_fixed_m5: float = INPUT(label='DC fixed rate May', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_fixed_m6: float = INPUT(label='DC fixed rate June', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_fixed_m7: float = INPUT(label='DC fixed rate July', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_fixed_m8: float = INPUT(label='DC fixed rate August', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_fixed_m9: float = INPUT(label='DC fixed rate September', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_fixed_m10: float = INPUT(label='DC fixed rate October', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_fixed_m11: float = INPUT(label='DC fixed rate November', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_fixed_m12: float = INPUT(label='DC fixed rate December', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_p1: float = INPUT(label='DC TOU rate period 1', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_p2: float = INPUT(label='DC TOU rate period 2', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_p3: float = INPUT(label='DC TOU rate period 3', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_p4: float = INPUT(label='DC TOU rate period 4', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_p5: float = INPUT(label='DC TOU rate period 5', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_p6: float = INPUT(label='DC TOU rate period 6', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_p7: float = INPUT(label='DC TOU rate period 7', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_p8: float = INPUT(label='DC TOU rate period 8', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_p9: float = INPUT(label='DC TOU rate period 9', units='$/kW,pk', type='NUMBER', required='?=0.0')
    ur_dc_sched_weekday: str = INPUT(label='DC TOU weekday schedule', type='STRING', required='ur_dc_enable=1', constraints='TOUSCHED', meta='288 digits 0-9, 24x12')
    ur_dc_sched_weekend: str = INPUT(label='DC TOU weekend schedule', type='STRING', required='ur_dc_enable=1', constraints='TOUSCHED', meta='288 digits 0-9, 24x12')
    ur_tr_enable: float = INPUT(label='Enable tiered rates', units='0/1', type='NUMBER', required='?=0', constraints='BOOLEAN')
    ur_tr_sell_mode: float = INPUT(label='Tiered rate sell mode', units='0,1,2', type='NUMBER', required='?=1', constraints='INTEGER,MIN=0,MAX=2', meta='0=specified,1=tier1,2=lowest')
    ur_tr_sell_rate: float = INPUT(label='Specified tiered sell rate', units='$/kW', type='NUMBER', required='ur_tr_sell_mode=0')
    ur_tr_s1_energy_ub1: float = INPUT(label='Tiered struct. 1 Energy UB 1', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s1_energy_ub2: float = INPUT(label='Tiered struct. 1 Energy UB 2', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s1_energy_ub3: float = INPUT(label='Tiered struct. 1 Energy UB 3', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s1_energy_ub4: float = INPUT(label='Tiered struct. 1 Energy UB 4', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s1_energy_ub5: float = INPUT(label='Tiered struct. 1 Energy UB 5', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s1_energy_ub6: float = INPUT(label='Tiered struct. 1 Energy UB 6', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s1_rate1: float = INPUT(label='Tiered struct. 1 Rate 1', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s1_rate2: float = INPUT(label='Tiered struct. 1 Rate 2', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s1_rate3: float = INPUT(label='Tiered struct. 1 Rate 3', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s1_rate4: float = INPUT(label='Tiered struct. 1 Rate 4', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s1_rate5: float = INPUT(label='Tiered struct. 1 Rate 5', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s1_rate6: float = INPUT(label='Tiered struct. 1 Rate 6', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s2_energy_ub1: float = INPUT(label='Tiered struct. 2 Energy UB 1', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s2_energy_ub2: float = INPUT(label='Tiered struct. 2 Energy UB 2', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s2_energy_ub3: float = INPUT(label='Tiered struct. 2 Energy UB 3', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s2_energy_ub4: float = INPUT(label='Tiered struct. 2 Energy UB 4', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s2_energy_ub5: float = INPUT(label='Tiered struct. 2 Energy UB 5', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s2_energy_ub6: float = INPUT(label='Tiered struct. 2 Energy UB 6', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s2_rate1: float = INPUT(label='Tiered struct. 2 Rate 1', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s2_rate2: float = INPUT(label='Tiered struct. 2 Rate 2', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s2_rate3: float = INPUT(label='Tiered struct. 2 Rate 3', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s2_rate4: float = INPUT(label='Tiered struct. 2 Rate 4', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s2_rate5: float = INPUT(label='Tiered struct. 2 Rate 5', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s2_rate6: float = INPUT(label='Tiered struct. 2 Rate 6', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s3_energy_ub1: float = INPUT(label='Tiered struct. 3 Energy UB 1', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s3_energy_ub2: float = INPUT(label='Tiered struct. 3 Energy UB 2', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s3_energy_ub3: float = INPUT(label='Tiered struct. 3 Energy UB 3', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s3_energy_ub4: float = INPUT(label='Tiered struct. 3 Energy UB 4', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s3_energy_ub5: float = INPUT(label='Tiered struct. 3 Energy UB 5', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s3_energy_ub6: float = INPUT(label='Tiered struct. 3 Energy UB 6', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s3_rate1: float = INPUT(label='Tiered struct. 3 Rate 1', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s3_rate2: float = INPUT(label='Tiered struct. 3 Rate 2', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s3_rate3: float = INPUT(label='Tiered struct. 3 Rate 3', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s3_rate4: float = INPUT(label='Tiered struct. 3 Rate 4', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s3_rate5: float = INPUT(label='Tiered struct. 3 Rate 5', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s3_rate6: float = INPUT(label='Tiered struct. 3 Rate 6', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s4_energy_ub1: float = INPUT(label='Tiered struct. 4 Energy UB 1', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s4_energy_ub2: float = INPUT(label='Tiered struct. 4 Energy UB 2', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s4_energy_ub3: float = INPUT(label='Tiered struct. 4 Energy UB 3', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s4_energy_ub4: float = INPUT(label='Tiered struct. 4 Energy UB 4', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s4_energy_ub5: float = INPUT(label='Tiered struct. 4 Energy UB 5', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s4_energy_ub6: float = INPUT(label='Tiered struct. 4 Energy UB 6', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s4_rate1: float = INPUT(label='Tiered struct. 4 Rate 1', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s4_rate2: float = INPUT(label='Tiered struct. 4 Rate 2', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s4_rate3: float = INPUT(label='Tiered struct. 4 Rate 3', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s4_rate4: float = INPUT(label='Tiered struct. 4 Rate 4', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s4_rate5: float = INPUT(label='Tiered struct. 4 Rate 5', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s4_rate6: float = INPUT(label='Tiered struct. 4 Rate 6', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s5_energy_ub1: float = INPUT(label='Tiered struct. 5 Energy UB 1', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s5_energy_ub2: float = INPUT(label='Tiered struct. 5 Energy UB 2', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s5_energy_ub3: float = INPUT(label='Tiered struct. 5 Energy UB 3', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s5_energy_ub4: float = INPUT(label='Tiered struct. 5 Energy UB 4', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s5_energy_ub5: float = INPUT(label='Tiered struct. 5 Energy UB 5', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s5_energy_ub6: float = INPUT(label='Tiered struct. 5 Energy UB 6', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s5_rate1: float = INPUT(label='Tiered struct. 5 Rate 1', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s5_rate2: float = INPUT(label='Tiered struct. 5 Rate 2', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s5_rate3: float = INPUT(label='Tiered struct. 5 Rate 3', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s5_rate4: float = INPUT(label='Tiered struct. 5 Rate 4', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s5_rate5: float = INPUT(label='Tiered struct. 5 Rate 5', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s5_rate6: float = INPUT(label='Tiered struct. 5 Rate 6', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s6_energy_ub1: float = INPUT(label='Tiered struct. 6 Energy UB 1', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s6_energy_ub2: float = INPUT(label='Tiered struct. 6 Energy UB 2', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s6_energy_ub3: float = INPUT(label='Tiered struct. 6 Energy UB 3', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s6_energy_ub4: float = INPUT(label='Tiered struct. 6 Energy UB 4', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s6_energy_ub5: float = INPUT(label='Tiered struct. 6 Energy UB 5', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s6_energy_ub6: float = INPUT(label='Tiered struct. 6 Energy UB 6', units='kWh', type='NUMBER', required='?=1e99')
    ur_tr_s6_rate1: float = INPUT(label='Tiered struct. 6 Rate 1', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s6_rate2: float = INPUT(label='Tiered struct. 6 Rate 2', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s6_rate3: float = INPUT(label='Tiered struct. 6 Rate 3', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s6_rate4: float = INPUT(label='Tiered struct. 6 Rate 4', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s6_rate5: float = INPUT(label='Tiered struct. 6 Rate 5', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_s6_rate6: float = INPUT(label='Tiered struct. 6 Rate 6', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_tr_sched_m1: float = INPUT(label='Tiered structure for January', units='0-5', type='NUMBER', required='?=0', constraints='INTEGER,MIN=0,MAX=5', meta='tiered structure #')
    ur_tr_sched_m2: float = INPUT(label='Tiered structure for February', units='0-5', type='NUMBER', required='?=0', constraints='INTEGER,MIN=0,MAX=5', meta='tiered structure #')
    ur_tr_sched_m3: float = INPUT(label='Tiered structure for March', units='0-5', type='NUMBER', required='?=0', constraints='INTEGER,MIN=0,MAX=5', meta='tiered structure #')
    ur_tr_sched_m4: float = INPUT(label='Tiered structure for April', units='0-5', type='NUMBER', required='?=0', constraints='INTEGER,MIN=0,MAX=5', meta='tiered structure #')
    ur_tr_sched_m5: float = INPUT(label='Tiered structure for May', units='0-5', type='NUMBER', required='?=0', constraints='INTEGER,MIN=0,MAX=5', meta='tiered structure #')
    ur_tr_sched_m6: float = INPUT(label='Tiered structure for June', units='0-5', type='NUMBER', required='?=0', constraints='INTEGER,MIN=0,MAX=5', meta='tiered structure #')
    ur_tr_sched_m7: float = INPUT(label='Tiered structure for July', units='0-5', type='NUMBER', required='?=0', constraints='INTEGER,MIN=0,MAX=5', meta='tiered structure #')
    ur_tr_sched_m8: float = INPUT(label='Tiered structure for August', units='0-5', type='NUMBER', required='?=0', constraints='INTEGER,MIN=0,MAX=5', meta='tiered structure #')
    ur_tr_sched_m9: float = INPUT(label='Tiered structure for September', units='0-5', type='NUMBER', required='?=0', constraints='INTEGER,MIN=0,MAX=5', meta='tiered structure #')
    ur_tr_sched_m10: float = INPUT(label='Tiered structure for October', units='0-5', type='NUMBER', required='?=0', constraints='INTEGER,MIN=0,MAX=5', meta='tiered structure #')
    ur_tr_sched_m11: float = INPUT(label='Tiered structure for November', units='0-5', type='NUMBER', required='?=0', constraints='INTEGER,MIN=0,MAX=5', meta='tiered structure #')
    ur_tr_sched_m12: float = INPUT(label='Tiered structure for December', units='0-5', type='NUMBER', required='?=0', constraints='INTEGER,MIN=0,MAX=5', meta='tiered structure #')
    energy_value: Final[Array] = OUTPUT(label='Energy value by each year', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    energy_net: Final[Array] = OUTPUT(label='Energy by each year', units='kW', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    revenue_with_system: Final[Array] = OUTPUT(label='Total revenue with system', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    revenue_without_system: Final[Array] = OUTPUT(label='Total revenue without system', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    elec_cost_with_system: Final[Array] = OUTPUT(label='Electricity cost with system', units='$/yr', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    elec_cost_without_system: Final[Array] = OUTPUT(label='Electricity cost without system', units='$/yr', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    year1_hourly_e_grid: Final[Array] = OUTPUT(label='Electricity at grid', units='kWh', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_system_output: Final[Array] = OUTPUT(label='Electricity from system', units='kWh', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_e_demand: Final[Array] = OUTPUT(label='Electricity from grid', units='kWh', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_system_to_grid: Final[Array] = OUTPUT(label='Electricity to grid', units='kWh', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_system_to_load: Final[Array] = OUTPUT(label='Electricity to load', units='kWh', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_p_grid: Final[Array] = OUTPUT(label='Peak at grid ', units='kW', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_p_demand: Final[Array] = OUTPUT(label='Peak from grid', units='kW', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_p_system_to_load: Final[Array] = OUTPUT(label='Peak to load ', units='kW', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_revenue_with_system: Final[Array] = OUTPUT(label='Revenue with system', units='$', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_payment_with_system: Final[Array] = OUTPUT(label='Payment with system', units='$', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_income_with_system: Final[Array] = OUTPUT(label='Income with system', units='$', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_price_with_system: Final[Array] = OUTPUT(label='Price with system', units='$', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_revenue_without_system: Final[Array] = OUTPUT(label='Revenue without system', units='$', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_payment_without_system: Final[Array] = OUTPUT(label='Payment without system', units='$', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_income_without_system: Final[Array] = OUTPUT(label='Income without system', units='$', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_price_without_system: Final[Array] = OUTPUT(label='Price without system', units='$', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_monthly_dc_fixed_with_system: Final[Array] = OUTPUT(label='Demand charge (fixed) with system', units='$', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_dc_tou_with_system: Final[Array] = OUTPUT(label='Demand charge (TOU) with system', units='$', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_tr_charge_with_system: Final[Array] = OUTPUT(label='Tiered charge with system', units='$', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_tr_rate_with_system: Final[Array] = OUTPUT(label='Tiered rate with system', units='$', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_dc_fixed_without_system: Final[Array] = OUTPUT(label='Demand charge (fixed) without system', units='$', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_dc_tou_without_system: Final[Array] = OUTPUT(label='Demand charge (TOU) without system', units='$', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_tr_charge_without_system: Final[Array] = OUTPUT(label='Tiered charge without system', units='$', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_tr_rate_without_system: Final[Array] = OUTPUT(label='Tiered rate without system', units='$', type='ARRAY', required='*', constraints='LENGTH=12')
    charge_dc_fixed_jan: Final[Array] = OUTPUT(label='Demand charge (fixed) in Jan', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_feb: Final[Array] = OUTPUT(label='Demand charge (fixed) in Feb', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_mar: Final[Array] = OUTPUT(label='Demand charge (fixed) in Mar', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_apr: Final[Array] = OUTPUT(label='Demand charge (fixed) in Apr', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_may: Final[Array] = OUTPUT(label='Demand charge (fixed) in May', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_jun: Final[Array] = OUTPUT(label='Demand charge (fixed) in Jun', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_jul: Final[Array] = OUTPUT(label='Demand charge (fixed) in Jul', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_aug: Final[Array] = OUTPUT(label='Demand charge (fixed) in Aug', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_sep: Final[Array] = OUTPUT(label='Demand charge (fixed) in Sep', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_oct: Final[Array] = OUTPUT(label='Demand charge (fixed) in Oct', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_nov: Final[Array] = OUTPUT(label='Demand charge (fixed) in Nov', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_dec: Final[Array] = OUTPUT(label='Demand charge (fixed) in Dec', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_jan: Final[Array] = OUTPUT(label='Demand charge (TOU) in Jan', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_feb: Final[Array] = OUTPUT(label='Demand charge (TOU) in Feb', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_mar: Final[Array] = OUTPUT(label='Demand charge (TOU) in Mar', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_apr: Final[Array] = OUTPUT(label='Demand charge (TOU) in Apr', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_may: Final[Array] = OUTPUT(label='Demand charge (TOU) in May', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_jun: Final[Array] = OUTPUT(label='Demand charge (TOU) in Jun', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_jul: Final[Array] = OUTPUT(label='Demand charge (TOU) in Jul', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_aug: Final[Array] = OUTPUT(label='Demand charge (TOU) in Aug', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_sep: Final[Array] = OUTPUT(label='Demand charge (TOU) in Sep', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_oct: Final[Array] = OUTPUT(label='Demand charge (TOU) in Oct', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_nov: Final[Array] = OUTPUT(label='Demand charge (TOU) in Nov', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_dec: Final[Array] = OUTPUT(label='Demand charge (TOU) in Dec', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_tr_jan: Final[Array] = OUTPUT(label='Tiered rate charge in Jan', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_tr_feb: Final[Array] = OUTPUT(label='Tiered rate charge in Feb', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_tr_mar: Final[Array] = OUTPUT(label='Tiered rate charge in Mar', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_tr_apr: Final[Array] = OUTPUT(label='Tiered rate charge in Apr', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_tr_may: Final[Array] = OUTPUT(label='Tiered rate charge in May', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_tr_jun: Final[Array] = OUTPUT(label='Tiered rate charge in Jun', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_tr_jul: Final[Array] = OUTPUT(label='Tiered rate charge in Jul', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_tr_aug: Final[Array] = OUTPUT(label='Tiered rate charge in Aug', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_tr_sep: Final[Array] = OUTPUT(label='Tiered rate charge in Sep', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_tr_oct: Final[Array] = OUTPUT(label='Tiered rate charge in Oct', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_tr_nov: Final[Array] = OUTPUT(label='Tiered rate charge in Nov', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_tr_dec: Final[Array] = OUTPUT(label='Tiered rate charge in Dec', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')

    def __init__(self, *args: Mapping[str, Any],
                 analysis_period: float = ...,
                 e_with_system: Array = ...,
                 p_with_system: Array = ...,
                 e_without_system: Array = ...,
                 p_without_system: Array = ...,
                 system_availability: Array = ...,
                 system_degradation: Array = ...,
                 load_escalation: Array = ...,
                 rate_escalation: Array = ...,
                 ur_sell_eq_buy: float = ...,
                 ur_monthly_fixed_charge: float = ...,
                 ur_flat_buy_rate: float = ...,
                 ur_flat_sell_rate: float = ...,
                 ur_tou_enable: float = ...,
                 ur_tou_p1_buy_rate: float = ...,
                 ur_tou_p1_sell_rate: float = ...,
                 ur_tou_p2_buy_rate: float = ...,
                 ur_tou_p2_sell_rate: float = ...,
                 ur_tou_p3_buy_rate: float = ...,
                 ur_tou_p3_sell_rate: float = ...,
                 ur_tou_p4_buy_rate: float = ...,
                 ur_tou_p4_sell_rate: float = ...,
                 ur_tou_p5_buy_rate: float = ...,
                 ur_tou_p5_sell_rate: float = ...,
                 ur_tou_p6_buy_rate: float = ...,
                 ur_tou_p6_sell_rate: float = ...,
                 ur_tou_p7_buy_rate: float = ...,
                 ur_tou_p7_sell_rate: float = ...,
                 ur_tou_p8_buy_rate: float = ...,
                 ur_tou_p8_sell_rate: float = ...,
                 ur_tou_p9_buy_rate: float = ...,
                 ur_tou_p9_sell_rate: float = ...,
                 ur_tou_sched_weekday: str = ...,
                 ur_tou_sched_weekend: str = ...,
                 ur_dc_enable: float = ...,
                 ur_dc_fixed_m1: float = ...,
                 ur_dc_fixed_m2: float = ...,
                 ur_dc_fixed_m3: float = ...,
                 ur_dc_fixed_m4: float = ...,
                 ur_dc_fixed_m5: float = ...,
                 ur_dc_fixed_m6: float = ...,
                 ur_dc_fixed_m7: float = ...,
                 ur_dc_fixed_m8: float = ...,
                 ur_dc_fixed_m9: float = ...,
                 ur_dc_fixed_m10: float = ...,
                 ur_dc_fixed_m11: float = ...,
                 ur_dc_fixed_m12: float = ...,
                 ur_dc_p1: float = ...,
                 ur_dc_p2: float = ...,
                 ur_dc_p3: float = ...,
                 ur_dc_p4: float = ...,
                 ur_dc_p5: float = ...,
                 ur_dc_p6: float = ...,
                 ur_dc_p7: float = ...,
                 ur_dc_p8: float = ...,
                 ur_dc_p9: float = ...,
                 ur_dc_sched_weekday: str = ...,
                 ur_dc_sched_weekend: str = ...,
                 ur_tr_enable: float = ...,
                 ur_tr_sell_mode: float = ...,
                 ur_tr_sell_rate: float = ...,
                 ur_tr_s1_energy_ub1: float = ...,
                 ur_tr_s1_energy_ub2: float = ...,
                 ur_tr_s1_energy_ub3: float = ...,
                 ur_tr_s1_energy_ub4: float = ...,
                 ur_tr_s1_energy_ub5: float = ...,
                 ur_tr_s1_energy_ub6: float = ...,
                 ur_tr_s1_rate1: float = ...,
                 ur_tr_s1_rate2: float = ...,
                 ur_tr_s1_rate3: float = ...,
                 ur_tr_s1_rate4: float = ...,
                 ur_tr_s1_rate5: float = ...,
                 ur_tr_s1_rate6: float = ...,
                 ur_tr_s2_energy_ub1: float = ...,
                 ur_tr_s2_energy_ub2: float = ...,
                 ur_tr_s2_energy_ub3: float = ...,
                 ur_tr_s2_energy_ub4: float = ...,
                 ur_tr_s2_energy_ub5: float = ...,
                 ur_tr_s2_energy_ub6: float = ...,
                 ur_tr_s2_rate1: float = ...,
                 ur_tr_s2_rate2: float = ...,
                 ur_tr_s2_rate3: float = ...,
                 ur_tr_s2_rate4: float = ...,
                 ur_tr_s2_rate5: float = ...,
                 ur_tr_s2_rate6: float = ...,
                 ur_tr_s3_energy_ub1: float = ...,
                 ur_tr_s3_energy_ub2: float = ...,
                 ur_tr_s3_energy_ub3: float = ...,
                 ur_tr_s3_energy_ub4: float = ...,
                 ur_tr_s3_energy_ub5: float = ...,
                 ur_tr_s3_energy_ub6: float = ...,
                 ur_tr_s3_rate1: float = ...,
                 ur_tr_s3_rate2: float = ...,
                 ur_tr_s3_rate3: float = ...,
                 ur_tr_s3_rate4: float = ...,
                 ur_tr_s3_rate5: float = ...,
                 ur_tr_s3_rate6: float = ...,
                 ur_tr_s4_energy_ub1: float = ...,
                 ur_tr_s4_energy_ub2: float = ...,
                 ur_tr_s4_energy_ub3: float = ...,
                 ur_tr_s4_energy_ub4: float = ...,
                 ur_tr_s4_energy_ub5: float = ...,
                 ur_tr_s4_energy_ub6: float = ...,
                 ur_tr_s4_rate1: float = ...,
                 ur_tr_s4_rate2: float = ...,
                 ur_tr_s4_rate3: float = ...,
                 ur_tr_s4_rate4: float = ...,
                 ur_tr_s4_rate5: float = ...,
                 ur_tr_s4_rate6: float = ...,
                 ur_tr_s5_energy_ub1: float = ...,
                 ur_tr_s5_energy_ub2: float = ...,
                 ur_tr_s5_energy_ub3: float = ...,
                 ur_tr_s5_energy_ub4: float = ...,
                 ur_tr_s5_energy_ub5: float = ...,
                 ur_tr_s5_energy_ub6: float = ...,
                 ur_tr_s5_rate1: float = ...,
                 ur_tr_s5_rate2: float = ...,
                 ur_tr_s5_rate3: float = ...,
                 ur_tr_s5_rate4: float = ...,
                 ur_tr_s5_rate5: float = ...,
                 ur_tr_s5_rate6: float = ...,
                 ur_tr_s6_energy_ub1: float = ...,
                 ur_tr_s6_energy_ub2: float = ...,
                 ur_tr_s6_energy_ub3: float = ...,
                 ur_tr_s6_energy_ub4: float = ...,
                 ur_tr_s6_energy_ub5: float = ...,
                 ur_tr_s6_energy_ub6: float = ...,
                 ur_tr_s6_rate1: float = ...,
                 ur_tr_s6_rate2: float = ...,
                 ur_tr_s6_rate3: float = ...,
                 ur_tr_s6_rate4: float = ...,
                 ur_tr_s6_rate5: float = ...,
                 ur_tr_s6_rate6: float = ...,
                 ur_tr_sched_m1: float = ...,
                 ur_tr_sched_m2: float = ...,
                 ur_tr_sched_m3: float = ...,
                 ur_tr_sched_m4: float = ...,
                 ur_tr_sched_m5: float = ...,
                 ur_tr_sched_m6: float = ...,
                 ur_tr_sched_m7: float = ...,
                 ur_tr_sched_m8: float = ...,
                 ur_tr_sched_m9: float = ...,
                 ur_tr_sched_m10: float = ...,
                 ur_tr_sched_m11: float = ...,
                 ur_tr_sched_m12: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
