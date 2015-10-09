metadata = """
summary @ Graphical user interface toolkit for X
homepage @ http://www.fltk.org/
license @ custom LGPL
src_url @ http://fltk.org/pub/fltk/$version/fltk-$version-source.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/expat
build @ dev-util/pkg-config
"""


def configure():
    conf("--enable-shared \
               --enable-gl \
               --enable-threads") 
            

def build():
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
