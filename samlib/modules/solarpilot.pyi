
# This is a generated file

"""solarpilot - SolarPILOT - CSP tower solar field layout tool."""

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
        'solar_resource_file': str,
        'helio_width': float,
        'helio_height': float,
        'helio_optical_error': float,
        'helio_active_fraction': float,
        'dens_mirror': float,
        'helio_reflectance': float,
        'rec_absorptance': float,
        'rec_height': float,
        'rec_aspect': float,
        'rec_hl_perm2': float,
        'q_design': float,
        'dni_des': float,
        'land_max': float,
        'land_min': float,
        'h_tower': float,
        'c_atm_0': float,
        'c_atm_1': float,
        'c_atm_2': float,
        'c_atm_3': float,
        'n_facet_x': float,
        'n_facet_y': float,
        'focus_type': float,
        'cant_type': float,
        'n_flux_days': float,
        'delta_flux_hrs': float,
        'calc_fluxmaps': float,
        'n_flux_x': float,
        'n_flux_y': float,
        'check_max_flux': float,
        'tower_fixed_cost': float,
        'tower_exp': float,
        'rec_ref_cost': float,
        'rec_ref_area': float,
        'rec_cost_exp': float,
        'site_spec_cost': float,
        'heliostat_spec_cost': float,
        'land_spec_cost': float,
        'contingency_rate': float,
        'sales_tax_rate': float,
        'sales_tax_frac': float,
        'cost_sf_fixed': float,
        'is_optimize': float,
        'flux_max': float,
        'opt_init_step': float,
        'opt_max_iter': float,
        'opt_conv_tol': float,
        'opt_algorithm': float,
        'opt_flux_penalty': float,
        'helio_positions_in': Matrix,
        'opteff_table': Matrix,
        'flux_table': Matrix,
        'heliostat_positions': Matrix,
        'number_heliostats': float,
        'area_sf': float,
        'base_land_area': float,
        'land_area': float,
        'h_tower_opt': float,
        'rec_height_opt': float,
        'rec_aspect_opt': float,
        'flux_max_observed': float,
        'cost_rec_tot': float,
        'cost_sf_tot': float,
        'cost_tower_tot': float,
        'cost_land_tot': float,
        'cost_site_tot': float
    }, total=False)

