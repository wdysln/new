metadata = """
summary @ Gstreamer FFMpeg Plugin
homepage @ http://gstreamer.freedesktop.org/
license @ LGPL
src_url @ http://gstreamer.freedesktop.org/src/gst-ffmpeg/gst-ffmpeg-0.10.13.tar.bz2
arch @ ~x86_64
"""

depends = """
common @ media-libs/gstreamer:0 media-plugins/gst-plugins-base:0 sys-libs/glib
"""

opt_build = """
orc @ dev-lang/orc
"""

def prepare():
    patch(level = 1)

def configure():
    conf("--disable-static \
--disable-valgrind \
--without-system-ffmpeg")

def install():
    raw_install("DESTDIR=%s" % install_dir)
