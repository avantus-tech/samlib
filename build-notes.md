# How to build official wheels

There are multiple methods to build official wheels to publish to PyPI. The GitHub workflow method
is the easiest and least prone to build issues. It is the recommended method.

But sometimes it may be necessary to build packages manually, so steps are also included for
building assuming a Linux host system with Windows and macOS virtual machines or remote hosts.


## GitHub workflows

1. Push changes, if any, to a branch in the *samlib* GitHub repo.
2. Check the [SSC releases](https://github.com/NREL/ssc/releases) and decide which release to build wheels for.
3. Kick off a build from the [*Build packages* workflow on the Actions tab](https://github.com/avantus-tech/samlib/actions/workflows/build.yaml)
   by submitting the SSC release from the previous step using the *Run workflow* dropdown.
4. Once the build completes successfully, download the artifacts and extract the source and wheel
   archives and test them.
5. After tests indicate the wheels are working, copy the *run ID* from the build in step 3 and
   submit it to the [*Publish packages* workflow](https://github.com/avantus-tech/samlib/actions/workflows/publish.yaml).
6. Repeat for additional SSC releases.


## Manual build

1. Build sdist and wheel on Linux:

       docker run -it --rm --volume "$PWD":/home/samlib:rw --user "$UID:$GID" \
         --workdir /home/samlib quay.io/pypa/manylinux_2_28_x86_64 \
         bash -c 'env SSC_BUILD_DIR="$PWD/build/manylinux" SSC_BUILD_JOBS=10 \
         PLATFORM_NAME="$AUDITWHEEL_PLAT" SSC_RELEASE=2020.2.29.r2.ssc.240 \
         uv build --cache-dir "$PWD/build/.cache"'

   or

       docker run -it --rm --volume "$PWD":/home/samlib:rw --user "$UID:$GID" \
         --workdir /home/samlib quay.io/pypa/manylinux_2_28_x86_64 \
         bash -c '/opt/python/cp310-cp310/bin/python build-samlib.py \
         --build-dir build/manylinux --jobs 10 --plat-name "$AUDITWHEEL_PLAT" \
         --ssc-release 2020.2.29.r2.ssc.240 -- --cache-dir build/.cache'

2. Transfer sdist to macos:

       scp dist/samlib-1.240.1.tar.gz macos:devel/samlib-build

3. SSH into macOS box and build universal wheel:

       env MACOSX_DEPLOYMENT_TARGET=10.9 CMAKE_OSX_ARCHITECTURES="arm64;x86_64" \
         CFLAGS="-arch arm64 -arch x86_64" PLATFORM_NAME=macosx_10_9_universal2 \
         SSC_BUILD_DIR=$HOME/devel/samlib-build/build SSC_BUILD_JOBS=8 \
         uv build --wheel samlib-1.240.1.tar.gz

4. Transfer resulting wheels back to Linux:

       scp macos:devel/samlib-build/samlib-1.240.1-\*.whl dist/

5. Transfer sdist to Windows:

       scp dist/samlib-1.240.1.tar.gz win10:devel/samlib-build

6. SSH into Windows box and build wheels:

       set SSC_BUILD_DIR="%USERPROFILE%\devel\samlib-build\build"
       set SSC_BUILD_JOBS=8
       set PLATFORM_NAME=win_amd64
       uv build --wheel samlib-1.240.1.tar.gz

7. Transfer wheels back to the Linux box:

       scp win10:devel/samlib-build/samlib-2.240.1-*.whl dist/

8. Test the wheels and then upload to PyPI

       uv publish ...

9. Repeat for additional SSC releases
