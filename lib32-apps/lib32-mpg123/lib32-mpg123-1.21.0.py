metadata = """
summary @ A console based real time MPEG Audio Player for Layer 1, 2 and 3
homepage @ http://sourceforge.net/projects/mpg123
license @ GPL2 LGPL2.1
src_url @ http://downloads.sourceforge.net/sourceforge/mpg123/mpg123-$version.tar.bz2
arch @ ~x86_64
options @ ipv6
"""

depends = """
build @ dev-util/pkg-config sys-devel/libtool media-libs/alsa-lib
"""

srcdir = "mpg123-%s" % version
get("main/lib32_utils")


def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

def configure():
    flags()
    raw_configure('--with-audio="alsa"',
                  "--prefix=/usr",
                  "--libdir=/usr/lib32",
                  "--with-cpu=i586")

def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/{bin,include,share}"% install_dir)