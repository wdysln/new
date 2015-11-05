metadata = """
summary @ X11 RandR extension library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXrandr-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libXext x11-libs/libXrender x11-proto/randrproto
build @ x11-misc/util-macros lib32-apps/lib32-libXrender
"""

srcdir = "libXrandr-%s" % version

get("main/lib32_utils")


def configure():
    lib32_conf("--disable-static")