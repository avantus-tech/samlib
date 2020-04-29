import cffi
import sys

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


if __name__ == '__main__':
    ffibuilder.compile(verbose=True)
