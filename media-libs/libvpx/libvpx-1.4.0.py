metadata = """
summary @ The VP8 Codec SDK
homepage @ http://www.webmproject.org/
license @ BSD
src_url @ https://github.com/webmproject/$name/archive/v$version.tar.gz
arch @ ~x86_64
options @ altivec debug mmx postproc sse sse2 sse3 ssse3 sse4_1 threads cpudetection
"""

depends = """
runtime @ sys-libs/glibc
build @ dev-lang/yasm
"""

srcdir = name+"-"+version

def configure():
    raw_configure("--prefix=/usr \
        --enable-vp8 \
        --enable-vp9 \
        --enable-runtime-cpu-detect \
        --enable-shared \
        --enable-postproc \
        --enable-pic \
        --disable-install-docs \
        --disable-install-srcs")

def install():
    raw_install("DIST_DIR=%s/usr" % install_dir)

    insdoc("LICENSE")
