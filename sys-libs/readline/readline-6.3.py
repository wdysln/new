metadata = """
summary @ GNU readline library
homepage @ http://tiswww.case.edu/php/chet/readline/rltop.html
license @ GPL
src_url @ http://ftp.gnu.org/gnu/readline/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
common @ sys-libs/ncurses
"""

def prepare():
    sed("-i '/MV.*old/d' Makefile.in")
    sed("-i '/{OLDSUFF}/c:' support/shlib-install")
    patch("readline63-001.patch",level=0)
    patch("readline63-002.patch",level=0)
    patch("readline63-003.patch",level=0)
    

    
def configure():
    raw_configure("--prefix=/usr",
            "--libdir=/usr/lib")

def build():
    make("SHLIB_LIBS=-lncurses")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insfile("%s/inputrc" % filesdir, "/etc/inputrc")