
# This is a generated file

"""biomass - Utility scale wind farm model (adapted from TRNSYS code by P.Quinlan and openWind software by AWS Truepower)"""

# VERSION: 2

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
        'file_name': str,
        'system_capacity': float,
        'biopwr.feedstock.total': float,
        'biopwr.feedstock.total_biomass': float,
        'biopwr.feedstock.total_moisture': float,
        'biopwr.feedstock.total_coal': float,
        'biopwr.feedstock.total_lhv': float,
        'biopwr.feedstock.total_hhv': float,
        'biopwr.feedstock.total_c': float,
        'biopwr.feedstock.total_biomass_c': float,
        'biopwr.feedstock.total_h': float,
        'biopwr.feedstock.bagasse_frac': float,
        'biopwr.feedstock.barley_frac': float,
        'biopwr.feedstock.stover_frac': float,
        'biopwr.feedstock.rice_frac': float,
        'biopwr.feedstock.wheat_frac': float,
        'biopwr.feedstock.forest_frac': float,
        'biopwr.feedstock.mill_frac': float,
        'biopwr.feedstock.mill_c': float,
        'biopwr.feedstock.urban_frac': float,
        'biopwr.feedstock.urban_c': float,
        'biopwr.feedstock.woody_frac': float,
        'biopwr.feedstock.woody_c': float,
        'biopwr.feedstock.herb_frac': float,
        'biopwr.feedstock.herb_c': float,
        'biopwr.feedstock.additional_opt': float,
        'biopwr.feedstock.feedstock1_resource': float,
        'biopwr.feedstock.feedstock2_resource': float,
        'biopwr.feedstock.feedstock1_c': float,
        'biopwr.feedstock.feedstock2_c': float,
        'biopwr.feedstock.feedstock1_h': float,
        'biopwr.feedstock.feedstock2_h': float,
        'biopwr.feedstock.feedstock1_hhv': float,
        'biopwr.feedstock.feedstock2_hhv': float,
        'biopwr.feedstock.feedstock1_frac': float,
        'biopwr.feedstock.feedstock2_frac': float,
        'biopwr.feedstock.bit_frac': float,
        'biopwr.feedstock.subbit_frac': float,
        'biopwr.feedstock.lig_frac': float,
        'biopwr.feedstock.bagasse_moisture': float,
        'biopwr.feedstock.barley_moisture': float,
        'biopwr.feedstock.stover_moisture': float,
        'biopwr.feedstock.rice_moisture': float,
        'biopwr.feedstock.wheat_moisture': float,
        'biopwr.feedstock.forest_moisture': float,
        'biopwr.feedstock.mill_moisture': float,
        'biopwr.feedstock.urban_moisture': float,
        'biopwr.feedstock.woody_moisture': float,
        'biopwr.feedstock.herb_moisture': float,
        'biopwr.feedstock.feedstock1_moisture': float,
        'biopwr.feedstock.feedstock2_moisture': float,
        'biopwr.feedstock.bit_moisture': float,
        'biopwr.feedstock.subbit_moisture': float,
        'biopwr.feedstock.lig_moisture': float,
        'biopwr.feedstock.collection_radius': float,
        'biopwr.emissions.avoided_cred': float,
        'biopwr.emissions.collection_fuel': float,
        'biopwr.emissions.transport_fuel': float,
        'biopwr.emissions.transport_legs': float,
        'biopwr.emissions.transport_predist': float,
        'biopwr.emissions.transport_long': float,
        'biopwr.emissions.transport_longmiles': float,
        'biopwr.emissions.transport_longopt': float,
        'biopwr.emissions.pre_chipopt': float,
        'biopwr.emissions.pre_grindopt': float,
        'biopwr.emissions.pre_pelletopt': float,
        'biopwr.emissions.grid_intensity': float,
        'biopwr.plant.drying_method': float,
        'biopwr.plant.drying_spec': float,
        'biopwr.plant.combustor_type': float,
        'biopwr.plant.boiler.air_feed': float,
        'biopwr.plant.boiler.flue_temp': float,
        'biopwr.plant.boiler.steam_enthalpy': float,
        'biopwr.plant.boiler.num': float,
        'biopwr.plant.boiler.cap_per_boiler': float,
        'biopwr.plant.nameplate': float,
        'biopwr.plant.rated_eff': float,
        'biopwr.plant.min_load': float,
        'biopwr.plant.max_over_design': float,
        'biopwr.plant.boiler.over_design': float,
        'biopwr.plant.cycle_design_temp': float,
        'biopwr.plant.pl_eff_f0': float,
        'biopwr.plant.pl_eff_f1': float,
        'biopwr.plant.pl_eff_f2': float,
        'biopwr.plant.pl_eff_f3': float,
        'biopwr.plant.pl_eff_f4': float,
        'biopwr.plant.temp_eff_f0': float,
        'biopwr.plant.temp_eff_f1': float,
        'biopwr.plant.temp_eff_f2': float,
        'biopwr.plant.temp_eff_f3': float,
        'biopwr.plant.temp_eff_f4': float,
        'biopwr.plant.temp_corr_mode': float,
        'biopwr.plant.par_percent': float,
        'biopwr.plant.tou_option': float,
        'biopwr.plant.disp.power': Array,
        'biopwr.plant.ramp_rate': float,
        'biopwr.plant.tou_grid': str,
        'biopwr.plant.boiler.steam_pressure': float,
        'hourly_q_to_pb': Array,
        'hourly_boiler_eff': Array,
        'hourly_pbeta': Array,
        'monthly_energy': Array,
        'monthly_q_to_pb': Array,
        'monthly_pb_eta': Array,
        'monthly_boiler_eff': Array,
        'monthly_moist': Array,
        'monthly_lhv_heatrate': Array,
        'monthly_hhv_heatrate': Array,
        'monthly_bagasse_emc': Array,
        'monthly_barley_emc': Array,
        'monthly_stover_emc': Array,
        'monthly_rice_emc': Array,
        'monthly_wheat_emc': Array,
        'monthly_forest_emc': Array,
        'monthly_mill_emc': Array,
        'monthly_urban_emc': Array,
        'monthly_woody_emc': Array,
        'monthly_herb_emc': Array,
        'monthly_temp_c': Array,
        'monthly_rh': Array,
        'annual_energy': float,
        'system.annual.e_net': float,
        'system.annual.biomass': float,
        'system.annual.coal': float,
        'annual_fuel_usage': float,
        'annual_watter_usage': float,
        'system.annual.ash': float,
        'system.capfactor': float,
        'system.hhv_heatrate': float,
        'system.lhv_heatrate': float,
        'system_heat_rate': float,
        'system.hhv_thermeff': float,
        'system.lhv_thermeff': float,
        'system.total_moisture': float,
        'system.emissions.growth': float,
        'system.emissions.avoided': float,
        'system.emissions.transport': float,
        'system.emissions.preprocessing': float,
        'system.emissions.drying': float,
        'system.emissions.combustion': float,
        'system.emissions.uptake': float,
        'system.emissions.total_sum': float,
        'system.emissions.diesel': float,
        'system.emissions.biodiesel': float,
        'system.emissions.bunker': float,
        'system.emissions.oil': float,
        'system.emissions.naturalgas': float,
        'system.emissions.nitrogen': float,
        'system.emissions.potassium': float,
        'system.emissions.phosphorus': float,
        'system.emissions.lime': float,
        'system.emissions.ems_per_lb': float,
        'system.annual.boiler_loss_fuel_kwh': float,
        'system.annual.boiler_loss_unburn_kwh': float,
        'system.annual.boiler_loss_manu_kwh': float,
        'system.annual.boiler_loss_rad_kwh': float,
        'system.annual.boiler_loss_dry_kwh': float,
        'system.annual.boiler_loss_wet_kwh': float,
        'system.annual.pb_eta_kwh': float,
        'system.annual.par_loss_kwh': float,
        'system.annual.boiler_loss_total_kwh': float,
        'system.annual.boiler_output': float,
        'system.annual.turbine_output': float,
        'system.annual.boiler_loss_fuel': float,
        'system.annual.boiler_loss_unburn': float,
        'system.annual.boiler_loss_manu': float,
        'system.annual.boiler_loss_rad': float,
        'system.annual.boiler_loss_dry': float,
        'system.annual.boiler_loss_wet': float,
        'system.annual.pb_eta': float,
        'system.annual.par_loss': float,
        'system.annual.boiler_loss_total': float,
        'system.annual.qtoboil_tot': float,
        'system.annual.qtopb_tot': float,
        'capacity_factor': float,
        'kwh_per_kw': float,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix,
        'gen': Array
    }, total=False)

