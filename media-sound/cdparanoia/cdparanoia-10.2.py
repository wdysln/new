metadata = """
summary @ Compact Disc Digital Audio extraction tool
homepage @ http://www.xiph.org/paranoia/
license @ GPL
src_url @ http://downloads.xiph.org/releases/cdparanoia/cdparanoia-III-$version.src.tgz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

srcdir = name+"-III-"+version

def prepare():
	patch()

def configure():
	autoconf()
	conf(
	"--prefix=/usr --mandir=/usr/share/man")

def build():
	make(j=1)

def install():
	raw_install('prefix="%s/usr" MANDIR="%s/usr/share/man"' % (install_dir, install_dir))


