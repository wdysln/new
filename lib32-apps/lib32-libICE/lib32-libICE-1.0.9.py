metadata = """
summary @ X11 Inter-Client Exchange library
homepage @ http://xorg.freedesktop.org
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libICE-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-proto/xproto
build @ x11-libs/xtrans lib32-apps/lib32-util-linux
"""

get("main/lib32_utils")

srcdir = "libICE-%s" %version
