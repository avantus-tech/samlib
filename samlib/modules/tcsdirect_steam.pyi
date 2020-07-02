
# This is a generated file

"""tcsdirect_steam - CSP model using the direct steam power tower TCS types."""

# VERSION: 4

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'solar_resource_file': str,
        'system_capacity': float,
        'weekday_schedule': Matrix,
        'weekend_schedule': Matrix,
        'run_type': float,
        'helio_width': float,
        'helio_height': float,
        'helio_optical_error': float,
        'helio_active_fraction': float,
        'helio_reflectance': float,
        'rec_absorptance': float,
        'rec_aspect': float,
        'rec_height': float,
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
        'dens_mirror': float,
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
        'water_usage_per_wash': float,
        'washing_frequency': float,
        'H_rec': float,
        'THT': float,
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
        'fossil_mode': float,
        'q_pb_design': float,
        'q_aux_max': float,
        'lhv_eff': float,
        'h_tower': float,
        'n_panels': float,
        'flowtype': float,
        'd_rec': float,
        'q_rec_des': float,
        'f_rec_min': float,
        'rec_qf_delay': float,
        'rec_su_delay': float,
        'f_pb_cutoff': float,
        'f_pb_sb': float,
        't_standby_ini': float,
        'x_b_target': float,
        'eta_rec_pump': float,
        'P_hp_in_des': float,
        'P_hp_out_des': float,
        'f_mdotrh_des': float,
        'p_cycle_design': float,
        'ct': float,
        'T_amb_des': float,
        'dT_cw_ref': float,
        'T_approach': float,
        'T_ITD_des': float,
        'hl_ffact': float,
        'h_boiler': float,
        'd_t_boiler': float,
        'th_t_boiler': float,
        'rec_emis': float,
        'mat_boiler': float,
        'h_sh': float,
        'd_sh': float,
        'th_sh': float,
        'mat_sh': float,
        'T_sh_out_des': float,
        'h_rh': float,
        'd_rh': float,
        'th_rh': float,
        'mat_rh': float,
        'T_rh_out_des': float,
        'cycle_max_frac': float,
        'A_sf': float,
        'ffrac': Array,
        'P_b_in_init': float,
        'f_mdot_rh_init': float,
        'P_hp_out': float,
        'T_hp_out': float,
        'T_rh_target': float,
        'T_fw_init': float,
        'P_cond_init': float,
        'P_ref': float,
        'eta_ref': float,
        'T_hot_ref': float,
        'T_cold_ref': float,
        'q_sby_frac': float,
        'P_boil_des': float,
        'P_rh_ref': float,
        'rh_frac_ref': float,
        'startup_time': float,
        'startup_frac': float,
        'P_cond_ratio': float,
        'pb_bd_frac': float,
        'P_cond_min': float,
        'n_pl_inc': float,
        'F_wc': Array,
        'T_hot': float,
        'Piping_loss': float,
        'Piping_length': float,
        'piping_length_mult': float,
        'piping_length_add': float,
        'Design_power': float,
        'design_eff': float,
        'pb_fixed_par': float,
        'aux_par': float,
        'aux_par_f': float,
        'aux_par_0': float,
        'aux_par_1': float,
        'aux_par_2': float,
        'bop_par': float,
        'bop_par_f': float,
        'bop_par_0': float,
        'bop_par_1': float,
        'bop_par_2': float,
        'month': Array,
        'hour': Array,
        'solazi': Array,
        'solzen': Array,
        'beam': Array,
        'tdry': Array,
        'twet': Array,
        'wspd': Array,
        'pres': Array,
        'tou_value': Array,
        'eta_field': Array,
        'defocus': Array,
        'q_b_conv': Array,
        'q_b_rad': Array,
        'q_b_abs': Array,
        'P_b_in': Array,
        'P_b_out': Array,
        'P_drop_b': Array,
        'eta_b': Array,
        'T_b_in': Array,
        'T_boiling': Array,
        'T_max_b_surf': Array,
        'm_dot_sh': Array,
        'q_sh_conv': Array,
        'q_sh_rad': Array,
        'q_sh_abs': Array,
        'P_sh_out': Array,
        'dP_sh': Array,
        'T_max_sh_surf': Array,
        'eta_sh': Array,
        'v_sh_max': Array,
        'f_mdot_rh': Array,
        'q_rh_conv': Array,
        'q_rh_rad': Array,
        'q_rh_abs': Array,
        'P_rh_in': Array,
        'P_rh_out': Array,
        'dP_rh': Array,
        'eta_rh': Array,
        'T_rh_in': Array,
        'T_rh_out': Array,
        'T_max_rh_surf': Array,
        'v_rh_max': Array,
        'q_inc_full': Array,
        'q_abs_rec': Array,
        'q_rad_rec': Array,
        'q_conv_rec': Array,
        'q_therm_in_rec': Array,
        'eta_rec': Array,
        'm_dot_aux': Array,
        'q_aux': Array,
        'q_aux_fuel': Array,
        'P_out_net': Array,
        'P_cycle': Array,
        'T_fw': Array,
        'm_dot_makeup': Array,
        'P_cond': Array,
        'f_bays': Array,
        'W_dot_boost': Array,
        'pparasi': Array,
        'P_plant_balance_tot': Array,
        'P_fixed': Array,
        'P_cooling_tower_tot': Array,
        'P_piping_tot': Array,
        'P_parasitics': Array,
        'annual_energy': float,
        'annual_W_cycle_gross': float,
        'annual_total_water_use': float,
        'conversion_factor': float,
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
    system_capacity: float = INPUT(label='Nameplate capacity', units='kW', type='NUMBER', group='direct steam tower', required='*')
    weekday_schedule: Matrix = INPUT(label='12x24 Time of Use Values for week days', type='MATRIX', group='tou_translator', required='*')
    weekend_schedule: Matrix = INPUT(label='12x24 Time of Use Values for week end days', type='MATRIX', group='tou_translator', required='*')
    run_type: float = INPUT(label='Run type', units='-', type='NUMBER', group='heliostat', required='*')
    helio_width: float = INPUT(label='Heliostat width', units='m', type='NUMBER', group='heliostat', required='*')
    helio_height: float = INPUT(label='Heliostat height', units='m', type='NUMBER', group='heliostat', required='*')
    helio_optical_error: float = INPUT(label='Heliostat optical error', units='rad', type='NUMBER', group='heliostat', required='*')
    helio_active_fraction: float = INPUT(label='Heliostat active frac.', type='NUMBER', group='heliostat', required='*')
    helio_reflectance: float = INPUT(label='Heliostat reflectance', type='NUMBER', group='heliostat', required='*')
    rec_absorptance: float = INPUT(label='Receiver absorptance', type='NUMBER', group='heliostat', required='*')
    rec_aspect: float = INPUT(label='Receiver aspect ratio', type='NUMBER', group='heliostat', required='*')
    rec_height: float = INPUT(label='Receiver height', units='m', type='NUMBER', group='heliostat', required='*')
    rec_hl_perm2: float = INPUT(label='Receiver design heatloss', units='kW/m2', type='NUMBER', group='heliostat', required='*')
    land_bound_type: float = INPUT(label='Land boundary type', type='NUMBER', group='heliostat', required='?=0')
    land_max: float = INPUT(label='Land max boundary', units='-ORm', type='NUMBER', group='heliostat', required='?=7.5')
    land_min: float = INPUT(label='Land min boundary', units='-ORm', type='NUMBER', group='heliostat', required='?=0.75')
    land_bound_table: Matrix = INPUT(label='Land boundary table', units='m', type='MATRIX', group='heliostat', required='?')
    land_bound_list: Array = INPUT(label='Boundary table listing', type='ARRAY', group='heliostat', required='?')
    dni_des: float = INPUT(label='Design-point DNI', units='W/m2', type='NUMBER', group='heliostat', required='*')
    p_start: float = INPUT(label='Heliostat startup energy', units='kWe-hr', type='NUMBER', group='heliostat', required='*')
    p_track: float = INPUT(label='Heliostat tracking energy', units='kWe', type='NUMBER', group='heliostat', required='*')
    hel_stow_deploy: float = INPUT(label='Stow/deploy elevation', units='deg', type='NUMBER', group='heliostat', required='*')
    v_wind_max: float = INPUT(label='Max. wind velocity', units='m/s', type='NUMBER', group='heliostat', required='*')
    interp_nug: float = INPUT(label='Interpolation nugget', type='NUMBER', group='heliostat', required='?=0')
    interp_beta: float = INPUT(label='Interpolation beta coef.', type='NUMBER', group='heliostat', required='?=1.99')
    n_flux_x: float = INPUT(label='Flux map X resolution', type='NUMBER', group='heliostat', required='?=12')
    n_flux_y: float = INPUT(label='Flux map Y resolution', type='NUMBER', group='heliostat', required='?=1')
    dens_mirror: float = INPUT(label='Ratio of reflective area to profile', type='NUMBER', group='heliostat', required='*')
    helio_positions: Matrix = INPUT(label='Heliostat position table', units='m', type='MATRIX', group='heliostat', required='run_type=1')
    helio_aim_points: Matrix = INPUT(label='Heliostat aim point table', units='m', type='MATRIX', group='heliostat', required='?')
    N_hel: float = INPUT(label='Number of heliostats', type='NUMBER', group='heliostat', required='?')
    eta_map: Matrix = INPUT(label='Field efficiency array', type='MATRIX', group='heliostat', required='?')
    flux_positions: Matrix = INPUT(label='Flux map sun positions', units='deg', type='MATRIX', group='heliostat', required='?')
    flux_maps: Matrix = INPUT(label='Flux map intensities', type='MATRIX', group='heliostat', required='?')
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
    water_usage_per_wash: float = INPUT(label='Water usage per wash', units='L/m2_aper', type='NUMBER', group='heliostat', required='*')
    washing_frequency: float = INPUT(label='Mirror washing frequency', type='NUMBER', group='heliostat', required='*')
    H_rec: float = INPUT(label='The height of the receiver', units='m', type='NUMBER', group='receiver', required='*')
    THT: float = INPUT(label='The height of the tower (hel. pivot to rec equator)', units='m', type='NUMBER', group='receiver', required='*')
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
    fossil_mode: float = INPUT(label='Fossil model: 1=Normal, 2=Supplemental', units='-', type='NUMBER', group='dsg_controller', required='*', constraints='INTEGER')
    q_pb_design: float = INPUT(label='Heat rate into powerblock at design', units='MW', type='NUMBER', group='dsg_controller', required='*')
    q_aux_max: float = INPUT(label='Maximum heat rate of auxiliary heater', units='MW', type='NUMBER', group='dsg_controller', required='*')
    lhv_eff: float = INPUT(label='Aux Heater lower heating value efficiency', units='-', type='NUMBER', group='dsg_controller', required='*')
    h_tower: float = INPUT(label='Tower Height', units='m', type='NUMBER', group='dsg_controller', required='*')
    n_panels: float = INPUT(label='Number of panels', units='-', type='NUMBER', group='dsg_controller', required='*')
    flowtype: float = INPUT(label='Code for flow pattern through rec.', units='-', type='NUMBER', group='dsg_controller', required='*', constraints='INTEGER')
    d_rec: float = INPUT(label='Diameter of Receiver', units='m', type='NUMBER', group='dsg_controller', required='*')
    q_rec_des: float = INPUT(label='Design-point thermal power', units='MW', type='NUMBER', group='dsg_controller', required='*')
    f_rec_min: float = INPUT(label='Minimum receiver absorbed power fraction', units='-', type='NUMBER', group='dsg_controller', required='*')
    rec_qf_delay: float = INPUT(label='Receiver start-up delay fraction of thermal energy of receiver running at design for 1 hour', units='-', type='NUMBER', group='dsg_controller', required='*')
    rec_su_delay: float = INPUT(label='Receiver start-up delay time', units='hr', type='NUMBER', group='dsg_controller', required='*')
    f_pb_cutoff: float = INPUT(label='Cycle cut-off fraction', units='-', type='NUMBER', group='dsg_controller', required='*')
    f_pb_sb: float = INPUT(label='Cycle minimum standby fraction', units='-', type='NUMBER', group='dsg_controller', required='*')
    t_standby_ini: float = INPUT(label='Power block standby time', units='hr', type='NUMBER', group='dsg_controller', required='*')
    x_b_target: float = INPUT(label='Target boiler outlet quality', units='-', type='NUMBER', group='dsg_controller', required='*')
    eta_rec_pump: float = INPUT(label='Feedwater pump efficiency', units='-', type='NUMBER', group='dsg_controller', required='*')
    P_hp_in_des: float = INPUT(label='Design HP Turbine Inlet Pressure', units='bar', type='NUMBER', group='dsg_controller', required='*')
    P_hp_out_des: float = INPUT(label='Design HP Turbine Outlet Pressure', units='bar', type='NUMBER', group='dsg_controller', required='*')
    f_mdotrh_des: float = INPUT(label='Design reheat mass flow rate fraction', units='-', type='NUMBER', group='dsg_controller', required='*')
    p_cycle_design: float = INPUT(label='Design Cycle Power', units='MW', type='NUMBER', group='dsg_controller', required='*')
    ct: float = INPUT(label='Cooling Type', units='-', type='NUMBER', group='dsg_controller', required='*', constraints='INTEGER')
    T_amb_des: float = INPUT(label='Design ambient temperature (power cycle)', units='C', type='NUMBER', group='dsg_controller', required='*')
    dT_cw_ref: float = INPUT(label='Reference condenser water dT', units='C', type='NUMBER', group='dsg_controller', required='*')
    T_approach: float = INPUT(label='Approach temperature for wet cooling', units='C', type='NUMBER', group='dsg_controller', required='*')
    T_ITD_des: float = INPUT(label='Approach temperature for dry cooling', units='C', type='NUMBER', group='dsg_controller', required='*')
    hl_ffact: float = INPUT(label='Heat Loss Fudge FACTor', units='-', type='NUMBER', group='dsg_controller', required='*')
    h_boiler: float = INPUT(label='Height of boiler', units='m', type='NUMBER', group='dsg_controller', required='*')
    d_t_boiler: float = INPUT(label='O.D. of boiler tubes', units='m', type='NUMBER', group='dsg_controller', required='*')
    th_t_boiler: float = INPUT(label='Thickness of boiler tubes', units='m', type='NUMBER', group='dsg_controller', required='*')
    rec_emis: float = INPUT(label='Emissivity of receiver tubes', units='-', type='NUMBER', group='dsg_controller', required='*')
    mat_boiler: float = INPUT(label='Numerical code for tube material', units='-', type='NUMBER', group='dsg_controller', required='*', constraints='INTEGER')
    h_sh: float = INPUT(label='Height of superheater', units='m', type='NUMBER', group='dsg_controller', required='*')
    d_sh: float = INPUT(label='O.D. of superheater tubes', units='m', type='NUMBER', group='dsg_controller', required='*')
    th_sh: float = INPUT(label='Thickness of superheater tubes', units='m', type='NUMBER', group='dsg_controller', required='*')
    mat_sh: float = INPUT(label='Numerical code for superheater material', units='-', type='NUMBER', group='dsg_controller', required='*', constraints='INTEGER')
    T_sh_out_des: float = INPUT(label='Target superheater outlet temperature', units='C', type='NUMBER', group='dsg_controller', required='*')
    h_rh: float = INPUT(label='Height of reheater', units='m', type='NUMBER', group='dsg_controller', required='*')
    d_rh: float = INPUT(label='O.D. of reheater tubes', units='m', type='NUMBER', group='dsg_controller', required='*')
    th_rh: float = INPUT(label='Thickness of reheater tubes', units='m', type='NUMBER', group='dsg_controller', required='*')
    mat_rh: float = INPUT(label='Numerical code for reheater material', units='-', type='NUMBER', group='dsg_controller', required='*', constraints='INTEGER')
    T_rh_out_des: float = INPUT(label='Target reheater outlet temperature', units='C', type='NUMBER', group='dsg_controller', required='*')
    cycle_max_frac: float = INPUT(label='Cycle maximum overdesign fraction', units='-', type='NUMBER', group='dsg_controller', required='*')
    A_sf: float = INPUT(label='Solar field area', units='m^2', type='NUMBER', group='dsg_controller', required='*')
    ffrac: Array = INPUT(label='Fossil dispatch logic', units='-', type='ARRAY', group='dsg_controller', required='*')
    P_b_in_init: float = INPUT(label='Initial Boiler inlet pressure', units='bar', type='NUMBER', group='dsg_controller', required='*')
    f_mdot_rh_init: float = INPUT(label='Reheat mass flow rate fraction', units='-', type='NUMBER', group='dsg_controller', required='*')
    P_hp_out: float = INPUT(label='HP turbine outlet pressure', units='bar', type='NUMBER', group='dsg_controller', required='*')
    T_hp_out: float = INPUT(label='HP turbine outlet temperature', units='C', type='NUMBER', group='dsg_controller', required='*')
    T_rh_target: float = INPUT(label='Target reheater outlet temp.', units='C', type='NUMBER', group='dsg_controller', required='*')
    T_fw_init: float = INPUT(label='Initial Feedwater outlet temperature', units='C', type='NUMBER', group='dsg_controller', required='*')
    P_cond_init: float = INPUT(label='Condenser pressure', units='Pa', type='NUMBER', group='dsg_controller', required='*')
    P_ref: float = INPUT(label='Reference output electric power at design condition', units='MW', type='NUMBER', group='powerblock', required='*')
    eta_ref: float = INPUT(label='Reference conversion efficiency at design condition', units='none', type='NUMBER', group='powerblock', required='*')
    T_hot_ref: float = INPUT(label='Reference HTF inlet temperature at design', units='C', type='NUMBER', group='powerblock', required='*')
    T_cold_ref: float = INPUT(label='Reference HTF outlet temperature at design', units='C', type='NUMBER', group='powerblock', required='*')
    q_sby_frac: float = INPUT(label='Fraction of thermal power required for standby mode', units='none', type='NUMBER', group='powerblock', required='*')
    P_boil_des: float = INPUT(label='Boiler operating pressure @ design', units='bar', type='NUMBER', group='powerblock', required='*')
    P_rh_ref: float = INPUT(label='Reheater operating pressure at design', units='bar', type='NUMBER', group='powerblock', required='*')
    rh_frac_ref: float = INPUT(label='Reheater flow fraction at design', units='none', type='NUMBER', group='powerblock', required='*')
    startup_time: float = INPUT(label='Time needed for power block startup', units='hr', type='NUMBER', group='powerblock', required='*')
    startup_frac: float = INPUT(label='Fraction of design thermal power needed for startup', units='none', type='NUMBER', group='powerblock', required='*')
    P_cond_ratio: float = INPUT(label='Condenser pressure ratio', units='none', type='NUMBER', group='powerblock', required='*')
    pb_bd_frac: float = INPUT(label='Power block blowdown steam fraction ', units='none', type='NUMBER', group='powerblock', required='*')
    P_cond_min: float = INPUT(label='Minimum condenser pressure', units='inHg', type='NUMBER', group='powerblock', required='*')
    n_pl_inc: float = INPUT(label='Number of part-load increments for the heat rejection system', units='none', type='NUMBER', group='powerblock', required='*', constraints='INTEGER')
    F_wc: Array = INPUT(label='Fraction indicating wet cooling use for hybrid system', units='none', type='ARRAY', group='powerblock', required='*')
    T_hot: float = INPUT(label='Hot HTF inlet temperature, from storage tank', units='C', type='NUMBER', group='powerblock', required='*')
    Piping_loss: float = INPUT(label='Thermal loss per meter of piping', units='Wt/m', type='NUMBER', group='parasitics', required='*')
    Piping_length: float = INPUT(label='Total length of exposed piping', units='m', type='NUMBER', group='parasitics', required='*')
    piping_length_mult: float = INPUT(label='Piping length multiplier', type='NUMBER', group='parasitics', required='*')
    piping_length_add: float = INPUT(label='Piping constant length', units='m', type='NUMBER', group='parasitics', required='*')
    Design_power: float = INPUT(label='Power production at design conditions', units='MWe', type='NUMBER', group='parasitics', required='*')
    design_eff: float = INPUT(label='Power cycle efficiency at design', units='none', type='NUMBER', group='parasitics', required='*')
    pb_fixed_par: float = INPUT(label='Fixed parasitic load - runs at all times', units='MWe/MWcap', type='NUMBER', group='parasitics', required='*')
    aux_par: float = INPUT(label='Aux heater, boiler parasitic', units='MWe/MWcap', type='NUMBER', group='parasitics', required='*')
    aux_par_f: float = INPUT(label='Aux heater, boiler parasitic - multiplying fraction', units='none', type='NUMBER', group='parasitics', required='*')
    aux_par_0: float = INPUT(label='Aux heater, boiler parasitic - constant coefficient', units='none', type='NUMBER', group='parasitics', required='*')
    aux_par_1: float = INPUT(label='Aux heater, boiler parasitic - linear coefficient', units='none', type='NUMBER', group='parasitics', required='*')
    aux_par_2: float = INPUT(label='Aux heater, boiler parasitic - quadratic coefficient', units='none', type='NUMBER', group='parasitics', required='*')
    bop_par: float = INPUT(label='Balance of plant parasitic power fraction', units='MWe/MWcap', type='NUMBER', group='parasitics', required='*')
    bop_par_f: float = INPUT(label='Balance of plant parasitic power fraction - mult frac', units='none', type='NUMBER', group='parasitics', required='*')
    bop_par_0: float = INPUT(label='Balance of plant parasitic power fraction - const coeff', units='none', type='NUMBER', group='parasitics', required='*')
    bop_par_1: float = INPUT(label='Balance of plant parasitic power fraction - linear coeff', units='none', type='NUMBER', group='parasitics', required='*')
    bop_par_2: float = INPUT(label='Balance of plant parasitic power fraction - quadratic coeff', units='none', type='NUMBER', group='parasitics', required='*')
    month: Final[Array] = OUTPUT(label='Resource Month', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    hour: Final[Array] = OUTPUT(label='Resource Hour of Day', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    solazi: Final[Array] = OUTPUT(label='Resource Solar Azimuth', units='deg', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    solzen: Final[Array] = OUTPUT(label='Resource Solar Zenith', units='deg', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    beam: Final[Array] = OUTPUT(label='Resource Beam normal irradiance', units='W/m2', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    tdry: Final[Array] = OUTPUT(label='Resource Dry bulb temperature', units='C', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    twet: Final[Array] = OUTPUT(label='Resource Wet bulb temperature', units='C', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    wspd: Final[Array] = OUTPUT(label='Resource Wind Speed', units='m/s', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    pres: Final[Array] = OUTPUT(label='Resource Pressure', units='mbar', type='ARRAY', group='weather', required='*', constraints='LENGTH=8760')
    tou_value: Final[Array] = OUTPUT(label='Resource Time-of-use value', type='ARRAY', group='tou', required='*', constraints='LENGTH=8760')
    eta_field: Final[Array] = OUTPUT(label='Field optical efficiency', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    defocus: Final[Array] = OUTPUT(label='Field optical focus fraction', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_b_conv: Final[Array] = OUTPUT(label='Receiver boiler power loss to convection', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_b_rad: Final[Array] = OUTPUT(label='Receiver boiler power loss to radiation', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_b_abs: Final[Array] = OUTPUT(label='Receiver boiler power absorbed', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_b_in: Final[Array] = OUTPUT(label='Receiver boiler pressure inlet', units='kPa', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_b_out: Final[Array] = OUTPUT(label='Receiver boiler pressure outlet', units='kPa', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_drop_b: Final[Array] = OUTPUT(label='Receiver boiler pressure drop', units='Pa', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    eta_b: Final[Array] = OUTPUT(label='Receiver boiler thermal efficiency', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    T_b_in: Final[Array] = OUTPUT(label='Receiver boiler temperature inlet', units='C', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    T_boiling: Final[Array] = OUTPUT(label='Receiver boiler temperature drum', units='C', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    T_max_b_surf: Final[Array] = OUTPUT(label='Receiver boiler temperature surface max', units='C', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    m_dot_sh: Final[Array] = OUTPUT(label='Receiver superheater mass flow rate', units='kg/hr', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_sh_conv: Final[Array] = OUTPUT(label='Receiver superheater power loss to convection', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_sh_rad: Final[Array] = OUTPUT(label='Receiver superheater power loss to radiation', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_sh_abs: Final[Array] = OUTPUT(label='Receiver superheater power absorbed', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_sh_out: Final[Array] = OUTPUT(label='Receiver superheater pressure outlet', units='kPa', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    dP_sh: Final[Array] = OUTPUT(label='Receiver superheater pressure drop', units='Pa', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    T_max_sh_surf: Final[Array] = OUTPUT(label='Receiver superheater temperature surface max', units='C', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    eta_sh: Final[Array] = OUTPUT(label='Receiver superheater thermal efficiency', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    v_sh_max: Final[Array] = OUTPUT(label='Receiver superheater velocity at outlet', units='m/s', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    f_mdot_rh: Final[Array] = OUTPUT(label='Receiver reheater mass flow rate fraction', units='-', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_rh_conv: Final[Array] = OUTPUT(label='Receiver reheater power loss to convection', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_rh_rad: Final[Array] = OUTPUT(label='Receiver reheater power loss to radiation', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_rh_abs: Final[Array] = OUTPUT(label='Receiver reheater power absorbed', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_rh_in: Final[Array] = OUTPUT(label='Receiver reheater pressure inlet', units='kPa', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_rh_out: Final[Array] = OUTPUT(label='Receiver reheater pressure outlet', units='kPa', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    dP_rh: Final[Array] = OUTPUT(label='Receiver reheater pressure drop', units='Pa', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    eta_rh: Final[Array] = OUTPUT(label='Receiver reheater thermal efficiency', units='-', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    T_rh_in: Final[Array] = OUTPUT(label='Receiver reheater temperature inlet', units='C', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    T_rh_out: Final[Array] = OUTPUT(label='Receiver reheater temperature outlet', units='C', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    T_max_rh_surf: Final[Array] = OUTPUT(label='Receiver reheater temperature surface max', units='C', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    v_rh_max: Final[Array] = OUTPUT(label='Receiver reheater velocity at outlet', units='m/s', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_inc_full: Final[Array] = OUTPUT(label='Receiver power incident (excl. defocus)', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_abs_rec: Final[Array] = OUTPUT(label='Receiver power absorbed total', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_rad_rec: Final[Array] = OUTPUT(label='Receiver power loss to radiation total', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_conv_rec: Final[Array] = OUTPUT(label='Receiver power loss to convection total', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_therm_in_rec: Final[Array] = OUTPUT(label='Receiver power to steam total', units='MWt', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    eta_rec: Final[Array] = OUTPUT(label='Receiver thermal efficiency', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    m_dot_aux: Final[Array] = OUTPUT(label='Auxiliary mass flow rate', units='kg/hr', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_aux: Final[Array] = OUTPUT(label='Auxiliary heat rate delivered to cycle', units='MW', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    q_aux_fuel: Final[Array] = OUTPUT(label='Fuel energy rate to aux heater', units='MMBTU', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_out_net: Final[Array] = OUTPUT(label='Cycle electrical power output (net)', units='MWe', type='ARRAY', group='Net_E_Calc', required='*', constraints='LENGTH=8760')
    P_cycle: Final[Array] = OUTPUT(label='Cycle electrical power output (gross)', units='MWe', type='ARRAY', group='Net_E_Calc', required='*', constraints='LENGTH=8760')
    T_fw: Final[Array] = OUTPUT(label='Cycle temperature feedwater outlet', units='C', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    m_dot_makeup: Final[Array] = OUTPUT(label='Cycle mass flow rate cooling water makeup', units='kg/hr', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    P_cond: Final[Array] = OUTPUT(label='Condenser pressure', units='Pa', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    f_bays: Final[Array] = OUTPUT(label='Condenser fraction of operating bays', type='ARRAY', group='Type250', required='*', constraints='LENGTH=8760')
    W_dot_boost: Final[Array] = OUTPUT(label='Parasitic power receiver boost pump', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    pparasi: Final[Array] = OUTPUT(label='Parasitic power heliostat drives', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_plant_balance_tot: Final[Array] = OUTPUT(label='Parasitic power generation-dependent load', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_fixed: Final[Array] = OUTPUT(label='Parasitic power fixed load', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_cooling_tower_tot: Final[Array] = OUTPUT(label='Parasitic power condenser operation', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_piping_tot: Final[Array] = OUTPUT(label='Parasitic power equiv. header pipe losses', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    P_parasitics: Final[Array] = OUTPUT(label='Parasitic power total consumption', units='MWe', type='ARRAY', group='Outputs', required='*', constraints='LENGTH=8760')
    annual_energy: Final[float] = OUTPUT(label='Annual Energy', units='kWh', type='NUMBER', group='Type228', required='*')
    annual_W_cycle_gross: Final[float] = OUTPUT(label='Electrical source - Power cycle gross output', units='kWh', type='NUMBER', group='Type228', required='*')
    annual_total_water_use: Final[float] = OUTPUT(label='Total Annual Water Usage: cycle + mirror washing', units='m3', type='NUMBER', group='PostProcess', required='*')
    conversion_factor: Final[float] = OUTPUT(label='Gross to Net Conversion Factor', units='%', type='NUMBER', group='Calculated', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', required='*')
    kwh_per_kw: Final[float] = OUTPUT(label='First year kWh/kW', units='kWh/kW', type='NUMBER', required='*')
    system_heat_rate: Final[float] = OUTPUT(label='System heat rate', units='MMBtu/MWh', type='NUMBER', required='*')
    annual_fuel_usage: Final[float] = OUTPUT(label='Annual fuel usage', units='kWh', type='NUMBER', required='*')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Adjustment Factors', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly Adjustment Factors', units='%', type='ARRAY', group='Adjustment Factors', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based Adjustment Factors', units='%', type='MATRIX', group='Adjustment Factors', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    gen: Final[Array] = OUTPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')
    sf_adjust_constant: float = INPUT(name='sf_adjust:constant', label='SF Constant loss adjustment', units='%', type='NUMBER', group='Adjustment Factors', required='*', constraints='MAX=100')
    sf_adjust_hourly: Array = INPUT(name='sf_adjust:hourly', label='SF Hourly Adjustment Factors', units='%', type='ARRAY', group='Adjustment Factors', required='?', constraints='LENGTH=8760')
    sf_adjust_periods: Matrix = INPUT(name='sf_adjust:periods', label='SF Period-based Adjustment Factors', units='%', type='MATRIX', group='Adjustment Factors', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')

    def __init__(self, *args: Mapping[str, Any],
                 solar_resource_file: str = ...,
                 system_capacity: float = ...,
                 weekday_schedule: Matrix = ...,
                 weekend_schedule: Matrix = ...,
                 run_type: float = ...,
                 helio_width: float = ...,
                 helio_height: float = ...,
                 helio_optical_error: float = ...,
                 helio_active_fraction: float = ...,
                 helio_reflectance: float = ...,
                 rec_absorptance: float = ...,
                 rec_aspect: float = ...,
                 rec_height: float = ...,
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
                 dens_mirror: float = ...,
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
                 water_usage_per_wash: float = ...,
                 washing_frequency: float = ...,
                 H_rec: float = ...,
                 THT: float = ...,
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
                 fossil_mode: float = ...,
                 q_pb_design: float = ...,
                 q_aux_max: float = ...,
                 lhv_eff: float = ...,
                 h_tower: float = ...,
                 n_panels: float = ...,
                 flowtype: float = ...,
                 d_rec: float = ...,
                 q_rec_des: float = ...,
                 f_rec_min: float = ...,
                 rec_qf_delay: float = ...,
                 rec_su_delay: float = ...,
                 f_pb_cutoff: float = ...,
                 f_pb_sb: float = ...,
                 t_standby_ini: float = ...,
                 x_b_target: float = ...,
                 eta_rec_pump: float = ...,
                 P_hp_in_des: float = ...,
                 P_hp_out_des: float = ...,
                 f_mdotrh_des: float = ...,
                 p_cycle_design: float = ...,
                 ct: float = ...,
                 T_amb_des: float = ...,
                 dT_cw_ref: float = ...,
                 T_approach: float = ...,
                 T_ITD_des: float = ...,
                 hl_ffact: float = ...,
                 h_boiler: float = ...,
                 d_t_boiler: float = ...,
                 th_t_boiler: float = ...,
                 rec_emis: float = ...,
                 mat_boiler: float = ...,
                 h_sh: float = ...,
                 d_sh: float = ...,
                 th_sh: float = ...,
                 mat_sh: float = ...,
                 T_sh_out_des: float = ...,
                 h_rh: float = ...,
                 d_rh: float = ...,
                 th_rh: float = ...,
                 mat_rh: float = ...,
                 T_rh_out_des: float = ...,
                 cycle_max_frac: float = ...,
                 A_sf: float = ...,
                 ffrac: Array = ...,
                 P_b_in_init: float = ...,
                 f_mdot_rh_init: float = ...,
                 P_hp_out: float = ...,
                 T_hp_out: float = ...,
                 T_rh_target: float = ...,
                 T_fw_init: float = ...,
                 P_cond_init: float = ...,
                 P_ref: float = ...,
                 eta_ref: float = ...,
                 T_hot_ref: float = ...,
                 T_cold_ref: float = ...,
                 q_sby_frac: float = ...,
                 P_boil_des: float = ...,
                 P_rh_ref: float = ...,
                 rh_frac_ref: float = ...,
                 startup_time: float = ...,
                 startup_frac: float = ...,
                 P_cond_ratio: float = ...,
                 pb_bd_frac: float = ...,
                 P_cond_min: float = ...,
                 n_pl_inc: float = ...,
                 F_wc: Array = ...,
                 T_hot: float = ...,
                 Piping_loss: float = ...,
                 Piping_length: float = ...,
                 piping_length_mult: float = ...,
                 piping_length_add: float = ...,
                 Design_power: float = ...,
                 design_eff: float = ...,
                 pb_fixed_par: float = ...,
                 aux_par: float = ...,
                 aux_par_f: float = ...,
                 aux_par_0: float = ...,
                 aux_par_1: float = ...,
                 aux_par_2: float = ...,
                 bop_par: float = ...,
                 bop_par_f: float = ...,
                 bop_par_0: float = ...,
                 bop_par_1: float = ...,
                 bop_par_2: float = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...,
                 sf_adjust_constant: float = ...,
                 sf_adjust_hourly: Array = ...,
                 sf_adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
