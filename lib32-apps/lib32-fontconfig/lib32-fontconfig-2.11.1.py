metadata = """
summary @ A library for configuring and customizing font access
homepage @ http://www.fontconfig.org/release/
license @ custom
src_url @ http://www.fontconfig.org/release/fontconfig-$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc media-libs/freetype dev-libs/expat
"""
srcdir = "fontconfig-%s" % version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
    
    
def prepare():
    patch(level=1)
    
def configure():
    flags()
    raw_configure("--prefix=/usr",
                  "--bindir=/tmp32",
                  "--libdir=/usr/lib32")

def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    move("%s/tmp32/fc-cache" % install_dir, "/usr/bin/fc-cache-32")
    system("rm -rf '%s'/usr/{var,etc,include,share}"% install_dir)
    rmdir("/tmp32")
