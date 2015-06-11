metadata = """
summary @ Extensible Binary Meta Language library 
homepage @ http://dl.matroska.org/downloads/libebml/ 
license @ LGPL 
src_url @ http://dl.matroska.org/downloads/libebml/$name-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-devel/gcc
"""

def configure():
	cd("make/linux")
	conf()
def build():
	cd("make/linux")
	make()

def install():
	cd("make/linux")
	raw_install("prefix=%s/usr" % install_dir)

#	insdoc("COPYING")

