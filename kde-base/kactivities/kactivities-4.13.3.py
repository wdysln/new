metadata = """
summary @ API for using and interacting with Activities
homepage @ http://kde.org/
license @ GPL-2 LGPL FDL
src_url @ http://download.kde.org/stable/$version/src/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
build @ dev-util/cmake dev-util/automoc4

"""

get("main/kde4_utils")

def configure():
    cd("build")
    cmake_conf(
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_SKIP_RPATH=ON",
    "-DKDE4_BUILD_TESTS=OFF",
    "-DBUILD_nepomuk=OFF",
    "-Wno-dev",
    "-DAutomoc4_DIR=/usr/lib/automoc4",
    "-DCMAKE_INSTALL_PREFIX=/usr", sourcedir=build_dir)
    
def build():
    export("HOME", build_dir)
    cd("build")
    make()
