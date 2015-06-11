metadata = """
summary @ Musepack decoding library
homepage @ http://musepack.net/
license @ custom
src_url @ http://files.musepack.net/source/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
	conf(
	"--disable-static")

def install():
	raw_install("DESTDIR=%s" % install_dir)

	insdoc("COPYING")

