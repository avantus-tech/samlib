
# This is a generated file

"""sco2_design_cycle - Calls sCO2 auto-design cycle function"""

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
        'I_W_dot_net_des': float,
        'I_T_mc_in_des': float,
        'I_T_t_in_des': float,
        'I_N_t_des': float,
        'I_eta_mc': float,
        'I_eta_rc': float,
        'I_eta_t': float,
        'I_tol': float,
        'I_opt_tol': float,
        'I_UA_total_des': float,
        'I_P_high_limit': float,
        'O_LT_frac_des': float,
        'O_P_mc_out_des': float,
        'O_PR_mc_des': float,
        'O_recomp_frac_des': float,
        'O_eta_thermal_des': float,
        'O_N_mc_des': float,
        'O_m_dot_PHX': float,
        'O_T_array_des': Array
    }, total=False)

class Data(ssc.DataDict):
    I_W_dot_net_des: float = INPUT(label='Design cycle power output', units='MW', type='NUMBER', group='sCO2 power cycle', required='*')
    I_T_mc_in_des: float = INPUT(label='Main compressor inlet temp at design', units='C', type='NUMBER', group='sCO2 power cycle', required='*')
    I_T_t_in_des: float = INPUT(label='Turbine inlet temp at design', units='C', type='NUMBER', group='sCO2 power cycle', required='*')
    I_N_t_des: float = INPUT(label='Design turbine speed, negative links to comp.', units='rpm', type='NUMBER', group='sCO2 power cycle', required='*')
    I_eta_mc: float = INPUT(label='Design main compressor isentropic efficiency', units='-', type='NUMBER', group='sCO2 power cycle', required='*')
    I_eta_rc: float = INPUT(label='Design re-compressor isentropic efficiency', units='-', type='NUMBER', group='sCO2 power cycle', required='*')
    I_eta_t: float = INPUT(label='Design turbine isentropic efficiency', units='-', type='NUMBER', group='sCO2 power cycle', required='*')
    I_tol: float = INPUT(label='Convergence tolerance for performance calcs', units='-', type='NUMBER', group='sCO2 power cycle', required='*')
    I_opt_tol: float = INPUT(label='Convergence tolerance - optimization calcs', units='-', type='NUMBER', group='sCO2 power cycle', required='*')
    I_UA_total_des: float = INPUT(label='Total UA allocatable to recuperators', units='kW/K', type='NUMBER', group='sCO2 power cycle', required='*')
    I_P_high_limit: float = INPUT(label='High pressure limit in cycle', units='MPa', type='NUMBER', group='sCO2 power cycle', required='*')
    O_LT_frac_des: Final[float] = OUTPUT(label='Optimized design point UA distribution', units='-', type='NUMBER', group='sCO2 power cycle', required='*')
    O_P_mc_out_des: Final[float] = OUTPUT(label='Optimized design point high side pressure', units='MPa', type='NUMBER', group='sCO2 power cycle', required='*')
    O_PR_mc_des: Final[float] = OUTPUT(label='Optimized Pressure Ratio across main compressor', type='NUMBER', group='sCO2 power cycle', required='*')
    O_recomp_frac_des: Final[float] = OUTPUT(label='Optimized recompression fraction', units='-', type='NUMBER', group='sCO2 power cycle', required='*')
    O_eta_thermal_des: Final[float] = OUTPUT(label='Design cycle thermal efficiency', units='-', type='NUMBER', group='sCO2 power cycle', required='*')
    O_N_mc_des: Final[float] = OUTPUT(label='Design point compressor shaft speed', units='rpm', type='NUMBER', group='sCO2 power cycle', required='*')
    O_m_dot_PHX: Final[float] = OUTPUT(label='Mass flow rate through primary HX', units='kg/s', type='NUMBER', group='sCO2 power cycle', required='*')
    O_T_array_des: Final[Array] = OUTPUT(label='Cycle temp state points at design', units='K', type='ARRAY', group='sCO2 power cycle', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 I_W_dot_net_des: float = ...,
                 I_T_mc_in_des: float = ...,
                 I_T_t_in_des: float = ...,
                 I_N_t_des: float = ...,
                 I_eta_mc: float = ...,
                 I_eta_rc: float = ...,
                 I_eta_t: float = ...,
                 I_tol: float = ...,
                 I_opt_tol: float = ...,
                 I_UA_total_des: float = ...,
                 I_P_high_limit: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
