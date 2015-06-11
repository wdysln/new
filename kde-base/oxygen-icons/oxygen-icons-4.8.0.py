metadata = """
summary @ Oxygen SVG icon theme
homepage @ http://www.oxygen-icons.org/
license @ LGPL
src_url @ http://download.kde.org/stable/$version/src/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ dev-util/automoc4 dev-util/cmake
"""

get("main/cmake_utils", "main/fdo_mime", "main/extract_utils")
#srcdir = "kde-baseapps-%s" % version
extract = lambda: tar_extract("%s.tar.bz2" % fullname)
prepare = lambda: makedirs("build")
configure = lambda: (cd("build"), cmake_conf(sourcedir=build_dir))
build = lambda: (cd("build"), make())
install = lambda: (cd("build"), installd())

