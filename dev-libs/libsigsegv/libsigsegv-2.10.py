metadata = """
summary @ Page fault detection library 
homepage @ http://libsigsegv.sourceforge.net/ 
license @ GPL2 
src_url @ http://ftp.gnu.org/gnu/$name/$name-$version.tar.gz 
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
	conf(
	"--enable-shared")

def install():
	raw_install("DESTDIR=%s" % install_dir)


