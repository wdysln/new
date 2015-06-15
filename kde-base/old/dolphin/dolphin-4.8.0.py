metadata = """
summary @ File Manager for KDE
homepage @ http://kde.org/
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/kde-baseapps-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ >=kde-base/kdelibs-4.8.0 >=kde-base/kdebase-libs-4.8.0
"""

get("main/kde4_utils")

srcdir = "kde-baseapps-%s" % version
subdir = "dolphin"

def configure():
    cd("%s" % subdir)
    export ("Automoc4_DIR","=/usr/lib/automoc4") 
    export ("CMAKE_PREFIX_PATH","=/usr")
    cmake_conf("-DAutomoc4_DIR=/usr/lib/automoc4",
            "-DSTRIGI_INCLUDE_DIR=/usr/include/strigi",
            cmake_config_have("3dnow"), sourcedir=build_dir)
def build():
    cd("%s" % subdir)
    make()

def install():
    cd("%s" % subdir)
    installd()
