metadata = """
summary @ A scalable cross-platform server that combines SQL/RDF/XML Data Management with Web Application Server and Web Services Platform functionality
homepage @ http://virtuoso.openlinksw.com/wiki/main/Main/
license @ GPL 
src_url @ http://downloads.sourceforge.net/$name/$name-opensource-$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/openssl
build @ sys-devel/bison sys-devel/flex
"""

srcdir = name+"-opensource-"+version

def configure():
	conf(
	"--localstatedir=/var \
	 --sysconfdir=/etc \
	 --disable-rendezvous \
	 --disable-hslookup \
	 --disable-all-vads")

def install():
	cd("./binsrc/virtuoso")
	raw_install("DESTDIR=%s" % install_dir)
	cd("../driver")
	raw_install("DESTDIR=%s" % install_dir)
