# samlib

Samlib is a high-level Python wrapper to the [SAM SSC library](https://github.com/NREL/ssc/)
from the [SAM SDK](https://sam.nrel.gov/sdk).

## Overview

Samlib uses [cffi](https://pypi.org/project/cffi/) to build Pythonic library
bindings to the SAM SSC library. It includes mypy stubs for static type analysis
and code completion.

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

The build-samlib.py script provides a nice wrapper for building *samlib* source
and wheel distributions. It requires the *build* package, which can be installed
with `pip install --upgrade build`.

Building universal (fat) wheels on macOS requires a recent SDK. Execute the
following command, replacing the deployment target if desired.

`env MACOSX_DEPLOYMENT_TARGET=10.9 CMAKE_OSX_ARCHITECTURES="arm64;x86_64" CFLAGS="-arch arm64 -arch x86_64" python build-samlib.py --build-dir build --plat-name macosx_10_9_universal2`
