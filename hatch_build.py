import os
import pathlib
import shutil
import subprocess
import sys
import sysconfig
import tarfile
import tempfile
from typing import Any, Dict, List

import cffi
from hatchling.builders.hooks.plugin.interface import BuildHookInterface
import packaging.tags
import requests

# mypy: allow_any_unimported


SSC_BASENAME = '{sam_version}.ssc.{ssc_revision}'
SSC_DIRNAME = f'ssc-{SSC_BASENAME}'
SSC_TARBALL = f'{SSC_BASENAME}.tar.gz'
SSC_DOWNLOAD_URL = f'https://github.com/NREL/ssc/archive/'

IS_WINDOWS = sys.platform in ['win32', 'cygwin']


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version: str, build_data: Dict[str, Any]) -> None:
        try:
            build_dir = os.environ['SSC_BUILD_DIR']
        except KeyError:
            self.app.display_warning('''\
The 'wheel' target uses environment variables to control the build.

Required variables:

   SSC_BUILD_DIR=PATH  - PATH is an empty string, to build in a temporary
                         directory, or a full path to the build directory

Optional variables:

   SSC_BUILD_JOBS=N    - N is the number of build jobs to run in parallel
   SSC_BUILD_DEBUG=yes - Enable debug build
   PLATFORM_NAME=NAME  - Build platform name (e.g., manylinux2010_x86_64)
''')
            self.app.abort("Missing required environment variable 'SSC_BUILD_DIR'")
        if build_dir and not os.path.isabs(build_dir):
            self.app.abort(f"Build path from 'SSD_BUILD_DIR' is not absolute: {build_dir!r}")
        _jobs = os.environ.get('SSC_BUILD_JOBS') or None
        jobs = int(_jobs) if _jobs is not None else None
        debug = os.environ.get('SSC_BUILD_DEBUG', '').lower() in ['y', 'yes', 't', 'true', '1']
        sam_version = self.config['SAM-version']
        ssc_revision = self.config['SSC-revision']
        artifacts = Builder(sam_version, ssc_revision, pathlib.Path(build_dir), jobs=jobs, debug=debug).run()
        if IS_WINDOWS:
            artifacts = [str(pathlib.Path(p).as_posix()) for p in artifacts]  # hatchling expects POSIX paths
        build_data['artifacts'] += artifacts
        platform_name = os.environ.get('PLATFORM_NAME')
        if not platform_name:
            platform_name = sysconfig.get_platform().translate(str.maketrans('.-', '__'))
        build_data['tag'] = str(next(packaging.tags.cpython_tags(platforms=[platform_name])))


