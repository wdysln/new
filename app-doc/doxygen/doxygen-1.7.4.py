metadata = """
summary @ A documentation system for C++, C, Java, IDL and PHP
homepage @ http://www.doxygen.org/
license @ GPL
src_url @ ftp://ftp.stack.nl/pub/users/dimitri/$name-$version.src.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-lang/python:2.7 media-libs/libpng
build @ sys-apps/sed sys-devel/flex
"""

def configure():
	export("QTDIR", "/usr")
	raw_configure("--prefix /usr")

def install():
	raw_install("INSTALL=%s/usr MAN1DIR=share/man/man1" % install_dir)


#todo docs opt and latex
