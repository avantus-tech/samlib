# BSD 3-Clause License
#
# Copyright (c) 2020, Avantus LLC
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

import importlib.util
import keyword
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import types
import sysconfig
from typing import Any, Final

# mypy: allow_any_unimported
from hatchling.builders.hooks.plugin.interface import BuildHookInterface
import packaging.tags

import cffi
import requests


SSC_DOWNLOAD_URL: Final = f'https://github.com/NREL/ssc/archive/refs/tags'
IS_WINDOWS: Final = sys.platform in ['win32', 'cygwin']


class CustomBuildHook(BuildHookInterface):
    """Customize wheel building to include the SSC library.

    Builds the SSC library from source and includes it in the binary
    package distribution.

    See README.md for information on environment variables used to control
    the build.
    """

    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        build_dir = os.environ.get('SSC_BUILD_DIR', '')
        if build_dir and not os.path.isabs(build_dir):
            self.app.abort(f"Build path from 'SSC_BUILD_DIR' is not absolute; got {build_dir!r}")

        jobs = os.environ.get('SSC_BUILD_JOBS')
        debug = os.environ.get('SSC_BUILD_DEBUG', '').lower() in ['y', 'yes', 't', 'true', '1']
        patches = os.environ.get('SSC_PATCHES', '').split()

        # Read version and SSC revision form version file
        version_file = self.metadata.config['tool']['hatch']['metadata']['hooks']['custom']['file']
        version, ssc_release = read_version_file(version_file)
        assert version == self.metadata.version, 'version mismatch'
        artifacts = [version_file]

        artifacts += Builder(ssc_release, pathlib.Path(build_dir),
                             jobs=jobs, debug=debug, patches=patches).run()
        if IS_WINDOWS:
            artifacts = [str(pathlib.Path(p).as_posix()) for p in artifacts]  # hatchling expects POSIX paths
        build_data['artifacts'] += artifacts

        # Built packages should depend on the version of cffi used to build ssc
        build_data['dependencies'].append(f'cffi~={cffi.__version__}')
        build_data['pure_python'] = False
        platform_name = os.environ.get('PLATFORM_NAME')
        if not platform_name:
            platform_name = sysconfig.get_platform().translate(str.maketrans('.-', '__'))

        # Derive the interpreter tag version from requires-python in pyproject.toml.
        # Expects that requires-python is something like '>=3.xy'. The tag version
        # is derived by stripping off all characters but digits, producing '3xy'.
        requires_python = self.metadata.config['project']['requires-python']
        interpreter_tag_version = re.sub(r'\D', '', requires_python)
        assert re.match(r'^3\d\d$', interpreter_tag_version), 'unexpected interpreter tag version'
        build_data['tag'] = f'cp{interpreter_tag_version}-abi3-{platform_name}'


def read_version_file(version_file: str) -> tuple[str, str]:
    spec = importlib.util.spec_from_file_location('__version__', version_file)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    try:
        assert spec.loader is not None
        spec.loader.exec_module(module)
    except FileNotFoundError:
        raise ValueError(f'Expected a __version__ module at {version_file} but none was found')
    return module.VERSION, module.SSC_RELEASE


