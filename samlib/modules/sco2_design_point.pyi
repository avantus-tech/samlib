
# This is a generated file

"""sco2_design_point - Returns optimized sco2 cycle parameters given inputs"""

# VERSION: 0

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
        'W_dot_net_des': float,
        'eta_c': float,
        'eta_t': float,
        'P_high_limit': float,
        'deltaT_PHX': float,
        'deltaT_ACC': float,
        'T_amb_des': float,
        'T_htf_hot_des': float,
        'eta_des': float,
        'run_off_des_study': float,
        'part_load_fracs': Array,
        'T_amb_array': Array,
        'eta_thermal_calc': float,
        'UA_total': float,
        'recomp_frac': float,
        'P_comp_in': float,
        'P_comp_out': float,
        'T_htf_cold': float,
        'part_load_fracs_out': Array,
        'part_load_eta': Array,
        'part_load_coefs': Array,
        'part_load_r_squared': float,
        'T_amb_array_out': Array,
        'T_amb_eta': Array,
        'T_amb_coefs': Array,
        'T_amb_r_squared': float
    }, total=False)

class Data(ssc.DataDict):
    W_dot_net_des: float = INPUT(label='Design cycle power output', units='MW', type='NUMBER', required='*')
    eta_c: float = INPUT(label='Design compressor(s) isentropic efficiency', units='-', type='NUMBER', required='*')
    eta_t: float = INPUT(label='Design turbine isentropic efficiency', units='-', type='NUMBER', required='*')
    P_high_limit: float = INPUT(label='High pressure limit in cycle', units='MPa', type='NUMBER', required='*')
    deltaT_PHX: float = INPUT(label='Temp diff btw hot HTF and turbine inlet', units='C', type='NUMBER', required='*')
    deltaT_ACC: float = INPUT(label='Temp diff btw ambient air and compressor inlet', units='C', type='NUMBER', required='*')
    T_amb_des: float = INPUT(label='Design: Ambient temperature for air cooler', units='C', type='NUMBER', required='*')
    T_htf_hot_des: float = INPUT(label='Tower design outlet temp', units='C', type='NUMBER', required='*')
    eta_des: float = INPUT(label='Power cycle thermal efficiency', type='NUMBER', required='*')
    run_off_des_study: float = INPUT(label='1 = yes, 0/other = no', type='NUMBER', required='*')
    part_load_fracs: Array = INPUT(label='Array of part load q_dot_in fractions for off-design parametric', type='ARRAY', required='run_off_des_study=1')
    T_amb_array: Array = INPUT(label='Array of ambient temperatures for off-design parametric', units='C', type='ARRAY', required='run_off_des_study=1')
    eta_thermal_calc: Final[float] = OUTPUT(label='Calculated cycle thermal efficiency', units='-', type='NUMBER', required='*')
    UA_total: Final[float] = OUTPUT(label='Total recuperator UA', units='kW/K', type='NUMBER', required='*')
    recomp_frac: Final[float] = OUTPUT(label='Recompression fraction', units='-', type='NUMBER', required='*')
    P_comp_in: Final[float] = OUTPUT(label='Compressor inlet pressure', units='MPa', type='NUMBER', required='*')
    P_comp_out: Final[float] = OUTPUT(label='Compressor outlet pressure', units='MPa', type='NUMBER', required='*')
    T_htf_cold: Final[float] = OUTPUT(label='Calculated cold HTF temp', units='C', type='NUMBER', required='*')
    part_load_fracs_out: Final[Array] = OUTPUT(label='Array of part load fractions that SOLVED at off design', units='-', type='ARRAY', required='run_off_des_study=1')
    part_load_eta: Final[Array] = OUTPUT(label='Matrix of power cycle efficiency results for q_dot_in part load', units='-', type='ARRAY', required='run_off_des_study=1')
    part_load_coefs: Final[Array] = OUTPUT(label='Part load polynomial coefficients', units='-', type='ARRAY', required='run_off_des_study=1')
    part_load_r_squared: Final[float] = OUTPUT(label='Part load curve fit R squared', units='-', type='NUMBER', required='run_off_des_study=1')
    T_amb_array_out: Final[Array] = OUTPUT(label='Array of ambient temps that SOLVED at off design', units='C', type='ARRAY', required='run_off_des_study=1')
    T_amb_eta: Final[Array] = OUTPUT(label='Matrix of ambient temps and power cycle efficiency', units='-', type='ARRAY', required='run_off_des_study=1')
    T_amb_coefs: Final[Array] = OUTPUT(label='Part load polynomial coefficients', units='-', type='ARRAY', required='run_off_des_study=1')
    T_amb_r_squared: Final[float] = OUTPUT(label='T amb curve fit R squared', units='-', type='NUMBER', required='run_off_des_study=1')

    def __init__(self, *args: Mapping[str, Any],
                 W_dot_net_des: float = ...,
                 eta_c: float = ...,
                 eta_t: float = ...,
                 P_high_limit: float = ...,
                 deltaT_PHX: float = ...,
                 deltaT_ACC: float = ...,
                 T_amb_des: float = ...,
                 T_htf_hot_des: float = ...,
                 eta_des: float = ...,
                 run_off_des_study: float = ...,
                 part_load_fracs: Array = ...,
                 T_amb_array: Array = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
