
1. Build sdist and wheel on Linux:

       docker run -it --rm --volume "$PWD":/home/samlib:rw --user "$UID:$GID" \
         --workdir /home/samlib quay.io/pypa/manylinux_2_28_x86_64 \
         bash -c 'env SSC_BUILD_DIR="$PWD/build/manylinux" SSC_BUILD_JOBS=10 \
         PLATFORM_NAME="$AUDITWHEEL_PLAT" SSC_RELEASE=2020.2.29.r2.ssc.240 \
         uv build --cache-dir "$PWD/build/.cache"'

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
