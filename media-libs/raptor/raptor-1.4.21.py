metadata = """
summary @ A C library that parses RDF/XML/N-Triples into RDF triples - old V1 api for compatibility
homepage @ http://librdf.org/raptor
license @ LGPL
src_url @ http://librdf.org/dist/source/$fullname.tar.gz
arch @ ~x86_64
slot @ 1.4
"""

depends = """
runtime @ dev-libs/libxml2 net-misc/curl sys-libs/zlib dev-libs/libxslt
"""

def configure():
	conf(
	"-disable-static")

def install():
	raw_install("DESTDIR=%s" % install_dir)

