
# This is a generated file

"""cb_mspt_system_costs - CSP molten salt power tower system costs"""

# VERSION: 0

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
        'A_sf': float,
        'site_spec_cost': float,
        'heliostat_spec_cost': float,
        'csp.pt.cost.fixed_sf': float,
        'h_tower': float,
        'H_rec': float,
        'helio_height': float,
        'tower_fixed_cost': float,
        'tower_exp': float,
        'csp.pt.cost.receiver.area': float,
        'rec_ref_cost': float,
        'rec_ref_area': float,
        'rec_cost_exp': float,
        'csp.pt.cost.storage_mwht': float,
        'tes_spec_cost': float,
        'P_ref': float,
        'csp.pt.cost.power_block_per_kwe': float,
        'bop_spec_cost': float,
        'fossil_spec_cost': float,
        'contingency_rate': float,
        'csp.pt.cost.total_land_area': float,
        'system_capacity': float,
        'csp.pt.cost.epc.per_acre': float,
        'csp.pt.cost.epc.percent': float,
        'csp.pt.cost.epc.per_watt': float,
        'csp.pt.cost.epc.fixed': float,
        'csp.pt.cost.plm.per_acre': float,
        'csp.pt.cost.plm.percent': float,
        'csp.pt.cost.plm.per_watt': float,
        'csp.pt.cost.plm.fixed': float,
        'sales_tax_frac': float,
        'sales_tax_rate': float,
        'csp.pt.cost.site_improvements': float,
        'csp.pt.cost.heliostats': float,
        'csp.pt.cost.tower': float,
        'csp.pt.cost.receiver': float,
        'csp.pt.cost.storage': float,
        'csp.pt.cost.power_block': float,
        'csp.pt.cost.bop': float,
        'csp.pt.cost.fossil': float,
        'ui_direct_subtotal': float,
        'csp.pt.cost.contingency': float,
        'total_direct_cost': float,
        'csp.pt.cost.epc.total': float,
        'csp.pt.cost.plm.total': float,
        'csp.pt.cost.sales_tax.total': float,
        'total_indirect_cost': float,
        'total_installed_cost': float,
        'csp.pt.cost.installed_per_capacity': float
    }, total=False)

