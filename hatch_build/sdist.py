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
from typing import Any

# mypy: allow_any_unimported
from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from hatchling.metadata.plugin.interface import MetadataHookInterface


class CustomMetadataHook(MetadataHookInterface):
    """Update the version from environment variables or version file."""

    def update(self, metadata: dict) -> None:
        version, *_ = get_version(self.config)
        metadata['version'] = version


class CustomBuildHook(BuildHookInterface):
    """Customize sdist building to include the SSC library."""

    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        config = self.metadata.config['tool']['hatch']['metadata']['hooks']['custom']
        version, ssc_revision, version_file = get_version(config)
        write_version_file(version, ssc_revision, version_file)
        build_data['artifacts'] = [version_file]


def get_version(config: dict[str, Any]) -> tuple[str, str, str]:
    api_version = str(config['version'])
    version_file = str(config['file'])
    ssc_release = os.environ.get('SSC_RELEASE')
    if ssc_release:
        api_revision = str(config['revision'])
        version = version_from_ssc_release(api_version, api_revision, ssc_release)
    else:
        version, ssc_release = read_version_file(version_file)
    version += os.environ.get('SAMLIB_EXTRA_VERSION', '')
    return version, ssc_release, version_file


def version_from_ssc_release(api_version: str, api_revision: str, ssc_release: str) -> str:
    match = re.match(r'^(?:\w+\.)+ssc\.(\d+)$', ssc_release, re.I)
    if match is None:
        raise ValueError(f'Expected ssc_release in the form YYYY.MM.DD[.rcN].ssc.REV; got {ssc_release!r}')
    ssc_revision = match.group(1)
    return f'{api_version}.{ssc_revision}.{api_revision}'


def read_version_file(version_file: str) -> tuple[str, str]:
    spec = importlib.util.spec_from_file_location('__version__', version_file)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    try:
        assert spec.loader is not None
        spec.loader.exec_module(module)
    except FileNotFoundError:
        raise ValueError('Building from git requires setting the SSC_RELEASE environment variable')
    return module.VERSION, module.SSC_RELEASE


def write_version_file(version: str, ssc_release: str, version_file: str) -> None:
    print(f'Using SSC {ssc_release}')
    with open(version_file, 'w', encoding='utf-8') as file:
        file.write(f'''
# This is a generated file

import typing as _typing

VERSION: _typing.Final = {version!r}
SSC_RELEASE: _typing.Final = {ssc_release!r}
''')
