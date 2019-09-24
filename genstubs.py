
import keyword
from pathlib import Path
import re
from typing import Dict

from samlib import ssc


_data_types = {
    ssc.DataType.STRING: 'str',
    ssc.DataType.NUMBER: 'float',
    ssc.DataType.ARRAY: 'Array',
    ssc.DataType.MATRIX: 'Matrix',
    ssc.DataType.TABLE: 'Table',
}

def gen_stubs(sam_path):
    word = re.compile(r'^\w+$')
    non_word = re.compile(r'[^\w]+')
    name_map: Dict[str, str] = {}

    def check_name(entry_name: str) -> str:
        name = entry_name
        if word.match(name) is None:
            name = non_word.sub('_', name)
        if name[0].isnumeric():
            name = f'_{name}'
        if keyword.iskeyword(name):
            name = f'{name}_'
        if name != entry_name:
            assert name_map.get(name) in [None, entry_name]
            name_map[name] = entry_name
        return name

    modules = []
    for entry in ssc.iter_entries():
        module = check_name(entry.name)
        modules.append(module)
        vars = set()
        attrs = []
        params = []
        keys = []
        for var in entry.module():
            name = check_name(var.name)
            if name in vars:
                continue  # skip duplicate name
            vars.add(name)
            data_type = _data_types[var.data_type]
            keys.append(f'{var.name!r}: {data_type}')
            if var.var_type == ssc.VarType.OUTPUT:
                data_type = f'Final[{data_type}]'
            else:
                params.append(f'{name}: {data_type} = ...')
            attr = [
                (key, value)
                for key, value in [
                    ('name', '' if name == var.name else var.name),
                    ('label', var.label),
                    ('units', var.units),
                    ('type', var.data_type.name),
                    ('group', var.group),
                    ('required', var.required),
                    ('constraints', var.constraints),
                    ('meta', var.meta),
                ]
                if value
            ]
            attr = ', '.join(f'{k}={v!r}' for k, v in attr)
            attrs.append(f'{name}: {data_type} = {var.var_type.name}({attr})')

        attrs = f'\n    '.join(attrs)
        params = f',\n{" " * 17}'.join(params)
        keys = f',\n        '.join(keys)
        with (sam_path / 'modules' / f'{module}.pyi').open('w') as file:
            file.write(f'''
# This is a generated file

"""{entry.name} - {entry.description}"""

# VERSION: {entry.version}

from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

try:
    from mypy_extensions import TypedDict
except ImportError:
    DataDict = Dict[str, Any]
else:
    DataDict = TypedDict('DataDict', {{
        {keys}
    }}, total=False)

class Data(ssc.DataDict):
    {attrs}

    def __init__(self, *args: Mapping[str, Any],
                 {params}) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
''')

    names = '\n'.join(f'    {k!r}: {v!r},' for k, v in name_map.items())
    with (sam_path / '_ssc.py').open('w') as file:
        file.write(f'''
# This is a generated file

_name_map = {{
{names}
}}
''')
    return modules


if __name__ == '__main__':
    path: Path = Path(ssc.__file__).parent
    modules = gen_stubs(path)
    extra = set(p.name for p in (path / 'modules').glob('*.pyi')) - {f'{name}.pyi' for name in modules}
    extra -= {'_util.pyi'}
    if extra:
        print('Extra (unknown) stubs:', ', '.join(extra))
