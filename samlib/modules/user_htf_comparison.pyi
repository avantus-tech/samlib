
# This is a generated file

"""user_htf_comparison - Evaluates equivalence of two user-defined HTF tables"""

# VERSION: 0

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'HTF_code1': float,
        'fl_props1': Matrix,
        'HTF_code2': float,
        'fl_props2': Matrix,
        'are_equal': float
}, total=False)

class Data(ssc.DataDict):
    HTF_code1: float = INPUT(label='HTF fluid code: Fluid 1', units='-', type='NUMBER', required='*')
    fl_props1: Matrix = INPUT(label='User defined field fluid property data, Fluid 1', units='-', type='MATRIX', required='*', meta='7 columns (T,Cp,dens,visc,kvisc,cond,h), at least 3 rows')
    HTF_code2: float = INPUT(label='HTF fluid code: Fluid 2', units='-', type='NUMBER', required='*')
    fl_props2: Matrix = INPUT(label='User defined field fluid property data, Fluid 2', units='-', type='MATRIX', required='*', meta='7 columns (T,Cp,dens,visc,kvisc,cond,h), at least 3 rows')
    are_equal: Final[float] = OUTPUT(label='1: Input tables are equal, 0: not equal', units='-', type='NUMBER', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 HTF_code1: float = ...,
                 fl_props1: Matrix = ...,
                 HTF_code2: float = ...,
                 fl_props2: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
