metadata = """
summary @ The OpenGL Utility Library
homepage @ http://cgit.freedesktop.org/mesa/glu/
license @ LGPL
src_url @ ftp://ftp.freedesktop.org/pub/mesa/glu/glu-$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ media-libs/mesa
"""

srcdir = "glu-%s" % version


def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

def configure():
    flags()
    raw_configure("--prefix=/usr",
                  "--libdir=/usr/lib32")

def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/include"% install_dir)
