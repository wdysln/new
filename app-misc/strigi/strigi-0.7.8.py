metadata = """
summary @ Fast crawling desktop search engine with Qt4 GUI
homepage @ http://www.vandenoever.info/software/strigi/
license @ GPL2
src_url @ http://www.vandenoever.info/software/strigi/strigi-0.7.8.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/qt app-arch/bzip2 media-gfx/exiv2 dev-libs/libxml2
build @ dev-util/cmake dev-util/pkg-config
common @ dev-libs/boost
"""

get("main/cmake_utils")

def configure():
    cmake_conf("-DENABLE_INOTIFY=ON",
            "-DENABLE_LOG4CXX=OFF",
            "-DENABLE_FAM=OFF",
            "-DENABLE_CLUCENE=OFF",
            "-DENABLE_CLUCENE_NG=OFF",
            "DENABLE_FFMPEG=OFF")

def install():
    for item in ("libstreams", "libstreamanalyzer", \
            "strigiclient/lib/searchclient/qtdbus", "strigiutils"):
        cd("%s/%s" % (build_dir, item))
	raw_install("DESTDIR=%s" % install_dir)

