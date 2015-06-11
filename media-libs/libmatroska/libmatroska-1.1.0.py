metadata = """
summary @ Matroska library 
homepage @ http://dl.matroska.org/downloads/libmatroska/ 
license @ LGPL 
src_url @ http://dl.matroska.org/downloads/libmatroska/$name-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/libebml
"""

def configure():
	cd("make/linux")
	conf()

def build():
	cd("make/linux")
	make("sharedlib")

def install():
	cd("make/linux")
	raw_install("prefix=%s/usr" % install_dir)

#	insdoc("COPYING")

