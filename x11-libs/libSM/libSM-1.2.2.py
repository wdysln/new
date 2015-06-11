metadata = """
summary @ X11 Session Management library
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libSM-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libICE sys-apps/util-linux
build @ x11-misc/util-macros x11-libs/xtrans
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
