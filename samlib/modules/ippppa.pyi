
# This is a generated file

"""ippppa - Utility IPP/Commerical PPA Finance model."""

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
        'om_opt_fuel_1_usage': float,
        'om_opt_fuel_1_cost': Array,
        'om_opt_fuel_1_cost_escal': float,
        'om_opt_fuel_2_usage': float,
        'om_opt_fuel_2_cost': Array,
        'om_opt_fuel_2_cost_escal': float,
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
        'market': float,
        'system_use_lifetime_output': float,
        'gen': Array,
        'degradation': Array,
        'soln_mode': float,
        'ppa_soln_tolerance': float,
        'ppa_soln_min': float,
        'ppa_soln_max': float,
        'ppa_soln_max_iterations': float,
        'bid_price': Array,
        'bid_price_esc': float,
        'construction_financing_cost': float,
        'total_installed_cost': float,
        'salvage_percentage': float,
        'min_dscr_target': float,
        'min_irr_target': float,
        'ppa_escalation': float,
        'min_dscr_required': float,
        'positive_cashflow_required': float,
        'optimize_lcoe_wrt_debt_fraction': float,
        'optimize_lcoe_wrt_ppa_escalation': float,
        'system_use_recapitalization': float,
        'system_recapitalization_cost': float,
        'system_recapitalization_escalation': float,
        'system_recapitalization_boolean': Array,
        'cf_recapitalization': Array,
        'dispatch_factor1': float,
        'dispatch_factor2': float,
        'dispatch_factor3': float,
        'dispatch_factor4': float,
        'dispatch_factor5': float,
        'dispatch_factor6': float,
        'dispatch_factor7': float,
        'dispatch_factor8': float,
        'dispatch_factor9': float,
        'dispatch_sched_weekday': Matrix,
        'dispatch_sched_weekend': Matrix,
        'cf_energy_net_jan': Array,
        'cf_revenue_jan': Array,
        'cf_energy_net_feb': Array,
        'cf_revenue_feb': Array,
        'cf_energy_net_mar': Array,
        'cf_revenue_mar': Array,
        'cf_energy_net_apr': Array,
        'cf_revenue_apr': Array,
        'cf_energy_net_may': Array,
        'cf_revenue_may': Array,
        'cf_energy_net_jun': Array,
        'cf_revenue_jun': Array,
        'cf_energy_net_jul': Array,
        'cf_revenue_jul': Array,
        'cf_energy_net_aug': Array,
        'cf_revenue_aug': Array,
        'cf_energy_net_sep': Array,
        'cf_revenue_sep': Array,
        'cf_energy_net_oct': Array,
        'cf_revenue_oct': Array,
        'cf_energy_net_nov': Array,
        'cf_revenue_nov': Array,
        'cf_energy_net_dec': Array,
        'cf_revenue_dec': Array,
        'cf_energy_net_dispatch1': Array,
        'cf_revenue_dispatch1': Array,
        'cf_energy_net_dispatch2': Array,
        'cf_revenue_dispatch2': Array,
        'cf_energy_net_dispatch3': Array,
        'cf_revenue_dispatch3': Array,
        'cf_energy_net_dispatch4': Array,
        'cf_revenue_dispatch4': Array,
        'cf_energy_net_dispatch5': Array,
        'cf_revenue_dispatch5': Array,
        'cf_energy_net_dispatch6': Array,
        'cf_revenue_dispatch6': Array,
        'cf_energy_net_dispatch7': Array,
        'cf_revenue_dispatch7': Array,
        'cf_energy_net_dispatch8': Array,
        'cf_revenue_dispatch8': Array,
        'cf_energy_net_dispatch9': Array,
        'cf_revenue_dispatch9': Array,
        'firstyear_revenue_dispatch1': float,
        'firstyear_revenue_dispatch2': float,
        'firstyear_revenue_dispatch3': float,
        'firstyear_revenue_dispatch4': float,
        'firstyear_revenue_dispatch5': float,
        'firstyear_revenue_dispatch6': float,
        'firstyear_revenue_dispatch7': float,
        'firstyear_revenue_dispatch8': float,
        'firstyear_revenue_dispatch9': float,
        'firstyear_energy_dispatch1': float,
        'firstyear_energy_dispatch2': float,
        'firstyear_energy_dispatch3': float,
        'firstyear_energy_dispatch4': float,
        'firstyear_energy_dispatch5': float,
        'firstyear_energy_dispatch6': float,
        'firstyear_energy_dispatch7': float,
        'firstyear_energy_dispatch8': float,
        'firstyear_energy_dispatch9': float,
        'firstyear_energy_price1': float,
        'firstyear_energy_price2': float,
        'firstyear_energy_price3': float,
        'firstyear_energy_price4': float,
        'firstyear_energy_price5': float,
        'firstyear_energy_price6': float,
        'firstyear_energy_price7': float,
        'firstyear_energy_price8': float,
        'firstyear_energy_price9': float,
        'cf_revenue_monthly_firstyear_TOD1': Array,
        'cf_energy_net_monthly_firstyear_TOD1': Array,
        'cf_revenue_monthly_firstyear_TOD2': Array,
        'cf_energy_net_monthly_firstyear_TOD2': Array,
        'cf_revenue_monthly_firstyear_TOD3': Array,
        'cf_energy_net_monthly_firstyear_TOD3': Array,
        'cf_revenue_monthly_firstyear_TOD4': Array,
        'cf_energy_net_monthly_firstyear_TOD4': Array,
        'cf_revenue_monthly_firstyear_TOD5': Array,
        'cf_energy_net_monthly_firstyear_TOD5': Array,
        'cf_revenue_monthly_firstyear_TOD6': Array,
        'cf_energy_net_monthly_firstyear_TOD6': Array,
        'cf_revenue_monthly_firstyear_TOD7': Array,
        'cf_energy_net_monthly_firstyear_TOD7': Array,
        'cf_revenue_monthly_firstyear_TOD8': Array,
        'cf_energy_net_monthly_firstyear_TOD8': Array,
        'cf_revenue_monthly_firstyear_TOD9': Array,
        'cf_energy_net_monthly_firstyear_TOD9': Array,
        'cf_length': float,
        'lcoe_real': float,
        'lcoe_nom': float,
        'lppa_real': float,
        'lppa_nom': float,
        'latcf_real': float,
        'latcf_nom': float,
        'npv': float,
        'ppa': float,
        'min_cashflow': float,
        'irr': float,
        'min_dscr': float,
        'actual_debt_frac': float,
        'actual_ppa_escalation': float,
        'present_value_oandm': float,
        'present_value_oandm_nonfuel': float,
        'present_value_fuel': float,
        'present_value_insandproptax': float,
        'cf_energy_net': Array,
        'cf_degradation': Array,
        'cf_energy_value': Array,
        'cf_energy_price': Array,
        'cf_om_fixed_expense': Array,
        'cf_om_production_expense': Array,
        'cf_om_capacity_expense': Array,
        'cf_om_fuel_expense': Array,
        'cf_om_opt_fuel_1_expense': Array,
        'cf_om_opt_fuel_2_expense': Array,
        'cf_property_tax_assessed_value': Array,
        'cf_property_tax_expense': Array,
        'cf_insurance_expense': Array,
        'cf_operating_expenses': Array,
        'cf_operating_income': Array,
        'cf_net_salvage_value': Array,
        'cf_deductible_expenses': Array,
        'cf_debt_balance': Array,
        'cf_debt_payment_interest': Array,
        'cf_debt_payment_principal': Array,
        'cf_debt_payment_total': Array,
        'ibi_total_fed': float,
        'ibi_total_sta': float,
        'ibi_total_oth': float,
        'ibi_total_uti': float,
        'ibi_total': float,
        'cbi_total_fed': float,
        'cbi_total_sta': float,
        'cbi_total_oth': float,
        'cbi_total_uti': float,
        'cbi_total': float,
        'cf_pbi_total_fed': Array,
        'cf_pbi_total_sta': Array,
        'cf_pbi_total_oth': Array,
        'cf_pbi_total_uti': Array,
        'cf_pbi_total': Array,
        'cf_ptc_fed': Array,
        'cf_ptc_sta': Array,
        'cf_ptc_total': Array,
        'itc_fed_total': float,
        'itc_sta_total': float,
        'itc_total': float,
        'cf_sta_depr_sched': Array,
        'cf_sta_depreciation': Array,
        'cf_sta_incentive_income_less_deductions': Array,
        'cf_sta_taxable_income_less_deductions': Array,
        'cf_sta_tax_savings': Array,
        'cf_sta_income_taxes': Array,
        'cf_fed_depr_sched': Array,
        'cf_fed_depreciation': Array,
        'cf_fed_incentive_income_less_deductions': Array,
        'cf_fed_taxable_income_less_deductions': Array,
        'cf_fed_tax_savings': Array,
        'cf_fed_income_taxes': Array,
        'cf_sta_and_fed_tax_savings': Array,
        'cf_after_tax_net_equity_cash_flow': Array,
        'cf_after_tax_net_equity_cost_flow': Array,
        'cf_after_tax_cash_flow': Array,
        'cf_ppa_price': Array,
        'cf_pretax_dscr': Array,
        'lcoptc_fed_real': float,
        'lcoptc_fed_nom': float,
        'lcoptc_sta_real': float,
        'lcoptc_sta_nom': float,
        'wacc': float,
        'effective_tax_rate': float
}, total=False)

