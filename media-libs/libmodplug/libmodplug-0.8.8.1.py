metadata = """
summary @ A MOD playing library
homepage @ http://modplug-xmms.sourceforge.net/
license @ custom
src_url @ http://downloads.sourceforge.net/sourceforge/modplug-xmms/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-devel/gcc 
"""

def install():
	raw_install("DESTDIR=%s" % install_dir)

	insdoc("COPYING")

