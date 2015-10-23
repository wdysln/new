metadata = """
summary @ Extra modules and scripts for CMake
homepage @ https://projects.kde.org/projects/kdesupport/extra-cmake-modules
license @ LGPL
src_url @ http://download.kde.org/stable/frameworks/5.15/$fulname.tar.xz
arch @ ~x86_64
"""

depends = """
build @ dev-util/cmake
"""

get("main/cmake_utils")

def configure():
    cmake_conf("-DCMAKE_BUILD_TYPE=Release \
                -DCMAKE_INSTALL_PREFIX=/usr \
                -DBUILD_HTML_DOCS=OFF \
                -DBUILD_TESTING=OFF")
                
