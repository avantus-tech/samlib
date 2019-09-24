
# This is a generated file

"""windpower - Utility scale wind farm model (adapted from TRNSYS code by P.Quinlan and openWind software by AWS Truepower)"""

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
        'wind_resource_filename': str,
        'wind_resource_data': Table,
        'wind_resource_shear': float,
        'wind_resource_turbulence_coeff': float,
        'system_capacity': float,
        'wind_resource_model_choice': float,
        'weibull_reference_height': float,
        'weibull_k_factor': float,
        'weibull_wind_speed': float,
        'wind_turbine_rotor_diameter': float,
        'wind_turbine_powercurve_windspeeds': Array,
        'wind_turbine_powercurve_powerout': Array,
        'wind_turbine_hub_ht': float,
        'wind_turbine_max_cp': float,
        'wind_farm_xCoordinates': Array,
        'wind_farm_yCoordinates': Array,
        'wind_farm_losses_percent': float,
        'wind_farm_wake_model': float,
        'en_low_temp_cutoff': float,
        'low_temp_cutoff': float,
        'en_icing_cutoff': float,
        'icing_cutoff_temp': float,
        'icing_cutoff_rh': float,
        'turbine_output_by_windspeed_bin': Array,
        'wind_direction': Array,
        'wind_speed': Array,
        'temp': Array,
        'pressure': Array,
        'gen': Array,
        'monthly_energy': Array,
        'annual_energy': float,
        'capacity_factor': float,
        'kwh_per_kw': float,
        'cutoff_losses': float,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix
    }, total=False)

