metadata = """
summary @ a library that exposes a event API on top of Linux futexes
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libxshmfence-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libSM x11-libs/libX11
build @ x11-misc/util-macros
"""

srcdir = "libxshmfence-%s" % version


get("main/lib32_utils")


def install():
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/{bin,include,share}"% install_dir)