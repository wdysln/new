metadata = """
summary @ Port of the default KDE widget theme (Oxygen) to GTK 
homepage @ http://kde-look.org/content/show.php/?content=136216 
license @ LGPL 
src_url @ ftp://ftp.kde.org/pub/kde/stable/oxygen-gtk/$version/src/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/gtk+:2 
build @ dev-util/cmake
"""

get("main/cmake_utils")

def prepare(): 
    makedirs("build")

def configure():
    cd("build")
    cmake_conf(sourcedir=build_dir)

def build():
    cd("build")
    make()

def install():
    cd("build")
    raw_install("DESTDIR=%s" % install_dir)

