metadata = """
summary @ X11 damaged region extension library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libXdamage-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libXfixes x11-proto/damageproto
build @ lib32-apps/lib32-libXfixes
"""

srcdir = "libXdamage-%s" % version
get("main/lib32_utils")


def install():
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/{bin,include,share}"% install_dir)