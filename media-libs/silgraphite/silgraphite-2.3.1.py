metadata = """
summary @  SILGraphite - a "smart font" rendering engine - the libs and headers
homepage @  http://graphite.sil.org/
license @  custom_SIL Dual license
src_url @  http://downloads.sourceforge.net/project/silgraphite/silgraphite/$version/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-devel/gcc
"""

def configure():
	conf(
	"--disable-static")

def install():
	raw_install("DESTDIR=%s" % install_dir)

