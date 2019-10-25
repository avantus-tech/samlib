
# This is a generated file

"""pv_get_shade_loss_mpp - PV get shade loss fraction for strings from Sara MacAlpine"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'global_poa_irrad': Array,
        'diffuse_irrad': Array,
        'str_shade_fracs': Matrix,
        'pv_cell_temp': Array,
        'mods_per_string': Array,
        'str_vmp_stc': Array,
        'v_mppt_low': Array,
        'v_mppt_high': Array,
        'N': Array,
        'd': Array,
        't': Array,
        'S': Array,
        'shade_loss': Array
}, total=False)

class Data(ssc.DataDict):
    global_poa_irrad: Array = INPUT(label='Global POA irradiance', type='ARRAY', group='PV Shade Loss DB', required='*')
    diffuse_irrad: Array = INPUT(label='Diffuse irradiance', type='ARRAY', group='PV Shade Loss DB', required='*')
    str_shade_fracs: Matrix = INPUT(label='Shading fractions for each string', type='MATRIX', group='PV Shade Loss DB', required='*')
    pv_cell_temp: Array = INPUT(label='PV cell temperature', type='ARRAY', group='PV Shade Loss DB', required='*')
    mods_per_string: Array = INPUT(label='Modules per string', type='ARRAY', group='PV Shade Loss DB', required='*')
    str_vmp_stc: Array = INPUT(label='Unshaded Vmp of the string at STC', type='ARRAY', group='PV Shade Loss DB', required='*')
    v_mppt_low: Array = INPUT(label='Lower bound of inverter MPPT range', type='ARRAY', group='PV Shade Loss DB', required='*')
    v_mppt_high: Array = INPUT(label='Upper bound of inverter MPPT range', type='ARRAY', group='PV Shade Loss DB', required='*')
    N: Final[Array] = OUTPUT(label='N', type='ARRAY', group='PV Shade Loss DB', required='*')
    d: Final[Array] = OUTPUT(label='d', type='ARRAY', group='PV Shade Loss DB', required='*')
    t: Final[Array] = OUTPUT(label='t', type='ARRAY', group='PV Shade Loss DB', required='*')
    S: Final[Array] = OUTPUT(label='S', type='ARRAY', group='PV Shade Loss DB', required='*')
    shade_loss: Final[Array] = OUTPUT(label='Shade loss fraction', type='ARRAY', group='PV Shade Loss DB', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 global_poa_irrad: Array = ...,
                 diffuse_irrad: Array = ...,
                 str_shade_fracs: Matrix = ...,
                 pv_cell_temp: Array = ...,
                 mods_per_string: Array = ...,
                 str_vmp_stc: Array = ...,
                 v_mppt_low: Array = ...,
                 v_mppt_high: Array = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
