
# This is a generated file

"""singlediodeparams - Single diode model parameter calculation."""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'I': float,
        'T': float,
        'alpha_isc': float,
        'Adj_ref': float,
        'a_ref': float,
        'Il_ref': float,
        'Io_ref': float,
        'Rs_ref': float,
        'Rsh_ref': float,
        'a': float,
        'Il': float,
        'Io': float,
        'Rs': float,
        'Rsh': float
}, total=False)

class Data(ssc.DataDict):
    I: float = INPUT(label='Irradiance', units='W/m2', type='NUMBER', group='Single Diode Model', required='*')
    T: float = INPUT(label='Temperature', units='C', type='NUMBER', group='Single Diode Model', required='*')
    alpha_isc: float = INPUT(label='Temp coeff of current at SC', units="A/'C", type='NUMBER', group='Single Diode Model', required='*')
    Adj_ref: float = INPUT(label='OC SC temp coeff adjustment', units='%', type='NUMBER', group='Single Diode Model', required='*')
    a_ref: float = INPUT(label='Modified nonideality factor', units='1/V', type='NUMBER', group='Single Diode Model', required='*')
    Il_ref: float = INPUT(label='Light current', units='A', type='NUMBER', group='Single Diode Model', required='*')
    Io_ref: float = INPUT(label='Saturation current', units='A', type='NUMBER', group='Single Diode Model', required='*')
    Rs_ref: float = INPUT(label='Series resistance', units='ohm', type='NUMBER', group='Single Diode Model', required='*')
    Rsh_ref: float = INPUT(label='Shunt resistance', units='ohm', type='NUMBER', group='Single Diode Model', required='*')
    a: Final[float] = OUTPUT(label='Modified nonideality factor', units='1/V', type='NUMBER', group='Single Diode Model', required='*')
    Il: Final[float] = OUTPUT(label='Light current', units='A', type='NUMBER', group='Single Diode Model', required='*')
    Io: Final[float] = OUTPUT(label='Saturation current', units='A', type='NUMBER', group='Single Diode Model', required='*')
    Rs: Final[float] = OUTPUT(label='Series resistance', units='ohm', type='NUMBER', group='Single Diode Model', required='*')
    Rsh: Final[float] = OUTPUT(label='Shunt resistance', units='ohm', type='NUMBER', group='Single Diode Model', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 I: float = ...,
                 T: float = ...,
                 alpha_isc: float = ...,
                 Adj_ref: float = ...,
                 a_ref: float = ...,
                 Il_ref: float = ...,
                 Io_ref: float = ...,
                 Rs_ref: float = ...,
                 Rsh_ref: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
