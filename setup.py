"""Setup script for samlib"""

from distutils.command.build_ext import build_ext as _build_ext
from distutils.dep_util import newer_group
from distutils import log, spawn
import math
import pathlib
import shutil
import sys
import zipfile

from setuptools import Command, find_packages, setup


SSC_REVISION = 209
SSC_VERSION = '2018.11.11.r4'
SSC_ZIP_NAME = f'sam-sdk-{SSC_REVISION}_{"_".join(SSC_VERSION.rsplit(".", 1))}.zip'
SSC_URL = f'https://github.com/NREL/ssc/releases/download/{SSC_VERSION}/{SSC_ZIP_NAME}'
SSC_ZIP = pathlib.Path('sam-sdk', SSC_ZIP_NAME)


class download(Command):
    description = 'download the SSC library'
    user_options = [
        ('force', 'f',
         'download even if the file already exists'),
    ]
    boolean_options = ['force']

    def initialize_options(self):
        self.force = None

    def finalize_options(self):
        if self.force is None:
            self.force = False

    def run(self):
        import requests

        if not self.force and SSC_ZIP.exists():
            log.debug(f'skipping download; {SSC_ZIP} exists')
            return
        log.info(f'downloading {SSC_URL}')
        if not self.dry_run:
            with requests.get(SSC_URL, stream=True) as response, SSC_ZIP.open('wb') as dst:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, dst)


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
        if self.force or newer_group([SSC_ZIP], lib_path, 'newer'):
            log.debug(f'extracting SDK to {sdk_path}')
            if not self.dry_run:
                sdk_path.mkdir(0o755, True, True)
                dirname = f'{platform}{bits}/'
                with zipfile.ZipFile(SSC_ZIP) as file:
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


with open('README.md') as file:
    long_description = file.read()


setup(
    name='samlib',
    version='0.1.3.{}'.format(SSC_REVISION),
    python_requires='>=3.6',

    packages=find_packages(include=['samlib']),

    cffi_modules=["build_ssc.py:ffibuilder"],

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
    ],

    author='Brandon Carpenter',
    author_email='brandon@8minute.com',
    description="High-level library for using NREL's SAM Simulation Core (SSC)",
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
        'download': download,
    }
)
