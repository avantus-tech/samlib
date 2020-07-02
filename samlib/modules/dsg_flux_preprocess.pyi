
# This is a generated file

"""dsg_flux_preprocess - Calculate receiver max flux and absorber (boiler, etc.) fractions"""

# VERSION: 0

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'P_HP_in': float,
        'P_HP_out': float,
        'T_sh_out_ref': float,
        'T_rh_out_ref': float,
        'P_cycle_des': float,
        'eta_cycle_des': float,
        'rh_frac_ref': float,
        'CT': float,
        'dT_cooling_ref': float,
        'T_approach': float,
        'T_amb_des': float,
        'T_ITD_des': float,
        'Q_rec_des': float,
        'max_flux_b': float,
        'max_flux_sh': float,
        'max_flux_rh': float,
        'b_q_loss_flux': float,
        'sh_q_loss_flux': float,
        'rh_q_loss_flux': float,
        'max_flux': float,
        'f_b': float,
        'f_sh': float,
        'f_rh': float
}, total=False)

class Data(ssc.DataDict):
    P_HP_in: float = INPUT(label='HP Turbine inlet pressure', units='bar', type='NUMBER', required='*')
    P_HP_out: float = INPUT(label='HP Turbine outlet pressure', units='bar', type='NUMBER', required='*')
    T_sh_out_ref: float = INPUT(label='Superheater outlet temperature', units='C', type='NUMBER', required='*')
    T_rh_out_ref: float = INPUT(label='Reheater outlet temperature', units='C', type='NUMBER', required='*')
    P_cycle_des: float = INPUT(label='Cycle power output at design', units='MW', type='NUMBER', required='*')
    eta_cycle_des: float = INPUT(label='Cycle thermal efficiency at des.', type='NUMBER', required='*')
    rh_frac_ref: float = INPUT(label='Mdot fraction to reheat at design', type='NUMBER', required='*')
    CT: float = INPUT(label='Cooling type', type='NUMBER', required='*')
    dT_cooling_ref: float = INPUT(label='dT of cooling water', units='C', type='NUMBER', required='*')
    T_approach: float = INPUT(label='dT cold cooling water - T_wb', units='C', type='NUMBER', required='*')
    T_amb_des: float = INPUT(label='Ambient (wb) temp at design', units='C', type='NUMBER', required='*')
    T_ITD_des: float = INPUT(label='T_cond - T_db', units='C', type='NUMBER', required='*')
    Q_rec_des: float = INPUT(label='Receiver thermal power at des.', units='MW', type='NUMBER', required='*')
    max_flux_b: float = INPUT(label='Max allow. boiler flux', units='kW/m2', type='NUMBER', required='*')
    max_flux_sh: float = INPUT(label='Max allow. superheater flux', units='kW/m2', type='NUMBER', required='*')
    max_flux_rh: float = INPUT(label='Max allow. reheater flux', units='kW/m2', type='NUMBER', required='*')
    b_q_loss_flux: float = INPUT(label='Boiler heat loss flux', units='kW/m2', type='NUMBER', required='*')
    sh_q_loss_flux: float = INPUT(label='Superheater heat loss flux', units='kW/m2', type='NUMBER', required='*')
    rh_q_loss_flux: float = INPUT(label='Reheater heat loss flux', units='kW/m2', type='NUMBER', required='*')
    max_flux: Final[float] = OUTPUT(label='Maximum flux allow. on receiver', units='kW/m2', type='NUMBER', required='*')
    f_b: Final[float] = OUTPUT(label='Fraction of total height to boiler', type='NUMBER', required='*')
    f_sh: Final[float] = OUTPUT(label='Fraction of total height to SH', type='NUMBER', required='*')
    f_rh: Final[float] = OUTPUT(label='Fraction of total height to RH', type='NUMBER', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 P_HP_in: float = ...,
                 P_HP_out: float = ...,
                 T_sh_out_ref: float = ...,
                 T_rh_out_ref: float = ...,
                 P_cycle_des: float = ...,
                 eta_cycle_des: float = ...,
                 rh_frac_ref: float = ...,
                 CT: float = ...,
                 dT_cooling_ref: float = ...,
                 T_approach: float = ...,
                 T_amb_des: float = ...,
                 T_ITD_des: float = ...,
                 Q_rec_des: float = ...,
                 max_flux_b: float = ...,
                 max_flux_sh: float = ...,
                 max_flux_rh: float = ...,
                 b_q_loss_flux: float = ...,
                 sh_q_loss_flux: float = ...,
                 rh_q_loss_flux: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
