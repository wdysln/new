metadata = """
summary @ Base libraries for basic KDE applications
homepage @ http://kde.org/
license @ GPL-2 LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/kde-baseapps-$version.tar.xz
arch @ ~x86_64
"""
depends = """
runtime @ kde-base/kdelibs
"""

get("main/cmake_utils", "main/fdo_mime", "main/extract_utils")
srcdir = "kde-baseapps-%s" % version
extract = lambda: tar_extract("kde-baseapps-%s.tar.xz" % version)
prepare   = lambda: makedirs("build")
build     = lambda: (cd("build/lib"), make())
install   = lambda: (cd("build/lib"), installd())



def configure():
    cd("build")
    export ("Automoc4_DIR","=/usr/lib/automoc4") 
    export ("CMAKE_PREFIX_PATH","=/usr")
    cmake_conf("-DAutomoc4_DIR=/usr/lib/automoc4",
            "-DSTRIGI_INCLUDE_DIR=/usr/include/strigi",
            cmake_config_have("3dnow"), sourcedir=build_dir+"/lib")




