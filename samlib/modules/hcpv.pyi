
# This is a generated file

"""hcpv - High-X Concentrating PV, SAM component models V.1"""

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
        'file_name': str,
        'system_capacity': float,
        'module_cell_area': float,
        'module_concentration': float,
        'module_optical_error': float,
        'module_alignment_error': float,
        'module_flutter_loss_coeff': float,
        'module_a0': float,
        'module_a1': float,
        'module_a2': float,
        'module_a3': float,
        'module_a4': float,
        'module_ncells': float,
        'module_mjeff': Array,
        'module_rad': Array,
        'module_reference': float,
        'module_a': float,
        'module_b': float,
        'module_dT': float,
        'module_temp_coeff': float,
        'inv_snl_c0': float,
        'inv_snl_c1': float,
        'inv_snl_c2': float,
        'inv_snl_c3': float,
        'inv_snl_paco': float,
        'inv_snl_pdco': float,
        'inv_snl_pnt': float,
        'inv_snl_pso': float,
        'inv_snl_vdco': float,
        'inv_snl_vdcmax': float,
        'array_modules_per_tracker': float,
        'array_num_trackers': float,
        'array_num_inverters': float,
        'array_wind_stow_speed': float,
        'array_tracker_power_fraction': float,
        'array_rlim_el_min': float,
        'array_rlim_el_max': float,
        'array_rlim_az_min': float,
        'array_rlim_az_max': float,
        'array_enable_azalt_sf': float,
        'azaltsf': Matrix,
        'array_monthly_soiling': Array,
        'array_dc_mismatch_loss': float,
        'array_dc_wiring_loss': float,
        'array_diode_conn_loss': float,
        'array_ac_wiring_loss': float,
        'array_tracking_error': float,
        'hourly_solazi': Array,
        'hourly_solzen': Array,
        'hourly_sazi': Array,
        'hourly_stilt': Array,
        'hourly_sunup': Array,
        'hourly_beam': Array,
        'hourly_tdry': Array,
        'hourly_windspd': Array,
        'hourly_airmass': Array,
        'hourly_shading_derate': Array,
        'hourly_poa': Array,
        'hourly_input_radiation': Array,
        'hourly_tmod': Array,
        'hourly_tcell': Array,
        'hourly_celleff': Array,
        'hourly_modeff': Array,
        'hourly_dc': Array,
        'hourly_dc_net': Array,
        'hourly_ac': Array,
        'monthly_energy': Array,
        'monthly_beam': Array,
        'monthly_input_radiation': Array,
        'monthly_dc_net': Array,
        'annual_energy': float,
        'annual_beam': float,
        'annual_input_radiation': float,
        'annual_dc': float,
        'annual_dc_net': float,
        'annual_ac': float,
        'tracker_nameplate_watts': float,
        'modeff_ref': float,
        'dc_loss_stowing_kwh': float,
        'ac_loss_tracker_kwh': float,
        'dc_nominal': float,
        'capacity_factor': float,
        'kwh_per_kw': float,
        'adjust:constant': float,
        'adjust:hourly': Array,
        'adjust:periods': Matrix,
        'gen': Array
    }, total=False)

