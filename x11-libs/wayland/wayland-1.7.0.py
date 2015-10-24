metadata = """
summary @ Wayland Compositor Infrastructure
homepage @ http://wayland.freedesktop.org/
license @ GPL2
src_url @ http://wayland.freedesktop.org/releases/wayland-1.7.0.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""
def configure():
	autoreconf("-vif")
	conf("--disable-documentation --disable-static")
	
def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
