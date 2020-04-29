# BSD 3-Clause License
#
# Copyright (c) 2020, 8minute Solar Energy LLC
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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

from mypy_extensions import TypedDict
from typing import Any, Dict, Mapping
from typing_extensions import Final

from .. import ssc
from ._util import *

DataDict = TypedDict('DataDict', {{
    {keys}
}}, total=False)

class Data(ssc.DataDict):
    {attrs}

    def __init__(self, *args: Mapping[str, Any],
                 {params}) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

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