class Data(ssc.DataDict):
    solar_resource_file: str = INPUT(label='Solar weather data file', type='STRING', group='SolarPILOT', required='?', constraints='LOCAL_FILE')
    helio_width: float = INPUT(label='Heliostat width', units='m', type='NUMBER', group='SolarPILOT', required='*')
    helio_height: float = INPUT(label='Heliostat height', units='m', type='NUMBER', group='SolarPILOT', required='*')
    helio_optical_error: float = INPUT(label='Optical error', units='rad', type='NUMBER', group='SolarPILOT', required='*')
    helio_active_fraction: float = INPUT(label='Active fraction of reflective area', units='frac', type='NUMBER', group='SolarPILOT', required='*')
    dens_mirror: float = INPUT(label='Ratio of reflective area to profile', units='frac', type='NUMBER', group='SolarPILOT', required='*')
    helio_reflectance: float = INPUT(label='Mirror reflectance', units='frac', type='NUMBER', group='SolarPILOT', required='*')
    rec_absorptance: float = INPUT(label='Absorptance', units='frac', type='NUMBER', group='SolarPILOT', required='*')
    rec_height: float = INPUT(label='Receiver height', units='m', type='NUMBER', group='SolarPILOT', required='*')
    rec_aspect: float = INPUT(label='Receiver aspect ratio (H/W)', units='frac', type='NUMBER', group='SolarPILOT', required='*')
    rec_hl_perm2: float = INPUT(label='Receiver design heat loss', units='kW/m2', type='NUMBER', group='SolarPILOT', required='*')
    q_design: float = INPUT(label='Receiver thermal design power', units='MW', type='NUMBER', group='SolarPILOT', required='*')
    dni_des: float = INPUT(label='Design-point DNI', units='W/m2', type='NUMBER', group='SolarPILOT', required='*')
    land_max: float = INPUT(label='Max heliostat-dist-to-tower-height ratio', type='NUMBER', group='SolarPILOT', required='*')
    land_min: float = INPUT(label='Min heliostat-dist-to-tower-height ratio', type='NUMBER', group='SolarPILOT', required='*')
    h_tower: float = INPUT(label='Tower height', units='m', type='NUMBER', group='SolarPILOT', required='*')
    c_atm_0: float = INPUT(label='Attenuation coefficient 0', type='NUMBER', group='SolarPILOT', required='?=0.006789')
    c_atm_1: float = INPUT(label='Attenuation coefficient 1', type='NUMBER', group='SolarPILOT', required='?=0.1046')
    c_atm_2: float = INPUT(label='Attenuation coefficient 2', type='NUMBER', group='SolarPILOT', required='?=-0.0107')
    c_atm_3: float = INPUT(label='Attenuation coefficient 3', type='NUMBER', group='SolarPILOT', required='?=0.002845')
    n_facet_x: float = INPUT(label='Number of heliostat facets - X', type='NUMBER', group='SolarPILOT', required='*')
    n_facet_y: float = INPUT(label='Number of heliostat facets - Y', type='NUMBER', group='SolarPILOT', required='*')
    focus_type: float = INPUT(label='Heliostat focus method', type='NUMBER', group='SolarPILOT', required='*')
    cant_type: float = INPUT(label='Heliostat cant method', type='NUMBER', group='SolarPILOT', required='*')
    n_flux_days: float = INPUT(label='No. days in flux map lookup', type='NUMBER', group='SolarPILOT', required='?=8')
    delta_flux_hrs: float = INPUT(label='Hourly frequency in flux map lookup', type='NUMBER', group='SolarPILOT', required='?=1')
    calc_fluxmaps: float = INPUT(label='Include fluxmap calculations', type='NUMBER', group='SolarPILOT', required='?=0')
    n_flux_x: float = INPUT(label='Flux map X resolution', type='NUMBER', group='SolarPILOT', required='?=12')
    n_flux_y: float = INPUT(label='Flux map Y resolution', type='NUMBER', group='SolarPILOT', required='?=1')
    check_max_flux: float = INPUT(label='Check max flux at design point', type='NUMBER', group='SolarPILOT', required='?=0')
    tower_fixed_cost: float = INPUT(label='Tower fixed cost', units='$', type='NUMBER', group='SolarPILOT', required='*')
    tower_exp: float = INPUT(label='Tower cost scaling exponent', type='NUMBER', group='SolarPILOT', required='*')
    rec_ref_cost: float = INPUT(label='Receiver reference cost', units='$', type='NUMBER', group='SolarPILOT', required='*')
    rec_ref_area: float = INPUT(label='Receiver reference area for cost scale', type='NUMBER', group='SolarPILOT', required='*')
    rec_cost_exp: float = INPUT(label='Receiver cost scaling exponent', type='NUMBER', group='SolarPILOT', required='*')
    site_spec_cost: float = INPUT(label='Site improvement cost', units='$/m2', type='NUMBER', group='SolarPILOT', required='*')
    heliostat_spec_cost: float = INPUT(label='Heliostat field cost', units='$/m2', type='NUMBER', group='SolarPILOT', required='*')
    land_spec_cost: float = INPUT(label='Total land area cost', units='$/acre', type='NUMBER', group='SolarPILOT', required='*')
    contingency_rate: float = INPUT(label='Contingency for cost overrun', units='%', type='NUMBER', group='SolarPILOT', required='*')
    sales_tax_rate: float = INPUT(label='Sales tax rate', units='%', type='NUMBER', group='SolarPILOT', required='*')
    sales_tax_frac: float = INPUT(label='Percent of cost to which sales tax applies', units='%', type='NUMBER', group='SolarPILOT', required='*')
    cost_sf_fixed: float = INPUT(label='Soalr field fixed cost', units='$', type='NUMBER', group='SolarPILOT', required='*')
    is_optimize: float = INPUT(label='Do SolarPILOT optimization', type='NUMBER', group='SolarPILOT', required='?=0')
    flux_max: float = INPUT(label='Maximum allowable flux', type='NUMBER', group='SolarPILOT', required='?=1000')
    opt_init_step: float = INPUT(label='Optimization initial step size', type='NUMBER', group='SolarPILOT', required='?=0.05')
    opt_max_iter: float = INPUT(label='Max. number iteration steps', type='NUMBER', group='SolarPILOT', required='?=200')
    opt_conv_tol: float = INPUT(label='Optimization convergence tol', type='NUMBER', group='SolarPILOT', required='?=0.001')
    opt_algorithm: float = INPUT(label='Optimization algorithm', type='NUMBER', group='SolarPILOT', required='?=0')
    opt_flux_penalty: float = INPUT(label='Optimization flux overage penalty', type='NUMBER', group='SolarPILOT', required='*')
    helio_positions_in: Matrix = INPUT(label='Heliostat position table', type='MATRIX', group='SolarPILOT')
    opteff_table: Final[Matrix] = OUTPUT(label='Optical efficiency (azi, zen, eff x nsim)', type='MATRIX', group='SolarPILOT', required='*')
    flux_table: Final[Matrix] = OUTPUT(label='Flux intensity table (flux(X) x (flux(y) x position)', units='frac', type='MATRIX', group='SolarPILOT', required='*')
    heliostat_positions: Final[Matrix] = OUTPUT(label='Heliostat positions (x,y)', units='m', type='MATRIX', group='SolarPILOT', required='*')
    number_heliostats: Final[float] = OUTPUT(label='Number of heliostats', type='NUMBER', group='SolarPILOT', required='*')
    area_sf: Final[float] = OUTPUT(label='Total reflective heliostat area', units='m^2', type='NUMBER', group='SolarPILOT', required='*')
    base_land_area: Final[float] = OUTPUT(label='Land area occupied by heliostats', units='acre', type='NUMBER', group='SolarPILOT', required='*')
    land_area: Final[float] = OUTPUT(label='Total land area', units='acre', type='NUMBER', group='SolarPILOT', required='*')
    h_tower_opt: Final[float] = OUTPUT(label='Optimized tower height', units='m', type='NUMBER', group='SolarPILOT', required='*')
    rec_height_opt: Final[float] = OUTPUT(label='Optimized receiver height', units='m', type='NUMBER', group='SolarPILOT', required='*')
    rec_aspect_opt: Final[float] = OUTPUT(label='Optimized receiver aspect ratio', units='-', type='NUMBER', group='SolarPILOT', required='*')
    flux_max_observed: Final[float] = OUTPUT(label='Maximum observed flux at design', units='kW/m2', type='NUMBER', group='SolarPILOT', required='check_max_flux=1')
    cost_rec_tot: Final[float] = OUTPUT(label='Total receiver cost', units='$', type='NUMBER', group='SolarPILOT', required='*')
    cost_sf_tot: Final[float] = OUTPUT(label='Total heliostat field cost', units='$', type='NUMBER', group='SolarPILOT', required='*')
    cost_tower_tot: Final[float] = OUTPUT(label='Total tower cost', units='$', type='NUMBER', group='SolarPILOT', required='*')
    cost_land_tot: Final[float] = OUTPUT(label='Total land cost', units='$', type='NUMBER', group='SolarPILOT', required='*')
    cost_site_tot: Final[float] = OUTPUT(label='Total site cost', units='$', type='NUMBER', group='SolarPILOT', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 solar_resource_file: str = ...,
                 helio_width: float = ...,
                 helio_height: float = ...,
                 helio_optical_error: float = ...,
                 helio_active_fraction: float = ...,
                 dens_mirror: float = ...,
                 helio_reflectance: float = ...,
                 rec_absorptance: float = ...,
                 rec_height: float = ...,
                 rec_aspect: float = ...,
                 rec_hl_perm2: float = ...,
                 q_design: float = ...,
                 dni_des: float = ...,
                 land_max: float = ...,
                 land_min: float = ...,
                 h_tower: float = ...,
                 c_atm_0: float = ...,
                 c_atm_1: float = ...,
                 c_atm_2: float = ...,
                 c_atm_3: float = ...,
                 n_facet_x: float = ...,
                 n_facet_y: float = ...,
                 focus_type: float = ...,
                 cant_type: float = ...,
                 n_flux_days: float = ...,
                 delta_flux_hrs: float = ...,
                 calc_fluxmaps: float = ...,
                 n_flux_x: float = ...,
                 n_flux_y: float = ...,
                 check_max_flux: float = ...,
                 tower_fixed_cost: float = ...,
                 tower_exp: float = ...,
                 rec_ref_cost: float = ...,
                 rec_ref_area: float = ...,
                 rec_cost_exp: float = ...,
                 site_spec_cost: float = ...,
                 heliostat_spec_cost: float = ...,
                 land_spec_cost: float = ...,
                 contingency_rate: float = ...,
                 sales_tax_rate: float = ...,
                 sales_tax_frac: float = ...,
                 cost_sf_fixed: float = ...,
                 is_optimize: float = ...,
                 flux_max: float = ...,
                 opt_init_step: float = ...,
                 opt_max_iter: float = ...,
                 opt_conv_tol: float = ...,
                 opt_algorithm: float = ...,
                 opt_flux_penalty: float = ...,
                 helio_positions_in: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
