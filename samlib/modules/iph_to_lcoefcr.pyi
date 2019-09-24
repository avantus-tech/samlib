
# This is a generated file

"""iph_to_lcoefcr - Convert annual energy to kWt-hr and adjust fixed cost to include electric parasitic costs."""

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
        'annual_electricity_consumption': float,
        'electricity_rate': float,
        'fixed_operating_cost': float
    }, total=False)

class Data(ssc.DataDict):
    annual_electricity_consumption: float = INPUT(label='Annual electricity consumptoin w/ avail derate', units='kWe-hr', type='NUMBER', group='IPH_LCOH', required='*')
    electricity_rate: float = INPUT(label='Cost of electricity used to operate pumps/trackers', units='$/kWe', type='NUMBER', group='IPH_LCOH', required='*')
    fixed_operating_cost: float = INOUT(label='Annual fixed operating cost', units='$/kW', type='NUMBER', group='Simple LCOE', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 annual_electricity_consumption: float = ...,
                 electricity_rate: float = ...,
                 fixed_operating_cost: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