class Data(ssc.DataDict):
    wind_resource_filename: str = INPUT(label='local wind data file path', type='STRING', group='WindPower', required='?', constraints='LOCAL_FILE')
    wind_resource_data: Table = INPUT(label='wind resouce data in memory', type='TABLE', group='WindPower', required='?')
    wind_resource_shear: float = INPUT(label='Shear exponent', type='NUMBER', group='WindPower', required='*', constraints='MIN=0')
    wind_resource_turbulence_coeff: float = INPUT(label='Turbulence coefficient', units='%', type='NUMBER', group='WindPower', required='*', constraints='MIN=0')
    system_capacity: float = INPUT(label='Nameplate capacity', units='kW', type='NUMBER', group='WindPower', required='*', constraints='MIN=0')
    wind_resource_model_choice: float = INPUT(label='Hourly or Weibull model', units='0/1', type='NUMBER', group='WindPower', required='*', constraints='INTEGER')
    weibull_reference_height: float = INPUT(label='Reference height for Weibull wind speed', units='m', type='NUMBER', group='WindPower', required='?=50', constraints='MIN=0')
    weibull_k_factor: float = INPUT(label='Weibull K factor for wind resource', type='NUMBER', group='WindPower', required='wind_resource_model_choice=1')
    weibull_wind_speed: float = INPUT(label='Average wind speed for Weibull model', type='NUMBER', group='WindPower', required='wind_resource_model_choice=1', constraints='MIN=0')
    wind_turbine_rotor_diameter: float = INPUT(label='Rotor diameter', units='m', type='NUMBER', group='WindPower', required='*', constraints='POSITIVE')
    wind_turbine_powercurve_windspeeds: Array = INOUT(label='Power curve wind speed array', units='m/s', type='ARRAY', group='WindPower', required='*')
    wind_turbine_powercurve_powerout: Array = INOUT(label='Power curve turbine output array', units='kW', type='ARRAY', group='WindPower', required='*', constraints='LENGTH_EQUAL=wind_turbine_powercurve_windspeeds')
    wind_turbine_hub_ht: float = INPUT(label='Hub height', units='m', type='NUMBER', group='WindPower', required='*', constraints='POSITIVE')
    wind_turbine_max_cp: float = INPUT(label='Max cp', type='NUMBER', group='WindPower', required='wind_resource_model_choice=1', constraints='MIN=0')
    wind_farm_xCoordinates: Array = INPUT(label='Turbine X coordinates', units='m', type='ARRAY', group='WindPower', required='*')
    wind_farm_yCoordinates: Array = INPUT(label='Turbine Y coordinates', units='m', type='ARRAY', group='WindPower', required='*', constraints='LENGTH_EQUAL=wind_farm_xCoordinates')
    wind_farm_losses_percent: float = INPUT(label='Percentage losses', units='%', type='NUMBER', group='WindPower', required='*')
    wind_farm_wake_model: float = INPUT(label='Wake Model', units='0/1/2', type='NUMBER', group='WindPower', required='*', constraints='INTEGER')
    en_low_temp_cutoff: float = INPUT(label='Enable Low Temperature Cutoff', units='0/1', type='NUMBER', group='WindPower', required='?=0', constraints='INTEGER')
    low_temp_cutoff: float = INPUT(label='Low Temperature Cutoff', units='C', type='NUMBER', group='WindPower', required='en_low_temp_cutoff=1')
    en_icing_cutoff: float = INPUT(label='Enable Icing Cutoff', units='0/1', type='NUMBER', group='WindPower', required='?=0', constraints='INTEGER')
    icing_cutoff_temp: float = INPUT(label='Icing Cutoff Temperature', units='C', type='NUMBER', group='WindPower', required='en_icing_cutoff=1')
    icing_cutoff_rh: float = INPUT(label='Icing Cutoff Relative Humidity', units='%', type='NUMBER', group='WindPower', required='en_icing_cutoff=1', constraints='MIN=0')
    turbine_output_by_windspeed_bin: Final[Array] = OUTPUT(label='Turbine output by wind speed bin', units='kW', type='ARRAY', group='Power Curve', constraints='LENGTH_EQUAL=wind_turbine_powercurve_windspeeds')
    wind_direction: Final[Array] = OUTPUT(label='Wind direction', units='deg', type='ARRAY', group='Time Series', required='wind_resource_model_choice=0')
    wind_speed: Final[Array] = OUTPUT(label='Wind speed', units='m/s', type='ARRAY', group='Time Series', required='wind_resource_model_choice=0')
    temp: Final[Array] = OUTPUT(label='Air temperature', units="'C", type='ARRAY', group='Time Series', required='wind_resource_model_choice=0')
    pressure: Final[Array] = OUTPUT(label='Pressure', units='atm', type='ARRAY', group='Time Series', required='wind_resource_model_choice=0')
    gen: Final[Array] = OUTPUT(label='Total electric power to grid', units='kWh', type='ARRAY', group='(Sub)Hourly', required='*')
    monthly_energy: Final[Array] = OUTPUT(label='Monthly Energy', units='kWh', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    annual_energy: Final[float] = OUTPUT(label='Annual Energy', units='kWh', type='NUMBER', group='Annual', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', group='Annual', required='*')
    kwh_per_kw: Final[float] = OUTPUT(label='First year kWh/kW', units='kWh/kW', type='NUMBER', group='Annual', required='*')
    cutoff_losses: Final[float] = OUTPUT(label='Cutoff losses', units='%', type='NUMBER', group='Annual')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')

    def __init__(self, *args: Mapping[str, Any],
                 wind_resource_filename: str = ...,
                 wind_resource_data: Table = ...,
                 wind_resource_shear: float = ...,
                 wind_resource_turbulence_coeff: float = ...,
                 system_capacity: float = ...,
                 wind_resource_model_choice: float = ...,
                 weibull_reference_height: float = ...,
                 weibull_k_factor: float = ...,
                 weibull_wind_speed: float = ...,
                 wind_turbine_rotor_diameter: float = ...,
                 wind_turbine_powercurve_windspeeds: Array = ...,
                 wind_turbine_powercurve_powerout: Array = ...,
                 wind_turbine_hub_ht: float = ...,
                 wind_turbine_max_cp: float = ...,
                 wind_farm_xCoordinates: Array = ...,
                 wind_farm_yCoordinates: Array = ...,
                 wind_farm_losses_percent: float = ...,
                 wind_farm_wake_model: float = ...,
                 en_low_temp_cutoff: float = ...,
                 low_temp_cutoff: float = ...,
                 en_icing_cutoff: float = ...,
                 icing_cutoff_temp: float = ...,
                 icing_cutoff_rh: float = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
