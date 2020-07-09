"""Setup script for samlib"""
import os
import pathlib
import shutil
import subprocess
import sys
import tarfile

import setuptools
from distutils.command.build_ext import build_ext as _build_ext
from distutils.dep_util import newer
from distutils.util import get_platform
from distutils import errors
from distutils import log


SAM_VERSION = '2020.2.29.r2'
SSC_REVISION = 240
SSC_BASENAME = f'{SAM_VERSION}.ssc.{SSC_REVISION}'
SSC_DIRNAME = f'ssc-{SSC_BASENAME}'
SSC_TARBALL = f'{SSC_BASENAME}.tar.gz'
SSC_DOWNLOAD_URL = f'https://github.com/NREL/ssc/archive/{SSC_TARBALL}'


class download_ssc(setuptools.Command):
    description = 'download SSC source code'
    user_options = [
        ('build-base=', 'b',
         'base directory for build library'),
        ('force', 'f',
         'forcibly build everything (ignore file timestamps)'),
    ]
    boolean_options = ['force']

    def initialize_options(self):
        self.build_base = None
        self.force = None

    def finalize_options(self):
        if self.force is None:
            self.force = 0
        self.set_undefined_options(
            'build',
            ('build_base', 'build_base'),
        )
        self.tarball_path = pathlib.Path(self.build_base, SSC_TARBALL)

    def run(self):
        import requests

        if self.force or not self.tarball_path.exists():
            log.info(f'downloading {SSC_DOWNLOAD_URL}')
            if not self.dry_run:
                with requests.get(SSC_DOWNLOAD_URL, stream=True) as response:
                    response.raise_for_status()
                    response.raw.decode_content = True
                    parent = self.tarball_path.parent
                    try:
                        if not parent.exists():
                            parent.mkdir(parents=True, exist_ok=True)
                        with open(self.tarball_path, 'wb') as tarball:
                            shutil.copyfileobj(response.raw, tarball)
                    except:
                        self.tarball_path.unlink()
                        raise


class build_ssc(setuptools.Command):
    description = 'build SSC library'
    user_options = [
        ('build-base=', 'b',
         'base directory for build library'),
        ('debug', 'g',
         "compile with debugging information"),
        ('force', 'f',
         "forcibly build everything (ignore file timestamps)"),
        ('parallel=', 'j',
         "number of parallel build jobs"),
    ]
    boolean_options = ['debug', 'force']
    sub_commands = [
        ('download_ssc', lambda _: True),
    ]

    def initialize_options(self):
        self.build_base = None
        self.debug = None
        self.force = None
        self.parallel = None

    def finalize_options(self):
        self.set_undefined_options(
            'build_ext',
            ('build_base', 'build_base'),
            ('debug', 'debug'),
            ('force', 'force'),
            ('parallel', 'parallel'),
        )
        if isinstance(self.parallel, str):
            try:
                self.parallel = int(self.parallel)
            except ValueError:
                raise errors.DistutilsOptionError("parallel should be an integer")
        self.build_path = pathlib.Path(self.build_base, 'ssc', SSC_DIRNAME)
        self.source_path = pathlib.Path(self.build_base, 'src', SSC_DIRNAME)
        self.tarball_path = pathlib.Path(self.build_base, SSC_TARBALL)

    def extract(self):
        if self.force or not (self.source_path/'CMakeLists.txt').exists():
            if not self.tarball_path.exists():
                self.run_command('download_ssc')
            log.info(f'extracting {self.tarball_path}')
            if not self.dry_run:
                with tarfile.open(self.tarball_path) as tarball:
                    tarball.extractall(self.source_path.parent)

    def spawn(self, cmd, **kwargs):
        log.info(' '.join(cmd))
        if self.dry_run:
            return
        rc = subprocess.run(cmd, **kwargs).returncode
        if rc:
            sys.exit(rc)

    def cmake(self, *additional_args, env=None):
        if not self.build_path.exists():
            self.build_path.mkdir(0o755, parents=True)
        self.spawn(['cmake', *additional_args, '-Dskip_tools=1', '-Dskip_tests=1',
                    str(self.source_path.absolute())], cwd=self.build_path, env=env)
        jobs = (f'-j{self.parallel}',) if self.parallel else ()
        self.spawn(['cmake', '--build', str(self.build_path), *jobs,
                    '--config', 'Debug' if self.debug else 'Release', '--target', 'ssc'], env=env)

    def build_linux(self):
        self.cmake(f'-DCMAKE_BUILD_TYPE={"Debug" if self.debug else "Release"}', '-DSAMAPI_EXPORT=1')

    def build_macos(self):
        self.cmake(f'-DCMAKE_BUILD_TYPE={"Debug" if self.debug else "Release"}')
        source = self.build_path/'ssc/ssc.dylib'
        target = self.build_path/'ssc/libssc.dylib'
        if newer(source, target):
            shutil.copy(source, target)
            try:
                self.spawn(['install_name_tool', '-id', '@loader_path/libssc.dylib', str(target)])
            except:
                target.unlink()
                raise

    def build_windows(self):
        env = {**os.environ, 'SAMNTDIR': str(self.build_path.absolute())}
        (self.build_path/'deploy/x64').mkdir(0o755, parents=True, exist_ok=True)
        self.cmake('-G', 'Visual Studio 16 2019', '-DCMAKE_CONFIGURATION_TYPES=Debug;Release',
                   '-DCMAKE_SYSTEM_VERSION=10.0', '-Dskip_api=1', env=env)

    def run(self):
        self.extract()
        build = {
            'cygwin': self.build_windows,
            'win32': self.build_windows,
            'darwin': self.build_macos,
        }.get(sys.platform, self.build_linux)
        print('building ssc library')
        build()


