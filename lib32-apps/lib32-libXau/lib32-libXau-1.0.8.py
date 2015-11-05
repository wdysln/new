metadata = """
summary @ X11 authorisation library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXau-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-proto/xproto
"""
get("main/lib32_utils")

srcdir = "libXau-%s" %version

