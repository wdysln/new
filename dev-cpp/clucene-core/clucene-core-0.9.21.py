metadata = """
summary @ CLucene is a C++ port of Lucene: A high-performance, full-featured text search engine
homepage @ http://clucene.sourceforge.net/
license @ APACHE + LGPL
src_url @ http://downloads.sourceforge.net/clucene/$fullname.tar.bz2
arch @ ~x86_64
options @ static-libs threads
"""

depends = """
runtime @ sys-devel/gcc
build @ sys-devel/libtool sys-devel/autoconf sys-devel/automake
"""

def configure():
	conf(
	config_enable("static-libs", "static"),
	config_enable("threads", "multithreading"),
	"--prefix=/usr")

def install():
	raw_install("DESTDIR=%s" % install_dir)

#TODO: threading hatali
