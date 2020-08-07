
# This is a generated file

"""ui_tes_calcs - Calculates values for all calculated values on UI TES page(s)"""

# VERSION: 0

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'P_ref': float,
        'design_eff': float,
        'tshours': float,
        'T_htf_hot_des': float,
        'T_htf_cold_des': float,
        'rec_htf': float,
        'field_fl_props': Matrix,
        'h_tank_min': float,
        'h_tank': float,
        'tank_pairs': float,
        'u_tank': float,
        'q_tes': float,
        'tes_avail_vol': float,
        'vol_tank': float,
        'csp_pt_tes_tank_diameter': float,
        'q_dot_tes_est': float,
        'csp_pt_tes_htf_density': float
}, total=False)

class Data(ssc.DataDict):
    P_ref: float = INPUT(label='Power cycle output at design', units='MWe', type='NUMBER', required='*')
    design_eff: float = INPUT(label='Power cycle thermal efficiency', type='NUMBER', required='*')
    tshours: float = INPUT(label='Hours of TES relative to q_dot_pb_des', units='hr', type='NUMBER', required='*')
    T_htf_hot_des: float = INPUT(label='Hot HTF temp (into TES HX, if applicable)', units='C', type='NUMBER', required='*')
    T_htf_cold_des: float = INPUT(label='Cold HTF temp (out of TES HX, if applicable)', units='C', type='NUMBER', required='*')
    rec_htf: float = INPUT(label='TES storage fluid code', type='NUMBER', required='*')
    field_fl_props: Matrix = INPUT(label='User defined tes storage fluid prop data', type='MATRIX', required='*', meta='7 columns (T,Cp,dens,visc,kvisc,cond,h), at least 3 rows')
    h_tank_min: float = INPUT(label='Min. allowable HTF height in storage tank', units='m', type='NUMBER', required='*')
    h_tank: float = INPUT(label='Total height of tank (HTF when tank is full', units='m', type='NUMBER', required='*')
    tank_pairs: float = INPUT(label='Number of equivalent tank pairs', type='NUMBER', required='*')
    u_tank: float = INPUT(label='Loss coefficient from the tank', units='W/m2-K', type='NUMBER', required='*')
    q_tes: Final[float] = OUTPUT(label='TES thermal capacity at design', units='MWt-hr', type='NUMBER', required='*')
    tes_avail_vol: Final[float] = OUTPUT(label='Available single temp storage volume', units='m^3', type='NUMBER', required='*')
    vol_tank: Final[float] = OUTPUT(label='Total single temp storage volume', units='m^3', type='NUMBER', required='*')
    csp_pt_tes_tank_diameter: Final[float] = OUTPUT(label='Single tank diameter', units='m', type='NUMBER', required='*')
    q_dot_tes_est: Final[float] = OUTPUT(label='Estimated tank heat loss to env.', units='MWt', type='NUMBER', required='*')
    csp_pt_tes_htf_density: Final[float] = OUTPUT(label='HTF dens', units='kg/m^3', type='NUMBER', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 P_ref: float = ...,
                 design_eff: float = ...,
                 tshours: float = ...,
                 T_htf_hot_des: float = ...,
                 T_htf_cold_des: float = ...,
                 rec_htf: float = ...,
                 field_fl_props: Matrix = ...,
                 h_tank_min: float = ...,
                 h_tank: float = ...,
                 tank_pairs: float = ...,
                 u_tank: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
