metadata = """
summary @ A BitTorrent protocol implementation 
homepage @ http://ktorrent.org 
license @ GPL2 
src_url @ http://ktorrent.pwsp.net/downloads/4.3.1/$fullname.tar.bz2
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
	-DAutomoc4_DIR=/usr/lib/automoc4 \
	-DCMAKE_INSTALL_PREFIX=/usr")
	make()

def install():
	cd("./build")
	raw_install("DESTDIR=%s" % install_dir)

