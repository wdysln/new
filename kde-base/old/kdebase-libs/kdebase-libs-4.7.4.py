metadata = """
summary @ Base libraries for basic KDE applications
homepage @ http://kde.org/
license @ GPL-2 LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/kde-baseapps-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ kde-base/kdelibs
"""

get("main/cmake_utils", "main/fdo_mime", "main/extract_utils")
srcdir = "kde-baseapps-%s" % version
extract = lambda: tar_extract("kde-baseapps-%s.tar.bz2" % version)
prepare   = lambda: makedirs("build")
configure = lambda: (cd("build"), cmake_conf(sourcedir=build_dir+"/lib"))
build     = lambda: (cd("build/lib"), make())
install   = lambda: (cd("build/lib"), installd())
