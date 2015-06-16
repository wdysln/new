metadata = """
summary @ GStreamer phonon backend
homepage @ http://phonon.kde.org/
license @ LGPL
src_url @ http://download.kde.org/stable/phonon/phonon-backend-gstreamer/4.8.2/src/phonon-backend-gstreamer-4.8.2.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/qt media-libs/phonon media-libs/gstreamer:1 media-plugins/gst-plugins-base:1 media-plugins/gst-plugins-good:1
        media-plugins/gst-plugins-bad:1 media-plugins/gst-plugins-ugly:1
build @ dev-util/cmake dev-util/automoc4
"""

get("main/cmake_utils")


def configure():
    cmake_conf("-DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_SKIP_RPATH=ON \
    -D__KDE_HAVE_GCC_VISIBILITY=NO \
    -DCMAKE_INSTALL_LIBDIR=lib")

def install():
    raw_install("DESTDIR=%s" % install_dir)

