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
def configure():
    append_cxxflags("-lrt")
    append_cxxflags("-pthread -I/usr/include/OpenEXR -I/usr/include/libdrm")
    append_ldflags("-lImath -lHalf -lIex -lIexMath -lIlmThread -lpthread")
    system("./bootstrap")
    conf("--enable-shared \
                         --disable-static")
    
def build():
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")
