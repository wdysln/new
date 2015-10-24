metadata = """
summary @ The multimedia framework for KDE4
homepage @ http://phonon.kde.org/
license @ LGPL
src_url @ http://download.kde.org/stable/phonon/$version/src/phonon-$version.tar.xz
arch @ ~x86_64
options @ mplayer vlc
"""

depends = """
runtime @ x11-libs/qt5
build @ dev-util/cmake 
"""

opt_postmerge = """
mplayer @ media-libs/phonon-mplayer
vlc @ media-libs/phonon-vlc
"""

get("main/cmake_utils")

srcdir = "phonon-4.8.3"
def configure():
    cmake_conf("-DCMAKE_BUILD_TYPE=Release \
				-DCMAKE_SKIP_RPATH=ON \
				-DCMAKE_INSTALL_PREFIX=/usr \
				-DPHONON_INSTALL_QT_EXTENSIONS_INTO_SYSTEM_QT=ON \
				-DPHONON_BUILD_PHONON4QT5=ON \
				-D__KDE_HAVE_GCC_VISIBILITY=NO \
				-DCMAKE_INSTALL_LIBDIR=lib")

