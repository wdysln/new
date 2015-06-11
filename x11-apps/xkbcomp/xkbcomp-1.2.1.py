metadata = """
summary @ X Keyboard description compiler
homepage @ http://xorg.freedesktop.org
license @ custom
src_url @ http://www.x.org/releases/individual/app/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libxkbfile
build @ x11-misc/util-macros
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
