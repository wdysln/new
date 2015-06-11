metadata = """
summary @ View disk usage information
homepage @ http://kde-apps.org/content/show.php?content=9887
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
common @ >=kde-base/kde-runtime-4.8.0
build @ dev-util/cmake dev-util/automoc4
"""

get("main/cmake_utils")
