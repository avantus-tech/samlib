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

import enum
from types import MappingProxyType
from typing import (Any, Callable, Dict, Generic, Iterator, List, Mapping, NamedTuple,
                    NewType, Optional, overload, Sequence, SupportsFloat, Union, Type, TypeVar)
from typing_extensions import Final

from ._ssc_cffi import ffi as _ffi, lib as _lib
from . import _ssc, _util


_data_t = NewType('_data_t', object)
_entry_t = NewType('_entry_t', object)
_info_t = NewType('_info_t', object)
_module_t = NewType('_module_t', object)

_Data = TypeVar('_Data', bound='DataDict')

_String = Union[bytes, str]
_Number = Union[float, int]
_Array = Sequence[_Number]
_Matrix = Sequence[_Array]


class End(Exception):
    pass


class DataType(enum.Enum):
    STRING = _lib.SSC_STRING
    NUMBER = _lib.SSC_NUMBER
    ARRAY = _lib.SSC_ARRAY
    MATRIX = _lib.SSC_MATRIX
    TABLE = _lib.SSC_TABLE

    @classmethod
    def from_object(cls, obj: Any) -> 'DataType':
        if isinstance(obj, (bytes, str)):
            return cls.STRING
        if isinstance(obj, Sequence):
            if obj and isinstance(obj[0], Sequence):
                return cls.MATRIX
            return cls.ARRAY
        if isinstance(obj, Mapping):
            return cls.TABLE
        return cls.NUMBER

class LogAction(enum.Enum):
    LOG = _lib.SSC_LOG
    UPDATE = _lib.SSC_UPDATE

class LogLevel(enum.Enum):
    NOTICE = _lib.SSC_NOTICE
    WARNING = _lib.SSC_WARNING
    ERROR = _lib.SSC_ERROR

class VarType(enum.Enum):
    INPUT = _lib.SSC_INPUT
    OUTPUT = _lib.SSC_OUTPUT
    INOUT = _lib.SSC_INOUT


class LogMessage(NamedTuple):
    message: str
    level: LogLevel
    time: float

    def __str__(self) -> str:
        return self.message

class ProgressUpdate(NamedTuple):
    message: str
    percent_done: float
    time: float

    def __str__(self) -> str:
        return self.message


class _ReadOnlyMixin:
    def __delattr__(self, name: str) -> None:
        if name in self.__slots__:
            raise AttributeError(f'attribute {name!r} is read-only')
        super().__delattr__(name)

    def __setattr__(self, name: str, value: Any) -> None:
        if name in self.__slots__:
            raise AttributeError(f'attribute {name!r} is read-only')
        super().__setattr__(name, value)


class VarInfo(_ReadOnlyMixin):
    __slots__ = ('_info', 'constraints', 'data_type', 'group', 'index', 'label', 'meta',
                 'module', 'name', 'required', 'uihint', 'units', 'var_type')

    _info: _info_t
    constraints: str
    data_type: DataType
    group: str
    index: int
    label: str
    meta: str
    module: str
    name: str
    required: str
    uihint: str
    units: str
    var_type: VarType

    def __init__(self, module: Union['Module', str], index: int) -> None:
        if not isinstance(module, Module):
            module = Module(module)
        info = _lib.ssc_module_var_info(module._module, index)
        if info == _ffi.NULL:
            raise IndexError(index)
        object.__setattr__(self, '_info', info)
        object.__setattr__(self, 'module', module.name)
        object.__setattr__(self, 'index', index)

    def __getattr__(self, name: str) -> Any:
        get = globals().get(f'info_{name}')
        if get is None:
            raise AttributeError(name)
        value = get(self)
        object.__setattr__(self, name, value)
        return value

    def __eq__(self, other: object) -> bool:
        if isinstance(other, VarInfo):
            return (other.module, other.index) == (self.module, self.index)
        return False

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.module}, {self.index} <{self.name}>)'


