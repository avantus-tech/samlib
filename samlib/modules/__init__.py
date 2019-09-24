
from typing import Set

from .. import ssc


__all__ = ()


_modules: Set[str]


class ModuleProxy:
    __slots__ = 'name',

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r})'

    def Module(self) -> ssc.Module:
        return ssc.Module(self.name)

    DataDict = ssc.DataDict
    Data = ssc.Data


def __getattr__(name: str) -> ModuleProxy:
    global _modules
    try:
        _modules
    except NameError:
        _modules = set(entry.name for entry in ssc.iter_entries())
    if name in _modules:
        return ModuleProxy(name)
    raise AttributeError(f'module {name} does not exist')
