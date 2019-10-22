
# This is a generated file

"""utilityrate2 - Complex utility rate structure net revenue calculator OpenEI Version 2"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'analysis_period': float,
        'hourly_gen': Array,
        'p_with_system': Array,
        'e_load': Array,
        'p_load': Array,
        'degradation': Array,
        'load_escalation': Array,
        'rate_escalation': Array,
        'ur_enable_net_metering': float,
        'ur_nm_yearend_sell_rate': float,
        'ur_monthly_fixed_charge': float,
        'ur_flat_buy_rate': float,
        'ur_flat_sell_rate': float,
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
        'elec_cost_with_system': Array,
        'elec_cost_without_system': Array,
        'year1_hourly_e_tofromgrid': Array,
        'year1_hourly_load': Array,
        'year1_hourly_p_tofromgrid': Array,
        'year1_hourly_p_system_to_load': Array,
        'year1_hourly_salespurchases_with_system': Array,
        'year1_hourly_salespurchases_without_system': Array,
        'year1_hourly_dc_with_system': Array,
        'year1_hourly_dc_without_system': Array,
        'year1_hourly_ec_tou_schedule': Array,
        'year1_hourly_dc_tou_schedule': Array,
        'year1_monthly_dc_fixed_with_system': Array,
        'year1_monthly_dc_tou_with_system': Array,
        'year1_monthly_ec_charge_with_system': Array,
        'year1_monthly_dc_fixed_without_system': Array,
        'year1_monthly_dc_tou_without_system': Array,
        'year1_monthly_ec_charge_without_system': Array,
        'year1_monthly_load': Array,
        'year1_monthly_electricity_to_grid': Array,
        'year1_monthly_cumulative_excess_generation': Array,
        'year1_monthly_salespurchases': Array,
        'year1_monthly_salespurchases_wo_sys': Array,
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
        'charge_ec_jan': Array,
        'charge_ec_feb': Array,
        'charge_ec_mar': Array,
        'charge_ec_apr': Array,
        'charge_ec_may': Array,
        'charge_ec_jun': Array,
        'charge_ec_jul': Array,
        'charge_ec_aug': Array,
        'charge_ec_sep': Array,
        'charge_ec_oct': Array,
        'charge_ec_nov': Array,
        'charge_ec_dec': Array
}, total=False)

class Data(ssc.DataDict):
    analysis_period: float = INPUT(label='Number of years in analysis', units='years', type='NUMBER', required='*', constraints='INTEGER,POSITIVE')
    hourly_gen: Array = INPUT(label='Energy at grid with system', units='kWh', type='ARRAY', required='*', constraints='LENGTH=8760')
    p_with_system: Array = INPUT(label='Max power at grid with system', units='kW', type='ARRAY', required='?', constraints='LENGTH=8760')
    e_load: Array = INPUT(label='Energy at grid without system (load only)', units='kWh', type='ARRAY', required='?', constraints='LENGTH=8760')
    p_load: Array = INPUT(label='Max power at grid without system (load only)', units='kW', type='ARRAY', required='?', constraints='LENGTH=8760')
    degradation: Array = INPUT(label='Annual energy degradation', units='%', type='ARRAY', group='AnnualOutput', required='*')
    load_escalation: Array = INPUT(label='Annual load escalation', units='%/year', type='ARRAY', required='?=0')
    rate_escalation: Array = INPUT(label='Annual utility rate escalation', units='%/year', type='ARRAY', required='?=0')
    ur_enable_net_metering: float = INPUT(label='Enable net metering', units='0/1', type='NUMBER', required='?=1', constraints='BOOLEAN', meta='Enforce net metering')
    ur_nm_yearend_sell_rate: float = INPUT(label='Year end sell rate', units='$/kWh', type='NUMBER', required='?=0.0')
    ur_monthly_fixed_charge: float = INPUT(label='Monthly fixed charge', units='$', type='NUMBER', required='?=0.0')
    ur_flat_buy_rate: float = INPUT(label='Flat rate (buy)', units='$/kWh', type='NUMBER', required='*')
    ur_flat_sell_rate: float = INPUT(label='Flat rate (sell)', units='$/kWh', type='NUMBER', required='?=0.0')
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
    ur_dc_sched_weekday: Matrix = INPUT(label='Demend Charge Weekday Schedule', type='MATRIX', required='ur_dc_enable=1', meta='12x24')
    ur_dc_sched_weekend: Matrix = INPUT(label='Demend Charge Weekend Schedule', type='MATRIX', required='ur_dc_enable=1', meta='12x24')
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
    annual_energy_value: Final[Array] = OUTPUT(label='Energy value in each year', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    elec_cost_with_system: Final[Array] = OUTPUT(label='Electricity cost with system', units='$/yr', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    elec_cost_without_system: Final[Array] = OUTPUT(label='Electricity cost without system', units='$/yr', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    year1_hourly_e_tofromgrid: Final[Array] = OUTPUT(label='Year 1 electricity to/from grid', units='kWh', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_load: Final[Array] = OUTPUT(label='Year 1 hourly electric load', units='kWh', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_p_tofromgrid: Final[Array] = OUTPUT(label='Year 1 subhourly peak to/from grid', units='kW', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_p_system_to_load: Final[Array] = OUTPUT(label='Year 1 subhourly peak load', units='kW', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_salespurchases_with_system: Final[Array] = OUTPUT(label='Year 1 hourly sales/purchases with sytem', units='$', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_salespurchases_without_system: Final[Array] = OUTPUT(label='Year 1 hourly sales/purchases without sytem', units='$', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_dc_with_system: Final[Array] = OUTPUT(label='Year 1 demand charge by hour with system', units='$/kW', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_dc_without_system: Final[Array] = OUTPUT(label='Year 1 demand charge by hour without system', units='$/kW', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_ec_tou_schedule: Final[Array] = OUTPUT(label='Hourly energy charge TOU period', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_hourly_dc_tou_schedule: Final[Array] = OUTPUT(label='Hourly demand charge TOU period', type='ARRAY', required='*', constraints='LENGTH=8760')
    year1_monthly_dc_fixed_with_system: Final[Array] = OUTPUT(label='Year 1 monthly demand charge (Fixed) with system', units='$', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_dc_tou_with_system: Final[Array] = OUTPUT(label='Year 1 monthly demand charge (TOU) with system', units='$', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_ec_charge_with_system: Final[Array] = OUTPUT(label='Year 1 monthly energy charge with system', units='$', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_dc_fixed_without_system: Final[Array] = OUTPUT(label='Year 1 monthly demand charge (Fixed) without system', units='$', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_dc_tou_without_system: Final[Array] = OUTPUT(label='Year 1 monthly demand charge (TOU) without system', units='$', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_ec_charge_without_system: Final[Array] = OUTPUT(label='Year 1 monthly energy charge without system', units='$', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_load: Final[Array] = OUTPUT(label='Year 1 monthly electric load', units='kWh', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_electricity_to_grid: Final[Array] = OUTPUT(label='Year 1 monthly electricity to/from grid', units='kWh', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_cumulative_excess_generation: Final[Array] = OUTPUT(label='Year 1 monthly net metering credit', units='kWh', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_salespurchases: Final[Array] = OUTPUT(label='Year 1 monthly sales/purchases with system', units='$', type='ARRAY', required='*', constraints='LENGTH=12')
    year1_monthly_salespurchases_wo_sys: Final[Array] = OUTPUT(label='Year 1 monthly sales/purchases without system', units='$', type='ARRAY', required='*', constraints='LENGTH=12')
    charge_dc_fixed_jan: Final[Array] = OUTPUT(label='Demand Charge (Fixed) in Jan', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_feb: Final[Array] = OUTPUT(label='Demand Charge (Fixed) in Feb', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_mar: Final[Array] = OUTPUT(label='Demand Charge (Fixed) in Mar', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_apr: Final[Array] = OUTPUT(label='Demand Charge (Fixed) in Apr', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_may: Final[Array] = OUTPUT(label='Demand Charge (Fixed) in May', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_jun: Final[Array] = OUTPUT(label='Demand Charge (Fixed) in Jun', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_jul: Final[Array] = OUTPUT(label='Demand Charge (Fixed) in Jul', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_aug: Final[Array] = OUTPUT(label='Demand Charge (Fixed) in Aug', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_sep: Final[Array] = OUTPUT(label='Demand Charge (Fixed) in Sep', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_oct: Final[Array] = OUTPUT(label='Demand Charge (Fixed) in Oct', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_nov: Final[Array] = OUTPUT(label='Demand Charge (Fixed) in Nov', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_fixed_dec: Final[Array] = OUTPUT(label='Demand Charge (Fixed) in Dec', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_jan: Final[Array] = OUTPUT(label='Demand Charge (TOU) in Jan', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_feb: Final[Array] = OUTPUT(label='Demand Charge (TOU) in Feb', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_mar: Final[Array] = OUTPUT(label='Demand Charge (TOU) in Mar', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_apr: Final[Array] = OUTPUT(label='Demand Charge (TOU) in Apr', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_may: Final[Array] = OUTPUT(label='Demand Charge (TOU) in May', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_jun: Final[Array] = OUTPUT(label='Demand Charge (TOU) in Jun', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_jul: Final[Array] = OUTPUT(label='Demand Charge (TOU) in Jul', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_aug: Final[Array] = OUTPUT(label='Demand Charge (TOU) in Aug', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_sep: Final[Array] = OUTPUT(label='Demand Charge (TOU) in Sep', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_oct: Final[Array] = OUTPUT(label='Demand Charge (TOU) in Oct', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_nov: Final[Array] = OUTPUT(label='Demand Charge (TOU) in Nov', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_dc_tou_dec: Final[Array] = OUTPUT(label='Demand Charge (TOU) in Dec', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_ec_jan: Final[Array] = OUTPUT(label='Energy Charge in Jan', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_ec_feb: Final[Array] = OUTPUT(label='Energy Charge in Feb', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_ec_mar: Final[Array] = OUTPUT(label='Energy Charge in Mar', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_ec_apr: Final[Array] = OUTPUT(label='Energy Charge in Apr', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_ec_may: Final[Array] = OUTPUT(label='Energy Charge in May', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_ec_jun: Final[Array] = OUTPUT(label='Energy Charge in Jun', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_ec_jul: Final[Array] = OUTPUT(label='Energy Charge in Jul', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_ec_aug: Final[Array] = OUTPUT(label='Energy Charge in Aug', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_ec_sep: Final[Array] = OUTPUT(label='Energy Charge in Sep', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_ec_oct: Final[Array] = OUTPUT(label='Energy Charge in Oct', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_ec_nov: Final[Array] = OUTPUT(label='Energy Charge in Nov', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')
    charge_ec_dec: Final[Array] = OUTPUT(label='Energy Charge in Dec', units='$', type='ARRAY', required='*', constraints='LENGTH_EQUAL=analysis_period')

    def __init__(self, *args: Mapping[str, Any],
                 analysis_period: float = ...,
                 hourly_gen: Array = ...,
                 p_with_system: Array = ...,
                 e_load: Array = ...,
                 p_load: Array = ...,
                 degradation: Array = ...,
                 load_escalation: Array = ...,
                 rate_escalation: Array = ...,
                 ur_enable_net_metering: float = ...,
                 ur_nm_yearend_sell_rate: float = ...,
                 ur_monthly_fixed_charge: float = ...,
                 ur_flat_buy_rate: float = ...,
                 ur_flat_sell_rate: float = ...,
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
