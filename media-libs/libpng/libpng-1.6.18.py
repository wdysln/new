metadata = """
summary @ A collection of routines used to create PNG format graphics files
homepage @ http://www.libpng.org/pub/png/libpng.html
license @ custom
src_url @ http://downloads.sourceforge.net/sourceforge/libpng/$fullname.tar.xz  
	  http://downloads.sourceforge.net/project/libpng-apng/libpng16/1.6.18/libpng-1.6.18-apng.patch.gz
options @ apng static-libs
arch @ ~x86_64
slot @ 1.6
"""

depends = """
runtime @ sys-libs/glibc sys-libs/zlib
"""

def prepare():
    if opt("apng"):
        patch("%s/../libpng-1.6.18-apng.patch" % build_dir, level=1)
        autoreconf("-fi")
        libtoolize()

def configure():
    conf(config_enable("static-libs", "static"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    insdoc("LICENSE")
