metadata = """
summary @ GObject bindings for libudev
homepage @ https://wiki.gnome.org/Projects/libgudev
license @ LGPL2.1
src_url @ https://download.gnome.org/sources/libgudev/230/libgudev-230.tar.xz
arch @ ~x86_64
"""
srcdir ="libgudev-230"

depends = """
runtime @ sys-libs/glibc
"""

def install():
    raw_install("DESTDIR=%s" % install_dir)
