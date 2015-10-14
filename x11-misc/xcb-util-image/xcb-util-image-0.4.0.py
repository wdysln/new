metadata = """
summary @ Utility libraries for XC Binding - Port of Xlib's XImage and XShmImage functions
homepage @ http://xcb.freedesktop.org/
license @ MIT
src_url @ http://xcb.freedesktop.org/dist/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libxcb
build @ x11-misc/xcb-util
"""
def build():
    make("check")

def install():
    raw_install("DESTDIR=%s" % install_dir)
