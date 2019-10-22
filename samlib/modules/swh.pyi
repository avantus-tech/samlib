
# This is a generated file

"""swh - Solar water heating model using multi-mode tank node model."""

# VERSION: 10

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'solar_resource_file': str,
        'scaled_draw': Array,
        'system_capacity': float,
        'load': Array,
        'tilt': float,
        'azimuth': float,
        'albedo': float,
        'irrad_mode': float,
        'sky_model': float,
        'shading:timestep': Matrix,
        'shading:mxh': Matrix,
        'shading:azal': Matrix,
        'shading:diff': float,
        'mdot': float,
        'ncoll': float,
        'fluid': float,
        'area_coll': float,
        'FRta': float,
        'FRUL': float,
        'iam': float,
        'test_fluid': float,
        'test_flow': float,
        'pipe_length': float,
        'pipe_diam': float,
        'pipe_k': float,
        'pipe_insul': float,
        'tank_h2d_ratio': float,
        'U_tank': float,
        'V_tank': float,
        'hx_eff': float,
        'T_room': float,
        'T_tank_max': float,
        'T_set': float,
        'pump_power': float,
        'pump_eff': float,
        'use_custom_mains': float,
        'custom_mains': Array,
        'use_custom_set': float,
        'custom_set': Array,
        'beam': Array,
        'diffuse': Array,
        'I_incident': Array,
        'I_transmitted': Array,
        'shading_loss': Array,
        'Q_transmitted': Array,
        'Q_useful': Array,
        'Q_deliv': Array,
        'Q_loss': Array,
        'Q_aux': Array,
        'Q_auxonly': Array,
        'P_pump': Array,
        'T_amb': Array,
        'T_cold': Array,
        'T_deliv': Array,
        'T_hot': Array,
        'T_mains': Array,
        'T_tank': Array,
        'V_hot': Array,
        'V_cold': Array,
        'draw': Array,
        'mode': Array,
        'monthly_Q_deliv': Array,
        'monthly_Q_aux': Array,
        'monthly_Q_auxonly': Array,
        'monthly_energy': Array,
        'annual_Q_deliv': float,
        'annual_Q_aux': float,
        'annual_Q_auxonly': float,
        'annual_energy': float,
        'solar_fraction': float,
        'capacity_factor': float,
        'kwh_per_kw': float,
        'ts_shift_hours': float,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix,
        'gen': Array
}, total=False)

