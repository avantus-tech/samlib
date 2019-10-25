
# This is a generated file

"""windcsm - WISDEM turbine cost model"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'turbine_class': float,
        'turbine_user_exponent': float,
        'turbine_carbon_blades': float,
        'turbine_rotor_diameter': float,
        'machine_rating': float,
        'rotor_torque': float,
        'onboard_crane': float,
        'hub_height': float,
        'num_blades': float,
        'num_bearings': float,
        'rotor_mass': float,
        'rotor_cost': float,
        'blade_cost': float,
        'hub_cost': float,
        'pitch_cost': float,
        'spinner_cost': float,
        'drivetrain_mass': float,
        'drivetrain_cost': float,
        'low_speed_side_cost': float,
        'main_bearings_cost': float,
        'gearbox_cost': float,
        'high_speed_side_cost': float,
        'generator_cost': float,
        'bedplate_cost': float,
        'yaw_system_cost': float,
        'variable_speed_electronics_cost': float,
        'hvac_cost': float,
        'electrical_connections_cost': float,
        'controls_cost': float,
        'mainframe_cost': float,
        'transformer_cost': float,
        'tower_mass': float,
        'tower_cost': float,
        'turbine_cost': float
}, total=False)

class Data(ssc.DataDict):
    turbine_class: float = INPUT(label='Turbine class', type='NUMBER', group='wind_csm', required='?=0', constraints='INTEGER,MIN=0,MAX=3')
    turbine_user_exponent: float = INPUT(label='Turbine user exponent', type='NUMBER', group='wind_csm', required='?=2.5')
    turbine_carbon_blades: float = INPUT(label='Turbine carbon blades', units='0/1', type='NUMBER', group='wind_csm', required='?=0', constraints='INTEGER,MIN=0,MAX=1')
    turbine_rotor_diameter: float = INPUT(label='Turbine rotor diameter', units='m', type='NUMBER', group='wind_csm', required='*')
    machine_rating: float = INPUT(label='Machine rating', units='kW', type='NUMBER', group='wind_csm', required='*')
    rotor_torque: float = INPUT(label='Rotor torque', units='Nm', type='NUMBER', group='wind_csm', required='*')
    onboard_crane: float = INPUT(label='Onboard crane', units='0/1', type='NUMBER', group='wind_csm', required='?=0', constraints='INTEGER,MIN=0,MAX=1')
    hub_height: float = INPUT(label='Hub height', units='m', type='NUMBER', group='wind_csm', required='*')
    num_blades: float = INPUT(label='Number of blades', type='NUMBER', group='wind_csm', required='?=3', constraints='INTEGER,MIN=1')
    num_bearings: float = INPUT(label='Number of main bearings', type='NUMBER', group='wind_csm', required='?=2', constraints='INTEGER,MIN=1')
    rotor_mass: Final[float] = OUTPUT(label='Rotor mass', units='kg', type='NUMBER', group='wind_csm', required='*')
    rotor_cost: Final[float] = OUTPUT(label='Rotor cost', units='$', type='NUMBER', group='wind_csm', required='*')
    blade_cost: Final[float] = OUTPUT(label='Rotor cost', units='$', type='NUMBER', group='wind_csm', required='*')
    hub_cost: Final[float] = OUTPUT(label='Hub cost', units='$', type='NUMBER', group='wind_csm', required='*')
    pitch_cost: Final[float] = OUTPUT(label='Pitch cost', units='$', type='NUMBER', group='wind_csm', required='*')
    spinner_cost: Final[float] = OUTPUT(label='Spinner cost', units='$', type='NUMBER', group='wind_csm', required='*')
    drivetrain_mass: Final[float] = OUTPUT(label='Drivetrain mass', units='kg', type='NUMBER', group='wind_csm', required='*')
    drivetrain_cost: Final[float] = OUTPUT(label='Drivetrain cost', units='$', type='NUMBER', group='wind_csm', required='*')
    low_speed_side_cost: Final[float] = OUTPUT(label='Low speed side cost', units='$', type='NUMBER', group='wind_csm', required='*')
    main_bearings_cost: Final[float] = OUTPUT(label='Main bearings cost', units='$', type='NUMBER', group='wind_csm', required='*')
    gearbox_cost: Final[float] = OUTPUT(label='Gearbox cost', units='$', type='NUMBER', group='wind_csm', required='*')
    high_speed_side_cost: Final[float] = OUTPUT(label='High speed side cost', units='$', type='NUMBER', group='wind_csm', required='*')
    generator_cost: Final[float] = OUTPUT(label='Generator cost', units='$', type='NUMBER', group='wind_csm', required='*')
    bedplate_cost: Final[float] = OUTPUT(label='Bedplate cost', units='$', type='NUMBER', group='wind_csm', required='*')
    yaw_system_cost: Final[float] = OUTPUT(label='Yaw system cost', units='$', type='NUMBER', group='wind_csm', required='*')
    variable_speed_electronics_cost: Final[float] = OUTPUT(label='Variable speed electronics cost', units='$', type='NUMBER', group='wind_csm', required='*')
    hvac_cost: Final[float] = OUTPUT(label='HVAC cost', units='$', type='NUMBER', group='wind_csm', required='*')
    electrical_connections_cost: Final[float] = OUTPUT(label='Electrical connections cost', units='$', type='NUMBER', group='wind_csm', required='*')
    controls_cost: Final[float] = OUTPUT(label='Controls cost', units='$', type='NUMBER', group='wind_csm', required='*')
    mainframe_cost: Final[float] = OUTPUT(label='Mainframe cost', units='$', type='NUMBER', group='wind_csm', required='*')
    transformer_cost: Final[float] = OUTPUT(label='Transformer cost', units='$', type='NUMBER', group='wind_csm', required='*')
    tower_mass: Final[float] = OUTPUT(label='Tower mass', units='kg', type='NUMBER', group='wind_csm', required='*')
    tower_cost: Final[float] = OUTPUT(label='Tower cost', units='$', type='NUMBER', group='wind_csm', required='*')
    turbine_cost: Final[float] = OUTPUT(label='Turbine cost', units='$', type='NUMBER', group='wind_csm', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 turbine_class: float = ...,
                 turbine_user_exponent: float = ...,
                 turbine_carbon_blades: float = ...,
                 turbine_rotor_diameter: float = ...,
                 machine_rating: float = ...,
                 rotor_torque: float = ...,
                 onboard_crane: float = ...,
                 hub_height: float = ...,
                 num_blades: float = ...,
                 num_bearings: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