class Builder:
    """Build SSC from source given a release version."""

    def __init__(self, ssc_release: str, build_dir: pathlib.Path, *,
                 jobs: str | None, debug: bool, patches: list[str]) -> None:
        self.tarball: Final = build_dir / f'{ssc_release}.tar.gz'  # Location to download tarball
        self.build_path: Final = build_dir / 'ssc' / f'ssc-{ssc_release}'
        self.source_path: Final = build_dir / 'src' / self.build_path.name
        self.jobs: Final = jobs
        self.debug: Final = debug
        self.patches: Final = patches

        basename = 'sscd' if self.debug else 'ssc'
        if IS_WINDOWS:
            lib_name = f'{"Debug" if debug else "Release"}/{basename}.dll'
        elif sys.platform == 'darwin':
            lib_name = f'lib{basename}.dylib'
        else:
            lib_name = f'lib{basename}.so'
        self.lib_basename: Final = basename
        self.lib_path: Final = self.build_path / 'ssc' / lib_name

    def build_lib(self) -> None:
        self.extract_lib_source()
        self.apply_patches()
        build = {
            'cygwin': self._build_lib_windows,
            'win32': self._build_lib_windows,
            'darwin': self._build_lib_macos,
        }.get(sys.platform, self._build_lib_linux)
        print('Building SSC library')
        build()

    def extract_lib_source(self) -> None:
        if not (self.source_path / 'CMakeLists.txt').exists():
            if not self.tarball.exists():
                self.download_lib_source()
            with tarfile.open(self.tarball) as tar_file:
                tar_file.extractall(self.source_path.parent)
            assert self.source_path.exists(), 'tarball does not contain the expected directory'

    def download_lib_source(self) -> None:
        if not self.tarball.parent.exists():
            self.tarball.parent.mkdir(0o755, parents=True)
        url = f'{SSC_DOWNLOAD_URL}/{self.tarball.name}'
        print(f'Downloading {url} to {self.tarball}')
        with requests.get(url, stream=True) as response, self.tarball.open('wb') as file:
            try:
                response.raise_for_status()
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, file)
            except:
                self.tarball.unlink()
                raise

    def apply_patches(self) -> None:
        applied = set()
        # Reverse previously applied patches that are not requested this run
        for path in (self.source_path / 'applied_patches').glob('*'):
            if path.name not in self.patches:
                self._patch(path.name, reverse=True)
                path.unlink()
            else:
                applied.add(path.name)
        # Apply requested patches
        for name in self.patches:
            if name in applied:
                continue
            self._patch(name)
            path = (self.source_path / f'applied_patches/{name}')
            if not path.parent.exists():
                path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()

    def _patch(self, name: str, reverse: bool = False) -> None:
        args = ['patch']
        if reverse:
            args.append('-R')
        args += '-N', '-p1', '-d', str(self.source_path)
        path = f'patches/{name}.patch'
        print(*args, f'<{path}')
        with open(path, encoding='utf-8') as patch:
            subprocess.run(args, stdin=patch, check=True)

    def _build_lib_linux(self) -> None:
        self._posix_cmake('-DSAMAPI_EXPORT=1')

    def _build_lib_macos(self) -> None:
        env = {
            # Warn on implicit function declaration
            'CFLAGS': f'-Wno-error=implicit-function-declaration {os.environ.get("CFLAGS", "")}',
            # Properly handle definition of finite() macro
            'CXXFLAGS': f'-D_IOS_VER=1 {os.environ.get("CXXFLAGS", "")}',
        }
        self._posix_cmake('-DSAMAPI_EXPORT=0', env=env)
        source = self.build_path / 'ssc/ssc.dylib'
        target = self.build_path / 'ssc/libssc.dylib'
        if newer(source, target):
            shutil.copy(source, target)
            try:
                spawn(['install_name_tool', '-id', '@loader_path/libssc.dylib', str(target)])
            except:
                target.unlink()
                raise

    def _build_lib_windows(self) -> None:
        env = {'SAMNTDIR': str(self.build_path.absolute())}
        (self.build_path / 'deploy/x64').mkdir(0o755, parents=True, exist_ok=True)
        self.cmake('-DCMAKE_CONFIGURATION_TYPES=Debug;Release',
                   '-DCMAKE_SYSTEM_VERSION=10.0', '-Dskip_api=1', env=env)

    def _posix_cmake(self, *additional_args: str, env: dict[str, str] | None = None) -> None:
        self.cmake(f'-DCMAKE_BUILD_TYPE={"Debug" if self.debug else "Release"}',
                   *additional_args, env=env)

    def cmake(self, *additional_args: str, env: dict[str, str] | None = None) -> None:
        if env:
            env = os.environ | env
        if not self.build_path.exists():
            self.build_path.mkdir(0o755, parents=True)
        spawn(['cmake', '--fresh', *additional_args, '-Dskip_tools=1', '-Dskip_tests=1',
               '-DSAM_SKIP_TOOLS=1', '-DSAM_SKIP_TESTS=1',
               str(self.source_path.absolute())], cwd=self.build_path, env=env)
        jobs = [f'-j{self.jobs}'] if self.jobs else []
        spawn(['cmake', '--build', str(self.build_path), *jobs,
               '--config', 'Debug' if self.debug else 'Release', '--target', 'ssc'], env=env)

    def run(self) -> list[str]:
        if not self.lib_path.exists():
            self.build_lib()
        return [
            self.compile_extension(),
            self.copy_lib(),
            *build_stubs(),
        ]

    def read_sscapi(self) -> str:
        source = []
        with (self.source_path / 'ssc' / 'sscapi.h').open(encoding='utf-8') as file:
            for line in file:
                if line.startswith('#endif // __SSCLINKAGECPP__'):
                    break
            for line in file:
                if line.startswith('#ifndef __SSCLINKAGECPP__'):
                    break
                if line.startswith('SSCEXPORT '):
                    line = line[10:]
                source.append(line)
        source.append(r"""
extern "Python" ssc_bool_t _handle_update(ssc_module_t module, ssc_handler_t handler,
       int action, float f0, float f1, const char *s0, const char *s1, void *user_data);
    """)
        return ''.join(source)

    def compile_extension(self) -> str:
        ffibuilder = cffi.FFI()
        ffibuilder.cdef(self.read_sscapi())
        ffibuilder.set_source('samlib._ssc_cffi', '#include "sscapi.h"', libraries=[self.lib_basename],
                              include_dirs=[str(self.source_path / 'ssc')], library_dirs=[str(self.lib_path.parent)],
                              extra_link_args=(['-Wl,-rpath=${ORIGIN}'] if sys.platform == 'linux' else []))

        # From the cffi package documentation at https://cffi.readthedocs.io/en/stable/cdef.html#id14
        #
        # New in version 1.8: the C code produced by emit_c_code() or compile() contains #define
        # Py_LIMITED_API. This means that on CPython >= 3.2, compiling this source produces a
        # binary .so/.dll that should work for any version of CPython >= 3.2 (as opposed to only
        # for the same version of CPython x.y). However, the standard distutils package will still
        # produce a file called e.g. NAME.cpython-35m-x86_64-linux-gnu.so. You can manually rename
        # it to NAME.abi3.so, or use setuptools version 26 or later. Also, note that compiling with
        # a debug version of Python will not actually define Py_LIMITED_API, as doing so makes
        # Python.h unhappy.
        with tempfile.TemporaryDirectory() as tmpdir:
            ext = 'pyd' if sys.platform == 'win32' else 'so'
            extension = ffibuilder.compile(tmpdir=tmpdir, debug=self.debug, target=f'_ssc_cffi.{ext}')
            dest = pathlib.Path('src/samlib', os.path.basename(extension))
            shutil.copy(extension, dest)
            return str(dest)

    def copy_lib(self) -> str:
        dest = pathlib.Path('src/samlib', self.lib_path.name)
        shutil.copyfile(self.lib_path, dest)
        return str(dest)


