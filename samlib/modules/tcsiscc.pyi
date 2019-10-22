
# This is a generated file

"""tcsiscc - Triple pressure NGCC integrated with MS power tower"""

# VERSION: 4

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'solar_resource_file': str,
        'system_capacity': float,
        'run_type': float,
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
        'land_bound_type': float,
        'land_max': float,
        'land_min': float,
        'land_bound_table': Matrix,
        'land_bound_list': Array,
        'dni_des': float,
        'p_start': float,
        'p_track': float,
        'hel_stow_deploy': float,
        'v_wind_max': float,
        'interp_nug': float,
        'interp_beta': float,
        'n_flux_x': float,
        'n_flux_y': float,
        'helio_positions': Matrix,
        'helio_aim_points': Matrix,
        'N_hel': float,
        'eta_map': Matrix,
        'flux_positions': Matrix,
        'flux_maps': Matrix,
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
        'h_tower': float,
        'q_design': float,
        'calc_fluxmaps': float,
        'tower_fixed_cost': float,
        'tower_exp': float,
        'rec_ref_cost': float,
        'rec_ref_area': float,
        'rec_cost_exp': float,
        'site_spec_cost': float,
        'heliostat_spec_cost': float,
        'plant_spec_cost': float,
        'bop_spec_cost': float,
        'tes_spec_cost': float,
        'land_spec_cost': float,
        'contingency_rate': float,
        'sales_tax_rate': float,
        'sales_tax_frac': float,
        'cost_sf_fixed': float,
        'fossil_spec_cost': float,
        'is_optimize': float,
        'flux_max': float,
        'opt_init_step': float,
        'opt_max_iter': float,
        'opt_conv_tol': float,
        'opt_flux_penalty': float,
        'opt_algorithm': float,
        'check_max_flux': float,
        'csp.pt.cost.epc.per_acre': float,
        'csp.pt.cost.epc.percent': float,
        'csp.pt.cost.epc.per_watt': float,
        'csp.pt.cost.epc.fixed': float,
        'csp.pt.cost.plm.per_acre': float,
        'csp.pt.cost.plm.percent': float,
        'csp.pt.cost.plm.per_watt': float,
        'csp.pt.cost.plm.fixed': float,
        'csp.pt.sf.fixed_land_area': float,
        'csp.pt.sf.land_overhead_factor': float,
        'total_installed_cost': float,
        'receiver_type': float,
        'N_panels': float,
        'D_rec': float,
        'H_rec': float,
        'THT': float,
        'd_tube_out': float,
        'th_tube': float,
        'mat_tube': float,
        'rec_htf': float,
        'field_fl_props': Matrix,
        'Flow_type': float,
        'crossover_shift': float,
        'epsilon': float,
        'hl_ffact': float,
        'T_htf_hot_des': float,
        'T_htf_cold_des': float,
        'f_rec_min': float,
        'Q_rec_des': float,
        'rec_su_delay': float,
        'rec_qf_delay': float,
        'm_dot_htf_max': float,
        'A_sf': float,
        'eta_pump': float,
        'q_pb_design': float,
        'elev': float,
        'ngcc_model': float,
        'pinch_point_hotside': float,
        'pinch_point_coldside': float,
        'pb_pump_coef': float,
        'piping_loss': float,
        'piping_length': float,
        'piping_length_mult': float,
        'piping_length_const': float,
        'pb_fixed_par': float,
        'bop_par': float,
        'bop_par_f': float,
        'bop_par_0': float,
        'bop_par_1': float,
        'bop_par_2': float,
        'fossil_output': float,
        'W_dot_solar_des': float,
        'month': Array,
        'hour': Array,
        'solazi': Array,
        'solzen': Array,
        'beam': Array,
        'tdry': Array,
        'twet': Array,
        'wspd': Array,
        'pres': Array,
        'eta_field': Array,
        'field_eff_adj': Array,
        'eta_therm': Array,
        'Q_solar_total': Array,
        'q_conv_sum': Array,
        'q_rad_sum': Array,
        'Q_thermal': Array,
        'm_dot_ss': Array,
        'm_dot_salt_tot': Array,
        'T_htf_cold': Array,
        'T_salt_hot': Array,
        'q_startup': Array,
        'f_timestep': Array,
        'm_dot_steam': Array,
        'T_st_cold': Array,
        'T_st_hot': Array,
        'Q_dot_max': Array,
        'fuel_use': Array,
        'W_dot_pc_hybrid': Array,
        'W_dot_pc_fossil': Array,
        'W_dot_plant_hybrid': Array,
        'W_dot_plant_fossil': Array,
        'W_dot_plant_solar': Array,
        'eta_solar_use': Array,
        'eta_fuel': Array,
        'solar_fraction': Array,
        'W_dot_pump': Array,
        'pparasi': Array,
        'P_plant_balance_tot': Array,
        'P_fixed': Array,
        'annual_energy': float,
        'capacity_factor': float,
        'kwh_per_kw': float,
        'system_heat_rate': float,
        'annual_fuel_usage': float,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix,
        'gen': Array,
        'sf_adjust:constant': float,
        'sf_adjust:hourly': Array,
        'sf_adjust:periods': Matrix
}, total=False)