class Data(ssc.DataDict):
    file_name: str = INPUT(label='Local weather file path', type='STRING', group='biopower', required='*', constraints='LOCAL_FILE')
    system_capacity: float = INPUT(label='Nameplate capacity', units='kW', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_total: float = INPUT(name='biopwr.feedstock.total', label='Total fuel resource (dt/yr)', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_total_biomass: float = INPUT(name='biopwr.feedstock.total_biomass', label='Total biomass resource (dt/yr)', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_total_moisture: float = INPUT(name='biopwr.feedstock.total_moisture', label='Overall Moisture Content (dry %)', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_total_coal: float = INPUT(name='biopwr.feedstock.total_coal', label='Total coal resource (dt/yr)', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_total_lhv: float = INPUT(name='biopwr.feedstock.total_lhv', label='Dry feedstock LHV (Btu/lb)', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_total_hhv: float = INPUT(name='biopwr.feedstock.total_hhv', label='Dry feedstock HHV (Btu/lb)', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_total_c: float = INPUT(name='biopwr.feedstock.total_c', label='Mass fraction carbon', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_total_biomass_c: float = INPUT(name='biopwr.feedstock.total_biomass_c', label='Biomass fraction carbon', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_total_h: float = INPUT(name='biopwr.feedstock.total_h', label='Mass fraction hydrogen', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_bagasse_frac: float = INPUT(name='biopwr.feedstock.bagasse_frac', label='Bagasse feedstock fraction', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_barley_frac: float = INPUT(name='biopwr.feedstock.barley_frac', label='Barley feedstock fraction', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_stover_frac: float = INPUT(name='biopwr.feedstock.stover_frac', label='Stover feedstock fraction', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_rice_frac: float = INPUT(name='biopwr.feedstock.rice_frac', label='Rice straw feedstock fraction', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_wheat_frac: float = INPUT(name='biopwr.feedstock.wheat_frac', label='Wheat straw feedstock fraction', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_forest_frac: float = INPUT(name='biopwr.feedstock.forest_frac', label='Forest residue feedstock fraction', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_mill_frac: float = INPUT(name='biopwr.feedstock.mill_frac', label='Mill residue feedstock fraction', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_mill_c: float = INPUT(name='biopwr.feedstock.mill_c', label='Carbon fraction in mill residue', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_urban_frac: float = INPUT(name='biopwr.feedstock.urban_frac', label='Urban wood residue feedstock fraction', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_urban_c: float = INPUT(name='biopwr.feedstock.urban_c', label='Carbon fraction in urban residue', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_woody_frac: float = INPUT(name='biopwr.feedstock.woody_frac', label='Woody energy crop feedstock fraction', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_woody_c: float = INPUT(name='biopwr.feedstock.woody_c', label='Carbon fraction in woody energy crop', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_herb_frac: float = INPUT(name='biopwr.feedstock.herb_frac', label='Herbaceous energy crop feedstock fraction', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_herb_c: float = INPUT(name='biopwr.feedstock.herb_c', label='Carbon fraction in herbaceous energy crop', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_additional_opt: float = INPUT(name='biopwr.feedstock.additional_opt', type='NUMBER', group='biopower', required='*', constraints='INTEGER')
    biopwr_feedstock_feedstock1_resource: float = INPUT(name='biopwr.feedstock.feedstock1_resource', label='Opt feedstock 1 (dt/yr)', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_feedstock2_resource: float = INPUT(name='biopwr.feedstock.feedstock2_resource', label='Opt feedstock 2 (dt/yr)', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_feedstock1_c: float = INPUT(name='biopwr.feedstock.feedstock1_c', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_feedstock2_c: float = INPUT(name='biopwr.feedstock.feedstock2_c', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_feedstock1_h: float = INPUT(name='biopwr.feedstock.feedstock1_h', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_feedstock2_h: float = INPUT(name='biopwr.feedstock.feedstock2_h', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_feedstock1_hhv: float = INPUT(name='biopwr.feedstock.feedstock1_hhv', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_feedstock2_hhv: float = INPUT(name='biopwr.feedstock.feedstock2_hhv', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_feedstock1_frac: float = INPUT(name='biopwr.feedstock.feedstock1_frac', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_feedstock2_frac: float = INPUT(name='biopwr.feedstock.feedstock2_frac', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_bit_frac: float = INPUT(name='biopwr.feedstock.bit_frac', label='Bituminos coal feedstock fraction', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_subbit_frac: float = INPUT(name='biopwr.feedstock.subbit_frac', label='Sub-bituminous coal feedstock fraction', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_lig_frac: float = INPUT(name='biopwr.feedstock.lig_frac', label='Lignite coal feedstock fraction', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_bagasse_moisture: float = INPUT(name='biopwr.feedstock.bagasse_moisture', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_barley_moisture: float = INPUT(name='biopwr.feedstock.barley_moisture', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_stover_moisture: float = INPUT(name='biopwr.feedstock.stover_moisture', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_rice_moisture: float = INPUT(name='biopwr.feedstock.rice_moisture', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_wheat_moisture: float = INPUT(name='biopwr.feedstock.wheat_moisture', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_forest_moisture: float = INPUT(name='biopwr.feedstock.forest_moisture', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_mill_moisture: float = INPUT(name='biopwr.feedstock.mill_moisture', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_urban_moisture: float = INPUT(name='biopwr.feedstock.urban_moisture', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_woody_moisture: float = INPUT(name='biopwr.feedstock.woody_moisture', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_herb_moisture: float = INPUT(name='biopwr.feedstock.herb_moisture', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_feedstock1_moisture: float = INPUT(name='biopwr.feedstock.feedstock1_moisture', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_feedstock2_moisture: float = INPUT(name='biopwr.feedstock.feedstock2_moisture', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_bit_moisture: float = INPUT(name='biopwr.feedstock.bit_moisture', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_subbit_moisture: float = INPUT(name='biopwr.feedstock.subbit_moisture', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_lig_moisture: float = INPUT(name='biopwr.feedstock.lig_moisture', type='NUMBER', group='biopower', required='*')
    biopwr_feedstock_collection_radius: float = INPUT(name='biopwr.feedstock.collection_radius', type='NUMBER', group='biopower', required='*')
    biopwr_emissions_avoided_cred: float = INPUT(name='biopwr.emissions.avoided_cred', type='NUMBER', group='biopower', required='*', constraints='INTEGER')
    biopwr_emissions_collection_fuel: float = INPUT(name='biopwr.emissions.collection_fuel', type='NUMBER', group='biopower', required='*', constraints='INTEGER')
    biopwr_emissions_transport_fuel: float = INPUT(name='biopwr.emissions.transport_fuel', type='NUMBER', group='biopower', required='*', constraints='INTEGER')
    biopwr_emissions_transport_legs: float = INPUT(name='biopwr.emissions.transport_legs', type='NUMBER', group='biopower', required='*', constraints='INTEGER')
    biopwr_emissions_transport_predist: float = INPUT(name='biopwr.emissions.transport_predist', type='NUMBER', group='biopower', required='*')
    biopwr_emissions_transport_long: float = INPUT(name='biopwr.emissions.transport_long', type='NUMBER', group='biopower', required='*', constraints='INTEGER')
    biopwr_emissions_transport_longmiles: float = INPUT(name='biopwr.emissions.transport_longmiles', type='NUMBER', group='biopower', required='*')
    biopwr_emissions_transport_longopt: float = INPUT(name='biopwr.emissions.transport_longopt', type='NUMBER', group='biopower', required='*', constraints='INTEGER')
    biopwr_emissions_pre_chipopt: float = INPUT(name='biopwr.emissions.pre_chipopt', type='NUMBER', group='biopower', required='*', constraints='INTEGER')
    biopwr_emissions_pre_grindopt: float = INPUT(name='biopwr.emissions.pre_grindopt', type='NUMBER', group='biopower', required='*', constraints='INTEGER')
    biopwr_emissions_pre_pelletopt: float = INPUT(name='biopwr.emissions.pre_pelletopt', type='NUMBER', group='biopower', required='*', constraints='INTEGER')
    biopwr_emissions_grid_intensity: float = INPUT(name='biopwr.emissions.grid_intensity', type='NUMBER', group='biopower', required='*')
    biopwr_plant_drying_method: float = INPUT(name='biopwr.plant.drying_method', type='NUMBER', group='biopower', required='*', constraints='INTEGER')
    biopwr_plant_drying_spec: float = INPUT(name='biopwr.plant.drying_spec', type='NUMBER', group='biopower', required='*')
    biopwr_plant_combustor_type: float = INPUT(name='biopwr.plant.combustor_type', type='NUMBER', group='biopower', required='*', constraints='INTEGER')
    biopwr_plant_boiler_air_feed: float = INPUT(name='biopwr.plant.boiler.air_feed', type='NUMBER', group='biopower', required='*')
    biopwr_plant_boiler_flue_temp: float = INPUT(name='biopwr.plant.boiler.flue_temp', type='NUMBER', group='biopower', required='*')
    biopwr_plant_boiler_steam_enthalpy: float = INPUT(name='biopwr.plant.boiler.steam_enthalpy', type='NUMBER', group='biopower', required='*')
    biopwr_plant_boiler_num: float = INPUT(name='biopwr.plant.boiler.num', type='NUMBER', group='biopower', required='*')
    biopwr_plant_boiler_cap_per_boiler: float = INPUT(name='biopwr.plant.boiler.cap_per_boiler', type='NUMBER', group='biopower', required='*')
    biopwr_plant_nameplate: float = INPUT(name='biopwr.plant.nameplate', type='NUMBER', group='biopower', required='*')
    biopwr_plant_rated_eff: float = INPUT(name='biopwr.plant.rated_eff', type='NUMBER', group='biopower', required='*')
    biopwr_plant_min_load: float = INPUT(name='biopwr.plant.min_load', type='NUMBER', group='biopower', required='*')
    biopwr_plant_max_over_design: float = INPUT(name='biopwr.plant.max_over_design', type='NUMBER', group='biopower', required='*')
    biopwr_plant_boiler_over_design: float = INPUT(name='biopwr.plant.boiler.over_design', type='NUMBER', group='biopower', required='*')
    biopwr_plant_cycle_design_temp: float = INPUT(name='biopwr.plant.cycle_design_temp', type='NUMBER', group='biopower', required='*')
    biopwr_plant_pl_eff_f0: float = INPUT(name='biopwr.plant.pl_eff_f0', type='NUMBER', group='biopower', required='*')
    biopwr_plant_pl_eff_f1: float = INPUT(name='biopwr.plant.pl_eff_f1', type='NUMBER', group='biopower', required='*')
    biopwr_plant_pl_eff_f2: float = INPUT(name='biopwr.plant.pl_eff_f2', type='NUMBER', group='biopower', required='*')
    biopwr_plant_pl_eff_f3: float = INPUT(name='biopwr.plant.pl_eff_f3', type='NUMBER', group='biopower', required='*')
    biopwr_plant_pl_eff_f4: float = INPUT(name='biopwr.plant.pl_eff_f4', type='NUMBER', group='biopower', required='*')
    biopwr_plant_temp_eff_f0: float = INPUT(name='biopwr.plant.temp_eff_f0', type='NUMBER', group='biopower', required='*')
    biopwr_plant_temp_eff_f1: float = INPUT(name='biopwr.plant.temp_eff_f1', type='NUMBER', group='biopower', required='*')
    biopwr_plant_temp_eff_f2: float = INPUT(name='biopwr.plant.temp_eff_f2', type='NUMBER', group='biopower', required='*')
    biopwr_plant_temp_eff_f3: float = INPUT(name='biopwr.plant.temp_eff_f3', type='NUMBER', group='biopower', required='*')
    biopwr_plant_temp_eff_f4: float = INPUT(name='biopwr.plant.temp_eff_f4', type='NUMBER', group='biopower', required='*')
    biopwr_plant_temp_corr_mode: float = INPUT(name='biopwr.plant.temp_corr_mode', type='NUMBER', group='biopower', required='*', constraints='INTEGER')
    biopwr_plant_par_percent: float = INPUT(name='biopwr.plant.par_percent', type='NUMBER', group='biopower', required='*')
    biopwr_plant_tou_option: float = INPUT(name='biopwr.plant.tou_option', type='NUMBER', group='biopower', required='*', constraints='INTEGER')
    biopwr_plant_disp_power: Array = INPUT(name='biopwr.plant.disp.power', type='ARRAY', group='biopower', required='*', constraints='LENGTH=9')
    biopwr_plant_ramp_rate: float = INPUT(name='biopwr.plant.ramp_rate', type='NUMBER', group='biopower', required='*')
    biopwr_plant_tou_grid: str = INPUT(name='biopwr.plant.tou_grid', type='STRING', group='biopower', required='*')
    biopwr_plant_boiler_steam_pressure: float = INPUT(name='biopwr.plant.boiler.steam_pressure', type='NUMBER', group='biopower', required='*')
    hourly_q_to_pb: Final[Array] = OUTPUT(label='Q To Power Block', units='kW', type='ARRAY', group='biomass', required='*', constraints='LENGTH=8760')
    hourly_boiler_eff: Final[Array] = OUTPUT(label='Boiler Efficiency', type='ARRAY', group='biomass', required='*', constraints='LENGTH=8760')
    hourly_pbeta: Final[Array] = OUTPUT(label='Power Block Efficiency', type='ARRAY', group='biomass', required='*', constraints='LENGTH=8760')
    monthly_energy: Final[Array] = OUTPUT(label='Monthly Energy', units='kWh', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_q_to_pb: Final[Array] = OUTPUT(label='Q To Power Block', units='kWh', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_pb_eta: Final[Array] = OUTPUT(label='Power Block Effiency', units='%', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_boiler_eff: Final[Array] = OUTPUT(label='Total Boiler Efficiency - HHV (%)', units='%', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_moist: Final[Array] = OUTPUT(label='Monthly biomass moisture fraction (dry)', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_lhv_heatrate: Final[Array] = OUTPUT(label='Net Monthly Heat Rate (MMBtu/MWh)', units='MMBtu/MWh', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_hhv_heatrate: Final[Array] = OUTPUT(label='Gross Monthly Heat Rate (MMBtu/MWh)', units='MMBtu/MWh', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_bagasse_emc: Final[Array] = OUTPUT(label='Monthly bagasse EMC (dry)', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_barley_emc: Final[Array] = OUTPUT(label='Monthly barley EMC (dry)', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_stover_emc: Final[Array] = OUTPUT(label='Monthly stover EMC (dry)', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_rice_emc: Final[Array] = OUTPUT(label='Monthly rice straw EMC (dry)', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_wheat_emc: Final[Array] = OUTPUT(label='Monthly wheat straw EMC (dry)', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_forest_emc: Final[Array] = OUTPUT(label='Monthly forest EMC (dry)', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_mill_emc: Final[Array] = OUTPUT(label='Monthly mill waste EMC (dry)', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_urban_emc: Final[Array] = OUTPUT(label='Monthly urban wood waste EMC (dry)', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_woody_emc: Final[Array] = OUTPUT(label='Monthly woody crop EMC (dry)', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_herb_emc: Final[Array] = OUTPUT(label='Monthly herbaceous crop EMC (dry)', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_temp_c: Final[Array] = OUTPUT(label='Temperature', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    monthly_rh: Final[Array] = OUTPUT(label='Relative humidity', type='ARRAY', group='biomass', required='*', constraints='LENGTH=12')
    annual_energy: Final[float] = OUTPUT(label='Annual Energy', units='kWh', type='NUMBER', group='biomass', required='*')
    system_annual_e_net: Final[float] = OUTPUT(name='system.annual.e_net', label='Gross Annual Energy', units='kWh', type='NUMBER', group='biomass', required='*')
    system_annual_biomass: Final[float] = OUTPUT(name='system.annual.biomass', label='Annual biomass usage', units='dry tons/yr', type='NUMBER', group='biomass', required='*')
    system_annual_coal: Final[float] = OUTPUT(name='system.annual.coal', label='Annual coal usage', units='dry tons/yr', type='NUMBER', group='biomass', required='*')
    annual_fuel_usage: Final[float] = OUTPUT(label='Annual Fuel Usage', units='kWht', type='NUMBER', group='biomass', required='*')
    annual_watter_usage: Final[float] = OUTPUT(label='Annual Water Usage', units='m3', type='NUMBER', group='biomass', required='*')
    system_annual_ash: Final[float] = OUTPUT(name='system.annual.ash', label='Ash produced', units='tons/yr', type='NUMBER', group='biomass', required='*')
    system_capfactor: Final[float] = OUTPUT(name='system.capfactor', label='Annual Capacity Factor (%)', units='%', type='NUMBER', group='biomass', required='*')
    system_hhv_heatrate: Final[float] = OUTPUT(name='system.hhv_heatrate', label='Gross Heat Rate (MMBtu/MWh)', units='MMBtu/MWh', type='NUMBER', group='biomass', required='*')
    system_lhv_heatrate: Final[float] = OUTPUT(name='system.lhv_heatrate', label='Net Heat Rate (MMBtu/MWh)', units='MMBtu/MWh', type='NUMBER', group='biomass', required='*')
    system_heat_rate: Final[float] = OUTPUT(label='Heat Rate Conversion Factor (MMBTUs/MWhe)', units='MMBTUs/MWhe', type='NUMBER', group='biomass', required='*')
    system_hhv_thermeff: Final[float] = OUTPUT(name='system.hhv_thermeff', label='Thermal efficiency, HHV (%)', units='%', type='NUMBER', group='biomass', required='*')
    system_lhv_thermeff: Final[float] = OUTPUT(name='system.lhv_thermeff', label='Thermal efficiency, LHV (%)', units='%', type='NUMBER', group='biomass', required='*')
    system_total_moisture: Final[float] = OUTPUT(name='system.total_moisture', label='Overall Moisture Content (dry %)', units='%', type='NUMBER', group='biomass', required='*')
    system_emissions_growth: Final[float] = OUTPUT(name='system.emissions.growth', label='Biomass Collection', units='kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_avoided: Final[float] = OUTPUT(name='system.emissions.avoided', label='Biomass Avoided Use', units='kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_transport: Final[float] = OUTPUT(name='system.emissions.transport', label='Biomass Transport', units='kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_preprocessing: Final[float] = OUTPUT(name='system.emissions.preprocessing', label='Biomass Preprocessing', units='kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_drying: Final[float] = OUTPUT(name='system.emissions.drying', label='Biomass Drying', units='kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_combustion: Final[float] = OUTPUT(name='system.emissions.combustion', label='Combustion', units='kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_uptake: Final[float] = OUTPUT(name='system.emissions.uptake', label='Biomass CO2 Uptake', units='kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_total_sum: Final[float] = OUTPUT(name='system.emissions.total_sum', label='Biomass Life Cycle CO2', units='kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_diesel: Final[float] = OUTPUT(name='system.emissions.diesel', label='Life Cycle Diesel use', units='Btu/kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_biodiesel: Final[float] = OUTPUT(name='system.emissions.biodiesel', label='Life Cycle Biodiesel use', units='Btu/kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_bunker: Final[float] = OUTPUT(name='system.emissions.bunker', label='Life Cycle Bunker fuel use', units='Btu/kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_oil: Final[float] = OUTPUT(name='system.emissions.oil', label='Life Cycle Oil use', units='Btu/kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_naturalgas: Final[float] = OUTPUT(name='system.emissions.naturalgas', label='Life Cycle Natural gas use', units='Btu/kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_nitrogen: Final[float] = OUTPUT(name='system.emissions.nitrogen', label='Life Cycle Nitrogen fertilizer use', units='lb N/kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_potassium: Final[float] = OUTPUT(name='system.emissions.potassium', label='Life Cycle Potassium fertilizer use', units='lb P2O5/kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_phosphorus: Final[float] = OUTPUT(name='system.emissions.phosphorus', label='Life Cycle Phosphorus fertilizer use', units='lb K2O/kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_lime: Final[float] = OUTPUT(name='system.emissions.lime', label='Life Cycle Lime fertilizer use', units='lb Lime/kWh', type='NUMBER', group='biomass', required='*')
    system_emissions_ems_per_lb: Final[float] = OUTPUT(name='system.emissions.ems_per_lb', label='Life Cycle g CO2eq released/lb dry biomass', type='NUMBER', group='biomass', required='*')
    system_annual_boiler_loss_fuel_kwh: Final[float] = OUTPUT(name='system.annual.boiler_loss_fuel_kwh', label='Energy lost in fuel out of boiler', units='kWh', type='NUMBER', group='biomass', required='*')
    system_annual_boiler_loss_unburn_kwh: Final[float] = OUTPUT(name='system.annual.boiler_loss_unburn_kwh', label='Energy lost in unburned fuel', units='kWh', type='NUMBER', group='biomass', required='*')
    system_annual_boiler_loss_manu_kwh: Final[float] = OUTPUT(name='system.annual.boiler_loss_manu_kwh', label="Energy loss included in manufacturer's margin", units='kWh', type='NUMBER', group='biomass', required='*')
    system_annual_boiler_loss_rad_kwh: Final[float] = OUTPUT(name='system.annual.boiler_loss_rad_kwh', label='Energy loss due to boiler radiation', units='kWh', type='NUMBER', group='biomass', required='*')
    system_annual_boiler_loss_dry_kwh: Final[float] = OUTPUT(name='system.annual.boiler_loss_dry_kwh', label='Energy lost in hot flue gas', units='kWh', type='NUMBER', group='biomass', required='*')
    system_annual_boiler_loss_wet_kwh: Final[float] = OUTPUT(name='system.annual.boiler_loss_wet_kwh', label='Energy lost to moisture in air', units='kWh', type='NUMBER', group='biomass', required='*')
    system_annual_pb_eta_kwh: Final[float] = OUTPUT(name='system.annual.pb_eta_kwh', label='Energy lost in steam turbine and generator', units='kWh', type='NUMBER', group='biomass', required='*')
    system_annual_par_loss_kwh: Final[float] = OUTPUT(name='system.annual.par_loss_kwh', label='Energy consumed within plant - parasitic load', units='kWh', type='NUMBER', group='biomass', required='*')
    system_annual_boiler_loss_total_kwh: Final[float] = OUTPUT(name='system.annual.boiler_loss_total_kwh', label='Energy lost in boiler - total', units='kWh', type='NUMBER', group='biomass', required='*')
    system_annual_boiler_output: Final[float] = OUTPUT(name='system.annual.boiler_output', label='Boiler output', units='kWh', type='NUMBER', group='biomass', required='*')
    system_annual_turbine_output: Final[float] = OUTPUT(name='system.annual.turbine_output', label='Turbine output', units='kWh', type='NUMBER', group='biomass', required='*')
    system_annual_boiler_loss_fuel: Final[float] = OUTPUT(name='system.annual.boiler_loss_fuel', label='Energy lost in fuel out of boiler', units='%', type='NUMBER', group='biomass', required='*')
    system_annual_boiler_loss_unburn: Final[float] = OUTPUT(name='system.annual.boiler_loss_unburn', label='Energy lost in unburned fuel', units='%', type='NUMBER', group='biomass', required='*')
    system_annual_boiler_loss_manu: Final[float] = OUTPUT(name='system.annual.boiler_loss_manu', label="Energy loss included in manufacturer's margin", units='%', type='NUMBER', group='biomass', required='*')
    system_annual_boiler_loss_rad: Final[float] = OUTPUT(name='system.annual.boiler_loss_rad', label='Energy loss due to boiler radiation', units='%', type='NUMBER', group='biomass', required='*')
    system_annual_boiler_loss_dry: Final[float] = OUTPUT(name='system.annual.boiler_loss_dry', label='Energy lost in hot flue gas', units='%', type='NUMBER', group='biomass', required='*')
    system_annual_boiler_loss_wet: Final[float] = OUTPUT(name='system.annual.boiler_loss_wet', label='Energy lost to moisture in air', units='%', type='NUMBER', group='biomass', required='*')
    system_annual_pb_eta: Final[float] = OUTPUT(name='system.annual.pb_eta', label='Energy lost in steam turbine and generator', units='%', type='NUMBER', group='biomass', required='*')
    system_annual_par_loss: Final[float] = OUTPUT(name='system.annual.par_loss', label='Energy consumed within plant - parasitic load', units='%', type='NUMBER', group='biomass', required='*')
    system_annual_boiler_loss_total: Final[float] = OUTPUT(name='system.annual.boiler_loss_total', label='Energy lost in boiler - total', units='%', type='NUMBER', group='biomass', required='*')
    system_annual_qtoboil_tot: Final[float] = OUTPUT(name='system.annual.qtoboil_tot', label='Q to Boiler', units='kWh', type='NUMBER', group='biomass', required='*')
    system_annual_qtopb_tot: Final[float] = OUTPUT(name='system.annual.qtopb_tot', label='Q to Power Block', units='kWh', type='NUMBER', group='biomass', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', required='*')
    kwh_per_kw: Final[float] = OUTPUT(label='First year kWh/kW', units='kWh/kW', type='NUMBER', required='*')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    gen: Final[Array] = OUTPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 file_name: str = ...,
                 system_capacity: float = ...,
                 biopwr_feedstock_total: float = ...,
                 biopwr_feedstock_total_biomass: float = ...,
                 biopwr_feedstock_total_moisture: float = ...,
                 biopwr_feedstock_total_coal: float = ...,
                 biopwr_feedstock_total_lhv: float = ...,
                 biopwr_feedstock_total_hhv: float = ...,
                 biopwr_feedstock_total_c: float = ...,
                 biopwr_feedstock_total_biomass_c: float = ...,
                 biopwr_feedstock_total_h: float = ...,
                 biopwr_feedstock_bagasse_frac: float = ...,
                 biopwr_feedstock_barley_frac: float = ...,
                 biopwr_feedstock_stover_frac: float = ...,
                 biopwr_feedstock_rice_frac: float = ...,
                 biopwr_feedstock_wheat_frac: float = ...,
                 biopwr_feedstock_forest_frac: float = ...,
                 biopwr_feedstock_mill_frac: float = ...,
                 biopwr_feedstock_mill_c: float = ...,
                 biopwr_feedstock_urban_frac: float = ...,
                 biopwr_feedstock_urban_c: float = ...,
                 biopwr_feedstock_woody_frac: float = ...,
                 biopwr_feedstock_woody_c: float = ...,
                 biopwr_feedstock_herb_frac: float = ...,
                 biopwr_feedstock_herb_c: float = ...,
                 biopwr_feedstock_additional_opt: float = ...,
                 biopwr_feedstock_feedstock1_resource: float = ...,
                 biopwr_feedstock_feedstock2_resource: float = ...,
                 biopwr_feedstock_feedstock1_c: float = ...,
                 biopwr_feedstock_feedstock2_c: float = ...,
                 biopwr_feedstock_feedstock1_h: float = ...,
                 biopwr_feedstock_feedstock2_h: float = ...,
                 biopwr_feedstock_feedstock1_hhv: float = ...,
                 biopwr_feedstock_feedstock2_hhv: float = ...,
                 biopwr_feedstock_feedstock1_frac: float = ...,
                 biopwr_feedstock_feedstock2_frac: float = ...,
                 biopwr_feedstock_bit_frac: float = ...,
                 biopwr_feedstock_subbit_frac: float = ...,
                 biopwr_feedstock_lig_frac: float = ...,
                 biopwr_feedstock_bagasse_moisture: float = ...,
                 biopwr_feedstock_barley_moisture: float = ...,
                 biopwr_feedstock_stover_moisture: float = ...,
                 biopwr_feedstock_rice_moisture: float = ...,
                 biopwr_feedstock_wheat_moisture: float = ...,
                 biopwr_feedstock_forest_moisture: float = ...,
                 biopwr_feedstock_mill_moisture: float = ...,
                 biopwr_feedstock_urban_moisture: float = ...,
                 biopwr_feedstock_woody_moisture: float = ...,
                 biopwr_feedstock_herb_moisture: float = ...,
                 biopwr_feedstock_feedstock1_moisture: float = ...,
                 biopwr_feedstock_feedstock2_moisture: float = ...,
                 biopwr_feedstock_bit_moisture: float = ...,
                 biopwr_feedstock_subbit_moisture: float = ...,
                 biopwr_feedstock_lig_moisture: float = ...,
                 biopwr_feedstock_collection_radius: float = ...,
                 biopwr_emissions_avoided_cred: float = ...,
                 biopwr_emissions_collection_fuel: float = ...,
                 biopwr_emissions_transport_fuel: float = ...,
                 biopwr_emissions_transport_legs: float = ...,
                 biopwr_emissions_transport_predist: float = ...,
                 biopwr_emissions_transport_long: float = ...,
                 biopwr_emissions_transport_longmiles: float = ...,
                 biopwr_emissions_transport_longopt: float = ...,
                 biopwr_emissions_pre_chipopt: float = ...,
                 biopwr_emissions_pre_grindopt: float = ...,
                 biopwr_emissions_pre_pelletopt: float = ...,
                 biopwr_emissions_grid_intensity: float = ...,
                 biopwr_plant_drying_method: float = ...,
                 biopwr_plant_drying_spec: float = ...,
                 biopwr_plant_combustor_type: float = ...,
                 biopwr_plant_boiler_air_feed: float = ...,
                 biopwr_plant_boiler_flue_temp: float = ...,
                 biopwr_plant_boiler_steam_enthalpy: float = ...,
                 biopwr_plant_boiler_num: float = ...,
                 biopwr_plant_boiler_cap_per_boiler: float = ...,
                 biopwr_plant_nameplate: float = ...,
                 biopwr_plant_rated_eff: float = ...,
                 biopwr_plant_min_load: float = ...,
                 biopwr_plant_max_over_design: float = ...,
                 biopwr_plant_boiler_over_design: float = ...,
                 biopwr_plant_cycle_design_temp: float = ...,
                 biopwr_plant_pl_eff_f0: float = ...,
                 biopwr_plant_pl_eff_f1: float = ...,
                 biopwr_plant_pl_eff_f2: float = ...,
                 biopwr_plant_pl_eff_f3: float = ...,
                 biopwr_plant_pl_eff_f4: float = ...,
                 biopwr_plant_temp_eff_f0: float = ...,
                 biopwr_plant_temp_eff_f1: float = ...,
                 biopwr_plant_temp_eff_f2: float = ...,
                 biopwr_plant_temp_eff_f3: float = ...,
                 biopwr_plant_temp_eff_f4: float = ...,
                 biopwr_plant_temp_corr_mode: float = ...,
                 biopwr_plant_par_percent: float = ...,
                 biopwr_plant_tou_option: float = ...,
                 biopwr_plant_disp_power: Array = ...,
                 biopwr_plant_ramp_rate: float = ...,
                 biopwr_plant_tou_grid: str = ...,
                 biopwr_plant_boiler_steam_pressure: float = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
