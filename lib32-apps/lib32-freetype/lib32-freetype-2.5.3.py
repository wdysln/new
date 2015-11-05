metadata = """
summary @ TrueType font rendering library
homepage @ http://freetype.sourceforge.net/
license @ GPL
src_url @ http://downloads.sourceforge.net/sourceforge/freetype/freetype-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc sys-libs/zlib
"""
srcdir = "freetype-%s" % version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

def configure():
    flags()
    raw_configure("--prefix=/usr",
                  "--disable-harbuzz",
                  "--without-harfbuzz",
                  "--libdir=/usr/lib32")

def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/{bin,include,share}"% install_dir)