class ModuleLog(Sequence[LogMessage]):
    __slots__ = '_module',

    def __init__(self, module: 'Module') -> None:
        self._module = module

    @overload
    def __getitem__(self, index: int) -> LogMessage:
        pass
    @overload
    def __getitem__(self, index: slice) -> Sequence[LogMessage]:
        pass
    def __getitem__(self, index: Union[int, slice]) -> Any:
        if isinstance(index, slice):
            logs = []
            for i in _util.range_from_slice(index):
                log = module_log(self._module, i)
                if log is None:
                    break
                logs.append(log)
            return logs
        log = module_log(self._module, index)
        if log is None:
            raise IndexError
        return log

    def __len__(self) -> int:
        return NotImplemented


class Module(_ReadOnlyMixin, Sequence[VarInfo], Generic[_Data]):
    __slots__ = '_module', 'name'

    _module: _module_t
    name: str

    def __init__(self, name: str) -> None:
        module = _lib.ssc_module_create(_util.encode(name))
        if module == _ffi.NULL:
            raise KeyError(name)
        object.__setattr__(self, '_module', module)
        object.__setattr__(self, 'name', name)

    def __del__(self) -> None:
        try:
            module = self._module
        except AttributeError:
            return
        _lib.ssc_module_free(module)

    @overload
    def __getitem__(self, index: int) -> VarInfo:
        pass
    @overload
    def __getitem__(self, index: slice) -> Sequence[VarInfo]:
        pass
    def __getitem__(self, index: Union[int, slice]) -> Any:
        if isinstance(index, slice):
            vars = []
            for i in _util.range_from_slice(index):
                try:
                    vars.append(VarInfo(self, i))
                except IndexError:
                    break
            return vars
        return VarInfo(self, index)

    def __len__(self) -> int:
        return NotImplemented

    @staticmethod
    def exec_set_print(enable: bool) -> None:
        module_exec_set_print(enable)

    @property
    def log(self) -> ModuleLog:
        return ModuleLog(self)

    def exec(self, data: _Data, *,
             set_print: Optional[bool] = None,
             log_callback: Optional[Callable[[LogMessage], Optional[bool]]] = None,
             progress_callback: Optional[Callable[[ProgressUpdate], Optional[bool]]] = None) -> bool:
        if set_print is not None:
            module_exec_set_print(set_print)
        if log_callback is None and progress_callback is None:
            return module_exec(self, data)
        return module_exec_with_handler(self, data, log_callback, progress_callback)

    __call__ = exec

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Module):
            return other.name == self.name
        return False

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r})'


class Entry(_ReadOnlyMixin):
    __slots__ = '_entry', 'name', 'description', 'index', 'version'

    _entry: _entry_t
    name: str
    description: str
    index: int
    version: int

    def __init__(self, index: int) -> None:
        entry = _lib.ssc_module_entry(index)
        if entry == _ffi.NULL:
            raise IndexError(index)
        object.__setattr__(self, '_entry', entry)
        object.__setattr__(self, 'index', index)

    def __getattr__(self, name: str) -> Any:
        get = globals().get(f'entry_{name}')
        if get is None:
            raise AttributeError(name)
        value = get(self)
        object.__setattr__(self, name, value)
        return value

    def module(self) -> Module:
        return Module(self.name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Entry):
            return other.index == self.index
        return False

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.index})'


