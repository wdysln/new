metadata = """
summary @ KDE MDI editor/IDE
homepage @ http://www.kde.org
license @ GPL-2
src_url @ http://download.kde.org/stable/$version/src/kate-$version.tar.bz2
arch @ ~x86_64
"""


get("main/cmake_utils", "main/extract_utils")

srcdir = "kate-%s" % version
extract = lambda: tar_extract("kate-%s.tar.bz2" % version)
prepare = lambda: makedirs("build")
configure = lambda: (cd("build"), cmake_conf("-DAutomoc4_DIR=/usr/lib/automoc4",
                                             sourcedir=build_dir+"/kate"))
build = lambda: (cd("build/kate"), make())
install = lambda: (cd("build/kate"), installd())