class Data(ssc.DataDict):
    solar_resource_file: str = INPUT(label='local weather file path', type='STRING', group='Weather', required='*', constraints='LOCAL_FILE')
    system_capacity: float = INPUT(label='Nameplate capacity', units='kW', type='NUMBER', group='molten salt tower', required='*')
    run_type: float = INPUT(label='Run type', units='-', type='NUMBER', group='heliostat', required='*')
    helio_width: float = INPUT(label='Heliostat width', units='m', type='NUMBER', group='heliostat', required='*')
    helio_height: float = INPUT(label='Heliostat height', units='m', type='NUMBER', group='heliostat', required='*')
    helio_optical_error: float = INPUT(label='Heliostat optical error', units='rad', type='NUMBER', group='heliostat', required='*')
    helio_active_fraction: float = INPUT(label='Heliostat active frac.', units='-', type='NUMBER', group='heliostat', required='*')
    dens_mirror: float = INPUT(label='Ratio of Reflective Area to Profile', units='-', type='NUMBER', group='heliostat', required='*')
    helio_reflectance: float = INPUT(label='Heliostat reflectance', units='-', type='NUMBER', group='heliostat', required='*')
    rec_absorptance: float = INPUT(label='Receiver absorptance', units='-', type='NUMBER', group='heliostat', required='*')
    rec_height: float = INPUT(label='Receiver height', units='m', type='NUMBER', group='heliostat', required='*')
    rec_aspect: float = INPUT(label='Receiver aspect ratio', units='-', type='NUMBER', group='heliostat', required='*')
    rec_hl_perm2: float = INPUT(label='Receiver design heatloss', units='kW/m2', type='NUMBER', group='heliostat', required='*')
    land_bound_type: float = INPUT(label='Land boundary type', units='-', type='NUMBER', group='heliostat', required='?=0')
    land_max: float = INPUT(label='Land max boundary', units='-ORm', type='NUMBER', group='heliostat', required='?=7.5')
    land_min: float = INPUT(label='Land min boundary', units='-ORm', type='NUMBER', group='heliostat', required='?=0.75')
    land_bound_table: Matrix = INPUT(label='Land boundary table', units='m', type='MATRIX', group='heliostat', required='?')
    land_bound_list: Array = INPUT(label='Boundary table listing', units='-', type='ARRAY', group='heliostat', required='?')
    dni_des: float = INPUT(label='Design-point DNI', units='W/m2', type='NUMBER', group='heliostat', required='*')
    p_start: float = INPUT(label='Heliostat startup energy', units='kWe-hr', type='NUMBER', group='heliostat', required='*')
    p_track: float = INPUT(label='Heliostat tracking energy', units='kWe', type='NUMBER', group='heliostat', required='*')
    hel_stow_deploy: float = INPUT(label='Stow/deploy elevation', units='deg', type='NUMBER', group='heliostat', required='*')
    v_wind_max: float = INPUT(label='Max. wind velocity', units='m/s', type='NUMBER', group='heliostat', required='*')
    interp_nug: float = INPUT(label='Interpolation nugget', units='-', type='NUMBER', group='heliostat', required='?=0')
    interp_beta: float = INPUT(label='Interpolation beta coef.', units='-', type='NUMBER', group='heliostat', required='?=1.99')
    n_flux_x: float = INPUT(label='Flux map X resolution', units='-', type='NUMBER', group='heliostat', required='?=12')
    n_flux_y: float = INPUT(label='Flux map Y resolution', units='-', type='NUMBER', group='heliostat', required='?=1')
    helio_positions: Matrix = INPUT(label='Heliostat position table', units='m', type='MATRIX', group='heliostat', required='run_type=1')
    helio_aim_points: Matrix = INPUT(label='Heliostat aim point table', units='m', type='MATRIX', group='heliostat', required='?')
    N_hel: float = INPUT(label='Number of heliostats', units='-', type='NUMBER', group='heliostat', required='?')
    eta_map: Matrix = INPUT(label='Field efficiency array', units='-', type='MATRIX', group='heliostat', required='?')
    flux_positions: Matrix = INPUT(label='Flux map sun positions', units='deg', type='MATRIX', group='heliostat', required='?')
    flux_maps: Matrix = INPUT(label='Flux map intensities', units='-', type='MATRIX', group='heliostat', required='?')
    c_atm_0: float = INPUT(label='Attenuation coefficient 0', type='NUMBER', group='heliostat', required='?=0.006789')
    c_atm_1: float = INPUT(label='Attenuation coefficient 1', type='NUMBER', group='heliostat', required='?=0.1046')
    c_atm_2: float = INPUT(label='Attenuation coefficient 2', type='NUMBER', group='heliostat', required='?=-0.0107')
    c_atm_3: float = INPUT(label='Attenuation coefficient 3', type='NUMBER', group='heliostat', required='?=0.002845')
    n_facet_x: float = INPUT(label='Number of heliostat facets - X', type='NUMBER', group='heliostat', required='*')
    n_facet_y: float = INPUT(label='Number of heliostat facets - Y', type='NUMBER', group='heliostat', required='*')
    focus_type: float = INPUT(label='Heliostat focus method', type='NUMBER', group='heliostat', required='*')
    cant_type: float = INPUT(label='Heliostat cant method', type='NUMBER', group='heliostat', required='*')
    n_flux_days: float = INPUT(label='No. days in flux map lookup', type='NUMBER', group='heliostat', required='?=8')
    delta_flux_hrs: float = INPUT(label='Hourly frequency in flux map lookup', type='NUMBER', group='heliostat', required='?=1')
    h_tower: float = INPUT(label='Tower height', units='m', type='NUMBER', group='heliostat', required='*')
    q_design: float = INPUT(label='Receiver thermal design power', units='MW', type='NUMBER', group='heliostat', required='*')
    calc_fluxmaps: float = INPUT(label='Include fluxmap calculations', type='NUMBER', group='heliostat', required='?=0')
    tower_fixed_cost: float = INPUT(label='Tower fixed cost', units='$', type='NUMBER', group='heliostat', required='*')
    tower_exp: float = INPUT(label='Tower cost scaling exponent', type='NUMBER', group='heliostat', required='*')
    rec_ref_cost: float = INPUT(label='Receiver reference cost', units='$', type='NUMBER', group='heliostat', required='*')
    rec_ref_area: float = INPUT(label='Receiver reference area for cost scale', type='NUMBER', group='heliostat', required='*')
    rec_cost_exp: float = INPUT(label='Receiver cost scaling exponent', type='NUMBER', group='heliostat', required='*')
    site_spec_cost: float = INPUT(label='Site improvement cost', units='$/m2', type='NUMBER', group='heliostat', required='*')
    heliostat_spec_cost: float = INPUT(label='Heliostat field cost', units='$/m2', type='NUMBER', group='heliostat', required='*')
    plant_spec_cost: float = INPUT(label='Power cycle specific cost', units='$/kWe', type='NUMBER', group='heliostat', required='*')
    bop_spec_cost: float = INPUT(label='BOS specific cost', units='$/kWe', type='NUMBER', group='heliostat', required='*')
    tes_spec_cost: float = INPUT(label='Thermal energy storage cost', units='$/kWht', type='NUMBER', group='heliostat', required='*')
    land_spec_cost: float = INPUT(label='Total land area cost', units='$/acre', type='NUMBER', group='heliostat', required='*')
    contingency_rate: float = INPUT(label='Contingency for cost overrun', units='%', type='NUMBER', group='heliostat', required='*')
    sales_tax_rate: float = INPUT(label='Sales tax rate', units='%', type='NUMBER', group='heliostat', required='*')
    sales_tax_frac: float = INPUT(label='Percent of cost to which sales tax applies', units='%', type='NUMBER', group='heliostat', required='*')
    cost_sf_fixed: float = INPUT(label='Solar field fixed cost', units='$', type='NUMBER', group='heliostat', required='*')
    fossil_spec_cost: float = INPUT(label='Fossil system specific cost', units='$/kWe', type='NUMBER', group='heliostat', required='*')
    is_optimize: float = INPUT(label='Do SolarPILOT optimization', type='NUMBER', group='heliostat', required='?=0')
    flux_max: float = INPUT(label='Maximum allowable flux', type='NUMBER', group='heliostat', required='?=1000')
    opt_init_step: float = INPUT(label='Optimization initial step size', type='NUMBER', group='heliostat', required='?=0.05')
    opt_max_iter: float = INPUT(label='Max. number iteration steps', type='NUMBER', group='heliostat', required='?=200')
    opt_conv_tol: float = INPUT(label='Optimization convergence tol', type='NUMBER', group='heliostat', required='?=0.001')
    opt_flux_penalty: float = INPUT(label='Optimization flux overage penalty', type='NUMBER', group='heliostat', required='*')
    opt_algorithm: float = INPUT(label='Optimization algorithm', type='NUMBER', group='heliostat', required='?=0')
    check_max_flux: float = INPUT(label='Check max flux at design point', type='NUMBER', group='heliostat', required='?=0')
    csp_pt_cost_epc_per_acre: float = INPUT(name='csp.pt.cost.epc.per_acre', label='EPC cost per acre', units='$/acre', type='NUMBER', group='heliostat', required='*')
    csp_pt_cost_epc_percent: float = INPUT(name='csp.pt.cost.epc.percent', label='EPC cost percent of direct', type='NUMBER', group='heliostat', required='*')
    csp_pt_cost_epc_per_watt: float = INPUT(name='csp.pt.cost.epc.per_watt', label='EPC cost per watt', units='$/W', type='NUMBER', group='heliostat', required='*')
    csp_pt_cost_epc_fixed: float = INPUT(name='csp.pt.cost.epc.fixed', label='EPC fixed', units='$', type='NUMBER', group='heliostat', required='*')
    csp_pt_cost_plm_per_acre: float = INPUT(name='csp.pt.cost.plm.per_acre', label='PLM cost per acre', units='$/acre', type='NUMBER', group='heliostat', required='*')
    csp_pt_cost_plm_percent: float = INPUT(name='csp.pt.cost.plm.percent', label='PLM cost percent of direct', type='NUMBER', group='heliostat', required='*')
    csp_pt_cost_plm_per_watt: float = INPUT(name='csp.pt.cost.plm.per_watt', label='PLM cost per watt', units='$/W', type='NUMBER', group='heliostat', required='*')
    csp_pt_cost_plm_fixed: float = INPUT(name='csp.pt.cost.plm.fixed', label='PLM fixed', units='$', type='NUMBER', group='heliostat', required='*')
    csp_pt_sf_fixed_land_area: float = INPUT(name='csp.pt.sf.fixed_land_area', label='Fixed land area', units='acre', type='NUMBER', group='heliostat', required='*')
    csp_pt_sf_land_overhead_factor: float = INPUT(name='csp.pt.sf.land_overhead_factor', label='Land overhead factor', type='NUMBER', group='heliostat', required='*')
    total_installed_cost: float = INPUT(label='Total installed cost', units='$', type='NUMBER', group='heliostat', required='*')
    receiver_type: float = INPUT(label='External=0, Cavity=1', type='NUMBER', group='receiver', required='*', constraints='INTEGER')
    N_panels: float = INPUT(label='Number of individual panels on the receiver', type='NUMBER', group='receiver', required='*', constraints='INTEGER')
    D_rec: float = INPUT(label='The overall outer diameter of the receiver', units='m', type='NUMBER', group='receiver', required='*')
    H_rec: float = INPUT(label='The height of the receiver', units='m', type='NUMBER', group='receiver', required='*')
    THT: float = INPUT(label='The height of the tower (hel. pivot to rec equator)', units='m', type='NUMBER', group='receiver', required='*')
    d_tube_out: float = INPUT(label='The outer diameter of an individual receiver tube', units='mm', type='NUMBER', group='receiver', required='*')
    th_tube: float = INPUT(label='The wall thickness of a single receiver tube', units='mm', type='NUMBER', group='receiver', required='*')
    mat_tube: float = INPUT(label='The material name of the receiver tubes', type='NUMBER', group='receiver', required='*')
    rec_htf: float = INPUT(label='The name of the HTF used in the receiver', type='NUMBER', group='receiver', required='*')
    field_fl_props: Matrix = INPUT(label='User defined field fluid property data', units='-', type='MATRIX', group='receiver', required='*')
    Flow_type: float = INPUT(label='A flag indicating which flow pattern is used', type='NUMBER', group='receiver', required='*')
    crossover_shift: float = INPUT(label='No. panels shift in receiver crossover position', type='NUMBER', group='receiver', required='?=0')
    epsilon: float = INPUT(label='The emissivity of the receiver surface coating', type='NUMBER', group='receiver', required='*')
    hl_ffact: float = INPUT(label='The heat loss factor (thermal loss fudge factor)', type='NUMBER', group='receiver', required='*')
    T_htf_hot_des: float = INPUT(label='Hot HTF outlet temperature at design conditions', units='C', type='NUMBER', group='receiver', required='*')
    T_htf_cold_des: float = INPUT(label='Cold HTF inlet temperature at design conditions', units='C', type='NUMBER', group='receiver', required='*')
    f_rec_min: float = INPUT(label='Minimum receiver mass flow rate turn down fraction', type='NUMBER', group='receiver', required='*')
    Q_rec_des: float = INPUT(label='Design-point receiver thermal power output', units='MWt', type='NUMBER', group='receiver', required='*')
    rec_su_delay: float = INPUT(label='Fixed startup delay time for the receiver', units='hr', type='NUMBER', group='receiver', required='*')
    rec_qf_delay: float = INPUT(label='Energy-based rcvr startup delay (fraction of rated thermal power)', type='NUMBER', group='receiver', required='*')
    m_dot_htf_max: float = INPUT(label='Maximum receiver mass flow rate', units='kg/hr', type='NUMBER', group='receiver', required='*')
    A_sf: float = INPUT(label='Solar Field Area', units='m^2', type='NUMBER', group='receiver', required='*')
    eta_pump: float = INPUT(label='Receiver HTF pump efficiency', type='NUMBER', group='receiver', required='*')
    q_pb_design: float = INPUT(label='Design point power block thermal power', units='MWt', type='NUMBER', group='powerblock', required='*')
    elev: float = INPUT(label='Plant elevation', units='m', type='NUMBER', group='powerblock', required='*')
    ngcc_model: float = INPUT(label='1: NREL, 2: GE', type='NUMBER', group='powerblock', required='*')
    pinch_point_hotside: float = INPUT(label='Hot side temperature HX temperature difference', units='C', type='NUMBER', group='powerblock', required='*')
    pinch_point_coldside: float = INPUT(label='Cold side HX pinch point', units='C', type='NUMBER', group='powerblock', required='*')
    pb_pump_coef: float = INPUT(label='Required pumping power for HTF through power block', units='kJ/kg', type='NUMBER', group='parasitics', required='*')
    piping_loss: float = INPUT(label='Thermal loss per meter of piping', units='Wt/m', type='NUMBER', group='parasitics', required='*')
    piping_length: float = INPUT(label='Total length of exposed piping', units='m', type='NUMBER', group='parasitics', required='*')
    piping_length_mult: float = INPUT(label='Piping length multiplier', type='NUMBER', group='parasitics', required='*')
    piping_length_const: float = INPUT(label='Piping constant length', units='m', type='NUMBER', group='parasitics', required='*')
    pb_fixed_par: float = INPUT(label='Fixed parasitic load - runs at all times', units='MWe/MWcap', type='NUMBER', group='parasitics', required='*')
    bop_par: float = INPUT(label='Balance of plant parasitic power fraction', units='MWe/MWcap', type='NUMBER', group='parasitics', required='*')
    bop_par_f: float = INPUT(label='Balance of plant parasitic power fraction - mult frac', units='none', type='NUMBER', group='parasitics', required='*')
    bop_par_0: float = INPUT(label='Balance of plant parasitic power fraction - const coeff', units='none', type='NUMBER', group='parasitics', required='*')
    bop_par_1: float = INPUT(label='Balance of plant parasitic power fraction - linear coeff', units='none', type='NUMBER', group='parasitics', required='*')
    bop_par_2: float = INPUT(label='Balance of plant parasitic power fraction - quadratic coeff', units='none', type='NUMBER', group='parasitics', required='*')
    fossil_output: float = INPUT(label='Fossil-only cycle output at design', units='MWe', type='NUMBER', group='parasitics', required='*')
    W_dot_solar_des: float = INPUT(label='Solar contribution to cycle output at designMWe', type='NUMBER', group='*', meta='parasitics')
    month: Final[Array] = OUTPUT(label='Resource Month', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    hour: Final[Array] = OUTPUT(label='Resource Hour of Day', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    solazi: Final[Array] = OUTPUT(label='Resource Solar Azimuth', units='deg', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    solzen: Final[Array] = OUTPUT(label='Resource Solar Zenith', units='deg', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    beam: Final[Array] = OUTPUT(label='Resource Beam normal irradiance', units='W/m2', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    tdry: Final[Array] = OUTPUT(label='Resource Dry bulb temperature', units='C', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    twet: Final[Array] = OUTPUT(label='Resource Wet bulb temperature', units='C', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    wspd: Final[Array] = OUTPUT(label='Resource Wind Speed', units='m/s', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    pres: Final[Array] = OUTPUT(label='Resource Pressure', units='mbar', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    eta_field: Final[Array] = OUTPUT(label='Field optical efficiency', type='ARRAY', group='Outputs', required='*')
    field_eff_adj: Final[Array] = OUTPUT(label='Solar field efficiency w/ defocusing', type='ARRAY', group='Outputs', required='*')
    eta_therm: Final[Array] = OUTPUT(label='Receiver thermal efficiency', type='ARRAY', group='Outputs', required='*')
    Q_solar_total: Final[Array] = OUTPUT(label='Receiver thermal power absorbed', units='MWt', type='ARRAY', group='Outputs', required='*')
    q_conv_sum: Final[Array] = OUTPUT(label='Receiver thermal power loss to convection', units='MWt', type='ARRAY', group='Outputs', required='*')
    q_rad_sum: Final[Array] = OUTPUT(label='Receiver thermal power loss to radiation', units='MWt', type='ARRAY', group='Outputs', required='*')
    Q_thermal: Final[Array] = OUTPUT(label='Receiver thermal power to HTF', units='MWt', type='ARRAY', group='Outputs', required='*')
    m_dot_ss: Final[Array] = OUTPUT(label='Receiver mass flow rate, steady state', units='kg/s', type='ARRAY', group='Outputs', required='*')
    m_dot_salt_tot: Final[Array] = OUTPUT(label='Receiver mass flow rate, derated for startup', units='kg/s', type='ARRAY', group='Outputs', required='*')
    T_htf_cold: Final[Array] = OUTPUT(label='Receiver HTF temperature in', units='C', type='ARRAY', group='Outputs', required='*')
    T_salt_hot: Final[Array] = OUTPUT(label='Receiver HTF temperature out', units='C', type='ARRAY', group='Outputs', required='*')
    q_startup: Final[Array] = OUTPUT(label='Receiver startup power', units='MWt', type='ARRAY', group='Outputs', required='*')
    f_timestep: Final[Array] = OUTPUT(label='Receiver operating fraction after startup', type='ARRAY', group='Outputs', required='*')
    m_dot_steam: Final[Array] = OUTPUT(label='Cycle solar steam mass flow rate', units='kg/hr', type='ARRAY', group='Outputs', required='*')
    T_st_cold: Final[Array] = OUTPUT(label='Cycle steam temp from NGCC to HX', units='C', type='ARRAY', group='Outputs', required='*')
    T_st_hot: Final[Array] = OUTPUT(label='Cycle steam temp from HX back to NGCC', units='C', type='ARRAY', group='Outputs', required='*')
    Q_dot_max: Final[Array] = OUTPUT(label='Cycle max allowable thermal power to NGCC', units='MWt', type='ARRAY', group='Outputs', required='*')
    fuel_use: Final[Array] = OUTPUT(label='Cycle natural gas used during timestep', units='MMBTU', type='ARRAY', group='Outputs', required='*')
    W_dot_pc_hybrid: Final[Array] = OUTPUT(label='Cycle net output including solar power', units='MWe', type='ARRAY', group='Outputs', required='*')
    W_dot_pc_fossil: Final[Array] = OUTPUT(label='Cycle net output only considering fossil power', units='MWe', type='ARRAY', group='Outputs', required='*')
    W_dot_plant_hybrid: Final[Array] = OUTPUT(label='Plant net output including solar power & parasitics', units='MWe', type='ARRAY', group='Outputs', required='*')
    W_dot_plant_fossil: Final[Array] = OUTPUT(label='Plant net output only considering fossil power & parasitics', units='MWe', type='ARRAY', group='Outputs', required='*')
    W_dot_plant_solar: Final[Array] = OUTPUT(label='Plant net output attributable to solar', units='MWe', type='ARRAY', group='Outputs', required='*')
    eta_solar_use: Final[Array] = OUTPUT(label='Plant solar use efficiency considering parasitics', units='-', type='ARRAY', group='Outputs', required='*')
    eta_fuel: Final[Array] = OUTPUT(label='Plant efficiency of fossil only operation (LHV basis)', units='%', type='ARRAY', group='Outputs', required='*')
    solar_fraction: Final[Array] = OUTPUT(label='Plant solar fraction', units='-', type='ARRAY', group='Outputs', required='*')
    W_dot_pump: Final[Array] = OUTPUT(label='Parasitic power receiver HTF pump', units='MWe', type='ARRAY', group='Outputs', required='*')
    pparasi: Final[Array] = OUTPUT(label='Parasitic power heliostat drives', units='MWe', type='ARRAY', group='Outputs', required='*')
    P_plant_balance_tot: Final[Array] = OUTPUT(label='Parasitic power generation-dependent load', units='MWe', type='ARRAY', group='Outputs', required='*')
    P_fixed: Final[Array] = OUTPUT(label='Parasitic power fixed load', units='MWe', type='ARRAY', group='Outputs', required='*')
    annual_energy: Final[float] = OUTPUT(label='Annual Energy', units='kW', type='NUMBER', group='Net_E_Calc', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', required='*')
    kwh_per_kw: Final[float] = OUTPUT(label='First year kWh/kW', units='kWh/kW', type='NUMBER', required='*')
    system_heat_rate: Final[float] = OUTPUT(label='System heat rate', units='MMBtu/MWh', type='NUMBER', required='*')
    annual_fuel_usage: Final[float] = OUTPUT(label='Annual fuel usage', units='kWh', type='NUMBER', required='*')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    gen: Final[Array] = OUTPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')
    sf_adjust_constant: float = INPUT(name='sf_adjust:constant', label='SF Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    sf_adjust_hourly: Array = INPUT(name='sf_adjust:hourly', label='SF Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    sf_adjust_periods: Matrix = INPUT(name='sf_adjust:periods', label='SF Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')

    def __init__(self, *args: Mapping[str, Any],
                 solar_resource_file: str = ...,
                 system_capacity: float = ...,
                 run_type: float = ...,
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
                 land_bound_type: float = ...,
                 land_max: float = ...,
                 land_min: float = ...,
                 land_bound_table: Matrix = ...,
                 land_bound_list: Array = ...,
                 dni_des: float = ...,
                 p_start: float = ...,
                 p_track: float = ...,
                 hel_stow_deploy: float = ...,
                 v_wind_max: float = ...,
                 interp_nug: float = ...,
                 interp_beta: float = ...,
                 n_flux_x: float = ...,
                 n_flux_y: float = ...,
                 helio_positions: Matrix = ...,
                 helio_aim_points: Matrix = ...,
                 N_hel: float = ...,
                 eta_map: Matrix = ...,
                 flux_positions: Matrix = ...,
                 flux_maps: Matrix = ...,
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
                 h_tower: float = ...,
                 q_design: float = ...,
                 calc_fluxmaps: float = ...,
                 tower_fixed_cost: float = ...,
                 tower_exp: float = ...,
                 rec_ref_cost: float = ...,
                 rec_ref_area: float = ...,
                 rec_cost_exp: float = ...,
                 site_spec_cost: float = ...,
                 heliostat_spec_cost: float = ...,
                 plant_spec_cost: float = ...,
                 bop_spec_cost: float = ...,
                 tes_spec_cost: float = ...,
                 land_spec_cost: float = ...,
                 contingency_rate: float = ...,
                 sales_tax_rate: float = ...,
                 sales_tax_frac: float = ...,
                 cost_sf_fixed: float = ...,
                 fossil_spec_cost: float = ...,
                 is_optimize: float = ...,
                 flux_max: float = ...,
                 opt_init_step: float = ...,
                 opt_max_iter: float = ...,
                 opt_conv_tol: float = ...,
                 opt_flux_penalty: float = ...,
                 opt_algorithm: float = ...,
                 check_max_flux: float = ...,
                 csp_pt_cost_epc_per_acre: float = ...,
                 csp_pt_cost_epc_percent: float = ...,
                 csp_pt_cost_epc_per_watt: float = ...,
                 csp_pt_cost_epc_fixed: float = ...,
                 csp_pt_cost_plm_per_acre: float = ...,
                 csp_pt_cost_plm_percent: float = ...,
                 csp_pt_cost_plm_per_watt: float = ...,
                 csp_pt_cost_plm_fixed: float = ...,
                 csp_pt_sf_fixed_land_area: float = ...,
                 csp_pt_sf_land_overhead_factor: float = ...,
                 total_installed_cost: float = ...,
                 receiver_type: float = ...,
                 N_panels: float = ...,
                 D_rec: float = ...,
                 H_rec: float = ...,
                 THT: float = ...,
                 d_tube_out: float = ...,
                 th_tube: float = ...,
                 mat_tube: float = ...,
                 rec_htf: float = ...,
                 field_fl_props: Matrix = ...,
                 Flow_type: float = ...,
                 crossover_shift: float = ...,
                 epsilon: float = ...,
                 hl_ffact: float = ...,
                 T_htf_hot_des: float = ...,
                 T_htf_cold_des: float = ...,
                 f_rec_min: float = ...,
                 Q_rec_des: float = ...,
                 rec_su_delay: float = ...,
                 rec_qf_delay: float = ...,
                 m_dot_htf_max: float = ...,
                 A_sf: float = ...,
                 eta_pump: float = ...,
                 q_pb_design: float = ...,
                 elev: float = ...,
                 ngcc_model: float = ...,
                 pinch_point_hotside: float = ...,
                 pinch_point_coldside: float = ...,
                 pb_pump_coef: float = ...,
                 piping_loss: float = ...,
                 piping_length: float = ...,
                 piping_length_mult: float = ...,
                 piping_length_const: float = ...,
                 pb_fixed_par: float = ...,
                 bop_par: float = ...,
                 bop_par_f: float = ...,
                 bop_par_0: float = ...,
                 bop_par_1: float = ...,
                 bop_par_2: float = ...,
                 fossil_output: float = ...,
                 W_dot_solar_des: float = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...,
                 sf_adjust_constant: float = ...,
                 sf_adjust_hourly: Array = ...,
                 sf_adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
