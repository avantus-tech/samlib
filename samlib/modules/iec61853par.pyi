
# This is a generated file

"""iec61853par - Calculate 11-parameter single diode model parameters from IEC-61853 PV module test data."""

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
        'nser': float,
        'type': float,
        'verbose': float,
        'alphaIsc': float,
        'betaVoc': float,
        'gammaPmp': float,
        'n': float,
        'Il': float,
        'Io': float,
        'C1': float,
        'C2': float,
        'C3': float,
        'D1': float,
        'D2': float,
        'D3': float,
        'Egref': float
    }, total=False)

class Data(ssc.DataDict):
    input: Matrix = INPUT(label='IEC-61853 matrix test data', units='various', type='MATRIX', group='IEC61853', required='*', meta='[IRR,TC,PMP,VMP,VOC,ISC]')
    nser: float = INPUT(label='Number of cells in series', type='NUMBER', group='IEC61853', required='*')
    type: float = INPUT(label='Cell technology type', units='0..5', type='NUMBER', group='IEC61853', required='*', meta='monoSi,multiSi/polySi,cdte,cis,cigs,amorphous')
    verbose: float = INPUT(label='Output solver messages', units='0/1', type='NUMBER', group='IEC61853', required='*')
    alphaIsc: Final[float] = OUTPUT(label='SC temp coefficient @ STC', units='A/C', type='NUMBER', group='IEC61853', required='*')
    betaVoc: Final[float] = OUTPUT(label='OC temp coefficient @ STC', units='V/C', type='NUMBER', group='IEC61853', required='*')
    gammaPmp: Final[float] = OUTPUT(label='MP temp coefficient @ STC', units='%/C', type='NUMBER', group='IEC61853', required='*')
    n: Final[float] = OUTPUT(label='Diode factor', type='NUMBER', group='IEC61853', required='*')
    Il: Final[float] = OUTPUT(label='Light current', units='A', type='NUMBER', group='IEC61853', required='*')
    Io: Final[float] = OUTPUT(label='Saturation current', units='A', type='NUMBER', group='IEC61853', required='*')
    C1: Final[float] = OUTPUT(label='Rsh fitting C1', type='NUMBER', group='IEC61853', required='*')
    C2: Final[float] = OUTPUT(label='Rsh fitting C2', type='NUMBER', group='IEC61853', required='*')
    C3: Final[float] = OUTPUT(label='Rsh fitting C3', type='NUMBER', group='IEC61853', required='*')
    D1: Final[float] = OUTPUT(label='Rs fitting D1', type='NUMBER', group='IEC61853', required='*')
    D2: Final[float] = OUTPUT(label='Rs fitting D2', type='NUMBER', group='IEC61853', required='*')
    D3: Final[float] = OUTPUT(label='Rs fitting D3', type='NUMBER', group='IEC61853', required='*')
    Egref: Final[float] = OUTPUT(label='Bandgap voltage', units='eV', type='NUMBER', group='IEC61853', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 input: Matrix = ...,
                 nser: float = ...,
                 type: float = ...,
                 verbose: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