class DataDict(Mapping[str, Any]):
    __slots__ = '_data', '_free'

    _data: _data_t
    _free: bool

    def __init__(self, *args: Mapping[str, Any], **kwargs: Any) -> None:
        data = _lib.ssc_data_create()
        if data == _ffi.NULL:
            raise MemoryError('insufficient memory to create object')
        object.__setattr__(self, '_data', data)
        object.__setattr__(self, '_free', True)
        self.update(*args, **kwargs)

    def __del__(self) -> None:
        try:
            free = self._free
        except AttributeError:
            return
        if free:
            _lib.ssc_data_free(self._data)

    @classmethod
    def _from_object(cls: Type[_Data], data: _data_t) -> _Data:
        obj = object.__new__(cls)
        object.__setattr__(obj, '_data', data)
        object.__setattr__(obj, '_free', False)
        return obj

    def clear(self) -> None:
        data_clear(self)

    def rename(self, oldname: str, newname: str) -> None:
        if not data_rename(self, oldname, newname):
            raise KeyError(oldname)

    def query(self, name: str) -> DataType:
        data_type = data_query(self, name)
        if data_type is None:
            raise KeyError(name)
        return data_type

    def __iter__(self) -> Iterator[str]:
        yield from list(iter_data(self))

    def __getitem__(self, name: str) -> Any:
        value = data_get_value(self, name, self.query(name))
        if value is None:
            raise KeyError(name)
        return value

    def __setitem__(self, name: str, value: Any) -> None:
        data_set_value(self, name, DataType.from_object(value), value)

    def __delitem__(self, name: str) -> None:
        self.query(name)
        data_unassign(self, name)

    def __contains__(self, name: object) -> bool:
        if isinstance(name, str):
            return _lib.ssc_query(name) != _ffi.NULL
        return False

    def __len__(self) -> int:
        return NotImplemented

    def __bool__(self) -> bool:
        return not data_empty(self)

    def update(self, *args: Mapping[str, Any], **kwargs: Any) -> None:
        args += (kwargs,)
        for table in args:
            for key, value in table.items():
                self[key] = value

    def to_dict(self) -> Dict[str, Any]:
        return {_util.decode(key): value.to_dict() if isinstance(value, DataDict) else value
                for key, value in self.items()}

    @classmethod
    def from_dict(cls: Type[_Data], table: Mapping[str, Any]) -> _Data:
        data = cls()
        for key, value in table.items():
            if isinstance(value, Mapping):
                value = cls.from_dict(value)
            data[key] = value
        return data


class Data(DataDict):
    def __getattr__(self, name: str) -> Any:
        try:
            return self[_ssc._name_map.get(name, name)]
        except KeyError:
            raise AttributeError(name) from None

    def __setattr__(self, name: str, value: Any) -> None:
        try:
            self[_ssc._name_map.get(name, name)] = value
        except KeyError:
            raise AttributeError(name) from None

    def __delattr__(self, name: str) -> None:
        try:
            del self[_ssc._name_map.get(name, name)]
        except KeyError:
            raise AttributeError(name) from None


def iter_entries() -> Iterator['Entry']:
    i = 0
    while True:
        try:
            yield Entry(i)
        except IndexError:
            return
        i += 1


def version() -> int:
    """Returns the library version number as an integer.

    Version numbers start at 1.
    """
    return _lib.ssc_version()

def build_info() -> str:
    """Returns information about the SCC library build configuration.

    The returned information is for the linked library binary and is a
    text string that lists the compiler, platform, build date/time and
    other information.
    """
    return _util.decode(_ffi.string(_lib.ssc_build_info()))

def data_create() -> Data:
    """Return a new data object.

    A data object stores a table of named values, where each value can
    be of any SSC datatype.
    """
    return Data()

def data_free(data: _Data) -> None:
    """Frees the memory associated with a data object."""
    pass

def data_clear(data: _Data) -> None:
    """Clears all of the variables in a data object."""
    _lib.ssc_data_clear(data._data)

def data_unassign(data: _Data, name: _String) -> None:
    """Unassigns the variable with the specified name."""
    _lib.ssc_data_unassign(data._data, _util.encode(name))

def data_rename(data: _Data, oldname: _String, newname: _String) -> bool:
    """Rename a variable in the data table.

    Returns True if the rename succeeded, False otherwise.
    """
    return _lib.ssc_data_rename(data._data, _util.encode(oldname), _util.encode(newname))

def data_query(data: _Data, name: _String) -> Optional[DataType]:
    """Return the data type of the given attribute in the data object.

    Returns None if name does not exist.
    """
    data_type = _lib.ssc_data_query(data._data, _util.encode(name))
    if data_type == _lib.SSC_INVALID:
        return None
    return DataType(data_type)

def data_first(data: _Data) -> Optional[str]:
    """Returns the name of the first variable in the table.

    Returns None if the data object is empty.
    """
    name = _lib.ssc_data_first(data._data)
    if name == _ffi.NULL:
        return None
    return _util.decode(_ffi.string(name))

