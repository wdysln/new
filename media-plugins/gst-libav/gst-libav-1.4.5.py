metadata = """
summary @ Gstreamer libav Plugin
homepage @ http://gstreamer.freedesktop.org/
license @ LGPL
src_url @ http://gstreamer.freedesktop.org/src/$name/$fullname.bzip2
arch @ ~x86_64
"""

depends = """
common @ media-libs/gstreamer media-plugins/gst-plugins-base:1 sys-libs/glib
"""

opt_build = """
orc @ dev-lang/orc
"""


def configure():
    conf()

def install():
    raw_install("DESTDIR=%s" % install_dir)
