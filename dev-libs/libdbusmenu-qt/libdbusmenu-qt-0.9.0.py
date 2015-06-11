metadata = """
summary @ A library that provides a Qt implementation of the DBusMenu spec
homepage @ https://launchpad.net/libdbusmenu-qt
license @ GPL
src_url @ http://launchpad.net/$name/trunk/$version/+download/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/qt
build @ dev-util/cmake net-misc/wget[ssl,gnutls]
"""

get("main/cmake_utils")

def configure():
    cmake_conf("-DWITH_DOC=OFF")
