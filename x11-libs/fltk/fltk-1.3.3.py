metadata = """
summary @ Graphical user interface toolkit for X
homepage @ http://www.fltk.org/
license @ custom LGPL
src_url @ http://fltk.org/pub/fltk/$version/fltk-$version-source.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-libs/expat x11-libs/libXinerama media-libs/libjpeg-turbo x11-libs/libXft
          dev-util/desktop-file-utils media-libs/alsa-lib media-libs/mesa media-libs/glu
build @ dev-util/pkg-config
"""
def prepare():
    patch(level=1)

def configure():
    conf("--enable-shared \
               --enable-gl \
               --enable-threads") 
            

def build():
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
