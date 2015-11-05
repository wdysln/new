metadata = """
summary @ X cursor management library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXcursor-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libXfixes x11-libs/libXrender lib32-apps/lib32-libXrender
"""
get("main/lib32_utils")

srcdir = "libXcursor-%s" %version

def configure():
    lib32_conf("--disable-static")
    
