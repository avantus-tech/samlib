"""setup - Setup script for samlib"""

# More information on the formatting of this file and the directives may
# be found in the setuptools documentation.
#
#   https://setuptools.readthedocs.io/en/latest/setuptools.html

from distutils.command.build_ext import build_ext as _build_ext
from distutils.dep_util import newer_group
from distutils import log, spawn
import math
import pathlib
import shutil
import ssl
import sys
import urllib.request
import zipfile

import cffi
from setuptools import Command, find_packages, setup


ssc_revision = 209
ssc_version = '2018.11.11.r4'
ssc_zip_name = f'sam-sdk-{ssc_revision}_{"_".join(ssc_version.rsplit(".", 1))}.zip'
ssc_url = f'https://github.com/NREL/ssc/releases/download/{ssc_version}/{ssc_zip_name}'
ssc_zip = pathlib.Path('sam-sdk', ssc_zip_name)


class download(Command):
    description = 'download the SSC library'
    user_options = [
        ('force', 'f',
         'download even if the file already exists'),
    ]
    boolean_options = ['force']

    def initialize_options(self):
        self.force = False

    def finalize_options(self):
        pass

    def run(self):
        if not self.force and ssc_zip.exists():
            log.debug(f'skipping download; {ssc_zip} exists')
            return
        log.info(f'downloading {ssc_url}')
        if not self.dry_run:
            ctx = ssl.create_default_context(cafile=ssc_zip.parent / 'cacert.pem')
            with urllib.request.urlopen(ssc_url, context=ctx) as src, ssc_zip.open('wb') as dst:
                shutil.copyfileobj(src, dst, 8192)


class build_ext(_build_ext):
    sub_commands = [
        ('download', lambda _: True),
    ]

    def run(self):
        for cmd in self.get_sub_commands():
            self.run_command(cmd)
        self.extract_ssc()
        super().run()

    def extract_ssc(self):
        bits = int(math.log2(sys.maxsize) + 1)
        if sys.platform in ['win32', 'cygwin']:
            platform = 'win'
            lib_name = 'ssc.dll'
        elif sys.platform == 'darwin':
            platform = 'osx'
            lib_name = 'libssc.dylib'
        else:
            platform = 'linux'
            lib_name = 'libssc.so'
        sdk_path = pathlib.Path(self.build_temp, 'sam-sdk')
        self.library_dirs.append(str(sdk_path))
        lib_path = sdk_path / lib_name
        if self.force or newer_group([ssc_zip], lib_path, 'newer'):
            log.debug(f'extracting SDK to {sdk_path}')
            if not self.dry_run:
                sdk_path.mkdir(0o755, True, True)
                dirname = f'{platform}{bits}/'
                with zipfile.ZipFile(ssc_zip) as file:
                    for info in file.filelist:
                        if not info.filename.startswith(dirname) or info.is_dir():
                            continue
                        name = info.filename.split('/')[-1]
                        if name in ['ssc.so', 'ssc.dylib']:
                            name = f'lib{name}'
                        with file.open(info, 'r') as src, (sdk_path / name).open('wb') as dst:
                            shutil.copyfileobj(src, dst)
                if platform != 'win':
                    lib_path.chmod(0o755)
                if sys.platform == 'darwin':
                    spawn.spawn(['install_name_tool', '-id', '@loader_path/libssc.dylib', str(lib_path)])
        libssc_path = pathlib.Path('.' if self.inplace else self.build_lib, 'samlib', lib_name)
        if self.force or newer_group([lib_path], libssc_path, 'newer'):
            if not self.dry_run:
                shutil.copyfile(lib_path, libssc_path)
                if platform != 'win':
                    libssc_path.chmod(0o755)


def read_source():
    source = []
    with open('sam-sdk/sscapi.h') as file:
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


ffibuilder = cffi.FFI()
ffibuilder.cdef(read_source())
ffibuilder.set_source('samlib._ssc_cffi', '#include "sscapi.h"',
                      include_dirs=['sam-sdk'], libraries=['ssc'],
                      extra_link_args=(['-Wl,-rpath=${ORIGIN}'] if sys.platform == 'linux' else []))


setup(
    name='samlib',
    version='0.1.1+' + ssc_version,
    python_requires='>=3.6',

    packages=find_packages(include=['samlib']),

    ext_modules=[ffibuilder.distutils_extension()],

    include_package_data=True,
    package_data={
        'samlib': ['*.pyi', 'py.typed'],
    },

    # Required dependencies
    install_requires=[
        'cffi>=1.12',
        'mypy-extensions',
        'typing-extensions',
    ],

    setup_requires=[
        'cffi>=1.12',
        'setuptools',
    ],

    author='8minute Solar Energy',
    author_email='storage@8minute.com',
    description='High-level library for accessing SAM Simulation Core (SSC)',
    license='BSD',
    url='http://www.8minute.com',
    zip_safe=False,

    # Customize extension building to download library
    cmdclass={
        'build_ext': build_ext,
        'download': download,
    }
)
