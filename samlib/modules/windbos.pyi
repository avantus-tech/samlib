
# This is a generated file

"""windbos - Wind Balance of System cost model"""

# VERSION: 1

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
        'machine_rating': float,
        'rotor_diameter': float,
        'hub_height': float,
        'number_of_turbines': float,
        'interconnect_voltage': float,
        'distance_to_interconnect': float,
        'site_terrain': float,
        'turbine_layout': float,
        'soil_condition': float,
        'construction_time': float,
        'om_building_size': float,
        'quantity_test_met_towers': float,
        'quantity_permanent_met_towers': float,
        'weather_delay_days': float,
        'crane_breakdowns': float,
        'access_road_entrances': float,
        'turbine_capital_cost': float,
        'tower_top_mass': float,
        'delivery_assist_required': float,
        'pad_mount_transformer_required': float,
        'new_switchyard_required': float,
        'rock_trenching_required': float,
        'mv_thermal_backfill': float,
        'mv_overhead_collector': float,
        'performance_bond': float,
        'contingency': float,
        'warranty_management': float,
        'sales_and_use_tax': float,
        'overhead': float,
        'profit_margin': float,
        'development_fee': float,
        'turbine_transportation': float,
        'project_total_budgeted_cost': float,
        'transportation_cost': float,
        'insurance_cost': float,
        'engineering_cost': float,
        'power_performance_cost': float,
        'site_compound_security_cost': float,
        'building_cost': float,
        'transmission_cost': float,
        'markup_cost': float,
        'development_cost': float,
        'access_roads_cost': float,
        'foundation_cost': float,
        'erection_cost': float,
        'electrical_materials_cost': float,
        'electrical_installation_cost': float,
        'substation_cost': float,
        'project_mgmt_cost': float
    }, total=False)

