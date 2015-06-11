metadata = """
summary @ Terminal Application for KDE
homepage @ http://kde.org/applications/system/konsole/
license @ GPL-2 LGPL FDL
src_url @ http://download.kde.org/stable/$version/src/konsole-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ dev-util/cmake dev-util/automoc4
runtime @ kde-base/kde-runtime
"""

get("kde4_utils")