class Builder:
    def __init__(self, sam_version: str, ssc_revision: str,
                 build_dir: pathlib.Path, *,
                 jobs: int = None, debug: bool = False) -> None:
        args = dict(sam_version=sam_version, ssc_revision=ssc_revision)
        self.tarball = build_dir/SSC_TARBALL.format(**args)
        self.build_path = build_dir/'ssc'/SSC_DIRNAME.format(**args)
        self.source_path = build_dir/'src'/SSC_DIRNAME.format(**args)
        self.jobs = jobs
        self.debug = debug

        basename = 'sscd' if self.debug else 'ssc'
        if IS_WINDOWS:
            lib_name = f'{"Debug" if debug else "Release"}/{basename}.dll'
        elif sys.platform == 'darwin':
            lib_name = f'lib{basename}.dylib'
        else:
            lib_name = f'lib{basename}.so'
        self.lib_basename = basename
        self.lib_path = self.build_path/'ssc'/lib_name

    def build_lib(self) -> None:
        self.extract_lib_source()
        build = {
            'cygwin': self._build_lib_windows,
            'win32': self._build_lib_windows,
            'darwin': self._build_lib_macos,
        }.get(sys.platform, self._build_lib_linux)
        print('Building SSC library')
        build()

    def extract_lib_source(self) -> None:
        if not (self.source_path/'CMakeLists.txt').exists():
            if not self.tarball.exists():
                self.download_lib_source()
            with tarfile.open(self.tarball) as tar_file:
                tar_file.extractall(self.source_path.parent)

    def download_lib_source(self) -> None:
        if not self.tarball.parent.exists():
            self.tarball.parent.mkdir(0o755, parents=True)
        url = f'{SSC_DOWNLOAD_URL}{self.tarball.name}'
        print(f'Downloading {url} to {self.tarball}')
        with requests.get(url, stream=True) as response, self.tarball.open('wb') as file:
            response.raise_for_status()
            response.raw.decode_content = True
            try:
                shutil.copyfileobj(response.raw, file)
            except:
                self.tarball.unlink()
                raise

    def _build_lib_linux(self) -> None:
        self.cmake(f'-DCMAKE_BUILD_TYPE={"Debug" if self.debug else "Release"}', '-DSAMAPI_EXPORT=1')

    def _build_lib_macos(self) -> None:
        env = {
            **os.environ,
            'CFLAGS': f'-Wno-error=implicit-function-declaration {os.environ.get("CFLAGS", "")}',  # Warn on implicit function declaration
            'CXXFLAGS': f'-D_IOS_VER=1 {os.environ.get("CXXFLAGS", "")}',  # Properly handle definition of finite() macro
        }
        self.cmake(f'-DCMAKE_BUILD_TYPE={"Debug" if self.debug else "Release"}', env=env)
        source = self.build_path/'ssc/ssc.dylib'
        target = self.build_path/'ssc/libssc.dylib'
        if newer(source, target):
            shutil.copy(source, target)
            try:
                spawn(['install_name_tool', '-id', '@loader_path/libssc.dylib', str(target)])
            except:
                target.unlink()
                raise

    def _build_lib_windows(self) -> None:
        env = {**os.environ, 'SAMNTDIR': str(self.build_path.absolute())}
        (self.build_path/'deploy/x64').mkdir(0o755, parents=True, exist_ok=True)
        self.cmake('-G', 'Visual Studio 16 2019', '-DCMAKE_CONFIGURATION_TYPES=Debug;Release',
                   '-DCMAKE_SYSTEM_VERSION=10.0', '-Dskip_api=1', env=env)

    def cmake(self, *additional_args: str, env: Dict[str, str] = None) -> None:
        if not self.build_path.exists():
            self.build_path.mkdir(0o755, parents=True)
        spawn(['cmake', *additional_args, '-Dskip_tools=1', '-Dskip_tests=1',
               str(self.source_path.absolute())], cwd=self.build_path, env=env)
        jobs = [f'-j{self.jobs}'] if self.jobs else []
        spawn(['cmake', '--build', str(self.build_path), *jobs,
               '--config', 'Debug' if self.debug else 'Release', '--target', 'ssc'], env=env)

    def run(self) -> List[str]:
        if not self.lib_path.exists():
            self.build_lib()
        return [
            self.compile_extension(),
            self.copy_lib(),
        ]

    def read_sscapi(self) -> str:
        source = []
        with (self.source_path/'ssc'/'sscapi.h').open() as file:
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
                              include_dirs=[str(self.source_path/'ssc')], library_dirs=[str(self.lib_path.parent)],
                              extra_link_args=(['-Wl,-rpath=${ORIGIN}'] if sys.platform == 'linux' else []))
        with tempfile.TemporaryDirectory() as tmpdir:
            extension = ffibuilder.compile(tmpdir=tmpdir, debug=self.debug)
            dest = pathlib.Path('samlib', os.path.basename(extension))
            shutil.copy(extension, dest)
            return str(dest)

    def copy_lib(self) -> str:
        dest = pathlib.Path('samlib', self.lib_path.name)
        shutil.copyfile(self.lib_path, dest)
        return str(dest)


def spawn(cmd: List[str], **kwargs: Any) -> None:
    print(' '.join(cmd))
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
