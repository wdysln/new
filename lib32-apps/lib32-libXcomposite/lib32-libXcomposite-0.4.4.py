metadata = """
summary @ X11 Composite extension library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXcomposite-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libXfixes x11-proto/compositeproto lib32-apps/lib32-libX11
"""
get("main/lib32_utils")

srcdir = "libXcomposite-%s" %version

def configure():
    lib32_conf("--disable-static")


