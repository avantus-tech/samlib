
# This is a generated file

"""ui_udpc_checks - Calculates the levels and number of paramteric runs for 3 udpc ind variables"""

# VERSION: 0

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'ud_ind_od': Matrix,
        'n_T_htf_pars': float,
        'T_htf_low': float,
        'T_htf_des': float,
        'T_htf_high': float,
        'n_T_amb_pars': float,
        'T_amb_low': float,
        'T_amb_des': float,
        'T_amb_high': float,
        'n_m_dot_pars': float,
        'm_dot_low': float,
        'm_dot_des': float,
        'm_dot_high': float
}, total=False)

class Data(ssc.DataDict):
    ud_ind_od: Matrix = INPUT(label='Off design user-defined power cycle performance as function of T_htf, m_dot_htf [ND], and T_amb', type='MATRIX', group='User Defined Power Cycle', required='?=[[0]]')
    n_T_htf_pars: Final[float] = OUTPUT(label='Number of HTF parametrics', units='-', type='NUMBER', required='*')
    T_htf_low: Final[float] = OUTPUT(label='HTF low temperature', units='C', type='NUMBER', required='*')
    T_htf_des: Final[float] = OUTPUT(label='HTF design temperature', units='C', type='NUMBER', required='*')
    T_htf_high: Final[float] = OUTPUT(label='HTF high temperature', units='C', type='NUMBER', required='*')
    n_T_amb_pars: Final[float] = OUTPUT(label='Number of ambient temperature parametrics', units='-', type='NUMBER', required='*')
    T_amb_low: Final[float] = OUTPUT(label='Low ambient temperature', units='C', type='NUMBER', required='*')
    T_amb_des: Final[float] = OUTPUT(label='Design ambient temperature', units='C', type='NUMBER', required='*')
    T_amb_high: Final[float] = OUTPUT(label='High ambient temperature', units='C', type='NUMBER', required='*')
    n_m_dot_pars: Final[float] = OUTPUT(label='Number of HTF mass flow parametrics', units='-', type='NUMBER', required='*')
    m_dot_low: Final[float] = OUTPUT(label='Low ambient temperature', units='C', type='NUMBER', required='*')
    m_dot_des: Final[float] = OUTPUT(label='Design ambient temperature', units='C', type='NUMBER', required='*')
    m_dot_high: Final[float] = OUTPUT(label='High ambient temperature', units='C', type='NUMBER', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 ud_ind_od: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
