
# This is a generated file

"""timeseq - Time sequence generator"""

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
        'start_time': float,
        'end_time': float,
        'time_step': float,
        'time': Array,
        'timehr': Array,
        'month': Array,
        'day': Array,
        'hour': Array,
        'minute': Array
    }, total=False)

class Data(ssc.DataDict):
    start_time: float = INPUT(label='Start time', units='seconds', type='NUMBER', group='Time Sequence', required='*', constraints='MIN=0,MAX=31536000', meta='0=jan1st 12am')
    end_time: float = INPUT(label='End time', units='seconds', type='NUMBER', group='Time Sequence', required='*', constraints='MIN=0,MAX=31536000', meta='0=jan1st 12am')
    time_step: float = INPUT(label='Time step', units='seconds', type='NUMBER', group='Time Sequence', required='*', constraints='MIN=1,MAX=3600')
    time: Final[Array] = OUTPUT(label='Time', units='secs', type='ARRAY', group='Time', required='*', meta='0=jan1st 12am')
    timehr: Final[Array] = OUTPUT(label='HourTime', units='hours', type='ARRAY', group='Time', required='*', meta='0=jan1st 12am')
    month: Final[Array] = OUTPUT(label='Month', type='ARRAY', group='Time', required='*', meta='1-12')
    day: Final[Array] = OUTPUT(label='Day', type='ARRAY', group='Time', required='*', meta='1-{28,30,31}')
    hour: Final[Array] = OUTPUT(label='Hour', type='ARRAY', group='Time', required='*', meta='0-23')
    minute: Final[Array] = OUTPUT(label='Minute', type='ARRAY', group='Time', required='*', meta='0-59')

    def __init__(self, *args: Mapping[str, Any],
                 start_time: float = ...,
                 end_time: float = ...,
                 time_step: float = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
