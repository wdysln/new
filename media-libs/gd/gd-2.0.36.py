metadata = """
summary @ Library for the dynamic creation of images by programmers 
homepage @ http://www.libgd.org/ 
license @ custom 
src_url @ http://www.libgd.org/releases/$name-$versionRC1.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ dev-lang/perl media-libs/libpng media-libs/jpeg media-libs/fontconfig
"""

def prepare():
	patch(level=1)

def configure():
	conf(
	"--without-xpm")

def install():
	raw_install("DESTDIR=%s" % install_dir)

	insdoc("COPYING")

