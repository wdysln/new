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
    cmake_conf("-DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DPHONON_INSTALL_QT_EXTENSIONS_INTO_SYSTEM_QT=ON \
                          -DQT_QMAKE_EXECUTABLE=/usr/bin/qmake \
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DCMAKE_SKIP_RPATH:BOOL=YES")