def data_next(data: _Data) -> Optional[str]:
    """Returns the name of the next variable in the table.

    Returns None if there are no more variables in the data object.
    """
    name = _lib.ssc_data_next(data._data)
    if name == _ffi.NULL:
        return None
    return _util.decode(_ffi.string(name))

def data_empty(data: _Data) -> bool:
    """Returns True if the given table is empty, False otherwise."""
    return _lib.ssc_data_first(data._data) == _ffi.NULL

def iter_data(data: _Data) -> Iterator[str]:
    """Helper to iterate over all the attributes in a data object.

    Calling this will reset the position for all concurrent iterators.
    """
    name = _lib.ssc_data_first(data._data)
    while name != _ffi.NULL:
        yield _util.decode(_ffi.string(name))
        name = _lib.ssc_data_next(data._data)

def data_set_string(data: _Data, name: _String, value: _String) -> None:
    """Assign a string value to a variable."""
    _lib.ssc_data_set_string(data._data, _util.encode(name), _util.encode(value))

def data_set_number(data: _Data, name: _String, value: SupportsFloat) -> None:
    """Assign a numeric value to a variable."""
    _lib.ssc_data_set_number(data._data, _util.encode(name), float(value))

def data_set_array(data: _Data, name: _String, value: _Array) -> None:
    """Assign a numeric array to a variable."""
    array = _ffi.new('ssc_number_t[]', [float(x) for x in value])
    _lib.ssc_data_set_array(data._data, _util.encode(name), array, len(array))

def data_set_matrix(data: _Data, name: _String, value: _Matrix) -> None:
    """Assign a numeric matrix to a variable."""
    nrows = len(value)
    ncols = max(len(row) for row in value) if nrows else 0
    matrix = _ffi.cast('ssc_number_t *',
                       _ffi.new(f'ssc_number_t[{nrows}][{ncols}]', [[float(x) for x in row] for row in value]))
    _lib.ssc_data_set_matrix(data._data, _util.encode(name), matrix, nrows, ncols)

def data_set_table(data: _Data, name: _String, value: _Data) -> None:
    """Assign a table value to a variable."""
    if not isinstance(value, DataDict):
        value = Data.from_dict(value)
    _lib.ssc_data_set_table(data._data, _util.encode(name), value._data)

def data_get_bytes(data: _Data, name: _String) -> Optional[bytes]:
    """Return a string variable as bytes."""
    string = _lib.ssc_data_get_string(data._data, _util.encode(name))
    if string == _ffi.NULL:
        return None
    return _ffi.string(string)

def data_get_string(data: _Data, name: _String) -> Optional[str]:
    """Return a string variable as a decoded string."""
    string = data_get_bytes(data, name)
    return None if string is None else _util.decode(string)

def data_get_number(data: _Data, name: _String) -> Optional[float]:
    """Return a numeric variable as a float."""
    number = _ffi.new('ssc_number_t *')
    if not _lib.ssc_data_get_number(data._data, _util.encode(name), number):
        return None
    return number[0]

def data_get_array(data: _Data, name: _String) -> Optional[List[float]]:
    """Return an array variable as a list."""
    length = _ffi.new('int *')
    array = _lib.ssc_data_get_array(data._data, _util.encode(name), length)
    if array == _ffi.NULL:
        return None
    return _ffi.unpack(array, length[0])

def data_get_matrix(data: _Data, name: _String) -> Optional[List[List[float]]]:
    """Return a matrix variable as a list of lists."""
    nrows = _ffi.new('int *')
    ncols = _ffi.new('int *')
    matrix = _lib.ssc_data_get_matrix(data._data, _util.encode(name), nrows, ncols)
    if matrix == _ffi.NULL:
        return None
    it = iter(_ffi.unpack(matrix, nrows[0] * ncols[0]))
    return [[next(it) for _ in range(ncols[0])] for _ in range(nrows[0])]

def data_get_table(data: _Data, name: _String) -> Optional[Data]:
    """Return a table variable."""
    table = _lib.ssc_data_get_table(data._data, _util.encode(name))
    if table == _ffi.NULL:
        return None
    return Data._from_object(table)


