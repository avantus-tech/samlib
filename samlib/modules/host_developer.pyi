
# This is a generated file

"""host_developer - Host Developer Financial Model_"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'ppa_soln_mode': float,
        'ppa_soln_tolerance': float,
        'ppa_soln_min': float,
        'ppa_soln_max': float,
        'ppa_soln_max_iterations': float,
        'ppa_price_input': Array,
        'ppa_escalation': float,
        'lppa_real': float,
        'lppa_nom': float,
        'ppa': float,
        'npv_ppa_revenue': float,
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
        'reserves_interest': float,
        'equip1_reserve_cost': float,
        'equip1_reserve_freq': float,
        'equip2_reserve_cost': float,
        'equip2_reserve_freq': float,
        'equip3_reserve_cost': float,
        'equip3_reserve_freq': float,
        'equip_reserve_depr_sta': float,
        'equip_reserve_depr_fed': float,
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
        'depr_alloc_macrs_5_percent': float,
        'depr_alloc_macrs_15_percent': float,
        'depr_alloc_sl_5_percent': float,
        'depr_alloc_sl_15_percent': float,
        'depr_alloc_sl_20_percent': float,
        'depr_alloc_sl_39_percent': float,
        'depr_alloc_custom_percent': float,
        'depr_custom_schedule': Array,
        'depr_bonus_sta': float,
        'depr_bonus_sta_macrs_5': float,
        'depr_bonus_sta_macrs_15': float,
        'depr_bonus_sta_sl_5': float,
        'depr_bonus_sta_sl_15': float,
        'depr_bonus_sta_sl_20': float,
        'depr_bonus_sta_sl_39': float,
        'depr_bonus_sta_custom': float,
        'depr_bonus_fed': float,
        'depr_bonus_fed_macrs_5': float,
        'depr_bonus_fed_macrs_15': float,
        'depr_bonus_fed_sl_5': float,
        'depr_bonus_fed_sl_15': float,
        'depr_bonus_fed_sl_20': float,
        'depr_bonus_fed_sl_39': float,
        'depr_bonus_fed_custom': float,
        'depr_itc_sta_macrs_5': float,
        'depr_itc_sta_macrs_15': float,
        'depr_itc_sta_sl_5': float,
        'depr_itc_sta_sl_15': float,
        'depr_itc_sta_sl_20': float,
        'depr_itc_sta_sl_39': float,
        'depr_itc_sta_custom': float,
        'depr_itc_fed_macrs_5': float,
        'depr_itc_fed_macrs_15': float,
        'depr_itc_fed_sl_5': float,
        'depr_itc_fed_sl_15': float,
        'depr_itc_fed_sl_20': float,
        'depr_itc_fed_sl_39': float,
        'depr_itc_fed_custom': float,
        'cf_stadepr_macrs_5': Array,
        'cf_stadepr_macrs_15': Array,
        'cf_stadepr_sl_5': Array,
        'cf_stadepr_sl_15': Array,
        'cf_stadepr_sl_20': Array,
        'cf_stadepr_sl_39': Array,
        'cf_stadepr_custom': Array,
        'cf_stadepr_me1': Array,
        'cf_stadepr_me2': Array,
        'cf_stadepr_me3': Array,
        'cf_stadepr_total': Array,
        'cf_statax_income_prior_incentives': Array,
        'cf_statax_taxable_incentives': Array,
        'cf_statax_income_with_incentives': Array,
        'cf_statax': Array,
        'cf_feddepr_macrs_5': Array,
        'cf_feddepr_macrs_15': Array,
        'cf_feddepr_sl_5': Array,
        'cf_feddepr_sl_15': Array,
        'cf_feddepr_sl_20': Array,
        'cf_feddepr_sl_39': Array,
        'cf_feddepr_custom': Array,
        'cf_feddepr_me1': Array,
        'cf_feddepr_me2': Array,
        'cf_feddepr_me3': Array,
        'cf_feddepr_total': Array,
        'cf_fedtax_income_prior_incentives': Array,
        'cf_fedtax_taxable_incentives': Array,
        'cf_fedtax_income_with_incentives': Array,
        'cf_fedtax': Array,
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
        'term_tenor': float,
        'term_int_rate': float,
        'dscr': float,
        'dscr_reserve_months': float,
        'debt_percent': float,
        'debt_option': float,
        'payment_option': float,
        'cost_debt_closing': float,
        'cost_debt_fee': float,
        'months_working_reserve': float,
        'months_receivables_reserve': float,
        'cost_other_financing': float,
        'flip_target_percent': float,
        'flip_target_year': float,
        'pbi_fed_for_ds': float,
        'pbi_sta_for_ds': float,
        'pbi_uti_for_ds': float,
        'pbi_oth_for_ds': float,
        'debt_fraction': float,
        'flip_target_irr': float,
        'flip_actual_year': float,
        'flip_actual_irr': float,
        'lcoe_real': float,
        'lcoe_nom': float,
        'npv_energy_nom': float,
        'npv_energy_real': float,
        'present_value_oandm': float,
        'present_value_oandm_nonfuel': float,
        'present_value_fuel': float,
        'present_value_insandproptax': float,
        'lcoptc_fed_real': float,
        'lcoptc_fed_nom': float,
        'lcoptc_sta_real': float,
        'lcoptc_sta_nom': float,
        'wacc': float,
        'effective_tax_rate': float,
        'analysis_period_irr': float,
        'annual_energy_value': Array,
        'elec_cost_with_system': Array,
        'elec_cost_without_system': Array,
        'host_real_discount_rate': float,
        'cf_agreement_cost': Array,
        'cf_after_tax_net_equity_cost_flow': Array,
        'cf_after_tax_cash_flow': Array,
        'cf_payback_with_expenses': Array,
        'cf_cumulative_payback_with_expenses': Array,
        'npv': float,
        'cf_nte': Array,
        'host_nominal_discount_rate': float,
        'year1_nte': float,
        'lnte_real': float,
        'lnte_nom': float,
        'gen': Array,
        'degradation': Array,
        'roe_input': Array,
        'cf_return_on_equity': Array,
        'cf_return_on_equity_input': Array,
        'cf_return_on_equity_dollars': Array,
        'cf_lcog_costs': Array,
        'lcog_om': float,
        'lcog_depr': float,
        'lcog_loan_int': float,
        'lcog_wc_int': float,
        'lcog_roe': float,
        'lcog': float,
        'loan_moratorium': float,
        'system_use_recapitalization': float,
        'system_recapitalization_cost': float,
        'system_recapitalization_escalation': float,
        'system_lifetime_recapitalize': Array,
        'cf_recapitalization': Array,
        'system_use_lifetime_output': float,
        'ppa_multiplier_model': float,
        'dispatch_factors_ts': Array,
        'ppa_multipliers': Array,
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
        'total_installed_cost': float,
        'salvage_percentage': float,
        'construction_financing_cost': float,
        'cost_debt_upfront': float,
        'cost_financing': float,
        'cost_prefinancing': float,
        'cost_installed': float,
        'cost_installedperwatt': float,
        'nominal_discount_rate': float,
        'prop_tax_assessed_value': float,
        'salvage_value': float,
        'depr_alloc_none_percent': float,
        'depr_alloc_none': float,
        'depr_alloc_total': float,
        'depr_stabas_percent_macrs_5': float,
        'depr_alloc_macrs_5': float,
        'depr_stabas_ibi_reduc_macrs_5': float,
        'depr_stabas_cbi_reduc_macrs_5': float,
        'depr_stabas_prior_itc_macrs_5': float,
        'itc_sta_qual_macrs_5': float,
        'depr_stabas_percent_qual_macrs_5': float,
        'depr_stabas_percent_amount_macrs_5': float,
        'itc_disallow_sta_percent_macrs_5': float,
        'depr_stabas_fixed_amount_macrs_5': float,
        'itc_disallow_sta_fixed_macrs_5': float,
        'depr_stabas_itc_sta_reduction_macrs_5': float,
        'depr_stabas_itc_fed_reduction_macrs_5': float,
        'depr_stabas_after_itc_macrs_5': float,
        'depr_stabas_first_year_bonus_macrs_5': float,
        'depr_stabas_macrs_5': float,
        'depr_stabas_percent_macrs_15': float,
        'depr_alloc_macrs_15': float,
        'depr_stabas_ibi_reduc_macrs_15': float,
        'depr_stabas_cbi_reduc_macrs_15': float,
        'depr_stabas_prior_itc_macrs_15': float,
        'itc_sta_qual_macrs_15': float,
        'depr_stabas_percent_qual_macrs_15': float,
        'depr_stabas_percent_amount_macrs_15': float,
        'itc_disallow_sta_percent_macrs_15': float,
        'depr_stabas_fixed_amount_macrs_15': float,
        'itc_disallow_sta_fixed_macrs_15': float,
        'depr_stabas_itc_sta_reduction_macrs_15': float,
        'depr_stabas_itc_fed_reduction_macrs_15': float,
        'depr_stabas_after_itc_macrs_15': float,
        'depr_stabas_first_year_bonus_macrs_15': float,
        'depr_stabas_macrs_15': float,
        'depr_stabas_percent_sl_5': float,
        'depr_alloc_sl_5': float,
        'depr_stabas_ibi_reduc_sl_5': float,
        'depr_stabas_cbi_reduc_sl_5': float,
        'depr_stabas_prior_itc_sl_5': float,
        'itc_sta_qual_sl_5': float,
        'depr_stabas_percent_qual_sl_5': float,
        'depr_stabas_percent_amount_sl_5': float,
        'itc_disallow_sta_percent_sl_5': float,
        'depr_stabas_fixed_amount_sl_5': float,
        'itc_disallow_sta_fixed_sl_5': float,
        'depr_stabas_itc_sta_reduction_sl_5': float,
        'depr_stabas_itc_fed_reduction_sl_5': float,
        'depr_stabas_after_itc_sl_5': float,
        'depr_stabas_first_year_bonus_sl_5': float,
        'depr_stabas_sl_5': float,
        'depr_stabas_percent_sl_15': float,
        'depr_alloc_sl_15': float,
        'depr_stabas_ibi_reduc_sl_15': float,
        'depr_stabas_cbi_reduc_sl_15': float,
        'depr_stabas_prior_itc_sl_15': float,
        'itc_sta_qual_sl_15': float,
        'depr_stabas_percent_qual_sl_15': float,
        'depr_stabas_percent_amount_sl_15': float,
        'itc_disallow_sta_percent_sl_15': float,
        'depr_stabas_fixed_amount_sl_15': float,
        'itc_disallow_sta_fixed_sl_15': float,
        'depr_stabas_itc_sta_reduction_sl_15': float,
        'depr_stabas_itc_fed_reduction_sl_15': float,
        'depr_stabas_after_itc_sl_15': float,
        'depr_stabas_first_year_bonus_sl_15': float,
        'depr_stabas_sl_15': float,
        'depr_stabas_percent_sl_20': float,
        'depr_alloc_sl_20': float,
        'depr_stabas_ibi_reduc_sl_20': float,
        'depr_stabas_cbi_reduc_sl_20': float,
        'depr_stabas_prior_itc_sl_20': float,
        'itc_sta_qual_sl_20': float,
        'depr_stabas_percent_qual_sl_20': float,
        'depr_stabas_percent_amount_sl_20': float,
        'itc_disallow_sta_percent_sl_20': float,
        'depr_stabas_fixed_amount_sl_20': float,
        'itc_disallow_sta_fixed_sl_20': float,
        'depr_stabas_itc_sta_reduction_sl_20': float,
        'depr_stabas_itc_fed_reduction_sl_20': float,
        'depr_stabas_after_itc_sl_20': float,
        'depr_stabas_first_year_bonus_sl_20': float,
        'depr_stabas_sl_20': float,
        'depr_stabas_percent_sl_39': float,
        'depr_alloc_sl_39': float,
        'depr_stabas_ibi_reduc_sl_39': float,
        'depr_stabas_cbi_reduc_sl_39': float,
        'depr_stabas_prior_itc_sl_39': float,
        'itc_sta_qual_sl_39': float,
        'depr_stabas_percent_qual_sl_39': float,
        'depr_stabas_percent_amount_sl_39': float,
        'itc_disallow_sta_percent_sl_39': float,
        'depr_stabas_fixed_amount_sl_39': float,
        'itc_disallow_sta_fixed_sl_39': float,
        'depr_stabas_itc_sta_reduction_sl_39': float,
        'depr_stabas_itc_fed_reduction_sl_39': float,
        'depr_stabas_after_itc_sl_39': float,
        'depr_stabas_first_year_bonus_sl_39': float,
        'depr_stabas_sl_39': float,
        'depr_stabas_percent_custom': float,
        'depr_alloc_custom': float,
        'depr_stabas_ibi_reduc_custom': float,
        'depr_stabas_cbi_reduc_custom': float,
        'depr_stabas_prior_itc_custom': float,
        'itc_sta_qual_custom': float,
        'depr_stabas_percent_qual_custom': float,
        'depr_stabas_percent_amount_custom': float,
        'itc_disallow_sta_percent_custom': float,
        'depr_stabas_fixed_amount_custom': float,
        'itc_disallow_sta_fixed_custom': float,
        'depr_stabas_itc_sta_reduction_custom': float,
        'depr_stabas_itc_fed_reduction_custom': float,
        'depr_stabas_after_itc_custom': float,
        'depr_stabas_first_year_bonus_custom': float,
        'depr_stabas_custom': float,
        'depr_stabas_percent_total': float,
        'depr_stabas_ibi_reduc_total': float,
        'depr_stabas_cbi_reduc_total': float,
        'depr_stabas_prior_itc_total': float,
        'itc_sta_qual_total': float,
        'depr_stabas_percent_qual_total': float,
        'depr_stabas_percent_amount_total': float,
        'itc_disallow_sta_percent_total': float,
        'depr_stabas_fixed_amount_total': float,
        'itc_disallow_sta_fixed_total': float,
        'depr_stabas_itc_sta_reduction_total': float,
        'depr_stabas_itc_fed_reduction_total': float,
        'depr_stabas_after_itc_total': float,
        'depr_stabas_first_year_bonus_total': float,
        'depr_stabas_total': float,
        'itc_sta_percent_total': float,
        'itc_sta_fixed_total': float,
        'depr_fedbas_percent_macrs_5': float,
        'depr_fedbas_ibi_reduc_macrs_5': float,
        'depr_fedbas_cbi_reduc_macrs_5': float,
        'depr_fedbas_prior_itc_macrs_5': float,
        'itc_fed_qual_macrs_5': float,
        'depr_fedbas_percent_qual_macrs_5': float,
        'depr_fedbas_percent_amount_macrs_5': float,
        'itc_disallow_fed_percent_macrs_5': float,
        'depr_fedbas_fixed_amount_macrs_5': float,
        'itc_disallow_fed_fixed_macrs_5': float,
        'depr_fedbas_itc_sta_reduction_macrs_5': float,
        'depr_fedbas_itc_fed_reduction_macrs_5': float,
        'depr_fedbas_after_itc_macrs_5': float,
        'depr_fedbas_first_year_bonus_macrs_5': float,
        'depr_fedbas_macrs_5': float,
        'depr_fedbas_percent_macrs_15': float,
        'depr_fedbas_ibi_reduc_macrs_15': float,
        'depr_fedbas_cbi_reduc_macrs_15': float,
        'depr_fedbas_prior_itc_macrs_15': float,
        'itc_fed_qual_macrs_15': float,
        'depr_fedbas_percent_qual_macrs_15': float,
        'depr_fedbas_percent_amount_macrs_15': float,
        'itc_disallow_fed_percent_macrs_15': float,
        'depr_fedbas_fixed_amount_macrs_15': float,
        'itc_disallow_fed_fixed_macrs_15': float,
        'depr_fedbas_itc_sta_reduction_macrs_15': float,
        'depr_fedbas_itc_fed_reduction_macrs_15': float,
        'depr_fedbas_after_itc_macrs_15': float,
        'depr_fedbas_first_year_bonus_macrs_15': float,
        'depr_fedbas_macrs_15': float,
        'depr_fedbas_percent_sl_5': float,
        'depr_fedbas_ibi_reduc_sl_5': float,
        'depr_fedbas_cbi_reduc_sl_5': float,
        'depr_fedbas_prior_itc_sl_5': float,
        'itc_fed_qual_sl_5': float,
        'depr_fedbas_percent_qual_sl_5': float,
        'depr_fedbas_percent_amount_sl_5': float,
        'itc_disallow_fed_percent_sl_5': float,
        'depr_fedbas_fixed_amount_sl_5': float,
        'itc_disallow_fed_fixed_sl_5': float,
        'depr_fedbas_itc_sta_reduction_sl_5': float,
        'depr_fedbas_itc_fed_reduction_sl_5': float,
        'depr_fedbas_after_itc_sl_5': float,
        'depr_fedbas_first_year_bonus_sl_5': float,
        'depr_fedbas_sl_5': float,
        'depr_fedbas_percent_sl_15': float,
        'depr_fedbas_ibi_reduc_sl_15': float,
        'depr_fedbas_cbi_reduc_sl_15': float,
        'depr_fedbas_prior_itc_sl_15': float,
        'itc_fed_qual_sl_15': float,
        'depr_fedbas_percent_qual_sl_15': float,
        'depr_fedbas_percent_amount_sl_15': float,
        'itc_disallow_fed_percent_sl_15': float,
        'depr_fedbas_fixed_amount_sl_15': float,
        'itc_disallow_fed_fixed_sl_15': float,
        'depr_fedbas_itc_sta_reduction_sl_15': float,
        'depr_fedbas_itc_fed_reduction_sl_15': float,
        'depr_fedbas_after_itc_sl_15': float,
        'depr_fedbas_first_year_bonus_sl_15': float,
        'depr_fedbas_sl_15': float,
        'depr_fedbas_percent_sl_20': float,
        'depr_fedbas_ibi_reduc_sl_20': float,
        'depr_fedbas_cbi_reduc_sl_20': float,
        'depr_fedbas_prior_itc_sl_20': float,
        'itc_fed_qual_sl_20': float,
        'depr_fedbas_percent_qual_sl_20': float,
        'depr_fedbas_percent_amount_sl_20': float,
        'itc_disallow_fed_percent_sl_20': float,
        'depr_fedbas_fixed_amount_sl_20': float,
        'itc_disallow_fed_fixed_sl_20': float,
        'depr_fedbas_itc_sta_reduction_sl_20': float,
        'depr_fedbas_itc_fed_reduction_sl_20': float,
        'depr_fedbas_after_itc_sl_20': float,
        'depr_fedbas_first_year_bonus_sl_20': float,
        'depr_fedbas_sl_20': float,
        'depr_fedbas_percent_sl_39': float,
        'depr_fedbas_ibi_reduc_sl_39': float,
        'depr_fedbas_cbi_reduc_sl_39': float,
        'depr_fedbas_prior_itc_sl_39': float,
        'itc_fed_qual_sl_39': float,
        'depr_fedbas_percent_qual_sl_39': float,
        'depr_fedbas_percent_amount_sl_39': float,
        'itc_disallow_fed_percent_sl_39': float,
        'depr_fedbas_fixed_amount_sl_39': float,
        'itc_disallow_fed_fixed_sl_39': float,
        'depr_fedbas_itc_sta_reduction_sl_39': float,
        'depr_fedbas_itc_fed_reduction_sl_39': float,
        'depr_fedbas_after_itc_sl_39': float,
        'depr_fedbas_first_year_bonus_sl_39': float,
        'depr_fedbas_sl_39': float,
        'depr_fedbas_percent_custom': float,
        'depr_fedbas_ibi_reduc_custom': float,
        'depr_fedbas_cbi_reduc_custom': float,
        'depr_fedbas_prior_itc_custom': float,
        'itc_fed_qual_custom': float,
        'depr_fedbas_percent_qual_custom': float,
        'depr_fedbas_percent_amount_custom': float,
        'itc_disallow_fed_percent_custom': float,
        'depr_fedbas_fixed_amount_custom': float,
        'itc_disallow_fed_fixed_custom': float,
        'depr_fedbas_itc_sta_reduction_custom': float,
        'depr_fedbas_itc_fed_reduction_custom': float,
        'depr_fedbas_after_itc_custom': float,
        'depr_fedbas_first_year_bonus_custom': float,
        'depr_fedbas_custom': float,
        'depr_fedbas_percent_total': float,
        'depr_fedbas_ibi_reduc_total': float,
        'depr_fedbas_cbi_reduc_total': float,
        'depr_fedbas_prior_itc_total': float,
        'itc_fed_qual_total': float,
        'depr_fedbas_percent_qual_total': float,
        'depr_fedbas_percent_amount_total': float,
        'itc_disallow_fed_percent_total': float,
        'depr_fedbas_fixed_amount_total': float,
        'itc_disallow_fed_fixed_total': float,
        'depr_fedbas_itc_sta_reduction_total': float,
        'depr_fedbas_itc_fed_reduction_total': float,
        'depr_fedbas_after_itc_total': float,
        'depr_fedbas_first_year_bonus_total': float,
        'depr_fedbas_total': float,
        'itc_fed_percent_total': float,
        'itc_fed_fixed_total': float,
        'depr_stabas_method': float,
        'depr_fedbas_method': float,
        'cash_for_debt_service': float,
        'pv_cafds': float,
        'size_of_debt': float,
        'size_of_equity': float,
        'cf_length': float,
        'ppa_price': float,
        'cf_energy_net': Array,
        'cf_ppa_price': Array,
        'cf_energy_value': Array,
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
        'cf_net_salvage_value': Array,
        'cf_total_revenue': Array,
        'cf_ebitda': Array,
        'cf_reserve_debtservice': Array,
        'cf_reserve_om': Array,
        'cf_reserve_receivables': Array,
        'cf_reserve_equip1': Array,
        'cf_reserve_equip2': Array,
        'cf_reserve_equip3': Array,
        'cf_reserve_total': Array,
        'cf_reserve_interest': Array,
        'cf_funding_debtservice': Array,
        'cf_funding_om': Array,
        'cf_funding_receivables': Array,
        'cf_funding_equip1': Array,
        'cf_funding_equip2': Array,
        'cf_funding_equip3': Array,
        'cf_disbursement_debtservice': Array,
        'cf_disbursement_om': Array,
        'cf_disbursement_receivables': Array,
        'cf_disbursement_equip1': Array,
        'cf_disbursement_equip2': Array,
        'cf_disbursement_equip3': Array,
        'cf_cash_for_ds': Array,
        'cf_pv_interest_factor': Array,
        'cf_pv_cash_for_ds': Array,
        'cf_debt_size': Array,
        'cf_debt_balance': Array,
        'cf_debt_payment_interest': Array,
        'cf_debt_payment_principal': Array,
        'cf_debt_payment_total': Array,
        'cf_project_operating_activities': Array,
        'purchase_of_property': float,
        'cf_project_dsra': Array,
        'cf_project_wcra': Array,
        'cf_project_receivablesra': Array,
        'cf_project_me1ra': Array,
        'cf_project_me2ra': Array,
        'cf_project_me3ra': Array,
        'cf_project_ra': Array,
        'cf_project_me1cs': Array,
        'cf_project_me2cs': Array,
        'cf_project_me3cs': Array,
        'cf_project_mecs': Array,
        'cf_project_investing_activities': Array,
        'issuance_of_equity': float,
        'cf_project_financing_activities': Array,
        'cf_pretax_cashflow': Array,
        'cf_project_return_pretax': Array,
        'cf_project_return_pretax_irr': Array,
        'cf_project_return_pretax_npv': Array,
        'cf_project_return_aftertax_cash': Array,
        'cf_project_return_aftertax': Array,
        'cf_project_return_aftertax_irr': Array,
        'cf_project_return_aftertax_max_irr': Array,
        'cf_project_return_aftertax_npv': Array,
        'project_return_aftertax_irr': float,
        'project_return_aftertax_npv': float,
        'cf_annual_costs': Array,
        'npv_annual_costs': float,
        'adjusted_installed_cost': float,
        'min_dscr': float,
        'cf_pretax_dscr': Array,
        'en_batt': float,
        'batt_bank_replacement': Array,
        'batt_replacement_schedule': Array,
        'batt_replacement_option': float,
        'battery_per_kWh': float,
        'batt_computed_bank_capacity': float,
        'cf_battery_replacement_cost': Array,
        'cf_battery_replacement_cost_schedule': Array
}, total=False)

class Data(ssc.DataDict):
    ppa_soln_mode: float = INPUT(label='PPA solution mode', units='0/1', type='NUMBER', group='Revenue', required='?=0', constraints='INTEGER,MIN=0,MAX=1', meta='0=solve ppa,1=specify ppa')
    ppa_soln_tolerance: float = INPUT(label='PPA solution tolerance', type='NUMBER', group='Revenue', required='?=1e-5')
    ppa_soln_min: float = INPUT(label='PPA solution minimum ppa', units='cents/kWh', type='NUMBER', group='Revenue', required='?=0')
    ppa_soln_max: float = INPUT(label='PPA solution maximum ppa', units='cents/kWh', type='NUMBER', group='Revenue', required='?=100')
    ppa_soln_max_iterations: float = INPUT(label='PPA solution maximum number of iterations', type='NUMBER', group='Revenue', required='?=100', constraints='INTEGER,MIN=1')
    ppa_price_input: Array = INPUT(label='PPA price in first year', units='$/kWh', type='ARRAY', group='Revenue', required='*')
    ppa_escalation: float = INPUT(label='PPA escalation rate', units='%/year', type='NUMBER', group='Revenue', required='?=0')
    lppa_real: Final[float] = OUTPUT(label='Levelized PPA price (real)', units='cents/kWh', type='NUMBER', group='Metrics', required='*')
    lppa_nom: Final[float] = OUTPUT(label='Levelized PPA price (nominal)', units='cents/kWh', type='NUMBER', group='Metrics', required='*')
    ppa: Final[float] = OUTPUT(label='PPA price (Year 1)', units='cents/kWh', type='NUMBER', group='Metrics', required='*')
    npv_ppa_revenue: Final[float] = OUTPUT(label='Present value of PPA revenue', units='$', type='NUMBER', group='Metrics', required='*')
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
    reserves_interest: float = INPUT(label='Interest on reserves', units='%', type='NUMBER', group='Financial Parameters', required='?=1.75', constraints='MIN=0,MAX=100')
    equip1_reserve_cost: float = INPUT(label='Major equipment reserve 1 cost', units='$/W', type='NUMBER', group='Financial Parameters', required='?=0.25', constraints='MIN=0')
    equip1_reserve_freq: float = INPUT(label='Major equipment reserve 1 frequency', units='years', type='NUMBER', group='Financial Parameters', required='?=12', constraints='INTEGER,MIN=0')
    equip2_reserve_cost: float = INPUT(label='Major equipment reserve 2 cost', units='$/W', type='NUMBER', group='Financial Parameters', required='?=0', constraints='MIN=0')
    equip2_reserve_freq: float = INPUT(label='Major equipment reserve 2 frequency', units='years', type='NUMBER', group='Financial Parameters', required='?=15', constraints='INTEGER,MIN=0')
    equip3_reserve_cost: float = INPUT(label='Major equipment reserve 3 cost', units='$/W', type='NUMBER', group='Financial Parameters', required='?=0', constraints='MIN=0')
    equip3_reserve_freq: float = INPUT(label='Major equipment reserve 3 frequency', units='years', type='NUMBER', group='Financial Parameters', required='?=20', constraints='INTEGER,MIN=0')
    equip_reserve_depr_sta: float = INPUT(label='Major equipment reserve state depreciation', type='NUMBER', group='Financial Parameters', required='?=0', constraints='INTEGER,MIN=0,MAX=6', meta='0=5yr MACRS,1=15yr MACRS,2=5yr SL,3=15yr SL, 4=20yr SL,5=39yr SL,6=Custom')
    equip_reserve_depr_fed: float = INPUT(label='Major equipment reserve federal depreciation', type='NUMBER', group='Financial Parameters', required='?=0', constraints='INTEGER,MIN=0,MAX=6', meta='0=5yr MACRS,1=15yr MACRS,2=5yr SL,3=15yr SL, 4=20yr SL,5=39yr SL,6=Custom')
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
    depr_alloc_macrs_5_percent: float = INPUT(label='5-yr MACRS depreciation federal and state allocation', units='%', type='NUMBER', group='Depreciation', required='?=89', constraints='MIN=0,MAX=100')
    depr_alloc_macrs_15_percent: float = INPUT(label='15-yr MACRS depreciation federal and state allocation', units='%', type='NUMBER', group='Depreciation', required='?=1.5', constraints='MIN=0,MAX=100')
    depr_alloc_sl_5_percent: float = INPUT(label='5-yr straight line depreciation federal and state allocation', units='%', type='NUMBER', group='Depreciation', required='?=0', constraints='MIN=0,MAX=100')
    depr_alloc_sl_15_percent: float = INPUT(label='15-yr straight line depreciation federal and state allocation', units='%', type='NUMBER', group='Depreciation', required='?=3', constraints='MIN=0,MAX=100')
    depr_alloc_sl_20_percent: float = INPUT(label='20-yr straight line depreciation federal and state allocation', units='%', type='NUMBER', group='Depreciation', required='?=3', constraints='MIN=0,MAX=100')
    depr_alloc_sl_39_percent: float = INPUT(label='39-yr straight line depreciation federal and state allocation', units='%', type='NUMBER', group='Depreciation', required='?=0.5', constraints='MIN=0,MAX=100')
    depr_alloc_custom_percent: float = INPUT(label='Custom depreciation federal and state allocation', units='%', type='NUMBER', group='Depreciation', required='?=0', constraints='MIN=0,MAX=100')
    depr_custom_schedule: Array = INPUT(label='Custom depreciation schedule', units='%', type='ARRAY', group='Depreciation', required='*')
    depr_bonus_sta: float = INPUT(label='State bonus depreciation', units='%', type='NUMBER', group='Depreciation', required='?=0', constraints='MIN=0,MAX=100')
    depr_bonus_sta_macrs_5: float = INPUT(label='State bonus depreciation 5-yr MACRS', units='0/1', type='NUMBER', group='Depreciation', required='?=1', constraints='BOOLEAN')
    depr_bonus_sta_macrs_15: float = INPUT(label='State bonus depreciation 15-yr MACRS', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_bonus_sta_sl_5: float = INPUT(label='State bonus depreciation 5-yr straight line', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_bonus_sta_sl_15: float = INPUT(label='State bonus depreciation 15-yr straight line', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_bonus_sta_sl_20: float = INPUT(label='State bonus depreciation 20-yr straight line', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_bonus_sta_sl_39: float = INPUT(label='State bonus depreciation 39-yr straight line', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_bonus_sta_custom: float = INPUT(label='State bonus depreciation custom', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_bonus_fed: float = INPUT(label='Federal bonus depreciation', units='%', type='NUMBER', group='Depreciation', required='?=0', constraints='MIN=0,MAX=100')
    depr_bonus_fed_macrs_5: float = INPUT(label='Federal bonus depreciation 5-yr MACRS', units='0/1', type='NUMBER', group='Depreciation', required='?=1', constraints='BOOLEAN')
    depr_bonus_fed_macrs_15: float = INPUT(label='Federal bonus depreciation 15-yr MACRS', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_bonus_fed_sl_5: float = INPUT(label='Federal bonus depreciation 5-yr straight line', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_bonus_fed_sl_15: float = INPUT(label='Federal bonus depreciation 15-yr straight line', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_bonus_fed_sl_20: float = INPUT(label='Federal bonus depreciation 20-yr straight line', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_bonus_fed_sl_39: float = INPUT(label='Federal bonus depreciation 39-yr straight line', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_bonus_fed_custom: float = INPUT(label='Federal bonus depreciation custom', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_itc_sta_macrs_5: float = INPUT(label='State ITC depreciation 5-yr MACRS', units='0/1', type='NUMBER', group='Depreciation', required='?=1', constraints='BOOLEAN')
    depr_itc_sta_macrs_15: float = INPUT(label='State ITC depreciation 15-yr MACRS', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_itc_sta_sl_5: float = INPUT(label='State ITC depreciation 5-yr straight line', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_itc_sta_sl_15: float = INPUT(label='State ITC depreciation 15-yr straight line', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_itc_sta_sl_20: float = INPUT(label='State ITC depreciation 20-yr straight line', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_itc_sta_sl_39: float = INPUT(label='State ITC depreciation 39-yr straight line', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_itc_sta_custom: float = INPUT(label='State ITC depreciation custom', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_itc_fed_macrs_5: float = INPUT(label='Federal ITC depreciation 5-yr MACRS', units='0/1', type='NUMBER', group='Depreciation', required='?=1', constraints='BOOLEAN')
    depr_itc_fed_macrs_15: float = INPUT(label='Federal ITC depreciation 15-yr MACRS', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_itc_fed_sl_5: float = INPUT(label='Federal ITC depreciation 5-yr straight line', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_itc_fed_sl_15: float = INPUT(label='Federal ITC depreciation 15-yr straight line', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_itc_fed_sl_20: float = INPUT(label='Federal ITC depreciation 20-yr straight line', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_itc_fed_sl_39: float = INPUT(label='Federal ITC depreciation 39-yr straight line', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    depr_itc_fed_custom: float = INPUT(label='Federal ITC depreciation custom', units='0/1', type='NUMBER', group='Depreciation', required='?=0', constraints='BOOLEAN')
    cf_stadepr_macrs_5: Final[Array] = OUTPUT(label='State depreciation from 5-yr MACRS', units='$', type='ARRAY', group='Cash Flow State Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_stadepr_macrs_15: Final[Array] = OUTPUT(label='State depreciation from 15-yr MACRS', units='$', type='ARRAY', group='Cash Flow State Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_stadepr_sl_5: Final[Array] = OUTPUT(label='State depreciation from 5-yr straight line', units='$', type='ARRAY', group='Cash Flow State Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_stadepr_sl_15: Final[Array] = OUTPUT(label='State depreciation from 15-yr straight line', units='$', type='ARRAY', group='Cash Flow State Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_stadepr_sl_20: Final[Array] = OUTPUT(label='State depreciation from 20-yr straight line', units='$', type='ARRAY', group='Cash Flow State Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_stadepr_sl_39: Final[Array] = OUTPUT(label='State depreciation from 39-yr straight line', units='$', type='ARRAY', group='Cash Flow State Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_stadepr_custom: Final[Array] = OUTPUT(label='State depreciation from custom', units='$', type='ARRAY', group='Cash Flow State Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_stadepr_me1: Final[Array] = OUTPUT(label='State depreciation from major equipment 1', units='$', type='ARRAY', group='Cash Flow State Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_stadepr_me2: Final[Array] = OUTPUT(label='State depreciation from major equipment 2', units='$', type='ARRAY', group='Cash Flow State Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_stadepr_me3: Final[Array] = OUTPUT(label='State depreciation from major equipment 3', units='$', type='ARRAY', group='Cash Flow State Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_stadepr_total: Final[Array] = OUTPUT(label='Total state tax depreciation', units='$', type='ARRAY', group='Cash Flow State Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_statax_income_prior_incentives: Final[Array] = OUTPUT(label='State taxable income without incentives', units='$', type='ARRAY', group='Cash Flow State Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_statax_taxable_incentives: Final[Array] = OUTPUT(label='State taxable incentives', units='$', type='ARRAY', group='Cash Flow State Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_statax_income_with_incentives: Final[Array] = OUTPUT(label='State taxable income', units='$', type='ARRAY', group='Cash Flow State Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_statax: Final[Array] = OUTPUT(label='State tax benefit (liability)', units='$', type='ARRAY', group='Cash Flow State Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_feddepr_macrs_5: Final[Array] = OUTPUT(label='Federal depreciation from 5-yr MACRS', units='$', type='ARRAY', group='Cash Flow Federal Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_feddepr_macrs_15: Final[Array] = OUTPUT(label='Federal depreciation from 15-yr MACRS', units='$', type='ARRAY', group='Cash Flow Federal Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_feddepr_sl_5: Final[Array] = OUTPUT(label='Federal depreciation from 5-yr straight line', units='$', type='ARRAY', group='Cash Flow Federal Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_feddepr_sl_15: Final[Array] = OUTPUT(label='Federal depreciation from 15-yr straight line', units='$', type='ARRAY', group='Cash Flow Federal Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_feddepr_sl_20: Final[Array] = OUTPUT(label='Federal depreciation from 20-yr straight line', units='$', type='ARRAY', group='Cash Flow Federal Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_feddepr_sl_39: Final[Array] = OUTPUT(label='Federal depreciation from 39-yr straight line', units='$', type='ARRAY', group='Cash Flow Federal Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_feddepr_custom: Final[Array] = OUTPUT(label='Federal depreciation from custom', units='$', type='ARRAY', group='Cash Flow Federal Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_feddepr_me1: Final[Array] = OUTPUT(label='Federal depreciation from major equipment 1', units='$', type='ARRAY', group='Cash Flow Federal Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_feddepr_me2: Final[Array] = OUTPUT(label='Federal depreciation from major equipment 2', units='$', type='ARRAY', group='Cash Flow Federal Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_feddepr_me3: Final[Array] = OUTPUT(label='Federal depreciation from major equipment 3', units='$', type='ARRAY', group='Cash Flow Federal Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_feddepr_total: Final[Array] = OUTPUT(label='Total federal tax depreciation', units='$', type='ARRAY', group='Cash Flow Federal Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_fedtax_income_prior_incentives: Final[Array] = OUTPUT(label='Federal taxable income without incentives', units='$', type='ARRAY', group='Cash Flow Federal Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_fedtax_taxable_incentives: Final[Array] = OUTPUT(label='Federal taxable incentives', units='$', type='ARRAY', group='Cash Flow Federal Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_fedtax_income_with_incentives: Final[Array] = OUTPUT(label='Federal taxable income', units='$', type='ARRAY', group='Cash Flow Federal Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_fedtax: Final[Array] = OUTPUT(label='Federal tax benefit (liability)', units='$', type='ARRAY', group='Cash Flow Federal Income Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
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
    term_tenor: float = INPUT(label='Term financing period', units='years', type='NUMBER', group='Financial Parameters', required='?=10', constraints='INTEGER,MIN=0')
    term_int_rate: float = INPUT(label='Term financing interest rate', units='%', type='NUMBER', group='Financial Parameters', required='?=8.5', constraints='MIN=0,MAX=100')
    dscr: float = INPUT(label='Debt service coverage ratio', type='NUMBER', group='Financial Parameters', required='?=1.5', constraints='MIN=0')
    dscr_reserve_months: float = INPUT(label='Debt service reserve account', units='months P&I', type='NUMBER', group='Financial Parameters', required='?=6', constraints='MIN=0')
    debt_percent: float = INPUT(label='Debt percent', units='%', type='NUMBER', group='Financial Parameters', required='?=50', constraints='MIN=0,MAX=100')
    debt_option: float = INPUT(label='Debt option', units='0/1', type='NUMBER', group='Financial Parameters', required='?=1', constraints='INTEGER,MIN=0,MAX=1', meta='0=debt percent,1=dscr')
    payment_option: float = INPUT(label='Debt repayment option', units='0/1', type='NUMBER', group='Financial Parameters', required='?=0', constraints='INTEGER,MIN=0,MAX=1', meta='0=Equal payments (standard amortization),1=Fixed principal declining interest')
    cost_debt_closing: float = INPUT(label='Debt closing cost', units='$', type='NUMBER', group='Financial Parameters', required='?=250000', constraints='MIN=0')
    cost_debt_fee: float = INPUT(label='Debt closing fee (% of total debt amount)', units='%', type='NUMBER', group='Financial Parameters', required='?=1.5', constraints='MIN=0')
    months_working_reserve: float = INPUT(label='Working capital reserve months of operating costs', units='months', type='NUMBER', group='Financial Parameters', required='?=6', constraints='MIN=0')
    months_receivables_reserve: float = INPUT(label='Receivables reserve months of PPA revenue', units='months', type='NUMBER', group='Financial Parameters', required='?=0', constraints='MIN=0')
    cost_other_financing: float = INPUT(label='Other financing cost', units='$', type='NUMBER', group='Financial Parameters', required='?=150000', constraints='MIN=0')
    flip_target_percent: float = INPUT(label='After-tax IRR target', units='%', type='NUMBER', group='Revenue', required='?=11', constraints='MIN=0,MAX=100')
    flip_target_year: float = INPUT(label='IRR target year', units='Year', type='NUMBER', group='Revenue', required='?=11', constraints='MIN=1')
    pbi_fed_for_ds: float = INPUT(label='Federal PBI available for debt service', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    pbi_sta_for_ds: float = INPUT(label='State PBI available for debt service', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    pbi_uti_for_ds: float = INPUT(label='Utility PBI available for debt service', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    pbi_oth_for_ds: float = INPUT(label='Other PBI available for debt service', units='0/1', type='NUMBER', group='Payment Incentives', required='?=0', constraints='BOOLEAN')
    debt_fraction: Final[float] = OUTPUT(label='Debt percent', units='%', type='NUMBER', group='Metrics', required='*')
    flip_target_irr: Final[float] = OUTPUT(label='IRR target', units='%', type='NUMBER', group='Metrics', required='*')
    flip_actual_year: Final[float] = OUTPUT(label='Year target IRR was achieved', units='year', type='NUMBER', group='Metrics', required='*')
    flip_actual_irr: Final[float] = OUTPUT(label='IRR in target year', units='%', type='NUMBER', group='Metrics', required='*')
    lcoe_real: Final[float] = OUTPUT(label='Levelized cost (real)', units='cents/kWh', type='NUMBER', group='Metrics', required='*')
    lcoe_nom: Final[float] = OUTPUT(label='Levelized cost (nominal)', units='cents/kWh', type='NUMBER', group='Metrics', required='*')
    npv_energy_nom: Final[float] = OUTPUT(label='Present value of annual energy (nominal)', units='kWh', type='NUMBER', group='Metrics', required='*')
    npv_energy_real: Final[float] = OUTPUT(label='Present value of annual energy (real)', units='kWh', type='NUMBER', group='Metrics', required='*')
    present_value_oandm: Final[float] = OUTPUT(label='Present value of O&M', units='$', type='NUMBER', group='Metrics', required='*')
    present_value_oandm_nonfuel: Final[float] = OUTPUT(label='Present value of non-fuel O&M', units='$', type='NUMBER', group='Metrics', required='*')
    present_value_fuel: Final[float] = OUTPUT(label='Present value of fuel O&M', units='$', type='NUMBER', group='Metrics', required='*')
    present_value_insandproptax: Final[float] = OUTPUT(label='Present value of insurance and prop tax', units='$', type='NUMBER', group='Metrics', required='*')
    lcoptc_fed_real: Final[float] = OUTPUT(label='Levelized federal PTC (real)', units='cents/kWh', type='NUMBER', group='Metrics', required='*')
    lcoptc_fed_nom: Final[float] = OUTPUT(label='Levelized federal PTC (nominal)', units='cents/kWh', type='NUMBER', group='Metrics', required='*')
    lcoptc_sta_real: Final[float] = OUTPUT(label='Levelized state PTC (real)', units='cents/kWh', type='NUMBER', group='Metrics', required='*')
    lcoptc_sta_nom: Final[float] = OUTPUT(label='Levelized state PTC (nominal)', units='cents/kWh', type='NUMBER', group='Metrics', required='*')
    wacc: Final[float] = OUTPUT(label='Weighted average cost of capital (WACC)', units='$', type='NUMBER', group='Metrics', required='*')
    effective_tax_rate: Final[float] = OUTPUT(label='Effective tax rate', units='%', type='NUMBER', group='Metrics', required='*')
    analysis_period_irr: Final[float] = OUTPUT(label='IRR at end of analysis period', units='%', type='NUMBER', group='Metrics', required='*')
    annual_energy_value: Array = INPUT(label='Host energy value', units='$', type='ARRAY', group='Host', required='*')
    elec_cost_with_system: Array = INPUT(label='Host energy bill with system', units='$', type='ARRAY', group='Host', required='*')
    elec_cost_without_system: Array = INPUT(label='Host energy bill without system', units='$', type='ARRAY', group='Host', required='*')
    host_real_discount_rate: float = INPUT(label='Host real discount rate', units='%', type='NUMBER', group='Host', required='*')
    cf_agreement_cost: Final[Array] = OUTPUT(label='Host agreement cost', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_after_tax_net_equity_cost_flow: Final[Array] = OUTPUT(label='Host after-tax annual costs', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_after_tax_cash_flow: Final[Array] = OUTPUT(label='Host after-tax cash flow', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_payback_with_expenses: Final[Array] = OUTPUT(label='Host simple payback with expenses', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_cumulative_payback_with_expenses: Final[Array] = OUTPUT(label='Host cumulative simple payback with expenses', units='$', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    npv: Final[float] = OUTPUT(label='Host net present value', units='$', type='NUMBER', group='Cash Flow', required='*')
    cf_nte: Final[Array] = OUTPUT(label='Host indifference point by year', units='cents/kWh', type='ARRAY', group='Cash Flow', required='*', constraints='LENGTH_EQUAL=cf_length')
    host_nominal_discount_rate: Final[float] = OUTPUT(label='Host nominal discount rate', units='%', type='NUMBER', group='Intermediate Costs', required='*')
    year1_nte: Final[float] = OUTPUT(label='Host indifference point in Year 1', units='cents/kWh', type='NUMBER', group='Cash Flow', required='*')
    lnte_real: Final[float] = OUTPUT(label='Host indifference point real levelized value', units='cents/kWh', type='NUMBER', group='Cash Flow', required='*')
    lnte_nom: Final[float] = OUTPUT(label='Host indifference point nominal levelized value', units='cents/kWh', type='NUMBER', group='Cash Flow', required='*')
    gen: Array = INPUT(label='Power generated by renewable resource', units='kW', type='ARRAY', group='System Output', required='*')
    degradation: Array = INPUT(label='Annual energy degradation', type='ARRAY', group='System Output', required='*')
    roe_input: Array = INPUT(label='Return on equity', type='ARRAY', group='Return on Equity', required='?=20')
    cf_return_on_equity: Final[Array] = OUTPUT(label='Return on equity', units='$/kWh', type='ARRAY', group='Return on Equity', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_return_on_equity_input: Final[Array] = OUTPUT(label='Return on equity input', units='%', type='ARRAY', group='Return on Equity', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_return_on_equity_dollars: Final[Array] = OUTPUT(label='Return on equity dollars', units='$', type='ARRAY', group='Return on Equity', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_lcog_costs: Final[Array] = OUTPUT(label='Total LCOG costs', units='$', type='ARRAY', group='Return on Equity', required='*', constraints='LENGTH_EQUAL=cf_length')
    lcog_om: Final[float] = OUTPUT(label='LCOG O and M', units='cents/kWh', type='NUMBER', group='Return on Equity', required='*')
    lcog_depr: Final[float] = OUTPUT(label='LCOG depreciation', units='cents/kWh', type='NUMBER', group='Return on Equity', required='*')
    lcog_loan_int: Final[float] = OUTPUT(label='LCOG loan interest', units='cents/kWh', type='NUMBER', group='Return on Equity', required='*')
    lcog_wc_int: Final[float] = OUTPUT(label='LCOG working capital interest', units='cents/kWh', type='NUMBER', group='Return on Equity', required='*')
    lcog_roe: Final[float] = OUTPUT(label='LCOG return on equity', units='cents/kWh', type='NUMBER', group='Return on Equity', required='*')
    lcog: Final[float] = OUTPUT(label='LCOG Levelized cost of generation', units='cents/kWh', type='NUMBER', group='Return on Equity', required='*')
    loan_moratorium: float = INPUT(label='Loan moratorium period', units='years', type='NUMBER', group='Moratorium', required='?=0', constraints='INTEGER,MIN=0')
    system_use_recapitalization: float = INOUT(label='Recapitalization expenses', units='0/1', type='NUMBER', group='Recapitalization', required='?=0', constraints='INTEGER,MIN=0', meta='0=None,1=Recapitalize')
    system_recapitalization_cost: float = INPUT(label='Recapitalization cost', units='$', type='NUMBER', group='Recapitalization', required='?=0')
    system_recapitalization_escalation: float = INPUT(label='Recapitalization escalation (above inflation)', units='%', type='NUMBER', group='Recapitalization', required='?=0', constraints='MIN=0,MAX=100')
    system_lifetime_recapitalize: Array = INPUT(label='Recapitalization boolean', type='ARRAY', group='Recapitalization', required='?=0')
    cf_recapitalization: Final[Array] = OUTPUT(label='Recapitalization operating expense', units='$', type='ARRAY', group='Recapitalization', required='*', constraints='LENGTH_EQUAL=cf_length')
    system_use_lifetime_output: float = INPUT(label='Lifetime hourly system outputs', units='0/1', type='NUMBER', group='Time of Delivery', required='*', constraints='INTEGER,MIN=0', meta='0=hourly first year,1=hourly lifetime')
    ppa_multiplier_model: float = INPUT(label='PPA multiplier model', units='0/1', type='NUMBER', group='Time of Delivery', required='?=0', constraints='INTEGER,MIN=0', meta='0=diurnal,1=timestep')
    dispatch_factors_ts: Array = INPUT(label='Dispatch payment factor array', type='ARRAY', group='Time of Delivery', required='ppa_multiplier_model=1')
    ppa_multipliers: Final[Array] = OUTPUT(label='TOD factors', type='ARRAY', group='Time of Delivery', required='*')
    dispatch_factor1: float = INPUT(label='TOD factor for period 1', type='NUMBER', group='Time of Delivery', required='ppa_multiplier_model=0')
    dispatch_factor2: float = INPUT(label='TOD factor for period 2', type='NUMBER', group='Time of Delivery', required='ppa_multiplier_model=0')
    dispatch_factor3: float = INPUT(label='TOD factor for period 3', type='NUMBER', group='Time of Delivery', required='ppa_multiplier_model=0')
    dispatch_factor4: float = INPUT(label='TOD factor for period 4', type='NUMBER', group='Time of Delivery', required='ppa_multiplier_model=0')
    dispatch_factor5: float = INPUT(label='TOD factor for period 5', type='NUMBER', group='Time of Delivery', required='ppa_multiplier_model=0')
    dispatch_factor6: float = INPUT(label='TOD factor for period 6', type='NUMBER', group='Time of Delivery', required='ppa_multiplier_model=0')
    dispatch_factor7: float = INPUT(label='TOD factor for period 7', type='NUMBER', group='Time of Delivery', required='ppa_multiplier_model=0')
    dispatch_factor8: float = INPUT(label='TOD factor for period 8', type='NUMBER', group='Time of Delivery', required='ppa_multiplier_model=0')
    dispatch_factor9: float = INPUT(label='TOD factor for period 9', type='NUMBER', group='Time of Delivery', required='ppa_multiplier_model=0')
    dispatch_sched_weekday: Matrix = INPUT(label='Diurnal weekday TOD periods', units='1..9', type='MATRIX', group='Time of Delivery', required='ppa_multiplier_model=0', meta='12 x 24 matrix')
    dispatch_sched_weekend: Matrix = INPUT(label='Diurnal weekend TOD periods', units='1..9', type='MATRIX', group='Time of Delivery', required='ppa_multiplier_model=0', meta='12 x 24 matrix')
    cf_energy_net_jan: Final[Array] = OUTPUT(label='Energy produced by the system in January', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_jan: Final[Array] = OUTPUT(label='Revenue from the system in January', units='$', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_feb: Final[Array] = OUTPUT(label='Energy produced by the system in February', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_feb: Final[Array] = OUTPUT(label='Revenue from the system in February', units='$', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_mar: Final[Array] = OUTPUT(label='Energy produced by the system in March', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_mar: Final[Array] = OUTPUT(label='Revenue from the system in March', units='$', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_apr: Final[Array] = OUTPUT(label='Energy produced by the system in April', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_apr: Final[Array] = OUTPUT(label='Revenue from the system in April', units='$', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_may: Final[Array] = OUTPUT(label='Energy produced by the system in May', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_may: Final[Array] = OUTPUT(label='Revenue from the system in May', units='$', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_jun: Final[Array] = OUTPUT(label='Energy produced by the system in June', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_jun: Final[Array] = OUTPUT(label='Revenue from the system in June', units='$', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_jul: Final[Array] = OUTPUT(label='Energy produced by the system in July', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_jul: Final[Array] = OUTPUT(label='Revenue from the system in July', units='$', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_aug: Final[Array] = OUTPUT(label='Energy produced by the system in August', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_aug: Final[Array] = OUTPUT(label='Revenue from the system in August', units='$', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_sep: Final[Array] = OUTPUT(label='Energy produced by the system in September', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_sep: Final[Array] = OUTPUT(label='Revenue from the system in September', units='$', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_oct: Final[Array] = OUTPUT(label='Energy produced by the system in October', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_oct: Final[Array] = OUTPUT(label='Revenue from the system in October', units='$', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_nov: Final[Array] = OUTPUT(label='Energy produced by the system in November', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_nov: Final[Array] = OUTPUT(label='Revenue from the system in November', units='$', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dec: Final[Array] = OUTPUT(label='Energy produced by the system in December', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dec: Final[Array] = OUTPUT(label='Revenue from the system in December', units='$', type='ARRAY', group='Cash Flow Revenue', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch1: Final[Array] = OUTPUT(label='Energy produced by the system in TOD period 1', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch1: Final[Array] = OUTPUT(label='Revenue from the system in TOD period 1', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch2: Final[Array] = OUTPUT(label='Energy produced by the system in TOD period 2', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch2: Final[Array] = OUTPUT(label='Revenue from the system in TOD period 2', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch3: Final[Array] = OUTPUT(label='Energy produced by the system in TOD period 3', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch3: Final[Array] = OUTPUT(label='Revenue from the system in TOD period 3', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch4: Final[Array] = OUTPUT(label='Energy produced by the system in TOD period 4', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch4: Final[Array] = OUTPUT(label='Revenue from the system in TOD period 4', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch5: Final[Array] = OUTPUT(label='Energy produced by the system in TOD period 5', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch5: Final[Array] = OUTPUT(label='Revenue from the system in TOD period 5', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch6: Final[Array] = OUTPUT(label='Energy produced by the system in TOD period 6', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch6: Final[Array] = OUTPUT(label='Revenue from the system in TOD period 6', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch7: Final[Array] = OUTPUT(label='Energy produced by the system in TOD period 7', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch7: Final[Array] = OUTPUT(label='Revenue from the system in TOD period 7', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch8: Final[Array] = OUTPUT(label='Energy produced by the system in TOD period 8', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch8: Final[Array] = OUTPUT(label='Revenue from the system in TOD period 8', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_net_dispatch9: Final[Array] = OUTPUT(label='Energy produced by the system in TOD period 9', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    cf_revenue_dispatch9: Final[Array] = OUTPUT(label='Revenue from the system in TOD period 9', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0', constraints='LENGTH_EQUAL=cf_length')
    firstyear_revenue_dispatch1: Final[float] = OUTPUT(label='First year revenue from the system in TOD period 1', units='$', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_revenue_dispatch2: Final[float] = OUTPUT(label='First year revenue from the system in TOD period 2', units='$', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_revenue_dispatch3: Final[float] = OUTPUT(label='First year revenue from the system in TOD period 3', units='$', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_revenue_dispatch4: Final[float] = OUTPUT(label='First year revenue from the system in TOD period 4', units='$', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_revenue_dispatch5: Final[float] = OUTPUT(label='First year revenue from the system in TOD period 5', units='$', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_revenue_dispatch6: Final[float] = OUTPUT(label='First year revenue from the system in TOD period 6', units='$', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_revenue_dispatch7: Final[float] = OUTPUT(label='First year revenue from the system in TOD period 7', units='$', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_revenue_dispatch8: Final[float] = OUTPUT(label='First year revenue from the system in TOD period 8', units='$', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_revenue_dispatch9: Final[float] = OUTPUT(label='First year revenue from the system in TOD period 9', units='$', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_dispatch1: Final[float] = OUTPUT(label='First year energy from the system in TOD period 1', units='kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_dispatch2: Final[float] = OUTPUT(label='First year energy from the system in TOD period 2', units='kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_dispatch3: Final[float] = OUTPUT(label='First year energy from the system in TOD period 3', units='kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_dispatch4: Final[float] = OUTPUT(label='First year energy from the system in TOD period 4', units='kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_dispatch5: Final[float] = OUTPUT(label='First year energy from the system in TOD period 5', units='kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_dispatch6: Final[float] = OUTPUT(label='First year energy from the system in TOD period 6', units='kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_dispatch7: Final[float] = OUTPUT(label='First year energy from the system in TOD period 7', units='kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_dispatch8: Final[float] = OUTPUT(label='First year energy from the system in TOD period 8', units='kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_dispatch9: Final[float] = OUTPUT(label='First year energy from the system in TOD period 9', units='kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_price1: Final[float] = OUTPUT(label='First year energy price for TOD period 1', units='cents/kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_price2: Final[float] = OUTPUT(label='First year energy price for TOD period 2', units='cents/kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_price3: Final[float] = OUTPUT(label='First year energy price for TOD period 3', units='cents/kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_price4: Final[float] = OUTPUT(label='First year energy price for TOD period 4', units='cents/kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_price5: Final[float] = OUTPUT(label='First year energy price for TOD period 5', units='cents/kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_price6: Final[float] = OUTPUT(label='First year energy price for TOD period 6', units='cents/kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_price7: Final[float] = OUTPUT(label='First year energy price for TOD period 7', units='cents/kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_price8: Final[float] = OUTPUT(label='First year energy price for TOD period 8', units='cents/kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    firstyear_energy_price9: Final[float] = OUTPUT(label='First year energy price for TOD period 9', units='cents/kWh', type='NUMBER', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_revenue_monthly_firstyear_TOD1: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD period 1', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_energy_net_monthly_firstyear_TOD1: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD period 1', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_revenue_monthly_firstyear_TOD2: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD period 2', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_energy_net_monthly_firstyear_TOD2: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD period 2', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_revenue_monthly_firstyear_TOD3: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD period 3', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_energy_net_monthly_firstyear_TOD3: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD period 3', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_revenue_monthly_firstyear_TOD4: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD period 4', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_energy_net_monthly_firstyear_TOD4: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD period 4', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_revenue_monthly_firstyear_TOD5: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD period 5', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_energy_net_monthly_firstyear_TOD5: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD period 5', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_revenue_monthly_firstyear_TOD6: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD period 6', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_energy_net_monthly_firstyear_TOD6: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD period 6', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_revenue_monthly_firstyear_TOD7: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD period 7', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_energy_net_monthly_firstyear_TOD7: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD period 7', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_revenue_monthly_firstyear_TOD8: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD period 8', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_energy_net_monthly_firstyear_TOD8: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD period 8', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_revenue_monthly_firstyear_TOD9: Final[Array] = OUTPUT(label='First year revenue from the system by month for TOD period 9', units='$', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    cf_energy_net_monthly_firstyear_TOD9: Final[Array] = OUTPUT(label='First year energy from the system by month for TOD period 9', units='kWh', type='ARRAY', group='Cash Flow Revenue', required='ppa_multiplier_model=0')
    total_installed_cost: float = INPUT(label='Installed cost', units='$', type='NUMBER', group='System Costs', required='*')
    salvage_percentage: float = INPUT(label='Net pre-tax cash salvage value', units='%', type='NUMBER', group='Financial Parameters', required='?=10', constraints='MIN=0,MAX=100')
    construction_financing_cost: float = INPUT(label='Construction financing total', units='$', type='NUMBER', group='Construction Financing', required='*')
    cost_debt_upfront: Final[float] = OUTPUT(label='Debt up-front fee', units='$', type='NUMBER', group='Intermediate Costs', required='?=0')
    cost_financing: Final[float] = OUTPUT(label='Financing cost', units='$', type='NUMBER', group='Intermediate Costs', required='*')
    cost_prefinancing: Final[float] = OUTPUT(label='Total installed cost', units='$', type='NUMBER', group='Intermediate Costs', required='*')
    cost_installed: Final[float] = OUTPUT(label='Net capital cost', units='$', type='NUMBER', group='Intermediate Costs', required='*')
    cost_installedperwatt: Final[float] = OUTPUT(label='Net capital cost per watt', units='$/W', type='NUMBER', group='Intermediate Costs', required='*')
    nominal_discount_rate: Final[float] = OUTPUT(label='Nominal discount rate', units='%', type='NUMBER', group='Intermediate Costs', required='*')
    prop_tax_assessed_value: Final[float] = OUTPUT(label='Assessed value of property for tax purposes', units='$', type='NUMBER', group='Intermediate Costs', required='*')
    salvage_value: Final[float] = OUTPUT(label='Net pre-tax cash salvage value', units='$', type='NUMBER', group='Intermediate Costs', required='*')
    depr_alloc_none_percent: Final[float] = OUTPUT(label='Non-depreciable federal and state allocation', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_alloc_none: Final[float] = OUTPUT(label='Non-depreciable federal and state allocation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_alloc_total: Final[float] = OUTPUT(label='Total depreciation federal and state allocation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS state percent of total depreciable basis', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_alloc_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS depreciation federal and state allocation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_ibi_reduc_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS state IBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_cbi_reduc_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS state CBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_prior_itc_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS state depreciation basis prior ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_sta_qual_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS depreciation state ITC adj qualifying costs', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_qual_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS state percent of qualifying costs', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_amount_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS depreciation ITC basis from state percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_sta_percent_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS depreciation ITC basis disallowance from state percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_fixed_amount_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS depreciation ITC basis from state fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_sta_fixed_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS depreciation ITC basis disallowance from state fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_itc_sta_reduction_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS state basis state ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_itc_fed_reduction_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS state basis federal ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_after_itc_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS state depreciation basis after ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_first_year_bonus_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS state first year bonus depreciation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS state depreciation basis', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS state percent of total depreciable basis', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_alloc_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS depreciation federal and state allocation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_ibi_reduc_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS state IBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_cbi_reduc_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS state CBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_prior_itc_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS state depreciation basis prior ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_sta_qual_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS depreciation state ITC adj qualifying costs', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_qual_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS state percent of qualifying costs', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_amount_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS depreciation ITC basis from state percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_sta_percent_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS depreciation ITC basis disallowance from state percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_fixed_amount_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS depreciation ITC basis from state fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_sta_fixed_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS depreciation ITC basis disallowance from state fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_itc_sta_reduction_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS state basis state ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_itc_fed_reduction_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS state basis federal ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_after_itc_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS state depreciation basis after ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_first_year_bonus_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS state first year bonus depreciation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS state depreciation basis', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_sl_5: Final[float] = OUTPUT(label='5-yr straight line state percent of total depreciable basis', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_alloc_sl_5: Final[float] = OUTPUT(label='5-yr straight line depreciation federal and state allocation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_ibi_reduc_sl_5: Final[float] = OUTPUT(label='5-yr straight line state IBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_cbi_reduc_sl_5: Final[float] = OUTPUT(label='5-yr straight line state CBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_prior_itc_sl_5: Final[float] = OUTPUT(label='5-yr straight line state depreciation basis prior ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_sta_qual_sl_5: Final[float] = OUTPUT(label='5-yr straight line depreciation state ITC adj qualifying costs', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_qual_sl_5: Final[float] = OUTPUT(label='5-yr straight line state percent of qualifying costs', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_amount_sl_5: Final[float] = OUTPUT(label='5-yr straight line depreciation ITC basis from state percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_sta_percent_sl_5: Final[float] = OUTPUT(label='5-yr straight line depreciation ITC basis disallowance from state percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_fixed_amount_sl_5: Final[float] = OUTPUT(label='5-yr straight line depreciation ITC basis from state fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_sta_fixed_sl_5: Final[float] = OUTPUT(label='5-yr straight line depreciation ITC basis disallowance from state fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_itc_sta_reduction_sl_5: Final[float] = OUTPUT(label='5-yr straight line state basis state ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_itc_fed_reduction_sl_5: Final[float] = OUTPUT(label='5-yr straight line state basis federal ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_after_itc_sl_5: Final[float] = OUTPUT(label='5-yr straight line state depreciation basis after ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_first_year_bonus_sl_5: Final[float] = OUTPUT(label='5-yr straight line state first year bonus depreciation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_sl_5: Final[float] = OUTPUT(label='5-yr straight line state depreciation basis', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_sl_15: Final[float] = OUTPUT(label='15-yr straight line state percent of total depreciable basis', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_alloc_sl_15: Final[float] = OUTPUT(label='15-yr straight line depreciation federal and state allocation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_ibi_reduc_sl_15: Final[float] = OUTPUT(label='15-yr straight line state IBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_cbi_reduc_sl_15: Final[float] = OUTPUT(label='15-yr straight line state CBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_prior_itc_sl_15: Final[float] = OUTPUT(label='15-yr straight line state depreciation basis prior ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_sta_qual_sl_15: Final[float] = OUTPUT(label='15-yr straight line depreciation state ITC adj qualifying costs', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_qual_sl_15: Final[float] = OUTPUT(label='15-yr straight line state percent of qualifying costs', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_amount_sl_15: Final[float] = OUTPUT(label='15-yr straight line depreciation ITC basis from state percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_sta_percent_sl_15: Final[float] = OUTPUT(label='15-yr straight line depreciation ITC basis disallowance from state percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_fixed_amount_sl_15: Final[float] = OUTPUT(label='15-yr straight line depreciation ITC basis from state fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_sta_fixed_sl_15: Final[float] = OUTPUT(label='15-yr straight line depreciation ITC basis disallowance from state fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_itc_sta_reduction_sl_15: Final[float] = OUTPUT(label='15-yr straight line state basis state ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_itc_fed_reduction_sl_15: Final[float] = OUTPUT(label='15-yr straight line state basis federal ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_after_itc_sl_15: Final[float] = OUTPUT(label='15-yr straight line state depreciation basis after ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_first_year_bonus_sl_15: Final[float] = OUTPUT(label='15-yr straight line state first year bonus depreciation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_sl_15: Final[float] = OUTPUT(label='15-yr straight line state depreciation basis', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_sl_20: Final[float] = OUTPUT(label='20-yr straight line state percent of total depreciable basis', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_alloc_sl_20: Final[float] = OUTPUT(label='20-yr straight line depreciation federal and state allocation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_ibi_reduc_sl_20: Final[float] = OUTPUT(label='20-yr straight line state IBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_cbi_reduc_sl_20: Final[float] = OUTPUT(label='20-yr straight line state CBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_prior_itc_sl_20: Final[float] = OUTPUT(label='20-yr straight line state depreciation basis prior ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_sta_qual_sl_20: Final[float] = OUTPUT(label='20-yr straight line depreciation state ITC adj qualifying costs', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_qual_sl_20: Final[float] = OUTPUT(label='20-yr straight line state percent of qualifying costs', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_amount_sl_20: Final[float] = OUTPUT(label='20-yr straight line depreciation ITC basis from state percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_sta_percent_sl_20: Final[float] = OUTPUT(label='20-yr straight line depreciation ITC basis disallowance from state percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_fixed_amount_sl_20: Final[float] = OUTPUT(label='20-yr straight line depreciation ITC basis from state fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_sta_fixed_sl_20: Final[float] = OUTPUT(label='20-yr straight line depreciation ITC basis disallowance from state fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_itc_sta_reduction_sl_20: Final[float] = OUTPUT(label='20-yr straight line state basis state ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_itc_fed_reduction_sl_20: Final[float] = OUTPUT(label='20-yr straight line state basis federal ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_after_itc_sl_20: Final[float] = OUTPUT(label='20-yr straight line state depreciation basis after ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_first_year_bonus_sl_20: Final[float] = OUTPUT(label='20-yr straight line state first year bonus depreciation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_sl_20: Final[float] = OUTPUT(label='20-yr straight line state depreciation basis', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_sl_39: Final[float] = OUTPUT(label='39-yr straight line state percent of total depreciable basis', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_alloc_sl_39: Final[float] = OUTPUT(label='39-yr straight line depreciation federal and state allocation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_ibi_reduc_sl_39: Final[float] = OUTPUT(label='39-yr straight line state IBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_cbi_reduc_sl_39: Final[float] = OUTPUT(label='39-yr straight line state CBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_prior_itc_sl_39: Final[float] = OUTPUT(label='39-yr straight line state depreciation basis prior ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_sta_qual_sl_39: Final[float] = OUTPUT(label='39-yr straight line depreciation state ITC adj qualifying costs', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_qual_sl_39: Final[float] = OUTPUT(label='39-yr straight line state percent of qualifying costs', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_amount_sl_39: Final[float] = OUTPUT(label='39-yr straight line depreciation ITC basis from state percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_sta_percent_sl_39: Final[float] = OUTPUT(label='39-yr straight line depreciation ITC basis disallowance from state percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_fixed_amount_sl_39: Final[float] = OUTPUT(label='39-yr straight line depreciation ITC basis from state fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_sta_fixed_sl_39: Final[float] = OUTPUT(label='39-yr straight line depreciation ITC basis disallowance from state fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_itc_sta_reduction_sl_39: Final[float] = OUTPUT(label='39-yr straight line state basis state ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_itc_fed_reduction_sl_39: Final[float] = OUTPUT(label='39-yr straight line state basis federal ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_after_itc_sl_39: Final[float] = OUTPUT(label='39-yr straight line state depreciation basis after ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_first_year_bonus_sl_39: Final[float] = OUTPUT(label='39-yr straight line state first year bonus depreciation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_sl_39: Final[float] = OUTPUT(label='39-yr straight line state depreciation basis', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_custom: Final[float] = OUTPUT(label='Custom straight line state percent of total depreciable basis', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_alloc_custom: Final[float] = OUTPUT(label='Custom straight line depreciation federal and state allocation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_ibi_reduc_custom: Final[float] = OUTPUT(label='Custom straight line state IBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_cbi_reduc_custom: Final[float] = OUTPUT(label='Custom straight line state CBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_prior_itc_custom: Final[float] = OUTPUT(label='Custom straight line state depreciation basis prior ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_sta_qual_custom: Final[float] = OUTPUT(label='Custom straight line depreciation state ITC adj qualifying costs', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_qual_custom: Final[float] = OUTPUT(label='Custom straight line state percent of qualifying costs', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_amount_custom: Final[float] = OUTPUT(label='Custom straight line depreciation ITC basis from state percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_sta_percent_custom: Final[float] = OUTPUT(label='Custom straight line depreciation ITC basis disallowance from state percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_fixed_amount_custom: Final[float] = OUTPUT(label='Custom straight line depreciation ITC basis from state fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_sta_fixed_custom: Final[float] = OUTPUT(label='Custom straight line depreciation ITC basis disallowance from state fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_itc_sta_reduction_custom: Final[float] = OUTPUT(label='Custom straight line state basis state ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_itc_fed_reduction_custom: Final[float] = OUTPUT(label='Custom straight line state basis federal ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_after_itc_custom: Final[float] = OUTPUT(label='Custom straight line state depreciation basis after ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_first_year_bonus_custom: Final[float] = OUTPUT(label='Custom straight line state first year bonus depreciation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_custom: Final[float] = OUTPUT(label='Custom straight line state depreciation basis', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_total: Final[float] = OUTPUT(label='Total state percent of total depreciable basis', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_ibi_reduc_total: Final[float] = OUTPUT(label='Total state IBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_cbi_reduc_total: Final[float] = OUTPUT(label='Total state CBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_prior_itc_total: Final[float] = OUTPUT(label='Total state depreciation basis prior ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_sta_qual_total: Final[float] = OUTPUT(label='Total state ITC adj qualifying costs', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_qual_total: Final[float] = OUTPUT(label='Total state percent of qualifying costs', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_percent_amount_total: Final[float] = OUTPUT(label='Total depreciation ITC basis from state percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_sta_percent_total: Final[float] = OUTPUT(label='Total depreciation ITC basis disallowance from state percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_fixed_amount_total: Final[float] = OUTPUT(label='Total depreciation ITC basis from state fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_sta_fixed_total: Final[float] = OUTPUT(label='Total depreciation ITC basis disallowance from state fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_itc_sta_reduction_total: Final[float] = OUTPUT(label='Total state basis state ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_itc_fed_reduction_total: Final[float] = OUTPUT(label='Total state basis federal ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_after_itc_total: Final[float] = OUTPUT(label='Total state depreciation basis after ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_first_year_bonus_total: Final[float] = OUTPUT(label='Total state first year bonus depreciation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_stabas_total: Final[float] = OUTPUT(label='Total state depreciation basis', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_sta_percent_total: Final[float] = OUTPUT(label='State ITC percent total', units='$', type='NUMBER', group='Tax Credits', required='*')
    itc_sta_fixed_total: Final[float] = OUTPUT(label='State ITC fixed total', units='$', type='NUMBER', group='Tax Credits', required='*')
    depr_fedbas_percent_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS federal percent of total depreciable basis', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_ibi_reduc_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS federal IBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_cbi_reduc_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS federal CBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_prior_itc_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS federal depreciation basis prior ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_fed_qual_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS depreciation federal ITC adj qualifying costs', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_qual_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS federal percent of qualifying costs', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_amount_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS depreciation ITC basis from federal percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_fed_percent_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS depreciation ITC basis disallowance from federal percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_fixed_amount_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS depreciation ITC basis from federal fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_fed_fixed_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS depreciation ITC basis disallowance from federal fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_itc_sta_reduction_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS federal basis state ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_itc_fed_reduction_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS federal basis federal ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_after_itc_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS federal depreciation basis after ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_first_year_bonus_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS federal first year bonus depreciation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_macrs_5: Final[float] = OUTPUT(label='5-yr MACRS federal depreciation basis', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS federal percent of total depreciable basis', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_ibi_reduc_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS federal IBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_cbi_reduc_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS federal CBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_prior_itc_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS federal depreciation basis prior ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_fed_qual_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS depreciation federal ITC adj qualifying costs', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_qual_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS federal percent of qualifying costs', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_amount_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS depreciation ITC basis from federal percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_fed_percent_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS depreciation ITC basis disallowance from federal percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_fixed_amount_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS depreciation ITC basis from federal fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_fed_fixed_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS depreciation ITC basis disallowance from federal fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_itc_sta_reduction_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS federal basis state ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_itc_fed_reduction_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS federal basis federal ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_after_itc_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS federal depreciation basis after ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_first_year_bonus_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS federal first year bonus depreciation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_macrs_15: Final[float] = OUTPUT(label='15-yr MACRS federal depreciation basis', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_sl_5: Final[float] = OUTPUT(label='5-yr straight line federal percent of total depreciable basis', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_ibi_reduc_sl_5: Final[float] = OUTPUT(label='5-yr straight line federal IBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_cbi_reduc_sl_5: Final[float] = OUTPUT(label='5-yr straight line federal CBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_prior_itc_sl_5: Final[float] = OUTPUT(label='5-yr straight line federal depreciation basis prior ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_fed_qual_sl_5: Final[float] = OUTPUT(label='5-yr straight line depreciation federal ITC adj qualifying costs', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_qual_sl_5: Final[float] = OUTPUT(label='5-yr straight line federal percent of qualifying costs', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_amount_sl_5: Final[float] = OUTPUT(label='5-yr straight line depreciation ITC basis from federal percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_fed_percent_sl_5: Final[float] = OUTPUT(label='5-yr straight line depreciation ITC basis disallowance from federal percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_fixed_amount_sl_5: Final[float] = OUTPUT(label='5-yr straight line depreciation ITC basis from federal fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_fed_fixed_sl_5: Final[float] = OUTPUT(label='5-yr straight line depreciation ITC basis disallowance from federal fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_itc_sta_reduction_sl_5: Final[float] = OUTPUT(label='5-yr straight line federal basis state ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_itc_fed_reduction_sl_5: Final[float] = OUTPUT(label='5-yr straight line federal basis federal ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_after_itc_sl_5: Final[float] = OUTPUT(label='5-yr straight line federal depreciation basis after ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_first_year_bonus_sl_5: Final[float] = OUTPUT(label='5-yr straight line federal first year bonus depreciation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_sl_5: Final[float] = OUTPUT(label='5-yr straight line federal depreciation basis', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_sl_15: Final[float] = OUTPUT(label='15-yr straight line federal percent of total depreciable basis', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_ibi_reduc_sl_15: Final[float] = OUTPUT(label='15-yr straight line federal IBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_cbi_reduc_sl_15: Final[float] = OUTPUT(label='15-yr straight line federal CBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_prior_itc_sl_15: Final[float] = OUTPUT(label='15-yr straight line federal depreciation basis prior ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_fed_qual_sl_15: Final[float] = OUTPUT(label='15-yr straight line depreciation federal ITC adj qualifying costs', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_qual_sl_15: Final[float] = OUTPUT(label='15-yr straight line federal percent of qualifying costs', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_amount_sl_15: Final[float] = OUTPUT(label='15-yr straight line depreciation ITC basis from federal percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_fed_percent_sl_15: Final[float] = OUTPUT(label='15-yr straight line depreciation ITC basis disallowance from federal percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_fixed_amount_sl_15: Final[float] = OUTPUT(label='15-yr straight line depreciation ITC basis from federal fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_fed_fixed_sl_15: Final[float] = OUTPUT(label='15-yr straight line depreciation ITC basis disallowance from federal fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_itc_sta_reduction_sl_15: Final[float] = OUTPUT(label='15-yr straight line federal basis state ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_itc_fed_reduction_sl_15: Final[float] = OUTPUT(label='15-yr straight line federal basis federal ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_after_itc_sl_15: Final[float] = OUTPUT(label='15-yr straight line federal depreciation basis after ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_first_year_bonus_sl_15: Final[float] = OUTPUT(label='15-yr straight line federal first year bonus depreciation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_sl_15: Final[float] = OUTPUT(label='15-yr straight line federal depreciation basis', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_sl_20: Final[float] = OUTPUT(label='20-yr straight line federal percent of total depreciable basis', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_ibi_reduc_sl_20: Final[float] = OUTPUT(label='20-yr straight line federal IBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_cbi_reduc_sl_20: Final[float] = OUTPUT(label='20-yr straight line federal CBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_prior_itc_sl_20: Final[float] = OUTPUT(label='20-yr straight line federal depreciation basis prior ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_fed_qual_sl_20: Final[float] = OUTPUT(label='20-yr straight line depreciation federal ITC adj qualifying costs', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_qual_sl_20: Final[float] = OUTPUT(label='20-yr straight line federal percent of qualifying costs', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_amount_sl_20: Final[float] = OUTPUT(label='20-yr straight line depreciation ITC basis from federal percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_fed_percent_sl_20: Final[float] = OUTPUT(label='20-yr straight line depreciation ITC basis disallowance from federal percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_fixed_amount_sl_20: Final[float] = OUTPUT(label='20-yr straight line depreciation ITC basis from federal fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_fed_fixed_sl_20: Final[float] = OUTPUT(label='20-yr straight line depreciation ITC basis disallowance from federal fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_itc_sta_reduction_sl_20: Final[float] = OUTPUT(label='20-yr straight line federal basis state ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_itc_fed_reduction_sl_20: Final[float] = OUTPUT(label='20-yr straight line federal basis federal ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_after_itc_sl_20: Final[float] = OUTPUT(label='20-yr straight line federal depreciation basis after ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_first_year_bonus_sl_20: Final[float] = OUTPUT(label='20-yr straight line federal first year bonus depreciation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_sl_20: Final[float] = OUTPUT(label='20-yr straight line federal depreciation basis', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_sl_39: Final[float] = OUTPUT(label='39-yr straight line federal percent of total depreciable basis', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_ibi_reduc_sl_39: Final[float] = OUTPUT(label='39-yr straight line federal IBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_cbi_reduc_sl_39: Final[float] = OUTPUT(label='39-yr straight line federal CBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_prior_itc_sl_39: Final[float] = OUTPUT(label='39-yr straight line federal depreciation basis prior ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_fed_qual_sl_39: Final[float] = OUTPUT(label='39-yr straight line depreciation federal ITC adj qualifying costs', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_qual_sl_39: Final[float] = OUTPUT(label='39-yr straight line federal percent of qualifying costs', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_amount_sl_39: Final[float] = OUTPUT(label='39-yr straight line depreciation ITC basis from federal percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_fed_percent_sl_39: Final[float] = OUTPUT(label='39-yr straight line depreciation ITC basis disallowance from federal percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_fixed_amount_sl_39: Final[float] = OUTPUT(label='39-yr straight line depreciation ITC basis from federal fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_fed_fixed_sl_39: Final[float] = OUTPUT(label='39-yr straight line depreciation ITC basis disallowance from federal fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_itc_sta_reduction_sl_39: Final[float] = OUTPUT(label='39-yr straight line federal basis state ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_itc_fed_reduction_sl_39: Final[float] = OUTPUT(label='39-yr straight line federal basis federal ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_after_itc_sl_39: Final[float] = OUTPUT(label='39-yr straight line federal depreciation basis after ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_first_year_bonus_sl_39: Final[float] = OUTPUT(label='39-yr straight line federal first year bonus depreciation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_sl_39: Final[float] = OUTPUT(label='39-yr straight line federal depreciation basis', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_custom: Final[float] = OUTPUT(label='Custom straight line federal percent of total depreciable basis', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_ibi_reduc_custom: Final[float] = OUTPUT(label='Custom straight line federal IBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_cbi_reduc_custom: Final[float] = OUTPUT(label='Custom straight line federal CBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_prior_itc_custom: Final[float] = OUTPUT(label='Custom straight line federal depreciation basis prior ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_fed_qual_custom: Final[float] = OUTPUT(label='Custom straight line depreciation federal ITC adj qualifying costs', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_qual_custom: Final[float] = OUTPUT(label='Custom straight line federal percent of qualifying costs', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_amount_custom: Final[float] = OUTPUT(label='Custom straight line depreciation ITC basis from federal percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_fed_percent_custom: Final[float] = OUTPUT(label='Custom straight line depreciation ITC basis disallowance from federal percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_fixed_amount_custom: Final[float] = OUTPUT(label='Custom straight line depreciation ITC basis from federal fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_fed_fixed_custom: Final[float] = OUTPUT(label='Custom straight line depreciation ITC basis disallowance from federal fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_itc_sta_reduction_custom: Final[float] = OUTPUT(label='Custom straight line federal basis state ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_itc_fed_reduction_custom: Final[float] = OUTPUT(label='Custom straight line federal basis federal ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_after_itc_custom: Final[float] = OUTPUT(label='Custom straight line federal depreciation basis after ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_first_year_bonus_custom: Final[float] = OUTPUT(label='Custom straight line federal first year bonus depreciation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_custom: Final[float] = OUTPUT(label='Custom straight line federal depreciation basis', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_total: Final[float] = OUTPUT(label='Total federal percent of total depreciable basis', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_ibi_reduc_total: Final[float] = OUTPUT(label='Total federal IBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_cbi_reduc_total: Final[float] = OUTPUT(label='Total federal CBI reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_prior_itc_total: Final[float] = OUTPUT(label='Total federal depreciation basis prior ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_fed_qual_total: Final[float] = OUTPUT(label='Total federal ITC adj qualifying costs', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_qual_total: Final[float] = OUTPUT(label='Total federal percent of qualifying costs', units='%', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_percent_amount_total: Final[float] = OUTPUT(label='Total depreciation ITC basis from federal percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_fed_percent_total: Final[float] = OUTPUT(label='Total depreciation ITC basis disallowance from federal percentage', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_fixed_amount_total: Final[float] = OUTPUT(label='Total depreciation ITC basis from federal fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_disallow_fed_fixed_total: Final[float] = OUTPUT(label='Total depreciation ITC basis disallowance from federal fixed amount', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_itc_sta_reduction_total: Final[float] = OUTPUT(label='Total federal basis state ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_itc_fed_reduction_total: Final[float] = OUTPUT(label='Total federal basis federal ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_after_itc_total: Final[float] = OUTPUT(label='Total federal depreciation basis after ITC reduction', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_first_year_bonus_total: Final[float] = OUTPUT(label='Total federal first year bonus depreciation', units='$', type='NUMBER', group='Depreciation', required='*')
    depr_fedbas_total: Final[float] = OUTPUT(label='Total federal depreciation basis', units='$', type='NUMBER', group='Depreciation', required='*')
    itc_fed_percent_total: Final[float] = OUTPUT(label='Federal ITC percent total', units='$', type='NUMBER', group='Tax Credits', required='*')
    itc_fed_fixed_total: Final[float] = OUTPUT(label='Federal ITC fixed total', units='$', type='NUMBER', group='Tax Credits', required='*')
    depr_stabas_method: float = INPUT(label='Method of state depreciation reduction', type='NUMBER', group='Depreciation', required='?=0', constraints='INTEGER,MIN=0,MAX=1', meta='0=5yr MACRS,1=Proportional')
    depr_fedbas_method: float = INPUT(label='Method of federal depreciation reduction', type='NUMBER', group='Depreciation', required='?=0', constraints='INTEGER,MIN=0,MAX=1', meta='0=5yr MACRS,1=Proportional')
    cash_for_debt_service: Final[float] = OUTPUT(label='Cash available for debt service (CAFDS)', units='$', type='NUMBER', group='Debt Sizing', required='*')
    pv_cafds: Final[float] = OUTPUT(label='Present value of CAFDS', units='$', type='NUMBER', group='Debt Sizing', required='*')
    size_of_debt: Final[float] = OUTPUT(label='Size of debt', units='$', type='NUMBER', group='Debt Sizing', required='*')
    size_of_equity: Final[float] = OUTPUT(label='Equity', units='$', type='NUMBER', group='Debt Sizing', required='*')
    cf_length: Final[float] = OUTPUT(label='Number of periods in cashflow', type='NUMBER', group='Cash Flow', required='*', constraints='INTEGER')
    ppa_price: Final[float] = OUTPUT(label='PPA price in first year', units='cents/kWh', type='NUMBER', group='PPA Price', required='*')
    cf_energy_net: Final[Array] = OUTPUT(label='Energy', units='kWh', type='ARRAY', group='Cash Flow Revenues', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_ppa_price: Final[Array] = OUTPUT(label='PPA price', units='cents/kWh', type='ARRAY', group='Cash Flow Revenues', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_energy_value: Final[Array] = OUTPUT(label='PPA revenue', units='$', type='ARRAY', group='Cash Flow Revenues', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_fixed_expense: Final[Array] = OUTPUT(label='O&M fixed expense', units='$', type='ARRAY', group='Cash Flow Expenses', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_production_expense: Final[Array] = OUTPUT(label='O&M production-based expense', units='$', type='ARRAY', group='Cash Flow Expenses', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_capacity_expense: Final[Array] = OUTPUT(label='O&M capacity-based expense', units='$', type='ARRAY', group='Cash Flow Expenses', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_fuel_expense: Final[Array] = OUTPUT(label='O&M fuel expense', units='$', type='ARRAY', group='Cash Flow Expenses', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_opt_fuel_1_expense: Final[Array] = OUTPUT(label='O&M biomass feedstock expense', units='$', type='ARRAY', group='Cash Flow Expenses', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_om_opt_fuel_2_expense: Final[Array] = OUTPUT(label='O&M coal feedstock expense', units='$', type='ARRAY', group='Cash Flow Expenses', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_property_tax_assessed_value: Final[Array] = OUTPUT(label='Property tax net assessed value', units='$', type='ARRAY', group='Cash Flow Expenses', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_property_tax_expense: Final[Array] = OUTPUT(label='Property tax expense', units='$', type='ARRAY', group='Cash Flow Expenses', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_insurance_expense: Final[Array] = OUTPUT(label='Insurance expense', units='$', type='ARRAY', group='Cash Flow Expenses', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_operating_expenses: Final[Array] = OUTPUT(label='Total operating expenses', units='$', type='ARRAY', group='Cash Flow Expenses', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_net_salvage_value: Final[Array] = OUTPUT(label='Salvage value', units='$', type='ARRAY', group='Cash Flow Revenues', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_total_revenue: Final[Array] = OUTPUT(label='Total revenue', units='$', type='ARRAY', group='Cash Flow Revenues', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_ebitda: Final[Array] = OUTPUT(label='EBITDA', units='$', type='ARRAY', group='Cash Flow Expenses', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_reserve_debtservice: Final[Array] = OUTPUT(label='Reserves debt service balance', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_reserve_om: Final[Array] = OUTPUT(label='Reserves working capital balance ', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_reserve_receivables: Final[Array] = OUTPUT(label='Reserves receivables balance', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_reserve_equip1: Final[Array] = OUTPUT(label='Reserves major equipment 1 balance', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_reserve_equip2: Final[Array] = OUTPUT(label='Reserves major equipment 2 balance', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_reserve_equip3: Final[Array] = OUTPUT(label='Reserves major equipment 3 balance', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_reserve_total: Final[Array] = OUTPUT(label='Reserves total reserves balance', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_reserve_interest: Final[Array] = OUTPUT(label='Interest earned on reserves', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_funding_debtservice: Final[Array] = OUTPUT(label='Reserves debt service funding', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_funding_om: Final[Array] = OUTPUT(label='Reserves working capital funding', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_funding_receivables: Final[Array] = OUTPUT(label='Reserves receivables funding', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_funding_equip1: Final[Array] = OUTPUT(label='Reserves major equipment 1 funding', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_funding_equip2: Final[Array] = OUTPUT(label='Reserves major equipment 2 funding', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_funding_equip3: Final[Array] = OUTPUT(label='Reserves major equipment 3 funding', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_disbursement_debtservice: Final[Array] = OUTPUT(label='Reserves debt service disbursement ', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_disbursement_om: Final[Array] = OUTPUT(label='Reserves working capital disbursement', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_disbursement_receivables: Final[Array] = OUTPUT(label='Reserves receivables disbursement', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_disbursement_equip1: Final[Array] = OUTPUT(label='Reserves major equipment 1 disbursement', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_disbursement_equip2: Final[Array] = OUTPUT(label='Reserves major equipment 2 disbursement', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_disbursement_equip3: Final[Array] = OUTPUT(label='Reserves major equipment 3 disbursement', units='$', type='ARRAY', group='Cash Flow Reserves', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_cash_for_ds: Final[Array] = OUTPUT(label='Cash available for debt service (CAFDS)', units='$', type='ARRAY', group='Cash Flow Debt Sizing', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_pv_interest_factor: Final[Array] = OUTPUT(label='Present value interest factor for CAFDS', type='ARRAY', group='Cash Flow Debt Repayment', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_pv_cash_for_ds: Final[Array] = OUTPUT(label='Present value of CAFDS', units='$', type='ARRAY', group='Cash Flow Debt Sizing', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_debt_size: Final[Array] = OUTPUT(label='Size of debt', units='$', type='ARRAY', group='Cash Flow Debt Sizing', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_debt_balance: Final[Array] = OUTPUT(label='Debt balance', units='$', type='ARRAY', group='Cash Flow Debt Repayment', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_debt_payment_interest: Final[Array] = OUTPUT(label='Debt interest payment', units='$', type='ARRAY', group='Cash Flow Debt Repayment', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_debt_payment_principal: Final[Array] = OUTPUT(label='Debt principal payment', units='$', type='ARRAY', group='Cash Flow Debt Repayment', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_debt_payment_total: Final[Array] = OUTPUT(label='Debt total payment', units='$', type='ARRAY', group='Cash Flow Debt Repayment', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_operating_activities: Final[Array] = OUTPUT(label='Cash flow from operating activities', units='$', type='ARRAY', group='Cash Flow Pre Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    purchase_of_property: Final[float] = OUTPUT(label='Purchase of property', units='$', type='NUMBER', group='Cash Flow Pre Tax', required='*')
    cf_project_dsra: Final[Array] = OUTPUT(label='Reserve (increase)/decrease debt service ', units='$', type='ARRAY', group='Cash Flow Pre Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_wcra: Final[Array] = OUTPUT(label='Reserve (increase)/decrease working capital', units='$', type='ARRAY', group='Cash Flow Pre Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_receivablesra: Final[Array] = OUTPUT(label='Reserve (increase)/decrease receivables', units='$', type='ARRAY', group='Cash Flow Pre Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_me1ra: Final[Array] = OUTPUT(label='Reserve (increase)/decrease major equipment 1', units='$', type='ARRAY', group='Cash Flow Pre Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_me2ra: Final[Array] = OUTPUT(label='Reserve (increase)/decrease major equipment 2', units='$', type='ARRAY', group='Cash Flow Pre Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_me3ra: Final[Array] = OUTPUT(label='Reserve (increase)/decrease major equipment 3', units='$', type='ARRAY', group='Cash Flow Pre Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_ra: Final[Array] = OUTPUT(label='Reserve (increase)/decrease total reserve account', units='$', type='ARRAY', group='Cash Flow Pre Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_me1cs: Final[Array] = OUTPUT(label='Reserve capital spending major equipment 1', units='$', type='ARRAY', group='Cash Flow Pre Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_me2cs: Final[Array] = OUTPUT(label='Reserve capital spending major equipment 2', units='$', type='ARRAY', group='Cash Flow Pre Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_me3cs: Final[Array] = OUTPUT(label='Reserve capital spending major equipment 3', units='$', type='ARRAY', group='Cash Flow Pre Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_mecs: Final[Array] = OUTPUT(label='Reserve capital spending major equipment total', units='$', type='ARRAY', group='Cash Flow Pre Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_investing_activities: Final[Array] = OUTPUT(label='Cash flow from investing activities', units='$', type='ARRAY', group='Cash Flow Pre Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    issuance_of_equity: Final[float] = OUTPUT(label='Issuance of equity', units='$', type='NUMBER', group='Cash Flow Pre Tax', required='*')
    cf_project_financing_activities: Final[Array] = OUTPUT(label='Cash flow from financing activities', units='$', type='ARRAY', group='Cash Flow Pre Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_pretax_cashflow: Final[Array] = OUTPUT(label='Total pre-tax cash flow', units='$', type='ARRAY', group='Cash Flow Pre Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_return_pretax: Final[Array] = OUTPUT(label='Total pre-tax project returns', units='$', type='ARRAY', group='Cash Flow Pre Tax Returns', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_return_pretax_irr: Final[Array] = OUTPUT(label='Pre-tax project cumulative IRR', units='%', type='ARRAY', group='Cash Flow Pre Tax Returns', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_return_pretax_npv: Final[Array] = OUTPUT(label='Pre-tax project cumulative NPV', units='$', type='ARRAY', group='Cash Flow Pre Tax Returns', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_return_aftertax_cash: Final[Array] = OUTPUT(label='Total after-tax project cash returns', units='$', type='ARRAY', group='Cash Flow After Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_return_aftertax: Final[Array] = OUTPUT(label='Total after-tax project returns', units='$', type='ARRAY', group='Cash Flow After Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_return_aftertax_irr: Final[Array] = OUTPUT(label='After-tax project cumulative IRR', units='%', type='ARRAY', group='Cash Flow After Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_return_aftertax_max_irr: Final[Array] = OUTPUT(label='After-tax project maximum IRR', units='%', type='ARRAY', group='Cash Flow After Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    cf_project_return_aftertax_npv: Final[Array] = OUTPUT(label='After-tax project cumulative NPV', units='$', type='ARRAY', group='Cash Flow After Tax', required='*', constraints='LENGTH_EQUAL=cf_length')
    project_return_aftertax_irr: Final[float] = OUTPUT(label='Internal rate of return (after-tax)', units='%', type='NUMBER', group='Metrics', required='*')
    project_return_aftertax_npv: Final[float] = OUTPUT(label='Net present value (after-tax)', units='$', type='NUMBER', group='Metrics', required='*')
    cf_annual_costs: Final[Array] = OUTPUT(label='Annual costs', units='$', type='ARRAY', group='LCOE calculations', required='*', constraints='LENGTH_EQUAL=cf_length')
    npv_annual_costs: Final[float] = OUTPUT(label='Present value of annual costs', units='$', type='NUMBER', group='LCOE calculations', required='*')
    adjusted_installed_cost: Final[float] = OUTPUT(label='Initial cost less cash incentives', units='$', type='NUMBER', required='*')
    min_dscr: Final[float] = OUTPUT(label='Minimum DSCR', type='NUMBER', group='DSCR')
    cf_pretax_dscr: Final[Array] = OUTPUT(label='DSCR (pre-tax)', type='ARRAY', group='DSCR', required='*', constraints='LENGTH_EQUAL=cf_length')
    en_batt: float = INPUT(label='Enable battery storage model', units='0/1', type='NUMBER', group='BatterySystem', required='?=0')
    batt_bank_replacement: Array = INPUT(label='Battery bank replacements per year', units='number/year', type='ARRAY', group='BatterySystem')
    batt_replacement_schedule: Array = INPUT(label='Battery bank replacements per year (user specified)', units='number/year', type='ARRAY', group='BatterySystem')
    batt_replacement_option: float = INPUT(label='Enable battery replacement?', units='0=none,1=capacity based,2=user schedule', type='NUMBER', group='BatterySystem', required='?=0', constraints='INTEGER,MIN=0,MAX=2')
    battery_per_kWh: float = INPUT(label='Battery cost', units='$/kWh', type='NUMBER', group='BatterySystem', required='?=0.0')
    batt_computed_bank_capacity: float = INPUT(label='Battery bank capacity', units='kWh', type='NUMBER', group='BatterySystem', required='?=0.0')
    cf_battery_replacement_cost: Final[Array] = OUTPUT(label='Battery replacement cost', units='$', type='ARRAY', group='Cash Flow', required='*')
    cf_battery_replacement_cost_schedule: Final[Array] = OUTPUT(label='Battery replacement cost schedule', units='$/kWh', type='ARRAY', group='Cash Flow', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 ppa_soln_mode: float = ...,
                 ppa_soln_tolerance: float = ...,
                 ppa_soln_min: float = ...,
                 ppa_soln_max: float = ...,
                 ppa_soln_max_iterations: float = ...,
                 ppa_price_input: Array = ...,
                 ppa_escalation: float = ...,
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
                 reserves_interest: float = ...,
                 equip1_reserve_cost: float = ...,
                 equip1_reserve_freq: float = ...,
                 equip2_reserve_cost: float = ...,
                 equip2_reserve_freq: float = ...,
                 equip3_reserve_cost: float = ...,
                 equip3_reserve_freq: float = ...,
                 equip_reserve_depr_sta: float = ...,
                 equip_reserve_depr_fed: float = ...,
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
                 depr_alloc_macrs_5_percent: float = ...,
                 depr_alloc_macrs_15_percent: float = ...,
                 depr_alloc_sl_5_percent: float = ...,
                 depr_alloc_sl_15_percent: float = ...,
                 depr_alloc_sl_20_percent: float = ...,
                 depr_alloc_sl_39_percent: float = ...,
                 depr_alloc_custom_percent: float = ...,
                 depr_custom_schedule: Array = ...,
                 depr_bonus_sta: float = ...,
                 depr_bonus_sta_macrs_5: float = ...,
                 depr_bonus_sta_macrs_15: float = ...,
                 depr_bonus_sta_sl_5: float = ...,
                 depr_bonus_sta_sl_15: float = ...,
                 depr_bonus_sta_sl_20: float = ...,
                 depr_bonus_sta_sl_39: float = ...,
                 depr_bonus_sta_custom: float = ...,
                 depr_bonus_fed: float = ...,
                 depr_bonus_fed_macrs_5: float = ...,
                 depr_bonus_fed_macrs_15: float = ...,
                 depr_bonus_fed_sl_5: float = ...,
                 depr_bonus_fed_sl_15: float = ...,
                 depr_bonus_fed_sl_20: float = ...,
                 depr_bonus_fed_sl_39: float = ...,
                 depr_bonus_fed_custom: float = ...,
                 depr_itc_sta_macrs_5: float = ...,
                 depr_itc_sta_macrs_15: float = ...,
                 depr_itc_sta_sl_5: float = ...,
                 depr_itc_sta_sl_15: float = ...,
                 depr_itc_sta_sl_20: float = ...,
                 depr_itc_sta_sl_39: float = ...,
                 depr_itc_sta_custom: float = ...,
                 depr_itc_fed_macrs_5: float = ...,
                 depr_itc_fed_macrs_15: float = ...,
                 depr_itc_fed_sl_5: float = ...,
                 depr_itc_fed_sl_15: float = ...,
                 depr_itc_fed_sl_20: float = ...,
                 depr_itc_fed_sl_39: float = ...,
                 depr_itc_fed_custom: float = ...,
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
                 term_tenor: float = ...,
                 term_int_rate: float = ...,
                 dscr: float = ...,
                 dscr_reserve_months: float = ...,
                 debt_percent: float = ...,
                 debt_option: float = ...,
                 payment_option: float = ...,
                 cost_debt_closing: float = ...,
                 cost_debt_fee: float = ...,
                 months_working_reserve: float = ...,
                 months_receivables_reserve: float = ...,
                 cost_other_financing: float = ...,
                 flip_target_percent: float = ...,
                 flip_target_year: float = ...,
                 pbi_fed_for_ds: float = ...,
                 pbi_sta_for_ds: float = ...,
                 pbi_uti_for_ds: float = ...,
                 pbi_oth_for_ds: float = ...,
                 annual_energy_value: Array = ...,
                 elec_cost_with_system: Array = ...,
                 elec_cost_without_system: Array = ...,
                 host_real_discount_rate: float = ...,
                 gen: Array = ...,
                 degradation: Array = ...,
                 roe_input: Array = ...,
                 loan_moratorium: float = ...,
                 system_use_recapitalization: float = ...,
                 system_recapitalization_cost: float = ...,
                 system_recapitalization_escalation: float = ...,
                 system_lifetime_recapitalize: Array = ...,
                 system_use_lifetime_output: float = ...,
                 ppa_multiplier_model: float = ...,
                 dispatch_factors_ts: Array = ...,
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
                 dispatch_sched_weekend: Matrix = ...,
                 total_installed_cost: float = ...,
                 salvage_percentage: float = ...,
                 construction_financing_cost: float = ...,
                 depr_stabas_method: float = ...,
                 depr_fedbas_method: float = ...,
                 en_batt: float = ...,
                 batt_bank_replacement: Array = ...,
                 batt_replacement_schedule: Array = ...,
                 batt_replacement_option: float = ...,
                 battery_per_kWh: float = ...,
                 batt_computed_bank_capacity: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
