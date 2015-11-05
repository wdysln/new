metadata = """
summary @ GNU readline library
homepage @ http://tiswww.case.edu/php/chet/readline/rltop.html
license @ GPL
src_url @ http://ftp.gnu.org/gnu/readline/readline-$version.tar.gz
arch @ ~x86_64
"""

depends = """
common @ sys-libs/ncurses
"""
srcdir ="readline-%s" %version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
    
def prepare():
    sed("-i '/MV.*old/d' Makefile.in")
    sed("-i '/{OLDSUFF}/c:' support/shlib-install")
    patch("readline63-001.patch",level=0)
    patch("readline63-002.patch",level=0)
    patch("readline63-003.patch",level=0)
    

    
def configure():
    flags()
    raw_configure("--prefix=/usr",
            "--libdir=/usr/lib32")

def build():
    flags()
    make("SHLIB_LIBS=-lncurses")

def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/{bin,include,share}"% install_dir)