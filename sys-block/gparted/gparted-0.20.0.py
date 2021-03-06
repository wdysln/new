metadata = """
summary @ A Partition Magic clone, frontend to GNU Parted
homepage @ http://gparted.sourceforge.net
license @ GPL
src_url @ http://downloads.sourceforge.net/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-block/parted dev-cpp/gtkmm
"""
def prepare ():
    export("CXXFLAGS", "-g -O2 -std=c++11")
    
def configure():
    conf("--disable-static --disable-doc")


def install():
    raw_install("DESTDIR=%s" % install_dir)
