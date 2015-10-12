metadata = """
summary @ Xfce's freedesktop.org specification compatible menu implementation library
homepage @ http://wiki.xfce.org/dev/garcon
license @ LGPL
src_url @ http://archive.xfce.org/src/libs/garcon/0.5/garcon-$version.tar.bz2
arch @ ~x86_64
options @ debug
"""

depends = """
build @ xfce-base/libxfce4ui xfce-base/libxfce4util
runtime @ sys-libs/glib
"""

def configure():
    conf("--disable-static --disable-gtk3",
    config_enable("debug"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
