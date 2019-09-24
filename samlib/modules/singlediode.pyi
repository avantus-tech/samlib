
# This is a generated file

"""singlediode - Single diode model function."""

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
        'a': float,
        'Il': float,
        'Io': float,
        'Rs': float,
        'Rsh': float,
        'Vop': float,
        'V': float,
        'I': float,
        'Voc': float,
        'Isc': float
    }, total=False)

class Data(ssc.DataDict):
    a: float = INPUT(label='Modified nonideality factor', units='1/V', type='NUMBER', group='Single Diode Model', required='*')
    Il: float = INPUT(label='Light current', units='A', type='NUMBER', group='Single Diode Model', required='*')
    Io: float = INPUT(label='Saturation current', units='A', type='NUMBER', group='Single Diode Model', required='*')
    Rs: float = INPUT(label='Series resistance', units='ohm', type='NUMBER', group='Single Diode Model', required='*')
    Rsh: float = INPUT(label='Shunt resistance', units='ohm', type='NUMBER', group='Single Diode Model', required='*')
    Vop: float = INPUT(label='Module operating voltage', units='V', type='NUMBER', group='Single Diode Model', required='?')
    V: Final[float] = OUTPUT(label='Output voltage', units='V', type='NUMBER', group='Single Diode Model', required='*')
    I: Final[float] = OUTPUT(label='Output current', units='A', type='NUMBER', group='Single Diode Model', required='*')
    Voc: Final[float] = OUTPUT(label='Open circuit voltage', units='V', type='NUMBER', group='Single Diode Model', required='*')
    Isc: Final[float] = OUTPUT(label='Short circuit current', units='A', type='NUMBER', group='Single Diode Model', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 a: float = ...,
                 Il: float = ...,
                 Io: float = ...,
                 Rs: float = ...,
                 Rsh: float = ...,
                 Vop: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