class Data(ssc.DataDict):
    analysis_period: float = INPUT(label='Analyis period', units='years', type='NUMBER', group='Financials', required='?=30', constraints='INTEGER,MIN=0,MAX=50')
    federal_tax_rate: Array = INPUT(label='Federal income tax rate', units='%', type='ARRAY', group='Financials', required='*')
    state_tax_rate: Array = INPUT(label='State income tax rate', units='%', type='ARRAY', group='Financials', required='*')
    cf_federal_tax_frac: Final[Array] = OUTPUT(label='Federal income tax rate', units='frac', type='ARRAY', group='Financials', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_state_tax_frac: Final[Array] = OUTPUT(label='State income tax rate', units='frac', type='ARRAY', group='Financials', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_effective_tax_frac: Final[Array] = OUTPUT(label='Effective income tax rate', units='frac', type='ARRAY', group='Financials', required='*', constraints='LENGTH_EQUAL=cf_length')
    property_tax_rate: float = INPUT(label='Property tax rate', units='%', type='NUMBER', group='Financials', required='?=0.0', constraints='MIN=0,MAX=100')
    prop_tax_cost_assessed_percent: float = INPUT(label='Percent of pre-financing costs assessed', units='%', type='NUMBER', group='Financials', required='?=95', constraints='MIN=0,MAX=100')
    prop_tax_assessed_decline: float = INPUT(label='Assessed value annual decline', units='%', type='NUMBER', group='Financials', required='?=5', constraints='MIN=0,MAX=100')
    real_discount_rate: float = INPUT(label='Real discount rate', units='%', type='NUMBER', group='Financials', required='*', constraints='MIN=-99')
    inflation_rate: float = INPUT(label='Inflation rate', units='%', type='NUMBER', group='Financials', required='*', constraints='MIN=-99')
    insurance_rate: float = INPUT(label='Insurance rate', units='%', type='NUMBER', group='Financials', required='?=0.0', constraints='MIN=0,MAX=100')
    system_capacity: float = INPUT(label='System nameplate capacity', units='kW', type='NUMBER', group='System', required='*', constraints='POSITIVE')
    system_heat_rate: float = INPUT(label='System heat rate', units='MMBTus/MWh', type='NUMBER', group='System', required='?=0.0', constraints='MIN=0')
    loan_term: float = INPUT(label='Loan term', units='years', type='NUMBER', group='Loan', required='?=0', constraints='INTEGER,MIN=0,MAX=50')
    loan_rate: float = INPUT(label='Loan rate', units='%', type='NUMBER', group='Loan', required='?=0', constraints='MIN=0,MAX=100')
    debt_fraction: float = INPUT(label='Debt percentage', units='%', type='NUMBER', group='Loan', required='?=0', constraints='MIN=0,MAX=100')
    om_fixed: Array = INPUT(label='Fixed O&M annual amount', units='$/year', type='ARRAY', group='O&M', required='?=0.0')
    om_fixed_escal: float = INPUT(label='Fixed O&M escalation', units='%/year', type='NUMBER', group='O&M', required='?=0.0')
    om_production: Array = INPUT(label='Production-based O&M amount', units='$/MWh', type='ARRAY', group='O&M', required='?=0.0')
    om_production_escal: float = INPUT(label='Production-based O&M escalation', units='%/year', type='NUMBER', group='O&M', required='?=0.0')
    om_capacity: Array = INPUT(label='Capacity-based O&M amount', units='$/kWcap', type='ARRAY', group='O&M', required='?=0.0')
    om_capacity_escal: float = INPUT(label='Capacity-based O&M escalation', units='%/year', type='NUMBER', group='O&M', required='?=0.0')
    om_fuel_cost: Array = INPUT(label='Fuel cost', units='$/MMBtu', type='ARRAY', group='O&M', required='?=0.0')
    om_fuel_cost_escal: float = INPUT(label='Fuel cost escalation', units='%/year', type='NUMBER', group='O&M', required='?=0.0')
    annual_fuel_usage: float = INPUT(label='Fuel usage', units='kWht', type='NUMBER', group='O&M', required='?=0', constraints='MIN=0')
    om_opt_fuel_1_usage: float = INPUT(label='Biomass feedstock usage', units='unit', type='NUMBER', group='O&M', required='?=0.0')
    om_opt_fuel_1_cost: Array = INPUT(label='Biomass feedstock cost', units='$/unit', type='ARRAY', group='O&M', required='?=0.0')
    om_opt_fuel_1_cost_escal: float = INPUT(label='Biomass feedstock cost escalation', units='%/year', type='NUMBER', group='O&M', required='?=0.0')
    om_opt_fuel_2_usage: float = INPUT(label='Coal feedstock usage', units='unit', type='NUMBER', group='O&M', required='?=0.0')
    om_opt_fuel_2_cost: Array = INPUT(label='Coal feedstock cost', units='$/unit', type='ARRAY', group='O&M', required='?=0.0')
    om_opt_fuel_2_cost_escal: float = INPUT(label='Coal feedstock cost escalation', units='%/year', type='NUMBER', group='O&M', required='?=0.0')
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
    market: float = INPUT(label='Utility IPP or Commercial PPA', units='0/1', type='NUMBER', group='ippppa', required='?=0', constraints='INTEGER,MIN=0,MAX=1', meta='0=ipp,1=ppa')
    system_use_lifetime_output: float = INPUT(label='Lifetime hourly system outputs', units='0/1', type='NUMBER', group='ippppa', required='*', constraints='INTEGER,MIN=0', meta='0=hourly first year,1=hourly lifetime')
    gen: Array = INPUT(label='Power generated by renewable resource', units='kW', type='ARRAY', required='*')
    degradation: Array = INPUT(label='Annual energy degradation', type='ARRAY', group='ippppa', required='*')
    soln_mode: float = INPUT(label='PPA solution mode', units='0/1', type='NUMBER', group='ippppa', required='?=0', constraints='INTEGER,MIN=0,MAX=1', meta='0=solve ppa,1=specify ppa')
    ppa_soln_tolerance: float = INPUT(label='PPA solution tolerance', type='NUMBER', group='ippppa', required='?=1e-3')
    ppa_soln_min: float = INPUT(label='PPA solution minimum ppa', units='cents/kWh', type='NUMBER', group='ippppa', required='?=0')
    ppa_soln_max: float = INPUT(label='PPA solution maximum ppa', units='cents/kWh', type='NUMBER', group='ippppa', required='?=100')
    ppa_soln_max_iterations: float = INPUT(label='PPA solution maximum number of iterations', type='NUMBER', group='ippppa', required='?=100', constraints='INTEGER,MIN=1')
    bid_price: Array = INPUT(label='Initial year PPA price', units='$/kWh', type='ARRAY', group='ippppa', required='?=0.10')
    bid_price_esc: float = INPUT(label='PPA escalation', units='%', type='NUMBER', group='ippppa', required='?=0', constraints='MIN=0,MAX=100')
    construction_financing_cost: float = INPUT(label='Construction financing total', units='$', type='NUMBER', group='ippppa', required='*')
    total_installed_cost: float = INPUT(label='Total installed cost', units='$', type='NUMBER', group='ippppa', required='*', constraints='MIN=0')
    salvage_percentage: float = INPUT(label='Salvage value percentage', units='%', type='NUMBER', group='ippppa', required='?=0.0', constraints='MIN=0,MAX=100')
    min_dscr_target: float = INPUT(label='Minimum required DSCR', type='NUMBER', group='ippppa', required='?=1.4')
    min_irr_target: float = INPUT(label='Minimum required IRR', units='%', type='NUMBER', group='ippppa', required='?=15')
    ppa_escalation: float = INPUT(label='PPA escalation', units='%', type='NUMBER', group='ippppa', required='?=0.6')
    min_dscr_required: float = INPUT(label='Minimum DSCR required', units='0/1', type='NUMBER', group='ippppa', required='?=1', constraints='INTEGER,MIN=0,MAX=1', meta='0=no,1=yes')
    positive_cashflow_required: float = INPUT(label='Positive cash flow required', units='0/1', type='NUMBER', group='ippppa', required='?=1', constraints='INTEGER,MIN=0,MAX=1', meta='0=no,1=yes')
    optimize_lcoe_wrt_debt_fraction: float = INPUT(label='Optimize LCOE with respect to debt percent', units='0/1', type='NUMBER', group='ippppa', required='?=0', constraints='INTEGER,MIN=0,MAX=1', meta='0=no,1=yes')
    optimize_lcoe_wrt_ppa_escalation: float = INPUT(label='Optimize LCOE with respect to PPA escalation', units='0/1', type='NUMBER', group='ippppa', required='?=0', constraints='INTEGER,MIN=0,MAX=1', meta='0=no,1=yes')
    system_use_recapitalization: float = INOUT(label='Recapitalization expenses', units='0/1', type='NUMBER', group='ippppa', required='?=0', constraints='INTEGER,MIN=0', meta='0=None,1=Recapitalize')
    system_recapitalization_cost: float = INPUT(label='Recapitalization cost', units='$', type='NUMBER', group='ippppa', required='?=0')
    system_recapitalization_escalation: float = INPUT(label='Recapitalization escalation (above inflation)', units='%', type='NUMBER', group='ippppa', required='?=0', constraints='MIN=0,MAX=100')
    system_recapitalization_boolean: Array = INPUT(label='Recapitalization boolean', type='ARRAY', group='ippppa', required='?=0')
    cf_recapitalization: Final[Array] = OUTPUT(label='Recapitalization operating expense', units='$', type='ARRAY', group='ippppa', required='system_use_recapitalization=1', constraints='LENGTH_EQUAL=cf_length')
    dispatch_factor1: float = INPUT(label='Dispatch payment factor 1', type='NUMBER', group='ippppa', required='market=0')
    dispatch_factor2: float = INPUT(label='Dispatch payment factor 2', type='NUMBER', group='ippppa', required='market=0')
    dispatch_factor3: float = INPUT(label='Dispatch payment factor 3', type='NUMBER', group='ippppa', required='market=0')
    dispatch_factor4: float = INPUT(label='Dispatch payment factor 4', type='NUMBER', group='ippppa', required='market=0')
    dispatch_factor5: float = INPUT(label='Dispatch payment factor 5', type='NUMBER', group='ippppa', required='market=0')
    dispatch_factor6: float = INPUT(label='Dispatch payment factor 6', type='NUMBER', group='ippppa', required='market=0')
    dispatch_factor7: float = INPUT(label='Dispatch payment factor 7', type='NUMBER', group='ippppa', required='market=0')
    dispatch_factor8: float = INPUT(label='Dispatch payment factor 8', type='NUMBER', group='ippppa', required='market=0')
    dispatch_factor9: float = INPUT(label='Dispatch payment factor 9', type='NUMBER', group='ippppa', required='market=0')
    dispatch_sched_weekday: Matrix = INPUT(label='Diurnal weekday dispatch periods', units='1..9', type='MATRIX', group='ippppa', required='market=0', meta='12 x 24 matrix')
    dispatch_sched_weekend: Matrix = INPUT(label='Diurnal weekend dispatch periods', units='1..9', type='MATRIX', group='ippppa', required='market=0', meta='12 x 24 matrix')
    cf_energy_net_jan: Final[Array] = OUTPUT(label='Energy produced by the system in January', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_jan: Final[Array] = OUTPUT(label='Revenue from the system in January', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_feb: Final[Array] = OUTPUT(label='Energy produced by the system in February', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_feb: Final[Array] = OUTPUT(label='Revenue from the system in February', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_mar: Final[Array] = OUTPUT(label='Energy produced by the system in March', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_mar: Final[Array] = OUTPUT(label='Revenue from the system in March', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_apr: Final[Array] = OUTPUT(label='Energy produced by the system in April', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_apr: Final[Array] = OUTPUT(label='Revenue from the system in April', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_may: Final[Array] = OUTPUT(label='Energy produced by the system in May', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_may: Final[Array] = OUTPUT(label='Revenue from the system in May', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_jun: Final[Array] = OUTPUT(label='Energy produced by the system in June', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_jun: Final[Array] = OUTPUT(label='Revenue from the system in June', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_jul: Final[Array] = OUTPUT(label='Energy produced by the system in July', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_jul: Final[Array] = OUTPUT(label='Revenue from the system in July', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_aug: Final[Array] = OUTPUT(label='Energy produced by the system in August', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_aug: Final[Array] = OUTPUT(label='Revenue from the system in August', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_sep: Final[Array] = OUTPUT(label='Energy produced by the system in September', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_sep: Final[Array] = OUTPUT(label='Revenue from the system in September', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_oct: Final[Array] = OUTPUT(label='Energy produced by the system in October', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_oct: Final[Array] = OUTPUT(label='Revenue from the system in October', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_nov: Final[Array] = OUTPUT(label='Energy produced by the system in November', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_nov: Final[Array] = OUTPUT(label='Revenue from the system in November', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dec: Final[Array] = OUTPUT(label='Energy produced by the system in December', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dec: Final[Array] = OUTPUT(label='Revenue from the system in December', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch1: Final[Array] = OUTPUT(label='Energy produced by the system in dispatch period 1', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch1: Final[Array] = OUTPUT(label='Revenue from the system in dispatch period 1', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch2: Final[Array] = OUTPUT(label='Energy produced by the system in dispatch period 2', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch2: Final[Array] = OUTPUT(label='Revenue from the system in dispatch period 2', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch3: Final[Array] = OUTPUT(label='Energy produced by the system in dispatch period 3', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch3: Final[Array] = OUTPUT(label='Revenue from the system in dispatch period 3', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch4: Final[Array] = OUTPUT(label='Energy produced by the system in dispatch period 4', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch4: Final[Array] = OUTPUT(label='Revenue from the system in dispatch period 4', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch5: Final[Array] = OUTPUT(label='Energy produced by the system in dispatch period 5', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch5: Final[Array] = OUTPUT(label='Revenue from the system in dispatch period 5', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch6: Final[Array] = OUTPUT(label='Energy produced by the system in dispatch period 6', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch6: Final[Array] = OUTPUT(label='Revenue from the system in dispatch period 6', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch7: Final[Array] = OUTPUT(label='Energy produced by the system in dispatch period 7', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch7: Final[Array] = OUTPUT(label='Revenue from the system in dispatch period 7', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch8: Final[Array] = OUTPUT(label='Energy produced by the system in dispatch period 8', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch8: Final[Array] = OUTPUT(label='Revenue from the system in dispatch period 8', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch9: Final[Array] = OUTPUT(label='Energy produced by the system in dispatch period 9', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch9: Final[Array] = OUTPUT(label='Revenue from the system in dispatch period 9', type='ARRAY', group='ippppa', required='market=0', constraints='LENGTH_EQUAL=cf_length')
    firstyear_revenue_dispatch1: Final[float] = OUTPUT(label='First year revenue from the system in dispatch period 1', type='NUMBER', group='ippppa', required='market=0')
    firstyear_revenue_dispatch2: Final[float] = OUTPUT(label='First year revenue from the system in dispatch period 2', type='NUMBER', group='ippppa', required='market=0')
    firstyear_revenue_dispatch3: Final[float] = OUTPUT(label='First year revenue from the system in dispatch period 3', type='NUMBER', group='ippppa', required='market=0')
    firstyear_revenue_dispatch4: Final[float] = OUTPUT(label='First year revenue from the system in dispatch period 4', type='NUMBER', group='ippppa', required='market=0')
    firstyear_revenue_dispatch5: Final[float] = OUTPUT(label='First year revenue from the system in dispatch period 5', type='NUMBER', group='ippppa', required='market=0')
    firstyear_revenue_dispatch6: Final[float] = OUTPUT(label='First year revenue from the system in dispatch period 6', type='NUMBER', group='ippppa', required='market=0')
    firstyear_revenue_dispatch7: Final[float] = OUTPUT(label='First year revenue from the system in dispatch period 7', type='NUMBER', group='ippppa', required='market=0')
    firstyear_revenue_dispatch8: Final[float] = OUTPUT(label='First year revenue from the system in dispatch period 8', type='NUMBER', group='ippppa', required='market=0')
    firstyear_revenue_dispatch9: Final[float] = OUTPUT(label='First year revenue from the system in dispatch period 9', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_dispatch1: Final[float] = OUTPUT(label='First year energy from the system in dispatch period 1', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_dispatch2: Final[float] = OUTPUT(label='First year energy from the system in dispatch period 2', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_dispatch3: Final[float] = OUTPUT(label='First year energy from the system in dispatch period 3', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_dispatch4: Final[float] = OUTPUT(label='First year energy from the system in dispatch period 4', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_dispatch5: Final[float] = OUTPUT(label='First year energy from the system in dispatch period 5', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_dispatch6: Final[float] = OUTPUT(label='First year energy from the system in dispatch period 6', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_dispatch7: Final[float] = OUTPUT(label='First year energy from the system in dispatch period 7', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_dispatch8: Final[float] = OUTPUT(label='First year energy from the system in dispatch period 8', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_dispatch9: Final[float] = OUTPUT(label='First year energy from the system in dispatch period 9', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_price1: Final[float] = OUTPUT(label='First year energy price dispatch period 1', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_price2: Final[float] = OUTPUT(label='First year energy price dispatch period 2', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_price3: Final[float] = OUTPUT(label='First year energy price dispatch period 3', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_price4: Final[float] = OUTPUT(label='First year energy price dispatch period 4', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_price5: Final[float] = OUTPUT(label='First year energy price dispatch period 5', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_price6: Final[float] = OUTPUT(label='First year energy price dispatch period 6', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_price7: Final[float] = OUTPUT(label='First year energy price dispatch period 7', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_price8: Final[float] = OUTPUT(label='First year energy price dispatch period 8', type='NUMBER', group='ippppa', required='market=0')
    firstyear_energy_price9: Final[float] = OUTPUT(label='First year energy price dispatch period 9', type='NUMBER', group='ippppa', required='market=0')
    cf_revenue_monthly_firstyear_TOD1: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD1', type='ARRAY', group='ippppa', required='market=0')
    cf_energy_net_monthly_firstyear_TOD1: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD1', type='ARRAY', group='ippppa', required='market=0')
    cf_revenue_monthly_firstyear_TOD2: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD2', type='ARRAY', group='ippppa', required='market=0')
    cf_energy_net_monthly_firstyear_TOD2: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD2', type='ARRAY', group='ippppa', required='market=0')
    cf_revenue_monthly_firstyear_TOD3: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD3', type='ARRAY', group='ippppa', required='market=0')
    cf_energy_net_monthly_firstyear_TOD3: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD3', type='ARRAY', group='ippppa', required='market=0')
    cf_revenue_monthly_firstyear_TOD4: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD4', type='ARRAY', group='ippppa', required='market=0')
    cf_energy_net_monthly_firstyear_TOD4: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD4', type='ARRAY', group='ippppa', required='market=0')
    cf_revenue_monthly_firstyear_TOD5: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD5', type='ARRAY', group='ippppa', required='market=0')
    cf_energy_net_monthly_firstyear_TOD5: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD5', type='ARRAY', group='ippppa', required='market=0')
    cf_revenue_monthly_firstyear_TOD6: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD6', type='ARRAY', group='ippppa', required='market=0')
    cf_energy_net_monthly_firstyear_TOD6: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD6', type='ARRAY', group='ippppa', required='market=0')
    cf_revenue_monthly_firstyear_TOD7: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD7', type='ARRAY', group='ippppa', required='market=0')
    cf_energy_net_monthly_firstyear_TOD7: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD7', type='ARRAY', group='ippppa', required='market=0')
    cf_revenue_monthly_firstyear_TOD8: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD8', type='ARRAY', group='ippppa', required='market=0')
    cf_energy_net_monthly_firstyear_TOD8: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD8', type='ARRAY', group='ippppa', required='market=0')
    cf_revenue_monthly_firstyear_TOD9: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD9', type='ARRAY', group='ippppa', required='market=0')
    cf_energy_net_monthly_firstyear_TOD9: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD9', type='ARRAY', group='ippppa', required='market=0')
    cf_length: Final[float] = OUTPUT(label='Number of periods in cashflow', type='NUMBER', group='ippppa', required='*', constraints='INTEGER')
    lcoe_real: Final[float] = OUTPUT(label='Real LCOE', units='cents/kWh', type='NUMBER', group='ippppa', required='*')
    lcoe_nom: Final[float] = OUTPUT(label='Nominal LCOE', units='cents/kWh', type='NUMBER', group='ippppa', required='*')
    lppa_real: Final[float] = OUTPUT(label='Real LPPA', units='cents/kWh', type='NUMBER', group='ippppa', required='*')
    lppa_nom: Final[float] = OUTPUT(label='Nominal LPPA', units='cents/kWh', type='NUMBER', group='ippppa', required='*')
    latcf_real: Final[float] = OUTPUT(label='Real LATCF', units='cents/kWh', type='NUMBER', group='ippppa', required='*')
    latcf_nom: Final[float] = OUTPUT(label='Nominal LATCF', units='cents/kWh', type='NUMBER', group='ippppa', required='*')
    npv: Final[float] = OUTPUT(label='Net present value', units='$', type='NUMBER', group='ippppa', required='*')
    ppa: Final[float] = OUTPUT(label='First year PPA', units='cents/kWh', type='NUMBER', group='ippppa', required='*')
    min_cashflow: Final[float] = OUTPUT(label='Minimum cash flow value', units='$', type='NUMBER', group='ippppa', required='*')
    irr: Final[float] = OUTPUT(label='Internal rate of return', units='%', type='NUMBER', group='ippppa', required='*')
    min_dscr: Final[float] = OUTPUT(label='Minimum DSCR', type='NUMBER', group='ippppa', required='*')
    actual_debt_frac: Final[float] = OUTPUT(label='Calculated debt fraction', units='%', type='NUMBER', group='ippppa', required='*')
    actual_ppa_escalation: Final[float] = OUTPUT(label='Calculated ppa escalation', units='%', type='NUMBER', group='ippppa', required='*')
    present_value_oandm: Final[float] = OUTPUT(label='Present value of O and M', units='$', type='NUMBER', group='ippppa', required='*')
    present_value_oandm_nonfuel: Final[float] = OUTPUT(label='Present value of non-fuel O and M', units='$', type='NUMBER', group='ippppa', required='*')
    present_value_fuel: Final[float] = OUTPUT(label='Present value of fuel O and M', units='$', type='NUMBER', group='ippppa', required='*')
    present_value_insandproptax: Final[float] = OUTPUT(label='Present value of Insurance and Prop Tax', units='$', type='NUMBER', group='ippppa', required='*')
    cf_energy_net: Final[Array] = OUTPUT(label='Energy', units='kWh', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_degradation: Final[Array] = OUTPUT(label='Energy degradation', units='kWh', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_value: Final[Array] = OUTPUT(label='Energy Value', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_price: Final[Array] = OUTPUT(label='Energy Price', units='$/kWh', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_fixed_expense: Final[Array] = OUTPUT(label='O&M fixed expense', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_production_expense: Final[Array] = OUTPUT(label='O&M production-based expense', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_capacity_expense: Final[Array] = OUTPUT(label='O&M capacity-based expense', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_fuel_expense: Final[Array] = OUTPUT(label='O&M fuel expense', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_opt_fuel_1_expense: Final[Array] = OUTPUT(label='O&M biomass feedstock expense', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_opt_fuel_2_expense: Final[Array] = OUTPUT(label='O&M coal feedstock expense', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_property_tax_assessed_value: Final[Array] = OUTPUT(label='Property tax net assessed value', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_property_tax_expense: Final[Array] = OUTPUT(label='Property tax expense', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_insurance_expense: Final[Array] = OUTPUT(label='Insurance expense', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_operating_expenses: Final[Array] = OUTPUT(label='Total operating expense', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_operating_income: Final[Array] = OUTPUT(label='Total operating income', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_net_salvage_value: Final[Array] = OUTPUT(label='Net Salvage Value', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_deductible_expenses: Final[Array] = OUTPUT(label='Deductible expenses', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_debt_balance: Final[Array] = OUTPUT(label='Debt balance', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_debt_payment_interest: Final[Array] = OUTPUT(label='Debt interest payment', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_debt_payment_principal: Final[Array] = OUTPUT(label='Debt principal payment', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_debt_payment_total: Final[Array] = OUTPUT(label='Debt total payment', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    ibi_total_fed: Final[float] = OUTPUT(label='Total federal IBI incentive income', units='$', type='NUMBER', group='ippppa', required='*')
    ibi_total_sta: Final[float] = OUTPUT(label='Total state IBI incentive income', units='$', type='NUMBER', group='ippppa', required='*')
    ibi_total_oth: Final[float] = OUTPUT(label='Total other IBI incentive income', units='$', type='NUMBER', group='ippppa', required='*')
    ibi_total_uti: Final[float] = OUTPUT(label='Total utility IBI incentive income', units='$', type='NUMBER', group='ippppa', required='*')
    ibi_total: Final[float] = OUTPUT(label='Total IBI incentive income', units='$', type='NUMBER', group='ippppa', required='*')
    cbi_total_fed: Final[float] = OUTPUT(label='Total federal CBI incentive income', units='$', type='NUMBER', group='ippppa', required='*')
    cbi_total_sta: Final[float] = OUTPUT(label='Total state CBI incentive income', units='$', type='NUMBER', group='ippppa', required='*')
    cbi_total_oth: Final[float] = OUTPUT(label='Total other CBI incentive income', units='$', type='NUMBER', group='ippppa', required='*')
    cbi_total_uti: Final[float] = OUTPUT(label='Total utility CBI incentive income', units='$', type='NUMBER', group='ippppa', required='*')
    cbi_total: Final[float] = OUTPUT(label='Total CBI incentive income', units='$', type='NUMBER', group='ippppa', required='*')
    cf_pbi_total_fed: Final[Array] = OUTPUT(label='Total federal PBI incentive income', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_pbi_total_sta: Final[Array] = OUTPUT(label='Total state PBI incentive income', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_pbi_total_oth: Final[Array] = OUTPUT(label='Total other PBI incentive income', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_pbi_total_uti: Final[Array] = OUTPUT(label='Total utility PBI incentive income', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_pbi_total: Final[Array] = OUTPUT(label='Total PBI incentive income', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_ptc_fed: Final[Array] = OUTPUT(label='Federal PTC income', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_ptc_sta: Final[Array] = OUTPUT(label='State PTC income', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_ptc_total: Final[Array] = OUTPUT(label='Total PTC income', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    itc_fed_total: Final[float] = OUTPUT(label='Federal ITC income', units='$', type='NUMBER', group='ippppa', required='*')
    itc_sta_total: Final[float] = OUTPUT(label='State ITC income', units='$', type='NUMBER', group='ippppa', required='*')
    itc_total: Final[float] = OUTPUT(label='Total ITC income', units='$', type='NUMBER', group='ippppa', required='*')
    cf_sta_depr_sched: Final[Array] = OUTPUT(label='State depreciation schedule', units='%', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_sta_depreciation: Final[Array] = OUTPUT(label='State depreciation', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_sta_incentive_income_less_deductions: Final[Array] = OUTPUT(label='State incentive income less deductions', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_sta_taxable_income_less_deductions: Final[Array] = OUTPUT(label='State taxable income less deductions', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_sta_tax_savings: Final[Array] = OUTPUT(label='State tax savings', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_sta_income_taxes: Final[Array] = OUTPUT(label='State Income Taxes', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_fed_depr_sched: Final[Array] = OUTPUT(label='Federal depreciation schedule', units='%', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_fed_depreciation: Final[Array] = OUTPUT(label='Federal depreciation', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_fed_incentive_income_less_deductions: Final[Array] = OUTPUT(label='Federal incentive income less deductions', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_fed_taxable_income_less_deductions: Final[Array] = OUTPUT(label='Federal taxable income less deductions', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_fed_tax_savings: Final[Array] = OUTPUT(label='Federal tax savings', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_fed_income_taxes: Final[Array] = OUTPUT(label='Federal Income Taxes', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_sta_and_fed_tax_savings: Final[Array] = OUTPUT(label='Total tax savings (Federal & State)', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_after_tax_net_equity_cash_flow: Final[Array] = OUTPUT(label='After-tax net equity cash flow', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_after_tax_net_equity_cost_flow: Final[Array] = OUTPUT(label='After-tax net equity cost flow', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_after_tax_cash_flow: Final[Array] = OUTPUT(label='After-tax cash flow', units='$', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_ppa_price: Final[Array] = OUTPUT(label='PPA price', units='cents/kWh', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_pretax_dscr: Final[Array] = OUTPUT(label='Pre-tax DSCR', type='ARRAY', group='ippppa', required='*', constraints='LENGTH_EQUAL=cf_length')
    lcoptc_fed_real: Final[float] = OUTPUT(label='Levelized Federal PTC (real)', units='cents/kWh', type='NUMBER', group='DHF', required='*')
    lcoptc_fed_nom: Final[float] = OUTPUT(label='Levelized Federal PTC (nominal)', units='cents/kWh', type='NUMBER', group='DHF', required='*')
    lcoptc_sta_real: Final[float] = OUTPUT(label='Levelized State PTC (real)', units='cents/kWh', type='NUMBER', group='DHF', required='*')
    lcoptc_sta_nom: Final[float] = OUTPUT(label='Levelized State PTC (nominal)', units='cents/kWh', type='NUMBER', group='DHF', required='*')
    wacc: Final[float] = OUTPUT(label='Weighted Average Cost of Capital (WACC)', type='NUMBER', group='DHF', required='*')
    effective_tax_rate: Final[float] = OUTPUT(label='Effective Tax Rate', type='NUMBER', group='DHF', required='*')

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
                 om_opt_fuel_1_usage: float = ...,
                 om_opt_fuel_1_cost: Array = ...,
                 om_opt_fuel_1_cost_escal: float = ...,
                 om_opt_fuel_2_usage: float = ...,
                 om_opt_fuel_2_cost: Array = ...,
                 om_opt_fuel_2_cost_escal: float = ...,
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
                 market: float = ...,
                 system_use_lifetime_output: float = ...,
                 gen: Array = ...,
                 degradation: Array = ...,
                 soln_mode: float = ...,
                 ppa_soln_tolerance: float = ...,
                 ppa_soln_min: float = ...,
                 ppa_soln_max: float = ...,
                 ppa_soln_max_iterations: float = ...,
                 bid_price: Array = ...,
                 bid_price_esc: float = ...,
                 construction_financing_cost: float = ...,
                 total_installed_cost: float = ...,
                 salvage_percentage: float = ...,
                 min_dscr_target: float = ...,
                 min_irr_target: float = ...,
                 ppa_escalation: float = ...,
                 min_dscr_required: float = ...,
                 positive_cashflow_required: float = ...,
                 optimize_lcoe_wrt_debt_fraction: float = ...,
                 optimize_lcoe_wrt_ppa_escalation: float = ...,
                 system_use_recapitalization: float = ...,
                 system_recapitalization_cost: float = ...,
                 system_recapitalization_escalation: float = ...,
                 system_recapitalization_boolean: Array = ...,
                 dispatch_factor1: float = ...,
                 dispatch_factor2: float = ...,
                 dispatch_factor3: float = ...,
                 dispatch_factor4: float = ...,
                 dispatch_factor5: float = ...,
                 dispatch_factor6: float = ...,
                 dispatch_factor7: float = ...,
                 dispatch_factor8: float = ...,
                 dispatch_factor9: float = ...,
                 dispatch_sched_weekday: Matrix = ...,
                 dispatch_sched_weekend: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
