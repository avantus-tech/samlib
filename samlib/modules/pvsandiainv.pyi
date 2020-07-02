
# This is a generated file

"""pvsandiainv - Sandia PV inverter performance calculator."""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'dc': Array,
        'dc_voltage': Array,
        'paco': float,
        'pdco': float,
        'vdco': float,
        'pso': float,
        'pntare': float,
        'c0': float,
        'c1': float,
        'c2': float,
        'c3': float,
        'ac': Array,
        'acpar': Array,
        'plr': Array,
        'eff_inv': Array,
        'cliploss': Array,
        'soloss': Array,
        'ntloss': Array
}, total=False)

class Data(ssc.DataDict):
    dc: Array = INPUT(label='DC power input to inverter', units='Watt', type='ARRAY', group='Sandia Inverter Model', required='*')
    dc_voltage: Array = INPUT(label='DC voltage input to inverter', units='Volt', type='ARRAY', group='Sandia Inverter Model', required='*', constraints='LENGTH_EQUAL=dc')
    paco: float = INPUT(label='Max AC power rating', units='Wac', type='NUMBER', group='Sandia Inverter Model', required='*')
    pdco: float = INPUT(label='DC power level at which Paco is achieved', units='Wdc', type='NUMBER', group='Sandia Inverter Model', required='*')
    vdco: float = INPUT(label='DV voltage level at which Paco is achieved', units='Volt', type='NUMBER', group='Sandia Inverter Model', required='*')
    pso: float = INPUT(label='DC power level required to start inversion', units='Wdc', type='NUMBER', group='Sandia Inverter Model', required='*')
    pntare: float = INPUT(label='Parasitic AC consumption', units='Wac', type='NUMBER', group='Sandia Inverter Model', required='*')
    c0: float = INPUT(label='C0: Defines parabolic curvature of relationship between ac power and dc power at reference conditions', units='1/W', type='NUMBER', group='Sandia Inverter Model', required='*')
    c1: float = INPUT(label='C1: Parameter allowing Pdco to vary linearly with dc voltage input', units='1/V', type='NUMBER', group='Sandia Inverter Model', required='*')
    c2: float = INPUT(label='C2: Parameter allowing Pso to vary linearly with dc voltage input ', units='1/V', type='NUMBER', group='Sandia Inverter Model', required='*')
    c3: float = INPUT(label='C3: Parameter allowing C0 to vary linearly with dc voltage input', units='1/V', type='NUMBER', group='Sandia Inverter Model', required='*')
    ac: Final[Array] = OUTPUT(label='AC power output', units='Wac', type='ARRAY', group='Sandia Inverter Model', required='*', constraints='LENGTH_EQUAL=dc')
    acpar: Final[Array] = OUTPUT(label='AC parasitic power', units='Wac', type='ARRAY', group='Sandia Inverter Model', required='*', constraints='LENGTH_EQUAL=dc')
    plr: Final[Array] = OUTPUT(label='Part load ratio', units='0..1', type='ARRAY', group='Sandia Inverter Model', required='*', constraints='LENGTH_EQUAL=dc')
    eff_inv: Final[Array] = OUTPUT(label='Conversion efficiency', units='0..1', type='ARRAY', group='Sandia Inverter Model', required='*', constraints='LENGTH_EQUAL=dc')
    cliploss: Final[Array] = OUTPUT(label='Power loss due to clipping (Wac)', units='Wac', type='ARRAY', group='Sandia Inverter Model', required='*', constraints='LENGTH_EQUAL=dc')
    soloss: Final[Array] = OUTPUT(label='Power loss due to operating power consumption (Wac)', units='Wac', type='ARRAY', group='Sandia Inverter Model', required='*', constraints='LENGTH_EQUAL=dc')
    ntloss: Final[Array] = OUTPUT(label='Power loss due to night time tare loss (Wac)', units='Wac', type='ARRAY', group='Sandia Inverter Model', required='*', constraints='LENGTH_EQUAL=dc')

    def __init__(self, *args: Mapping[str, Any],
                 dc: Array = ...,
                 dc_voltage: Array = ...,
                 paco: float = ...,
                 pdco: float = ...,
                 vdco: float = ...,
                 pso: float = ...,
                 pntare: float = ...,
                 c0: float = ...,
                 c1: float = ...,
                 c2: float = ...,
                 c3: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
