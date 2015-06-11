metadata = """
summary @ A C library that parses RDF/XML/N-Triples into RDF triples
homepage @ http://librdf.org/raptor
license @ LGPL
src_url @ http://librdf.org/dist/source/raptor2-$version.tar.gz
arch @ ~x86_64
slot @ 2.0
options @ xml curl
"""

depends = """
runtime @ sys-libs/glib
"""

opt_runtime = """
xml @ dev-libs/libxml2 || dev-libs/expat
curl @ net-misc/curl
"""

srcdir = "raptor2-"+version

def configure():
	conf(
	config_enable("static-libs", "static"))
