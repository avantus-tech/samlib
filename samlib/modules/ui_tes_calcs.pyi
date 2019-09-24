
# This is a generated file

"""ui_tes_calcs - Calculates values for all calculated values on UI TES page(s)"""

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
        'W_dot_pb_des': float,
        'eta_pb_des': float,
        'tes_hrs': float,
        'T_HTF_hot': float,
        'T_HTF_cold': float,
        'TES_HTF_code': float,
        'TES_HTF_props': Matrix,
        'h_tank_min': float,
        'h_tank': float,
        'tank_pairs': float,
        'u_tank': float,
        'q_tes_des': float,
        'vol_one_temp_avail': float,
        'vol_one_temp_total': float,
        'd_tank': float,
        'q_dot_loss': float,
        'HTF_dens': float
    }, total=False)

class Data(ssc.DataDict):
    W_dot_pb_des: float = INPUT(label='Power cycle output at design', units='MWe', type='NUMBER', required='*')
    eta_pb_des: float = INPUT(label='Power cycle thermal efficiency', type='NUMBER', required='*')
    tes_hrs: float = INPUT(label='Hours of TES relative to q_dot_pb_des', units='hr', type='NUMBER', required='*')
    T_HTF_hot: float = INPUT(label='Hot HTF temp (into TES HX, if applicable)', units='C', type='NUMBER', required='*')
    T_HTF_cold: float = INPUT(label='Cold HTF temp (out of TES HX, if applicable)', units='C', type='NUMBER', required='*')
    TES_HTF_code: float = INPUT(label='TES storage fluid code', type='NUMBER', required='*')
    TES_HTF_props: Matrix = INPUT(label='User defined tes storage fluid prop data', type='MATRIX', required='*', meta='7 columns (T,Cp,dens,visc,kvisc,cond,h), at least 3 rows')
    h_tank_min: float = INPUT(label='Min. allowable HTF height in storage tank', units='m', type='NUMBER', required='*')
    h_tank: float = INPUT(label='Total height of tank (HTF when tank is full', units='m', type='NUMBER', required='*')
    tank_pairs: float = INPUT(label='Number of equivalent tank pairs', type='NUMBER', required='*')
    u_tank: float = INPUT(label='Loss coefficient from the tank', units='W/m2-K', type='NUMBER', required='*')
    q_tes_des: Final[float] = OUTPUT(label='TES thermal capacity at design', units='MWt-hr', type='NUMBER', required='*')
    vol_one_temp_avail: Final[float] = OUTPUT(label='Available single temp storage volume', units='m^3', type='NUMBER', required='*')
    vol_one_temp_total: Final[float] = OUTPUT(label='Total single temp storage volume', units='m^3', type='NUMBER', required='*')
    d_tank: Final[float] = OUTPUT(label='Single tank diameter', units='m', type='NUMBER', required='*')
    q_dot_loss: Final[float] = OUTPUT(label='Estimated tank heat loss to env.', units='MWt', type='NUMBER', required='*')
    HTF_dens: Final[float] = OUTPUT(label='HTF dens', units='kg/m^3', type='NUMBER', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 W_dot_pb_des: float = ...,
                 eta_pb_des: float = ...,
                 tes_hrs: float = ...,
                 T_HTF_hot: float = ...,
                 T_HTF_cold: float = ...,
                 TES_HTF_code: float = ...,
                 TES_HTF_props: Matrix = ...,
                 h_tank_min: float = ...,
                 h_tank: float = ...,
                 tank_pairs: float = ...,
                 u_tank: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
