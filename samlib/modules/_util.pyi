
from typing import Any, Mapping, Sequence

__all__ = 'Array', 'Matrix', 'Table', 'INPUT', 'INOUT', 'OUTPUT'

Array = Sequence[float]
Matrix = Sequence[Array]
Table = Mapping[str, Any]

def INPUT(**kwargs: str) -> Any: ...
def INOUT(**kwargs: str) -> Any: ...
def OUTPUT(**kwargs: str) -> Any: ...
