metadata = """
summary @ library implementation of the Media Transfer Protocol 
homepage @ http://libmtp.sourceforge.net 
license @ LGPL 
src_url @ http://downloads.sourceforge.net/$name/$name-$version.tar.gz 
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/libusb-compat
build @ app-doc/doxygen
"""

def configure():
	conf(
	" --with-udev-rules=52-libmtp.rules")

def install():
	raw_install("DESTDIR=%s" % install_dir)

#	insdoc("COPYING")

