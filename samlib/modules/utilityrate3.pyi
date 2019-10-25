
# This is a generated file

"""utilityrate3 - Complex utility rate structure net revenue calculator OpenEI Version 3"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'analysis_period': float,
        'system_use_lifetime_output': float,
        'gen': Array,
        'load': Array,
        'inflation_rate': float,
        'degradation': Array,
        'load_escalation': Array,
        'rate_escalation': Array,
        'ur_enable_net_metering': float,
        'ur_excess_monthly_energy_or_dollars': float,
        'ur_nm_yearend_sell_rate': float,
        'ur_monthly_fixed_charge': float,
        'ur_flat_buy_rate': float,
        'ur_flat_sell_rate': float,
        'ur_monthly_min_charge': float,
        'ur_annual_min_charge': float,
        'ur_ec_enable': float,
        'ur_ec_sched_weekday': Matrix,
        'ur_ec_sched_weekend': Matrix,
        'ur_ec_p1_t1_br': float,
        'ur_ec_p1_t1_sr': float,
        'ur_ec_p1_t1_ub': float,
        'ur_ec_p1_t2_br': float,
        'ur_ec_p1_t2_sr': float,
        'ur_ec_p1_t2_ub': float,
        'ur_ec_p1_t3_br': float,
        'ur_ec_p1_t3_sr': float,
        'ur_ec_p1_t3_ub': float,
        'ur_ec_p1_t4_br': float,
        'ur_ec_p1_t4_sr': float,
        'ur_ec_p1_t4_ub': float,
        'ur_ec_p1_t5_br': float,
        'ur_ec_p1_t5_sr': float,
        'ur_ec_p1_t5_ub': float,
        'ur_ec_p1_t6_br': float,
        'ur_ec_p1_t6_sr': float,
        'ur_ec_p1_t6_ub': float,
        'ur_ec_p2_t1_br': float,
        'ur_ec_p2_t1_sr': float,
        'ur_ec_p2_t1_ub': float,
        'ur_ec_p2_t2_br': float,
        'ur_ec_p2_t2_sr': float,
        'ur_ec_p2_t2_ub': float,
        'ur_ec_p2_t3_br': float,
        'ur_ec_p2_t3_sr': float,
        'ur_ec_p2_t3_ub': float,
        'ur_ec_p2_t4_br': float,
        'ur_ec_p2_t4_sr': float,
        'ur_ec_p2_t4_ub': float,
        'ur_ec_p2_t5_br': float,
        'ur_ec_p2_t5_sr': float,
        'ur_ec_p2_t5_ub': float,
        'ur_ec_p2_t6_br': float,
        'ur_ec_p2_t6_sr': float,
        'ur_ec_p2_t6_ub': float,
        'ur_ec_p3_t1_br': float,
        'ur_ec_p3_t1_sr': float,
        'ur_ec_p3_t1_ub': float,
        'ur_ec_p3_t2_br': float,
        'ur_ec_p3_t2_sr': float,
        'ur_ec_p3_t2_ub': float,
        'ur_ec_p3_t3_br': float,
        'ur_ec_p3_t3_sr': float,
        'ur_ec_p3_t3_ub': float,
        'ur_ec_p3_t4_br': float,
        'ur_ec_p3_t4_sr': float,
        'ur_ec_p3_t4_ub': float,
        'ur_ec_p3_t5_br': float,
        'ur_ec_p3_t5_sr': float,
        'ur_ec_p3_t5_ub': float,
        'ur_ec_p3_t6_br': float,
        'ur_ec_p3_t6_sr': float,
        'ur_ec_p3_t6_ub': float,
        'ur_ec_p4_t1_br': float,
        'ur_ec_p4_t1_sr': float,
        'ur_ec_p4_t1_ub': float,
        'ur_ec_p4_t2_br': float,
        'ur_ec_p4_t2_sr': float,
        'ur_ec_p4_t2_ub': float,
        'ur_ec_p4_t3_br': float,
        'ur_ec_p4_t3_sr': float,
        'ur_ec_p4_t3_ub': float,
        'ur_ec_p4_t4_br': float,
        'ur_ec_p4_t4_sr': float,
        'ur_ec_p4_t4_ub': float,
        'ur_ec_p4_t5_br': float,
        'ur_ec_p4_t5_sr': float,
        'ur_ec_p4_t5_ub': float,
        'ur_ec_p4_t6_br': float,
        'ur_ec_p4_t6_sr': float,
        'ur_ec_p4_t6_ub': float,
        'ur_ec_p5_t1_br': float,
        'ur_ec_p5_t1_sr': float,
        'ur_ec_p5_t1_ub': float,
        'ur_ec_p5_t2_br': float,
        'ur_ec_p5_t2_sr': float,
        'ur_ec_p5_t2_ub': float,
        'ur_ec_p5_t3_br': float,
        'ur_ec_p5_t3_sr': float,
        'ur_ec_p5_t3_ub': float,
        'ur_ec_p5_t4_br': float,
        'ur_ec_p5_t4_sr': float,
        'ur_ec_p5_t4_ub': float,
        'ur_ec_p5_t5_br': float,
        'ur_ec_p5_t5_sr': float,
        'ur_ec_p5_t5_ub': float,
        'ur_ec_p5_t6_br': float,
        'ur_ec_p5_t6_sr': float,
        'ur_ec_p5_t6_ub': float,
        'ur_ec_p6_t1_br': float,
        'ur_ec_p6_t1_sr': float,
        'ur_ec_p6_t1_ub': float,
        'ur_ec_p6_t2_br': float,
        'ur_ec_p6_t2_sr': float,
        'ur_ec_p6_t2_ub': float,
        'ur_ec_p6_t3_br': float,
        'ur_ec_p6_t3_sr': float,
        'ur_ec_p6_t3_ub': float,
        'ur_ec_p6_t4_br': float,
        'ur_ec_p6_t4_sr': float,
        'ur_ec_p6_t4_ub': float,
        'ur_ec_p6_t5_br': float,
        'ur_ec_p6_t5_sr': float,
        'ur_ec_p6_t5_ub': float,
        'ur_ec_p6_t6_br': float,
        'ur_ec_p6_t6_sr': float,
        'ur_ec_p6_t6_ub': float,
        'ur_ec_p7_t1_br': float,
        'ur_ec_p7_t1_sr': float,
        'ur_ec_p7_t1_ub': float,
        'ur_ec_p7_t2_br': float,
        'ur_ec_p7_t2_sr': float,
        'ur_ec_p7_t2_ub': float,
        'ur_ec_p7_t3_br': float,
        'ur_ec_p7_t3_sr': float,
        'ur_ec_p7_t3_ub': float,
        'ur_ec_p7_t4_br': float,
        'ur_ec_p7_t4_sr': float,
        'ur_ec_p7_t4_ub': float,
        'ur_ec_p7_t5_br': float,
        'ur_ec_p7_t5_sr': float,
        'ur_ec_p7_t5_ub': float,
        'ur_ec_p7_t6_br': float,
        'ur_ec_p7_t6_sr': float,
        'ur_ec_p7_t6_ub': float,
        'ur_ec_p8_t1_br': float,
        'ur_ec_p8_t1_sr': float,
        'ur_ec_p8_t1_ub': float,
        'ur_ec_p8_t2_br': float,
        'ur_ec_p8_t2_sr': float,
        'ur_ec_p8_t2_ub': float,
        'ur_ec_p8_t3_br': float,
        'ur_ec_p8_t3_sr': float,
        'ur_ec_p8_t3_ub': float,
        'ur_ec_p8_t4_br': float,
        'ur_ec_p8_t4_sr': float,
        'ur_ec_p8_t4_ub': float,
        'ur_ec_p8_t5_br': float,
        'ur_ec_p8_t5_sr': float,
        'ur_ec_p8_t5_ub': float,
        'ur_ec_p8_t6_br': float,
        'ur_ec_p8_t6_sr': float,
        'ur_ec_p8_t6_ub': float,
        'ur_ec_p9_t1_br': float,
        'ur_ec_p9_t1_sr': float,
        'ur_ec_p9_t1_ub': float,
        'ur_ec_p9_t2_br': float,
        'ur_ec_p9_t2_sr': float,
        'ur_ec_p9_t2_ub': float,
        'ur_ec_p9_t3_br': float,
        'ur_ec_p9_t3_sr': float,
        'ur_ec_p9_t3_ub': float,
        'ur_ec_p9_t4_br': float,
        'ur_ec_p9_t4_sr': float,
        'ur_ec_p9_t4_ub': float,
        'ur_ec_p9_t5_br': float,
        'ur_ec_p9_t5_sr': float,
        'ur_ec_p9_t5_ub': float,
        'ur_ec_p9_t6_br': float,
        'ur_ec_p9_t6_sr': float,
        'ur_ec_p9_t6_ub': float,
        'ur_ec_p10_t1_br': float,
        'ur_ec_p10_t1_sr': float,
        'ur_ec_p10_t1_ub': float,
        'ur_ec_p10_t2_br': float,
        'ur_ec_p10_t2_sr': float,
        'ur_ec_p10_t2_ub': float,
        'ur_ec_p10_t3_br': float,
        'ur_ec_p10_t3_sr': float,
        'ur_ec_p10_t3_ub': float,
        'ur_ec_p10_t4_br': float,
        'ur_ec_p10_t4_sr': float,
        'ur_ec_p10_t4_ub': float,
        'ur_ec_p10_t5_br': float,
        'ur_ec_p10_t5_sr': float,
        'ur_ec_p10_t5_ub': float,
        'ur_ec_p10_t6_br': float,
        'ur_ec_p10_t6_sr': float,
        'ur_ec_p10_t6_ub': float,
        'ur_ec_p11_t1_br': float,
        'ur_ec_p11_t1_sr': float,
        'ur_ec_p11_t1_ub': float,
        'ur_ec_p11_t2_br': float,
        'ur_ec_p11_t2_sr': float,
        'ur_ec_p11_t2_ub': float,
        'ur_ec_p11_t3_br': float,
        'ur_ec_p11_t3_sr': float,
        'ur_ec_p11_t3_ub': float,
        'ur_ec_p11_t4_br': float,
        'ur_ec_p11_t4_sr': float,
        'ur_ec_p11_t4_ub': float,
        'ur_ec_p11_t5_br': float,
        'ur_ec_p11_t5_sr': float,
        'ur_ec_p11_t5_ub': float,
        'ur_ec_p11_t6_br': float,
        'ur_ec_p11_t6_sr': float,
        'ur_ec_p11_t6_ub': float,
        'ur_ec_p12_t1_br': float,
        'ur_ec_p12_t1_sr': float,
        'ur_ec_p12_t1_ub': float,
        'ur_ec_p12_t2_br': float,
        'ur_ec_p12_t2_sr': float,
        'ur_ec_p12_t2_ub': float,
        'ur_ec_p12_t3_br': float,
        'ur_ec_p12_t3_sr': float,
        'ur_ec_p12_t3_ub': float,
        'ur_ec_p12_t4_br': float,
        'ur_ec_p12_t4_sr': float,
        'ur_ec_p12_t4_ub': float,
        'ur_ec_p12_t5_br': float,
        'ur_ec_p12_t5_sr': float,
        'ur_ec_p12_t5_ub': float,
        'ur_ec_p12_t6_br': float,
        'ur_ec_p12_t6_sr': float,
        'ur_ec_p12_t6_ub': float,
        'ur_dc_enable': float,
        'ur_dc_sched_weekday': Matrix,
        'ur_dc_sched_weekend': Matrix,
        'ur_dc_p1_t1_dc': float,
        'ur_dc_p1_t1_ub': float,
        'ur_dc_p1_t2_dc': float,
        'ur_dc_p1_t2_ub': float,
        'ur_dc_p1_t3_dc': float,
        'ur_dc_p1_t3_ub': float,
        'ur_dc_p1_t4_dc': float,
        'ur_dc_p1_t4_ub': float,
        'ur_dc_p1_t5_dc': float,
        'ur_dc_p1_t5_ub': float,
        'ur_dc_p1_t6_dc': float,
        'ur_dc_p1_t6_ub': float,
        'ur_dc_p2_t1_dc': float,
        'ur_dc_p2_t1_ub': float,
        'ur_dc_p2_t2_dc': float,
        'ur_dc_p2_t2_ub': float,
        'ur_dc_p2_t3_dc': float,
        'ur_dc_p2_t3_ub': float,
        'ur_dc_p2_t4_dc': float,
        'ur_dc_p2_t4_ub': float,
        'ur_dc_p2_t5_dc': float,
        'ur_dc_p2_t5_ub': float,
        'ur_dc_p2_t6_dc': float,
        'ur_dc_p2_t6_ub': float,
        'ur_dc_p3_t1_dc': float,
        'ur_dc_p3_t1_ub': float,
        'ur_dc_p3_t2_dc': float,
        'ur_dc_p3_t2_ub': float,
        'ur_dc_p3_t3_dc': float,
        'ur_dc_p3_t3_ub': float,
        'ur_dc_p3_t4_dc': float,
        'ur_dc_p3_t4_ub': float,
        'ur_dc_p3_t5_dc': float,
        'ur_dc_p3_t5_ub': float,
        'ur_dc_p3_t6_dc': float,
        'ur_dc_p3_t6_ub': float,
        'ur_dc_p4_t1_dc': float,
        'ur_dc_p4_t1_ub': float,
        'ur_dc_p4_t2_dc': float,
        'ur_dc_p4_t2_ub': float,
        'ur_dc_p4_t3_dc': float,
        'ur_dc_p4_t3_ub': float,
        'ur_dc_p4_t4_dc': float,
        'ur_dc_p4_t4_ub': float,
        'ur_dc_p4_t5_dc': float,
        'ur_dc_p4_t5_ub': float,
        'ur_dc_p4_t6_dc': float,
        'ur_dc_p4_t6_ub': float,
        'ur_dc_p5_t1_dc': float,
        'ur_dc_p5_t1_ub': float,
        'ur_dc_p5_t2_dc': float,
        'ur_dc_p5_t2_ub': float,
        'ur_dc_p5_t3_dc': float,
        'ur_dc_p5_t3_ub': float,
        'ur_dc_p5_t4_dc': float,
        'ur_dc_p5_t4_ub': float,
        'ur_dc_p5_t5_dc': float,
        'ur_dc_p5_t5_ub': float,
        'ur_dc_p5_t6_dc': float,
        'ur_dc_p5_t6_ub': float,
        'ur_dc_p6_t1_dc': float,
        'ur_dc_p6_t1_ub': float,
        'ur_dc_p6_t2_dc': float,
        'ur_dc_p6_t2_ub': float,
        'ur_dc_p6_t3_dc': float,
        'ur_dc_p6_t3_ub': float,
        'ur_dc_p6_t4_dc': float,
        'ur_dc_p6_t4_ub': float,
        'ur_dc_p6_t5_dc': float,
        'ur_dc_p6_t5_ub': float,
        'ur_dc_p6_t6_dc': float,
        'ur_dc_p6_t6_ub': float,
        'ur_dc_p7_t1_dc': float,
        'ur_dc_p7_t1_ub': float,
        'ur_dc_p7_t2_dc': float,
        'ur_dc_p7_t2_ub': float,
        'ur_dc_p7_t3_dc': float,
        'ur_dc_p7_t3_ub': float,
        'ur_dc_p7_t4_dc': float,
        'ur_dc_p7_t4_ub': float,
        'ur_dc_p7_t5_dc': float,
        'ur_dc_p7_t5_ub': float,
        'ur_dc_p7_t6_dc': float,
        'ur_dc_p7_t6_ub': float,
        'ur_dc_p8_t1_dc': float,
        'ur_dc_p8_t1_ub': float,
        'ur_dc_p8_t2_dc': float,
        'ur_dc_p8_t2_ub': float,
        'ur_dc_p8_t3_dc': float,
        'ur_dc_p8_t3_ub': float,
        'ur_dc_p8_t4_dc': float,
        'ur_dc_p8_t4_ub': float,
        'ur_dc_p8_t5_dc': float,
        'ur_dc_p8_t5_ub': float,
        'ur_dc_p8_t6_dc': float,
        'ur_dc_p8_t6_ub': float,
        'ur_dc_p9_t1_dc': float,
        'ur_dc_p9_t1_ub': float,
        'ur_dc_p9_t2_dc': float,
        'ur_dc_p9_t2_ub': float,
        'ur_dc_p9_t3_dc': float,
        'ur_dc_p9_t3_ub': float,
        'ur_dc_p9_t4_dc': float,
        'ur_dc_p9_t4_ub': float,
        'ur_dc_p9_t5_dc': float,
        'ur_dc_p9_t5_ub': float,
        'ur_dc_p9_t6_dc': float,
        'ur_dc_p9_t6_ub': float,
        'ur_dc_p10_t1_dc': float,
        'ur_dc_p10_t1_ub': float,
        'ur_dc_p10_t2_dc': float,
        'ur_dc_p10_t2_ub': float,
        'ur_dc_p10_t3_dc': float,
        'ur_dc_p10_t3_ub': float,
        'ur_dc_p10_t4_dc': float,
        'ur_dc_p10_t4_ub': float,
        'ur_dc_p10_t5_dc': float,
        'ur_dc_p10_t5_ub': float,
        'ur_dc_p10_t6_dc': float,
        'ur_dc_p10_t6_ub': float,
        'ur_dc_p11_t1_dc': float,
        'ur_dc_p11_t1_ub': float,
        'ur_dc_p11_t2_dc': float,
        'ur_dc_p11_t2_ub': float,
        'ur_dc_p11_t3_dc': float,
        'ur_dc_p11_t3_ub': float,
        'ur_dc_p11_t4_dc': float,
        'ur_dc_p11_t4_ub': float,
        'ur_dc_p11_t5_dc': float,
        'ur_dc_p11_t5_ub': float,
        'ur_dc_p11_t6_dc': float,
        'ur_dc_p11_t6_ub': float,
        'ur_dc_p12_t1_dc': float,
        'ur_dc_p12_t1_ub': float,
        'ur_dc_p12_t2_dc': float,
        'ur_dc_p12_t2_ub': float,
        'ur_dc_p12_t3_dc': float,
        'ur_dc_p12_t3_ub': float,
        'ur_dc_p12_t4_dc': float,
        'ur_dc_p12_t4_ub': float,
        'ur_dc_p12_t5_dc': float,
        'ur_dc_p12_t5_ub': float,
        'ur_dc_p12_t6_dc': float,
        'ur_dc_p12_t6_ub': float,
        'ur_dc_jan_t1_dc': float,
        'ur_dc_jan_t1_ub': float,
        'ur_dc_jan_t2_dc': float,
        'ur_dc_jan_t2_ub': float,
        'ur_dc_jan_t3_dc': float,
        'ur_dc_jan_t3_ub': float,
        'ur_dc_jan_t4_dc': float,
        'ur_dc_jan_t4_ub': float,
        'ur_dc_jan_t5_dc': float,
        'ur_dc_jan_t5_ub': float,
        'ur_dc_jan_t6_dc': float,
        'ur_dc_jan_t6_ub': float,
        'ur_dc_feb_t1_dc': float,
        'ur_dc_feb_t1_ub': float,
        'ur_dc_feb_t2_dc': float,
        'ur_dc_feb_t2_ub': float,
        'ur_dc_feb_t3_dc': float,
        'ur_dc_feb_t3_ub': float,
        'ur_dc_feb_t4_dc': float,
        'ur_dc_feb_t4_ub': float,
        'ur_dc_feb_t5_dc': float,
        'ur_dc_feb_t5_ub': float,
        'ur_dc_feb_t6_dc': float,
        'ur_dc_feb_t6_ub': float,
        'ur_dc_mar_t1_dc': float,
        'ur_dc_mar_t1_ub': float,
        'ur_dc_mar_t2_dc': float,
        'ur_dc_mar_t2_ub': float,
        'ur_dc_mar_t3_dc': float,
        'ur_dc_mar_t3_ub': float,
        'ur_dc_mar_t4_dc': float,
        'ur_dc_mar_t4_ub': float,
        'ur_dc_mar_t5_dc': float,
        'ur_dc_mar_t5_ub': float,
        'ur_dc_mar_t6_dc': float,
        'ur_dc_mar_t6_ub': float,
        'ur_dc_apr_t1_dc': float,
        'ur_dc_apr_t1_ub': float,
        'ur_dc_apr_t2_dc': float,
        'ur_dc_apr_t2_ub': float,
        'ur_dc_apr_t3_dc': float,
        'ur_dc_apr_t3_ub': float,
        'ur_dc_apr_t4_dc': float,
        'ur_dc_apr_t4_ub': float,
        'ur_dc_apr_t5_dc': float,
        'ur_dc_apr_t5_ub': float,
        'ur_dc_apr_t6_dc': float,
        'ur_dc_apr_t6_ub': float,
        'ur_dc_may_t1_dc': float,
        'ur_dc_may_t1_ub': float,
        'ur_dc_may_t2_dc': float,
        'ur_dc_may_t2_ub': float,
        'ur_dc_may_t3_dc': float,
        'ur_dc_may_t3_ub': float,
        'ur_dc_may_t4_dc': float,
        'ur_dc_may_t4_ub': float,
        'ur_dc_may_t5_dc': float,
        'ur_dc_may_t5_ub': float,
        'ur_dc_may_t6_dc': float,
        'ur_dc_may_t6_ub': float,
        'ur_dc_jun_t1_dc': float,
        'ur_dc_jun_t1_ub': float,
        'ur_dc_jun_t2_dc': float,
        'ur_dc_jun_t2_ub': float,
        'ur_dc_jun_t3_dc': float,
        'ur_dc_jun_t3_ub': float,
        'ur_dc_jun_t4_dc': float,
        'ur_dc_jun_t4_ub': float,
        'ur_dc_jun_t5_dc': float,
        'ur_dc_jun_t5_ub': float,
        'ur_dc_jun_t6_dc': float,
        'ur_dc_jun_t6_ub': float,
        'ur_dc_jul_t1_dc': float,
        'ur_dc_jul_t1_ub': float,
        'ur_dc_jul_t2_dc': float,
        'ur_dc_jul_t2_ub': float,
        'ur_dc_jul_t3_dc': float,
        'ur_dc_jul_t3_ub': float,
        'ur_dc_jul_t4_dc': float,
        'ur_dc_jul_t4_ub': float,
        'ur_dc_jul_t5_dc': float,
        'ur_dc_jul_t5_ub': float,
        'ur_dc_jul_t6_dc': float,
        'ur_dc_jul_t6_ub': float,
        'ur_dc_aug_t1_dc': float,
        'ur_dc_aug_t1_ub': float,
        'ur_dc_aug_t2_dc': float,
        'ur_dc_aug_t2_ub': float,
        'ur_dc_aug_t3_dc': float,
        'ur_dc_aug_t3_ub': float,
        'ur_dc_aug_t4_dc': float,
        'ur_dc_aug_t4_ub': float,
        'ur_dc_aug_t5_dc': float,
        'ur_dc_aug_t5_ub': float,
        'ur_dc_aug_t6_dc': float,
        'ur_dc_aug_t6_ub': float,
        'ur_dc_sep_t1_dc': float,
        'ur_dc_sep_t1_ub': float,
        'ur_dc_sep_t2_dc': float,
        'ur_dc_sep_t2_ub': float,
        'ur_dc_sep_t3_dc': float,
        'ur_dc_sep_t3_ub': float,
        'ur_dc_sep_t4_dc': float,
        'ur_dc_sep_t4_ub': float,
        'ur_dc_sep_t5_dc': float,
        'ur_dc_sep_t5_ub': float,
        'ur_dc_sep_t6_dc': float,
        'ur_dc_sep_t6_ub': float,
        'ur_dc_oct_t1_dc': float,
        'ur_dc_oct_t1_ub': float,
        'ur_dc_oct_t2_dc': float,
        'ur_dc_oct_t2_ub': float,
        'ur_dc_oct_t3_dc': float,
        'ur_dc_oct_t3_ub': float,
        'ur_dc_oct_t4_dc': float,
        'ur_dc_oct_t4_ub': float,
        'ur_dc_oct_t5_dc': float,
        'ur_dc_oct_t5_ub': float,
        'ur_dc_oct_t6_dc': float,
        'ur_dc_oct_t6_ub': float,
        'ur_dc_nov_t1_dc': float,
        'ur_dc_nov_t1_ub': float,
        'ur_dc_nov_t2_dc': float,
        'ur_dc_nov_t2_ub': float,
        'ur_dc_nov_t3_dc': float,
        'ur_dc_nov_t3_ub': float,
        'ur_dc_nov_t4_dc': float,
        'ur_dc_nov_t4_ub': float,
        'ur_dc_nov_t5_dc': float,
        'ur_dc_nov_t5_ub': float,
        'ur_dc_nov_t6_dc': float,
        'ur_dc_nov_t6_ub': float,
        'ur_dc_dec_t1_dc': float,
        'ur_dc_dec_t1_ub': float,
        'ur_dc_dec_t2_dc': float,
        'ur_dc_dec_t2_ub': float,
        'ur_dc_dec_t3_dc': float,
        'ur_dc_dec_t3_ub': float,
        'ur_dc_dec_t4_dc': float,
        'ur_dc_dec_t4_ub': float,
        'ur_dc_dec_t5_dc': float,
        'ur_dc_dec_t5_ub': float,
        'ur_dc_dec_t6_dc': float,
        'ur_dc_dec_t6_ub': float,
        'annual_energy_value': Array,
        'annual_electric_load': Array,
        'elec_cost_with_system': Array,
        'elec_cost_without_system': Array,
        'elec_cost_with_system_year1': float,
        'elec_cost_without_system_year1': float,
        'savings_year1': float,
        'year1_electric_load': float,
        'year1_hourly_e_tofromgrid': Array,
        'year1_hourly_load': Array,
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
        'year1_monthly_ec_charge_flat_with_system': Array,
        'year1_monthly_dc_fixed_without_system': Array,
        'year1_monthly_dc_tou_without_system': Array,
        'year1_monthly_ec_charge_without_system': Array,
        'year1_monthly_ec_charge_flat_without_system': Array,
        'year1_monthly_load': Array,
        'year1_monthly_electricity_to_grid': Array,
        'year1_monthly_cumulative_excess_generation': Array,
        'year1_monthly_cumulative_excess_dollars': Array,
        'year1_monthly_utility_bill_w_sys': Array,
        'year1_monthly_utility_bill_wo_sys': Array,
        'utility_bill_w_sys_jan': Array,
        'utility_bill_w_sys_feb': Array,
        'utility_bill_w_sys_mar': Array,
        'utility_bill_w_sys_apr': Array,
        'utility_bill_w_sys_may': Array,
        'utility_bill_w_sys_jun': Array,
        'utility_bill_w_sys_jul': Array,
        'utility_bill_w_sys_aug': Array,
        'utility_bill_w_sys_sep': Array,
        'utility_bill_w_sys_oct': Array,
        'utility_bill_w_sys_nov': Array,
        'utility_bill_w_sys_dec': Array,
        'utility_bill_w_sys': Array,
        'utility_bill_wo_sys_jan': Array,
        'utility_bill_wo_sys_feb': Array,
        'utility_bill_wo_sys_mar': Array,
        'utility_bill_wo_sys_apr': Array,
        'utility_bill_wo_sys_may': Array,
        'utility_bill_wo_sys_jun': Array,
        'utility_bill_wo_sys_jul': Array,
        'utility_bill_wo_sys_aug': Array,
        'utility_bill_wo_sys_sep': Array,
        'utility_bill_wo_sys_oct': Array,
        'utility_bill_wo_sys_nov': Array,
        'utility_bill_wo_sys_dec': Array,
        'utility_bill_wo_sys': Array,
        'charge_w_sys_fixed_jan': Array,
        'charge_w_sys_fixed_feb': Array,
        'charge_w_sys_fixed_mar': Array,
        'charge_w_sys_fixed_apr': Array,
        'charge_w_sys_fixed_may': Array,
        'charge_w_sys_fixed_jun': Array,
        'charge_w_sys_fixed_jul': Array,
        'charge_w_sys_fixed_aug': Array,
        'charge_w_sys_fixed_sep': Array,
        'charge_w_sys_fixed_oct': Array,
        'charge_w_sys_fixed_nov': Array,
        'charge_w_sys_fixed_dec': Array,
        'charge_w_sys_fixed': Array,
        'charge_wo_sys_fixed_jan': Array,
        'charge_wo_sys_fixed_feb': Array,
        'charge_wo_sys_fixed_mar': Array,
        'charge_wo_sys_fixed_apr': Array,
        'charge_wo_sys_fixed_may': Array,
        'charge_wo_sys_fixed_jun': Array,
        'charge_wo_sys_fixed_jul': Array,
        'charge_wo_sys_fixed_aug': Array,
        'charge_wo_sys_fixed_sep': Array,
        'charge_wo_sys_fixed_oct': Array,
        'charge_wo_sys_fixed_nov': Array,
        'charge_wo_sys_fixed_dec': Array,
        'charge_wo_sys_fixed': Array,
        'charge_w_sys_minimum_jan': Array,
        'charge_w_sys_minimum_feb': Array,
        'charge_w_sys_minimum_mar': Array,
        'charge_w_sys_minimum_apr': Array,
        'charge_w_sys_minimum_may': Array,
        'charge_w_sys_minimum_jun': Array,
        'charge_w_sys_minimum_jul': Array,
        'charge_w_sys_minimum_aug': Array,
        'charge_w_sys_minimum_sep': Array,
        'charge_w_sys_minimum_oct': Array,
        'charge_w_sys_minimum_nov': Array,
        'charge_w_sys_minimum_dec': Array,
        'charge_w_sys_minimum': Array,
        'charge_wo_sys_minimum_jan': Array,
        'charge_wo_sys_minimum_feb': Array,
        'charge_wo_sys_minimum_mar': Array,
        'charge_wo_sys_minimum_apr': Array,
        'charge_wo_sys_minimum_may': Array,
        'charge_wo_sys_minimum_jun': Array,
        'charge_wo_sys_minimum_jul': Array,
        'charge_wo_sys_minimum_aug': Array,
        'charge_wo_sys_minimum_sep': Array,
        'charge_wo_sys_minimum_oct': Array,
        'charge_wo_sys_minimum_nov': Array,
        'charge_wo_sys_minimum_dec': Array,
        'charge_wo_sys_minimum': Array,
        'charge_w_sys_dc_fixed_jan': Array,
        'charge_w_sys_dc_fixed_feb': Array,
        'charge_w_sys_dc_fixed_mar': Array,
        'charge_w_sys_dc_fixed_apr': Array,
        'charge_w_sys_dc_fixed_may': Array,
        'charge_w_sys_dc_fixed_jun': Array,
        'charge_w_sys_dc_fixed_jul': Array,
        'charge_w_sys_dc_fixed_aug': Array,
        'charge_w_sys_dc_fixed_sep': Array,
        'charge_w_sys_dc_fixed_oct': Array,
        'charge_w_sys_dc_fixed_nov': Array,
        'charge_w_sys_dc_fixed_dec': Array,
        'charge_w_sys_dc_fixed': Array,
        'charge_w_sys_dc_tou_jan': Array,
        'charge_w_sys_dc_tou_feb': Array,
        'charge_w_sys_dc_tou_mar': Array,
        'charge_w_sys_dc_tou_apr': Array,
        'charge_w_sys_dc_tou_may': Array,
        'charge_w_sys_dc_tou_jun': Array,
        'charge_w_sys_dc_tou_jul': Array,
        'charge_w_sys_dc_tou_aug': Array,
        'charge_w_sys_dc_tou_sep': Array,
        'charge_w_sys_dc_tou_oct': Array,
        'charge_w_sys_dc_tou_nov': Array,
        'charge_w_sys_dc_tou_dec': Array,
        'charge_w_sys_dc_tou': Array,
        'charge_w_sys_ec_jan': Array,
        'charge_w_sys_ec_feb': Array,
        'charge_w_sys_ec_mar': Array,
        'charge_w_sys_ec_apr': Array,
        'charge_w_sys_ec_may': Array,
        'charge_w_sys_ec_jun': Array,
        'charge_w_sys_ec_jul': Array,
        'charge_w_sys_ec_aug': Array,
        'charge_w_sys_ec_sep': Array,
        'charge_w_sys_ec_oct': Array,
        'charge_w_sys_ec_nov': Array,
        'charge_w_sys_ec_dec': Array,
        'charge_w_sys_ec': Array,
        'charge_w_sys_ec_flat_jan': Array,
        'charge_w_sys_ec_flat_feb': Array,
        'charge_w_sys_ec_flat_mar': Array,
        'charge_w_sys_ec_flat_apr': Array,
        'charge_w_sys_ec_flat_may': Array,
        'charge_w_sys_ec_flat_jun': Array,
        'charge_w_sys_ec_flat_jul': Array,
        'charge_w_sys_ec_flat_aug': Array,
        'charge_w_sys_ec_flat_sep': Array,
        'charge_w_sys_ec_flat_oct': Array,
        'charge_w_sys_ec_flat_nov': Array,
        'charge_w_sys_ec_flat_dec': Array,
        'charge_w_sys_ec_flat': Array,
        'charge_wo_sys_dc_fixed_jan': Array,
        'charge_wo_sys_dc_fixed_feb': Array,
        'charge_wo_sys_dc_fixed_mar': Array,
        'charge_wo_sys_dc_fixed_apr': Array,
        'charge_wo_sys_dc_fixed_may': Array,
        'charge_wo_sys_dc_fixed_jun': Array,
        'charge_wo_sys_dc_fixed_jul': Array,
        'charge_wo_sys_dc_fixed_aug': Array,
        'charge_wo_sys_dc_fixed_sep': Array,
        'charge_wo_sys_dc_fixed_oct': Array,
        'charge_wo_sys_dc_fixed_nov': Array,
        'charge_wo_sys_dc_fixed_dec': Array,
        'charge_wo_sys_dc_fixed': Array,
        'charge_wo_sys_dc_tou_jan': Array,
        'charge_wo_sys_dc_tou_feb': Array,
        'charge_wo_sys_dc_tou_mar': Array,
        'charge_wo_sys_dc_tou_apr': Array,
        'charge_wo_sys_dc_tou_may': Array,
        'charge_wo_sys_dc_tou_jun': Array,
        'charge_wo_sys_dc_tou_jul': Array,
        'charge_wo_sys_dc_tou_aug': Array,
        'charge_wo_sys_dc_tou_sep': Array,
        'charge_wo_sys_dc_tou_oct': Array,
        'charge_wo_sys_dc_tou_nov': Array,
        'charge_wo_sys_dc_tou_dec': Array,
        'charge_wo_sys_dc_tou': Array,
        'charge_wo_sys_ec_jan': Array,
        'charge_wo_sys_ec_feb': Array,
        'charge_wo_sys_ec_mar': Array,
        'charge_wo_sys_ec_apr': Array,
        'charge_wo_sys_ec_may': Array,
        'charge_wo_sys_ec_jun': Array,
        'charge_wo_sys_ec_jul': Array,
        'charge_wo_sys_ec_aug': Array,
        'charge_wo_sys_ec_sep': Array,
        'charge_wo_sys_ec_oct': Array,
        'charge_wo_sys_ec_nov': Array,
        'charge_wo_sys_ec_dec': Array,
        'charge_wo_sys_ec': Array,
        'charge_wo_sys_ec_flat_jan': Array,
        'charge_wo_sys_ec_flat_feb': Array,
        'charge_wo_sys_ec_flat_mar': Array,
        'charge_wo_sys_ec_flat_apr': Array,
        'charge_wo_sys_ec_flat_may': Array,
        'charge_wo_sys_ec_flat_jun': Array,
        'charge_wo_sys_ec_flat_jul': Array,
        'charge_wo_sys_ec_flat_aug': Array,
        'charge_wo_sys_ec_flat_sep': Array,
        'charge_wo_sys_ec_flat_oct': Array,
        'charge_wo_sys_ec_flat_nov': Array,
        'charge_wo_sys_ec_flat_dec': Array,
        'charge_wo_sys_ec_flat': Array,
        'charge_wo_sys_ec_jan_p1': Array,
        'charge_wo_sys_ec_jan_p2': Array,
        'charge_wo_sys_ec_jan_p3': Array,
        'charge_wo_sys_ec_jan_p4': Array,
        'charge_wo_sys_ec_jan_p5': Array,
        'charge_wo_sys_ec_jan_p6': Array,
        'charge_wo_sys_ec_jan_p7': Array,
        'charge_wo_sys_ec_jan_p8': Array,
        'charge_wo_sys_ec_jan_p9': Array,
        'charge_wo_sys_ec_jan_p10': Array,
        'charge_wo_sys_ec_jan_p11': Array,
        'charge_wo_sys_ec_jan_p12': Array,
        'charge_wo_sys_ec_feb_p1': Array,
        'charge_wo_sys_ec_feb_p2': Array,
        'charge_wo_sys_ec_feb_p3': Array,
        'charge_wo_sys_ec_feb_p4': Array,
        'charge_wo_sys_ec_feb_p5': Array,
        'charge_wo_sys_ec_feb_p6': Array,
        'charge_wo_sys_ec_feb_p7': Array,
        'charge_wo_sys_ec_feb_p8': Array,
        'charge_wo_sys_ec_feb_p9': Array,
        'charge_wo_sys_ec_feb_p10': Array,
        'charge_wo_sys_ec_feb_p11': Array,
        'charge_wo_sys_ec_feb_p12': Array,
        'charge_wo_sys_ec_mar_p1': Array,
        'charge_wo_sys_ec_mar_p2': Array,
        'charge_wo_sys_ec_mar_p3': Array,
        'charge_wo_sys_ec_mar_p4': Array,
        'charge_wo_sys_ec_mar_p5': Array,
        'charge_wo_sys_ec_mar_p6': Array,
        'charge_wo_sys_ec_mar_p7': Array,
        'charge_wo_sys_ec_mar_p8': Array,
        'charge_wo_sys_ec_mar_p9': Array,
        'charge_wo_sys_ec_mar_p10': Array,
        'charge_wo_sys_ec_mar_p11': Array,
        'charge_wo_sys_ec_mar_p12': Array,
        'charge_wo_sys_ec_apr_p1': Array,
        'charge_wo_sys_ec_apr_p2': Array,
        'charge_wo_sys_ec_apr_p3': Array,
        'charge_wo_sys_ec_apr_p4': Array,
        'charge_wo_sys_ec_apr_p5': Array,
        'charge_wo_sys_ec_apr_p6': Array,
        'charge_wo_sys_ec_apr_p7': Array,
        'charge_wo_sys_ec_apr_p8': Array,
        'charge_wo_sys_ec_apr_p9': Array,
        'charge_wo_sys_ec_apr_p10': Array,
        'charge_wo_sys_ec_apr_p11': Array,
        'charge_wo_sys_ec_apr_p12': Array,
        'charge_wo_sys_ec_may_p1': Array,
        'charge_wo_sys_ec_may_p2': Array,
        'charge_wo_sys_ec_may_p3': Array,
        'charge_wo_sys_ec_may_p4': Array,
        'charge_wo_sys_ec_may_p5': Array,
        'charge_wo_sys_ec_may_p6': Array,
        'charge_wo_sys_ec_may_p7': Array,
        'charge_wo_sys_ec_may_p8': Array,
        'charge_wo_sys_ec_may_p9': Array,
        'charge_wo_sys_ec_may_p10': Array,
        'charge_wo_sys_ec_may_p11': Array,
        'charge_wo_sys_ec_may_p12': Array,
        'charge_wo_sys_ec_jun_p1': Array,
        'charge_wo_sys_ec_jun_p2': Array,
        'charge_wo_sys_ec_jun_p3': Array,
        'charge_wo_sys_ec_jun_p4': Array,
        'charge_wo_sys_ec_jun_p5': Array,
        'charge_wo_sys_ec_jun_p6': Array,
        'charge_wo_sys_ec_jun_p7': Array,
        'charge_wo_sys_ec_jun_p8': Array,
        'charge_wo_sys_ec_jun_p9': Array,
        'charge_wo_sys_ec_jun_p10': Array,
        'charge_wo_sys_ec_jun_p11': Array,
        'charge_wo_sys_ec_jun_p12': Array,
        'charge_wo_sys_ec_jul_p1': Array,
        'charge_wo_sys_ec_jul_p2': Array,
        'charge_wo_sys_ec_jul_p3': Array,
        'charge_wo_sys_ec_jul_p4': Array,
        'charge_wo_sys_ec_jul_p5': Array,
        'charge_wo_sys_ec_jul_p6': Array,
        'charge_wo_sys_ec_jul_p7': Array,
        'charge_wo_sys_ec_jul_p8': Array,
        'charge_wo_sys_ec_jul_p9': Array,
        'charge_wo_sys_ec_jul_p10': Array,
        'charge_wo_sys_ec_jul_p11': Array,
        'charge_wo_sys_ec_jul_p12': Array,
        'charge_wo_sys_ec_aug_p1': Array,
        'charge_wo_sys_ec_aug_p2': Array,
        'charge_wo_sys_ec_aug_p3': Array,
        'charge_wo_sys_ec_aug_p4': Array,
        'charge_wo_sys_ec_aug_p5': Array,
        'charge_wo_sys_ec_aug_p6': Array,
        'charge_wo_sys_ec_aug_p7': Array,
        'charge_wo_sys_ec_aug_p8': Array,
        'charge_wo_sys_ec_aug_p9': Array,
        'charge_wo_sys_ec_aug_p10': Array,
        'charge_wo_sys_ec_aug_p11': Array,
        'charge_wo_sys_ec_aug_p12': Array,
        'charge_wo_sys_ec_sep_p1': Array,
        'charge_wo_sys_ec_sep_p2': Array,
        'charge_wo_sys_ec_sep_p3': Array,
        'charge_wo_sys_ec_sep_p4': Array,
        'charge_wo_sys_ec_sep_p5': Array,
        'charge_wo_sys_ec_sep_p6': Array,
        'charge_wo_sys_ec_sep_p7': Array,
        'charge_wo_sys_ec_sep_p8': Array,
        'charge_wo_sys_ec_sep_p9': Array,
        'charge_wo_sys_ec_sep_p10': Array,
        'charge_wo_sys_ec_sep_p11': Array,
        'charge_wo_sys_ec_sep_p12': Array,
        'charge_wo_sys_ec_oct_p1': Array,
        'charge_wo_sys_ec_oct_p2': Array,
        'charge_wo_sys_ec_oct_p3': Array,
        'charge_wo_sys_ec_oct_p4': Array,
        'charge_wo_sys_ec_oct_p5': Array,
        'charge_wo_sys_ec_oct_p6': Array,
        'charge_wo_sys_ec_oct_p7': Array,
        'charge_wo_sys_ec_oct_p8': Array,
        'charge_wo_sys_ec_oct_p9': Array,
        'charge_wo_sys_ec_oct_p10': Array,
        'charge_wo_sys_ec_oct_p11': Array,
        'charge_wo_sys_ec_oct_p12': Array,
        'charge_wo_sys_ec_nov_p1': Array,
        'charge_wo_sys_ec_nov_p2': Array,
        'charge_wo_sys_ec_nov_p3': Array,
        'charge_wo_sys_ec_nov_p4': Array,
        'charge_wo_sys_ec_nov_p5': Array,
        'charge_wo_sys_ec_nov_p6': Array,
        'charge_wo_sys_ec_nov_p7': Array,
        'charge_wo_sys_ec_nov_p8': Array,
        'charge_wo_sys_ec_nov_p9': Array,
        'charge_wo_sys_ec_nov_p10': Array,
        'charge_wo_sys_ec_nov_p11': Array,
        'charge_wo_sys_ec_nov_p12': Array,
        'charge_wo_sys_ec_dec_p1': Array,
        'charge_wo_sys_ec_dec_p2': Array,
        'charge_wo_sys_ec_dec_p3': Array,
        'charge_wo_sys_ec_dec_p4': Array,
        'charge_wo_sys_ec_dec_p5': Array,
        'charge_wo_sys_ec_dec_p6': Array,
        'charge_wo_sys_ec_dec_p7': Array,
        'charge_wo_sys_ec_dec_p8': Array,
        'charge_wo_sys_ec_dec_p9': Array,
        'charge_wo_sys_ec_dec_p10': Array,
        'charge_wo_sys_ec_dec_p11': Array,
        'charge_wo_sys_ec_dec_p12': Array,
        'energy_wo_sys_ec_jan_p1': Array,
        'energy_wo_sys_ec_jan_p2': Array,
        'energy_wo_sys_ec_jan_p3': Array,
        'energy_wo_sys_ec_jan_p4': Array,
        'energy_wo_sys_ec_jan_p5': Array,
        'energy_wo_sys_ec_jan_p6': Array,
        'energy_wo_sys_ec_jan_p7': Array,
        'energy_wo_sys_ec_jan_p8': Array,
        'energy_wo_sys_ec_jan_p9': Array,
        'energy_wo_sys_ec_jan_p10': Array,
        'energy_wo_sys_ec_jan_p11': Array,
        'energy_wo_sys_ec_jan_p12': Array,
        'energy_wo_sys_ec_feb_p1': Array,
        'energy_wo_sys_ec_feb_p2': Array,
        'energy_wo_sys_ec_feb_p3': Array,
        'energy_wo_sys_ec_feb_p4': Array,
        'energy_wo_sys_ec_feb_p5': Array,
        'energy_wo_sys_ec_feb_p6': Array,
        'energy_wo_sys_ec_feb_p7': Array,
        'energy_wo_sys_ec_feb_p8': Array,
        'energy_wo_sys_ec_feb_p9': Array,
        'energy_wo_sys_ec_feb_p10': Array,
        'energy_wo_sys_ec_feb_p11': Array,
        'energy_wo_sys_ec_feb_p12': Array,
        'energy_wo_sys_ec_mar_p1': Array,
        'energy_wo_sys_ec_mar_p2': Array,
        'energy_wo_sys_ec_mar_p3': Array,
        'energy_wo_sys_ec_mar_p4': Array,
        'energy_wo_sys_ec_mar_p5': Array,
        'energy_wo_sys_ec_mar_p6': Array,
        'energy_wo_sys_ec_mar_p7': Array,
        'energy_wo_sys_ec_mar_p8': Array,
        'energy_wo_sys_ec_mar_p9': Array,
        'energy_wo_sys_ec_mar_p10': Array,
        'energy_wo_sys_ec_mar_p11': Array,
        'energy_wo_sys_ec_mar_p12': Array,
        'energy_wo_sys_ec_apr_p1': Array,
        'energy_wo_sys_ec_apr_p2': Array,
        'energy_wo_sys_ec_apr_p3': Array,
        'energy_wo_sys_ec_apr_p4': Array,
        'energy_wo_sys_ec_apr_p5': Array,
        'energy_wo_sys_ec_apr_p6': Array,
        'energy_wo_sys_ec_apr_p7': Array,
        'energy_wo_sys_ec_apr_p8': Array,
        'energy_wo_sys_ec_apr_p9': Array,
        'energy_wo_sys_ec_apr_p10': Array,
        'energy_wo_sys_ec_apr_p11': Array,
        'energy_wo_sys_ec_apr_p12': Array,
        'energy_wo_sys_ec_may_p1': Array,
        'energy_wo_sys_ec_may_p2': Array,
        'energy_wo_sys_ec_may_p3': Array,
        'energy_wo_sys_ec_may_p4': Array,
        'energy_wo_sys_ec_may_p5': Array,
        'energy_wo_sys_ec_may_p6': Array,
        'energy_wo_sys_ec_may_p7': Array,
        'energy_wo_sys_ec_may_p8': Array,
        'energy_wo_sys_ec_may_p9': Array,
        'energy_wo_sys_ec_may_p10': Array,
        'energy_wo_sys_ec_may_p11': Array,
        'energy_wo_sys_ec_may_p12': Array,
        'energy_wo_sys_ec_jun_p1': Array,
        'energy_wo_sys_ec_jun_p2': Array,
        'energy_wo_sys_ec_jun_p3': Array,
        'energy_wo_sys_ec_jun_p4': Array,
        'energy_wo_sys_ec_jun_p5': Array,
        'energy_wo_sys_ec_jun_p6': Array,
        'energy_wo_sys_ec_jun_p7': Array,
        'energy_wo_sys_ec_jun_p8': Array,
        'energy_wo_sys_ec_jun_p9': Array,
        'energy_wo_sys_ec_jun_p10': Array,
        'energy_wo_sys_ec_jun_p11': Array,
        'energy_wo_sys_ec_jun_p12': Array,
        'energy_wo_sys_ec_jul_p1': Array,
        'energy_wo_sys_ec_jul_p2': Array,
        'energy_wo_sys_ec_jul_p3': Array,
        'energy_wo_sys_ec_jul_p4': Array,
        'energy_wo_sys_ec_jul_p5': Array,
        'energy_wo_sys_ec_jul_p6': Array,
        'energy_wo_sys_ec_jul_p7': Array,
        'energy_wo_sys_ec_jul_p8': Array,
        'energy_wo_sys_ec_jul_p9': Array,
        'energy_wo_sys_ec_jul_p10': Array,
        'energy_wo_sys_ec_jul_p11': Array,
        'energy_wo_sys_ec_jul_p12': Array,
        'energy_wo_sys_ec_aug_p1': Array,
        'energy_wo_sys_ec_aug_p2': Array,
        'energy_wo_sys_ec_aug_p3': Array,
        'energy_wo_sys_ec_aug_p4': Array,
        'energy_wo_sys_ec_aug_p5': Array,
        'energy_wo_sys_ec_aug_p6': Array,
        'energy_wo_sys_ec_aug_p7': Array,
        'energy_wo_sys_ec_aug_p8': Array,
        'energy_wo_sys_ec_aug_p9': Array,
        'energy_wo_sys_ec_aug_p10': Array,
        'energy_wo_sys_ec_aug_p11': Array,
        'energy_wo_sys_ec_aug_p12': Array,
        'energy_wo_sys_ec_sep_p1': Array,
        'energy_wo_sys_ec_sep_p2': Array,
        'energy_wo_sys_ec_sep_p3': Array,
        'energy_wo_sys_ec_sep_p4': Array,
        'energy_wo_sys_ec_sep_p5': Array,
        'energy_wo_sys_ec_sep_p6': Array,
        'energy_wo_sys_ec_sep_p7': Array,
        'energy_wo_sys_ec_sep_p8': Array,
        'energy_wo_sys_ec_sep_p9': Array,
        'energy_wo_sys_ec_sep_p10': Array,
        'energy_wo_sys_ec_sep_p11': Array,
        'energy_wo_sys_ec_sep_p12': Array,
        'energy_wo_sys_ec_oct_p1': Array,
        'energy_wo_sys_ec_oct_p2': Array,
        'energy_wo_sys_ec_oct_p3': Array,
        'energy_wo_sys_ec_oct_p4': Array,
        'energy_wo_sys_ec_oct_p5': Array,
        'energy_wo_sys_ec_oct_p6': Array,
        'energy_wo_sys_ec_oct_p7': Array,
        'energy_wo_sys_ec_oct_p8': Array,
        'energy_wo_sys_ec_oct_p9': Array,
        'energy_wo_sys_ec_oct_p10': Array,
        'energy_wo_sys_ec_oct_p11': Array,
        'energy_wo_sys_ec_oct_p12': Array,
        'energy_wo_sys_ec_nov_p1': Array,
        'energy_wo_sys_ec_nov_p2': Array,
        'energy_wo_sys_ec_nov_p3': Array,
        'energy_wo_sys_ec_nov_p4': Array,
        'energy_wo_sys_ec_nov_p5': Array,
        'energy_wo_sys_ec_nov_p6': Array,
        'energy_wo_sys_ec_nov_p7': Array,
        'energy_wo_sys_ec_nov_p8': Array,
        'energy_wo_sys_ec_nov_p9': Array,
        'energy_wo_sys_ec_nov_p10': Array,
        'energy_wo_sys_ec_nov_p11': Array,
        'energy_wo_sys_ec_nov_p12': Array,
        'energy_wo_sys_ec_dec_p1': Array,
        'energy_wo_sys_ec_dec_p2': Array,
        'energy_wo_sys_ec_dec_p3': Array,
        'energy_wo_sys_ec_dec_p4': Array,
        'energy_wo_sys_ec_dec_p5': Array,
        'energy_wo_sys_ec_dec_p6': Array,
        'energy_wo_sys_ec_dec_p7': Array,
        'energy_wo_sys_ec_dec_p8': Array,
        'energy_wo_sys_ec_dec_p9': Array,
        'energy_wo_sys_ec_dec_p10': Array,
        'energy_wo_sys_ec_dec_p11': Array,
        'energy_wo_sys_ec_dec_p12': Array,
        'charge_w_sys_ec_jan_p1': Array,
        'charge_w_sys_ec_jan_p2': Array,
        'charge_w_sys_ec_jan_p3': Array,
        'charge_w_sys_ec_jan_p4': Array,
        'charge_w_sys_ec_jan_p5': Array,
        'charge_w_sys_ec_jan_p6': Array,
        'charge_w_sys_ec_jan_p7': Array,
        'charge_w_sys_ec_jan_p8': Array,
        'charge_w_sys_ec_jan_p9': Array,
        'charge_w_sys_ec_jan_p10': Array,
        'charge_w_sys_ec_jan_p11': Array,
        'charge_w_sys_ec_jan_p12': Array,
        'charge_w_sys_ec_feb_p1': Array,
        'charge_w_sys_ec_feb_p2': Array,
        'charge_w_sys_ec_feb_p3': Array,
        'charge_w_sys_ec_feb_p4': Array,
        'charge_w_sys_ec_feb_p5': Array,
        'charge_w_sys_ec_feb_p6': Array,
        'charge_w_sys_ec_feb_p7': Array,
        'charge_w_sys_ec_feb_p8': Array,
        'charge_w_sys_ec_feb_p9': Array,
        'charge_w_sys_ec_feb_p10': Array,
        'charge_w_sys_ec_feb_p11': Array,
        'charge_w_sys_ec_feb_p12': Array,
        'charge_w_sys_ec_mar_p1': Array,
        'charge_w_sys_ec_mar_p2': Array,
        'charge_w_sys_ec_mar_p3': Array,
        'charge_w_sys_ec_mar_p4': Array,
        'charge_w_sys_ec_mar_p5': Array,
        'charge_w_sys_ec_mar_p6': Array,
        'charge_w_sys_ec_mar_p7': Array,
        'charge_w_sys_ec_mar_p8': Array,
        'charge_w_sys_ec_mar_p9': Array,
        'charge_w_sys_ec_mar_p10': Array,
        'charge_w_sys_ec_mar_p11': Array,
        'charge_w_sys_ec_mar_p12': Array,
        'charge_w_sys_ec_apr_p1': Array,
        'charge_w_sys_ec_apr_p2': Array,
        'charge_w_sys_ec_apr_p3': Array,
        'charge_w_sys_ec_apr_p4': Array,
        'charge_w_sys_ec_apr_p5': Array,
        'charge_w_sys_ec_apr_p6': Array,
        'charge_w_sys_ec_apr_p7': Array,
        'charge_w_sys_ec_apr_p8': Array,
        'charge_w_sys_ec_apr_p9': Array,
        'charge_w_sys_ec_apr_p10': Array,
        'charge_w_sys_ec_apr_p11': Array,
        'charge_w_sys_ec_apr_p12': Array,
        'charge_w_sys_ec_may_p1': Array,
        'charge_w_sys_ec_may_p2': Array,
        'charge_w_sys_ec_may_p3': Array,
        'charge_w_sys_ec_may_p4': Array,
        'charge_w_sys_ec_may_p5': Array,
        'charge_w_sys_ec_may_p6': Array,
        'charge_w_sys_ec_may_p7': Array,
        'charge_w_sys_ec_may_p8': Array,
        'charge_w_sys_ec_may_p9': Array,
        'charge_w_sys_ec_may_p10': Array,
        'charge_w_sys_ec_may_p11': Array,
        'charge_w_sys_ec_may_p12': Array,
        'charge_w_sys_ec_jun_p1': Array,
        'charge_w_sys_ec_jun_p2': Array,
        'charge_w_sys_ec_jun_p3': Array,
        'charge_w_sys_ec_jun_p4': Array,
        'charge_w_sys_ec_jun_p5': Array,
        'charge_w_sys_ec_jun_p6': Array,
        'charge_w_sys_ec_jun_p7': Array,
        'charge_w_sys_ec_jun_p8': Array,
        'charge_w_sys_ec_jun_p9': Array,
        'charge_w_sys_ec_jun_p10': Array,
        'charge_w_sys_ec_jun_p11': Array,
        'charge_w_sys_ec_jun_p12': Array,
        'charge_w_sys_ec_jul_p1': Array,
        'charge_w_sys_ec_jul_p2': Array,
        'charge_w_sys_ec_jul_p3': Array,
        'charge_w_sys_ec_jul_p4': Array,
        'charge_w_sys_ec_jul_p5': Array,
        'charge_w_sys_ec_jul_p6': Array,
        'charge_w_sys_ec_jul_p7': Array,
        'charge_w_sys_ec_jul_p8': Array,
        'charge_w_sys_ec_jul_p9': Array,
        'charge_w_sys_ec_jul_p10': Array,
        'charge_w_sys_ec_jul_p11': Array,
        'charge_w_sys_ec_jul_p12': Array,
        'charge_w_sys_ec_aug_p1': Array,
        'charge_w_sys_ec_aug_p2': Array,
        'charge_w_sys_ec_aug_p3': Array,
        'charge_w_sys_ec_aug_p4': Array,
        'charge_w_sys_ec_aug_p5': Array,
        'charge_w_sys_ec_aug_p6': Array,
        'charge_w_sys_ec_aug_p7': Array,
        'charge_w_sys_ec_aug_p8': Array,
        'charge_w_sys_ec_aug_p9': Array,
        'charge_w_sys_ec_aug_p10': Array,
        'charge_w_sys_ec_aug_p11': Array,
        'charge_w_sys_ec_aug_p12': Array,
        'charge_w_sys_ec_sep_p1': Array,
        'charge_w_sys_ec_sep_p2': Array,
        'charge_w_sys_ec_sep_p3': Array,
        'charge_w_sys_ec_sep_p4': Array,
        'charge_w_sys_ec_sep_p5': Array,
        'charge_w_sys_ec_sep_p6': Array,
        'charge_w_sys_ec_sep_p7': Array,
        'charge_w_sys_ec_sep_p8': Array,
        'charge_w_sys_ec_sep_p9': Array,
        'charge_w_sys_ec_sep_p10': Array,
        'charge_w_sys_ec_sep_p11': Array,
        'charge_w_sys_ec_sep_p12': Array,
        'charge_w_sys_ec_oct_p1': Array,
        'charge_w_sys_ec_oct_p2': Array,
        'charge_w_sys_ec_oct_p3': Array,
        'charge_w_sys_ec_oct_p4': Array,
        'charge_w_sys_ec_oct_p5': Array,
        'charge_w_sys_ec_oct_p6': Array,
        'charge_w_sys_ec_oct_p7': Array,
        'charge_w_sys_ec_oct_p8': Array,
        'charge_w_sys_ec_oct_p9': Array,
        'charge_w_sys_ec_oct_p10': Array,
        'charge_w_sys_ec_oct_p11': Array,
        'charge_w_sys_ec_oct_p12': Array,
        'charge_w_sys_ec_nov_p1': Array,
        'charge_w_sys_ec_nov_p2': Array,
        'charge_w_sys_ec_nov_p3': Array,
        'charge_w_sys_ec_nov_p4': Array,
        'charge_w_sys_ec_nov_p5': Array,
        'charge_w_sys_ec_nov_p6': Array,
        'charge_w_sys_ec_nov_p7': Array,
        'charge_w_sys_ec_nov_p8': Array,
        'charge_w_sys_ec_nov_p9': Array,
        'charge_w_sys_ec_nov_p10': Array,
        'charge_w_sys_ec_nov_p11': Array,
        'charge_w_sys_ec_nov_p12': Array,
        'charge_w_sys_ec_dec_p1': Array,
        'charge_w_sys_ec_dec_p2': Array,
        'charge_w_sys_ec_dec_p3': Array,
        'charge_w_sys_ec_dec_p4': Array,
        'charge_w_sys_ec_dec_p5': Array,
        'charge_w_sys_ec_dec_p6': Array,
        'charge_w_sys_ec_dec_p7': Array,
        'charge_w_sys_ec_dec_p8': Array,
        'charge_w_sys_ec_dec_p9': Array,
        'charge_w_sys_ec_dec_p10': Array,
        'charge_w_sys_ec_dec_p11': Array,
        'charge_w_sys_ec_dec_p12': Array,
        'energy_w_sys_ec_jan_p1': Array,
        'energy_w_sys_ec_jan_p2': Array,
        'energy_w_sys_ec_jan_p3': Array,
        'energy_w_sys_ec_jan_p4': Array,
        'energy_w_sys_ec_jan_p5': Array,
        'energy_w_sys_ec_jan_p6': Array,
        'energy_w_sys_ec_jan_p7': Array,
        'energy_w_sys_ec_jan_p8': Array,
        'energy_w_sys_ec_jan_p9': Array,
        'energy_w_sys_ec_jan_p10': Array,
        'energy_w_sys_ec_jan_p11': Array,
        'energy_w_sys_ec_jan_p12': Array,
        'energy_w_sys_ec_feb_p1': Array,
        'energy_w_sys_ec_feb_p2': Array,
        'energy_w_sys_ec_feb_p3': Array,
        'energy_w_sys_ec_feb_p4': Array,
        'energy_w_sys_ec_feb_p5': Array,
        'energy_w_sys_ec_feb_p6': Array,
        'energy_w_sys_ec_feb_p7': Array,
        'energy_w_sys_ec_feb_p8': Array,
        'energy_w_sys_ec_feb_p9': Array,
        'energy_w_sys_ec_feb_p10': Array,
        'energy_w_sys_ec_feb_p11': Array,
        'energy_w_sys_ec_feb_p12': Array,
        'energy_w_sys_ec_mar_p1': Array,
        'energy_w_sys_ec_mar_p2': Array,
        'energy_w_sys_ec_mar_p3': Array,
        'energy_w_sys_ec_mar_p4': Array,
        'energy_w_sys_ec_mar_p5': Array,
        'energy_w_sys_ec_mar_p6': Array,
        'energy_w_sys_ec_mar_p7': Array,
        'energy_w_sys_ec_mar_p8': Array,
        'energy_w_sys_ec_mar_p9': Array,
        'energy_w_sys_ec_mar_p10': Array,
        'energy_w_sys_ec_mar_p11': Array,
        'energy_w_sys_ec_mar_p12': Array,
        'energy_w_sys_ec_apr_p1': Array,
        'energy_w_sys_ec_apr_p2': Array,
        'energy_w_sys_ec_apr_p3': Array,
        'energy_w_sys_ec_apr_p4': Array,
        'energy_w_sys_ec_apr_p5': Array,
        'energy_w_sys_ec_apr_p6': Array,
        'energy_w_sys_ec_apr_p7': Array,
        'energy_w_sys_ec_apr_p8': Array,
        'energy_w_sys_ec_apr_p9': Array,
        'energy_w_sys_ec_apr_p10': Array,
        'energy_w_sys_ec_apr_p11': Array,
        'energy_w_sys_ec_apr_p12': Array,
        'energy_w_sys_ec_may_p1': Array,
        'energy_w_sys_ec_may_p2': Array,
        'energy_w_sys_ec_may_p3': Array,
        'energy_w_sys_ec_may_p4': Array,
        'energy_w_sys_ec_may_p5': Array,
        'energy_w_sys_ec_may_p6': Array,
        'energy_w_sys_ec_may_p7': Array,
        'energy_w_sys_ec_may_p8': Array,
        'energy_w_sys_ec_may_p9': Array,
        'energy_w_sys_ec_may_p10': Array,
        'energy_w_sys_ec_may_p11': Array,
        'energy_w_sys_ec_may_p12': Array,
        'energy_w_sys_ec_jun_p1': Array,
        'energy_w_sys_ec_jun_p2': Array,
        'energy_w_sys_ec_jun_p3': Array,
        'energy_w_sys_ec_jun_p4': Array,
        'energy_w_sys_ec_jun_p5': Array,
        'energy_w_sys_ec_jun_p6': Array,
        'energy_w_sys_ec_jun_p7': Array,
        'energy_w_sys_ec_jun_p8': Array,
        'energy_w_sys_ec_jun_p9': Array,
        'energy_w_sys_ec_jun_p10': Array,
        'energy_w_sys_ec_jun_p11': Array,
        'energy_w_sys_ec_jun_p12': Array,
        'energy_w_sys_ec_jul_p1': Array,
        'energy_w_sys_ec_jul_p2': Array,
        'energy_w_sys_ec_jul_p3': Array,
        'energy_w_sys_ec_jul_p4': Array,
        'energy_w_sys_ec_jul_p5': Array,
        'energy_w_sys_ec_jul_p6': Array,
        'energy_w_sys_ec_jul_p7': Array,
        'energy_w_sys_ec_jul_p8': Array,
        'energy_w_sys_ec_jul_p9': Array,
        'energy_w_sys_ec_jul_p10': Array,
        'energy_w_sys_ec_jul_p11': Array,
        'energy_w_sys_ec_jul_p12': Array,
        'energy_w_sys_ec_aug_p1': Array,
        'energy_w_sys_ec_aug_p2': Array,
        'energy_w_sys_ec_aug_p3': Array,
        'energy_w_sys_ec_aug_p4': Array,
        'energy_w_sys_ec_aug_p5': Array,
        'energy_w_sys_ec_aug_p6': Array,
        'energy_w_sys_ec_aug_p7': Array,
        'energy_w_sys_ec_aug_p8': Array,
        'energy_w_sys_ec_aug_p9': Array,
        'energy_w_sys_ec_aug_p10': Array,
        'energy_w_sys_ec_aug_p11': Array,
        'energy_w_sys_ec_aug_p12': Array,
        'energy_w_sys_ec_sep_p1': Array,
        'energy_w_sys_ec_sep_p2': Array,
        'energy_w_sys_ec_sep_p3': Array,
        'energy_w_sys_ec_sep_p4': Array,
        'energy_w_sys_ec_sep_p5': Array,
        'energy_w_sys_ec_sep_p6': Array,
        'energy_w_sys_ec_sep_p7': Array,
        'energy_w_sys_ec_sep_p8': Array,
        'energy_w_sys_ec_sep_p9': Array,
        'energy_w_sys_ec_sep_p10': Array,
        'energy_w_sys_ec_sep_p11': Array,
        'energy_w_sys_ec_sep_p12': Array,
        'energy_w_sys_ec_oct_p1': Array,
        'energy_w_sys_ec_oct_p2': Array,
        'energy_w_sys_ec_oct_p3': Array,
        'energy_w_sys_ec_oct_p4': Array,
        'energy_w_sys_ec_oct_p5': Array,
        'energy_w_sys_ec_oct_p6': Array,
        'energy_w_sys_ec_oct_p7': Array,
        'energy_w_sys_ec_oct_p8': Array,
        'energy_w_sys_ec_oct_p9': Array,
        'energy_w_sys_ec_oct_p10': Array,
        'energy_w_sys_ec_oct_p11': Array,
        'energy_w_sys_ec_oct_p12': Array,
        'energy_w_sys_ec_nov_p1': Array,
        'energy_w_sys_ec_nov_p2': Array,
        'energy_w_sys_ec_nov_p3': Array,
        'energy_w_sys_ec_nov_p4': Array,
        'energy_w_sys_ec_nov_p5': Array,
        'energy_w_sys_ec_nov_p6': Array,
        'energy_w_sys_ec_nov_p7': Array,
        'energy_w_sys_ec_nov_p8': Array,
        'energy_w_sys_ec_nov_p9': Array,
        'energy_w_sys_ec_nov_p10': Array,
        'energy_w_sys_ec_nov_p11': Array,
        'energy_w_sys_ec_nov_p12': Array,
        'energy_w_sys_ec_dec_p1': Array,
        'energy_w_sys_ec_dec_p2': Array,
        'energy_w_sys_ec_dec_p3': Array,
        'energy_w_sys_ec_dec_p4': Array,
        'energy_w_sys_ec_dec_p5': Array,
        'energy_w_sys_ec_dec_p6': Array,
        'energy_w_sys_ec_dec_p7': Array,
        'energy_w_sys_ec_dec_p8': Array,
        'energy_w_sys_ec_dec_p9': Array,
        'energy_w_sys_ec_dec_p10': Array,
        'energy_w_sys_ec_dec_p11': Array,
        'energy_w_sys_ec_dec_p12': Array
}, total=False)

class Data(ssc.DataDict):
    analysis_period: float = INPUT(label='Number of years in analysis', units='years', type='NUMBER', required='*', constraints='INTEGER,POSITIVE')
    system_use_lifetime_output: float = INPUT(label='Lifetime hourly system outputs', units='0/1', type='NUMBER', required='*', constraints='INTEGER,MIN=0,MAX=1', meta='0=hourly first year,1=hourly lifetime')
    gen: Array = INPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')
    load: Array = INPUT(label='Electricity load (year 1)', units='kW', type='ARRAY', group='Time Series', required='*')
    inflation_rate: float = INPUT(label='Inflation rate', units='%', type='NUMBER', group='Financials', required='*', constraints='MIN=-99')
    degradation: Array = INPUT(label='Annual energy degradation', units='%', type='ARRAY', group='AnnualOutput', required='*')
    load_escalation: Array = INPUT(label='Annual load escalation', units='%/year', type='ARRAY', required='?=0')
    rate_escalation: Array = INPUT(label='Annual utility rate escalation', units='%/year', type='ARRAY', required='?=0')
    ur_enable_net_metering: float = INPUT(label='Enable net metering', units='0/1', type='NUMBER', required='?=1', constraints='BOOLEAN', meta='Enforce net metering')
    ur_excess_monthly_energy_or_dollars: float = INPUT(label='Net metering handling of monthly excess', units='0=Rollover energy,1=Rollover dollars', type='NUMBER', required='?=0', constraints='INTEGER', meta='Net metering monthly excess')
    ur_nm_yearend_sell_rate: float = INPUT(label='Year end sell rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_monthly_fixed_charge: float = INPUT(label='Monthly fixed charge', units='$', type='NUMBER', required='?=0.0')
    ur_flat_buy_rate: float = INPUT(label='Flat rate (buy)', units='$/kWh', type='NUMBER', required='*')
    ur_flat_sell_rate: float = INPUT(label='Flat rate (sell)', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_monthly_min_charge: float = INPUT(label='Monthly minimum charge', units='$', type='NUMBER', required='?=0.0')
    ur_annual_min_charge: float = INPUT(label='Annual minimum charge', units='$', type='NUMBER', required='?=0.0')
    ur_ec_enable: float = INPUT(label='Enable energy charge', units='0/1', type='NUMBER', required='?=0', constraints='BOOLEAN')
    ur_ec_sched_weekday: Matrix = INPUT(label='Energy Charge Weekday Schedule', type='MATRIX', required='ur_ec_enable=1', meta='12x24')
    ur_ec_sched_weekend: Matrix = INPUT(label='Energy Charge Weekend Schedule', type='MATRIX', required='ur_ec_enable=1', meta='12x24')
    ur_ec_p1_t1_br: float = INPUT(label='Period 1 Tier 1 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t1_sr: float = INPUT(label='Period 1 Tier 1 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t1_ub: float = INPUT(label='Period 1 Tier 1 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t2_br: float = INPUT(label='Period 1 Tier 2 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t2_sr: float = INPUT(label='Period 1 Tier 2 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t2_ub: float = INPUT(label='Period 1 Tier 2 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t3_br: float = INPUT(label='Period 1 Tier 3 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t3_sr: float = INPUT(label='Period 1 Tier 3 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t3_ub: float = INPUT(label='Period 1 Tier 3 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t4_br: float = INPUT(label='Period 1 Tier 4 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t4_sr: float = INPUT(label='Period 1 Tier 4 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t4_ub: float = INPUT(label='Period 1 Tier 4 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t5_br: float = INPUT(label='Period 1 Tier 5 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t5_sr: float = INPUT(label='Period 1 Tier 5 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t5_ub: float = INPUT(label='Period 1 Tier 5 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t6_br: float = INPUT(label='Period 1 Tier 6 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t6_sr: float = INPUT(label='Period 1 Tier 6 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p1_t6_ub: float = INPUT(label='Period 1 Tier 6 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t1_br: float = INPUT(label='Period 2 Tier 1 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t1_sr: float = INPUT(label='Period 2 Tier 1 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t1_ub: float = INPUT(label='Period 2 Tier 1 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t2_br: float = INPUT(label='Period 2 Tier 2 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t2_sr: float = INPUT(label='Period 2 Tier 2 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t2_ub: float = INPUT(label='Period 2 Tier 2 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t3_br: float = INPUT(label='Period 2 Tier 3 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t3_sr: float = INPUT(label='Period 2 Tier 3 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t3_ub: float = INPUT(label='Period 2 Tier 3 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t4_br: float = INPUT(label='Period 2 Tier 4 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t4_sr: float = INPUT(label='Period 2 Tier 4 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t4_ub: float = INPUT(label='Period 2 Tier 4 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t5_br: float = INPUT(label='Period 2 Tier 5 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t5_sr: float = INPUT(label='Period 2 Tier 5 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t5_ub: float = INPUT(label='Period 2 Tier 5 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t6_br: float = INPUT(label='Period 2 Tier 6 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t6_sr: float = INPUT(label='Period 2 Tier 6 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p2_t6_ub: float = INPUT(label='Period 2 Tier 6 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t1_br: float = INPUT(label='Period 3 Tier 1 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t1_sr: float = INPUT(label='Period 3 Tier 1 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t1_ub: float = INPUT(label='Period 3 Tier 1 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t2_br: float = INPUT(label='Period 3 Tier 2 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t2_sr: float = INPUT(label='Period 3 Tier 2 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t2_ub: float = INPUT(label='Period 3 Tier 2 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t3_br: float = INPUT(label='Period 3 Tier 3 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t3_sr: float = INPUT(label='Period 3 Tier 3 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t3_ub: float = INPUT(label='Period 3 Tier 3 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t4_br: float = INPUT(label='Period 3 Tier 4 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t4_sr: float = INPUT(label='Period 3 Tier 4 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t4_ub: float = INPUT(label='Period 3 Tier 4 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t5_br: float = INPUT(label='Period 3 Tier 5 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t5_sr: float = INPUT(label='Period 3 Tier 5 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t5_ub: float = INPUT(label='Period 3 Tier 5 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t6_br: float = INPUT(label='Period 3 Tier 6 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t6_sr: float = INPUT(label='Period 3 Tier 6 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p3_t6_ub: float = INPUT(label='Period 3 Tier 6 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t1_br: float = INPUT(label='Period 4 Tier 1 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t1_sr: float = INPUT(label='Period 4 Tier 1 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t1_ub: float = INPUT(label='Period 4 Tier 1 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t2_br: float = INPUT(label='Period 4 Tier 2 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t2_sr: float = INPUT(label='Period 4 Tier 2 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t2_ub: float = INPUT(label='Period 4 Tier 2 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t3_br: float = INPUT(label='Period 4 Tier 3 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t3_sr: float = INPUT(label='Period 4 Tier 3 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t3_ub: float = INPUT(label='Period 4 Tier 3 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t4_br: float = INPUT(label='Period 4 Tier 4 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t4_sr: float = INPUT(label='Period 4 Tier 4 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t4_ub: float = INPUT(label='Period 4 Tier 4 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t5_br: float = INPUT(label='Period 4 Tier 5 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t5_sr: float = INPUT(label='Period 4 Tier 5 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t5_ub: float = INPUT(label='Period 4 Tier 5 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t6_br: float = INPUT(label='Period 4 Tier 6 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t6_sr: float = INPUT(label='Period 4 Tier 6 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p4_t6_ub: float = INPUT(label='Period 4 Tier 6 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t1_br: float = INPUT(label='Period 5 Tier 1 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t1_sr: float = INPUT(label='Period 5 Tier 1 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t1_ub: float = INPUT(label='Period 5 Tier 1 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t2_br: float = INPUT(label='Period 5 Tier 2 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t2_sr: float = INPUT(label='Period 5 Tier 2 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t2_ub: float = INPUT(label='Period 5 Tier 2 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t3_br: float = INPUT(label='Period 5 Tier 3 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t3_sr: float = INPUT(label='Period 5 Tier 3 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t3_ub: float = INPUT(label='Period 5 Tier 3 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t4_br: float = INPUT(label='Period 5 Tier 4 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t4_sr: float = INPUT(label='Period 5 Tier 4 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t4_ub: float = INPUT(label='Period 5 Tier 4 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t5_br: float = INPUT(label='Period 5 Tier 5 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t5_sr: float = INPUT(label='Period 5 Tier 5 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t5_ub: float = INPUT(label='Period 5 Tier 5 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t6_br: float = INPUT(label='Period 5 Tier 6 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t6_sr: float = INPUT(label='Period 5 Tier 6 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p5_t6_ub: float = INPUT(label='Period 5 Tier 6 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t1_br: float = INPUT(label='Period 6 Tier 1 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t1_sr: float = INPUT(label='Period 6 Tier 1 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t1_ub: float = INPUT(label='Period 6 Tier 1 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t2_br: float = INPUT(label='Period 6 Tier 2 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t2_sr: float = INPUT(label='Period 6 Tier 2 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t2_ub: float = INPUT(label='Period 6 Tier 2 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t3_br: float = INPUT(label='Period 6 Tier 3 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t3_sr: float = INPUT(label='Period 6 Tier 3 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t3_ub: float = INPUT(label='Period 6 Tier 3 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t4_br: float = INPUT(label='Period 6 Tier 4 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t4_sr: float = INPUT(label='Period 6 Tier 4 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t4_ub: float = INPUT(label='Period 6 Tier 4 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t5_br: float = INPUT(label='Period 6 Tier 5 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t5_sr: float = INPUT(label='Period 6 Tier 5 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t5_ub: float = INPUT(label='Period 6 Tier 5 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t6_br: float = INPUT(label='Period 6 Tier 6 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t6_sr: float = INPUT(label='Period 6 Tier 6 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p6_t6_ub: float = INPUT(label='Period 6 Tier 6 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t1_br: float = INPUT(label='Period 7 Tier 1 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t1_sr: float = INPUT(label='Period 7 Tier 1 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t1_ub: float = INPUT(label='Period 7 Tier 1 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t2_br: float = INPUT(label='Period 7 Tier 2 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t2_sr: float = INPUT(label='Period 7 Tier 2 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t2_ub: float = INPUT(label='Period 7 Tier 2 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t3_br: float = INPUT(label='Period 7 Tier 3 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t3_sr: float = INPUT(label='Period 7 Tier 3 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t3_ub: float = INPUT(label='Period 7 Tier 3 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t4_br: float = INPUT(label='Period 7 Tier 4 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t4_sr: float = INPUT(label='Period 7 Tier 4 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t4_ub: float = INPUT(label='Period 7 Tier 4 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t5_br: float = INPUT(label='Period 7 Tier 5 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t5_sr: float = INPUT(label='Period 7 Tier 5 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t5_ub: float = INPUT(label='Period 7 Tier 5 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t6_br: float = INPUT(label='Period 7 Tier 6 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t6_sr: float = INPUT(label='Period 7 Tier 6 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p7_t6_ub: float = INPUT(label='Period 7 Tier 6 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t1_br: float = INPUT(label='Period 8 Tier 1 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t1_sr: float = INPUT(label='Period 8 Tier 1 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t1_ub: float = INPUT(label='Period 8 Tier 1 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t2_br: float = INPUT(label='Period 8 Tier 2 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t2_sr: float = INPUT(label='Period 8 Tier 2 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t2_ub: float = INPUT(label='Period 8 Tier 2 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t3_br: float = INPUT(label='Period 8 Tier 3 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t3_sr: float = INPUT(label='Period 8 Tier 3 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t3_ub: float = INPUT(label='Period 8 Tier 3 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t4_br: float = INPUT(label='Period 8 Tier 4 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t4_sr: float = INPUT(label='Period 8 Tier 4 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t4_ub: float = INPUT(label='Period 8 Tier 4 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t5_br: float = INPUT(label='Period 8 Tier 5 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t5_sr: float = INPUT(label='Period 8 Tier 5 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t5_ub: float = INPUT(label='Period 8 Tier 5 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t6_br: float = INPUT(label='Period 8 Tier 6 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t6_sr: float = INPUT(label='Period 8 Tier 6 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p8_t6_ub: float = INPUT(label='Period 8 Tier 6 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t1_br: float = INPUT(label='Period 9 Tier 1 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t1_sr: float = INPUT(label='Period 9 Tier 1 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t1_ub: float = INPUT(label='Period 9 Tier 1 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t2_br: float = INPUT(label='Period 9 Tier 2 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t2_sr: float = INPUT(label='Period 9 Tier 2 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t2_ub: float = INPUT(label='Period 9 Tier 2 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t3_br: float = INPUT(label='Period 9 Tier 3 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t3_sr: float = INPUT(label='Period 9 Tier 3 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t3_ub: float = INPUT(label='Period 9 Tier 3 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t4_br: float = INPUT(label='Period 9 Tier 4 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t4_sr: float = INPUT(label='Period 9 Tier 4 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t4_ub: float = INPUT(label='Period 9 Tier 4 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t5_br: float = INPUT(label='Period 9 Tier 5 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t5_sr: float = INPUT(label='Period 9 Tier 5 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t5_ub: float = INPUT(label='Period 9 Tier 5 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t6_br: float = INPUT(label='Period 9 Tier 6 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t6_sr: float = INPUT(label='Period 9 Tier 6 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p9_t6_ub: float = INPUT(label='Period 9 Tier 6 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t1_br: float = INPUT(label='Period 10 Tier 1 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t1_sr: float = INPUT(label='Period 10 Tier 1 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t1_ub: float = INPUT(label='Period 10 Tier 1 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t2_br: float = INPUT(label='Period 10 Tier 2 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t2_sr: float = INPUT(label='Period 10 Tier 2 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t2_ub: float = INPUT(label='Period 10 Tier 2 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t3_br: float = INPUT(label='Period 10 Tier 3 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t3_sr: float = INPUT(label='Period 10 Tier 3 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t3_ub: float = INPUT(label='Period 10 Tier 3 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t4_br: float = INPUT(label='Period 10 Tier 4 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t4_sr: float = INPUT(label='Period 10 Tier 4 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t4_ub: float = INPUT(label='Period 10 Tier 4 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t5_br: float = INPUT(label='Period 10 Tier 5 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t5_sr: float = INPUT(label='Period 10 Tier 5 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t5_ub: float = INPUT(label='Period 10 Tier 5 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t6_br: float = INPUT(label='Period 10 Tier 6 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t6_sr: float = INPUT(label='Period 10 Tier 6 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p10_t6_ub: float = INPUT(label='Period 10 Tier 6 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t1_br: float = INPUT(label='Period 11 Tier 1 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t1_sr: float = INPUT(label='Period 11 Tier 1 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t1_ub: float = INPUT(label='Period 11 Tier 1 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t2_br: float = INPUT(label='Period 11 Tier 2 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t2_sr: float = INPUT(label='Period 11 Tier 2 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t2_ub: float = INPUT(label='Period 11 Tier 2 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t3_br: float = INPUT(label='Period 11 Tier 3 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t3_sr: float = INPUT(label='Period 11 Tier 3 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t3_ub: float = INPUT(label='Period 11 Tier 3 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t4_br: float = INPUT(label='Period 11 Tier 4 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t4_sr: float = INPUT(label='Period 11 Tier 4 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t4_ub: float = INPUT(label='Period 11 Tier 4 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t5_br: float = INPUT(label='Period 11 Tier 5 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t5_sr: float = INPUT(label='Period 11 Tier 5 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t5_ub: float = INPUT(label='Period 11 Tier 5 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t6_br: float = INPUT(label='Period 11 Tier 6 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t6_sr: float = INPUT(label='Period 11 Tier 6 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p11_t6_ub: float = INPUT(label='Period 11 Tier 6 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t1_br: float = INPUT(label='Period 12 Tier 1 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t1_sr: float = INPUT(label='Period 12 Tier 1 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t1_ub: float = INPUT(label='Period 12 Tier 1 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t2_br: float = INPUT(label='Period 12 Tier 2 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t2_sr: float = INPUT(label='Period 12 Tier 2 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t2_ub: float = INPUT(label='Period 12 Tier 2 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t3_br: float = INPUT(label='Period 12 Tier 3 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t3_sr: float = INPUT(label='Period 12 Tier 3 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t3_ub: float = INPUT(label='Period 12 Tier 3 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t4_br: float = INPUT(label='Period 12 Tier 4 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t4_sr: float = INPUT(label='Period 12 Tier 4 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t4_ub: float = INPUT(label='Period 12 Tier 4 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t5_br: float = INPUT(label='Period 12 Tier 5 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t5_sr: float = INPUT(label='Period 12 Tier 5 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t5_ub: float = INPUT(label='Period 12 Tier 5 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t6_br: float = INPUT(label='Period 12 Tier 6 Energy Buy Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t6_sr: float = INPUT(label='Period 12 Tier 6 Energy Sell Rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_ec_p12_t6_ub: float = INPUT(label='Period 12 Tier 6 Maximum Energy Usage', units='kWh', type='NUMBER', required='?=0.0')
    ur_dc_enable: float = INPUT(label='Enable Demand Charge', units='0/1', type='NUMBER', required='?=0', constraints='BOOLEAN')
    ur_dc_sched_weekday: Matrix = INPUT(label='Demend Charge Weekday Schedule', type='MATRIX', meta='12x24')
    ur_dc_sched_weekend: Matrix = INPUT(label='Demend Charge Weekend Schedule', type='MATRIX', meta='12x24')
    ur_dc_p1_t1_dc: float = INPUT(label='Period 1 Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p1_t1_ub: float = INPUT(label='Period 1 Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p1_t2_dc: float = INPUT(label='Period 1 Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p1_t2_ub: float = INPUT(label='Period 1 Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p1_t3_dc: float = INPUT(label='Period 1 Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p1_t3_ub: float = INPUT(label='Period 1 Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p1_t4_dc: float = INPUT(label='Period 1 Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p1_t4_ub: float = INPUT(label='Period 1 Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p1_t5_dc: float = INPUT(label='Period 1 Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p1_t5_ub: float = INPUT(label='Period 1 Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p1_t6_dc: float = INPUT(label='Period 1 Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p1_t6_ub: float = INPUT(label='Period 1 Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p2_t1_dc: float = INPUT(label='Period 2 Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p2_t1_ub: float = INPUT(label='Period 2 Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p2_t2_dc: float = INPUT(label='Period 2 Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p2_t2_ub: float = INPUT(label='Period 2 Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p2_t3_dc: float = INPUT(label='Period 2 Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p2_t3_ub: float = INPUT(label='Period 2 Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p2_t4_dc: float = INPUT(label='Period 2 Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p2_t4_ub: float = INPUT(label='Period 2 Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p2_t5_dc: float = INPUT(label='Period 2 Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p2_t5_ub: float = INPUT(label='Period 2 Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p2_t6_dc: float = INPUT(label='Period 2 Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p2_t6_ub: float = INPUT(label='Period 2 Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p3_t1_dc: float = INPUT(label='Period 3 Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p3_t1_ub: float = INPUT(label='Period 3 Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p3_t2_dc: float = INPUT(label='Period 3 Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p3_t2_ub: float = INPUT(label='Period 3 Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p3_t3_dc: float = INPUT(label='Period 3 Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p3_t3_ub: float = INPUT(label='Period 3 Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p3_t4_dc: float = INPUT(label='Period 3 Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p3_t4_ub: float = INPUT(label='Period 3 Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p3_t5_dc: float = INPUT(label='Period 3 Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p3_t5_ub: float = INPUT(label='Period 3 Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p3_t6_dc: float = INPUT(label='Period 3 Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p3_t6_ub: float = INPUT(label='Period 3 Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p4_t1_dc: float = INPUT(label='Period 4 Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p4_t1_ub: float = INPUT(label='Period 4 Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p4_t2_dc: float = INPUT(label='Period 4 Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p4_t2_ub: float = INPUT(label='Period 4 Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p4_t3_dc: float = INPUT(label='Period 4 Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p4_t3_ub: float = INPUT(label='Period 4 Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p4_t4_dc: float = INPUT(label='Period 4 Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p4_t4_ub: float = INPUT(label='Period 4 Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p4_t5_dc: float = INPUT(label='Period 4 Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p4_t5_ub: float = INPUT(label='Period 4 Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p4_t6_dc: float = INPUT(label='Period 4 Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p4_t6_ub: float = INPUT(label='Period 4 Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p5_t1_dc: float = INPUT(label='Period 5 Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p5_t1_ub: float = INPUT(label='Period 5 Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p5_t2_dc: float = INPUT(label='Period 5 Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p5_t2_ub: float = INPUT(label='Period 5 Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p5_t3_dc: float = INPUT(label='Period 5 Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p5_t3_ub: float = INPUT(label='Period 5 Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p5_t4_dc: float = INPUT(label='Period 5 Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p5_t4_ub: float = INPUT(label='Period 5 Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p5_t5_dc: float = INPUT(label='Period 5 Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p5_t5_ub: float = INPUT(label='Period 5 Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p5_t6_dc: float = INPUT(label='Period 5 Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p5_t6_ub: float = INPUT(label='Period 5 Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p6_t1_dc: float = INPUT(label='Period 6 Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p6_t1_ub: float = INPUT(label='Period 6 Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p6_t2_dc: float = INPUT(label='Period 6 Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p6_t2_ub: float = INPUT(label='Period 6 Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p6_t3_dc: float = INPUT(label='Period 6 Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p6_t3_ub: float = INPUT(label='Period 6 Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p6_t4_dc: float = INPUT(label='Period 6 Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p6_t4_ub: float = INPUT(label='Period 6 Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p6_t5_dc: float = INPUT(label='Period 6 Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p6_t5_ub: float = INPUT(label='Period 6 Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p6_t6_dc: float = INPUT(label='Period 6 Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p6_t6_ub: float = INPUT(label='Period 6 Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p7_t1_dc: float = INPUT(label='Period 7 Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p7_t1_ub: float = INPUT(label='Period 7 Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p7_t2_dc: float = INPUT(label='Period 7 Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p7_t2_ub: float = INPUT(label='Period 7 Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p7_t3_dc: float = INPUT(label='Period 7 Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p7_t3_ub: float = INPUT(label='Period 7 Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p7_t4_dc: float = INPUT(label='Period 7 Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p7_t4_ub: float = INPUT(label='Period 7 Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p7_t5_dc: float = INPUT(label='Period 7 Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p7_t5_ub: float = INPUT(label='Period 7 Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p7_t6_dc: float = INPUT(label='Period 7 Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p7_t6_ub: float = INPUT(label='Period 7 Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p8_t1_dc: float = INPUT(label='Period 8 Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p8_t1_ub: float = INPUT(label='Period 8 Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p8_t2_dc: float = INPUT(label='Period 8 Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p8_t2_ub: float = INPUT(label='Period 8 Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p8_t3_dc: float = INPUT(label='Period 8 Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p8_t3_ub: float = INPUT(label='Period 8 Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p8_t4_dc: float = INPUT(label='Period 8 Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p8_t4_ub: float = INPUT(label='Period 8 Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p8_t5_dc: float = INPUT(label='Period 8 Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p8_t5_ub: float = INPUT(label='Period 8 Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p8_t6_dc: float = INPUT(label='Period 8 Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p8_t6_ub: float = INPUT(label='Period 8 Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p9_t1_dc: float = INPUT(label='Period 9 Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p9_t1_ub: float = INPUT(label='Period 9 Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p9_t2_dc: float = INPUT(label='Period 9 Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p9_t2_ub: float = INPUT(label='Period 9 Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p9_t3_dc: float = INPUT(label='Period 9 Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p9_t3_ub: float = INPUT(label='Period 9 Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p9_t4_dc: float = INPUT(label='Period 9 Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p9_t4_ub: float = INPUT(label='Period 9 Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p9_t5_dc: float = INPUT(label='Period 9 Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p9_t5_ub: float = INPUT(label='Period 9 Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p9_t6_dc: float = INPUT(label='Period 9 Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p9_t6_ub: float = INPUT(label='Period 9 Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p10_t1_dc: float = INPUT(label='Period 10 Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p10_t1_ub: float = INPUT(label='Period 10 Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p10_t2_dc: float = INPUT(label='Period 10 Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p10_t2_ub: float = INPUT(label='Period 10 Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p10_t3_dc: float = INPUT(label='Period 10 Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p10_t3_ub: float = INPUT(label='Period 10 Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p10_t4_dc: float = INPUT(label='Period 10 Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p10_t4_ub: float = INPUT(label='Period 10 Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p10_t5_dc: float = INPUT(label='Period 10 Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p10_t5_ub: float = INPUT(label='Period 10 Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p10_t6_dc: float = INPUT(label='Period 10 Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p10_t6_ub: float = INPUT(label='Period 10 Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p11_t1_dc: float = INPUT(label='Period 11 Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p11_t1_ub: float = INPUT(label='Period 11 Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p11_t2_dc: float = INPUT(label='Period 11 Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p11_t2_ub: float = INPUT(label='Period 11 Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p11_t3_dc: float = INPUT(label='Period 11 Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p11_t3_ub: float = INPUT(label='Period 11 Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p11_t4_dc: float = INPUT(label='Period 11 Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p11_t4_ub: float = INPUT(label='Period 11 Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p11_t5_dc: float = INPUT(label='Period 11 Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p11_t5_ub: float = INPUT(label='Period 11 Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p11_t6_dc: float = INPUT(label='Period 11 Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p11_t6_ub: float = INPUT(label='Period 11 Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p12_t1_dc: float = INPUT(label='Period 12 Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p12_t1_ub: float = INPUT(label='Period 12 Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p12_t2_dc: float = INPUT(label='Period 12 Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p12_t2_ub: float = INPUT(label='Period 12 Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p12_t3_dc: float = INPUT(label='Period 12 Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p12_t3_ub: float = INPUT(label='Period 12 Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p12_t4_dc: float = INPUT(label='Period 12 Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p12_t4_ub: float = INPUT(label='Period 12 Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p12_t5_dc: float = INPUT(label='Period 12 Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p12_t5_ub: float = INPUT(label='Period 12 Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_p12_t6_dc: float = INPUT(label='Period 12 Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_p12_t6_ub: float = INPUT(label='Period 12 Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jan_t1_dc: float = INPUT(label='January Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jan_t1_ub: float = INPUT(label='January Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jan_t2_dc: float = INPUT(label='January Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jan_t2_ub: float = INPUT(label='January Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jan_t3_dc: float = INPUT(label='January Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jan_t3_ub: float = INPUT(label='January Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jan_t4_dc: float = INPUT(label='January Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jan_t4_ub: float = INPUT(label='January Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jan_t5_dc: float = INPUT(label='January Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jan_t5_ub: float = INPUT(label='January Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jan_t6_dc: float = INPUT(label='January Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jan_t6_ub: float = INPUT(label='January Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_feb_t1_dc: float = INPUT(label='February Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_feb_t1_ub: float = INPUT(label='February Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_feb_t2_dc: float = INPUT(label='February Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_feb_t2_ub: float = INPUT(label='February Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_feb_t3_dc: float = INPUT(label='February Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_feb_t3_ub: float = INPUT(label='February Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_feb_t4_dc: float = INPUT(label='February Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_feb_t4_ub: float = INPUT(label='February Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_feb_t5_dc: float = INPUT(label='February Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_feb_t5_ub: float = INPUT(label='February Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_feb_t6_dc: float = INPUT(label='February Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_feb_t6_ub: float = INPUT(label='February Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_mar_t1_dc: float = INPUT(label='March Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_mar_t1_ub: float = INPUT(label='March Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_mar_t2_dc: float = INPUT(label='March Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_mar_t2_ub: float = INPUT(label='March Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_mar_t3_dc: float = INPUT(label='March Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_mar_t3_ub: float = INPUT(label='March Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_mar_t4_dc: float = INPUT(label='March Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_mar_t4_ub: float = INPUT(label='March Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_mar_t5_dc: float = INPUT(label='March Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_mar_t5_ub: float = INPUT(label='March Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_mar_t6_dc: float = INPUT(label='March Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_mar_t6_ub: float = INPUT(label='March Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_apr_t1_dc: float = INPUT(label='April Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_apr_t1_ub: float = INPUT(label='April Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_apr_t2_dc: float = INPUT(label='April Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_apr_t2_ub: float = INPUT(label='April Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_apr_t3_dc: float = INPUT(label='April Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_apr_t3_ub: float = INPUT(label='April Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_apr_t4_dc: float = INPUT(label='April Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_apr_t4_ub: float = INPUT(label='April Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_apr_t5_dc: float = INPUT(label='April Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_apr_t5_ub: float = INPUT(label='April Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_apr_t6_dc: float = INPUT(label='April Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_apr_t6_ub: float = INPUT(label='April Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_may_t1_dc: float = INPUT(label='May Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_may_t1_ub: float = INPUT(label='May Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_may_t2_dc: float = INPUT(label='May Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_may_t2_ub: float = INPUT(label='May Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_may_t3_dc: float = INPUT(label='May Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_may_t3_ub: float = INPUT(label='May Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_may_t4_dc: float = INPUT(label='May Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_may_t4_ub: float = INPUT(label='May Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_may_t5_dc: float = INPUT(label='May Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_may_t5_ub: float = INPUT(label='May Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_may_t6_dc: float = INPUT(label='May Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_may_t6_ub: float = INPUT(label='May Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jun_t1_dc: float = INPUT(label='June Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jun_t1_ub: float = INPUT(label='June Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jun_t2_dc: float = INPUT(label='June Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jun_t2_ub: float = INPUT(label='June Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jun_t3_dc: float = INPUT(label='June Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jun_t3_ub: float = INPUT(label='June Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jun_t4_dc: float = INPUT(label='June Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jun_t4_ub: float = INPUT(label='June Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jun_t5_dc: float = INPUT(label='June Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jun_t5_ub: float = INPUT(label='June Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jun_t6_dc: float = INPUT(label='June Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jun_t6_ub: float = INPUT(label='June Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jul_t1_dc: float = INPUT(label='July Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jul_t1_ub: float = INPUT(label='July Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jul_t2_dc: float = INPUT(label='July Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jul_t2_ub: float = INPUT(label='July Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jul_t3_dc: float = INPUT(label='July Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jul_t3_ub: float = INPUT(label='July Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jul_t4_dc: float = INPUT(label='July Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jul_t4_ub: float = INPUT(label='July Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jul_t5_dc: float = INPUT(label='July Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jul_t5_ub: float = INPUT(label='July Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_jul_t6_dc: float = INPUT(label='July Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_jul_t6_ub: float = INPUT(label='July Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_aug_t1_dc: float = INPUT(label='August Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_aug_t1_ub: float = INPUT(label='August Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_aug_t2_dc: float = INPUT(label='August Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_aug_t2_ub: float = INPUT(label='August Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_aug_t3_dc: float = INPUT(label='August Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_aug_t3_ub: float = INPUT(label='August Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_aug_t4_dc: float = INPUT(label='August Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_aug_t4_ub: float = INPUT(label='August Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_aug_t5_dc: float = INPUT(label='August Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_aug_t5_ub: float = INPUT(label='August Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_aug_t6_dc: float = INPUT(label='August Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_aug_t6_ub: float = INPUT(label='August Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_sep_t1_dc: float = INPUT(label='September Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_sep_t1_ub: float = INPUT(label='September Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_sep_t2_dc: float = INPUT(label='September Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_sep_t2_ub: float = INPUT(label='September Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_sep_t3_dc: float = INPUT(label='September Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_sep_t3_ub: float = INPUT(label='September Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_sep_t4_dc: float = INPUT(label='September Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_sep_t4_ub: float = INPUT(label='September Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_sep_t5_dc: float = INPUT(label='September Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_sep_t5_ub: float = INPUT(label='September Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_sep_t6_dc: float = INPUT(label='September Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_sep_t6_ub: float = INPUT(label='September Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_oct_t1_dc: float = INPUT(label='October Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_oct_t1_ub: float = INPUT(label='October Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_oct_t2_dc: float = INPUT(label='October Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_oct_t2_ub: float = INPUT(label='October Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_oct_t3_dc: float = INPUT(label='October Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_oct_t3_ub: float = INPUT(label='October Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_oct_t4_dc: float = INPUT(label='October Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_oct_t4_ub: float = INPUT(label='October Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_oct_t5_dc: float = INPUT(label='October Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_oct_t5_ub: float = INPUT(label='October Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_oct_t6_dc: float = INPUT(label='October Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_oct_t6_ub: float = INPUT(label='October Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_nov_t1_dc: float = INPUT(label='November Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_nov_t1_ub: float = INPUT(label='November Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_nov_t2_dc: float = INPUT(label='November Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_nov_t2_ub: float = INPUT(label='November Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_nov_t3_dc: float = INPUT(label='November Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_nov_t3_ub: float = INPUT(label='November Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_nov_t4_dc: float = INPUT(label='November Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_nov_t4_ub: float = INPUT(label='November Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_nov_t5_dc: float = INPUT(label='November Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_nov_t5_ub: float = INPUT(label='November Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_nov_t6_dc: float = INPUT(label='November Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_nov_t6_ub: float = INPUT(label='November Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_dec_t1_dc: float = INPUT(label='December Tier 1 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_dec_t1_ub: float = INPUT(label='December Tier 1 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_dec_t2_dc: float = INPUT(label='December Tier 2 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_dec_t2_ub: float = INPUT(label='December Tier 2 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_dec_t3_dc: float = INPUT(label='December Tier 3 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_dec_t3_ub: float = INPUT(label='December Tier 3 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_dec_t4_dc: float = INPUT(label='December Tier 4 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_dec_t4_ub: float = INPUT(label='December Tier 4 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_dec_t5_dc: float = INPUT(label='December Tier 5 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_dec_t5_ub: float = INPUT(label='December Tier 5 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    ur_dc_dec_t6_dc: float = INPUT(label='December Tier 6 Demand Charge', units='$/kW', type='NUMBER', required='?=0.0')
    ur_dc_dec_t6_ub: float = INPUT(label='December Tier 6 Peak Demand', units='kW', type='NUMBER', required='?=0.0')
    annual_energy_value: Final[Array] = OUTPUT(label='Energy value in each year', units='$', type='ARRAY', group='Annual', required='*')
    annual_electric_load: Final[Array] = OUTPUT(label='Total electric load in each year', units='kWh', type='ARRAY', group='Annual', required='*')
    elec_cost_with_system: Final[Array] = OUTPUT(label='Electricity cost with system', units='$/yr', type='ARRAY', group='Annual', required='*')
    elec_cost_without_system: Final[Array] = OUTPUT(label='Electricity cost without system', units='$/yr', type='ARRAY', group='Annual', required='*')
    elec_cost_with_system_year1: Final[float] = OUTPUT(label='Electricity cost with system', units='$/yr', type='NUMBER', group='Financial Metrics', required='*')
    elec_cost_without_system_year1: Final[float] = OUTPUT(label='Electricity cost without system', units='$/yr', type='NUMBER', group='Financial Metrics', required='*')
    savings_year1: Final[float] = OUTPUT(label='Electricity savings', units='$/yr', type='NUMBER', group='Financial Metrics', required='*')
    year1_electric_load: Final[float] = OUTPUT(label='Electricity load', units='kWh/yr', type='NUMBER', group='Financial Metrics', required='*')
    year1_hourly_e_tofromgrid: Final[Array] = OUTPUT(label='Electricity to/from grid', units='kWh', type='ARRAY', group='Time Series', required='*', constraints='LENGTH=8760')
    year1_hourly_load: Final[Array] = OUTPUT(label='Electricity load (year 1)', units='kW', type='ARRAY', group='Time Series', required='*', constraints='LENGTH=8760')
    lifetime_load: Final[Array] = OUTPUT(label='Lifetime electricity load', units='kW', type='ARRAY', group='Time Series', required='system_use_lifetime_output=1')
    year1_hourly_p_tofromgrid: Final[Array] = OUTPUT(label='Electricity to/from grid peak', units='kW', type='ARRAY', group='Time Series', required='*', constraints='LENGTH=8760')
    year1_hourly_p_system_to_load: Final[Array] = OUTPUT(label='Electricity peak load met by system', units='kW', type='ARRAY', group='Time Series', required='*', constraints='LENGTH=8760')
    year1_hourly_salespurchases_with_system: Final[Array] = OUTPUT(label='Electricity sales/purchases with sytem', units='$', type='ARRAY', group='Time Series', required='*', constraints='LENGTH=8760')
    year1_hourly_salespurchases_without_system: Final[Array] = OUTPUT(label='Electricity sales/purchases without sytem', units='$', type='ARRAY', group='Time Series', required='*', constraints='LENGTH=8760')
    year1_hourly_ec_with_system: Final[Array] = OUTPUT(label='Electricity energy charge with system', units='$', type='ARRAY', group='Time Series', required='*', constraints='LENGTH=8760')
    year1_hourly_ec_without_system: Final[Array] = OUTPUT(label='Electricity energy charge without system', units='$', type='ARRAY', group='Time Series', required='*', constraints='LENGTH=8760')
    year1_hourly_dc_with_system: Final[Array] = OUTPUT(label='Electricity demand charge with system', units='$', type='ARRAY', group='Time Series', required='*', constraints='LENGTH=8760')
    year1_hourly_dc_without_system: Final[Array] = OUTPUT(label='Electricity demand charge without system', units='$', type='ARRAY', group='Time Series', required='*', constraints='LENGTH=8760')
    year1_hourly_ec_tou_schedule: Final[Array] = OUTPUT(label='Electricity TOU period for energy charges', type='ARRAY', group='Time Series', required='*', constraints='LENGTH=8760')
    year1_hourly_dc_tou_schedule: Final[Array] = OUTPUT(label='Electricity TOU period for demand charges', type='ARRAY', group='Time Series', required='*', constraints='LENGTH=8760')
    year1_hourly_dc_peak_per_period: Final[Array] = OUTPUT(label='Electricity from grid peak per TOU period', units='kW', type='ARRAY', group='Time Series', required='*', constraints='LENGTH=8760')
    year1_monthly_fixed_with_system: Final[Array] = OUTPUT(label='Electricity charge (fixed) with system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_fixed_without_system: Final[Array] = OUTPUT(label='Electricity charge (fixed) without system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_minimum_with_system: Final[Array] = OUTPUT(label='Electricity charge (minimum) with system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_minimum_without_system: Final[Array] = OUTPUT(label='Electricity charge (minimum) without system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_dc_fixed_with_system: Final[Array] = OUTPUT(label='Electricity demand charge (fixed) with system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_dc_tou_with_system: Final[Array] = OUTPUT(label='Electricity demand charge (TOU) with system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_ec_charge_with_system: Final[Array] = OUTPUT(label='Electricity energy charge (TOU) with system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_ec_charge_flat_with_system: Final[Array] = OUTPUT(label='Electricity energy charge (flat) with system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_dc_fixed_without_system: Final[Array] = OUTPUT(label='Electricity demand charge (fixed) without system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_dc_tou_without_system: Final[Array] = OUTPUT(label='Electricity demand charge (TOU) without system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_ec_charge_without_system: Final[Array] = OUTPUT(label='Electricity energy charge (TOU) without system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_ec_charge_flat_without_system: Final[Array] = OUTPUT(label='Electricity energy charge (flat) without system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_load: Final[Array] = OUTPUT(label='Electricity load', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_electricity_to_grid: Final[Array] = OUTPUT(label='Electricity to/from grid', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_cumulative_excess_generation: Final[Array] = OUTPUT(label='Electricity net metering credit', units='kWh/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_cumulative_excess_dollars: Final[Array] = OUTPUT(label='Dollar net metering credit', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_utility_bill_w_sys: Final[Array] = OUTPUT(label='Utility bill with system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    year1_monthly_utility_bill_wo_sys: Final[Array] = OUTPUT(label='Utility bill without system', units='$/mo', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    utility_bill_w_sys_jan: Final[Array] = OUTPUT(label='Utility bill with system in Jan', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_w_sys_feb: Final[Array] = OUTPUT(label='Utility bill with system in Feb', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_w_sys_mar: Final[Array] = OUTPUT(label='Utility bill with system in Mar', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_w_sys_apr: Final[Array] = OUTPUT(label='Utility bill with system in Apr', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_w_sys_may: Final[Array] = OUTPUT(label='Utility bill with system in May', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_w_sys_jun: Final[Array] = OUTPUT(label='Utility bill with system in Jun', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_w_sys_jul: Final[Array] = OUTPUT(label='Utility bill with system in Jul', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_w_sys_aug: Final[Array] = OUTPUT(label='Utility bill with system in Aug', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_w_sys_sep: Final[Array] = OUTPUT(label='Utility bill with system in Sep', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_w_sys_oct: Final[Array] = OUTPUT(label='Utility bill with system in Oct', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_w_sys_nov: Final[Array] = OUTPUT(label='Utility bill with system in Nov', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_w_sys_dec: Final[Array] = OUTPUT(label='Utility bill with system in Dec', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_w_sys: Final[Array] = OUTPUT(label='Utility bill with system', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_wo_sys_jan: Final[Array] = OUTPUT(label='Utility bill without system in Jan', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_wo_sys_feb: Final[Array] = OUTPUT(label='Utility bill without system in Feb', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_wo_sys_mar: Final[Array] = OUTPUT(label='Utility bill without system in Mar', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_wo_sys_apr: Final[Array] = OUTPUT(label='Utility bill without system in Apr', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_wo_sys_may: Final[Array] = OUTPUT(label='Utility bill without system in May', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_wo_sys_jun: Final[Array] = OUTPUT(label='Utility bill without system in Jun', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_wo_sys_jul: Final[Array] = OUTPUT(label='Utility bill without system in Jul', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_wo_sys_aug: Final[Array] = OUTPUT(label='Utility bill without system in Aug', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_wo_sys_sep: Final[Array] = OUTPUT(label='Utility bill without system in Sep', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_wo_sys_oct: Final[Array] = OUTPUT(label='Utility bill without system in Oct', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_wo_sys_nov: Final[Array] = OUTPUT(label='Utility bill without system in Nov', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_wo_sys_dec: Final[Array] = OUTPUT(label='Utility bill without system in Dec', units='$', type='ARRAY', group='Charges by Month', required='*')
    utility_bill_wo_sys: Final[Array] = OUTPUT(label='Utility bill without system', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_fixed_jan: Final[Array] = OUTPUT(label='Fixed charge with system in Jan', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_fixed_feb: Final[Array] = OUTPUT(label='Fixed charge with system in Feb', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_fixed_mar: Final[Array] = OUTPUT(label='Fixed charge with system in Mar', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_fixed_apr: Final[Array] = OUTPUT(label='Fixed charge with system in Apr', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_fixed_may: Final[Array] = OUTPUT(label='Fixed charge with system in May', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_fixed_jun: Final[Array] = OUTPUT(label='Fixed charge with system in Jun', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_fixed_jul: Final[Array] = OUTPUT(label='Fixed charge with system in Jul', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_fixed_aug: Final[Array] = OUTPUT(label='Fixed charge with system in Aug', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_fixed_sep: Final[Array] = OUTPUT(label='Fixed charge with system in Sep', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_fixed_oct: Final[Array] = OUTPUT(label='Fixed charge with system in Oct', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_fixed_nov: Final[Array] = OUTPUT(label='Fixed charge with system in Nov', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_fixed_dec: Final[Array] = OUTPUT(label='Fixed charge with system in Dec', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_fixed: Final[Array] = OUTPUT(label='Fixed charge with system', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_fixed_jan: Final[Array] = OUTPUT(label='Fixed charge without system in Jan', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_fixed_feb: Final[Array] = OUTPUT(label='Fixed charge without system in Feb', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_fixed_mar: Final[Array] = OUTPUT(label='Fixed charge without system in Mar', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_fixed_apr: Final[Array] = OUTPUT(label='Fixed charge without system in Apr', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_fixed_may: Final[Array] = OUTPUT(label='Fixed charge without system in May', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_fixed_jun: Final[Array] = OUTPUT(label='Fixed charge without system in Jun', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_fixed_jul: Final[Array] = OUTPUT(label='Fixed charge without system in Jul', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_fixed_aug: Final[Array] = OUTPUT(label='Fixed charge without system in Aug', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_fixed_sep: Final[Array] = OUTPUT(label='Fixed charge without system in Sep', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_fixed_oct: Final[Array] = OUTPUT(label='Fixed charge without system in Oct', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_fixed_nov: Final[Array] = OUTPUT(label='Fixed charge without system in Nov', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_fixed_dec: Final[Array] = OUTPUT(label='Fixed charge without system in Dec', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_fixed: Final[Array] = OUTPUT(label='Fixed charge without system', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_minimum_jan: Final[Array] = OUTPUT(label='Minimum charge with system in Jan', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_minimum_feb: Final[Array] = OUTPUT(label='Minimum charge with system in Feb', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_minimum_mar: Final[Array] = OUTPUT(label='Minimum charge with system in Mar', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_minimum_apr: Final[Array] = OUTPUT(label='Minimum charge with system in Apr', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_minimum_may: Final[Array] = OUTPUT(label='Minimum charge with system in May', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_minimum_jun: Final[Array] = OUTPUT(label='Minimum charge with system in Jun', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_minimum_jul: Final[Array] = OUTPUT(label='Minimum charge with system in Jul', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_minimum_aug: Final[Array] = OUTPUT(label='Minimum charge with system in Aug', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_minimum_sep: Final[Array] = OUTPUT(label='Minimum charge with system in Sep', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_minimum_oct: Final[Array] = OUTPUT(label='Minimum charge with system in Oct', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_minimum_nov: Final[Array] = OUTPUT(label='Minimum charge with system in Nov', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_minimum_dec: Final[Array] = OUTPUT(label='Minimum charge with system in Dec', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_minimum: Final[Array] = OUTPUT(label='Minimum charge with system', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_minimum_jan: Final[Array] = OUTPUT(label='Minimum charge without system in Jan', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_minimum_feb: Final[Array] = OUTPUT(label='Minimum charge without system in Feb', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_minimum_mar: Final[Array] = OUTPUT(label='Minimum charge without system in Mar', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_minimum_apr: Final[Array] = OUTPUT(label='Minimum charge without system in Apr', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_minimum_may: Final[Array] = OUTPUT(label='Minimum charge without system in May', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_minimum_jun: Final[Array] = OUTPUT(label='Minimum charge without system in Jun', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_minimum_jul: Final[Array] = OUTPUT(label='Minimum charge without system in Jul', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_minimum_aug: Final[Array] = OUTPUT(label='Minimum charge without system in Aug', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_minimum_sep: Final[Array] = OUTPUT(label='Minimum charge without system in Sep', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_minimum_oct: Final[Array] = OUTPUT(label='Minimum charge without system in Oct', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_minimum_nov: Final[Array] = OUTPUT(label='Minimum charge without system in Nov', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_minimum_dec: Final[Array] = OUTPUT(label='Minimum charge without system in Dec', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_minimum: Final[Array] = OUTPUT(label='Minimum charge without system', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_fixed_jan: Final[Array] = OUTPUT(label='Demand charge with system (fixed) in Jan', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_fixed_feb: Final[Array] = OUTPUT(label='Demand charge with system (fixed) in Feb', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_fixed_mar: Final[Array] = OUTPUT(label='Demand charge with system (fixed) in Mar', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_fixed_apr: Final[Array] = OUTPUT(label='Demand charge with system (fixed) in Apr', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_fixed_may: Final[Array] = OUTPUT(label='Demand charge with system (fixed) in May', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_fixed_jun: Final[Array] = OUTPUT(label='Demand charge with system (fixed) in Jun', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_fixed_jul: Final[Array] = OUTPUT(label='Demand charge with system (fixed) in Jul', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_fixed_aug: Final[Array] = OUTPUT(label='Demand charge with system (fixed) in Aug', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_fixed_sep: Final[Array] = OUTPUT(label='Demand charge with system (fixed) in Sep', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_fixed_oct: Final[Array] = OUTPUT(label='Demand charge with system (fixed) in Oct', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_fixed_nov: Final[Array] = OUTPUT(label='Demand charge with system (fixed) in Nov', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_fixed_dec: Final[Array] = OUTPUT(label='Demand charge with system (fixed) in Dec', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_fixed: Final[Array] = OUTPUT(label='Demand charge with system (fixed)', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_tou_jan: Final[Array] = OUTPUT(label='Demand charge with system (TOU) in Jan', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_tou_feb: Final[Array] = OUTPUT(label='Demand charge with system (TOU) in Feb', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_tou_mar: Final[Array] = OUTPUT(label='Demand charge with system (TOU) in Mar', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_tou_apr: Final[Array] = OUTPUT(label='Demand charge with system (TOU) in Apr', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_tou_may: Final[Array] = OUTPUT(label='Demand charge with system (TOU) in May', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_tou_jun: Final[Array] = OUTPUT(label='Demand charge with system (TOU) in Jun', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_tou_jul: Final[Array] = OUTPUT(label='Demand charge with system (TOU) in Jul', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_tou_aug: Final[Array] = OUTPUT(label='Demand charge with system (TOU) in Aug', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_tou_sep: Final[Array] = OUTPUT(label='Demand charge with system (TOU) in Sep', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_tou_oct: Final[Array] = OUTPUT(label='Demand charge with system (TOU) in Oct', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_tou_nov: Final[Array] = OUTPUT(label='Demand charge with system (TOU) in Nov', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_tou_dec: Final[Array] = OUTPUT(label='Demand charge with system (TOU) in Dec', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_dc_tou: Final[Array] = OUTPUT(label='Demand charge with system (TOU)', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jan: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jan', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_feb: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Feb', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_mar: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Mar', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_apr: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Apr', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_may: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in May', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jun: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jun', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jul: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jul', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_aug: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Aug', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_sep: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Sep', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_oct: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Oct', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_nov: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Nov', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_dec: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Dec', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec: Final[Array] = OUTPUT(label='Energy charge with system (TOU)', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_flat_jan: Final[Array] = OUTPUT(label='Energy charge with system (flat) in Jan', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_flat_feb: Final[Array] = OUTPUT(label='Energy charge with system (flat) in Feb', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_flat_mar: Final[Array] = OUTPUT(label='Energy charge with system (flat) in Mar', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_flat_apr: Final[Array] = OUTPUT(label='Energy charge with system (flat) in Apr', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_flat_may: Final[Array] = OUTPUT(label='Energy charge with system (flat) in May', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_flat_jun: Final[Array] = OUTPUT(label='Energy charge with system (flat) in Jun', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_flat_jul: Final[Array] = OUTPUT(label='Energy charge with system (flat) in Jul', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_flat_aug: Final[Array] = OUTPUT(label='Energy charge with system (flat) in Aug', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_flat_sep: Final[Array] = OUTPUT(label='Energy charge with system (flat) in Sep', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_flat_oct: Final[Array] = OUTPUT(label='Energy charge with system (flat) in Oct', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_flat_nov: Final[Array] = OUTPUT(label='Energy charge with system (flat) in Nov', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_flat_dec: Final[Array] = OUTPUT(label='Energy charge with system (flat) in Dec', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_flat: Final[Array] = OUTPUT(label='Energy charge with system (flat)', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_fixed_jan: Final[Array] = OUTPUT(label='Demand charge without system (fixed) in Jan', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_fixed_feb: Final[Array] = OUTPUT(label='Demand charge without system (fixed) in Feb', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_fixed_mar: Final[Array] = OUTPUT(label='Demand charge without system (fixed) in Mar', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_fixed_apr: Final[Array] = OUTPUT(label='Demand charge without system (fixed) in Apr', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_fixed_may: Final[Array] = OUTPUT(label='Demand charge without system (fixed) in May', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_fixed_jun: Final[Array] = OUTPUT(label='Demand charge without system (fixed) in Jun', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_fixed_jul: Final[Array] = OUTPUT(label='Demand charge without system (fixed) in Jul', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_fixed_aug: Final[Array] = OUTPUT(label='Demand charge without system (fixed) in Aug', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_fixed_sep: Final[Array] = OUTPUT(label='Demand charge without system (fixed) in Sep', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_fixed_oct: Final[Array] = OUTPUT(label='Demand charge without system (fixed) in Oct', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_fixed_nov: Final[Array] = OUTPUT(label='Demand charge without system (fixed) in Nov', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_fixed_dec: Final[Array] = OUTPUT(label='Demand charge without system (fixed) in Dec', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_fixed: Final[Array] = OUTPUT(label='Demand charge without system (fixed)', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_tou_jan: Final[Array] = OUTPUT(label='Demand charge without system (TOU) in Jan', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_tou_feb: Final[Array] = OUTPUT(label='Demand charge without system (TOU) in Feb', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_tou_mar: Final[Array] = OUTPUT(label='Demand charge without system (TOU) in Mar', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_tou_apr: Final[Array] = OUTPUT(label='Demand charge without system (TOU) in Apr', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_tou_may: Final[Array] = OUTPUT(label='Demand charge without system (TOU) in May', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_tou_jun: Final[Array] = OUTPUT(label='Demand charge without system (TOU) in Jun', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_tou_jul: Final[Array] = OUTPUT(label='Demand charge without system (TOU) in Jul', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_tou_aug: Final[Array] = OUTPUT(label='Demand charge without system (TOU) in Aug', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_tou_sep: Final[Array] = OUTPUT(label='Demand charge without system (TOU) in Sep', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_tou_oct: Final[Array] = OUTPUT(label='Demand charge without system (TOU) in Oct', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_tou_nov: Final[Array] = OUTPUT(label='Demand charge without system (TOU) in Nov', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_tou_dec: Final[Array] = OUTPUT(label='Demand charge without system (TOU) in Dec', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_dc_tou: Final[Array] = OUTPUT(label='Demand charge without system (TOU)', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jan: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jan', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_feb: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Feb', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_mar: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Mar', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_apr: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Apr', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_may: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in May', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jun: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jun', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jul: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jul', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_aug: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Aug', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_sep: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Sep', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_oct: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Oct', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_nov: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Nov', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_dec: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Dec', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec: Final[Array] = OUTPUT(label='Energy charge without system (TOU)', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_flat_jan: Final[Array] = OUTPUT(label='Energy charge without system (flat) in Jan', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_flat_feb: Final[Array] = OUTPUT(label='Energy charge without system (flat) in Feb', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_flat_mar: Final[Array] = OUTPUT(label='Energy charge without system (flat) in Mar', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_flat_apr: Final[Array] = OUTPUT(label='Energy charge without system (flat) in Apr', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_flat_may: Final[Array] = OUTPUT(label='Energy charge without system (flat) in May', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_flat_jun: Final[Array] = OUTPUT(label='Energy charge without system (flat) in Jun', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_flat_jul: Final[Array] = OUTPUT(label='Energy charge without system (flat) in Jul', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_flat_aug: Final[Array] = OUTPUT(label='Energy charge without system (flat) in Aug', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_flat_sep: Final[Array] = OUTPUT(label='Energy charge without system (flat) in Sep', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_flat_oct: Final[Array] = OUTPUT(label='Energy charge without system (flat) in Oct', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_flat_nov: Final[Array] = OUTPUT(label='Energy charge without system (flat) in Nov', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_flat_dec: Final[Array] = OUTPUT(label='Energy charge without system (flat) in Dec', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_flat: Final[Array] = OUTPUT(label='Energy charge without system (flat)', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jan_p1: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jan for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jan_p2: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jan for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jan_p3: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jan for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jan_p4: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jan for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jan_p5: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jan for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jan_p6: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jan for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jan_p7: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jan for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jan_p8: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jan for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jan_p9: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jan for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jan_p10: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jan for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jan_p11: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jan for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jan_p12: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jan for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_feb_p1: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Feb for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_feb_p2: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Feb for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_feb_p3: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Feb for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_feb_p4: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Feb for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_feb_p5: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Feb for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_feb_p6: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Feb for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_feb_p7: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Feb for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_feb_p8: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Feb for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_feb_p9: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Feb for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_feb_p10: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Feb for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_feb_p11: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Feb for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_feb_p12: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Feb for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_mar_p1: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Mar for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_mar_p2: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Mar for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_mar_p3: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Mar for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_mar_p4: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Mar for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_mar_p5: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Mar for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_mar_p6: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Mar for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_mar_p7: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Mar for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_mar_p8: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Mar for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_mar_p9: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Mar for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_mar_p10: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Mar for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_mar_p11: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Mar for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_mar_p12: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Mar for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_apr_p1: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Apr for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_apr_p2: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Apr for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_apr_p3: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Apr for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_apr_p4: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Apr for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_apr_p5: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Apr for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_apr_p6: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Apr for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_apr_p7: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Apr for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_apr_p8: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Apr for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_apr_p9: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Apr for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_apr_p10: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Apr for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_apr_p11: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Apr for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_apr_p12: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Apr for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_may_p1: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in May for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_may_p2: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in May for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_may_p3: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in May for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_may_p4: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in May for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_may_p5: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in May for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_may_p6: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in May for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_may_p7: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in May for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_may_p8: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in May for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_may_p9: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in May for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_may_p10: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in May for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_may_p11: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in May for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_may_p12: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in May for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jun_p1: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jun for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jun_p2: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jun for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jun_p3: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jun for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jun_p4: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jun for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jun_p5: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jun for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jun_p6: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jun for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jun_p7: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jun for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jun_p8: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jun for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jun_p9: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jun for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jun_p10: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jun for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jun_p11: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jun for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jun_p12: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jun for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jul_p1: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jul for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jul_p2: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jul for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jul_p3: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jul for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jul_p4: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jul for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jul_p5: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jul for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jul_p6: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jul for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jul_p7: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jul for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jul_p8: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jul for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jul_p9: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jul for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jul_p10: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jul for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jul_p11: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jul for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_jul_p12: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Jul for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_aug_p1: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Aug for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_aug_p2: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Aug for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_aug_p3: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Aug for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_aug_p4: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Aug for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_aug_p5: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Aug for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_aug_p6: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Aug for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_aug_p7: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Aug for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_aug_p8: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Aug for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_aug_p9: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Aug for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_aug_p10: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Aug for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_aug_p11: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Aug for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_aug_p12: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Aug for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_sep_p1: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Sep for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_sep_p2: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Sep for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_sep_p3: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Sep for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_sep_p4: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Sep for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_sep_p5: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Sep for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_sep_p6: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Sep for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_sep_p7: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Sep for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_sep_p8: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Sep for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_sep_p9: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Sep for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_sep_p10: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Sep for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_sep_p11: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Sep for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_sep_p12: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Sep for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_oct_p1: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Oct for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_oct_p2: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Oct for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_oct_p3: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Oct for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_oct_p4: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Oct for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_oct_p5: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Oct for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_oct_p6: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Oct for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_oct_p7: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Oct for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_oct_p8: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Oct for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_oct_p9: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Oct for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_oct_p10: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Oct for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_oct_p11: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Oct for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_oct_p12: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Oct for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_nov_p1: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Nov for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_nov_p2: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Nov for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_nov_p3: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Nov for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_nov_p4: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Nov for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_nov_p5: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Nov for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_nov_p6: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Nov for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_nov_p7: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Nov for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_nov_p8: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Nov for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_nov_p9: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Nov for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_nov_p10: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Nov for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_nov_p11: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Nov for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_nov_p12: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Nov for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_dec_p1: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Dec for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_dec_p2: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Dec for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_dec_p3: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Dec for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_dec_p4: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Dec for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_dec_p5: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Dec for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_dec_p6: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Dec for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_dec_p7: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Dec for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_dec_p8: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Dec for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_dec_p9: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Dec for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_dec_p10: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Dec for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_dec_p11: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Dec for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_wo_sys_ec_dec_p12: Final[Array] = OUTPUT(label='Energy charge without system (TOU) in Dec for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jan_p1: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jan for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jan_p2: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jan for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jan_p3: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jan for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jan_p4: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jan for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jan_p5: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jan for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jan_p6: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jan for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jan_p7: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jan for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jan_p8: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jan for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jan_p9: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jan for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jan_p10: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jan for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jan_p11: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jan for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jan_p12: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jan for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_feb_p1: Final[Array] = OUTPUT(label='Energy without system (TOU) in Feb for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_feb_p2: Final[Array] = OUTPUT(label='Energy without system (TOU) in Feb for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_feb_p3: Final[Array] = OUTPUT(label='Energy without system (TOU) in Feb for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_feb_p4: Final[Array] = OUTPUT(label='Energy without system (TOU) in Feb for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_feb_p5: Final[Array] = OUTPUT(label='Energy without system (TOU) in Feb for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_feb_p6: Final[Array] = OUTPUT(label='Energy without system (TOU) in Feb for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_feb_p7: Final[Array] = OUTPUT(label='Energy without system (TOU) in Feb for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_feb_p8: Final[Array] = OUTPUT(label='Energy without system (TOU) in Feb for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_feb_p9: Final[Array] = OUTPUT(label='Energy without system (TOU) in Feb for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_feb_p10: Final[Array] = OUTPUT(label='Energy without system (TOU) in Feb for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_feb_p11: Final[Array] = OUTPUT(label='Energy without system (TOU) in Feb for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_feb_p12: Final[Array] = OUTPUT(label='Energy without system (TOU) in Feb for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_mar_p1: Final[Array] = OUTPUT(label='Energy without system (TOU) in Mar for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_mar_p2: Final[Array] = OUTPUT(label='Energy without system (TOU) in Mar for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_mar_p3: Final[Array] = OUTPUT(label='Energy without system (TOU) in Mar for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_mar_p4: Final[Array] = OUTPUT(label='Energy without system (TOU) in Mar for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_mar_p5: Final[Array] = OUTPUT(label='Energy without system (TOU) in Mar for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_mar_p6: Final[Array] = OUTPUT(label='Energy without system (TOU) in Mar for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_mar_p7: Final[Array] = OUTPUT(label='Energy without system (TOU) in Mar for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_mar_p8: Final[Array] = OUTPUT(label='Energy without system (TOU) in Mar for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_mar_p9: Final[Array] = OUTPUT(label='Energy without system (TOU) in Mar for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_mar_p10: Final[Array] = OUTPUT(label='Energy without system (TOU) in Mar for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_mar_p11: Final[Array] = OUTPUT(label='Energy without system (TOU) in Mar for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_mar_p12: Final[Array] = OUTPUT(label='Energy without system (TOU) in Mar for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_apr_p1: Final[Array] = OUTPUT(label='Energy without system (TOU) in Apr for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_apr_p2: Final[Array] = OUTPUT(label='Energy without system (TOU) in Apr for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_apr_p3: Final[Array] = OUTPUT(label='Energy without system (TOU) in Apr for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_apr_p4: Final[Array] = OUTPUT(label='Energy without system (TOU) in Apr for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_apr_p5: Final[Array] = OUTPUT(label='Energy without system (TOU) in Apr for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_apr_p6: Final[Array] = OUTPUT(label='Energy without system (TOU) in Apr for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_apr_p7: Final[Array] = OUTPUT(label='Energy without system (TOU) in Apr for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_apr_p8: Final[Array] = OUTPUT(label='Energy without system (TOU) in Apr for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_apr_p9: Final[Array] = OUTPUT(label='Energy without system (TOU) in Apr for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_apr_p10: Final[Array] = OUTPUT(label='Energy without system (TOU) in Apr for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_apr_p11: Final[Array] = OUTPUT(label='Energy without system (TOU) in Apr for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_apr_p12: Final[Array] = OUTPUT(label='Energy without system (TOU) in Apr for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_may_p1: Final[Array] = OUTPUT(label='Energy without system (TOU) in May for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_may_p2: Final[Array] = OUTPUT(label='Energy without system (TOU) in May for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_may_p3: Final[Array] = OUTPUT(label='Energy without system (TOU) in May for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_may_p4: Final[Array] = OUTPUT(label='Energy without system (TOU) in May for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_may_p5: Final[Array] = OUTPUT(label='Energy without system (TOU) in May for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_may_p6: Final[Array] = OUTPUT(label='Energy without system (TOU) in May for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_may_p7: Final[Array] = OUTPUT(label='Energy without system (TOU) in May for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_may_p8: Final[Array] = OUTPUT(label='Energy without system (TOU) in May for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_may_p9: Final[Array] = OUTPUT(label='Energy without system (TOU) in May for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_may_p10: Final[Array] = OUTPUT(label='Energy without system (TOU) in May for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_may_p11: Final[Array] = OUTPUT(label='Energy without system (TOU) in May for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_may_p12: Final[Array] = OUTPUT(label='Energy without system (TOU) in May for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jun_p1: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jun for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jun_p2: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jun for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jun_p3: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jun for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jun_p4: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jun for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jun_p5: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jun for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jun_p6: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jun for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jun_p7: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jun for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jun_p8: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jun for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jun_p9: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jun for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jun_p10: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jun for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jun_p11: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jun for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jun_p12: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jun for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jul_p1: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jul for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jul_p2: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jul for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jul_p3: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jul for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jul_p4: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jul for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jul_p5: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jul for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jul_p6: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jul for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jul_p7: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jul for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jul_p8: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jul for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jul_p9: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jul for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jul_p10: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jul for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jul_p11: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jul for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_jul_p12: Final[Array] = OUTPUT(label='Energy without system (TOU) in Jul for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_aug_p1: Final[Array] = OUTPUT(label='Energy without system (TOU) in Aug for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_aug_p2: Final[Array] = OUTPUT(label='Energy without system (TOU) in Aug for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_aug_p3: Final[Array] = OUTPUT(label='Energy without system (TOU) in Aug for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_aug_p4: Final[Array] = OUTPUT(label='Energy without system (TOU) in Aug for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_aug_p5: Final[Array] = OUTPUT(label='Energy without system (TOU) in Aug for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_aug_p6: Final[Array] = OUTPUT(label='Energy without system (TOU) in Aug for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_aug_p7: Final[Array] = OUTPUT(label='Energy without system (TOU) in Aug for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_aug_p8: Final[Array] = OUTPUT(label='Energy without system (TOU) in Aug for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_aug_p9: Final[Array] = OUTPUT(label='Energy without system (TOU) in Aug for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_aug_p10: Final[Array] = OUTPUT(label='Energy without system (TOU) in Aug for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_aug_p11: Final[Array] = OUTPUT(label='Energy without system (TOU) in Aug for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_aug_p12: Final[Array] = OUTPUT(label='Energy without system (TOU) in Aug for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_sep_p1: Final[Array] = OUTPUT(label='Energy without system (TOU) in Sep for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_sep_p2: Final[Array] = OUTPUT(label='Energy without system (TOU) in Sep for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_sep_p3: Final[Array] = OUTPUT(label='Energy without system (TOU) in Sep for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_sep_p4: Final[Array] = OUTPUT(label='Energy without system (TOU) in Sep for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_sep_p5: Final[Array] = OUTPUT(label='Energy without system (TOU) in Sep for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_sep_p6: Final[Array] = OUTPUT(label='Energy without system (TOU) in Sep for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_sep_p7: Final[Array] = OUTPUT(label='Energy without system (TOU) in Sep for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_sep_p8: Final[Array] = OUTPUT(label='Energy without system (TOU) in Sep for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_sep_p9: Final[Array] = OUTPUT(label='Energy without system (TOU) in Sep for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_sep_p10: Final[Array] = OUTPUT(label='Energy without system (TOU) in Sep for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_sep_p11: Final[Array] = OUTPUT(label='Energy without system (TOU) in Sep for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_sep_p12: Final[Array] = OUTPUT(label='Energy without system (TOU) in Sep for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_oct_p1: Final[Array] = OUTPUT(label='Energy without system (TOU) in Oct for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_oct_p2: Final[Array] = OUTPUT(label='Energy without system (TOU) in Oct for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_oct_p3: Final[Array] = OUTPUT(label='Energy without system (TOU) in Oct for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_oct_p4: Final[Array] = OUTPUT(label='Energy without system (TOU) in Oct for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_oct_p5: Final[Array] = OUTPUT(label='Energy without system (TOU) in Oct for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_oct_p6: Final[Array] = OUTPUT(label='Energy without system (TOU) in Oct for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_oct_p7: Final[Array] = OUTPUT(label='Energy without system (TOU) in Oct for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_oct_p8: Final[Array] = OUTPUT(label='Energy without system (TOU) in Oct for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_oct_p9: Final[Array] = OUTPUT(label='Energy without system (TOU) in Oct for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_oct_p10: Final[Array] = OUTPUT(label='Energy without system (TOU) in Oct for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_oct_p11: Final[Array] = OUTPUT(label='Energy without system (TOU) in Oct for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_oct_p12: Final[Array] = OUTPUT(label='Energy without system (TOU) in Oct for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_nov_p1: Final[Array] = OUTPUT(label='Energy without system (TOU) in Nov for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_nov_p2: Final[Array] = OUTPUT(label='Energy without system (TOU) in Nov for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_nov_p3: Final[Array] = OUTPUT(label='Energy without system (TOU) in Nov for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_nov_p4: Final[Array] = OUTPUT(label='Energy without system (TOU) in Nov for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_nov_p5: Final[Array] = OUTPUT(label='Energy without system (TOU) in Nov for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_nov_p6: Final[Array] = OUTPUT(label='Energy without system (TOU) in Nov for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_nov_p7: Final[Array] = OUTPUT(label='Energy without system (TOU) in Nov for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_nov_p8: Final[Array] = OUTPUT(label='Energy without system (TOU) in Nov for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_nov_p9: Final[Array] = OUTPUT(label='Energy without system (TOU) in Nov for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_nov_p10: Final[Array] = OUTPUT(label='Energy without system (TOU) in Nov for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_nov_p11: Final[Array] = OUTPUT(label='Energy without system (TOU) in Nov for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_nov_p12: Final[Array] = OUTPUT(label='Energy without system (TOU) in Nov for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_dec_p1: Final[Array] = OUTPUT(label='Energy without system (TOU) in Dec for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_dec_p2: Final[Array] = OUTPUT(label='Energy without system (TOU) in Dec for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_dec_p3: Final[Array] = OUTPUT(label='Energy without system (TOU) in Dec for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_dec_p4: Final[Array] = OUTPUT(label='Energy without system (TOU) in Dec for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_dec_p5: Final[Array] = OUTPUT(label='Energy without system (TOU) in Dec for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_dec_p6: Final[Array] = OUTPUT(label='Energy without system (TOU) in Dec for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_dec_p7: Final[Array] = OUTPUT(label='Energy without system (TOU) in Dec for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_dec_p8: Final[Array] = OUTPUT(label='Energy without system (TOU) in Dec for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_dec_p9: Final[Array] = OUTPUT(label='Energy without system (TOU) in Dec for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_dec_p10: Final[Array] = OUTPUT(label='Energy without system (TOU) in Dec for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_dec_p11: Final[Array] = OUTPUT(label='Energy without system (TOU) in Dec for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_wo_sys_ec_dec_p12: Final[Array] = OUTPUT(label='Energy without system (TOU) in Dec for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jan_p1: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jan for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jan_p2: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jan for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jan_p3: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jan for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jan_p4: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jan for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jan_p5: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jan for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jan_p6: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jan for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jan_p7: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jan for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jan_p8: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jan for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jan_p9: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jan for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jan_p10: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jan for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jan_p11: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jan for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jan_p12: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jan for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_feb_p1: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Feb for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_feb_p2: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Feb for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_feb_p3: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Feb for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_feb_p4: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Feb for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_feb_p5: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Feb for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_feb_p6: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Feb for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_feb_p7: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Feb for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_feb_p8: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Feb for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_feb_p9: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Feb for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_feb_p10: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Feb for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_feb_p11: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Feb for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_feb_p12: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Feb for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_mar_p1: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Mar for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_mar_p2: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Mar for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_mar_p3: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Mar for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_mar_p4: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Mar for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_mar_p5: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Mar for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_mar_p6: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Mar for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_mar_p7: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Mar for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_mar_p8: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Mar for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_mar_p9: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Mar for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_mar_p10: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Mar for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_mar_p11: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Mar for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_mar_p12: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Mar for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_apr_p1: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Apr for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_apr_p2: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Apr for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_apr_p3: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Apr for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_apr_p4: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Apr for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_apr_p5: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Apr for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_apr_p6: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Apr for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_apr_p7: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Apr for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_apr_p8: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Apr for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_apr_p9: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Apr for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_apr_p10: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Apr for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_apr_p11: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Apr for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_apr_p12: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Apr for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_may_p1: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in May for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_may_p2: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in May for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_may_p3: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in May for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_may_p4: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in May for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_may_p5: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in May for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_may_p6: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in May for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_may_p7: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in May for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_may_p8: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in May for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_may_p9: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in May for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_may_p10: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in May for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_may_p11: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in May for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_may_p12: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in May for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jun_p1: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jun for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jun_p2: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jun for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jun_p3: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jun for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jun_p4: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jun for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jun_p5: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jun for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jun_p6: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jun for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jun_p7: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jun for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jun_p8: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jun for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jun_p9: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jun for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jun_p10: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jun for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jun_p11: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jun for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jun_p12: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jun for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jul_p1: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jul for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jul_p2: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jul for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jul_p3: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jul for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jul_p4: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jul for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jul_p5: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jul for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jul_p6: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jul for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jul_p7: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jul for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jul_p8: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jul for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jul_p9: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jul for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jul_p10: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jul for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jul_p11: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jul for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_jul_p12: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Jul for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_aug_p1: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Aug for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_aug_p2: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Aug for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_aug_p3: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Aug for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_aug_p4: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Aug for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_aug_p5: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Aug for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_aug_p6: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Aug for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_aug_p7: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Aug for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_aug_p8: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Aug for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_aug_p9: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Aug for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_aug_p10: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Aug for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_aug_p11: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Aug for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_aug_p12: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Aug for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_sep_p1: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Sep for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_sep_p2: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Sep for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_sep_p3: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Sep for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_sep_p4: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Sep for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_sep_p5: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Sep for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_sep_p6: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Sep for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_sep_p7: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Sep for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_sep_p8: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Sep for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_sep_p9: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Sep for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_sep_p10: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Sep for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_sep_p11: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Sep for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_sep_p12: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Sep for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_oct_p1: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Oct for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_oct_p2: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Oct for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_oct_p3: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Oct for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_oct_p4: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Oct for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_oct_p5: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Oct for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_oct_p6: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Oct for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_oct_p7: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Oct for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_oct_p8: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Oct for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_oct_p9: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Oct for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_oct_p10: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Oct for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_oct_p11: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Oct for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_oct_p12: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Oct for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_nov_p1: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Nov for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_nov_p2: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Nov for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_nov_p3: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Nov for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_nov_p4: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Nov for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_nov_p5: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Nov for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_nov_p6: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Nov for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_nov_p7: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Nov for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_nov_p8: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Nov for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_nov_p9: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Nov for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_nov_p10: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Nov for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_nov_p11: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Nov for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_nov_p12: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Nov for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_dec_p1: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Dec for period 1 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_dec_p2: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Dec for period 2 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_dec_p3: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Dec for period 3 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_dec_p4: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Dec for period 4 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_dec_p5: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Dec for period 5 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_dec_p6: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Dec for period 6 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_dec_p7: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Dec for period 7 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_dec_p8: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Dec for period 8 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_dec_p9: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Dec for period 9 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_dec_p10: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Dec for period 10 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_dec_p11: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Dec for period 11 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    charge_w_sys_ec_dec_p12: Final[Array] = OUTPUT(label='Energy charge with system (TOU) in Dec for period 12 and tiers 1 through 6', units='$', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jan_p1: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jan for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jan_p2: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jan for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jan_p3: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jan for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jan_p4: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jan for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jan_p5: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jan for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jan_p6: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jan for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jan_p7: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jan for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jan_p8: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jan for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jan_p9: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jan for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jan_p10: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jan for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jan_p11: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jan for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jan_p12: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jan for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_feb_p1: Final[Array] = OUTPUT(label='Energy with system (TOU) in Feb for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_feb_p2: Final[Array] = OUTPUT(label='Energy with system (TOU) in Feb for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_feb_p3: Final[Array] = OUTPUT(label='Energy with system (TOU) in Feb for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_feb_p4: Final[Array] = OUTPUT(label='Energy with system (TOU) in Feb for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_feb_p5: Final[Array] = OUTPUT(label='Energy with system (TOU) in Feb for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_feb_p6: Final[Array] = OUTPUT(label='Energy with system (TOU) in Feb for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_feb_p7: Final[Array] = OUTPUT(label='Energy with system (TOU) in Feb for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_feb_p8: Final[Array] = OUTPUT(label='Energy with system (TOU) in Feb for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_feb_p9: Final[Array] = OUTPUT(label='Energy with system (TOU) in Feb for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_feb_p10: Final[Array] = OUTPUT(label='Energy with system (TOU) in Feb for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_feb_p11: Final[Array] = OUTPUT(label='Energy with system (TOU) in Feb for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_feb_p12: Final[Array] = OUTPUT(label='Energy with system (TOU) in Feb for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_mar_p1: Final[Array] = OUTPUT(label='Energy with system (TOU) in Mar for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_mar_p2: Final[Array] = OUTPUT(label='Energy with system (TOU) in Mar for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_mar_p3: Final[Array] = OUTPUT(label='Energy with system (TOU) in Mar for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_mar_p4: Final[Array] = OUTPUT(label='Energy with system (TOU) in Mar for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_mar_p5: Final[Array] = OUTPUT(label='Energy with system (TOU) in Mar for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_mar_p6: Final[Array] = OUTPUT(label='Energy with system (TOU) in Mar for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_mar_p7: Final[Array] = OUTPUT(label='Energy with system (TOU) in Mar for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_mar_p8: Final[Array] = OUTPUT(label='Energy with system (TOU) in Mar for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_mar_p9: Final[Array] = OUTPUT(label='Energy with system (TOU) in Mar for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_mar_p10: Final[Array] = OUTPUT(label='Energy with system (TOU) in Mar for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_mar_p11: Final[Array] = OUTPUT(label='Energy with system (TOU) in Mar for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_mar_p12: Final[Array] = OUTPUT(label='Energy with system (TOU) in Mar for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_apr_p1: Final[Array] = OUTPUT(label='Energy with system (TOU) in Apr for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_apr_p2: Final[Array] = OUTPUT(label='Energy with system (TOU) in Apr for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_apr_p3: Final[Array] = OUTPUT(label='Energy with system (TOU) in Apr for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_apr_p4: Final[Array] = OUTPUT(label='Energy with system (TOU) in Apr for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_apr_p5: Final[Array] = OUTPUT(label='Energy with system (TOU) in Apr for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_apr_p6: Final[Array] = OUTPUT(label='Energy with system (TOU) in Apr for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_apr_p7: Final[Array] = OUTPUT(label='Energy with system (TOU) in Apr for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_apr_p8: Final[Array] = OUTPUT(label='Energy with system (TOU) in Apr for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_apr_p9: Final[Array] = OUTPUT(label='Energy with system (TOU) in Apr for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_apr_p10: Final[Array] = OUTPUT(label='Energy with system (TOU) in Apr for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_apr_p11: Final[Array] = OUTPUT(label='Energy with system (TOU) in Apr for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_apr_p12: Final[Array] = OUTPUT(label='Energy with system (TOU) in Apr for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_may_p1: Final[Array] = OUTPUT(label='Energy with system (TOU) in May for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_may_p2: Final[Array] = OUTPUT(label='Energy with system (TOU) in May for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_may_p3: Final[Array] = OUTPUT(label='Energy with system (TOU) in May for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_may_p4: Final[Array] = OUTPUT(label='Energy with system (TOU) in May for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_may_p5: Final[Array] = OUTPUT(label='Energy with system (TOU) in May for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_may_p6: Final[Array] = OUTPUT(label='Energy with system (TOU) in May for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_may_p7: Final[Array] = OUTPUT(label='Energy with system (TOU) in May for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_may_p8: Final[Array] = OUTPUT(label='Energy with system (TOU) in May for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_may_p9: Final[Array] = OUTPUT(label='Energy with system (TOU) in May for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_may_p10: Final[Array] = OUTPUT(label='Energy with system (TOU) in May for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_may_p11: Final[Array] = OUTPUT(label='Energy with system (TOU) in May for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_may_p12: Final[Array] = OUTPUT(label='Energy with system (TOU) in May for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jun_p1: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jun for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jun_p2: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jun for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jun_p3: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jun for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jun_p4: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jun for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jun_p5: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jun for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jun_p6: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jun for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jun_p7: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jun for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jun_p8: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jun for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jun_p9: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jun for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jun_p10: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jun for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jun_p11: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jun for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jun_p12: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jun for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jul_p1: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jul for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jul_p2: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jul for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jul_p3: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jul for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jul_p4: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jul for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jul_p5: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jul for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jul_p6: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jul for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jul_p7: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jul for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jul_p8: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jul for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jul_p9: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jul for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jul_p10: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jul for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jul_p11: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jul for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_jul_p12: Final[Array] = OUTPUT(label='Energy with system (TOU) in Jul for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_aug_p1: Final[Array] = OUTPUT(label='Energy with system (TOU) in Aug for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_aug_p2: Final[Array] = OUTPUT(label='Energy with system (TOU) in Aug for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_aug_p3: Final[Array] = OUTPUT(label='Energy with system (TOU) in Aug for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_aug_p4: Final[Array] = OUTPUT(label='Energy with system (TOU) in Aug for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_aug_p5: Final[Array] = OUTPUT(label='Energy with system (TOU) in Aug for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_aug_p6: Final[Array] = OUTPUT(label='Energy with system (TOU) in Aug for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_aug_p7: Final[Array] = OUTPUT(label='Energy with system (TOU) in Aug for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_aug_p8: Final[Array] = OUTPUT(label='Energy with system (TOU) in Aug for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_aug_p9: Final[Array] = OUTPUT(label='Energy with system (TOU) in Aug for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_aug_p10: Final[Array] = OUTPUT(label='Energy with system (TOU) in Aug for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_aug_p11: Final[Array] = OUTPUT(label='Energy with system (TOU) in Aug for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_aug_p12: Final[Array] = OUTPUT(label='Energy with system (TOU) in Aug for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_sep_p1: Final[Array] = OUTPUT(label='Energy with system (TOU) in Sep for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_sep_p2: Final[Array] = OUTPUT(label='Energy with system (TOU) in Sep for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_sep_p3: Final[Array] = OUTPUT(label='Energy with system (TOU) in Sep for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_sep_p4: Final[Array] = OUTPUT(label='Energy with system (TOU) in Sep for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_sep_p5: Final[Array] = OUTPUT(label='Energy with system (TOU) in Sep for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_sep_p6: Final[Array] = OUTPUT(label='Energy with system (TOU) in Sep for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_sep_p7: Final[Array] = OUTPUT(label='Energy with system (TOU) in Sep for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_sep_p8: Final[Array] = OUTPUT(label='Energy with system (TOU) in Sep for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_sep_p9: Final[Array] = OUTPUT(label='Energy with system (TOU) in Sep for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_sep_p10: Final[Array] = OUTPUT(label='Energy with system (TOU) in Sep for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_sep_p11: Final[Array] = OUTPUT(label='Energy with system (TOU) in Sep for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_sep_p12: Final[Array] = OUTPUT(label='Energy with system (TOU) in Sep for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_oct_p1: Final[Array] = OUTPUT(label='Energy with system (TOU) in Oct for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_oct_p2: Final[Array] = OUTPUT(label='Energy with system (TOU) in Oct for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_oct_p3: Final[Array] = OUTPUT(label='Energy with system (TOU) in Oct for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_oct_p4: Final[Array] = OUTPUT(label='Energy with system (TOU) in Oct for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_oct_p5: Final[Array] = OUTPUT(label='Energy with system (TOU) in Oct for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_oct_p6: Final[Array] = OUTPUT(label='Energy with system (TOU) in Oct for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_oct_p7: Final[Array] = OUTPUT(label='Energy with system (TOU) in Oct for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_oct_p8: Final[Array] = OUTPUT(label='Energy with system (TOU) in Oct for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_oct_p9: Final[Array] = OUTPUT(label='Energy with system (TOU) in Oct for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_oct_p10: Final[Array] = OUTPUT(label='Energy with system (TOU) in Oct for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_oct_p11: Final[Array] = OUTPUT(label='Energy with system (TOU) in Oct for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_oct_p12: Final[Array] = OUTPUT(label='Energy with system (TOU) in Oct for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_nov_p1: Final[Array] = OUTPUT(label='Energy with system (TOU) in Nov for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_nov_p2: Final[Array] = OUTPUT(label='Energy with system (TOU) in Nov for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_nov_p3: Final[Array] = OUTPUT(label='Energy with system (TOU) in Nov for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_nov_p4: Final[Array] = OUTPUT(label='Energy with system (TOU) in Nov for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_nov_p5: Final[Array] = OUTPUT(label='Energy with system (TOU) in Nov for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_nov_p6: Final[Array] = OUTPUT(label='Energy with system (TOU) in Nov for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_nov_p7: Final[Array] = OUTPUT(label='Energy with system (TOU) in Nov for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_nov_p8: Final[Array] = OUTPUT(label='Energy with system (TOU) in Nov for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_nov_p9: Final[Array] = OUTPUT(label='Energy with system (TOU) in Nov for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_nov_p10: Final[Array] = OUTPUT(label='Energy with system (TOU) in Nov for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_nov_p11: Final[Array] = OUTPUT(label='Energy with system (TOU) in Nov for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_nov_p12: Final[Array] = OUTPUT(label='Energy with system (TOU) in Nov for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_dec_p1: Final[Array] = OUTPUT(label='Energy with system (TOU) in Dec for period 1 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_dec_p2: Final[Array] = OUTPUT(label='Energy with system (TOU) in Dec for period 2 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_dec_p3: Final[Array] = OUTPUT(label='Energy with system (TOU) in Dec for period 3 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_dec_p4: Final[Array] = OUTPUT(label='Energy with system (TOU) in Dec for period 4 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_dec_p5: Final[Array] = OUTPUT(label='Energy with system (TOU) in Dec for period 5 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_dec_p6: Final[Array] = OUTPUT(label='Energy with system (TOU) in Dec for period 6 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_dec_p7: Final[Array] = OUTPUT(label='Energy with system (TOU) in Dec for period 7 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_dec_p8: Final[Array] = OUTPUT(label='Energy with system (TOU) in Dec for period 8 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_dec_p9: Final[Array] = OUTPUT(label='Energy with system (TOU) in Dec for period 9 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_dec_p10: Final[Array] = OUTPUT(label='Energy with system (TOU) in Dec for period 10 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_dec_p11: Final[Array] = OUTPUT(label='Energy with system (TOU) in Dec for period 11 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')
    energy_w_sys_ec_dec_p12: Final[Array] = OUTPUT(label='Energy with system (TOU) in Dec for period 12 and tiers 1 through 6', units='kWh', type='ARRAY', group='Charges by Month', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 analysis_period: float = ...,
                 system_use_lifetime_output: float = ...,
                 gen: Array = ...,
                 load: Array = ...,
                 inflation_rate: float = ...,
                 degradation: Array = ...,
                 load_escalation: Array = ...,
                 rate_escalation: Array = ...,
                 ur_enable_net_metering: float = ...,
                 ur_excess_monthly_energy_or_dollars: float = ...,
                 ur_nm_yearend_sell_rate: float = ...,
                 ur_monthly_fixed_charge: float = ...,
                 ur_flat_buy_rate: float = ...,
                 ur_flat_sell_rate: float = ...,
                 ur_monthly_min_charge: float = ...,
                 ur_annual_min_charge: float = ...,
                 ur_ec_enable: float = ...,
                 ur_ec_sched_weekday: Matrix = ...,
                 ur_ec_sched_weekend: Matrix = ...,
                 ur_ec_p1_t1_br: float = ...,
                 ur_ec_p1_t1_sr: float = ...,
                 ur_ec_p1_t1_ub: float = ...,
                 ur_ec_p1_t2_br: float = ...,
                 ur_ec_p1_t2_sr: float = ...,
                 ur_ec_p1_t2_ub: float = ...,
                 ur_ec_p1_t3_br: float = ...,
                 ur_ec_p1_t3_sr: float = ...,
                 ur_ec_p1_t3_ub: float = ...,
                 ur_ec_p1_t4_br: float = ...,
                 ur_ec_p1_t4_sr: float = ...,
                 ur_ec_p1_t4_ub: float = ...,
                 ur_ec_p1_t5_br: float = ...,
                 ur_ec_p1_t5_sr: float = ...,
                 ur_ec_p1_t5_ub: float = ...,
                 ur_ec_p1_t6_br: float = ...,
                 ur_ec_p1_t6_sr: float = ...,
                 ur_ec_p1_t6_ub: float = ...,
                 ur_ec_p2_t1_br: float = ...,
                 ur_ec_p2_t1_sr: float = ...,
                 ur_ec_p2_t1_ub: float = ...,
                 ur_ec_p2_t2_br: float = ...,
                 ur_ec_p2_t2_sr: float = ...,
                 ur_ec_p2_t2_ub: float = ...,
                 ur_ec_p2_t3_br: float = ...,
                 ur_ec_p2_t3_sr: float = ...,
                 ur_ec_p2_t3_ub: float = ...,
                 ur_ec_p2_t4_br: float = ...,
                 ur_ec_p2_t4_sr: float = ...,
                 ur_ec_p2_t4_ub: float = ...,
                 ur_ec_p2_t5_br: float = ...,
                 ur_ec_p2_t5_sr: float = ...,
                 ur_ec_p2_t5_ub: float = ...,
                 ur_ec_p2_t6_br: float = ...,
                 ur_ec_p2_t6_sr: float = ...,
                 ur_ec_p2_t6_ub: float = ...,
                 ur_ec_p3_t1_br: float = ...,
                 ur_ec_p3_t1_sr: float = ...,
                 ur_ec_p3_t1_ub: float = ...,
                 ur_ec_p3_t2_br: float = ...,
                 ur_ec_p3_t2_sr: float = ...,
                 ur_ec_p3_t2_ub: float = ...,
                 ur_ec_p3_t3_br: float = ...,
                 ur_ec_p3_t3_sr: float = ...,
                 ur_ec_p3_t3_ub: float = ...,
                 ur_ec_p3_t4_br: float = ...,
                 ur_ec_p3_t4_sr: float = ...,
                 ur_ec_p3_t4_ub: float = ...,
                 ur_ec_p3_t5_br: float = ...,
                 ur_ec_p3_t5_sr: float = ...,
                 ur_ec_p3_t5_ub: float = ...,
                 ur_ec_p3_t6_br: float = ...,
                 ur_ec_p3_t6_sr: float = ...,
                 ur_ec_p3_t6_ub: float = ...,
                 ur_ec_p4_t1_br: float = ...,
                 ur_ec_p4_t1_sr: float = ...,
                 ur_ec_p4_t1_ub: float = ...,
                 ur_ec_p4_t2_br: float = ...,
                 ur_ec_p4_t2_sr: float = ...,
                 ur_ec_p4_t2_ub: float = ...,
                 ur_ec_p4_t3_br: float = ...,
                 ur_ec_p4_t3_sr: float = ...,
                 ur_ec_p4_t3_ub: float = ...,
                 ur_ec_p4_t4_br: float = ...,
                 ur_ec_p4_t4_sr: float = ...,
                 ur_ec_p4_t4_ub: float = ...,
                 ur_ec_p4_t5_br: float = ...,
                 ur_ec_p4_t5_sr: float = ...,
                 ur_ec_p4_t5_ub: float = ...,
                 ur_ec_p4_t6_br: float = ...,
                 ur_ec_p4_t6_sr: float = ...,
                 ur_ec_p4_t6_ub: float = ...,
                 ur_ec_p5_t1_br: float = ...,
                 ur_ec_p5_t1_sr: float = ...,
                 ur_ec_p5_t1_ub: float = ...,
                 ur_ec_p5_t2_br: float = ...,
                 ur_ec_p5_t2_sr: float = ...,
                 ur_ec_p5_t2_ub: float = ...,
                 ur_ec_p5_t3_br: float = ...,
                 ur_ec_p5_t3_sr: float = ...,
                 ur_ec_p5_t3_ub: float = ...,
                 ur_ec_p5_t4_br: float = ...,
                 ur_ec_p5_t4_sr: float = ...,
                 ur_ec_p5_t4_ub: float = ...,
                 ur_ec_p5_t5_br: float = ...,
                 ur_ec_p5_t5_sr: float = ...,
                 ur_ec_p5_t5_ub: float = ...,
                 ur_ec_p5_t6_br: float = ...,
                 ur_ec_p5_t6_sr: float = ...,
                 ur_ec_p5_t6_ub: float = ...,
                 ur_ec_p6_t1_br: float = ...,
                 ur_ec_p6_t1_sr: float = ...,
                 ur_ec_p6_t1_ub: float = ...,
                 ur_ec_p6_t2_br: float = ...,
                 ur_ec_p6_t2_sr: float = ...,
                 ur_ec_p6_t2_ub: float = ...,
                 ur_ec_p6_t3_br: float = ...,
                 ur_ec_p6_t3_sr: float = ...,
                 ur_ec_p6_t3_ub: float = ...,
                 ur_ec_p6_t4_br: float = ...,
                 ur_ec_p6_t4_sr: float = ...,
                 ur_ec_p6_t4_ub: float = ...,
                 ur_ec_p6_t5_br: float = ...,
                 ur_ec_p6_t5_sr: float = ...,
                 ur_ec_p6_t5_ub: float = ...,
                 ur_ec_p6_t6_br: float = ...,
                 ur_ec_p6_t6_sr: float = ...,
                 ur_ec_p6_t6_ub: float = ...,
                 ur_ec_p7_t1_br: float = ...,
                 ur_ec_p7_t1_sr: float = ...,
                 ur_ec_p7_t1_ub: float = ...,
                 ur_ec_p7_t2_br: float = ...,
                 ur_ec_p7_t2_sr: float = ...,
                 ur_ec_p7_t2_ub: float = ...,
                 ur_ec_p7_t3_br: float = ...,
                 ur_ec_p7_t3_sr: float = ...,
                 ur_ec_p7_t3_ub: float = ...,
                 ur_ec_p7_t4_br: float = ...,
                 ur_ec_p7_t4_sr: float = ...,
                 ur_ec_p7_t4_ub: float = ...,
                 ur_ec_p7_t5_br: float = ...,
                 ur_ec_p7_t5_sr: float = ...,
                 ur_ec_p7_t5_ub: float = ...,
                 ur_ec_p7_t6_br: float = ...,
                 ur_ec_p7_t6_sr: float = ...,
                 ur_ec_p7_t6_ub: float = ...,
                 ur_ec_p8_t1_br: float = ...,
                 ur_ec_p8_t1_sr: float = ...,
                 ur_ec_p8_t1_ub: float = ...,
                 ur_ec_p8_t2_br: float = ...,
                 ur_ec_p8_t2_sr: float = ...,
                 ur_ec_p8_t2_ub: float = ...,
                 ur_ec_p8_t3_br: float = ...,
                 ur_ec_p8_t3_sr: float = ...,
                 ur_ec_p8_t3_ub: float = ...,
                 ur_ec_p8_t4_br: float = ...,
                 ur_ec_p8_t4_sr: float = ...,
                 ur_ec_p8_t4_ub: float = ...,
                 ur_ec_p8_t5_br: float = ...,
                 ur_ec_p8_t5_sr: float = ...,
                 ur_ec_p8_t5_ub: float = ...,
                 ur_ec_p8_t6_br: float = ...,
                 ur_ec_p8_t6_sr: float = ...,
                 ur_ec_p8_t6_ub: float = ...,
                 ur_ec_p9_t1_br: float = ...,
                 ur_ec_p9_t1_sr: float = ...,
                 ur_ec_p9_t1_ub: float = ...,
                 ur_ec_p9_t2_br: float = ...,
                 ur_ec_p9_t2_sr: float = ...,
                 ur_ec_p9_t2_ub: float = ...,
                 ur_ec_p9_t3_br: float = ...,
                 ur_ec_p9_t3_sr: float = ...,
                 ur_ec_p9_t3_ub: float = ...,
                 ur_ec_p9_t4_br: float = ...,
                 ur_ec_p9_t4_sr: float = ...,
                 ur_ec_p9_t4_ub: float = ...,
                 ur_ec_p9_t5_br: float = ...,
                 ur_ec_p9_t5_sr: float = ...,
                 ur_ec_p9_t5_ub: float = ...,
                 ur_ec_p9_t6_br: float = ...,
                 ur_ec_p9_t6_sr: float = ...,
                 ur_ec_p9_t6_ub: float = ...,
                 ur_ec_p10_t1_br: float = ...,
                 ur_ec_p10_t1_sr: float = ...,
                 ur_ec_p10_t1_ub: float = ...,
                 ur_ec_p10_t2_br: float = ...,
                 ur_ec_p10_t2_sr: float = ...,
                 ur_ec_p10_t2_ub: float = ...,
                 ur_ec_p10_t3_br: float = ...,
                 ur_ec_p10_t3_sr: float = ...,
                 ur_ec_p10_t3_ub: float = ...,
                 ur_ec_p10_t4_br: float = ...,
                 ur_ec_p10_t4_sr: float = ...,
                 ur_ec_p10_t4_ub: float = ...,
                 ur_ec_p10_t5_br: float = ...,
                 ur_ec_p10_t5_sr: float = ...,
                 ur_ec_p10_t5_ub: float = ...,
                 ur_ec_p10_t6_br: float = ...,
                 ur_ec_p10_t6_sr: float = ...,
                 ur_ec_p10_t6_ub: float = ...,
                 ur_ec_p11_t1_br: float = ...,
                 ur_ec_p11_t1_sr: float = ...,
                 ur_ec_p11_t1_ub: float = ...,
                 ur_ec_p11_t2_br: float = ...,
                 ur_ec_p11_t2_sr: float = ...,
                 ur_ec_p11_t2_ub: float = ...,
                 ur_ec_p11_t3_br: float = ...,
                 ur_ec_p11_t3_sr: float = ...,
                 ur_ec_p11_t3_ub: float = ...,
                 ur_ec_p11_t4_br: float = ...,
                 ur_ec_p11_t4_sr: float = ...,
                 ur_ec_p11_t4_ub: float = ...,
                 ur_ec_p11_t5_br: float = ...,
                 ur_ec_p11_t5_sr: float = ...,
                 ur_ec_p11_t5_ub: float = ...,
                 ur_ec_p11_t6_br: float = ...,
                 ur_ec_p11_t6_sr: float = ...,
                 ur_ec_p11_t6_ub: float = ...,
                 ur_ec_p12_t1_br: float = ...,
                 ur_ec_p12_t1_sr: float = ...,
                 ur_ec_p12_t1_ub: float = ...,
                 ur_ec_p12_t2_br: float = ...,
                 ur_ec_p12_t2_sr: float = ...,
                 ur_ec_p12_t2_ub: float = ...,
                 ur_ec_p12_t3_br: float = ...,
                 ur_ec_p12_t3_sr: float = ...,
                 ur_ec_p12_t3_ub: float = ...,
                 ur_ec_p12_t4_br: float = ...,
                 ur_ec_p12_t4_sr: float = ...,
                 ur_ec_p12_t4_ub: float = ...,
                 ur_ec_p12_t5_br: float = ...,
                 ur_ec_p12_t5_sr: float = ...,
                 ur_ec_p12_t5_ub: float = ...,
                 ur_ec_p12_t6_br: float = ...,
                 ur_ec_p12_t6_sr: float = ...,
                 ur_ec_p12_t6_ub: float = ...,
                 ur_dc_enable: float = ...,
                 ur_dc_sched_weekday: Matrix = ...,
                 ur_dc_sched_weekend: Matrix = ...,
                 ur_dc_p1_t1_dc: float = ...,
                 ur_dc_p1_t1_ub: float = ...,
                 ur_dc_p1_t2_dc: float = ...,
                 ur_dc_p1_t2_ub: float = ...,
                 ur_dc_p1_t3_dc: float = ...,
                 ur_dc_p1_t3_ub: float = ...,
                 ur_dc_p1_t4_dc: float = ...,
                 ur_dc_p1_t4_ub: float = ...,
                 ur_dc_p1_t5_dc: float = ...,
                 ur_dc_p1_t5_ub: float = ...,
                 ur_dc_p1_t6_dc: float = ...,
                 ur_dc_p1_t6_ub: float = ...,
                 ur_dc_p2_t1_dc: float = ...,
                 ur_dc_p2_t1_ub: float = ...,
                 ur_dc_p2_t2_dc: float = ...,
                 ur_dc_p2_t2_ub: float = ...,
                 ur_dc_p2_t3_dc: float = ...,
                 ur_dc_p2_t3_ub: float = ...,
                 ur_dc_p2_t4_dc: float = ...,
                 ur_dc_p2_t4_ub: float = ...,
                 ur_dc_p2_t5_dc: float = ...,
                 ur_dc_p2_t5_ub: float = ...,
                 ur_dc_p2_t6_dc: float = ...,
                 ur_dc_p2_t6_ub: float = ...,
                 ur_dc_p3_t1_dc: float = ...,
                 ur_dc_p3_t1_ub: float = ...,
                 ur_dc_p3_t2_dc: float = ...,
                 ur_dc_p3_t2_ub: float = ...,
                 ur_dc_p3_t3_dc: float = ...,
                 ur_dc_p3_t3_ub: float = ...,
                 ur_dc_p3_t4_dc: float = ...,
                 ur_dc_p3_t4_ub: float = ...,
                 ur_dc_p3_t5_dc: float = ...,
                 ur_dc_p3_t5_ub: float = ...,
                 ur_dc_p3_t6_dc: float = ...,
                 ur_dc_p3_t6_ub: float = ...,
                 ur_dc_p4_t1_dc: float = ...,
                 ur_dc_p4_t1_ub: float = ...,
                 ur_dc_p4_t2_dc: float = ...,
                 ur_dc_p4_t2_ub: float = ...,
                 ur_dc_p4_t3_dc: float = ...,
                 ur_dc_p4_t3_ub: float = ...,
                 ur_dc_p4_t4_dc: float = ...,
                 ur_dc_p4_t4_ub: float = ...,
                 ur_dc_p4_t5_dc: float = ...,
                 ur_dc_p4_t5_ub: float = ...,
                 ur_dc_p4_t6_dc: float = ...,
                 ur_dc_p4_t6_ub: float = ...,
                 ur_dc_p5_t1_dc: float = ...,
                 ur_dc_p5_t1_ub: float = ...,
                 ur_dc_p5_t2_dc: float = ...,
                 ur_dc_p5_t2_ub: float = ...,
                 ur_dc_p5_t3_dc: float = ...,
                 ur_dc_p5_t3_ub: float = ...,
                 ur_dc_p5_t4_dc: float = ...,
                 ur_dc_p5_t4_ub: float = ...,
                 ur_dc_p5_t5_dc: float = ...,
                 ur_dc_p5_t5_ub: float = ...,
                 ur_dc_p5_t6_dc: float = ...,
                 ur_dc_p5_t6_ub: float = ...,
                 ur_dc_p6_t1_dc: float = ...,
                 ur_dc_p6_t1_ub: float = ...,
                 ur_dc_p6_t2_dc: float = ...,
                 ur_dc_p6_t2_ub: float = ...,
                 ur_dc_p6_t3_dc: float = ...,
                 ur_dc_p6_t3_ub: float = ...,
                 ur_dc_p6_t4_dc: float = ...,
                 ur_dc_p6_t4_ub: float = ...,
                 ur_dc_p6_t5_dc: float = ...,
                 ur_dc_p6_t5_ub: float = ...,
                 ur_dc_p6_t6_dc: float = ...,
                 ur_dc_p6_t6_ub: float = ...,
                 ur_dc_p7_t1_dc: float = ...,
                 ur_dc_p7_t1_ub: float = ...,
                 ur_dc_p7_t2_dc: float = ...,
                 ur_dc_p7_t2_ub: float = ...,
                 ur_dc_p7_t3_dc: float = ...,
                 ur_dc_p7_t3_ub: float = ...,
                 ur_dc_p7_t4_dc: float = ...,
                 ur_dc_p7_t4_ub: float = ...,
                 ur_dc_p7_t5_dc: float = ...,
                 ur_dc_p7_t5_ub: float = ...,
                 ur_dc_p7_t6_dc: float = ...,
                 ur_dc_p7_t6_ub: float = ...,
                 ur_dc_p8_t1_dc: float = ...,
                 ur_dc_p8_t1_ub: float = ...,
                 ur_dc_p8_t2_dc: float = ...,
                 ur_dc_p8_t2_ub: float = ...,
                 ur_dc_p8_t3_dc: float = ...,
                 ur_dc_p8_t3_ub: float = ...,
                 ur_dc_p8_t4_dc: float = ...,
                 ur_dc_p8_t4_ub: float = ...,
                 ur_dc_p8_t5_dc: float = ...,
                 ur_dc_p8_t5_ub: float = ...,
                 ur_dc_p8_t6_dc: float = ...,
                 ur_dc_p8_t6_ub: float = ...,
                 ur_dc_p9_t1_dc: float = ...,
                 ur_dc_p9_t1_ub: float = ...,
                 ur_dc_p9_t2_dc: float = ...,
                 ur_dc_p9_t2_ub: float = ...,
                 ur_dc_p9_t3_dc: float = ...,
                 ur_dc_p9_t3_ub: float = ...,
                 ur_dc_p9_t4_dc: float = ...,
                 ur_dc_p9_t4_ub: float = ...,
                 ur_dc_p9_t5_dc: float = ...,
                 ur_dc_p9_t5_ub: float = ...,
                 ur_dc_p9_t6_dc: float = ...,
                 ur_dc_p9_t6_ub: float = ...,
                 ur_dc_p10_t1_dc: float = ...,
                 ur_dc_p10_t1_ub: float = ...,
                 ur_dc_p10_t2_dc: float = ...,
                 ur_dc_p10_t2_ub: float = ...,
                 ur_dc_p10_t3_dc: float = ...,
                 ur_dc_p10_t3_ub: float = ...,
                 ur_dc_p10_t4_dc: float = ...,
                 ur_dc_p10_t4_ub: float = ...,
                 ur_dc_p10_t5_dc: float = ...,
                 ur_dc_p10_t5_ub: float = ...,
                 ur_dc_p10_t6_dc: float = ...,
                 ur_dc_p10_t6_ub: float = ...,
                 ur_dc_p11_t1_dc: float = ...,
                 ur_dc_p11_t1_ub: float = ...,
                 ur_dc_p11_t2_dc: float = ...,
                 ur_dc_p11_t2_ub: float = ...,
                 ur_dc_p11_t3_dc: float = ...,
                 ur_dc_p11_t3_ub: float = ...,
                 ur_dc_p11_t4_dc: float = ...,
                 ur_dc_p11_t4_ub: float = ...,
                 ur_dc_p11_t5_dc: float = ...,
                 ur_dc_p11_t5_ub: float = ...,
                 ur_dc_p11_t6_dc: float = ...,
                 ur_dc_p11_t6_ub: float = ...,
                 ur_dc_p12_t1_dc: float = ...,
                 ur_dc_p12_t1_ub: float = ...,
                 ur_dc_p12_t2_dc: float = ...,
                 ur_dc_p12_t2_ub: float = ...,
                 ur_dc_p12_t3_dc: float = ...,
                 ur_dc_p12_t3_ub: float = ...,
                 ur_dc_p12_t4_dc: float = ...,
                 ur_dc_p12_t4_ub: float = ...,
                 ur_dc_p12_t5_dc: float = ...,
                 ur_dc_p12_t5_ub: float = ...,
                 ur_dc_p12_t6_dc: float = ...,
                 ur_dc_p12_t6_ub: float = ...,
                 ur_dc_jan_t1_dc: float = ...,
                 ur_dc_jan_t1_ub: float = ...,
                 ur_dc_jan_t2_dc: float = ...,
                 ur_dc_jan_t2_ub: float = ...,
                 ur_dc_jan_t3_dc: float = ...,
                 ur_dc_jan_t3_ub: float = ...,
                 ur_dc_jan_t4_dc: float = ...,
                 ur_dc_jan_t4_ub: float = ...,
                 ur_dc_jan_t5_dc: float = ...,
                 ur_dc_jan_t5_ub: float = ...,
                 ur_dc_jan_t6_dc: float = ...,
                 ur_dc_jan_t6_ub: float = ...,
                 ur_dc_feb_t1_dc: float = ...,
                 ur_dc_feb_t1_ub: float = ...,
                 ur_dc_feb_t2_dc: float = ...,
                 ur_dc_feb_t2_ub: float = ...,
                 ur_dc_feb_t3_dc: float = ...,
                 ur_dc_feb_t3_ub: float = ...,
                 ur_dc_feb_t4_dc: float = ...,
                 ur_dc_feb_t4_ub: float = ...,
                 ur_dc_feb_t5_dc: float = ...,
                 ur_dc_feb_t5_ub: float = ...,
                 ur_dc_feb_t6_dc: float = ...,
                 ur_dc_feb_t6_ub: float = ...,
                 ur_dc_mar_t1_dc: float = ...,
                 ur_dc_mar_t1_ub: float = ...,
                 ur_dc_mar_t2_dc: float = ...,
                 ur_dc_mar_t2_ub: float = ...,
                 ur_dc_mar_t3_dc: float = ...,
                 ur_dc_mar_t3_ub: float = ...,
                 ur_dc_mar_t4_dc: float = ...,
                 ur_dc_mar_t4_ub: float = ...,
                 ur_dc_mar_t5_dc: float = ...,
                 ur_dc_mar_t5_ub: float = ...,
                 ur_dc_mar_t6_dc: float = ...,
                 ur_dc_mar_t6_ub: float = ...,
                 ur_dc_apr_t1_dc: float = ...,
                 ur_dc_apr_t1_ub: float = ...,
                 ur_dc_apr_t2_dc: float = ...,
                 ur_dc_apr_t2_ub: float = ...,
                 ur_dc_apr_t3_dc: float = ...,
                 ur_dc_apr_t3_ub: float = ...,
                 ur_dc_apr_t4_dc: float = ...,
                 ur_dc_apr_t4_ub: float = ...,
                 ur_dc_apr_t5_dc: float = ...,
                 ur_dc_apr_t5_ub: float = ...,
                 ur_dc_apr_t6_dc: float = ...,
                 ur_dc_apr_t6_ub: float = ...,
                 ur_dc_may_t1_dc: float = ...,
                 ur_dc_may_t1_ub: float = ...,
                 ur_dc_may_t2_dc: float = ...,
                 ur_dc_may_t2_ub: float = ...,
                 ur_dc_may_t3_dc: float = ...,
                 ur_dc_may_t3_ub: float = ...,
                 ur_dc_may_t4_dc: float = ...,
                 ur_dc_may_t4_ub: float = ...,
                 ur_dc_may_t5_dc: float = ...,
                 ur_dc_may_t5_ub: float = ...,
                 ur_dc_may_t6_dc: float = ...,
                 ur_dc_may_t6_ub: float = ...,
                 ur_dc_jun_t1_dc: float = ...,
                 ur_dc_jun_t1_ub: float = ...,
                 ur_dc_jun_t2_dc: float = ...,
                 ur_dc_jun_t2_ub: float = ...,
                 ur_dc_jun_t3_dc: float = ...,
                 ur_dc_jun_t3_ub: float = ...,
                 ur_dc_jun_t4_dc: float = ...,
                 ur_dc_jun_t4_ub: float = ...,
                 ur_dc_jun_t5_dc: float = ...,
                 ur_dc_jun_t5_ub: float = ...,
                 ur_dc_jun_t6_dc: float = ...,
                 ur_dc_jun_t6_ub: float = ...,
                 ur_dc_jul_t1_dc: float = ...,
                 ur_dc_jul_t1_ub: float = ...,
                 ur_dc_jul_t2_dc: float = ...,
                 ur_dc_jul_t2_ub: float = ...,
                 ur_dc_jul_t3_dc: float = ...,
                 ur_dc_jul_t3_ub: float = ...,
                 ur_dc_jul_t4_dc: float = ...,
                 ur_dc_jul_t4_ub: float = ...,
                 ur_dc_jul_t5_dc: float = ...,
                 ur_dc_jul_t5_ub: float = ...,
                 ur_dc_jul_t6_dc: float = ...,
                 ur_dc_jul_t6_ub: float = ...,
                 ur_dc_aug_t1_dc: float = ...,
                 ur_dc_aug_t1_ub: float = ...,
                 ur_dc_aug_t2_dc: float = ...,
                 ur_dc_aug_t2_ub: float = ...,
                 ur_dc_aug_t3_dc: float = ...,
                 ur_dc_aug_t3_ub: float = ...,
                 ur_dc_aug_t4_dc: float = ...,
                 ur_dc_aug_t4_ub: float = ...,
                 ur_dc_aug_t5_dc: float = ...,
                 ur_dc_aug_t5_ub: float = ...,
                 ur_dc_aug_t6_dc: float = ...,
                 ur_dc_aug_t6_ub: float = ...,
                 ur_dc_sep_t1_dc: float = ...,
                 ur_dc_sep_t1_ub: float = ...,
                 ur_dc_sep_t2_dc: float = ...,
                 ur_dc_sep_t2_ub: float = ...,
                 ur_dc_sep_t3_dc: float = ...,
                 ur_dc_sep_t3_ub: float = ...,
                 ur_dc_sep_t4_dc: float = ...,
                 ur_dc_sep_t4_ub: float = ...,
                 ur_dc_sep_t5_dc: float = ...,
                 ur_dc_sep_t5_ub: float = ...,
                 ur_dc_sep_t6_dc: float = ...,
                 ur_dc_sep_t6_ub: float = ...,
                 ur_dc_oct_t1_dc: float = ...,
                 ur_dc_oct_t1_ub: float = ...,
                 ur_dc_oct_t2_dc: float = ...,
                 ur_dc_oct_t2_ub: float = ...,
                 ur_dc_oct_t3_dc: float = ...,
                 ur_dc_oct_t3_ub: float = ...,
                 ur_dc_oct_t4_dc: float = ...,
                 ur_dc_oct_t4_ub: float = ...,
                 ur_dc_oct_t5_dc: float = ...,
                 ur_dc_oct_t5_ub: float = ...,
                 ur_dc_oct_t6_dc: float = ...,
                 ur_dc_oct_t6_ub: float = ...,
                 ur_dc_nov_t1_dc: float = ...,
                 ur_dc_nov_t1_ub: float = ...,
                 ur_dc_nov_t2_dc: float = ...,
                 ur_dc_nov_t2_ub: float = ...,
                 ur_dc_nov_t3_dc: float = ...,
                 ur_dc_nov_t3_ub: float = ...,
                 ur_dc_nov_t4_dc: float = ...,
                 ur_dc_nov_t4_ub: float = ...,
                 ur_dc_nov_t5_dc: float = ...,
                 ur_dc_nov_t5_ub: float = ...,
                 ur_dc_nov_t6_dc: float = ...,
                 ur_dc_nov_t6_ub: float = ...,
                 ur_dc_dec_t1_dc: float = ...,
                 ur_dc_dec_t1_ub: float = ...,
                 ur_dc_dec_t2_dc: float = ...,
                 ur_dc_dec_t2_ub: float = ...,
                 ur_dc_dec_t3_dc: float = ...,
                 ur_dc_dec_t3_ub: float = ...,
                 ur_dc_dec_t4_dc: float = ...,
                 ur_dc_dec_t4_ub: float = ...,
                 ur_dc_dec_t5_dc: float = ...,
                 ur_dc_dec_t5_ub: float = ...,
                 ur_dc_dec_t6_dc: float = ...,
                 ur_dc_dec_t6_ub: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
