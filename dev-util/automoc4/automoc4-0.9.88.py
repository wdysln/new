metadata = """
summary @ Automatic moc for Qt4
homepage @ http://www.kde.org/
license @ custom
src_url @ http://download.kde.org/stable/$name/$version/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/qt
build @ dev-util/cmake dev-util/pkg-config
"""

get("main/cmake_utils")

