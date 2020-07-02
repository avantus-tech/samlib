
# This is a generated file

"""mhk_wave - MHK Wave power calculation model using power distribution."""

# VERSION: 3

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'wave_resource_matrix': Matrix,
        'wave_power_matrix': Matrix,
        'number_devices': float,
        'system_capacity': float,
        'device_rated_power': float,
        'loss_array_spacing': float,
        'loss_resource_overprediction': float,
        'loss_transmission': float,
        'loss_downtime': float,
        'loss_additional': float,
        'device_average_power': float,
        'annual_energy': float,
        'capacity_factor': float,
        'annual_energy_distribution': Matrix
}, total=False)

class Data(ssc.DataDict):
    wave_resource_matrix: Matrix = INPUT(label='Frequency distribution of wave resource as a function of Hs and Te', type='MATRIX', group='MHKWave', required='*')
    wave_power_matrix: Matrix = INPUT(label='Wave Power Matrix', type='MATRIX', group='MHKWave', required='*')
    number_devices: float = INPUT(label='Number of wave devices in the system', type='NUMBER', group='MHKWave', required='?=1', constraints='INTEGER')
    system_capacity: float = INPUT(label='System Nameplate Capacity', units='kW', type='NUMBER', group='MHKWave', required='?=0')
    device_rated_power: float = INPUT(label='Rated capacity of device', units='kW', type='NUMBER', group='MHKWave', required='*')
    loss_array_spacing: float = INPUT(label='Array spacing loss', units='%', type='NUMBER', group='MHKWave', required='*')
    loss_resource_overprediction: float = INPUT(label='Resource overprediction loss', units='%', type='NUMBER', group='MHKWave', required='*')
    loss_transmission: float = INPUT(label='Transmission losses', units='%', type='NUMBER', group='MHKWave', required='*')
    loss_downtime: float = INPUT(label='Array/WEC downtime loss', units='%', type='NUMBER', group='MHKWave', required='*')
    loss_additional: float = INPUT(label='Additional losses', units='%', type='NUMBER', group='MHKWave', required='*')
    device_average_power: Final[float] = OUTPUT(label='Average power production of a single device', units='kW', type='NUMBER', group='MHKWave', required='*')
    annual_energy: Final[float] = OUTPUT(label='Annual energy production of array', units='kWh', type='NUMBER', group='MHKWave', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity Factor', units='%', type='NUMBER', group='MHKWave', required='*')
    annual_energy_distribution: Final[Matrix] = OUTPUT(label='Annual energy production as function of Hs and Te', type='MATRIX', group='MHKWave', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 wave_resource_matrix: Matrix = ...,
                 wave_power_matrix: Matrix = ...,
                 number_devices: float = ...,
                 system_capacity: float = ...,
                 device_rated_power: float = ...,
                 loss_array_spacing: float = ...,
                 loss_resource_overprediction: float = ...,
                 loss_transmission: float = ...,
                 loss_downtime: float = ...,
                 loss_additional: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