class Data(ssc.DataDict):
    A_sf: float = INPUT(label='Total reflective solar field area', units='m2', type='NUMBER', group='heliostat', required='*')
    site_spec_cost: float = INPUT(label='Site improvement cost', units='$/m2', type='NUMBER', group='system_costs', required='*')
    heliostat_spec_cost: float = INPUT(label='Heliostat field cost', units='$/m2', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_fixed_sf: float = INPUT(name='csp.pt.cost.fixed_sf', label='Heliostat field cost fixed', units='$', type='NUMBER', group='system_costs', required='*')
    h_tower: float = INPUT(label='Tower height', units='m', type='NUMBER', group='receiver', required='*')
    H_rec: float = INPUT(label='The height of the receiver', units='m', type='NUMBER', group='receiver', required='*')
    helio_height: float = INPUT(label='Heliostat height', units='m', type='NUMBER', group='receiver', required='*')
    tower_fixed_cost: float = INPUT(label='Tower fixed cost', units='$', type='NUMBER', group='system_costs', required='*')
    tower_exp: float = INPUT(label='Tower cost scaling exponent', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_receiver_area: float = INPUT(name='csp.pt.cost.receiver.area', label='Receiver area', units='m2', type='NUMBER', group='receiver', required='*')
    rec_ref_cost: float = INPUT(label='Receiver reference cost', units='$', type='NUMBER', group='system_costs', required='*')
    rec_ref_area: float = INPUT(label='Receiver reference area for cost scale', type='NUMBER', group='system_costs', required='*')
    rec_cost_exp: float = INPUT(label='Receiver cost scaling exponent', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_storage_mwht: float = INPUT(name='csp.pt.cost.storage_mwht', label='Storage capacity', units='MWt-hr', type='NUMBER', group='TES', required='*')
    tes_spec_cost: float = INPUT(label='Thermal energy storage cost', units='$/kWht', type='NUMBER', group='system_costs', required='*')
    P_ref: float = INPUT(label='Reference output electric power at design condition', units='MWe', type='NUMBER', group='system_design', required='*')
    csp_pt_cost_power_block_per_kwe: float = INPUT(name='csp.pt.cost.power_block_per_kwe', label='Power cycle specific cost', units='$/kWe', type='NUMBER', group='system_costs', required='*')
    bop_spec_cost: float = INPUT(label='BOP specific cost', units='$/kWe', type='NUMBER', group='system_costs', required='*')
    fossil_spec_cost: float = INPUT(label='Fossil system specific cost', units='$/kWe', type='NUMBER', group='system_costs', required='*')
    contingency_rate: float = INPUT(label='Contingency for cost overrun', units='%', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_total_land_area: float = INPUT(name='csp.pt.cost.total_land_area', label='Total land area', units='acre', type='NUMBER', group='system_costs', required='*')
    system_capacity: float = INPUT(label='Nameplate capacity', units='MWe', type='NUMBER', group='system_design', required='*')
    csp_pt_cost_epc_per_acre: float = INPUT(name='csp.pt.cost.epc.per_acre', label='EPC cost per acre', units='$/acre', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_epc_percent: float = INPUT(name='csp.pt.cost.epc.percent', label='EPC cost percent of direct', units='%', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_epc_per_watt: float = INPUT(name='csp.pt.cost.epc.per_watt', label='EPC cost per watt', units='$/W', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_epc_fixed: float = INPUT(name='csp.pt.cost.epc.fixed', label='EPC fixed', units='$', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_plm_per_acre: float = INPUT(name='csp.pt.cost.plm.per_acre', label='PLM cost per acre', units='$/acre', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_plm_percent: float = INPUT(name='csp.pt.cost.plm.percent', label='PLM cost percent of direct', units='%', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_plm_per_watt: float = INPUT(name='csp.pt.cost.plm.per_watt', label='PLM cost per watt', units='$/W', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_plm_fixed: float = INPUT(name='csp.pt.cost.plm.fixed', label='PLM fixed', units='$', type='NUMBER', group='system_costs', required='*')
    sales_tax_frac: float = INPUT(label='Percent of cost to which sales tax applies', units='%', type='NUMBER', group='system_costs', required='*')
    sales_tax_rate: float = INPUT(label='Sales tax rate', units='%', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_site_improvements: Final[float] = OUTPUT(name='csp.pt.cost.site_improvements', label='Site improvement cost', units='$', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_heliostats: Final[float] = OUTPUT(name='csp.pt.cost.heliostats', label='Heliostat cost', units='$', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_tower: Final[float] = OUTPUT(name='csp.pt.cost.tower', label='Tower cost', units='$', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_receiver: Final[float] = OUTPUT(name='csp.pt.cost.receiver', label='Receiver cost', units='$', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_storage: Final[float] = OUTPUT(name='csp.pt.cost.storage', label='TES cost', units='$', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_power_block: Final[float] = OUTPUT(name='csp.pt.cost.power_block', label='Power cycle cost', units='$', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_bop: Final[float] = OUTPUT(name='csp.pt.cost.bop', label='BOP cost', units='$', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_fossil: Final[float] = OUTPUT(name='csp.pt.cost.fossil', label='Fossil backup cost', units='$', type='NUMBER', group='system_costs', required='*')
    ui_direct_subtotal: Final[float] = OUTPUT(label='Direct capital precontingency cost', units='$', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_contingency: Final[float] = OUTPUT(name='csp.pt.cost.contingency', label='Contingency cost', units='$', type='NUMBER', group='system_costs', required='*')
    total_direct_cost: Final[float] = OUTPUT(label='Total direct cost', units='$', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_epc_total: Final[float] = OUTPUT(name='csp.pt.cost.epc.total', label='EPC and owner cost', units='$', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_plm_total: Final[float] = OUTPUT(name='csp.pt.cost.plm.total', label='Total land cost', units='$', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_sales_tax_total: Final[float] = OUTPUT(name='csp.pt.cost.sales_tax.total', label='Sales tax cost', units='$', type='NUMBER', group='system_costs', required='*')
    total_indirect_cost: Final[float] = OUTPUT(label='Total indirect cost', units='$', type='NUMBER', group='system_costs', required='*')
    total_installed_cost: Final[float] = OUTPUT(label='Total installed cost', units='$', type='NUMBER', group='system_costs', required='*')
    csp_pt_cost_installed_per_capacity: Final[float] = OUTPUT(name='csp.pt.cost.installed_per_capacity', label='Estimated installed cost per cap', units='$', type='NUMBER', group='system_costs', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 A_sf: float = ...,
                 site_spec_cost: float = ...,
                 heliostat_spec_cost: float = ...,
                 csp_pt_cost_fixed_sf: float = ...,
                 h_tower: float = ...,
                 H_rec: float = ...,
                 helio_height: float = ...,
                 tower_fixed_cost: float = ...,
                 tower_exp: float = ...,
                 csp_pt_cost_receiver_area: float = ...,
                 rec_ref_cost: float = ...,
                 rec_ref_area: float = ...,
                 rec_cost_exp: float = ...,
                 csp_pt_cost_storage_mwht: float = ...,
                 tes_spec_cost: float = ...,
                 P_ref: float = ...,
                 csp_pt_cost_power_block_per_kwe: float = ...,
                 bop_spec_cost: float = ...,
                 fossil_spec_cost: float = ...,
                 contingency_rate: float = ...,
                 csp_pt_cost_total_land_area: float = ...,
                 system_capacity: float = ...,
                 csp_pt_cost_epc_per_acre: float = ...,
                 csp_pt_cost_epc_percent: float = ...,
                 csp_pt_cost_epc_per_watt: float = ...,
                 csp_pt_cost_epc_fixed: float = ...,
                 csp_pt_cost_plm_per_acre: float = ...,
                 csp_pt_cost_plm_percent: float = ...,
                 csp_pt_cost_plm_per_watt: float = ...,
                 csp_pt_cost_plm_fixed: float = ...,
                 sales_tax_frac: float = ...,
                 sales_tax_rate: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
