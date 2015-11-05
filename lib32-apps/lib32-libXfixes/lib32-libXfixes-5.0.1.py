metadata = """
summary @ X11 miscellaneous 'fixes' extension library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXfixes-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-proto/fixesproto x11-libs/libX11
build @ x11-misc/util-macros lib32-apps/lib32-libX11
"""

srcdir = "libXfixes-%s" % version
get("main/lib32_utils")

