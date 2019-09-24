
# This is a generated file

"""pv6parmod - CEC 6 Parameter PV module model performance calculator.  Does not include weather file reading or irradiance processing, or inverter (DC to AC) modeling."""

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
        'poa_beam': Array,
        'poa_skydiff': Array,
        'poa_gnddiff': Array,
        'tdry': Array,
        'wspd': Array,
        'wdir': Array,
        'sun_zen': Array,
        'incidence': Array,
        'surf_tilt': Array,
        'elev': float,
        'opvoltage': Array,
        'area': float,
        'Vmp': float,
        'Imp': float,
        'Voc': float,
        'Isc': float,
        'alpha_isc': float,
        'beta_voc': float,
        'gamma_pmp': float,
        'tnoct': float,
        'a': float,
        'Il': float,
        'Io': float,
        'Rs': float,
        'Rsh': float,
        'Adj': float,
        'standoff': float,
        'height': float,
        'tcell': Array,
        'dc_voltage': Array,
        'dc_current': Array,
        'eff': Array,
        'dc': Array
    }, total=False)

class Data(ssc.DataDict):
    poa_beam: Array = INPUT(label='Incident direct normal radiation', units='W/m2', type='ARRAY', group='Weather', required='*')
    poa_skydiff: Array = INPUT(label='Incident sky diffuse radiation', units='W/m2', type='ARRAY', group='Weather', required='*', constraints='LENGTH_EQUAL=poa_beam')
    poa_gnddiff: Array = INPUT(label='Incident ground diffuse irradiance', units='W/m2', type='ARRAY', group='Weather', required='*', constraints='LENGTH_EQUAL=poa_beam')
    tdry: Array = INPUT(label='Dry bulb temperature', units="'C", type='ARRAY', group='Weather', required='*', constraints='LENGTH_EQUAL=poa_beam')
    wspd: Array = INPUT(label='Wind speed', units='m/s', type='ARRAY', group='Weather', required='*', constraints='LENGTH_EQUAL=poa_beam')
    wdir: Array = INPUT(label='Wind direction', units='deg', type='ARRAY', group='Weather', required='*', constraints='LENGTH_EQUAL=poa_beam')
    sun_zen: Array = INPUT(label='Sun zenith angle', units='deg', type='ARRAY', group='Weather', required='*', constraints='LENGTH_EQUAL=poa_beam')
    incidence: Array = INPUT(label='Incidence angle to surface', units='deg', type='ARRAY', group='Weather', required='*', constraints='LENGTH_EQUAL=poa_beam')
    surf_tilt: Array = INPUT(label='Surface tilt angle', units='deg', type='ARRAY', group='Weather', required='*', constraints='LENGTH_EQUAL=poa_beam')
    elev: float = INPUT(label='Site elevation', units='m', type='NUMBER', group='Weather', required='*')
    opvoltage: Array = INPUT(label='Module operating voltage', units='Volt', type='ARRAY', group='CEC 6 Parameter PV Module Model', required='?')
    area: float = INPUT(label='Module area', units='m2', type='NUMBER', group='CEC 6 Parameter PV Module Model', required='*')
    Vmp: float = INPUT(label='Maximum power point voltage', units='V', type='NUMBER', group='CEC 6 Parameter PV Module Model', required='*')
    Imp: float = INPUT(label='Maximum power point current', units='A', type='NUMBER', group='CEC 6 Parameter PV Module Model', required='*')
    Voc: float = INPUT(label='Open circuit voltage', units='V', type='NUMBER', group='CEC 6 Parameter PV Module Model', required='*')
    Isc: float = INPUT(label='Short circuit current', units='A', type='NUMBER', group='CEC 6 Parameter PV Module Model', required='*')
    alpha_isc: float = INPUT(label='Temp coeff of current at SC', units="A/'C", type='NUMBER', group='CEC 6 Parameter PV Module Model', required='*')
    beta_voc: float = INPUT(label='Temp coeff of voltage at OC', units="V/'C", type='NUMBER', group='CEC 6 Parameter PV Module Model', required='*')
    gamma_pmp: float = INPUT(label='Temp coeff of power at MP', units="%/'C", type='NUMBER', group='CEC 6 Parameter PV Module Model', required='*')
    tnoct: float = INPUT(label='NOCT cell temperature', units="'C", type='NUMBER', group='CEC 6 Parameter PV Module Model', required='*')
    a: float = INPUT(label='Modified nonideality factor', units='1/V', type='NUMBER', group='CEC 6 Parameter PV Module Model', required='*')
    Il: float = INPUT(label='Light current', units='A', type='NUMBER', group='CEC 6 Parameter PV Module Model', required='*')
    Io: float = INPUT(label='Saturation current', units='A', type='NUMBER', group='CEC 6 Parameter PV Module Model', required='*')
    Rs: float = INPUT(label='Series resistance', units='ohm', type='NUMBER', group='CEC 6 Parameter PV Module Model', required='*')
    Rsh: float = INPUT(label='Shunt resistance', units='ohm', type='NUMBER', group='CEC 6 Parameter PV Module Model', required='*')
    Adj: float = INPUT(label='OC SC temp coeff adjustment', units='%', type='NUMBER', group='CEC 6 Parameter PV Module Model', required='*')
    standoff: float = INPUT(label='Mounting standoff option', units='0..6', type='NUMBER', group='CEC 6 Parameter PV Module Model', required='?=6', constraints='INTEGER,MIN=0,MAX=6', meta='0=bipv, 1= >3.5in, 2=2.5-3.5in, 3=1.5-2.5in, 4=0.5-1.5in, 5= <0.5in, 6=ground/rack')
    height: float = INPUT(label='System installation height', units='0/1', type='NUMBER', group='CEC 6 Parameter PV Module Model', required='?=0', constraints='INTEGER,MIN=0,MAX=1', meta='0=less than 22ft, 1=more than 22ft')
    tcell: Final[Array] = OUTPUT(label='Cell temperature', units="'C", type='ARRAY', group='CEC 6 Parameter PV Module Model', required='*', constraints='LENGTH_EQUAL=poa_beam')
    dc_voltage: Final[Array] = OUTPUT(label='DC module voltage', units='Volt', type='ARRAY', group='CEC 6 Parameter PV Module Model', required='*', constraints='LENGTH_EQUAL=poa_beam')
    dc_current: Final[Array] = OUTPUT(label='DC module current', units='Ampere', type='ARRAY', group='CEC 6 Parameter PV Module Model', required='*', constraints='LENGTH_EQUAL=poa_beam')
    eff: Final[Array] = OUTPUT(label='Conversion efficiency', units='0..1', type='ARRAY', group='CEC 6 Parameter PV Module Model', required='*', constraints='LENGTH_EQUAL=poa_beam')
    dc: Final[Array] = OUTPUT(label='DC power output', units='Watt', type='ARRAY', group='CEC 6 Parameter PV Module Model', required='*', constraints='LENGTH_EQUAL=poa_beam')

    def __init__(self, *args: Mapping[str, Any],
                 poa_beam: Array = ...,
                 poa_skydiff: Array = ...,
                 poa_gnddiff: Array = ...,
                 tdry: Array = ...,
                 wspd: Array = ...,
                 wdir: Array = ...,
                 sun_zen: Array = ...,
                 incidence: Array = ...,
                 surf_tilt: Array = ...,
                 elev: float = ...,
                 opvoltage: Array = ...,
                 area: float = ...,
                 Vmp: float = ...,
                 Imp: float = ...,
                 Voc: float = ...,
                 Isc: float = ...,
                 alpha_isc: float = ...,
                 beta_voc: float = ...,
                 gamma_pmp: float = ...,
                 tnoct: float = ...,
                 a: float = ...,
                 Il: float = ...,
                 Io: float = ...,
                 Rs: float = ...,
                 Rsh: float = ...,
                 Adj: float = ...,
                 standoff: float = ...,
                 height: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
