metadata = """
summary @ X11 Video Motion Compensation extension library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXvMC-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libXv lib32-apps/lib32-libXv
build @ dev-util/pkg-config
"""
srcdir = "libXvMC-%s" % version

get("main/lib32_utils")

