metadata = """
summary @ A backend utility to get CDDB discid information from a CD-ROM disc
homepage @ http://lly.org/~rcw/cd-discid/
license @ GPL
src_url @ http://lly.org/~rcw/$name/$name_$version.orig.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def install():
	raw_install("DESTDIR=%s INSTALL=/bin/install" % install_dir)

