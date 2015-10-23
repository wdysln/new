metadata = """
summary @ Extra modules and scripts for CMake
homepage @ https://projects.kde.org/projects/kdesupport/extra-cmake-modules
license @ LGPL
src_url @ http://distfiles.atheme.org/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ app-arch/unzip  
build @ dev-util/pkg-config
"""

get("main/cmake_utils")

def configure():
    cmake_conf("-DCMAKE_BUILD_TYPE=Release \
                -DCMAKE_INSTALL_PREFIX=/usr \
                -DBUILD_HTML_DOCS=OFF \
                -DBUILD_TESTING=OFF")
                
