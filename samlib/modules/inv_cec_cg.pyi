
# This is a generated file

"""inv_cec_cg - CEC Inverter Coefficient Generator"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'inv_cec_cg_paco': float,
        'inv_cec_cg_sample_power_units': float,
        'inv_cec_cg_test_samples': Matrix,
        'inv_cec_cg_Vmin': Matrix,
        'inv_cec_cg_Vnom': Matrix,
        'inv_cec_cg_Vmax': Matrix,
        'inv_cec_cg_Vmin_abc': Array,
        'inv_cec_cg_Vnom_abc': Array,
        'inv_cec_cg_Vmax_abc': Array,
        'inv_cec_cg_Vdc': Array,
        'inv_cec_cg_Vdc_Vnom': Array,
        'inv_cec_cg_Pdco': Array,
        'inv_cec_cg_Psco': Array,
        'inv_cec_cg_C0': Array,
        'inv_cec_cg_C1': Array,
        'inv_cec_cg_C2': Array,
        'inv_cec_cg_C3': Array,
        'Pdco': float,
        'Vdco': float,
        'Pso': float,
        'c0': float,
        'c1': float,
        'c2': float,
        'c3': float
}, total=False)

class Data(ssc.DataDict):
    inv_cec_cg_paco: float = INPUT(label='Rated max output', units='W', type='NUMBER', required='*')
    inv_cec_cg_sample_power_units: float = INPUT(label='Sample data units for power output', units='0=W,1=kW', type='NUMBER', required='?=0', constraints='INTEGER,MIN=0,MAX=1')
    inv_cec_cg_test_samples: Matrix = INPUT(label='Sample data', type='MATRIX', required='*')
    inv_cec_cg_Vmin: Final[Matrix] = OUTPUT(label='Vmin for least squares fit', type='MATRIX', required='*')
    inv_cec_cg_Vnom: Final[Matrix] = OUTPUT(label='Vnom for least squares fit', type='MATRIX', required='*')
    inv_cec_cg_Vmax: Final[Matrix] = OUTPUT(label='Vmax for least squares fit', type='MATRIX', required='*')
    inv_cec_cg_Vmin_abc: Final[Array] = OUTPUT(label='Vmin a,b,c for least squares fit', type='ARRAY', required='*')
    inv_cec_cg_Vnom_abc: Final[Array] = OUTPUT(label='Vnom a,b,c for least squares fit', type='ARRAY', required='*')
    inv_cec_cg_Vmax_abc: Final[Array] = OUTPUT(label='Vmax a,b,c for least squares fit', type='ARRAY', required='*')
    inv_cec_cg_Vdc: Final[Array] = OUTPUT(label='Vdc at Vmin, Vnom, Vmax', type='ARRAY', required='*')
    inv_cec_cg_Vdc_Vnom: Final[Array] = OUTPUT(label='Vdc - Vnom at Vmin, Vnom, Vmax', type='ARRAY', required='*')
    inv_cec_cg_Pdco: Final[Array] = OUTPUT(label='Pdco at Vmin, Vnom, Vmax', type='ARRAY', required='*')
    inv_cec_cg_Psco: Final[Array] = OUTPUT(label='Psco at Vmin, Vnom, Vmax', type='ARRAY', required='*')
    inv_cec_cg_C0: Final[Array] = OUTPUT(label='C0 at Vmin, Vnom, Vmax', type='ARRAY', required='*')
    inv_cec_cg_C1: Final[Array] = OUTPUT(label='C1 at m and b', type='ARRAY', required='*')
    inv_cec_cg_C2: Final[Array] = OUTPUT(label='C1 at m and b', type='ARRAY', required='*')
    inv_cec_cg_C3: Final[Array] = OUTPUT(label='C1 at m and b', type='ARRAY', required='*')
    Pdco: Final[float] = OUTPUT(label='CEC generated Pdco', units='Wac', type='NUMBER', required='*')
    Vdco: Final[float] = OUTPUT(label='CEC generated Vdco', units='Vdc', type='NUMBER', required='*')
    Pso: Final[float] = OUTPUT(label='CEC generated Pso', units='Wdc', type='NUMBER', required='*')
    c0: Final[float] = OUTPUT(label='CEC generated c0', units='1/W', type='NUMBER', required='*')
    c1: Final[float] = OUTPUT(label='CEC generated c1', units='1/V', type='NUMBER', required='*')
    c2: Final[float] = OUTPUT(label='CEC generated c2', units='1/V', type='NUMBER', required='*')
    c3: Final[float] = OUTPUT(label='CEC generated c3', units='1/V', type='NUMBER', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 inv_cec_cg_paco: float = ...,
                 inv_cec_cg_sample_power_units: float = ...,
                 inv_cec_cg_test_samples: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
