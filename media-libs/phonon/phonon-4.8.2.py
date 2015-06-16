metadata = """
summary @ The multimedia framework for KDE4
homepage @ http://phonon.kde.org/
license @ LGPL
src_url @ http://download.kde.org/stable/$name/$version/$fullname.tar.xz
arch @ ~x86_64
options @ mplayer vlc
"""

depends = """
runtime @ x11-libs/qt
build @ dev-util/cmake dev-util/automoc4
"""

opt_postmerge = """
mplayer @ media-libs/phonon-mplayer
vlc @ media-libs/phonon-vlc
"""

get("main/cmake_utils")


def configure():
    cmake_conf(
    "-DPHONON_QT_MKSPECS_INSTALL_DIR=/usr/share/qt/mkspecs/modules \
    -DPHONON_QT_PLUGIN_INSTALL_DIR=/usr/lib/qt/plugins/designer")
