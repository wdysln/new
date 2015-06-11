metadata = """
summary @ A library that allows developers to access PolicyKit API with a nice Qt-style API
homepage @ http://www.kde.org/
license @ LGPL
src_url @ http://download.kde.org/stable/apps/KDE4.x/admin/$name-1-0.112.0.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-auth/polkit x11-libs/qt
"""

srcdir = "%s-1-%s" % (name, version)
get("main/cmake_utils")

def configure():
    patch(level=1)
    makedirs("build")
    cd("build")
    cmake_conf("-DCMAKE_INSTALL_LIBDIR=lib",
     "-DUSE_QT4=TRUE",         
     "-Wno-dev",sourcedir=build_dir)
     

def build():
    cd("build")
    make()

def install():
    cd("build")	
    raw_install("DESTDIR=%s" % install_dir)

    	