class Data(ssc.DataDict):
    solar_resource_file: str = INPUT(label='local weather file path', type='STRING', group='Weather', required='*', constraints='LOCAL_FILE')
    scaled_draw: Array = INPUT(label='Hot water draw', units='kg/hr', type='ARRAY', group='SWH', required='*', constraints='LENGTH=8760')
    system_capacity: float = INPUT(label='Nameplate capacity', units='kW', type='NUMBER', group='SWH', required='*')
    load: Array = INPUT(label='Electricity load (year 1)', units='kW', type='ARRAY', group='SWH')
    tilt: float = INPUT(label='Collector tilt', units='deg', type='NUMBER', group='SWH', required='*', constraints='MIN=0,MAX=90')
    azimuth: float = INPUT(label='Collector azimuth', units='deg', type='NUMBER', group='SWH', required='*', constraints='MIN=0,MAX=360', meta='90=E,180=S')
    albedo: float = INPUT(label='Ground reflectance factor', units='0..1', type='NUMBER', group='SWH', required='*', constraints='FACTOR')
    irrad_mode: float = INPUT(label='Irradiance input mode', units='0/1/2', type='NUMBER', group='SWH', required='?=0', constraints='INTEGER,MIN=0,MAX=2', meta='Beam+Diff,Global+Beam,Global+Diff')
    sky_model: float = INPUT(label='Tilted surface irradiance model', units='0/1/2', type='NUMBER', group='SWH', required='?=1', constraints='INTEGER,MIN=0,MAX=2', meta='Isotropic,HDKR,Perez')
    shading_timestep: Matrix = INPUT(name='shading:timestep', label='Time step beam shading loss', units='%', type='MATRIX', group='SWH', required='?')
    shading_mxh: Matrix = INPUT(name='shading:mxh', label='Month x Hour beam shading loss', units='%', type='MATRIX', group='SWH', required='?')
    shading_azal: Matrix = INPUT(name='shading:azal', label='Azimuth x altitude beam shading loss', units='%', type='MATRIX', group='SWH', required='?')
    shading_diff: float = INPUT(name='shading:diff', label='Diffuse shading loss', units='%', type='NUMBER', group='SWH', required='?')
    mdot: float = INPUT(label='Total system mass flow rate', units='kg/s', type='NUMBER', group='SWH', required='*', constraints='POSITIVE')
    ncoll: float = INPUT(label='Number of collectors', type='NUMBER', group='SWH', required='*', constraints='POSITIVE,INTEGER')
    fluid: float = INPUT(label='Working fluid in system', type='NUMBER', group='SWH', required='*', constraints='INTEGER,MIN=0,MAX=1', meta='Water,Glycol')
    area_coll: float = INPUT(label='Single collector area', units='m2', type='NUMBER', group='SWH', required='*', constraints='POSITIVE')
    FRta: float = INPUT(label='FRta', type='NUMBER', group='SWH', required='*')
    FRUL: float = INPUT(label='FRUL', type='NUMBER', group='SWH', required='*')
    iam: float = INPUT(label='Incidence angle modifier', type='NUMBER', group='SWH', required='*')
    test_fluid: float = INPUT(label='Fluid used in collector test', type='NUMBER', group='SWH', required='*', constraints='INTEGER,MIN=0,MAX=1', meta='Water,Glycol')
    test_flow: float = INPUT(label='Flow rate used in collector test', units='kg/s', type='NUMBER', group='SWH', required='*', constraints='POSITIVE')
    pipe_length: float = INPUT(label='Length of piping in system', units='m', type='NUMBER', group='SWH', required='*', constraints='POSITIVE')
    pipe_diam: float = INPUT(label='Pipe diameter', units='m', type='NUMBER', group='SWH', required='*', constraints='POSITIVE')
    pipe_k: float = INPUT(label='Pipe insulation conductivity', units='W/m2.C', type='NUMBER', group='SWH', required='*', constraints='POSITIVE')
    pipe_insul: float = INPUT(label='Pipe insulation thickness', units='m', type='NUMBER', group='SWH', required='*', constraints='POSITIVE')
    tank_h2d_ratio: float = INPUT(label='Solar tank height to diameter ratio', type='NUMBER', group='SWH', required='*', constraints='POSITIVE')
    U_tank: float = INPUT(label='Solar tank heat loss coefficient', units='W/m2K', type='NUMBER', group='SWH', required='*', constraints='POSITIVE')
    V_tank: float = INPUT(label='Solar tank volume', units='m3', type='NUMBER', group='SWH', required='*', constraints='POSITIVE')
    hx_eff: float = INPUT(label='Heat exchanger effectiveness', units='0..1', type='NUMBER', group='SWH', required='*', constraints='POSITIVE')
    T_room: float = INPUT(label='Temperature around solar tank', units='C', type='NUMBER', group='SWH', required='*', constraints='POSITIVE')
    T_tank_max: float = INPUT(label='Max temperature in solar tank', units='C', type='NUMBER', group='SWH', required='*', constraints='POSITIVE')
    T_set: float = INPUT(label='Set temperature', units='C', type='NUMBER', group='SWH', required='*', constraints='POSITIVE')
    pump_power: float = INPUT(label='Pump power', units='W', type='NUMBER', group='SWH', required='*', constraints='POSITIVE')
    pump_eff: float = INPUT(label='Pumping efficiency', units='%', type='NUMBER', group='SWH', required='*', constraints='PERCENT')
    use_custom_mains: float = INPUT(label='Use custom mains', units='%', type='NUMBER', group='SWH', required='*', constraints='INTEGER,MIN=0,MAX=1')
    custom_mains: Array = INPUT(label='Custom mains', units='C', type='ARRAY', group='SWH', required='*', constraints='LENGTH=8760')
    use_custom_set: float = INPUT(label='Use custom set points', units='%', type='NUMBER', group='SWH', required='*', constraints='INTEGER,MIN=0,MAX=1')
    custom_set: Array = INPUT(label='Custom set points', units='C', type='ARRAY', group='SWH', required='*', constraints='LENGTH=8760')
    beam: Final[Array] = OUTPUT(label='Irradiance - Beam', units='W/m2', type='ARRAY', group='Time Series', required='*')
    diffuse: Final[Array] = OUTPUT(label='Irradiance - Diffuse', units='W/m2', type='ARRAY', group='Time Series', required='*')
    I_incident: Final[Array] = OUTPUT(label='Irradiance - Incident', units='W/m2', type='ARRAY', group='Time Series', required='*')
    I_transmitted: Final[Array] = OUTPUT(label='Irradiance - Transmitted', units='W/m2', type='ARRAY', group='Time Series', required='*')
    shading_loss: Final[Array] = OUTPUT(label='Shading losses', units='%', type='ARRAY', group='Time Series', required='*')
    Q_transmitted: Final[Array] = OUTPUT(label='Q transmitted', units='kW', type='ARRAY', group='Time Series', required='*')
    Q_useful: Final[Array] = OUTPUT(label='Q useful', units='kW', type='ARRAY', group='Time Series', required='*')
    Q_deliv: Final[Array] = OUTPUT(label='Q delivered', units='kW', type='ARRAY', group='Time Series', required='*')
    Q_loss: Final[Array] = OUTPUT(label='Q loss', units='kW', type='ARRAY', group='Time Series', required='*')
    Q_aux: Final[Array] = OUTPUT(label='Q auxiliary', units='kW', type='ARRAY', group='Time Series', required='*')
    Q_auxonly: Final[Array] = OUTPUT(label='Q auxiliary only', units='kW', type='ARRAY', group='Time Series', required='*')
    P_pump: Final[Array] = OUTPUT(label='P pump', units='kW', type='ARRAY', group='Time Series', required='*')
    T_amb: Final[Array] = OUTPUT(label='T ambient', units='C', type='ARRAY', group='Time Series', required='*')
    T_cold: Final[Array] = OUTPUT(label='T cold', units='C', type='ARRAY', group='Time Series', required='*')
    T_deliv: Final[Array] = OUTPUT(label='T delivered', units='C', type='ARRAY', group='Time Series', required='*')
    T_hot: Final[Array] = OUTPUT(label='T hot', units='C', type='ARRAY', group='Time Series', required='*')
    T_mains: Final[Array] = OUTPUT(label='T mains', units='C', type='ARRAY', group='Time Series', required='*')
    T_tank: Final[Array] = OUTPUT(label='T tank', units='C', type='ARRAY', group='Time Series', required='*')
    V_hot: Final[Array] = OUTPUT(label='V hot', units='m3', type='ARRAY', group='Time Series', required='*')
    V_cold: Final[Array] = OUTPUT(label='V cold', units='m3', type='ARRAY', group='Time Series', required='*')
    draw: Final[Array] = OUTPUT(label='Hot water draw', units='kg/hr', type='ARRAY', group='Time Series', required='*')
    mode: Final[Array] = OUTPUT(label='Operation mode', type='ARRAY', group='Time Series', required='*', meta='1,2,3,4')
    monthly_Q_deliv: Final[Array] = OUTPUT(label='Q delivered', units='kWh', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    monthly_Q_aux: Final[Array] = OUTPUT(label='Q auxiliary', units='kWh', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    monthly_Q_auxonly: Final[Array] = OUTPUT(label='Q auxiliary only', units='kWh', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    monthly_energy: Final[Array] = OUTPUT(label='System energy', units='kWh', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    annual_Q_deliv: Final[float] = OUTPUT(label='Q delivered', units='kWh', type='NUMBER', group='Annual', required='*')
    annual_Q_aux: Final[float] = OUTPUT(label='Q auxiliary', units='kWh', type='NUMBER', group='Annual', required='*')
    annual_Q_auxonly: Final[float] = OUTPUT(label='Q auxiliary only', units='kWh', type='NUMBER', group='Annual', required='*')
    annual_energy: Final[float] = OUTPUT(label='System energy', units='kWh', type='NUMBER', group='Annual', required='*')
    solar_fraction: Final[float] = OUTPUT(label='Solar fraction', type='NUMBER', group='Annual', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', group='Annual', required='*')
    kwh_per_kw: Final[float] = OUTPUT(label='First year kWh/kW', units='kWh/kW', type='NUMBER', group='Annual', required='*')
    ts_shift_hours: Final[float] = OUTPUT(label='Time offset for interpreting time series outputs', units='hours', type='NUMBER', group='Miscellaneous', required='*')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    gen: Final[Array] = OUTPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 solar_resource_file: str = ...,
                 scaled_draw: Array = ...,
                 system_capacity: float = ...,
                 load: Array = ...,
                 tilt: float = ...,
                 azimuth: float = ...,
                 albedo: float = ...,
                 irrad_mode: float = ...,
                 sky_model: float = ...,
                 shading_timestep: Matrix = ...,
                 shading_mxh: Matrix = ...,
                 shading_azal: Matrix = ...,
                 shading_diff: float = ...,
                 mdot: float = ...,
                 ncoll: float = ...,
                 fluid: float = ...,
                 area_coll: float = ...,
                 FRta: float = ...,
                 FRUL: float = ...,
                 iam: float = ...,
                 test_fluid: float = ...,
                 test_flow: float = ...,
                 pipe_length: float = ...,
                 pipe_diam: float = ...,
                 pipe_k: float = ...,
                 pipe_insul: float = ...,
                 tank_h2d_ratio: float = ...,
                 U_tank: float = ...,
                 V_tank: float = ...,
                 hx_eff: float = ...,
                 T_room: float = ...,
                 T_tank_max: float = ...,
                 T_set: float = ...,
                 pump_power: float = ...,
                 pump_eff: float = ...,
                 use_custom_mains: float = ...,
                 custom_mains: Array = ...,
                 use_custom_set: float = ...,
                 custom_set: Array = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
