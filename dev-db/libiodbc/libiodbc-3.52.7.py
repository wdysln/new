metadata = """
summary @ Independent Open DataBase Connectivity for Linux
homepage @ http://www.iodbc.org/dataspace/iodbc/wiki/iODBC/
license @ LGPL
src_url @ http://downloads.sourceforge.net/iodbc/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
build @ app-admin/chrpath
"""

def configure():
	conf(
	"--prefix=/usr \
		--disable-static \
		--includedir=/usr/include/libiodbc \
		--disable-gui \
		--disable-libodbc")

def install():
	raw_install("DESTDIR=%s" % install_dir)
	
def post_install():
	system("chrpath -d /usr/bin/iodbctest{,w}")
