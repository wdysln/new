metadata = """
summary @ Utility libraries for XC Binding - client and window-manager helpers for ICCCM
homepage @ http://xcb.freedesktop.org/
license @ MIT
src_url @ http://xcb.freedesktop.org/dist/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libxcb
build @ dev-util/gperf
"""
def build():
    make("check")

def install():
    raw_install("DESTDIR=%s" % install_dir)
