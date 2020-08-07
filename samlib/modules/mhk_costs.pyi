
# This is a generated file

"""mhk_costs - Calculates various cost categories for Marine Energy arrays for different device types."""

# VERSION: 3

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'device_rated_power': float,
        'system_capacity': float,
        'devices_per_row': float,
        'marine_energy_tech': float,
        'library_or_input_wec': float,
        'lib_wave_device': str,
        'inter_array_cable_length': float,
        'riser_cable_length': float,
        'export_cable_length': float,
        'structural_assembly_cost_method': float,
        'structural_assembly_cost_input': float,
        'power_takeoff_system_cost_method': float,
        'power_takeoff_system_cost_input': float,
        'mooring_found_substruc_cost_method': float,
        'mooring_found_substruc_cost_input': float,
        'development_cost_method': float,
        'development_cost_input': float,
        'eng_and_mgmt_cost_method': float,
        'eng_and_mgmt_cost_input': float,
        'assembly_and_install_cost_method': float,
        'assembly_and_install_cost_input': float,
        'other_infrastructure_cost_method': float,
        'other_infrastructure_cost_input': float,
        'array_cable_system_cost_method': float,
        'array_cable_system_cost_input': float,
        'export_cable_system_cost_method': float,
        'export_cable_system_cost_input': float,
        'onshore_substation_cost_method': float,
        'onshore_substation_cost_input': float,
        'offshore_substation_cost_method': float,
        'offshore_substation_cost_input': float,
        'other_elec_infra_cost_method': float,
        'other_elec_infra_cost_input': float,
        'structural_assembly_cost_modeled': float,
        'power_takeoff_system_cost_modeled': float,
        'mooring_found_substruc_cost_modeled': float,
        'development_cost_modeled': float,
        'eng_and_mgmt_cost_modeled': float,
        'plant_commissioning_cost_modeled': float,
        'site_access_port_staging_cost_modeled': float,
        'assembly_and_install_cost_modeled': float,
        'other_infrastructure_cost_modeled': float,
        'array_cable_system_cost_modeled': float,
        'export_cable_system_cost_modeled': float,
        'onshore_substation_cost_modeled': float,
        'offshore_substation_cost_modeled': float,
        'other_elec_infra_cost_modeled': float,
        'project_contingency': float,
        'insurance_during_construction': float,
        'reserve_accounts': float,
        'operations_cost': float,
        'maintenance_cost': float
}, total=False)

