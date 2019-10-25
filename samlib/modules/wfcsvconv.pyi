
# This is a generated file

"""wfcsvconv - Converter for TMY2, TMY3, INTL, EPW, SMW weather files to standard CSV format"""

# VERSION: 1

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {
    'input_file': str,
        'output_file': str,
        'output_folder': str,
        'output_filename_format': str
}, total=False)

class Data(ssc.DataDict):
    input_file: str = INPUT(label='Input weather file name', type='STRING', group='Weather File Converter', required='*', meta='tmy2,tmy3,intl,epw,smw')
    output_file: str = INOUT(label='Output file name', type='STRING', group='Weather File Converter', required='?')
    output_folder: str = INPUT(label='Output folder', type='STRING', group='Weather File Converter', required='?')
    output_filename_format: str = INPUT(label='Output file name format', type='STRING', group='Weather File Converter', required='?', meta='recognizes $city $state $country $type $loc')

    def __init__(self, *args: Mapping[str, Any],
                 input_file: str = ...,
                 output_file: str = ...,
                 output_folder: str = ...,
                 output_filename_format: str = ...) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
