metadata = """
summary @ PDF rendering library based on xpdf 3.0 code base
homepage @ http://poppler.freedesktop.org/
license @ GPL
src_url @ http://poppler.freedesktop.org/$name-$version.tar.xz
arch @ ~x86_64
options @ cairo introspection curl jpeg lcms png cjk
"""

#TODO: QT and Openjpeg Support

depends = """
common @ media-libs/fontconfig media-libs/freetype sys-libs/zlib
build @ dev-util/pkg-config media-libs/libpng media-libs/lcms media-libs/openjpeg
"""

opt_build = """
cairo @ sys-libs/glib x11-libs/cairo x11-libs/gtk+:2 
    introspection @ dev-libs/gobject-introspection
curl @ net-misc/curl
jpeg @ media-libs/jpeg
lcms @ media-libs/lcms

"""

opt_runtime = """
cjk @ app-text/poppler-data
"""
#get("main/cmake_utils")

def configure():
    conf("--disable-static \
          --enable-xpdf-headers \
          --enable-libtiff \
          --enable-libjpeg \
          --enable-libpng \
          --enable-libcurl")

def build():
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
