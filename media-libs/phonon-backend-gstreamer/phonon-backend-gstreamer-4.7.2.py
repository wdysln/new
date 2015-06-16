metadata = """
summary @ GStreamer phonon backend
homepage @ http://phonon.kde.org/
license @ LGPL
src_url @ http://download.kde.org/stable/$name/$version/$fullname.tar.xz
arch @ ~x86_64
options @ mplayer vlc
"""

depends = """
runtime @ x11-libs/qt media-libs/phonon media-libs/gstreamer:0 media-plugins/gst-plugins-base:0
build @ dev-util/cmake dev-util/automoc4
"""

opt_postmerge = """
mplayer @ media-libs/phonon-mplayer
vlc @ media-libs/phonon-vlc
"""

get("main/kde4_utils")


