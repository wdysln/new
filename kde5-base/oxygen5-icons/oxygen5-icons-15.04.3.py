metadata = """
summary @ Oxygen SVG icon theme
homepage @ http://www.oxygen-icons.org/
license @ LGPL
src_url @ http://download.kde.org/stable/applications/15.04.3/src/oxygen-icons-15.04.3.tar.xz
arch @ ~x86_64
"""

depends = """
build @ dev-util/cmake
"""
srcdir = "oxygen-icons-15.04.3"

get("main/cmake_utils", "main/fdo_mime", "main/extract_utils")
#srcdir = "kde-baseapps-%s" % version
extract = lambda: tar_extract("oxygen-icons-15.04.3.tar.xz")
prepare = lambda: makedirs("build")
configure = lambda: (cd("build"), cmake_conf(sourcedir=build_dir))
build = lambda: (cd("build"), make())
install = lambda: (cd("build"), installd())

