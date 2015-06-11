metadata = """
summary @ A C++ library that aims to be a good alternative to all the other bittorrent implementations around 
homepage @ http://www.rasterbar.com/products/libtorrent/ 
license @ custom 
src_url @ http://libtorrent.googlecode.com/files/$name-$version.tar.gz 
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/boost dev-lang/python
build @ dev-libs/boost
"""

def configure():
	conf(
	"--enable-python-binding")

def install():
	raw_install("DESTDIR=%s" % install_dir)

	insdoc("COPYING")

