# samlib

*Samlib* is a high-level Python wrapper to the [SAM SSC library](https://github.com/NREL/ssc/)
from the [SAM SDK](https://sam.nrel.gov/sdk).


## Overview

*Samlib* uses [cffi](https://pypi.org/project/cffi/) to build Pythonic library
bindings to the SAM SSC library. It includes typing stubs for static type
analysis and code completion.


## Installation

Install *samlib* using *pip*:
```shell
pip install samlib
```

If a wheel isn't available for your system, *pip* will attempt to build from
source, which will fail unless a build directory is provided via the
*SSC_BUILD_DIR* environment variable.

```shell
env SSC_BUILD_DIR="" SSC_BUILD_JOBS=4 pip install samlib
```

See [Building](#building) for more information on building *samlib*.


## Example

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

# Use results in data
```


## License

Samlib is provided under a [BSD 3-Clause license](LICENSE).

The SAM SSC, distributed in binary form in samlib wheels, is also
licensed under a [BSD 3-clause license](SSC-LICENSE).


## Building

Building requires *cmake*, a C++ compiler, and the Python *build* package,
which can be installed with `pip install --upgrade build`.

The *wheel* build target uses environment variables to control the build.

#### Required variables:

SSC_BUILD_DIR=PATH
: PATH is an empty string, to build in a temporary directory, or a full path
  to the build directory

#### Optional variables:

SSC_BUILD_JOBS=N
: N is the number of build jobs to run in parallel

SSC_BUILD_DEBUG=yes
: Enable debug build

PLATFORM_NAME=NAME
: Build platform name (e.g., manylinux2010_x86_64)

The *build-samlib.py* script provides a wrapper for building *samlib* source
and wheel distributions and sets the appropriate environment variables based
on the options provided during execution.


### Universal wheels

Building universal (fat) wheels on macOS requires a recent SDK. Execute the
following command, replacing the deployment target if desired.

`env MACOSX_DEPLOYMENT_TARGET=10.9 CMAKE_OSX_ARCHITECTURES="arm64;x86_64" CFLAGS="-arch arm64 -arch x86_64" python build-samlib.py --build-dir build --plat-name macosx_10_9_universal2`


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
docker run -it --rm --volume $PWD:/home/samlib:rw --user $UID:$GID --workdir /home/samlib \
  quay.io/pypa/manylinux_2_28_x86_64 bash -c \
  'for v in {8..12}; do /opt/python/cp3$v-cp3$v/bin/python build-samlib.py --build-dir=build/manylinux --jobs=4 --plat-name=$AUDITWHEEL_PLAT; done'
```


### Build issues

Recent versions of gcc may produce an error similar to the following error when building:

```
error: argument 1 range [18446744056529682432, 18446744073709551608] exceeds maximum object size 9223372036854775807 [-Werror=alloc-size-larger-than=]
   52 |   dest = (type *) malloc( sizeof(type)*size ); \
      |                   ~~~~~~^~~~~~~~~~~~~~~~~~~~~
```

This check can be disabled by setting `CXXFLAGS=-Wno-alloc-size-larger-than`:

```shell
env CXXFLAGS=-Wno-alloc-size-larger-than python build-smalib.py
```
