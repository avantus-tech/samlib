
# This is a generated file

"""cashloan - Residential/Commerical Finance model."""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'analysis_period': float,
        'federal_tax_rate': Array,
        'state_tax_rate': Array,
        'cf_federal_tax_frac': Array,
        'cf_state_tax_frac': Array,
        'cf_effective_tax_frac': Array,
        'property_tax_rate': float,
        'prop_tax_cost_assessed_percent': float,
        'prop_tax_assessed_decline': float,
        'real_discount_rate': float,
        'inflation_rate': float,
        'insurance_rate': float,
        'system_capacity': float,
        'system_heat_rate': float,
        'loan_term': float,
        'loan_rate': float,
        'debt_fraction': float,
        'om_fixed': Array,
        'om_fixed_escal': float,
        'om_production': Array,
        'om_production_escal': float,
        'om_capacity': Array,
        'om_capacity_escal': float,
        'om_fuel_cost': Array,
        'om_fuel_cost_escal': float,
        'annual_fuel_usage': float,
        'annual_fuel_usage_lifetime': Array,
        'om_replacement_cost1': Array,
        'om_replacement_cost2': Array,
        'om_replacement_cost_escal': float,
        'om_opt_fuel_1_usage': float,
        'om_opt_fuel_1_cost': Array,
        'om_opt_fuel_1_cost_escal': float,
        'om_opt_fuel_2_usage': float,
        'om_opt_fuel_2_cost': Array,
        'om_opt_fuel_2_cost_escal': float,
        'add_om_num_types': float,
        'om_capacity1_nameplate': float,
        'om_production1_values': Array,
        'om_fixed1': Array,
        'om_production1': Array,
        'om_capacity1': Array,
        'om_capacity2_nameplate': float,
        'om_production2_values': Array,
        'om_fixed2': Array,
        'om_production2': Array,
        'om_capacity2': Array,
        'depr_fed_type': float,
        'depr_fed_sl_years': float,
        'depr_fed_custom': Array,
        'depr_sta_type': float,
        'depr_sta_sl_years': float,
        'depr_sta_custom': Array,
        'itc_fed_amount': float,
        'itc_fed_amount_deprbas_fed': float,
        'itc_fed_amount_deprbas_sta': float,
        'itc_sta_amount': float,
        'itc_sta_amount_deprbas_fed': float,
        'itc_sta_amount_deprbas_sta': float,
        'itc_fed_percent': float,
        'itc_fed_percent_maxvalue': float,
        'itc_fed_percent_deprbas_fed': float,
        'itc_fed_percent_deprbas_sta': float,
        'itc_sta_percent': float,
        'itc_sta_percent_maxvalue': float,
        'itc_sta_percent_deprbas_fed': float,
        'itc_sta_percent_deprbas_sta': float,
        'ptc_fed_amount': Array,
        'ptc_fed_term': float,
        'ptc_fed_escal': float,
        'ptc_sta_amount': Array,
        'ptc_sta_term': float,
        'ptc_sta_escal': float,
        'ibi_fed_amount': float,
        'ibi_fed_amount_tax_fed': float,
        'ibi_fed_amount_tax_sta': float,
        'ibi_fed_amount_deprbas_fed': float,
        'ibi_fed_amount_deprbas_sta': float,
        'ibi_sta_amount': float,
        'ibi_sta_amount_tax_fed': float,
        'ibi_sta_amount_tax_sta': float,
        'ibi_sta_amount_deprbas_fed': float,
        'ibi_sta_amount_deprbas_sta': float,
        'ibi_uti_amount': float,
        'ibi_uti_amount_tax_fed': float,
        'ibi_uti_amount_tax_sta': float,
        'ibi_uti_amount_deprbas_fed': float,
        'ibi_uti_amount_deprbas_sta': float,
        'ibi_oth_amount': float,
        'ibi_oth_amount_tax_fed': float,
        'ibi_oth_amount_tax_sta': float,
        'ibi_oth_amount_deprbas_fed': float,
        'ibi_oth_amount_deprbas_sta': float,
        'ibi_fed_percent': float,
        'ibi_fed_percent_maxvalue': float,
        'ibi_fed_percent_tax_fed': float,
        'ibi_fed_percent_tax_sta': float,
        'ibi_fed_percent_deprbas_fed': float,
        'ibi_fed_percent_deprbas_sta': float,
        'ibi_sta_percent': float,
        'ibi_sta_percent_maxvalue': float,
        'ibi_sta_percent_tax_fed': float,
        'ibi_sta_percent_tax_sta': float,
        'ibi_sta_percent_deprbas_fed': float,
        'ibi_sta_percent_deprbas_sta': float,
        'ibi_uti_percent': float,
        'ibi_uti_percent_maxvalue': float,
        'ibi_uti_percent_tax_fed': float,
        'ibi_uti_percent_tax_sta': float,
        'ibi_uti_percent_deprbas_fed': float,
        'ibi_uti_percent_deprbas_sta': float,
        'ibi_oth_percent': float,
        'ibi_oth_percent_maxvalue': float,
        'ibi_oth_percent_tax_fed': float,
        'ibi_oth_percent_tax_sta': float,
        'ibi_oth_percent_deprbas_fed': float,
        'ibi_oth_percent_deprbas_sta': float,
        'cbi_fed_amount': float,
        'cbi_fed_maxvalue': float,
        'cbi_fed_tax_fed': float,
        'cbi_fed_tax_sta': float,
        'cbi_fed_deprbas_fed': float,
        'cbi_fed_deprbas_sta': float,
        'cbi_sta_amount': float,
        'cbi_sta_maxvalue': float,
        'cbi_sta_tax_fed': float,
        'cbi_sta_tax_sta': float,
        'cbi_sta_deprbas_fed': float,
        'cbi_sta_deprbas_sta': float,
        'cbi_uti_amount': float,
        'cbi_uti_maxvalue': float,
        'cbi_uti_tax_fed': float,
        'cbi_uti_tax_sta': float,
        'cbi_uti_deprbas_fed': float,
        'cbi_uti_deprbas_sta': float,
        'cbi_oth_amount': float,
        'cbi_oth_maxvalue': float,
        'cbi_oth_tax_fed': float,
        'cbi_oth_tax_sta': float,
        'cbi_oth_deprbas_fed': float,
        'cbi_oth_deprbas_sta': float,
        'pbi_fed_amount': Array,
        'pbi_fed_term': float,
        'pbi_fed_escal': float,
        'pbi_fed_tax_fed': float,
        'pbi_fed_tax_sta': float,
        'pbi_sta_amount': Array,
        'pbi_sta_term': float,
        'pbi_sta_escal': float,
        'pbi_sta_tax_fed': float,
        'pbi_sta_tax_sta': float,
        'pbi_uti_amount': Array,
        'pbi_uti_term': float,
        'pbi_uti_escal': float,
        'pbi_uti_tax_fed': float,
        'pbi_uti_tax_sta': float,
        'pbi_oth_amount': Array,
        'pbi_oth_term': float,
        'pbi_oth_escal': float,
        'pbi_oth_tax_fed': float,
        'pbi_oth_tax_sta': float,
        'cbi_total_fed': float,
        'cbi_total_sta': float,
        'cbi_total_oth': float,
        'cbi_total_uti': float,
        'cbi_total': float,
        'cbi_statax_total': float,
        'cbi_fedtax_total': float,
        'ibi_total_fed': float,
        'ibi_total_sta': float,
        'ibi_total_oth': float,
        'ibi_total_uti': float,
        'ibi_total': float,
        'ibi_statax_total': float,
        'ibi_fedtax_total': float,
        'cf_pbi_total_fed': Array,
        'cf_pbi_total_sta': Array,
        'cf_pbi_total_oth': Array,
        'cf_pbi_total_uti': Array,
        'cf_pbi_total': Array,
        'cf_pbi_statax_total': Array,
        'cf_pbi_fedtax_total': Array,
        'itc_total_fed': float,
        'itc_total_sta': float,
        'itc_total': float,
        'cf_ptc_fed': Array,
        'cf_ptc_sta': Array,
        'cf_ptc_total': Array,
        'en_batt': float,
        'batt_bank_replacement': Array,
        'batt_replacement_schedule': Array,
        'batt_replacement_option': float,
        'battery_per_kWh': float,
        'batt_computed_bank_capacity': float,
        'cf_battery_replacement_cost': Array,
        'cf_battery_replacement_cost_schedule': Array,
        'fuelcell_replacement': Array,
        'fuelcell_replacement_schedule': Array,
        'en_fuelcell': float,
        'fuelcell_replacement_option': float,
        'fuelcell_per_kWh': float,
        'fuelcell_computed_bank_capacity': float,
        'cf_fuelcell_replacement_cost': Array,
        'cf_fuelcell_replacement_cost_schedule': Array,
        'market': float,
        'mortgage': float,
        'total_installed_cost': float,
        'salvage_percentage': float,
        'annual_energy_value': Array,
        'annual_themal_value': Array,
        'gen': Array,
        'degradation': Array,
        'system_use_lifetime_output': float,
        'cf_length': float,
        'lcoe_real': float,
        'lcoe_nom': float,
        'payback': float,
        'discounted_payback': float,
        'npv': float,
        'present_value_oandm': float,
        'present_value_oandm_nonfuel': float,
        'present_value_fuel': float,
        'present_value_insandproptax': float,
        'adjusted_installed_cost': float,
        'loan_amount': float,
        'first_cost': float,
        'total_cost': float,
        'cf_energy_net': Array,
        'cf_energy_value': Array,
        'cf_thermal_value': Array,
        'cf_value_added': Array,
        'cf_om_fixed_expense': Array,
        'cf_om_production_expense': Array,
        'cf_om_capacity_expense': Array,
        'cf_om_fixed1_expense': Array,
        'cf_om_production1_expense': Array,
        'cf_om_capacity1_expense': Array,
        'cf_om_fixed2_expense': Array,
        'cf_om_production2_expense': Array,
        'cf_om_capacity2_expense': Array,
        'cf_om_fuel_expense': Array,
        'cf_om_opt_fuel_1_expense': Array,
        'cf_om_opt_fuel_2_expense': Array,
        'cf_property_tax_assessed_value': Array,
        'cf_property_tax_expense': Array,
        'cf_insurance_expense': Array,
        'cf_net_salvage_value': Array,
        'cf_operating_expenses': Array,
        'cf_deductible_expenses': Array,
        'cf_debt_balance': Array,
        'cf_debt_payment_interest': Array,
        'cf_debt_payment_principal': Array,
        'cf_debt_payment_total': Array,
        'cf_sta_depr_sched': Array,
        'cf_sta_depreciation': Array,
        'cf_sta_incentive_income_less_deductions': Array,
        'cf_sta_taxable_income_less_deductions': Array,
        'cf_sta_tax_savings': Array,
        'cf_sta_taxable_incentive_income': Array,
        'cf_fed_taxable_incentive_income': Array,
        'cf_fed_depr_sched': Array,
        'cf_fed_depreciation': Array,
        'cf_fed_incentive_income_less_deductions': Array,
        'cf_fed_taxable_income_less_deductions': Array,
        'cf_fed_tax_savings': Array,
        'cf_sta_and_fed_tax_savings': Array,
        'cf_after_tax_net_equity_cost_flow': Array,
        'cf_after_tax_cash_flow': Array,
        'cf_discounted_costs': Array,
        'cf_discounted_savings': Array,
        'cf_discounted_payback': Array,
        'cf_discounted_cumulative_payback': Array,
        'cf_payback_with_expenses': Array,
        'cf_cumulative_payback_with_expenses': Array,
        'cf_payback_without_expenses': Array,
        'cf_cumulative_payback_without_expenses': Array,
        'lcoptc_fed_real': float,
        'lcoptc_fed_nom': float,
        'lcoptc_sta_real': float,
        'lcoptc_sta_nom': float,
        'wacc': float,
        'effective_tax_rate': float,
        'elec_cost_with_system': Array,
        'elec_cost_without_system': Array,
        'cf_nte': Array,
        'year1_nte': float,
        'lnte_real': float,
        'lnte_nom': float
}, total=False)

