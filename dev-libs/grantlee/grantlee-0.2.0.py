metadata = """
summary @ A string template engine based on the Django template system and written in Qt
homepage @ http://www.gitorious.org/grantlee/pages/Home
license @ LGPL3
src_url @ http://downloads.grantlee.org/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/qt
build @ dev-util/cmake
"""

get("main/cmake_utils")
