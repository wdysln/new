metadata = """
summary @ An high dynamic-range image file format library
homepage @ http://www.openexr.com/
license @ BSD
src_url @ http://download.savannah.nongnu.org/releases/openexr/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ media-libs/ilmbase sys-libs/zlib
"""

def prepare():
    patch()

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")
