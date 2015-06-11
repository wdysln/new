metadata = """
summary @ A BitTorrent protocol implementation 
homepage @ http://ktorrent.org 
license @ GPL2 
src_url @ http://ktorrent.org/downloads/4.2.0/$name-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ kde-base/kdelibs
build @ dev-util/cmake dev-libs/boost dev-util/automoc4
"""

def configure():
	pass

def build():
	system("mkdir build")
	cd("./build")
	system("cmake ../ \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=/usr")
	make()

def install():
	cd("./build")
	raw_install("DESTDIR=%s" % install_dir)

