metadata = """
summary @ GStreamer Multimedia Framework
homepage @ http://gstreamer.freedesktop.org/
license @ LGPL
src_url @ http://gstreamer.freedesktop.org/src/gstreamer/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/libxml2 sys-libs/glib
build @ dev-util/intltool
"""

def prepare():
    patch(level=1)
    export("AUTOPOINT", "true")
    autoreconf("-vfi")
    
def configure():
    conf('--disable-static',
         '--disable-gtk-doc',
         '--disable-valgrind',
         '--enable-nls',
         '--enable-introspection',
         '--with-package-name="GStreamer (Hadron GNU/Linux)"',
         '--with-package-origin="http://www.hadronproject.org/"')

def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)