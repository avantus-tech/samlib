
# This is a generated file

"""iscc_design_point - Calculates design point inject, extraction, fossil output"""

# VERSION: 0

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'ngcc_model': float,
        'q_pb_design': float,
        'pinch_point_cold': float,
        'pinch_point_hot': float,
        'elev': float,
        'HTF_code': float,
        'field_fl_props': Matrix,
        'W_dot_fossil': float,
        'T_st_inject': float,
        'q_solar_max': float,
        'T_htf_cold': float,
        'W_dot_solar': float
}, total=False)

class Data(ssc.DataDict):
    ngcc_model: float = INPUT(label='1: NREL, 2: GE', type='NUMBER', required='*')
    q_pb_design: float = INPUT(label='Design point power block thermal power', units='MWt', type='NUMBER', required='*')
    pinch_point_cold: float = INPUT(label='Cold side pinch point', units='C', type='NUMBER', required='*')
    pinch_point_hot: float = INPUT(label='Hot side pinch point', units='C', type='NUMBER', required='*')
    elev: float = INPUT(label='Plant elevation', units='m', type='NUMBER', required='*')
    HTF_code: float = INPUT(label='HTF fluid code', units='-', type='NUMBER', required='*')
    field_fl_props: Matrix = INPUT(label='User defined field fluid property data', units='-', type='MATRIX', required='*', meta='7 columns (T,Cp,dens,visc,kvisc,cond,h), at least 3 rows')
    W_dot_fossil: Final[float] = OUTPUT(label='Electric output with no solar contribution', units='MWe', type='NUMBER', required='*')
    T_st_inject: Final[float] = OUTPUT(label='Steam injection temp into HRSG', units='C', type='NUMBER', required='*')
    q_solar_max: Final[float] = OUTPUT(label='Max. solar thermal input at design', units='MWt', type='NUMBER', required='*')
    T_htf_cold: Final[float] = OUTPUT(label='HTF return temp from HRSG', units='C', type='NUMBER', required='*')
    W_dot_solar: Final[float] = OUTPUT(label='Solar contribution to hybrid output', units='MWe', type='NUMBER', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 ngcc_model: float = ...,
                 q_pb_design: float = ...,
                 pinch_point_cold: float = ...,
                 pinch_point_hot: float = ...,
                 elev: float = ...,
                 HTF_code: float = ...,
                 field_fl_props: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
