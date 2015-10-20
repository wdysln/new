metadata = """
summary @ CLucene is a C++ port of Lucene: A high-performance, full-featured text search engine
homepage @ http://clucene.sourceforge.net/
license @ APACHE + LGPL
src_url @ http://downloads.sourceforge.net/clucene/$fullname.tar.gz
arch @ ~x86_64
options @ static-libs threads
"""

depends = """
runtime @ sys-devel/gcc
build @ sys-devel/libtool sys-devel/autoconf sys-devel/automake
"""
get("main/cmake_utils")
def prepare():
    patch(level=1)
    

def configure():
    cmake_conf("-DENABLE_ASCII_MODE=OFF \
                -DENABLE_PACKAGING=OFF \
                -DDISABLE_MULTITHREADING=OFF \
                -DBUILD_CONTRIBS_LIB:BOOL=ON")