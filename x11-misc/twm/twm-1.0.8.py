metadata = """
summary @ X.Org initialisation program
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/archive/individual/app/$name-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libX11 x11-misc/util-macros
"""


def configure():
    conf()

def install():
    raw_install("DESTDIR=%s" % install_dir)

