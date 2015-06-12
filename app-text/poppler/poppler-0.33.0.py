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
build @ dev-util/pkg-config
"""

opt_build = """
cairo @ sys-libs/glib x11-libs/cairo x11-libs/gtk+:2 
    introspection @ dev-libs/gobject-introspection
curl @ net-misc/curl
jpeg @ media-libs/jpeg
lcms @ media-libs/lcms
png @ media-libs/libpng
"""

opt_runtime = """
cjk @ app-text/poppler-data
"""

def configure():
    pass

def build():
    system("mkdir build")
    cd("./build")

    cmakeopts = " -DBUILD_GTK_TESTS=OFF \
    -DBUILD_QT4_TESTS=OFF \
    -DBUILD_CPP_TESTS=OFF \
    -DENABLE_ABIWORD=OFF \
    -DENABLE_SPLASH=ON \
    -DENABLE_ZLIB=ON "
    
    if opt("curl"):
        cmakeopts += " -DENABLE_LIBCURL"
    if opt("jpeg"):
        cmakeopts += " -DWITH_jpeg "
    if opt("png"):
        cmakeopts += " -DWITH_png "
    if opt("cairo"):
        cmakeopts += " -DWITH_cairo -DWITH_GTK "
    if opt("introspection"):
        cmakeopts += " -DWITH_GObjectIntrospection "

    system("cmake ../ \
            -DCMAKE_INSTALL_PREFIX=/usr %s" % cmakeopts)


    # What the fuck !?! Gentoo uses cmake, arch uses standard configure. FUCK PDF!