def spawn(cmd: list[str], **kwargs: Any) -> None:
    print(*cmd)
    rc = subprocess.run(cmd, **kwargs).returncode
    if rc:
        sys.exit(rc)


def newer(a: os.PathLike, b: os.PathLike) -> bool:
    try:
        st_b = os.stat(b)
    except FileNotFoundError:
        return True
    st_a = os.stat(a)
    return st_a.st_mtime > st_b.st_mtime


def build_stubs() -> list[str]:
    """Generate module stubs by inspecting the SSC library."""
    # Bootstrap the _ssc module since it is generated by this script, but is
    # also required by samlib.ssc, imported next.
    sys.modules['samlib._ssc'] = _ssc = types.ModuleType('samlib._ssc')
    name_map: dict[str, str] = {}
    _ssc._name_map = types.MappingProxyType(name_map)  # type: ignore[attr-defined]

    spec = importlib.util.spec_from_file_location('samlib', 'src/samlib/__init__.py')
    assert spec is not None
    samlib = importlib.util.module_from_spec(spec)
    sys.modules['samlib'] = samlib
    assert spec.loader is not None
    spec.loader.exec_module(samlib)

    _data_types = {
        samlib.DataType.STRING: 'str',
        samlib.DataType.NUMBER: 'float',
        samlib.DataType.ARRAY: 'Array',
        samlib.DataType.MATRIX: 'Matrix',
        samlib.DataType.TABLE: 'Table',
    }
    word = re.compile(r'^\w+$')
    non_word = re.compile(r'[^\w]+')

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

    artifacts: list[str] = []
    for entry in samlib.iter_entries():
        module = check_name(entry.name)
        names = set()
        attrs: list[str] = []
        params: list[str] = []
        keys: list[str] = []
        for var in entry.module():
            name = check_name(var.name)
            if name in names:
                continue  # skip duplicate name
            names.add(name)
            data_type = _data_types[var.data_type]
            keys.append(f'{var.name!r}: {data_type}')
            if var.var_type == samlib.VarType.OUTPUT:
                data_type = f'Final[{data_type}]'
            else:
                params.append(f'{name}: {data_type} = ...')
            attr = ', '.join(
                f'{key}={value!r}'
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
            )
            attrs.append(f'{name}: {data_type} = {var.var_type.name}({attr})')
        artifacts.append(_write_module_stub(module, entry, attrs, params, keys))
    artifacts.append(_write_ssc(name_map))
    return artifacts


def _write_module_stub(module: str, entry: Any, attrs: list[str],
                       params: list[str], keys: list[str]) -> str:
    data_attrs = f'\n    '.join(attrs)
    data_kwargs = f',\n{" " * 17}'.join(params)
    dict_keys = f',\n    '.join(keys)
    with open(f'src/samlib/modules/{module}.pyi', 'w', encoding='utf-8') as file:
        file.write(f'''
# This is a generated file

"""{entry.name} - {entry.description}"""

# VERSION: {entry.version}

from typing import Any, Final, Mapping, TypedDict

from .. import ssc
from ._types import *

DataDict = TypedDict('DataDict', {{
    {dict_keys}
}}, total=False)

class Data(ssc.DataDict):
    {data_attrs}

    def __init__(self, *args: Mapping[str, Any],
                 {data_kwargs}) -> None: ...
    def to_dict(self) -> DataDict: ...  # type: ignore[override]

class Module(ssc.Module[Data]):
    def __init__(self) -> None: ...
''')
    return file.name


def _write_ssc(name_map: dict[str, str]) -> str:
    names = '\n'.join(f'    {k!r}: {v!r},' for k, v in name_map.items())
    with open('src/samlib/_ssc.py', 'w', encoding='utf-8') as file:
        file.write(f'''
# This is a generated file

import types as _types
import typing as _typing

_name_map: _typing.Final = _types.MappingProxyType({{
{names}
}})
''')
    return file.name
