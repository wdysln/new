metadata = """
summary @ KDE file finder utility
homepage @ http://kde.org/
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/kde-baseapps-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ kde-base/kdelibs kde-base/kdebase-libs
"""

get("main/cmake_utils", "main/fdo_mime", "main/extract_utils")
srcdir = "kde-baseapps-%s" % version
extract = lambda: tar_extract("kde-baseapps-%s.tar.bz2" % version)

def configure():
    makedirs("build")
    cd("build")
    cmake_conf(sourcedir=build_dir+"/kfind")

build = lambda: (cd("build/kfind"), make())
install = lambda: (cd("build/kfind"), installd())
post_install = lambda: (xdg_icon_resource(), desktop_database_update())
