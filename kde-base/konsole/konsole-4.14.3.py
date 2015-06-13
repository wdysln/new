metadata = """
summary @ Terminal Application for KDE
homepage @ http://kde.org/applications/system/konsole/
license @ GPL-2 LGPL FDL
src_url @ http://download.kde.org/stable/$version/src/konsole-$version.tar.xz
arch @ ~x86_64
"""

get("main/kde4_utils")


depends = """
build @ >=kde-base/kde-runtime-4.14.3 >=kde-base/kdelibs-4.14.3 >=kde-base/kde-workspace-4.11.4
"""

def configure():
    cd("build")
    cmake_conf("-DAutomoc4_DIR=/usr/lib/automoc4",
                sourcedir=build_dir+"/%s" % subdir)
        
      