_getters: Final[Mapping[DataType, Callable[[_Data, _String], Optional[object]]]] = MappingProxyType({
    DataType.STRING: data_get_string,
    DataType.NUMBER: data_get_number,
    DataType.ARRAY: data_get_array,
    DataType.MATRIX: data_get_matrix,
    DataType.TABLE: data_get_table,
})

_setters: Final[Mapping[DataType, Callable[[_Data, _String, Any], None]]] = MappingProxyType({
    DataType.STRING: data_set_string,
    DataType.NUMBER: data_set_number,
    DataType.ARRAY: data_set_array,
    DataType.MATRIX: data_set_matrix,
    DataType.TABLE: data_set_table,
})


def data_get_value(data: _Data, name: _String, data_type: DataType) -> Optional[object]:
    """Helper to get attribute without knowing the data type."""
    try:
        get_value = _getters[data_type]
    except KeyError:
        raise TypeError(f'attribute data type {data_type} is unknown') from None
    return get_value(data, name)

def data_set_value(data: _Data, name: _String, data_type: DataType, value: Any) -> None:
    """Helper to set attribute without knowing the data type."""
    try:
        set_value = _setters[data_type]
    except KeyError:
        raise TypeError(f'attribute data type {data_type} is unknown') from None
    set_value(data, name, value)


def module_entry(index: int) -> Optional[Entry]:
    """Returns compute module information for the i-th module in the SSC library.

    Returns None if the module at the given index does not exist.
    """
    try:
        return Entry(index)
    except IndexError:
        return None

def entry_name(entry: Entry) -> str:
    """Returns the name of a compute module.

    This is the name that is used to create a new compute module.
    """
    return _util.decode(_ffi.string(_lib.ssc_entry_name(entry._entry)))

def entry_description(entry: Entry) -> str:
    """Returns a short text description of a compute module."""
    return _util.decode(_ffi.string(_lib.ssc_entry_description(entry._entry)))

def entry_version(entry: Entry) -> int:
    """Returns a short text description of a compute module."""
    return _lib.ssc_entry_version(entry._entry)

def module_create(name: _String) -> Optional[Module]:
    """Creates an instance of a compute module with the given name.

    Returns None if the given module does not exist.
    """
    try:
        return Module(_util.decode(name))
    except KeyError:
        return None

def module_free(module: Module) -> None:
    """Releases an instance of a compute module created with module_create()."""
    pass

def module_var_info(module: Module, index: int) -> Optional[VarInfo]:
    """Returns reference to a variable info object.

    Returns None if the given index is invalid.
    """
    try:
        return VarInfo(module, index)
    except IndexError:
        return None

def info_var_type(info: VarInfo) -> VarType:
    """Returns variable type information."""
    return VarType(_lib.ssc_info_var_type(info._info))

def info_data_type(info: VarInfo) -> DataType:
    """Returns the data type of the variable."""
    return DataType(_lib.ssc_info_data_type(info._info))

def info_name(info: VarInfo) -> str:
    """Returns the name of the variable."""
    return _util.decode(_ffi.string(_lib.ssc_info_name(info._info)))

def info_label(info: VarInfo) -> str:
    """Returns the short label description of the variable."""
    return _util.decode(_ffi.string(_lib.ssc_info_label(info._info)))

def info_units(info: VarInfo) -> str:
    """Returns the units of the values for the variable."""
    return _util.decode(_ffi.string(_lib.ssc_info_units(info._info)))

def info_meta(info: VarInfo) -> str:
    """Returns any extra information (metadata) for the variable."""
    return _util.decode(_ffi.string(_lib.ssc_info_meta(info._info)))

def info_group(info: VarInfo) -> str:
    """Returns any grouping information for the variable.

    Variables can be assigned to groups for presentation to the user,
    for example.
    """
    return _util.decode(_ffi.string(_lib.ssc_info_group(info._info)))

def info_required(info: VarInfo) -> str:
    """Returns whether a variable is required for a compute module to run.

    It may alternatively be given a default value, specified as '?=<value>'.
    """
    return _util.decode(_ffi.string(_lib.ssc_info_required(info._info)))

