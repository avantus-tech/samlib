
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
    ssc.DataType.TABLE: "'Data'",
}

def gen_stubs(mod_file, stub_file):
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

    stub_file.write('''
# This is a generated file

from typing import Dict, Sequence
from typing_extensions import Final

Array = Sequence[float]
Matrix = Sequence[Array]

_name_map: Final[Dict[str, str]]
''')
    modules = []
    for entry in ssc.iter_entries():
        module = check_name(entry.name)
        modules.append(module)
        stub_file.write(f'\nclass _{module}:\n')
        vars = set()
        for var in entry.module():
            name = check_name(var.name)
            if name in vars:
                continue  # skip duplicate name
            vars.add(name)
            data_type = _data_types[var.data_type]
            if var.var_type == ssc.VarType.OUTPUT:
                data_type = f'Final[{data_type}]'
            stub_file.write(f'    {name}: {data_type}\n')
    props = '\n'.join(f'''\
    @property
    def {name}(self) -> _{name}: ...''' for name in modules)
    stub_file.write(f'''
class Data:
{props}
''')

    names = '\n'.join(f'    {k!r}: {v!r},' for k, v in name_map.items())
    props = '\n'.join(f'''\
    @property
    def {name}(self):
        return _DataProxy(self)''' for name in modules)
    mod_file.write(f'''
# This is a generated file

_name_map = {{
{names}
}}


class _DataProxy:
    __slots__ = '_data',

    def __init__(self, data):
        object.__setattr__(self, '_data', data)

    def __getattr__(self, name):
        try:
            return self._data[_name_map.get(name, name)]
        except KeyError:
            raise AttributeError(name) from None

    def __setattr__(self, name, value):
        try:
            self._data[_name_map.get(name, name)] = value
        except KeyError:
            raise AttributeError(name) from None

    def __delattr__(self, name):
        try:
            del self._data[_name_map.get(name, name)]
        except KeyError:
            raise AttributeError(name) from None


class Data:
{props}
''')


if __name__ == '__main__':
    mod_path: Path = Path(ssc.__file__).parent / '_ssc.py'
    stub_path = mod_path.with_name(mod_path.name + 'i')
    with mod_path.open('w') as mod_file, stub_path.open('w') as stub_file:
        gen_stubs(mod_file, stub_file)
