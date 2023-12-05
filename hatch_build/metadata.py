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
import os
import re
from typing import Final

# mypy: allow_any_unimported
from hatchling.metadata.plugin.interface import MetadataHookInterface


_VERSION_FILE = 'samlib/__version__.py'


class CustomMetadataHook(MetadataHookInterface):
    """Update the version from environment variables or version file."""

    def update(self, metadata: dict) -> None:
        build_version = BuildVersion(metadata['version'])
        metadata['version'] = build_version.version
        self.config['__version__'] = build_version


class BuildVersion:
    """Helper object to aid version file reading and writing.

    Generates a version number here in a form that can be passed to builders.
    """

    __slots__ = 'version', 'ssc_release'

    def __init__(self, api_version: str) -> None:
        ssc_release = os.environ.get('SSC_RELEASE')
        if ssc_release:
            version = self.build_version(api_version, ssc_release)
        else:
            version, ssc_release = self.load()
        version += os.environ.get('SAMLIB_EXTRA_VERSION', '')
        self.version: Final = version
        self.ssc_release: Final = ssc_release

    @staticmethod
    def build_version(api_version: str, ssc_release: str) -> str:
        match = re.match(r'^(?:\w+\.)+ssc\.(\d+)$', ssc_release, re.I)
        if match is None:
            raise ValueError(f"expected ssc_release in the form YYYY.MM.DD[.rcN].ssc.REV; got {ssc_release!r}")
        ssc_revision = match.group(1)
        api_major, api_minor = api_version.split('.', 1)
        version = f'{api_major}.{ssc_revision}.{api_minor}'
        return version

    @staticmethod
    def load() -> tuple[str, str]:
        spec = importlib.util.spec_from_file_location('__version__', _VERSION_FILE)
        assert spec is not None
        module = importlib.util.module_from_spec(spec)
        try:
            assert spec.loader is not None
            spec.loader.exec_module(module)
        except FileNotFoundError:
            raise ValueError('Building from git requires setting the SSC_RELEASE environment variable')
        return module.VERSION, module.SSC_RELEASE

    def dump(self) -> str:
        print(f'Using SSC {self.ssc_release}')
        with open(_VERSION_FILE, 'w', encoding='utf-8') as file:
            file.write(f'''
# This is a generated file

import typing as _typing

VERSION: _typing.Final = {self.version!r}
SSC_RELEASE: _typing.Final = {self.ssc_release!r}
''')
        return _VERSION_FILE