def info_constraints(info: VarInfo) -> str:
    """Returns constraints on the values accepted.

    For example, MIN, MAX, BOOLEAN, INTEGER, POSITIVE are possible constraints.
    """
    return _util.decode(_ffi.string(_lib.ssc_info_constraints(info._info)))

def info_uihint(info: VarInfo) -> str:
    """Returns UI hints.

    This is additional information for use in a target application about
    how to show the variable to the user.
    """
    return _util.decode(_ffi.string(_lib.ssc_info_constraints(info._info)))

def module_exec_set_print(print: int) -> None:
    """Set whether modules should print output.

    Specifies whether the built-in execution handler prints messages and
    progress updates to the command line console.
    """
    _lib.ssc_module_exec_set_print(print)

def module_exec_simple(name: str, data: _Data) -> bool:
    """The simplest way to run a computation module over a data set.

    Simply specify the name of the module, and a data set.  If the whole
    process succeeded, the function returns 1, otherwise 0.  No error
    messages are available. This function can be thread-safe, depending
    on the computation module used. If the computation module requires
    the execution of external binary executables, it is not thread-safe.
    However, simpler implementations that do all calculations internally
    are probably thread-safe.  Unfortunately there is no standard way to
    report the thread-safety of a particular computation module.
    """
    return bool(_lib.ssc_module_exec_simple(_util.encode(name), data._data))

def module_exec_simple_nothread(name: str, data: _Data) -> str:
    """Another very simple way to run a computation module over a data set.

    The function returns the empty string on success.  If something went
    wrong, the first error message is returned.  This function is never
    thread-safe.
    """
    error = _lib.ssc_module_exec_simple_nothread(_util.encode(name), data._data)
    return '' if error == _ffi.NULL else _util.decode(error)

def module_exec(module: Module, data: _Data) -> bool:
    """Runs an instantiated computation module over the specified data set.

    Returns True on success, False on failure.  Uses default internal
    built-in handler.  Detailed notices, warnings, and errors can be
    retrieved using the module_log() function.
    """
    return bool(_lib.ssc_module_exec(module._module, data._data))

class _Callbacks:
    def __init__(self, log: Optional[Callable[[LogMessage], Optional[bool]]],
                 progress: Optional[Callable[[ProgressUpdate], Optional[bool]]]) -> None:
        self.handle = _ffi.new_handle(self)
        self.log = log
        self.progress = progress

@_ffi.def_extern()  # type: ignore
def _handle_update(_module: _module_t, _handler: object, action: int, f0: float,
                    f1: float, s0: object, _s1: object, user_data: object) -> bool:
    callbacks = _ffi.from_handle(user_data)
    if action == _lib.SSC_LOG and callbacks.log:
        log = LogMessage(_util.decode(_ffi.string(s0)), LogLevel(int(f0)), f1)
        result = callbacks.log(log)
    elif action == _lib.SSC_UPDATE and callbacks.progress:
        progress = ProgressUpdate(_util.decode(_ffi.string(s0)), f0, f1)
        result = callbacks.progress(progress)
    else:
        return True
    return False if result is False else True

def module_exec_with_handler(
        module: Module, data: _Data,
        log_callback: Optional[Callable[[LogMessage], Optional[bool]]],
        progress_callback: Optional[Callable[[ProgressUpdate], Optional[bool]]]) -> bool:
    """A full-featured way to run a compute module over a data set.

     Supports passing a callback function to handle custom logging,
     progress updates, and cancelation requests. Returns True on
     success, False on failure.
     """
    callbacks = _Callbacks(log_callback, progress_callback)
    return bool(_lib.ssc_module_exec_with_handler(module._module, data._data, _lib._handle_update, callbacks.handle))

def module_log(module: Module, index: int) -> Optional[LogMessage]:
    """Retrive notices, warnings, and error messages from the simulation.

    Returns a LogMessage instance or None if the index passed in was
    invalid.
    """
    level = _ffi.new('int *')
    timestamp = _ffi.new('float *')
    msg = _lib.ssc_module_log(module._module, index, level, timestamp)
    if msg == _ffi.NULL:
        return None
    return LogMessage(_util.decode(_ffi.string(msg)), LogLevel(level[0]), timestamp[0])