class Data(ssc.DataDict):
    machine_rating: float = INPUT(label='Machine Rating', units='kW', type='NUMBER', group='wind_bos', required='*')
    rotor_diameter: float = INPUT(label='Rotor Diameter', units='m', type='NUMBER', group='wind_bos', required='*')
    hub_height: float = INPUT(label='Hub Height', units='m', type='NUMBER', group='wind_bos', required='*')
    number_of_turbines: float = INPUT(label='Number of Turbines', type='NUMBER', group='wind_bos', required='*', constraints='INTEGER')
    interconnect_voltage: float = INPUT(label='Interconnect Voltage', units='kV', type='NUMBER', group='wind_bos', required='*')
    distance_to_interconnect: float = INPUT(label='Distance to Interconnect', units='miles', type='NUMBER', group='wind_bos', required='*')
    site_terrain: float = INPUT(label='Site Terrain', type='NUMBER', group='wind_bos', required='*', constraints='INTEGER')
    turbine_layout: float = INPUT(label='Turbine Layout', type='NUMBER', group='wind_bos', required='*', constraints='INTEGER')
    soil_condition: float = INPUT(label='Soil Condition', type='NUMBER', group='wind_bos', required='*', constraints='INTEGER')
    construction_time: float = INPUT(label='Construction Time', units='months', type='NUMBER', group='wind_bos', required='*')
    om_building_size: float = INPUT(label='O&M Building Size', units='ft^2', type='NUMBER', group='wind_bos', required='*')
    quantity_test_met_towers: float = INPUT(label='Quantity of Temporary Meteorological Towers for Testing', type='NUMBER', group='wind_bos', required='*')
    quantity_permanent_met_towers: float = INPUT(label='Quantity of Permanent Meteorological Towers for Testing', type='NUMBER', group='wind_bos', required='*')
    weather_delay_days: float = INPUT(label='Wind / Weather delay days', type='NUMBER', group='wind_bos', required='*')
    crane_breakdowns: float = INPUT(label='Crane breakdowns', type='NUMBER', group='wind_bos', required='*')
    access_road_entrances: float = INPUT(label='Access road entrances', type='NUMBER', group='wind_bos', required='*')
    turbine_capital_cost: float = INPUT(label='Turbine Capital Cost', units='$/kW', type='NUMBER', group='wind_bos', required='*')
    tower_top_mass: float = INPUT(label='Tower Top Mass', units='Tonnes', type='NUMBER', group='wind_bos', required='*')
    delivery_assist_required: float = INPUT(label='Delivery Assist Required', units='y/n', type='NUMBER', group='wind_bos', required='*', constraints='INTEGER')
    pad_mount_transformer_required: float = INPUT(label='Pad mount Transformer required', units='y/n', type='NUMBER', group='wind_bos', required='*', constraints='INTEGER')
    new_switchyard_required: float = INPUT(label='New Switchyard Required', units='y/n', type='NUMBER', group='wind_bos', required='*', constraints='INTEGER')
    rock_trenching_required: float = INPUT(label='Rock trenching required', units='%', type='NUMBER', group='wind_bos', required='*')
    mv_thermal_backfill: float = INPUT(label='MV thermal backfill', units='mi', type='NUMBER', group='wind_bos', required='*')
    mv_overhead_collector: float = INPUT(label='MV overhead collector', units='mi', type='NUMBER', group='wind_bos', required='*')
    performance_bond: float = INPUT(label='Performance bond', units='%', type='NUMBER', group='wind_bos', required='*')
    contingency: float = INPUT(label='Contingency', units='%', type='NUMBER', group='wind_bos', required='*')
    warranty_management: float = INPUT(label='Warranty management', units='%', type='NUMBER', group='wind_bos', required='*')
    sales_and_use_tax: float = INPUT(label='Sales and Use Tax', units='%', type='NUMBER', group='wind_bos', required='*')
    overhead: float = INPUT(label='Overhead', units='%', type='NUMBER', group='wind_bos', required='*')
    profit_margin: float = INPUT(label='Profit Margin', units='%', type='NUMBER', group='wind_bos', required='*')
    development_fee: float = INPUT(label='Development Fee', units='$M', type='NUMBER', group='wind_bos', required='*')
    turbine_transportation: float = INPUT(label='Turbine Transportation', units='mi', type='NUMBER', group='wind_bos', required='*')
    project_total_budgeted_cost: Final[float] = OUTPUT(label='Project Total Budgeted Cost', units='$s', type='NUMBER', group='wind_bos', required='*')
    transportation_cost: Final[float] = OUTPUT(label='Transportation Cost', units='$s', type='NUMBER', group='wind_bos', required='*')
    insurance_cost: Final[float] = OUTPUT(label='Insurance Cost', units='$s', type='NUMBER', group='wind_bos', required='*')
    engineering_cost: Final[float] = OUTPUT(label='Engineering Cost', units='$s', type='NUMBER', group='wind_bos', required='*')
    power_performance_cost: Final[float] = OUTPUT(label='Power Performance Cost', units='$s', type='NUMBER', group='wind_bos', required='*')
    site_compound_security_cost: Final[float] = OUTPUT(label='Site Compound & Security Cost', units='$s', type='NUMBER', group='wind_bos', required='*')
    building_cost: Final[float] = OUTPUT(label='Building Cost', units='$s', type='NUMBER', group='wind_bos', required='*')
    transmission_cost: Final[float] = OUTPUT(label='Transmission Cost', units='$s', type='NUMBER', group='wind_bos', required='*')
    markup_cost: Final[float] = OUTPUT(label='Markup Cost', units='$s', type='NUMBER', group='wind_bos', required='*')
    development_cost: Final[float] = OUTPUT(label='Development Cost', units='$s', type='NUMBER', group='wind_bos', required='*')
    access_roads_cost: Final[float] = OUTPUT(label='Access Roads Cost', units='$s', type='NUMBER', group='wind_bos', required='*')
    foundation_cost: Final[float] = OUTPUT(label='Foundation Cost', units='$s', type='NUMBER', group='wind_bos', required='*')
    erection_cost: Final[float] = OUTPUT(label='Turbine Erection Cost', units='$s', type='NUMBER', group='wind_bos', required='*')
    electrical_materials_cost: Final[float] = OUTPUT(label='MV Electrical Materials Cost', units='$s', type='NUMBER', group='wind_bos', required='*')
    electrical_installation_cost: Final[float] = OUTPUT(label='MV Electrical Installation Cost', units='$s', type='NUMBER', group='wind_bos', required='*')
    substation_cost: Final[float] = OUTPUT(label='Substation Cost', units='$s', type='NUMBER', group='wind_bos', required='*')
    project_mgmt_cost: Final[float] = OUTPUT(label='Project Management Cost', units='$s', type='NUMBER', group='wind_bos', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 machine_rating: float = ...,
                 rotor_diameter: float = ...,
                 hub_height: float = ...,
                 number_of_turbines: float = ...,
                 interconnect_voltage: float = ...,
                 distance_to_interconnect: float = ...,
                 site_terrain: float = ...,
                 turbine_layout: float = ...,
                 soil_condition: float = ...,
                 construction_time: float = ...,
                 om_building_size: float = ...,
                 quantity_test_met_towers: float = ...,
                 quantity_permanent_met_towers: float = ...,
                 weather_delay_days: float = ...,
                 crane_breakdowns: float = ...,
                 access_road_entrances: float = ...,
                 turbine_capital_cost: float = ...,
                 tower_top_mass: float = ...,
                 delivery_assist_required: float = ...,
                 pad_mount_transformer_required: float = ...,
                 new_switchyard_required: float = ...,
                 rock_trenching_required: float = ...,
                 mv_thermal_backfill: float = ...,
                 mv_overhead_collector: float = ...,
                 performance_bond: float = ...,
                 contingency: float = ...,
                 warranty_management: float = ...,
                 sales_and_use_tax: float = ...,
                 overhead: float = ...,
                 profit_margin: float = ...,
                 development_fee: float = ...,
                 turbine_transportation: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