class Data(ssc.DataDict):
    file_name: str = INPUT(label='Weather file in TMY2, TMY3, EPW, or SMW.', type='STRING', group='hcpv', required='*', constraints='LOCAL_FILE')
    system_capacity: float = INPUT(label='Nameplate capacity', units='kW', type='NUMBER', group='PVWatts', required='*')
    module_cell_area: float = INPUT(label='Single cell area', units='cm^2', type='NUMBER', group='hcpv', required='*')
    module_concentration: float = INPUT(label='Concentration ratio', units='none', type='NUMBER', group='hcpv', required='*')
    module_optical_error: float = INPUT(label='Optical error factor', units='0..1', type='NUMBER', group='hcpv', required='*')
    module_alignment_error: float = INPUT(label='Alignment loss factor', units='0..1', type='NUMBER', group='hcpv', required='*')
    module_flutter_loss_coeff: float = INPUT(label='Wind flutter loss factor', units='0..1 per m/s', type='NUMBER', group='hcpv', required='*')
    module_a0: float = INPUT(label='Air mass modifier coefficient 0', units='none', type='NUMBER', group='hcpv', required='*')
    module_a1: float = INPUT(label='Air mass modifier coefficient 1', units='none', type='NUMBER', group='hcpv', required='*')
    module_a2: float = INPUT(label='Air mass modifier coefficient 2', units='none', type='NUMBER', group='hcpv', required='*')
    module_a3: float = INPUT(label='Air mass modifier coefficient 3', units='none', type='NUMBER', group='hcpv', required='*')
    module_a4: float = INPUT(label='Air mass modifier coefficient 4', units='none', type='NUMBER', group='hcpv', required='*')
    module_ncells: float = INPUT(label='Number of cells', units='none', type='NUMBER', group='hcpv', required='*', constraints='INTEGER')
    module_mjeff: Array = INPUT(label='Module junction efficiency array', units='percent', type='ARRAY', group='hcpv', required='*')
    module_rad: Array = INPUT(label='POA irradiance array', units='W/m^2', type='ARRAY', group='hcpv', required='*')
    module_reference: float = INPUT(label='Index in arrays of the reference condition', units='none', type='NUMBER', group='hcpv', required='*', constraints='INTEGER')
    module_a: float = INPUT(label='Equation variable (a), at high irradiance & low wind speed', units='none', type='NUMBER', group='hcpv', required='*')
    module_b: float = INPUT(label='Equation variable (b), rate at which module temp drops', units='none', type='NUMBER', group='hcpv', required='*')
    module_dT: float = INPUT(label='Equation variable (dT), temp diff between heat sink & cell', units='C', type='NUMBER', group='hcpv', required='*')
    module_temp_coeff: float = INPUT(label='Temperature coefficient', units='%/C', type='NUMBER', group='hcpv', required='*')
    inv_snl_c0: float = INPUT(label='Parameter defining the curvature (parabolic) of the relationship between ac-power and dc-power at the reference operating condition, default value of zero gives a linear relationship, (1/W)', units='xxx', type='NUMBER', group='hcpv', required='*')
    inv_snl_c1: float = INPUT(label='Empirical coefficient allowing Pdco to vary linearly with dc-voltage input, default value is zero, (1/V)', units='xxx', type='NUMBER', group='hcpv', required='*')
    inv_snl_c2: float = INPUT(label='Empirical coefficient allowing Pso to vary linearly with dc-voltage input, default value is zero, (1/V)', units='xxx', type='NUMBER', group='hcpv', required='*')
    inv_snl_c3: float = INPUT(label='Empirical coefficient allowing Co to vary linearly with dc-voltage input, default value is zero, (1/V)', units='xxx', type='NUMBER', group='hcpv', required='*')
    inv_snl_paco: float = INPUT(label='W maximum ac-power rating for inverter at reference or nominal operating condition, assumed to be an upper limit value, (W)', units='xxx', type='NUMBER', group='hcpv', required='*')
    inv_snl_pdco: float = INPUT(label='W dc-power level at which the ac-power rating is achieved at the reference operating condition, (W)', units='xxx', type='NUMBER', group='hcpv', required='*')
    inv_snl_pnt: float = INPUT(label='W ac-power consumed by inverter at night (night tare) to maintain circuitry required to sense PV array voltage, (W)', units='xxx', type='NUMBER', group='hcpv', required='*')
    inv_snl_pso: float = INPUT(label='W dc-power required to start the inversion process, or self-consumption by inverter, strongly influences inverter efficiency at low power levels, (W)', units='xxx', type='NUMBER', group='hcpv', required='*')
    inv_snl_vdco: float = INPUT(label='V (Vnom) dc-voltage level at which the ac-power rating is achieved at the reference operating condition, (V)', units='xxx', type='NUMBER', group='hcpv', required='*')
    inv_snl_vdcmax: float = INPUT(label='V (Vdcmax) dc-voltage maximum operating voltage, (V)', units='xxx', type='NUMBER', group='hcpv', required='*')
    array_modules_per_tracker: float = INPUT(label='Modules on each tracker', units='none', type='NUMBER', group='hcpv', required='*', constraints='INTEGER')
    array_num_trackers: float = INPUT(label='Number of trackers', units='none', type='NUMBER', group='hcpv', required='*', constraints='INTEGER')
    array_num_inverters: float = INPUT(label='Number of inverters', units='none', type='NUMBER', group='hcpv', required='*')
    array_wind_stow_speed: float = INPUT(label='Allowed wind speed before stowing', units='m/s', type='NUMBER', group='hcpv', required='*')
    array_tracker_power_fraction: float = INPUT(label='Single tracker power fraction', units='0..1', type='NUMBER', group='hcpv', required='*')
    array_rlim_el_min: float = INPUT(label='Tracker minimum elevation angle', units='deg', type='NUMBER', group='hcpv', required='*')
    array_rlim_el_max: float = INPUT(label='Tracker maximum elevation angle', units='deg', type='NUMBER', group='hcpv', required='*')
    array_rlim_az_min: float = INPUT(label='Tracker minimum azimuth angle', units='deg', type='NUMBER', group='hcpv', required='*')
    array_rlim_az_max: float = INPUT(label='Tracker maximum azimuth angle', units='deg', type='NUMBER', group='hcpv', required='*')
    array_enable_azalt_sf: float = INPUT(label='Boolean for irradiance derate', units='0-1', type='NUMBER', group='hcpv', required='*', constraints='INTEGER')
    azaltsf: Matrix = INPUT(label='Azimuth-Altitude Shading Table', type='MATRIX', group='hcpv', required='*')
    array_monthly_soiling: Array = INPUT(label='Monthly soiling factors array', units='0..1', type='ARRAY', group='hcpv', required='*')
    array_dc_mismatch_loss: float = INPUT(label='DC module mismatch loss factor', units='0..1', type='NUMBER', group='hcpv', required='*')
    array_dc_wiring_loss: float = INPUT(label='DC Wiring loss factor', units='0..1', type='NUMBER', group='hcpv', required='*')
    array_diode_conn_loss: float = INPUT(label='Diodes and connections loss factor', units='0..1', type='NUMBER', group='hcpv', required='*')
    array_ac_wiring_loss: float = INPUT(label='AC wiring loss factor', units='0..1', type='NUMBER', group='hcpv', required='*')
    array_tracking_error: float = INPUT(label='General racking error', units='0..1', type='NUMBER', group='hcpv', required='*')
    hourly_solazi: Final[Array] = OUTPUT(label='Hourly solar azimuth', units='deg', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_solzen: Final[Array] = OUTPUT(label='Hourly solar zenith', units='deg', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_sazi: Final[Array] = OUTPUT(label='Tracker azimuth', units='deg', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_stilt: Final[Array] = OUTPUT(label='Tracker tilt', units='deg', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_sunup: Final[Array] = OUTPUT(label='Sun up? (0/1)', units='0 or 1', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_beam: Final[Array] = OUTPUT(label='Beam irradiance', units='kW/m2', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_tdry: Final[Array] = OUTPUT(label='Ambient dry bulb temperature', units='C', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_windspd: Final[Array] = OUTPUT(label='Wind speed', units='m/s', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_airmass: Final[Array] = OUTPUT(label='Relative air mass', units='none', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_shading_derate: Final[Array] = OUTPUT(label='Shading derate', units='none', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_poa: Final[Array] = OUTPUT(label='POA on cell', units='W/m2', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_input_radiation: Final[Array] = OUTPUT(label='Input radiation', units='kWh', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_tmod: Final[Array] = OUTPUT(label='Module backplate temp', units='C', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_tcell: Final[Array] = OUTPUT(label='Cell temperature', units='C', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_celleff: Final[Array] = OUTPUT(label='Cell efficiency', units='%', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_modeff: Final[Array] = OUTPUT(label='Module efficiency', units='%', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_dc: Final[Array] = OUTPUT(label='DC gross', units='kWh', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_dc_net: Final[Array] = OUTPUT(label='DC net', units='kWh', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    hourly_ac: Final[Array] = OUTPUT(label='AC gross', units='kWh', type='ARRAY', group='Hourly', required='*', constraints='LENGTH=8760')
    monthly_energy: Final[Array] = OUTPUT(label='Monthly Energy', units='kWh', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    monthly_beam: Final[Array] = OUTPUT(label='Beam irradiance', units='kW/m2', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    monthly_input_radiation: Final[Array] = OUTPUT(label='Input radiation', units='kWh', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    monthly_dc_net: Final[Array] = OUTPUT(label='DC net', units='kWh', type='ARRAY', group='Monthly', required='*', constraints='LENGTH=12')
    annual_energy: Final[float] = OUTPUT(label='Annual Energy', units='kWh', type='NUMBER', group='Annual', required='*')
    annual_beam: Final[float] = OUTPUT(label='Beam irradiance', units='kW/m2', type='NUMBER', group='Annual', required='*')
    annual_input_radiation: Final[float] = OUTPUT(label='Input radiation', units='kWh', type='NUMBER', group='Annual', required='*')
    annual_dc: Final[float] = OUTPUT(label='DC gross', units='kWh', type='NUMBER', group='Annual', required='*')
    annual_dc_net: Final[float] = OUTPUT(label='DC net', units='kWh', type='NUMBER', group='Annual', required='*')
    annual_ac: Final[float] = OUTPUT(label='AC gross', units='kWh', type='NUMBER', group='Annual', required='*')
    tracker_nameplate_watts: Final[float] = OUTPUT(label='Tracker nameplate', units='watts', type='NUMBER', group='Miscellaneous', required='*')
    modeff_ref: Final[float] = OUTPUT(label='Module efficiency', units='-', type='NUMBER', group='Miscellaneous', required='*')
    dc_loss_stowing_kwh: Final[float] = OUTPUT(label='Annual stowing power loss', units='kWh', type='NUMBER', group='Annual', required='*')
    ac_loss_tracker_kwh: Final[float] = OUTPUT(label='Annual tracker power loss', units='kWh', type='NUMBER', group='Annual', required='*')
    dc_nominal: Final[float] = OUTPUT(label='Annual DC nominal', units='kWh', type='NUMBER', group='Annual', required='*')
    capacity_factor: Final[float] = OUTPUT(label='Capacity factor', units='%', type='NUMBER', required='*')
    kwh_per_kw: Final[float] = OUTPUT(label='First year kWh/kW', units='kWh/kW', type='NUMBER', required='*')
    adjust_constant: float = INPUT(name='adjust:constant', label='Constant loss adjustment', units='%', type='NUMBER', group='Loss Adjustments', required='*', constraints='MAX=100')
    adjust_hourly: Array = INPUT(name='adjust:hourly', label='Hourly loss adjustments', units='%', type='ARRAY', group='Loss Adjustments', required='?', constraints='LENGTH=8760')
    adjust_periods: Matrix = INPUT(name='adjust:periods', label='Period-based loss adjustments', units='%', type='MATRIX', group='Loss Adjustments', required='?', constraints='COLS=3', meta='n x 3 matrix [ start, end, loss ]')
    gen: Final[Array] = OUTPUT(label='System power generated', units='kW', type='ARRAY', group='Time Series', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 file_name: str = ...,
                 system_capacity: float = ...,
                 module_cell_area: float = ...,
                 module_concentration: float = ...,
                 module_optical_error: float = ...,
                 module_alignment_error: float = ...,
                 module_flutter_loss_coeff: float = ...,
                 module_a0: float = ...,
                 module_a1: float = ...,
                 module_a2: float = ...,
                 module_a3: float = ...,
                 module_a4: float = ...,
                 module_ncells: float = ...,
                 module_mjeff: Array = ...,
                 module_rad: Array = ...,
                 module_reference: float = ...,
                 module_a: float = ...,
                 module_b: float = ...,
                 module_dT: float = ...,
                 module_temp_coeff: float = ...,
                 inv_snl_c0: float = ...,
                 inv_snl_c1: float = ...,
                 inv_snl_c2: float = ...,
                 inv_snl_c3: float = ...,
                 inv_snl_paco: float = ...,
                 inv_snl_pdco: float = ...,
                 inv_snl_pnt: float = ...,
                 inv_snl_pso: float = ...,
                 inv_snl_vdco: float = ...,
                 inv_snl_vdcmax: float = ...,
                 array_modules_per_tracker: float = ...,
                 array_num_trackers: float = ...,
                 array_num_inverters: float = ...,
                 array_wind_stow_speed: float = ...,
                 array_tracker_power_fraction: float = ...,
                 array_rlim_el_min: float = ...,
                 array_rlim_el_max: float = ...,
                 array_rlim_az_min: float = ...,
                 array_rlim_az_max: float = ...,
                 array_enable_azalt_sf: float = ...,
                 azaltsf: Matrix = ...,
                 array_monthly_soiling: Array = ...,
                 array_dc_mismatch_loss: float = ...,
                 array_dc_wiring_loss: float = ...,
                 array_diode_conn_loss: float = ...,
                 array_ac_wiring_loss: float = ...,
                 array_tracking_error: float = ...,
                 adjust_constant: float = ...,
                 adjust_hourly: Array = ...,
                 adjust_periods: Matrix = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
