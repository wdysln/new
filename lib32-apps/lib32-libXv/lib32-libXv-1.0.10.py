metadata = """
summary @ X11 Video extension library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXv-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-proto/videoproto x11-libs/libXext lib32-apps/lib32-libXext
"""

srcdir = "libXv-%s" % version

get("main/lib32_utils")
