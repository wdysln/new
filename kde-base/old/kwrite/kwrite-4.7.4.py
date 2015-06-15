metadata = """
summary @ KDE MDI editor/IDE
homepage @ http://www.kde.org
license @ GPL-2
src_url @ http://download.kde.org/stable/$version/src/kate-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
common @ kde-base/kde-runtime
"""

get("main/cmake_utils", "main/extract_utils")

srcdir = "kate-%s" % version

extract = lambda: tar_extract("kate-%s.tar.bz2" % version)

prepare = lambda: makedirs("build")

configure = lambda: (cd("build"), cmake_conf(sourcedir=build_dir+"/kwrite"))

build = lambda: (cd("build/kwrite"), make())

def install():
    cd("build/part"); installd()
    cd(build_dir)
    cd("build/kwrite"); installd()
