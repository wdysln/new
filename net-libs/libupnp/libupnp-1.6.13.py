metadata = """
summary @ Portable Open Source UPnP Development Kit 
homepage @ http://pupnp.sourceforge.net/ 
license @ BSD 
src_url @ http://downloads.sourceforge.net/sourceforge/pupnp/$name-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
build @ dev-util/pkg-config
"""

def install():
	raw_install("DESTDIR=%s" % install_dir)

	insdoc("LICENSE")

