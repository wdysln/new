metadata = """
summary @ Library for Neighbor Discovery Protocol
homepage @ http://libndp.org/
license @ LGPL2.1
src_url @ http://libndp.org/files/libndp-1.5.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    export("HOME", build_dir)
    conf("--disable-static")
    
def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)
