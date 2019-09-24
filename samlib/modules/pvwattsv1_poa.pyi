
# This is a generated file

"""pvwattsv1_poa - PVWatts system performance calculator.  Does not include weather file reading or irradiance processing - user must supply arrays of precalculated POA irradiance data."""

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
        'beam': Array,
        'poa_beam': Array,
        'poa_skydiff': Array,
        'poa_gnddiff': Array,
        'tdry': Array,
        'wspd': Array,
        'incidence': Array,
        'step': float,
        'system_size': float,
        'derate': float,
        'inoct': float,
        't_ref': float,
        'gamma': float,
        'inv_eff': float,
        'tcell': Array,
        'dc': Array,
        'ac': Array
    }, total=False)

class Data(ssc.DataDict):
    beam: Array = INPUT(label='Direct normal radiation', units='W/m2', type='ARRAY', group='Weather', required='*')
    poa_beam: Array = INPUT(label='Incident direct normal radiation', units='W/m2', type='ARRAY', group='Weather', required='*', constraints='LENGTH_EQUAL=beam')
    poa_skydiff: Array = INPUT(label='Incident sky diffuse radiation', units='W/m2', type='ARRAY', group='Weather', required='*', constraints='LENGTH_EQUAL=beam')
    poa_gnddiff: Array = INPUT(label='Incident ground diffuse irradiance', units='W/m2', type='ARRAY', group='Weather', required='*', constraints='LENGTH_EQUAL=beam')
    tdry: Array = INPUT(label='Dry bulb temperature', units="'C", type='ARRAY', group='Weather', required='*', constraints='LENGTH_EQUAL=beam')
    wspd: Array = INPUT(label='Wind speed', units='m/s', type='ARRAY', group='Weather', required='*', constraints='LENGTH_EQUAL=beam')
    incidence: Array = INPUT(label='Incidence angle to surface', units='deg', type='ARRAY', group='Weather', required='*', constraints='LENGTH_EQUAL=beam')
    step: float = INPUT(label='Time step of input data', units='sec', type='NUMBER', group='PVWatts', required='?=3600', constraints='POSITIVE')
    system_size: float = INPUT(label='Nameplate capacity', units='kW', type='NUMBER', group='PVWatts', required='*', constraints='MIN=0.5,MAX=100000')
    derate: float = INPUT(label='System derate value', units='frac', type='NUMBER', group='PVWatts', required='*', constraints='MIN=0,MAX=1')
    inoct: float = INPUT(label='Nominal operating cell temperature', units="'C", type='NUMBER', group='PVWatts', required='?=45.0', constraints='POSITIVE')
    t_ref: float = INPUT(label='Reference cell temperature', units="'C", type='NUMBER', group='PVWatts', required='?=25.0', constraints='POSITIVE')
    gamma: float = INPUT(label='Max power temperature coefficient', units="%/'C", type='NUMBER', group='PVWatts', required='?=-0.5')
    inv_eff: float = INPUT(label='Inverter efficiency at rated power', units='frac', type='NUMBER', group='PVWatts', required='?=0.92', constraints='MIN=0,MAX=1')
    tcell: Final[Array] = OUTPUT(label='Cell temperature', units="'C", type='ARRAY', group='PVWatts', required='*', constraints='LENGTH_EQUAL=beam')
    dc: Final[Array] = OUTPUT(label='DC array output', units='kWhdc', type='ARRAY', group='PVWatts', required='*', constraints='LENGTH_EQUAL=beam')
    ac: Final[Array] = OUTPUT(label='AC system output', units='kWhac', type='ARRAY', group='PVWatts', required='*', constraints='LENGTH_EQUAL=beam')

    def __init__(self, *args: Mapping[str, Any],
                 beam: Array = ...,
                 poa_beam: Array = ...,
                 poa_skydiff: Array = ...,
                 poa_gnddiff: Array = ...,
                 tdry: Array = ...,
                 wspd: Array = ...,
                 incidence: Array = ...,
                 step: float = ...,
                 system_size: float = ...,
                 derate: float = ...,
                 inoct: float = ...,
                 t_ref: float = ...,
                 gamma: float = ...,
                 inv_eff: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
