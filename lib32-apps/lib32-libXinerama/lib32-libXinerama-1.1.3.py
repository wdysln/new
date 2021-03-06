metadata = """
summary @ X11 Xinerama extension library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXinerama-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libXext x11-proto/xineramaproto
build @ x11-misc/util-macros
"""

srcdir = "libXinerama-%s" % version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

def configure():
    flags()
    raw_configure("--prefix=/usr \
                    --libdir=/usr/lib32")

def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/{include,share}"% install_dir)
