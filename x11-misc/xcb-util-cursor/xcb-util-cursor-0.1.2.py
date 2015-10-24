metadata = """
summary @ XCB cursor library
homepage @ http://xcb.freedesktop.org/
license @ MIT
src_url @ http://xcb.freedesktop.org/dist/xcb-util-cursor-0.1.2.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libxcb
build @ x11-misc/xcb-util
"""
def configure():
    conf("--with-pic")
                    
def build():
	make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
