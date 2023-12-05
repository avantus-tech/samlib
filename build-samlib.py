import argparse
import os
import pathlib
import subprocess
import sys


def main() -> None:
    parser = argparse.ArgumentParser(description='Kick off a samlib build.',
                                     usage='%(prog)s [OPTIONS...] [--] [BUILD_OPTIONS...]',
                                     epilog='Use `%(prog)s -- --help` for build help.')
    parser.add_argument('--build-dir', default=None, metavar='DIR',
                        dest='SSC_BUILD_DIR',
                        help='Build directory.')
    parser.add_argument('--debug', action='store_const', const='yes', default=None,
                        dest='SSC_BUILD_DEBUG',
                        help='Perform a debug build.')
    parser.add_argument('--extra-version', default=None,
                        dest='SAMLIB_EXTRA_VERSION',
                        help='String to append to generated version (e.g., .1, rc2, or .post1)')
    parser.add_argument('--jobs', type=int, default=None, metavar='N',
                        dest='SSC_BUILD_JOBS',
                        help='Number of parallel build jobs.')
    parser.add_argument('--patches', default=None,
                        dest='SSC_PATCHES',
                        help='Patches to apply to SSC source (from patches directory).')
    parser.add_argument('--plat-name', default=None,
                        dest='PLATFORM_NAME',
                        help='Build platform name (e.g., manylinux2010_x86_64)')
    parser.add_argument('--ssc-release', metavar='TAG', default=None,
                        dest='SSC_RELEASE',
                        help='Tag of SSC release to build')
    opts, build_args = parser.parse_known_args(sys.argv[1:])

    if opts.SSC_BUILD_DIR is None:
        opts.SSC_BUILD_DIR = str(pathlib.Path(__file__).absolute().parent / 'build')
    elif opts.SSC_BUILD_DIR:
        opts.SSC_BUILD_DIR = os.path.abspath(opts.SSC_BUILD_DIR)

    env = os.environ.copy()
    for key, value in opts.__dict__.items():
        if value is not None:
            env[key] = str(value)
        else:
            env.pop(key, None)

    if build_args and build_args[0] == '--':
        build_args = build_args[1:]
    sys.exit(subprocess.run([sys.executable, '-m', 'build', *build_args], env=env).returncode)


if __name__ == '__main__':
    main()