class Data(ssc.DataDict):
    analysis_period: float = INPUT(label='Analyis period', units='years', type='NUMBER', group='Financial Parameters', required='?=30', constraints='INTEGER,MIN=0,MAX=50')
    federal_tax_rate: Array = INPUT(label='Federal income tax rate', units='%', type='ARRAY', group='Financial Parameters', required='*')
    state_tax_rate: Array = INPUT(label='State income tax rate', units='%', type='ARRAY', group='Financial Parameters', required='*')
    cf_federal_tax_frac: Final[Array] = OUTPUT(label='Federal income tax rate', units='frac', type='ARRAY', group='Financial Parameters', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_state_tax_frac: Final[Array] = OUTPUT(label='State income tax rate', units='frac', type='ARRAY', group='Financial Parameters', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_effective_tax_frac: Final[Array] = OUTPUT(label='Effective income tax rate', units='frac', type='ARRAY', group='Financial Parameters', required='*', constraints='LENGTH_EQUAL=cf_length')
    property_tax_rate: float = INPUT(label='Property tax rate', units='%', type='NUMBER', group='Financial Parameters', required='?=0.0', constraints='MIN=0,MAX=100')
    prop_tax_cost_assessed_percent: float = INPUT(label='Percent of pre-financing costs assessed', units='%', type='NUMBER', group='Financial Parameters', required='?=95', constraints='MIN=0,MAX=100')
    prop_tax_assessed_decline: float = INPUT(label='Assessed value annual decline', units='%', type='NUMBER', group='Financial Parameters', required='?=5', constraints='MIN=0,MAX=100')
    real_discount_rate: float = INPUT(label='Real discount rate', units='%', type='NUMBER', group='Financial Parameters', required='*', constraints='MIN=-99')
    inflation_rate: float = INPUT(label='Inflation rate', units='%', type='NUMBER', group='Financial Parameters', required='*', constraints='MIN=-99')
    insurance_rate: float = INPUT(label='Insurance rate', units='%', type='NUMBER', group='Financial Parameters', required='?=0.0', constraints='MIN=0,MAX=100')
    system_capacity: float = INPUT(label='System nameplate capacity', units='kW', type='NUMBER', group='Financial Parameters', required='*', constraints='POSITIVE')
    system_heat_rate: float = INPUT(label='System heat rate', units='MMBTus/MWh', type='NUMBER', group='Financial Parameters', required='?=0.0', constraints='MIN=0')
    loan_term: float = INPUT(label='Loan term', units='years', type='NUMBER', group='Financial Parameters', required='?=0', constraints='INTEGER,MIN=0,MAX=50')
    loan_rate: float = INPUT(label='Loan rate', units='%', type='NUMBER', group='Financial Parameters', required='?=0', constraints='MIN=0,MAX=100')
    debt_fraction: float = INPUT(label='Debt percentage', units='%', type='NUMBER', group='Financial Parameters', required='?=0', constraints='MIN=0,MAX=100')
    om_fixed: Array = INPUT(label='Fixed O&M annual amount', units='$/year', type='ARRAY', group='System Costs', required='?=0.0')
    om_fixed_escal: float = INPUT(label='Fixed O&M escalation', units='%/year', type='NUMBER', group='System Costs', required='?=0.0')
    om_production: Array = INPUT(label='Production-based O&M amount', units='$/MWh', type='ARRAY', group='System Costs', required='?=0.0')
    om_production_escal: float = INPUT(label='Production-based O&M escalation', units='%/year', type='NUMBER', group='System Costs', required='?=0.0')
    om_capacity: Array = INPUT(label='Capacity-based O&M amount', units='$/kWcap', type='ARRAY', group='System Costs', required='?=0.0')
    om_capacity_escal: float = INPUT(label='Capacity-based O&M escalation', units='%/year', type='NUMBER', group='System Costs', required='?=0.0')
    om_fuel_cost: Array = INPUT(label='Fuel cost', units='$/MMBtu', type='ARRAY', group='System Costs', required='?=0.0')
    om_fuel_cost_escal: float = INPUT(label='Fuel cost escalation', units='%/year', type='NUMBER', group='System Costs', required='?=0.0')
    annual_fuel_usage: float = INPUT(label='Fuel usage (yr 1)', units='kWht', type='NUMBER', group='System Costs', required='?=0', constraints='MIN=0')
    annual_fuel_usage_lifetime: Array = INPUT(label='Fuel usage (lifetime)', units='kWht', type='ARRAY', group='System Costs')
    om_replacement_cost1: Array = INPUT(label='Replacement cost 1', units='$/kWh', type='ARRAY', group='System Costs', required='?=0.0')
    om_replacement_cost2: Array = INPUT(label='Replacement cost 2', units='$/kW', type='ARRAY', group='System Costs', required='?=0.0')
    om_replacement_cost_escal: float = INPUT(label='Replacement cost escalation', units='%/year', type='NUMBER', group='System Costs', required='?=0.0')
    om_opt_fuel_1_usage: float = INPUT(label='Biomass feedstock usage', units='unit', type='NUMBER', group='System Costs', required='?=0.0')
    om_opt_fuel_1_cost: Array = INPUT(label='Biomass feedstock cost', units='$/unit', type='ARRAY', group='System Costs', required='?=0.0')
    om_opt_fuel_1_cost_escal: float = INPUT(label='Biomass feedstock cost escalation', units='%/year', type='NUMBER', group='System Costs', required='?=0.0')
    om_opt_fuel_2_usage: float = INPUT(label='Coal feedstock usage', units='unit', type='NUMBER', group='System Costs', required='?=0.0')
    om_opt_fuel_2_cost: Array = INPUT(label='Coal feedstock cost', units='$/unit', type='ARRAY', group='System Costs', required='?=0.0')
    om_opt_fuel_2_cost_escal: float = INPUT(label='Coal feedstock cost escalation', units='%/year', type='NUMBER', group='System Costs', required='?=0.0')
    add_om_num_types: float = INPUT(label='Number of O and M types', type='NUMBER', group='System Costs', required='?=0', constraints='INTEGER,MIN=0,MAX=2')
    om_capacity1_nameplate: float = INPUT(label='Battery capacity for System Costs values', units='kW', type='NUMBER', group='System Costs', required='?=0')
    om_production1_values: Array = INPUT(label='Battery production for System Costs values', units='kWh', type='ARRAY', group='System Costs', required='?=0')
    om_fixed1: Array = INPUT(label='Battery fixed System Costs annual amount', units='$/year', type='ARRAY', group='System Costs', required='?=0.0')
    om_production1: Array = INPUT(label='Battery production-based System Costs amount', units='$/MWh', type='ARRAY', group='System Costs', required='?=0.0')
    om_capacity1: Array = INPUT(label='Battery capacity-based System Costs amount', units='$/kWcap', type='ARRAY', group='System Costs', required='?=0.0')
    om_capacity2_nameplate: float = INPUT(label='Fuel cell capacity for System Costs values', units='kW', type='NUMBER', group='System Costs', required='?=0')
    om_production2_values: Array = INPUT(label='Fuel cell production for System Costs values', units='kWh', type='ARRAY', group='System Costs', required='?=0')
    om_fixed2: Array = INPUT(label='Fuel cell fixed System Costs annual amount', units='$/year', type='ARRAY', group='System Costs', required='?=0.0')
    om_production2: Array = INPUT(label='Fuel cell production-based System Costs amount', units='$/MWh', type='ARRAY', group='System Costs', required='?=0.0')
    om_capacity2: Array = INPUT(label='Fuel cell capacity-based System Costs amount', units='$/kWcap', type='ARRAY', group='System Costs', required='?=0.0')
    depr_fed_type: float = INPUT(label='Federal depreciation type', type='NUMBER', group='Depreciation', required='?=0', constraints='INTEGER,MIN=0,MAX=3', meta='0=none,1=macrs_half_year,2=sl,3=custom')
    depr_fed_sl_years: float = INPUT(label='Federal depreciation straight-line Years', units='years', type='NUMBER', group='Depreciation', required='depr_fed_type=2', constraints='INTEGER,POSITIVE')
    depr_fed_custom: Array = INPUT(label='Federal custom depreciation', units='%/year', type='ARRAY', group='Depreciation', required='depr_fed_type=3')
    depr_sta_type: float = INPUT(label='State depreciation type', type='NUMBER', group='Depreciation', required='?=0', constraints='INTEGER,MIN=0,MAX=3', meta='0=none,1=macrs_half_year,2=sl,3=custom')
    depr_sta_sl_years: float = INPUT(label='State depreciation straight-line years', units='years', type='NUMBER', group='Depreciation', required='depr_sta_type=2', constraints='INTEGER,POSITIVE')
    depr_sta_custom: Array = INPUT(label='State custom depreciation', units='%/year', type='ARRAY', group='Depreciation', required='depr_sta_type=3')
    itc_fed_amount: float = INPUT(label='Federal amount-based ITC amount', units='$', type='NUMBER', group='Tax Credit Incentives', required='?=0')
    itc_fed_amount_deprbas_fed: float = INPUT(label='Federal amount-based ITC reduces federal depreciation basis', units='0/1', type='NUMBER', group='Tax Credit Incentives', required='?=1', constraints='BOOLEAN')
    itc_fed_amount_deprbas_sta: float = INPUT(label='Federal amount-based ITC reduces state depreciation basis', units='0/1', type='NUMBER', group='Tax Credit Incentives', required='?=1', constraints='BOOLEAN')
    itc_sta_amount: float = INPUT(label='State amount-based ITC amount', units='$', type='NUMBER', group='Tax Credit Incentives', required='?=0')
    itc_sta_amount_deprbas_fed: float = INPUT(label='State amount-based ITC reduces federal depreciation basis', units='0/1', type='NUMBER', group='Tax Credit Incentives', required='?=0', constraints='BOOLEAN')
    itc_sta_amount_deprbas_sta: float = INPUT(label='State amount-based ITC reduces state depreciation basis', units='0/1', type='NUMBER', group='Tax Credit Incentives', required='?=0', constraints='BOOLEAN')
    itc_fed_percent: float = INPUT(label='Federal percentage-based ITC percent', units='%', type='NUMBER', group='Tax Credit Incentives', required='?=0')
    itc_fed_percent_maxvalue: float = INPUT(label='Federal percentage-based ITC maximum value', units='$', type='NUMBER', group='Tax Credit Incentives', required='?=1e99')
    itc_fed_percent_deprbas_fed: float = INPUT(label='Federal percentage-based ITC reduces federal depreciation basis', units='0/1', type='NUMBER', group='Tax Credit Incentives', required='?=1', constraints='BOOLEAN')
    itc_fed_percent_deprbas_sta: float = INPUT(label='Federal percentage-based ITC reduces state depreciation basis', units='0/1', type='NUMBER', group='Tax Credit Incentives', required='?=1', constraints='BOOLEAN')
    itc_sta_percent: float = INPUT(label='State percentage-based ITC percent', units='%', type='NUMBER', group='Tax Credit Incentives', required='?=0')
    itc_sta_percent_maxvalue: float = INPUT(label='State percentage-based ITC maximum Value', units='$', type='NUMBER', group='Tax Credit Incentives', required='?=1e99')
    itc_sta_percent_deprbas_fed: float = INPUT(label='State percentage-based ITC reduces federal depreciation basis', units='0/1', type='NUMBER', group='Tax Credit Incentives', required='?=0', constraints='BOOLEAN')
    itc_sta_percent_deprbas_sta: float = INPUT(label='State percentage-based ITC reduces state depreciation basis', units='0/1', type='NUMBER', group='Tax Credit Incentives', required='?=0', constraints='BOOLEAN')
    ptc_fed_amount: Array = INPUT(label='Federal PTC amount', units='$/kWh', type='ARRAY', group='Tax Credit Incentives', required='?=0')
    ptc_fed_term: float = INPUT(label='Federal PTC term', units='years', type='NUMBER', group='Tax Credit Incentives', required='?=10')
    ptc_fed_escal: float = INPUT(label='Federal PTC escalation', units='%/year', type='NUMBER', group='Tax Credit Incentives', required='?=0')
    ptc_sta_amount: Array = INPUT(label='State PTC amount', units='$/kWh', type='ARRAY', group='Tax Credit Incentives', required='?=0')
    ptc_sta_term: float = INPUT(label='State PTC term', units='years', type='NUMBER', group='Tax Credit Incentives', required='?=10')
    ptc_sta_escal: float = INPUT(label='State PTC escalation', units='%/year', type='NUMBER', group='Tax Credit Incentives', required='?=0')
    ibi_fed_amount: float = INPUT(label='Federal amount-based IBI amount', units='$', type='NUMBER', group='Payment Incentives', required='?=0')
    ibi_fed_amount_tax_fed: float = INPUT(label='Federal amount-based IBI federal taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    ibi_fed_amount_tax_sta: float = INPUT(label='Federal amount-based IBI state taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    ibi_fed_amount_deprbas_fed: float = INPUT(label='Federal amount-based IBI reduces federal depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    ibi_fed_amount_deprbas_sta: float = INPUT(label='Federal amount-based IBI reduces state depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    ibi_sta_amount: float = INPUT(label='State amount-based IBI amount', units='$', type='NUMBER', group='Payment Incentives', required='?=0')
    ibi_sta_amount_tax_fed: float = INPUT(label='State amount-based IBI federal taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    ibi_sta_amount_tax_sta: float = INPUT(label='State amount-based IBI state taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    ibi_sta_amount_deprbas_fed: float = INPUT(label='State amount-based IBI reduces federal depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    ibi_sta_amount_deprbas_sta: float = INPUT(label='State amount-based IBI reduces state depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    ibi_uti_amount: float = INPUT(label='Utility amount-based IBI amount', units='$', type='NUMBER', group='Payment Incentives', required='?=0')
    ibi_uti_amount_tax_fed: float = INPUT(label='Utility amount-based IBI federal taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    ibi_uti_amount_tax_sta: float = INPUT(label='Utility amount-based IBI state taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    ibi_uti_amount_deprbas_fed: float = INPUT(label='Utility amount-based IBI reduces federal depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    ibi_uti_amount_deprbas_sta: float = INPUT(label='Utility amount-based IBI reduces state depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    ibi_oth_amount: float = INPUT(label='Other amount-based IBI amount', units='$', type='NUMBER', group='Payment Incentives', required='?=0')
    ibi_oth_amount_tax_fed: float = INPUT(label='Other amount-based IBI federal taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    ibi_oth_amount_tax_sta: float = INPUT(label='Other amount-based IBI state taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    ibi_oth_amount_deprbas_fed: float = INPUT(label='Other amount-based IBI reduces federal depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    ibi_oth_amount_deprbas_sta: float = INPUT(label='Other amount-based IBI reduces state depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    ibi_fed_percent: float = INPUT(label='Federal percentage-based IBI percent', units='%', type='NUMBER', group='Payment Incentives', required='?=0.0')
    ibi_fed_percent_maxvalue: float = INPUT(label='Federal percentage-based IBI maximum value', units='$', type='NUMBER', group='Payment Incentives', required='?=1e99')
    ibi_fed_percent_tax_fed: float = INPUT(label='Federal percentage-based IBI federal taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    ibi_fed_percent_tax_sta: float = INPUT(label='Federal percentage-based IBI state taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    ibi_fed_percent_deprbas_fed: float = INPUT(label='Federal percentage-based IBI reduces federal depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    ibi_fed_percent_deprbas_sta: float = INPUT(label='Federal percentage-based IBI reduces state depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    ibi_sta_percent: float = INPUT(label='State percentage-based IBI percent', units='%', type='NUMBER', group='Payment Incentives', required='?=0.0')
    ibi_sta_percent_maxvalue: float = INPUT(label='State percentage-based IBI maximum value', units='$', type='NUMBER', group='Payment Incentives', required='?=1e99')
    ibi_sta_percent_tax_fed: float = INPUT(label='State percentage-based IBI federal taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    ibi_sta_percent_tax_sta: float = INPUT(label='State percentage-based IBI state taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    ibi_sta_percent_deprbas_fed: float = INPUT(label='State percentage-based IBI reduces federal depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    ibi_sta_percent_deprbas_sta: float = INPUT(label='State percentage-based IBI reduces state depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    ibi_uti_percent: float = INPUT(label='Utility percentage-based IBI percent', units='%', type='NUMBER', group='Payment Incentives', required='?=0.0')
    ibi_uti_percent_maxvalue: float = INPUT(label='Utility percentage-based IBI maximum value', units='$', type='NUMBER', group='Payment Incentives', required='?=1e99')
    ibi_uti_percent_tax_fed: float = INPUT(label='Utility percentage-based IBI federal taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    ibi_uti_percent_tax_sta: float = INPUT(label='Utility percentage-based IBI state taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    ibi_uti_percent_deprbas_fed: float = INPUT(label='Utility percentage-based IBI reduces federal depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    ibi_uti_percent_deprbas_sta: float = INPUT(label='Utility percentage-based IBI reduces state depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    ibi_oth_percent: float = INPUT(label='Other percentage-based IBI percent', units='%', type='NUMBER', group='Payment Incentives', required='?=0.0')
    ibi_oth_percent_maxvalue: float = INPUT(label='Other percentage-based IBI maximum value', units='$', type='NUMBER', group='Payment Incentives', required='?=1e99')
    ibi_oth_percent_tax_fed: float = INPUT(label='Other percentage-based IBI federal taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    ibi_oth_percent_tax_sta: float = INPUT(label='Other percentage-based IBI state taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    ibi_oth_percent_deprbas_fed: float = INPUT(label='Other percentage-based IBI reduces federal depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    ibi_oth_percent_deprbas_sta: float = INPUT(label='Other percentage-based IBI reduces state depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    cbi_fed_amount: float = INPUT(label='Federal CBI amount', units='$/Watt', type='NUMBER', group='Payment Incentives', required='?=0.0')
    cbi_fed_maxvalue: float = INPUT(label='Federal CBI maximum', units='$', type='NUMBER', group='Payment Incentives', required='?=1e99')
    cbi_fed_tax_fed: float = INPUT(label='Federal CBI federal taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    cbi_fed_tax_sta: float = INPUT(label='Federal CBI state taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    cbi_fed_deprbas_fed: float = INPUT(label='Federal CBI reduces federal depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    cbi_fed_deprbas_sta: float = INPUT(label='Federal CBI reduces state depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    cbi_sta_amount: float = INPUT(label='State CBI amount', units='$/Watt', type='NUMBER', group='Payment Incentives', required='?=0.0')
    cbi_sta_maxvalue: float = INPUT(label='State CBI maximum', units='$', type='NUMBER', group='Payment Incentives', required='?=1e99')
    cbi_sta_tax_fed: float = INPUT(label='State CBI federal taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    cbi_sta_tax_sta: float = INPUT(label='State CBI state taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    cbi_sta_deprbas_fed: float = INPUT(label='State CBI reduces federal depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    cbi_sta_deprbas_sta: float = INPUT(label='State CBI reduces state depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    cbi_uti_amount: float = INPUT(label='Utility CBI amount', units='$/Watt', type='NUMBER', group='Payment Incentives', required='?=0.0')
    cbi_uti_maxvalue: float = INPUT(label='Utility CBI maximum', units='$', type='NUMBER', group='Payment Incentives', required='?=1e99')
    cbi_uti_tax_fed: float = INPUT(label='Utility CBI federal taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    cbi_uti_tax_sta: float = INPUT(label='Utility CBI state taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    cbi_uti_deprbas_fed: float = INPUT(label='Utility CBI reduces federal depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    cbi_uti_deprbas_sta: float = INPUT(label='Utility CBI reduces state depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    cbi_oth_amount: float = INPUT(label='Other CBI amount', units='$/Watt', type='NUMBER', group='Payment Incentives', required='?=0.0')
    cbi_oth_maxvalue: float = INPUT(label='Other CBI maximum', units='$', type='NUMBER', group='Payment Incentives', required='?=1e99')
    cbi_oth_tax_fed: float = INPUT(label='Other CBI federal taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    cbi_oth_tax_sta: float = INPUT(label='Other CBI state taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    cbi_oth_deprbas_fed: float = INPUT(label='Other CBI reduces federal depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    cbi_oth_deprbas_sta: float = INPUT(label='Other CBI reduces state depreciation basis', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    pbi_fed_amount: Array = INPUT(label='Federal PBI amount', units='$/kWh', type='ARRAY', group='Payment Incentives', required='?=0')
    pbi_fed_term: float = INPUT(label='Federal PBI term', units='years', type='NUMBER', group='Payment Incentives', required='?=0')
    pbi_fed_escal: float = INPUT(label='Federal PBI escalation', units='%', type='NUMBER', group='Payment Incentives', required='?=0')
    pbi_fed_tax_fed: float = INPUT(label='Federal PBI federal taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    pbi_fed_tax_sta: float = INPUT(label='Federal PBI state taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    pbi_sta_amount: Array = INPUT(label='State PBI amount', units='$/kWh', type='ARRAY', group='Payment Incentives', required='?=0')
    pbi_sta_term: float = INPUT(label='State PBI term', units='years', type='NUMBER', group='Payment Incentives', required='?=0')
    pbi_sta_escal: float = INPUT(label='State PBI escalation', units='%', type='NUMBER', group='Payment Incentives', required='?=0')
    pbi_sta_tax_fed: float = INPUT(label='State PBI federal taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    pbi_sta_tax_sta: float = INPUT(label='State PBI state taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    pbi_uti_amount: Array = INPUT(label='Utility PBI amount', units='$/kWh', type='ARRAY', group='Payment Incentives', required='?=0')
    pbi_uti_term: float = INPUT(label='Utility PBI term', units='years', type='NUMBER', group='Payment Incentives', required='?=0')
    pbi_uti_escal: float = INPUT(label='Utility PBI escalation', units='%', type='NUMBER', group='Payment Incentives', required='?=0')
    pbi_uti_tax_fed: float = INPUT(label='Utility PBI federal taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    pbi_uti_tax_sta: float = INPUT(label='Utility PBI state taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    pbi_oth_amount: Array = INPUT(label='Other PBI amount', units='$/kWh', type='ARRAY', group='Payment Incentives', required='?=0')
    pbi_oth_term: float = INPUT(label='Other PBI term', units='years', type='NUMBER', group='Payment Incentives', required='?=0')
    pbi_oth_escal: float = INPUT(label='Other PBI escalation', units='%', type='NUMBER', group='Payment Incentives', required='?=0')
    pbi_oth_tax_fed: float = INPUT(label='Other PBI federal taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    pbi_oth_tax_sta: float = INPUT(label='Other PBI state taxable', units='0/1', type='NUMBER', group='Payment Incentives', required='?=1', constraints='BOOLEAN')
    cbi_total_fed: Final[float] = OUTPUT(label='Federal CBI income', units='$', type='NUMBER', group='Cash Flow Incentives', required='*')
    cbi_total_sta: Final[float] = OUTPUT(label='State CBI income', units='$', type='NUMBER', group='Cash Flow Incentives', required='*')
    cbi_total_oth: Final[float] = OUTPUT(label='Other CBI income', units='$', type='NUMBER', group='Cash Flow Incentives', required='*')
    cbi_total_uti: Final[float] = OUTPUT(label='Utility CBI income', units='$', type='NUMBER', group='Cash Flow Incentives', required='*')
    cbi_total: Final[float] = OUTPUT(label='Total CBI income', units='$', type='NUMBER', group='Cash Flow Incentives', required='*')
    cbi_statax_total: Final[float] = OUTPUT(label='State taxable CBI income', units='$', type='NUMBER', group='Cash Flow Incentives')
    cbi_fedtax_total: Final[float] = OUTPUT(label='Federal taxable CBI income', units='$', type='NUMBER', group='Cash Flow Incentives')
    ibi_total_fed: Final[float] = OUTPUT(label='Federal IBI income', units='$', type='NUMBER', group='Cash Flow Incentives', required='*')
    ibi_total_sta: Final[float] = OUTPUT(label='State IBI income', units='$', type='NUMBER', group='Cash Flow Incentives', required='*')
    ibi_total_oth: Final[float] = OUTPUT(label='Other IBI income', units='$', type='NUMBER', group='Cash Flow Incentives', required='*')
    ibi_total_uti: Final[float] = OUTPUT(label='Utility IBI income', units='$', type='NUMBER', group='Cash Flow Incentives', required='*')
    ibi_total: Final[float] = OUTPUT(label='Total IBI income', units='$', type='NUMBER', group='Cash Flow Incentives', required='*')
    ibi_statax_total: Final[float] = OUTPUT(label='State taxable IBI income', units='$', type='NUMBER', group='Cash Flow Incentives')
    ibi_fedtax_total: Final[float] = OUTPUT(label='Federal taxable IBI income', units='$', type='NUMBER', group='Cash Flow Incentives')
    cf_pbi_total_fed: Final[Array] = OUTPUT(label='Federal PBI income', units='$', type='ARRAY', group='Cash Flow Incentives', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_pbi_total_sta: Final[Array] = OUTPUT(label='State PBI income', units='$', type='ARRAY', group='Cash Flow Incentives', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_pbi_total_oth: Final[Array] = OUTPUT(label='Other PBI income', units='$', type='ARRAY', group='Cash Flow Incentives', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_pbi_total_uti: Final[Array] = OUTPUT(label='Utility PBI income', units='$', type='ARRAY', group='Cash Flow Incentives', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_pbi_total: Final[Array] = OUTPUT(label='Total PBI income', units='$', type='ARRAY', group='Cash Flow Incentives', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_pbi_statax_total: Final[Array] = OUTPUT(label='State taxable PBI income', units='$', type='ARRAY', group='Cash Flow Incentives', constraints='LENGTH_EQUAL=cf_length')
    cf_pbi_fedtax_total: Final[Array] = OUTPUT(label='Federal taxable PBI income', units='$', type='ARRAY', group='Cash Flow Incentives', constraints='LENGTH_EQUAL=cf_length')
    itc_total_fed: Final[float] = OUTPUT(label='Federal ITC income', units='$', type='NUMBER', group='Cash Flow Incentives', required='*')
    itc_total_sta: Final[float] = OUTPUT(label='State ITC income', units='$', type='NUMBER', group='Cash Flow Incentives', required='*')
    itc_total: Final[float] = OUTPUT(label='Total ITC income', units='$', type='NUMBER', group='Cash Flow Incentives', required='*')
    cf_ptc_fed: Final[Array] = OUTPUT(label='Federal PTC income', units='$', type='ARRAY', group='Cash Flow Incentives', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_ptc_sta: Final[Array] = OUTPUT(label='State PTC income', units='$', type='ARRAY', group='Cash Flow Incentives', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_ptc_total: Final[Array] = OUTPUT(label='Total PTC', units='$', type='ARRAY', group='Cash Flow Incentives', constraints='LENGTH_EQUAL=cf_length')
    en_batt: float = INPUT(label='Enable battery storage model', units='0/1', type='NUMBER', group='BatterySystem', required='?=0')
    batt_bank_replacement: Array = INPUT(label='Battery bank replacements per year', units='number/year', type='ARRAY', group='BatterySystem')
    batt_replacement_schedule: Array = INPUT(label='Battery bank replacements per year (user specified)', units='number/year', type='ARRAY', group='BatterySystem')
    batt_replacement_option: float = INPUT(label='Enable battery replacement?', units='0=none,1=capacity based,2=user schedule', type='NUMBER', group='BatterySystem', required='?=0', constraints='INTEGER,MIN=0,MAX=2')
    battery_per_kWh: float = INPUT(label='Battery cost', units='$/kWh', type='NUMBER', group='BatterySystem', required='?=0.0')
    batt_computed_bank_capacity: float = INPUT(label='Battery bank capacity', units='kWh', type='NUMBER', group='BatterySystem', required='?=0.0')
    cf_battery_replacement_cost: Final[Array] = OUTPUT(label='Battery replacement cost', units='$', type='ARRAY', group='Cash Flow', required='*')
    cf_battery_replacement_cost_schedule: Final[Array] = OUTPUT(label='Battery replacement cost schedule', units='$/kWh', type='ARRAY', group='Cash Flow', required='*')
    fuelcell_replacement: Array = INPUT(label='Fuel cell replacements per year', units='number/year', type='ARRAY', group='Fuel Cell')
    fuelcell_replacement_schedule: Array = INPUT(label='Fuel cell replacements per year (user specified)', units='number/year', type='ARRAY', group='Fuel Cell')
    en_fuelcell: float = INPUT(label='Enable fuel cell storage model', units='0/1', type='NUMBER', group='Fuel Cell', required='?=0')
    fuelcell_replacement_option: float = INPUT(label='Enable fuel cell replacement?', units='0=none,1=capacity based,2=user schedule', type='NUMBER', group='Fuel Cell', required='?=0', constraints='INTEGER,MIN=0,MAX=2')
    fuelcell_per_kWh: float = INPUT(label='Fuel cell cost', units='$/kWh', type='NUMBER', group='Fuel Cell', required='?=0.0')
    fuelcell_computed_bank_capacity: float = INPUT(label='Fuel cell capacity', units='kWh', type='NUMBER', group='Fuel Cell', required='?=0.0')
    cf_fuelcell_replacement_cost: Final[Array] = OUTPUT(label='Fuel cell replacement cost', units='$', type='ARRAY', group='Cash Flow', required='*')
    cf_fuelcell_replacement_cost_schedule: Final[Array] = OUTPUT(label='Fuel cell replacement cost schedule', units='$/kW', type='ARRAY', group='Cash Flow', required='*')
    market: float = INPUT(label='Residential or Commercial Market', units='0/1', type='NUMBER', group='Financial Parameters', required='?=1', constraints='INTEGER,MIN=0,MAX=1', meta='0=residential,1=comm.')
    mortgage: float = INPUT(label='Use mortgage style loan (res. only)', units='0/1', type='NUMBER', group='Financial Parameters', required='?=0', constraints='INTEGER,MIN=0,MAX=1', meta='0=standard loan,1=mortgage')
    total_installed_cost: float = INPUT(label='Total installed cost', units='$', type='NUMBER', group='System Costs', required='*', constraints='MIN=0')
    salvage_percentage: float = INPUT(label='Salvage value percentage', units='%', type='NUMBER', group='Financial Parameters', required='?=0.0', constraints='MIN=0,MAX=100')
    annual_energy_value: Array = INPUT(label='Energy value', units='$', type='ARRAY', group='System Output', required='*')
    annual_themal_value: Array = INPUT(label='Energy value', units='$', type='ARRAY', group='System Output')
    gen: Array = INPUT(label='Power generated by renewable resource', units='kW', type='ARRAY', group='System Output', required='*')
    degradation: Array = INPUT(label='Annual degradation', units='%', type='ARRAY', group='System Output', required='*')
    system_use_lifetime_output: float = INPUT(label='Lifetime hourly system outputs', units='0/1', type='NUMBER', group='Lifetime', required='*', constraints='INTEGER,MIN=0', meta='0=hourly first year,1=hourly lifetime')
    cf_length: Final[float] = OUTPUT(label='Number of periods in cash flow', type='NUMBER', group='Cash Flow', required='*', constraints='INTEGER')
    lcoe_real: Final[float] = OUTPUT(label='Real LCOE', units='cents/kWh', type='NUMBER', group='Cash Flow', required='*')
    lcoe_nom: Final[float] = OUTPUT(label='Nominal LCOE', units='cents/kWh', type='NUMBER', group='Cash Flow', required='*')
    payback: Final[float] = OUTPUT(label='Payback period', units='years', type='NUMBER', group='Cash Flow', required='*')
    discounted_payback: Final[float] = OUTPUT(label='Discounted payback period', units='years', type='NUMBER', group='Cash Flow', required='*')
    npv: Final[float] = OUTPUT(label='Net present value', units='$', type='NUMBER', group='Cash Flow', required='*')
    present_value_oandm: Final[float] = OUTPUT(label='Present value of O&M expenses', units='$', type='NUMBER', group='Financial Metrics', required='*')
    present_value_oandm_nonfuel: Final[float] = OUTPUT(label='Present value of non-fuel O&M expenses', units='$', type='NUMBER', group='Financial Metrics', required='*')
    present_value_fuel: Final[float] = OUTPUT(label='Present value of fuel expenses', units='$', type='NUMBER', group='Financial Metrics', required='*')
    present_value_insandproptax: Final[float] = OUTPUT(label='Present value of insurance and property tax', units='$', type='NUMBER', group='Financial Metrics', required='*')
    adjusted_installed_cost: Final[float] = OUTPUT(label='Net capital cost', units='$', type='NUMBER', group='Financial Metrics', required='*')
    loan_amount: Final[float] = OUTPUT(label='Debt', units='$', type='NUMBER', group='Financial Metrics', required='*')
    first_cost: Final[float] = OUTPUT(label='Equity', units='$', type='NUMBER', group='Financial Metrics', required='*')
    total_cost: Final[float] = OUTPUT(label='Total installed cost', units='$', type='NUMBER', group='Financial Metrics', required='*')
    cf_energy_net: Final[Array] = OUTPUT(label='Energy', units='kWh', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_value: Final[Array] = OUTPUT(label='Value of electricity savings', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_thermal_value: Final[Array] = OUTPUT(label='Value of thermal savings', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_value_added: Final[Array] = OUTPUT(label='Real estate value added', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_fixed_expense: Final[Array] = OUTPUT(label='O&M fixed expense', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_production_expense: Final[Array] = OUTPUT(label='O&M production-based expense', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_capacity_expense: Final[Array] = OUTPUT(label='O&M capacity-based expense', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_fixed1_expense: Final[Array] = OUTPUT(label='Battery fixed expense', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_production1_expense: Final[Array] = OUTPUT(label='Battery production-based expense', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_capacity1_expense: Final[Array] = OUTPUT(label='Battery capacity-based expense', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_fixed2_expense: Final[Array] = OUTPUT(label='Fuel cell fixed expense', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_production2_expense: Final[Array] = OUTPUT(label='Fuel cell production-based expense', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_capacity2_expense: Final[Array] = OUTPUT(label='Fuel cell capacity-based expense', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_fuel_expense: Final[Array] = OUTPUT(label='O&M fuel expense', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_opt_fuel_1_expense: Final[Array] = OUTPUT(label='O&M biomass feedstock expense', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_opt_fuel_2_expense: Final[Array] = OUTPUT(label='O&M coal feedstock expense', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_property_tax_assessed_value: Final[Array] = OUTPUT(label='Property tax net assessed value', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_property_tax_expense: Final[Array] = OUTPUT(label='Property tax expense', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_insurance_expense: Final[Array] = OUTPUT(label='Insurance expense', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_net_salvage_value: Final[Array] = OUTPUT(label='Net salvage value', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_operating_expenses: Final[Array] = OUTPUT(label='Total operating expense', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_deductible_expenses: Final[Array] = OUTPUT(label='Deductible expenses', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_debt_balance: Final[Array] = OUTPUT(label='Debt balance', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_debt_payment_interest: Final[Array] = OUTPUT(label='Interest payment', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_debt_payment_principal: Final[Array] = OUTPUT(label='Principal payment', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_debt_payment_total: Final[Array] = OUTPUT(label='Total P&I debt payment', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_sta_depr_sched: Final[Array] = OUTPUT(label='State depreciation schedule', units='%', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_sta_depreciation: Final[Array] = OUTPUT(label='State depreciation', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_sta_incentive_income_less_deductions: Final[Array] = OUTPUT(label='State incentive income less deductions', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_sta_taxable_income_less_deductions: Final[Array] = OUTPUT(label='State taxable income less deductions', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_sta_tax_savings: Final[Array] = OUTPUT(label='State tax savings', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_sta_taxable_incentive_income: Final[Array] = OUTPUT(label='State taxable incentive income', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_fed_taxable_incentive_income: Final[Array] = OUTPUT(label='Federal taxable incentive income', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_fed_depr_sched: Final[Array] = OUTPUT(label='Federal depreciation schedule', units='%', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_fed_depreciation: Final[Array] = OUTPUT(label='Federal depreciation', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_fed_incentive_income_less_deductions: Final[Array] = OUTPUT(label='Federal incentive income less deductions', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_fed_taxable_income_less_deductions: Final[Array] = OUTPUT(label='Federal taxable income less deductions', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_fed_tax_savings: Final[Array] = OUTPUT(label='Federal tax savings', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_sta_and_fed_tax_savings: Final[Array] = OUTPUT(label='Total tax savings (federal and state)', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_after_tax_net_equity_cost_flow: Final[Array] = OUTPUT(label='After-tax annual costs', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_after_tax_cash_flow: Final[Array] = OUTPUT(label='After-tax cash flow', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_discounted_costs: Final[Array] = OUTPUT(label='Discounted costs', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_discounted_savings: Final[Array] = OUTPUT(label='Discounted savings', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_discounted_payback: Final[Array] = OUTPUT(label='Discounted payback', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_discounted_cumulative_payback: Final[Array] = OUTPUT(label='Cumulative discounted payback', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_payback_with_expenses: Final[Array] = OUTPUT(label='Simple payback with expenses', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_cumulative_payback_with_expenses: Final[Array] = OUTPUT(label='Cumulative simple payback with expenses', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_payback_without_expenses: Final[Array] = OUTPUT(label='Simple payback without expenses', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_cumulative_payback_without_expenses: Final[Array] = OUTPUT(label='Cumulative simple payback without expenses', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    lcoptc_fed_real: Final[float] = OUTPUT(label='Levelized federal PTC (real)', units='cents/kWh', type='NUMBER', group='Financial Metrics', required='*')
    lcoptc_fed_nom: Final[float] = OUTPUT(label='Levelized federal PTC (nominal)', units='cents/kWh', type='NUMBER', group='Financial Metrics', required='*')
    lcoptc_sta_real: Final[float] = OUTPUT(label='Levelized state PTC (real)', units='cents/kWh', type='NUMBER', group='Financial Metrics', required='*')
    lcoptc_sta_nom: Final[float] = OUTPUT(label='Levelized state PTC (nominal)', units='cents/kWh', type='NUMBER', group='Financial Metrics', required='*')
    wacc: Final[float] = OUTPUT(label='Weighted average cost of capital (WACC)', type='NUMBER', group='Financial Metrics', required='*')
    effective_tax_rate: Final[float] = OUTPUT(label='Effective tax rate', units='%', type='NUMBER', group='Financial Metrics', required='*')
    elec_cost_with_system: Array = INPUT(label='Energy value', units='$', type='ARRAY', group='ThirdPartyOwnership', required='*')
    elec_cost_without_system: Array = INPUT(label='Energy value', units='$', type='ARRAY', group='ThirdPartyOwnership', required='*')
    cf_nte: Final[Array] = OUTPUT(label='Not to exceed (NTE)', units='cents/kWh', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    year1_nte: Final[float] = OUTPUT(label='Year 1 NTE', units='cents/kWh', type='NUMBER', group='Cash Flow', required='*')
    lnte_real: Final[float] = OUTPUT(label='Real LNTE', units='cents/kWh', type='NUMBER', group='Cash Flow', required='*')
    lnte_nom: Final[float] = OUTPUT(label='Nominal LNTE', units='cents/kWh', type='NUMBER', group='Cash Flow', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 analysis_period: float = ...,
                 federal_tax_rate: Array = ...,
                 state_tax_rate: Array = ...,
                 property_tax_rate: float = ...,
                 prop_tax_cost_assessed_percent: float = ...,
                 prop_tax_assessed_decline: float = ...,
                 real_discount_rate: float = ...,
                 inflation_rate: float = ...,
                 insurance_rate: float = ...,
                 system_capacity: float = ...,
                 system_heat_rate: float = ...,
                 loan_term: float = ...,
                 loan_rate: float = ...,
                 debt_fraction: float = ...,
                 om_fixed: Array = ...,
                 om_fixed_escal: float = ...,
                 om_production: Array = ...,
                 om_production_escal: float = ...,
                 om_capacity: Array = ...,
                 om_capacity_escal: float = ...,
                 om_fuel_cost: Array = ...,
                 om_fuel_cost_escal: float = ...,
                 annual_fuel_usage: float = ...,
                 annual_fuel_usage_lifetime: Array = ...,
                 om_replacement_cost1: Array = ...,
                 om_replacement_cost2: Array = ...,
                 om_replacement_cost_escal: float = ...,
                 om_opt_fuel_1_usage: float = ...,
                 om_opt_fuel_1_cost: Array = ...,
                 om_opt_fuel_1_cost_escal: float = ...,
                 om_opt_fuel_2_usage: float = ...,
                 om_opt_fuel_2_cost: Array = ...,
                 om_opt_fuel_2_cost_escal: float = ...,
                 add_om_num_types: float = ...,
                 om_capacity1_nameplate: float = ...,
                 om_production1_values: Array = ...,
                 om_fixed1: Array = ...,
                 om_production1: Array = ...,
                 om_capacity1: Array = ...,
                 om_capacity2_nameplate: float = ...,
                 om_production2_values: Array = ...,
                 om_fixed2: Array = ...,
                 om_production2: Array = ...,
                 om_capacity2: Array = ...,
                 depr_fed_type: float = ...,
                 depr_fed_sl_years: float = ...,
                 depr_fed_custom: Array = ...,
                 depr_sta_type: float = ...,
                 depr_sta_sl_years: float = ...,
                 depr_sta_custom: Array = ...,
                 itc_fed_amount: float = ...,
                 itc_fed_amount_deprbas_fed: float = ...,
                 itc_fed_amount_deprbas_sta: float = ...,
                 itc_sta_amount: float = ...,
                 itc_sta_amount_deprbas_fed: float = ...,
                 itc_sta_amount_deprbas_sta: float = ...,
                 itc_fed_percent: float = ...,
                 itc_fed_percent_maxvalue: float = ...,
                 itc_fed_percent_deprbas_fed: float = ...,
                 itc_fed_percent_deprbas_sta: float = ...,
                 itc_sta_percent: float = ...,
                 itc_sta_percent_maxvalue: float = ...,
                 itc_sta_percent_deprbas_fed: float = ...,
                 itc_sta_percent_deprbas_sta: float = ...,
                 ptc_fed_amount: Array = ...,
                 ptc_fed_term: float = ...,
                 ptc_fed_escal: float = ...,
                 ptc_sta_amount: Array = ...,
                 ptc_sta_term: float = ...,
                 ptc_sta_escal: float = ...,
                 ibi_fed_amount: float = ...,
                 ibi_fed_amount_tax_fed: float = ...,
                 ibi_fed_amount_tax_sta: float = ...,
                 ibi_fed_amount_deprbas_fed: float = ...,
                 ibi_fed_amount_deprbas_sta: float = ...,
                 ibi_sta_amount: float = ...,
                 ibi_sta_amount_tax_fed: float = ...,
                 ibi_sta_amount_tax_sta: float = ...,
                 ibi_sta_amount_deprbas_fed: float = ...,
                 ibi_sta_amount_deprbas_sta: float = ...,
                 ibi_uti_amount: float = ...,
                 ibi_uti_amount_tax_fed: float = ...,
                 ibi_uti_amount_tax_sta: float = ...,
                 ibi_uti_amount_deprbas_fed: float = ...,
                 ibi_uti_amount_deprbas_sta: float = ...,
                 ibi_oth_amount: float = ...,
                 ibi_oth_amount_tax_fed: float = ...,
                 ibi_oth_amount_tax_sta: float = ...,
                 ibi_oth_amount_deprbas_fed: float = ...,
                 ibi_oth_amount_deprbas_sta: float = ...,
                 ibi_fed_percent: float = ...,
                 ibi_fed_percent_maxvalue: float = ...,
                 ibi_fed_percent_tax_fed: float = ...,
                 ibi_fed_percent_tax_sta: float = ...,
                 ibi_fed_percent_deprbas_fed: float = ...,
                 ibi_fed_percent_deprbas_sta: float = ...,
                 ibi_sta_percent: float = ...,
                 ibi_sta_percent_maxvalue: float = ...,
                 ibi_sta_percent_tax_fed: float = ...,
                 ibi_sta_percent_tax_sta: float = ...,
                 ibi_sta_percent_deprbas_fed: float = ...,
                 ibi_sta_percent_deprbas_sta: float = ...,
                 ibi_uti_percent: float = ...,
                 ibi_uti_percent_maxvalue: float = ...,
                 ibi_uti_percent_tax_fed: float = ...,
                 ibi_uti_percent_tax_sta: float = ...,
                 ibi_uti_percent_deprbas_fed: float = ...,
                 ibi_uti_percent_deprbas_sta: float = ...,
                 ibi_oth_percent: float = ...,
                 ibi_oth_percent_maxvalue: float = ...,
                 ibi_oth_percent_tax_fed: float = ...,
                 ibi_oth_percent_tax_sta: float = ...,
                 ibi_oth_percent_deprbas_fed: float = ...,
                 ibi_oth_percent_deprbas_sta: float = ...,
                 cbi_fed_amount: float = ...,
                 cbi_fed_maxvalue: float = ...,
                 cbi_fed_tax_fed: float = ...,
                 cbi_fed_tax_sta: float = ...,
                 cbi_fed_deprbas_fed: float = ...,
                 cbi_fed_deprbas_sta: float = ...,
                 cbi_sta_amount: float = ...,
                 cbi_sta_maxvalue: float = ...,
                 cbi_sta_tax_fed: float = ...,
                 cbi_sta_tax_sta: float = ...,
                 cbi_sta_deprbas_fed: float = ...,
                 cbi_sta_deprbas_sta: float = ...,
                 cbi_uti_amount: float = ...,
                 cbi_uti_maxvalue: float = ...,
                 cbi_uti_tax_fed: float = ...,
                 cbi_uti_tax_sta: float = ...,
                 cbi_uti_deprbas_fed: float = ...,
                 cbi_uti_deprbas_sta: float = ...,
                 cbi_oth_amount: float = ...,
                 cbi_oth_maxvalue: float = ...,
                 cbi_oth_tax_fed: float = ...,
                 cbi_oth_tax_sta: float = ...,
                 cbi_oth_deprbas_fed: float = ...,
                 cbi_oth_deprbas_sta: float = ...,
                 pbi_fed_amount: Array = ...,
                 pbi_fed_term: float = ...,
                 pbi_fed_escal: float = ...,
                 pbi_fed_tax_fed: float = ...,
                 pbi_fed_tax_sta: float = ...,
                 pbi_sta_amount: Array = ...,
                 pbi_sta_term: float = ...,
                 pbi_sta_escal: float = ...,
                 pbi_sta_tax_fed: float = ...,
                 pbi_sta_tax_sta: float = ...,
                 pbi_uti_amount: Array = ...,
                 pbi_uti_term: float = ...,
                 pbi_uti_escal: float = ...,
                 pbi_uti_tax_fed: float = ...,
                 pbi_uti_tax_sta: float = ...,
                 pbi_oth_amount: Array = ...,
                 pbi_oth_term: float = ...,
                 pbi_oth_escal: float = ...,
                 pbi_oth_tax_fed: float = ...,
                 pbi_oth_tax_sta: float = ...,
                 en_batt: float = ...,
                 batt_bank_replacement: Array = ...,
                 batt_replacement_schedule: Array = ...,
                 batt_replacement_option: float = ...,
                 battery_per_kWh: float = ...,
                 batt_computed_bank_capacity: float = ...,
                 fuelcell_replacement: Array = ...,
                 fuelcell_replacement_schedule: Array = ...,
                 en_fuelcell: float = ...,
                 fuelcell_replacement_option: float = ...,
                 fuelcell_per_kWh: float = ...,
                 fuelcell_computed_bank_capacity: float = ...,
                 market: float = ...,
                 mortgage: float = ...,
                 total_installed_cost: float = ...,
                 salvage_percentage: float = ...,
                 annual_energy_value: Array = ...,
                 annual_themal_value: Array = ...,
                 gen: Array = ...,
                 degradation: Array = ...,
                 system_use_lifetime_output: float = ...,
                 elec_cost_with_system: Array = ...,
                 elec_cost_without_system: Array = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
