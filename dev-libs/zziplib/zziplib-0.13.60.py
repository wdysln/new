metadata = """
summary @ A lightweight library that offers the ability to easily extract data from files archived in a single zip file 
homepage @ http://zziplib.sourceforge.net 
license @ LGPL MPL 
src_url @ http://downloads.sourceforge.net/$name/$name-$version.tar.bz2 
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/zlib
"""

def prepare():
	patch(level=1)

def install():
	raw_install("DESTDIR=%s" % install_dir)

