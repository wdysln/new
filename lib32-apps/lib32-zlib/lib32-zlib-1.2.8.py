metadata = """
summary @ Compression library implementing the deflate compression method found in gzip and PKZIP
homepage @ http://www.zlib.net
license @ ZLIB
src_url @ http://zlib.net/zlib-$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""
srcdir ="zlib-%s" %version


def prepare():
    append_cflags("-O2 -g -m32")
    append_cxxflags("-O2 -g -m32")
    append_ldflags("-O2 -g -m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        

def configure():
    prepare()
    raw_configure("--prefix=/usr \
                  --includedir=/tmp32/include \
                  --libdir=/usr/lib32")

def build():
    prepare()
    make()

def install():
    prepare()
    raw_install("DESTDIR=%s" % install_dir)
    rmdir("/tmp32")
    rmdir("/usr/share")