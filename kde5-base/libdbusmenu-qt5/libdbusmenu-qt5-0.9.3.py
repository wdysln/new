metadata = """
summary @ A library that provides a Qt implementation of the DBusMenu spec
homepage @ https://launchpad.net/libdbusmenu-qt
license @ GPL
src_url @ http://www.linuxfromscratch.org/~krejzi/libdbusmenu-qt-0.9.3+15.10.20150604.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/qt5
build @ dev-util/cmake net-misc/wget[ssl,gnutls] dev-libs/qjson
"""
srcdir = ""
get("main/cmake_utils")

def configure():
    cmake_conf("-DCMAKE_INSTALL_PREFIX=/usr \
				-DCMAKE_BUILD_TYPE=Release \
				-DCMAKE_INSTALL_LIBDIR=lib")