class Data(ssc.DataDict):
    device_rated_power: float = INPUT(label='Rated capacity of device', units='kW', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0')
    system_capacity: float = INPUT(label='System Nameplate Capacity', units='kW', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0')
    devices_per_row: float = INPUT(label='Number of wave devices per row in array', type='NUMBER', group='MHKCosts', required='*', constraints='INTEGER')
    marine_energy_tech: float = INPUT(label='Marine energy technology', units='0/1', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0,MAX=1', meta='0=Wave,1=Tidal')
    library_or_input_wec: float = INPUT(label='Wave library or user input', type='NUMBER', group='MHKCosts', required='marine_energy_tech=0', meta='0=Library,1=User')
    lib_wave_device: str = INPUT(label='Wave library name', type='STRING', group='MHKCosts', required='marine_energy_tech=0')
    inter_array_cable_length: float = INPUT(label='Inter-array cable length', units='m', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0')
    riser_cable_length: float = INPUT(label='Riser cable length', units='m', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0')
    export_cable_length: float = INPUT(label='Export cable length', units='m', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0')
    structural_assembly_cost_method: float = INPUT(label='Structural assembly cost method', units='0/1/2', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0,MAX=2', meta='0=Enter in $/kW,1=Enter in $,2=Use modeled value')
    structural_assembly_cost_input: float = INPUT(label='Structural assembly cost', units='$', type='NUMBER', group='MHKCosts', required='*')
    power_takeoff_system_cost_method: float = INPUT(label='Power take-off system cost method', units='0/1/2', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0,MAX=2', meta='0=Enter in $/kW,1=Enter in $,2=Use modeled value')
    power_takeoff_system_cost_input: float = INPUT(label='Power take-off system cost', units='$', type='NUMBER', group='MHKCosts', required='*')
    mooring_found_substruc_cost_method: float = INPUT(label='Mooring, foundation, and substructure cost method', units='0/1/2', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0,MAX=2', meta='0=Enter in $/kW,1=Enter in $,2=Use modeled value')
    mooring_found_substruc_cost_input: float = INPUT(label='Mooring, foundation, and substructure cost', units='$', type='NUMBER', group='MHKCosts', required='*')
    development_cost_method: float = INPUT(label='Development cost method', units='0/1/2', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0,MAX=2', meta='0=Enter in $/kW,1=Enter in $,2=Use modeled value')
    development_cost_input: float = INPUT(label='Development cost', units='$', type='NUMBER', group='MHKCosts', required='*')
    eng_and_mgmt_cost_method: float = INPUT(label='Engineering and management cost method', units='0/1/2', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0,MAX=2', meta='0=Enter in $/kW,1=Enter in $,2=Use modeled value')
    eng_and_mgmt_cost_input: float = INPUT(label='Engineering and management cost', units='$', type='NUMBER', group='MHKCosts', required='*')
    assembly_and_install_cost_method: float = INPUT(label='Assembly and installation cost method', units='0/1/2', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0,MAX=2', meta='0=Enter in $/kW,1=Enter in $,2=Use modeled value')
    assembly_and_install_cost_input: float = INPUT(label='Assembly and installation cost', units='$', type='NUMBER', group='MHKCosts', required='*')
    other_infrastructure_cost_method: float = INPUT(label='Other infrastructure cost method', units='0/1/2', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0,MAX=2', meta='0=Enter in $/kW,1=Enter in $,2=Use modeled value')
    other_infrastructure_cost_input: float = INPUT(label='Other infrastructure cost', units='$', type='NUMBER', group='MHKCosts', required='*')
    array_cable_system_cost_method: float = INPUT(label='Array cable system cost method', units='0/1/2', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0,MAX=2', meta='0=Enter in $/kW,1=Enter in $,2=Use modeled value')
    array_cable_system_cost_input: float = INPUT(label='Array cable system cost', units='$', type='NUMBER', group='MHKCosts', required='*')
    export_cable_system_cost_method: float = INPUT(label='Export cable system cost method', units='0/1/2', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0,MAX=2', meta='0=Enter in $/kW,1=Enter in $,2=Use modeled value')
    export_cable_system_cost_input: float = INPUT(label='Export cable system cost', units='$', type='NUMBER', group='MHKCosts', required='*')
    onshore_substation_cost_method: float = INPUT(label='Onshore substation cost method', units='0/1/2', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0,MAX=2', meta='0=Enter in $/kW,1=Enter in $,2=Use modeled value')
    onshore_substation_cost_input: float = INPUT(label='Onshore substation cost', units='$', type='NUMBER', group='MHKCosts', required='*')
    offshore_substation_cost_method: float = INPUT(label='Offshore substation cost method', units='0/1/2', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0,MAX=2', meta='0=Enter in $/kW,1=Enter in $,2=Use modeled value')
    offshore_substation_cost_input: float = INPUT(label='Offshore substation cost', units='$', type='NUMBER', group='MHKCosts', required='*')
    other_elec_infra_cost_method: float = INPUT(label='Other electrical infrastructure cost method', units='0/1/2', type='NUMBER', group='MHKCosts', required='*', constraints='MIN=0,MAX=2', meta='0=Enter in $/kW,1=Enter in $,2=Use modeled value')
    other_elec_infra_cost_input: float = INPUT(label='Other electrical infrastructure cost', units='$', type='NUMBER', group='MHKCosts', required='*')
    structural_assembly_cost_modeled: Final[float] = OUTPUT(label='Modeled structural assembly cost', units='$', type='NUMBER', group='MHKCosts')
    power_takeoff_system_cost_modeled: Final[float] = OUTPUT(label='Modeled power take-off cost', units='$', type='NUMBER', group='MHKCosts')
    mooring_found_substruc_cost_modeled: Final[float] = OUTPUT(label='Modeled mooring, foundation, and substructure cost', units='$', type='NUMBER', group='MHKCosts')
    development_cost_modeled: Final[float] = OUTPUT(label='Modeled development cost', units='$', type='NUMBER', group='MHKCosts')
    eng_and_mgmt_cost_modeled: Final[float] = OUTPUT(label='Modeled engineering and management cost', units='$', type='NUMBER', group='MHKCosts')
    plant_commissioning_cost_modeled: Final[float] = OUTPUT(label='Modeled plant commissioning cost', units='$', type='NUMBER', group='MHKCosts')
    site_access_port_staging_cost_modeled: Final[float] = OUTPUT(label='Modeled site access, port, and staging cost', units='$', type='NUMBER', group='MHKCosts')
    assembly_and_install_cost_modeled: Final[float] = OUTPUT(label='Modeled assembly and installation cost', units='$', type='NUMBER', group='MHKCosts')
    other_infrastructure_cost_modeled: Final[float] = OUTPUT(label='Modeled other infrastructure cost', units='$', type='NUMBER', group='MHKCosts')
    array_cable_system_cost_modeled: Final[float] = OUTPUT(label='Modeled array cable system cost', units='$', type='NUMBER', group='MHKCosts')
    export_cable_system_cost_modeled: Final[float] = OUTPUT(label='Modeled export cable system cost', units='$', type='NUMBER', group='MHKCosts')
    onshore_substation_cost_modeled: Final[float] = OUTPUT(label='Modeled onshore substation cost', units='$', type='NUMBER', group='MHKCosts')
    offshore_substation_cost_modeled: Final[float] = OUTPUT(label='Modeled offshore substation cost', units='$', type='NUMBER', group='MHKCosts')
    other_elec_infra_cost_modeled: Final[float] = OUTPUT(label='Modeled other electrical infrastructure cost', units='$', type='NUMBER', group='MHKCosts')
    project_contingency: Final[float] = OUTPUT(label='Modeled project contingency cost', units='$', type='NUMBER', group='MHKCosts')
    insurance_during_construction: Final[float] = OUTPUT(label='Modeled cost of insurance during construction', units='$', type='NUMBER', group='MHKCosts')
    reserve_accounts: Final[float] = OUTPUT(label='Modeled reserve account costs', units='$', type='NUMBER', group='MHKCosts')
    operations_cost: Final[float] = OUTPUT(label='Operations cost', units='$', type='NUMBER', group='MHKCosts')
    maintenance_cost: Final[float] = OUTPUT(label='Maintenance cost', units='$', type='NUMBER', group='MHKCosts')

    def __init__(self, *args: Mapping[str, Any],
                 device_rated_power: float = ...,
                 system_capacity: float = ...,
                 devices_per_row: float = ...,
                 marine_energy_tech: float = ...,
                 library_or_input_wec: float = ...,
                 lib_wave_device: str = ...,
                 inter_array_cable_length: float = ...,
                 riser_cable_length: float = ...,
                 export_cable_length: float = ...,
                 structural_assembly_cost_method: float = ...,
                 structural_assembly_cost_input: float = ...,
                 power_takeoff_system_cost_method: float = ...,
                 power_takeoff_system_cost_input: float = ...,
                 mooring_found_substruc_cost_method: float = ...,
                 mooring_found_substruc_cost_input: float = ...,
                 development_cost_method: float = ...,
                 development_cost_input: float = ...,
                 eng_and_mgmt_cost_method: float = ...,
                 eng_and_mgmt_cost_input: float = ...,
                 assembly_and_install_cost_method: float = ...,
                 assembly_and_install_cost_input: float = ...,
                 other_infrastructure_cost_method: float = ...,
                 other_infrastructure_cost_input: float = ...,
                 array_cable_system_cost_method: float = ...,
                 array_cable_system_cost_input: float = ...,
                 export_cable_system_cost_method: float = ...,
                 export_cable_system_cost_input: float = ...,
                 onshore_substation_cost_method: float = ...,
                 onshore_substation_cost_input: float = ...,
                 offshore_substation_cost_method: float = ...,
                 offshore_substation_cost_input: float = ...,
                 other_elec_infra_cost_method: float = ...,
                 other_elec_infra_cost_input: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
