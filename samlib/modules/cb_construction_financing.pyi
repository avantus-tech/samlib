
# This is a generated file

"""cb_construction_financing - Construction financing cost calculations"""

# VERSION: 0

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'total_installed_cost': float,
        'const_per_interest_rate1': float,
        'const_per_interest_rate2': float,
        'const_per_interest_rate3': float,
        'const_per_interest_rate4': float,
        'const_per_interest_rate5': float,
        'const_per_months1': float,
        'const_per_months2': float,
        'const_per_months3': float,
        'const_per_months4': float,
        'const_per_months5': float,
        'const_per_percent1': float,
        'const_per_percent2': float,
        'const_per_percent3': float,
        'const_per_percent4': float,
        'const_per_percent5': float,
        'const_per_upfront_rate1': float,
        'const_per_upfront_rate2': float,
        'const_per_upfront_rate3': float,
        'const_per_upfront_rate4': float,
        'const_per_upfront_rate5': float,
        'const_per_principal1': float,
        'const_per_principal2': float,
        'const_per_principal3': float,
        'const_per_principal4': float,
        'const_per_principal5': float,
        'const_per_interest1': float,
        'const_per_interest2': float,
        'const_per_interest3': float,
        'const_per_interest4': float,
        'const_per_interest5': float,
        'const_per_total1': float,
        'const_per_total2': float,
        'const_per_total3': float,
        'const_per_total4': float,
        'const_per_total5': float,
        'const_per_percent_total': float,
        'const_per_principal_total': float,
        'const_per_interest_total': float,
        'construction_financing_cost': float
}, total=False)

