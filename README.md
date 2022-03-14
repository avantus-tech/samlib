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
