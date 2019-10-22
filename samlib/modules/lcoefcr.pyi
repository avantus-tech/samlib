
# This is a generated file

"""lcoefcr - Calculate levelized cost of energy using fixed charge rate method."""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'capital_cost': float,
        'fixed_operating_cost': float,
        'variable_operating_cost': float,
        'fixed_charge_rate': float,
        'annual_energy': float,
        'lcoe_fcr': float
}, total=False)

class Data(ssc.DataDict):
    capital_cost: float = INPUT(label='Capital cost', units='$', type='NUMBER', group='Simple LCOE', required='*')
    fixed_operating_cost: float = INPUT(label='Annual fixed operating cost', units='$', type='NUMBER', group='Simple LCOE', required='*')
    variable_operating_cost: float = INPUT(label='Annual variable operating cost', units='$/kWh', type='NUMBER', group='Simple LCOE', required='*')
    fixed_charge_rate: float = INPUT(label='Fixed charge rate', type='NUMBER', group='Simple LCOE', required='*')
    annual_energy: float = INPUT(label='Annual energy production', units='kWh', type='NUMBER', group='Simple LCOE', required='*')
    lcoe_fcr: Final[float] = OUTPUT(label='Levelized cost of energy', units='$/kWh', type='NUMBER', group='Simple LCOE', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 capital_cost: float = ...,
                 fixed_operating_cost: float = ...,
                 variable_operating_cost: float = ...,
                 fixed_charge_rate: float = ...,
                 annual_energy: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
