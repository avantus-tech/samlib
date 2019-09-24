
# This is a generated file

"""cb_empirical_hce_heat_loss - Empirical HCE Heat Loss"""

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
        'HCEFrac': Array,
        'PerfFac': Array,
        'RefMirrAper': Array,
        'HCE_A0': Array,
        'HCE_A1': Array,
        'HCE_A2': Array,
        'HCE_A3': Array,
        'HCE_A4': Array,
        'HCE_A5': Array,
        'HCE_A6': Array,
        'ui_reference_wind_speed': float,
        'SfOutTempD': float,
        'SfInTempD': float,
        'ui_reference_ambient_temperature': float,
        'ui_reference_direct_normal_irradiance': float,
        'HL': Array,
        'HL_weighted': float,
        'HL_weighted_m2': float
    }, total=False)

class Data(ssc.DataDict):
    HCEFrac: Array = INPUT(label='Fraction of field that is this type of HCE', type='ARRAY', group='hce', required='*')
    PerfFac: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    RefMirrAper: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCE_A0: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCE_A1: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCE_A2: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCE_A3: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCE_A4: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCE_A5: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    HCE_A6: Array = INPUT(label='label', type='ARRAY', group='hce', required='*')
    ui_reference_wind_speed: float = INPUT(label='Wind speed for design heat loss', units='m/s', type='NUMBER', group='hce', required='*')
    SfOutTempD: float = INPUT(label='Solar Field Outlet Temp at design', units='C', type='NUMBER', group='hce', required='*')
    SfInTempD: float = INPUT(label='Solar Field Inlet Temp at design', units='C', type='NUMBER', group='hce', required='*')
    ui_reference_ambient_temperature: float = INPUT(label='Ambient temp at design heat loss', units='C', type='NUMBER', group='hce', required='*')
    ui_reference_direct_normal_irradiance: float = INPUT(label='DNI at design', units='W/m2', type='NUMBER', group='hce', required='*')
    HL: Final[Array] = OUTPUT(label='HCE Heat Losses', units='W/m', type='ARRAY', group='hce', required='*')
    HL_weighted: Final[float] = OUTPUT(label='Weighted HCE Heat Loss', units='W/m', type='NUMBER', group='hce', required='*')
    HL_weighted_m2: Final[float] = OUTPUT(label='Weighted HCE Heat Loss per Aperture Area', units='W/m2', type='NUMBER', group='hce', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 HCEFrac: Array = ...,
                 PerfFac: Array = ...,
                 RefMirrAper: Array = ...,
                 HCE_A0: Array = ...,
                 HCE_A1: Array = ...,
                 HCE_A2: Array = ...,
                 HCE_A3: Array = ...,
                 HCE_A4: Array = ...,
                 HCE_A5: Array = ...,
                 HCE_A6: Array = ...,
                 ui_reference_wind_speed: float = ...,
                 SfOutTempD: float = ...,
                 SfInTempD: float = ...,
                 ui_reference_ambient_temperature: float = ...,
                 ui_reference_direct_normal_irradiance: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
