metadata = """
summary @ Print contents of X events
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/archive/individual/app/xev-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc x11-libs/libX11
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
