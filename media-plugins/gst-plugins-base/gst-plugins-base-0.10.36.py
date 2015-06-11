metadata = """
summary @ GStreamer Multimedia Framework Base Plugins + Libraries
homepage @ http://gstreamer.freedesktop.org/
license @ LGPL
src_url @ http://gstreamer.freedesktop.org/src/gst-plugins-base/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ media-libs/gstreamer:0 x11-libs/libXv media-libs/alsa-lib media-libs/libvorbis media-libs/pango
        dev-libs/gobject-introspection dev-util/pkg-config dev-lang/orc
"""


    
def configure():
    export("HOME", build_dir)
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

