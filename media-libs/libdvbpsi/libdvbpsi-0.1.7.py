metadata = """
summary @ A library designed for decoding and generation of MPEG TS and DVB PSI tables
homepage @ http://developers.videolan.org/libdvbpsi/
license @ GPL
src_url @ http://download.videolan.org/pub/$name/$version/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""


def install():
	raw_install('prefix="%s/usr"' % install_dir)


