
# This is a generated file

"""mhk_tidal - MHK Tidal power calculation model using power distribution."""

# VERSION: 3

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'tidal_resource': Matrix,
        'tidal_power_curve': Matrix,
        'number_devices': float,
        'loss_array_spacing': float,
        'loss_resource_overprediction': float,
        'loss_transmission': float,
        'loss_downtime': float,
        'loss_additional': float,
        'device_rated_capacity': float,
        'device_average_power': float,
        'annual_energy': float,
        'capacity_factor': float,
        'annual_energy_distribution': Array,
        'annual_cumulative_energy_distribution': Array
}, total=False)

class Data(ssc.DataDict):
    tidal_resource: Matrix = INPUT(label='Frequency distribution of resource as a function of stream speeds', type='MATRIX', group='MHKTidal', required='*')
    tidal_power_curve: Matrix = INPUT(label='Power curve of tidal energy device as function of stream speeds', units='kW', type='MATRIX', group='MHKTidal', required='*')
    number_devices: float = INPUT(label='Number of tidal devices in the system', type='NUMBER', group='MHKTidal', required='?=1', constraints='INTEGER')
    loss_array_spacing: float = INPUT(label='Array spacing loss', units='%', type='NUMBER', group='MHKTidal', required='*')
    loss_resource_overprediction: float = INPUT(label='Resource overprediction loss', units='%', type='NUMBER', group='MHKTidal', required='*')
    loss_transmission: float = INPUT(label='Transmission losses', units='%', type='NUMBER', group='MHKTidal', required='*')
    loss_downtime: float = INPUT(label='Array/WEC downtime loss', units='%', type='NUMBER', group='MHKTidal', required='*')
    loss_additional: float = INPUT(label='Additional losses', units='%', type='NUMBER', group='MHKTidal', required='*')
    device_rated_capacity: Final[float] = OUTPUT(label='Rated capacity of device', units='kW', type='NUMBER', group='MHKTidal')
    device_average_power: Final[float] = OUTPUT(label='Average power production of a single device', units='kW', type='NUMBER', group='MHKTidal', required='*')
    annual_energy: Final[float] = OUTPUT(label='Annual energy production of array', units='kWh', type='NUMBER', group='MHKTidal', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity Factor of array', units='%', type='NUMBER', group='MHKTidal', required='*')
    annual_energy_distribution: Final[Array] = OUTPUT(label='Annual energy production of array as function of speed', units='kWh', type='ARRAY', group='MHKTidal', required='*')
    annual_cumulative_energy_distribution: Final[Array] = OUTPUT(label='Cumulative annual energy production of array as function of speed', units='kWh', type='ARRAY', group='MHKTidal', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 tidal_resource: Matrix = ...,
                 tidal_power_curve: Matrix = ...,
                 number_devices: float = ...,
                 loss_array_spacing: float = ...,
                 loss_resource_overprediction: float = ...,
                 loss_transmission: float = ...,
                 loss_downtime: float = ...,
                 loss_additional: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
