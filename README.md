# samlib

_Samlib_ is a high-level Python wrapper to the [_SAM_ _SSC_ library](https://github.com/NREL/ssc/)
from the [_SAM_ SDK](https://sam.nrel.gov/sdk).


## Overview

_Samlib_ uses [cffi](https://pypi.org/project/cffi/) to build Pythonic library
bindings to the _SAM_ _SSC_ library. It includes _typing_ stubs for static type
analysis and code completion.


## Installation

Install _samlib_ using *pip*:
```shell
pip install samlib
```


## Example usage

```python
import samlib
from samlib.modules import pvsamv1

wfd = samlib.Data()  # weather forecast data
wfd.lat = 38.743212
wfd.lon = -117.431238
...

data = pvsamv1.Data()
data.solar_resource_data = wfd
data.use_wf_albedo = 0
...

module = pvsamv1.Module()
module.exec(data)

# Use results saved in data
```


## Versioning

_Samlib_ uses semantic versioning with a twist. The version includes the _SSC_
revision number after the API major version and before the remaining API
version: _major.REV.minor_. This provides for pinning _samlib_ to a particular
API version or to a combination of API + _SSC_ revision. The _SSC_ revision is
the final component of _SSC_ release versions.

Here are a couple of examples:
* `samlib ~= 1.0` specifies _samlib_ API version 0, using the latest _SSC_ revision.
* `samlib ~= 1.240.0` specifies _samlib_ API version 0, using _SSC_ revision 240
  (which corresponds to SSC release _2020.2.29.r2.ssc.240_)

The major version is incremented for potentially breaking _samlib_ API changes
while the minor version is incremented for non-breaking API changes. There may
be additional _.N_ suffixes for releases with duplicate _SSC_ library revisions
or _rcN_ or _.postN_ suffixes for release candidates or post-release,
build-only updates.


## License

_Samlib_ is provided under a [BSD 3-Clause license](LICENSE).

The _SAM_ _SSC_, distributed in binary form in _samlib_ wheels, is also
licensed under a [BSD 3-clause license](SSC-LICENSE).


## Building

Building requires _cmake_ >= 3.24, a C++ compiler, and the Python _build_
package, which can be installed with `pip install --upgrade build`.

On windows, _cmake_ can be installed using `winget install --id Kitware.CMake`.

_CMake_ and _SSC_ options can be set using environment variables. See the
[_CMake_](https://cmake.org/cmake/help/latest/) and
[_SSC_](https://github.com/NREL/SAM/wiki) documentation for more details.

Environment variables may be provided to control the build.

#### Variables for building sdist or wheel targets:

SSC_RELEASE=TAG

: SSC revision to download and build; TAG should match an SSC tag from the NREL
  SSC git repository in the form `YYYY.MM.DD[.rcN].ssc.REV`. This variable is
  required when building sdist or wheel distributions from git source.

SAMLIB_EXTRA_VERSION=X

: Append X to the generated wheel version

#### Variables for building wheel targets:

SSC_BUILD_DIR=PATH

: Absolute path to a build directory; can speed up repeated builds

SSC_BUILD_JOBS=N

: Number of parallel build jobs

SSC_BUILD_DEBUG=yes

: Enable debug build

SSC_PATCHES=LIST

: A space-separated list of patches (without suffix), from the patches
  directory, to apply before building

PLATFORM_NAME=NAME

: Build platform name (e.g., manylinux2010_x86_64) The _wheel_ build target
  requires environment variables to control the build.

The _build-samlib.py_ script provides a wrapper for building _samlib_ source
and wheel distributions and sets the appropriate environment variables based
on the options provided during execution.


### Universal wheels

Building universal (fat) wheels on macOS requires a recent SDK. Execute the
following command, replacing the deployment target if desired.

```shell
env MACOSX_DEPLOYMENT_TARGET=10.9 CMAKE_OSX_ARCHITECTURES="arm64;x86_64" CFLAGS="-arch arm64 -arch x86_64" \
  python build-samlib.py --build-dir build/macos --plat-name macosx_10_9_universal2
```


### Building *manylinux* wheels

Building *manylinux* wheels requires *docker* and one of the
[manylinux](https://github.com/pypa/manylinux) docker images.

1. Pull the latest *manylinux* image for the desired architecture:
```shell
docker pull quay.io/pypa/manylinux_2_28_x86_64
```
2. Open a bash shell in the docker container:
```shell
docker run -it --rm --volume $PWD:/home/samlib:rw --user $UID:$GID --workdir /home/samlib quay.io/pypa/manylinux_2_28_x86_64 bash -l
```
3. Build a wheel for each desired Python version:
```shell
/opt/python/cp38-cp38/bin/python build-samlib.py --build-dir=build/manylinux --jobs=10 --plat-name=$AUDITWHEEL_PLAT
```
4. Exit the shell and docker container:
```shell
exit
```

Optionally, this one command can be used to build wheels for a range of Python versions:
```shell
docker pull quay.io/pypa/manylinux_2_28_x86_64 && \
docker run -it --rm --volume "$PWD":/home/samlib:rw --user "$UID:$GID" --workdir /home/samlib \
  quay.io/pypa/manylinux_2_28_x86_64 bash -c \
  'for v in {10..12}; do /opt/python/cp3$v-cp3$v/bin/python build-samlib.py --build-dir=build/manylinux --jobs=10 --plat-name="$AUDITWHEEL_PLAT"; done'
```


### Build issues

The following are build issues that might occur and possible solutions.

#### <limits> C++ header not included

_SSC_ revision 267, 268, and 274 may fail to build on Linux with the following error:

```
error: ‘numeric_limits’ is not a member of ‘std’
```

Applying the _limits_ patch should fix the issue.

```shell
env SAMLIB_PATCHES="limits" ... pyproject-build
```

#### gcc with -Werror=alloc-size-larger-than=

Recent versions of gcc may produce an error similar to the following error when building:

```
error: argument 1 range [18446744056529682432, 18446744073709551608] exceeds maximum object size 9223372036854775807 [-Werror=alloc-size-larger-than=]
   52 |   dest = (type *) malloc( sizeof(type)*size ); \
      |                   ~~~~~~^~~~~~~~~~~~~~~~~~~~~
```

This check can be disabled by setting `CXXFLAGS="-Wno-error=alloc-size-larger-than="`:

```shell
env CXXFLAGS="-Wno-error=alloc-size-larger-than=" python build-smalib.py
```

#### Visual Studio is missing ATL build tools

If _C++ ATL Build Tools_ haven't been installed for Visual Studio, the following error may be seen:

```
fatal error C1083: Cannot open include file: 'AtlBase.h': No such file or directory
```
