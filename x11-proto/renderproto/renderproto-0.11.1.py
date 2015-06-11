metadata = """
summary @ X11 Render extension wire protocol
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/proto/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