class build_ext(_build_ext):
    user_options = [
        ('build-base=', 'b',
         'base directory for build library'),
        *_build_ext.user_options,
    ]
    sub_commands = [
        ('build_ssc', lambda _: True),
    ]

    def initialize_options(self):
        super().initialize_options()
        self.build_base = None

    def finalize_options(self):
        super().finalize_options()
        self.set_undefined_options(
            'build',
            ('build_base', 'build_base'),
        )
        self.lib_name = 'sscd' if self.debug else 'ssc'
        self.lib_path = pathlib.Path(self.build_base, 'ssc', SSC_DIRNAME, 'ssc')
        if sys.platform == 'win32':
            self.lib_path /= 'Debug' if self.debug else 'Release'
        self.src_path = pathlib.Path(self.build_base, 'src', SSC_DIRNAME, 'ssc')

    def run(self):
        for cmd in self.get_sub_commands():
            self.run_command(cmd)
        self.setup_ssc()
        super().run()
        self.copy_ssc()

    def read_sscapi(self):
        source = []
        with (self.src_path/'sscapi.h').open() as file:
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

    def setup_ssc(self):
        import cffi

        extension, = self.extensions
        ffibuilder = cffi.FFI()
        ffibuilder.cdef(self.read_sscapi())
        ffibuilder.set_source(extension.name, '#include "sscapi.h"', libraries=[self.lib_name],
                              include_dirs=[str(self.src_path)], library_dirs=[str(self.lib_path)],
                              extra_link_args=(['-Wl,-rpath=${ORIGIN}'] if sys.platform == 'linux' else []))
        if not self.dry_run:
            self.extensions = [ffibuilder.distutils_extension(self.build_temp, self.verbose)]

    def copy_ssc(self):
        ssc = self.lib_name
        if sys.platform in ['win32', 'cygwin']:
            lib_name = f'{ssc}.dll'
        elif sys.platform == 'darwin':
            lib_name = f'lib{ssc}.dylib'
        else:
            lib_name = f'lib{ssc}.so'
        src = self.lib_path/lib_name
        dst = pathlib.Path('.' if self.inplace else self.build_lib, 'samlib', lib_name)
        if newer(src, dst):
            shutil.copy(src, dst)


with open('README.md') as file:
    long_description = file.read()


setuptools.setup(
    name='samlib',
    version='0.2.0.{}'.format(SSC_REVISION),
    python_requires='>=3.6',

    packages=setuptools.find_packages(include=['samlib']),

    ext_modules=[setuptools.Extension('samlib._ssc_cffi', [])],

    include_package_data=True,
    package_data={
        'samlib': ['*.pyi', 'py.typed'],
    },

    install_requires=[
        'cffi>=1.12,<2',
        'mypy-extensions',
        'typing-extensions',
    ],

    setup_requires=[
        'cffi>=1.12,<2',
        'requests',
        'setuptools',
        'wheel',
    ],

    author='Brandon Carpenter',
    author_email='brandon@8minute.com',
    description="High-level library for NREL's SAM Simulation Core (SSC)",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='BSD',
    url='https://bitbucket.org/8minutenergy/samlib',
    zip_safe=False,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering',
        'Typing :: Typed',
    ],

    # Customize extension building to download library
    cmdclass={
        'build_ext': build_ext,
        'build_ssc': build_ssc,
        'download_ssc': download_ssc,
    }
)
