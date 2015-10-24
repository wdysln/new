metadata = """
summary @ A spell checker designed to eventually replace Ispell
homepage @ http://aspell.net/
license @ LGPL
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc sys-libs/ncurses
"""

def install():
	raw_install("DESTDIR=%s" % install_dir)

