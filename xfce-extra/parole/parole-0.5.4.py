metadata = """
summary @ A modern simple media player
homepage @ http://www.xfce.org/
license @ GPL2
src_url @ http://archive.xfce.org/src/apps/parole/0.5/parole-0.5.4.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/gtk+:2 media-plugins/gst-plugins-bad:0 media-plugins/gst-plugins-base:0 media-plugins/gst-plugins-good:0 media-plugins/gst-plugins-bad:0
media-plugins/gst-plugins-ugly:0 media-libs/gstreamer:0
build @ x11-libs/libnotify x11-libs/gtk+:2

"""


def configure():
    conf("--disable-dependency-tracking \
                         --enable-libnotify \
                         --enable-taglib")
def build():
    make()    
    
def install():
    raw_install("DESTDIR=%s" % install_dir)    