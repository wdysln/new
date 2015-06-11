metadata = """
summary @ libjpeg derivative with accelerated baseline JPEG compression and decompression
homepage @ http://libjpeg-turbo.virtualgl.org/
license @ GPL
src_url @ http://sourceforge.net/projects/$name/files/$version/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
build @ dev-lang/nasm
"""

def configure():
	conf(
	"--with-jpeg8")

def install():
	raw_install("DESTDIR=%s" % install_dir)
	
	insdoc("LICENSE.txt")
