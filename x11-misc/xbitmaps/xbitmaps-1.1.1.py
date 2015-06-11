metadata = """
summary @ X.org Bitmap files
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/data/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ x11-misc/util-macros
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
