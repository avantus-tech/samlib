
# This is a generated file

"""6parsolve - Solver for CEC/6 parameter PV module coefficients"""

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
        'celltype': str,
        'Vmp': float,
        'Imp': float,
        'Voc': float,
        'Isc': float,
        'alpha_isc': float,
        'beta_voc': float,
        'gamma_pmp': float,
        'Nser': float,
        'Tref': float,
        'a': float,
        'Il': float,
        'Io': float,
        'Rs': float,
        'Rsh': float,
        'Adj': float
    }, total=False)

class Data(ssc.DataDict):
    celltype: str = INPUT(label='Cell technology type', units='monoSi,multiSi/polySi,cis,cigs,cdte,amorphous', type='STRING', group='6 Parameter Solver', required='*')
    Vmp: float = INPUT(label='Maximum power point voltage', units='V', type='NUMBER', group='6 Parameter Solver', required='*')
    Imp: float = INPUT(label='Maximum power point current', units='A', type='NUMBER', group='6 Parameter Solver', required='*')
    Voc: float = INPUT(label='Open circuit voltage', units='V', type='NUMBER', group='6 Parameter Solver', required='*')
    Isc: float = INPUT(label='Short circuit current', units='A', type='NUMBER', group='6 Parameter Solver', required='*')
    alpha_isc: float = INPUT(label='Temp coeff of current at SC', units="A/'C", type='NUMBER', group='6 Parameter Solver', required='*')
    beta_voc: float = INPUT(label='Temp coeff of voltage at OC', units="V/'C", type='NUMBER', group='6 Parameter Solver', required='*')
    gamma_pmp: float = INPUT(label='Temp coeff of power at MP', units="%/'C", type='NUMBER', group='6 Parameter Solver', required='*')
    Nser: float = INPUT(label='Number of cells in series', type='NUMBER', group='6 Parameter Solver', required='*', constraints='INTEGER,POSITIVE')
    Tref: float = INPUT(label='Reference cell temperature', units="'C", type='NUMBER', group='6 Parameter Solver', required='?')
    a: Final[float] = OUTPUT(label='Modified nonideality factor', units='1/V', type='NUMBER', group='6 Parameter Solver', required='*')
    Il: Final[float] = OUTPUT(label='Light current', units='A', type='NUMBER', group='6 Parameter Solver', required='*')
    Io: Final[float] = OUTPUT(label='Saturation current', units='A', type='NUMBER', group='6 Parameter Solver', required='*')
    Rs: Final[float] = OUTPUT(label='Series resistance', units='ohm', type='NUMBER', group='6 Parameter Solver', required='*')
    Rsh: Final[float] = OUTPUT(label='Shunt resistance', units='ohm', type='NUMBER', group='6 Parameter Solver', required='*')
    Adj: Final[float] = OUTPUT(label='OC SC temp coeff adjustment', units='%', type='NUMBER', group='6 Parameter Solver', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 celltype: str = ...,
                 Vmp: float = ...,
                 Imp: float = ...,
                 Voc: float = ...,
                 Isc: float = ...,
                 alpha_isc: float = ...,
                 beta_voc: float = ...,
                 gamma_pmp: float = ...,
                 Nser: float = ...,
                 Tref: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
