metadata = """
summary @ A powerful mathematical equation solver
homepage @ http://kde.org/
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/kdeplasma-addons-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ kde-base/kde-workspace
"""

get("main/cmake_utils", "main/extract_utils")
srcdir = "kdeplasma-addons-%s" % version
extract = lambda: tar_extract("kdeplasma-addons-%s.tar.bz2" % version)
prepare   = lambda: makedirs("build")
configure = lambda: (cd("build"), cmake_conf(sourcedir=build_dir))
build     = lambda: (cd("build/applets/systemloadviewer"), make())
install   = lambda: (cd("build/applets/systemloadviewer"), installd())
