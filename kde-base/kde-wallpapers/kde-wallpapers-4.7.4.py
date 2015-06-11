metadata = """
summary @ A set of wallpapers for KDE
homepage @ http://kde.org/
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/kde-wallpapers-$version.tar.bz2
arch @ ~x86_64
"""

get("main/cmake_utils", "main/extract_utils")

extract = lambda: tar_extract("kde-wallpapers-%s.tar.bz2" % version)

prepare = lambda: makedirs("build")

standard_procedure = False

def configure():
    cd("build")
    cmake_conf(sourcedir=build_dir)

def install():
    cd("build")
    installd()
