metadata = """
summary @ A collection of routines used to create PNG format graphics files
homepage @ http://www.libpng.org/pub/png/libpng.html
license @ custom
src_url @ http://downloads.sourceforge.net/sourceforge/libpng/libpng-$version.tar.bz2  
	  http://downloads.sourceforge.net/project/libpng-apng/libpng15/1.5.14/libpng-1.5.14-apng.patch.gz
options @ apng static-libs
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc sys-libs/zlib
"""
get("main/lib32_utils")

srcdir = "libpng-%s" %version


def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")


def prepare():
    patch("%s/../libpng-1.5.14-apng.patch" % build_dir, level=1)
    autoreconf("-fi")
    libtoolize()

def configure():
    lib32_conf("--program-suffix=-32 --disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/{include,share}"% install_dir)
    rmdir("/tmp32")
