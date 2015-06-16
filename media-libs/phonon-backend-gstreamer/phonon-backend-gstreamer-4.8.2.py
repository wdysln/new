metadata = """
summary @ GStreamer phonon backend
homepage @ http://phonon.kde.org/
license @ LGPL
src_url @ http://download.kde.org/stable/phonon/$name/$version/src/$fullname.tar.xz    
arch @ ~x86_64
options @ mplayer vlc
"""

depends = """
runtime @ x11-libs/qt media-libs/phonon media-libs/gstreamer:0 media-plugins/gst-plugins-base:0
build @ dev-util/cmake dev-util/automoc4
"""

get("main/kde4_utils")


