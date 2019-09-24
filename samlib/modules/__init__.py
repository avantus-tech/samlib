
from .. import ssc


__all__ = ()


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
    return ModuleProxy(name)
