import argparse
import os
import pathlib
import subprocess
import sys


def main() -> None:
    parser = argparse.ArgumentParser(description='Kick off samlib build.',
                                     usage='%(prog)s [OPTIONS...] [--] [BUILD_OPTIONS...]',
                                     epilog='Use `%(prog)s -- --help` for build help.')
    parser.add_argument('--build-dir', default=None, metavar='DIR',
                        help='Build directory.')
    parser.add_argument('--debug', action='store_true', default=False,
                        help='Perform a debug build.')
    parser.add_argument('--jobs', type=int, default=None, metavar='N',
                        help='Number of parallel build jobs.')
    parser.add_argument('--plat-name', default=None,
                        help='Build platform name (e.g., manylinux2010_x86_64)')
    opts, build_args = parser.parse_known_args(sys.argv[1:])

    if opts.build_dir is None:
        opts.build_dir = str(pathlib.Path(__file__).absolute().parent/'build')
    elif opts.build_dir:
        opts.build_dir = os.path.abspath(opts.build_dir)
    env = os.environ.copy()
    env.update({
        'SSC_BUILD_DIR': opts.build_dir,
        'SSC_BUILD_DEBUG': 'yes' if opts.debug else 'no',
    })
    if opts.jobs is not None:
        env['SSC_BUILD_JOBS'] = str(opts.jobs)
    else:
        env.pop('SSC_BUILD_JOBS', None)
    if opts.plat_name:
        env['PLATFORM_NAME'] = opts.plat_name
    else:
        env.pop('PLATFORM_NAME', None)

    if build_args and build_args[0] == '--':
        build_args = build_args[1:]
    sys.exit(subprocess.run([sys.executable, '-m', 'build', *build_args], env=env).returncode)


if __name__ == '__main__':
    main()
