metadata = """
summary @ GStreamer Good Plugins + Libraries
homepage @ http://gstreamer.freedesktop.org/
license @ LGPL
src_url @ http://gstreamer.freedesktop.org/src/$name/$fullname.tar.bz2
arch @ ~x86_64
options @ orc
slot @ 0
"""

depends = """
common @ media-libs/gstreamer media-plugins/gst-plugins-base:0 sys-libs/glib
   app-arch/bzip2 sys-libs/zlib
build @ dev-util/gtk-doc
"""

opt_build = """
orc @ dev-lang/orc
"""
def prepare():
    patch(level=1)

def configure():
    conf("--disable-static \
	--disable-esd \
	--disable-rpath \
        --disable-schemas-install")
  
def install():
    raw_install("DESTDIR=%s" % install_dir)
