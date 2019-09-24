
# This is a generated file

"""iec61853interp - Determine single diode model parameters from IEC 61853 solution matrix at a given temperature and irradiance."""

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
        'input': Matrix,
        'param': Matrix,
        'I': float,
        'T': float,
        'a': float,
        'Il': float,
        'Io': float,
        'Rs': float,
        'Rsh': float
    }, total=False)

class Data(ssc.DataDict):
    input: Matrix = INPUT(label='IEC-61853 matrix test data', units='various', type='MATRIX', group='IEC61853', required='*', meta='[IRR,TC,PMP,VMP,VOC,ISC]')
    param: Matrix = INPUT(label='Parameter solution matrix', type='MATRIX', group='IEC61853', required='*', meta='[IL,IO,RS,RSH,A]')
    I: float = INPUT(label='Irradiance', units='W/m2', type='NUMBER', group='Single Diode Model', required='*')
    T: float = INPUT(label='Temperature', units='C', type='NUMBER', group='Single Diode Model', required='*')
    a: Final[float] = OUTPUT(label='Modified nonideality factor', units='1/V', type='NUMBER', group='Single Diode Model', required='*')
    Il: Final[float] = OUTPUT(label='Light current', units='A', type='NUMBER', group='Single Diode Model', required='*')
    Io: Final[float] = OUTPUT(label='Saturation current', units='A', type='NUMBER', group='Single Diode Model', required='*')
    Rs: Final[float] = OUTPUT(label='Series resistance', units='ohm', type='NUMBER', group='Single Diode Model', required='*')
    Rsh: Final[float] = OUTPUT(label='Shunt resistance', units='ohm', type='NUMBER', group='Single Diode Model', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 input: Matrix = ...,
                 param: Matrix = ...,
                 I: float = ...,
                 T: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
