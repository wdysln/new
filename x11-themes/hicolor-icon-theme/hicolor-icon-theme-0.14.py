metadata = """
summary @ Freedesktop.org Hicolor icon theme
homepage @ http://icon-theme.freedesktop.org/wiki/HicolorTheme
license @ GPL2
src_url @ http://icon-theme.freedesktop.org/releases/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