class Data(ssc.DataDict):
    total_installed_cost: float = INPUT(label='Total installed cost', units='$', type='NUMBER', group='system costs', required='*')
    const_per_interest_rate1: float = INPUT(label='Interest rate, loan 1', units='%', type='NUMBER', group='financial parameters', required='*')
    const_per_interest_rate2: float = INPUT(label='Interest rate, loan 2', units='%', type='NUMBER', group='financial parameters', required='*')
    const_per_interest_rate3: float = INPUT(label='Interest rate, loan 3', units='%', type='NUMBER', group='financial parameters', required='*')
    const_per_interest_rate4: float = INPUT(label='Interest rate, loan 4', units='%', type='NUMBER', group='financial parameters', required='*')
    const_per_interest_rate5: float = INPUT(label='Interest rate, loan 5', units='%', type='NUMBER', group='financial parameters', required='*')
    const_per_months1: float = INPUT(label='Months prior to operation, loan 1', type='NUMBER', group='financial parameters', required='*')
    const_per_months2: float = INPUT(label='Months prior to operation, loan 2', type='NUMBER', group='financial parameters', required='*')
    const_per_months3: float = INPUT(label='Months prior to operation, loan 3', type='NUMBER', group='financial parameters', required='*')
    const_per_months4: float = INPUT(label='Months prior to operation, loan 4', type='NUMBER', group='financial parameters', required='*')
    const_per_months5: float = INPUT(label='Months prior to operation, loan 5', type='NUMBER', group='financial parameters', required='*')
    const_per_percent1: float = INPUT(label='Percent of tot. installed cost, loan 1', units='%', type='NUMBER', group='financial parameters', required='*')
    const_per_percent2: float = INPUT(label='Percent of tot. installed cost, loan 2', units='%', type='NUMBER', group='financial parameters', required='*')
    const_per_percent3: float = INPUT(label='Percent of tot. installed cost, loan 3', units='%', type='NUMBER', group='financial parameters', required='*')
    const_per_percent4: float = INPUT(label='Percent of tot. installed cost, loan 4', units='%', type='NUMBER', group='financial parameters', required='*')
    const_per_percent5: float = INPUT(label='Percent of tot. installed cost, loan 5', units='%', type='NUMBER', group='financial parameters', required='*')
    const_per_upfront_rate1: float = INPUT(label='Upfront fee on principal, loan 1', units='%', type='NUMBER', group='financial parameters', required='*')
    const_per_upfront_rate2: float = INPUT(label='Upfront fee on principal, loan 2', units='%', type='NUMBER', group='financial parameters', required='*')
    const_per_upfront_rate3: float = INPUT(label='Upfront fee on principal, loan 3', units='%', type='NUMBER', group='financial parameters', required='*')
    const_per_upfront_rate4: float = INPUT(label='Upfront fee on principal, loan 4', units='%', type='NUMBER', group='financial parameters', required='*')
    const_per_upfront_rate5: float = INPUT(label='Upfront fee on principal, loan 5', units='%', type='NUMBER', group='financial parameters', required='*')
    const_per_principal1: Final[float] = OUTPUT(label='Principal, loan 1', units='$', type='NUMBER', group='financial parameters', required='*')
    const_per_principal2: Final[float] = OUTPUT(label='Principal, loan 2', units='$', type='NUMBER', group='financial parameters', required='*')
    const_per_principal3: Final[float] = OUTPUT(label='Principal, loan 3', units='$', type='NUMBER', group='financial parameters', required='*')
    const_per_principal4: Final[float] = OUTPUT(label='Principal, loan 4', units='$', type='NUMBER', group='financial parameters', required='*')
    const_per_principal5: Final[float] = OUTPUT(label='Principal, loan 5', units='$', type='NUMBER', group='financial parameters', required='*')
    const_per_interest1: Final[float] = OUTPUT(label='Interest cost, loan 1', units='$', type='NUMBER', group='financial parameters', required='*')
    const_per_interest2: Final[float] = OUTPUT(label='Interest cost, loan 2', units='$', type='NUMBER', group='financial parameters', required='*')
    const_per_interest3: Final[float] = OUTPUT(label='Interest cost, loan 3', units='$', type='NUMBER', group='financial parameters', required='*')
    const_per_interest4: Final[float] = OUTPUT(label='Interest cost, loan 4', units='$', type='NUMBER', group='financial parameters', required='*')
    const_per_interest5: Final[float] = OUTPUT(label='Interest cost, loan 5', units='$', type='NUMBER', group='financial parameters', required='*')
    const_per_total1: Final[float] = OUTPUT(label='Total financing cost, loan 1', units='$', type='NUMBER', group='financial parameters', required='*')
    const_per_total2: Final[float] = OUTPUT(label='Total financing cost, loan 2', units='$', type='NUMBER', group='financial parameters', required='*')
    const_per_total3: Final[float] = OUTPUT(label='Total financing cost, loan 3', units='$', type='NUMBER', group='financial parameters', required='*')
    const_per_total4: Final[float] = OUTPUT(label='Total financing cost, loan 4', units='$', type='NUMBER', group='financial parameters', required='*')
    const_per_total5: Final[float] = OUTPUT(label='Total financing cost, loan 5', units='$', type='NUMBER', group='financial parameters', required='*')
    const_per_percent_total: Final[float] = OUTPUT(label='Total percent of installed costs, all loans', units='%', type='NUMBER', group='financial parameters', required='*')
    const_per_principal_total: Final[float] = OUTPUT(label='Total principal, all loans', units='$', type='NUMBER', group='financial parameters', required='*')
    const_per_interest_total: Final[float] = OUTPUT(label='Total interest costs, all loans', units='$', type='NUMBER', group='financial parameters', required='*')
    construction_financing_cost: Final[float] = OUTPUT(label='Total construction financing cost', units='$', type='NUMBER', group='financial parameters', required='*')

    def __init__(self, *args: Mapping[str, Any],
                 total_installed_cost: float = ...,
                 const_per_interest_rate1: float = ...,
                 const_per_interest_rate2: float = ...,
                 const_per_interest_rate3: float = ...,
                 const_per_interest_rate4: float = ...,
                 const_per_interest_rate5: float = ...,
                 const_per_months1: float = ...,
                 const_per_months2: float = ...,
                 const_per_months3: float = ...,
                 const_per_months4: float = ...,
                 const_per_months5: float = ...,
                 const_per_percent1: float = ...,
                 const_per_percent2: float = ...,
                 const_per_percent3: float = ...,
                 const_per_percent4: float = ...,
                 const_per_percent5: float = ...,
                 const_per_upfront_rate1: float = ...,
                 const_per_upfront_rate2: float = ...,
                 const_per_upfront_rate3: float = ...,
                 const_per_upfront_rate4: float = ...,
                 const_per_upfront_rate5: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
