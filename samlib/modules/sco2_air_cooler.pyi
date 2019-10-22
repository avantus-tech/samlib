
# This is a generated file

"""sco2_air_cooler - Returns air cooler dimensions given fluid and location design points"""

# VERSION: 0

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'T_amb': float,
        'q_dot_reject': float,
        'T_co2_hot_in': float,
        'P_co2_hot_in': float,
        'deltaP': float,
        'T_co2_cold_out': float,
        'W_dot_fan': float,
        'site_elevation': float,
        'd_tube_out': float,
        'd_tube_in': float,
        'depth_footprint': float,
        'width_footprint': float,
        'parallel_paths': float,
        'number_of_tubes': float,
        'length': float,
        'n_passes_series': float,
        'UA_total': float,
        'm_V_hx_material': float
}, total=False)

class Data(ssc.DataDict):
    T_amb: float = INPUT(label='Ambient temperature at design', units='C', type='NUMBER', required='*')
    q_dot_reject: float = INPUT(label='Heat rejected from CO2 stream', units='MWt', type='NUMBER', required='*')
    T_co2_hot_in: float = INPUT(label='Hot temperature of CO2 at inlet to cooler', units='C', type='NUMBER', required='*')
    P_co2_hot_in: float = INPUT(label='Pressure of CO2 at inlet to cooler', units='MPa', type='NUMBER', required='*')
    deltaP: float = INPUT(label='Pressure drop of CO2 through cooler', units='MPa', type='NUMBER', required='*')
    T_co2_cold_out: float = INPUT(label='Cold temperature of CO2 at cooler exit', units='C', type='NUMBER', required='*')
    W_dot_fan: float = INPUT(label='Air fan power', units='MWe', type='NUMBER', required='*')
    site_elevation: float = INPUT(label='Site elevation', units='m', type='NUMBER', required='*')
    d_tube_out: Final[float] = OUTPUT(label='CO2 tube outer diameter', units='cm', type='NUMBER', required='*')
    d_tube_in: Final[float] = OUTPUT(label='CO2 tube inner diameter', units='cm', type='NUMBER', required='*')
    depth_footprint: Final[float] = OUTPUT(label='Dimension of total air cooler in loop/air flow direction', units='m', type='NUMBER', required='*')
    width_footprint: Final[float] = OUTPUT(label='Dimension of total air cooler of parallel loops', units='m', type='NUMBER', required='*')
    parallel_paths: Final[float] = OUTPUT(label='Number of parallel flow paths', units='-', type='NUMBER', required='*')
    number_of_tubes: Final[float] = OUTPUT(label='Number of tubes (one pass)', units='-', type='NUMBER', required='*')
    length: Final[float] = OUTPUT(label='Length of tube (one pass)', units='m', type='NUMBER', required='*')
    n_passes_series: Final[float] = OUTPUT(label='Number of serial tubes in flow path', units='-', type='NUMBER', required='*')
    UA_total: Final[float] = OUTPUT(label='Total air-side conductance', units='kW/K', type='NUMBER', required='*')
    m_V_hx_material: Final[float] = OUTPUT(label='Total hx material volume - no headers', units='m^3', type='NUMBER', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 T_amb: float = ...,
                 q_dot_reject: float = ...,
                 T_co2_hot_in: float = ...,
                 P_co2_hot_in: float = ...,
                 deltaP: float = ...,
                 T_co2_cold_out: float = ...,
                 W_dot_fan: float = ...,
                 site_elevation: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
