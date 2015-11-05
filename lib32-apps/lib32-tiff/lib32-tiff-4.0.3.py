metadata = """
summary @ Library for manipulation of TIFF images
homepage @ http://www.remotesensing.org/libtiff/
license @ custom
src_url @ ftp://ftp.remotesensing.org/pub/libtiff/tiff-$version.tar.gz
arch @ ~x86_64
options @ jpeg lzma
"""

depends = """
runtime @ sys-libs/glibc sys-libs/zlib
build @ media-libs/freeglut x11-libs/libXi x11-libs/libXmu media-libs/mesa
"""

opt_runtime = """
jpeg @ media-libs/jpeg
lzma @ app-arch/xz
"""

srcdir = "tiff-%s" % version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

def configure():
    flags()
    autoreconf("-fi")
    raw_configure("--prefix=/usr \
                    --libdir=/usr/lib32")

def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/{bin,include,share}"% install_dir)