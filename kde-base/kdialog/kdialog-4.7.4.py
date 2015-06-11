metadata = """
summary @ A utility for displaying dialog boxes from shell scripts
homepage @ http://kde.org/
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/kde-baseapps-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ kde-base/kde-runtime
"""

get("main/cmake_utils", "main/fdo_mime", "main/extract_utils")
srcdir = "kde-baseapps-%s" % version
extract = lambda: tar_extract("kde-baseapps-%s.tar.bz2" % version)

def configure():
    makedirs("build")
    cd("build")
    cmake_conf(sourcedir=build_dir+"/kdialog")

build = lambda: (cd("build/kdialog"), make())
install = lambda: (cd("build/kdialog"), installd())
post_install = lambda: (xdg_icon_resource(), desktop_database_update())
