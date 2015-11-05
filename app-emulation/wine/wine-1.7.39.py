metadata = """
summary @ A compatibility layer for running Windows programs
homepage @ http://www.winehq.com
license @ LGPL
src_url @ http://prdownloads.sourceforge.net/wine/wine-1.7.39.tar.bz2
arch @ ~x86_64
options @ perl fontconfig udisks gnutls ncurses X xinerama alsa cups opengl mp3 xml png ssl xcomposite nls test jpeg truetype threads
"""

depends = """
runtime @ >=media-libs/freetype-2.0.0 media-fonts/freefonts sys-libs/ncurses
build @ sys-devel/autoconf sys-devel/bison sys-devel/flex sys-devel/prelink dev-util/pkg-config
"""

opt_runtime = """
jpeg @ media-libs/jpeg
fontconfig @ media-libs/fontconfig
opengl @ media-libs/mesa 
X @ x11-libs/libXcursor x11-libs/libXrandr x11-libs/libXdamage x11-libs/libXi dev-util/desktop-file-utils
nls @ sys-devel/gettext
udisks @ sys-apps/dbus sys-fs/udisks
gnutls @net-libs/gnutls
xinerama @ x11-libs/libXinerama
alsa @ media-libs/alsa-lib
cups @ net-print/cups
mp3 @ media-sound/mpg123
xml @ dev-libs/libxml2 dev-libs/libxslt
png @ media-libs/libpng
ssl @ dev-libs/openssl
xcomposite @ x11-libs/libXcomposite
nls @ sys-devel/gettext
"""
opt_build = """
perl @ dev-lang/perl dev-perl/XML-Simple
X @ x11-proto/inputproto x11-proto/xextproto x11-proto/xf86vidmodeproto
xinerama @ x11-proto/xineramaproto
"""
flags = ""  
flags32 = "-m32"  
standard_procedure = False

def configure():
    makedirs("wine64-build"); cd("wine64-build")
    system("install=wine.keyring")
    export("CC", "gcc %s " % flags)
    export("CXX", "g++ %s " % flags)

    export("CFLAGS", flags)
    export("CXXFLAGS", flags)
    system("../configure --without-hal \
            --without-capi \
            --without-hal \
            --without-gstreamer \
            --with-x \
            --enable-win64 \
            --prefix=/usr \
            --libdir=/usr/lib")
    make()
    raw_install("prefix=%s/usr libdir=%s/usr/lib dlldir=%s/usr/lib/wine" % (install_dir,install_dir,install_dir)) 
    cd("..")
     #wine32
    makedirs("wine32-build"); cd("wine32-build")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
    export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")
    system("install=wine.keyring")
    export("CC", "gcc %s " % flags32)
    export("CXX", "g++ %s " % flags32)

    export("CFLAGS", flags32)
    export("CXXFLAGS", flags32)
    system("../configure --without-hal \
            --without-capi \
            --without-hal \
            --without-gstreamer \
            --with-x \
            --with-wine64='%s/wine64-build' \
            --prefix=/usr \
            --libdir=/usr/lib32"% build_dir)
    make()
    raw_install("prefix=%s/usr libdir=%s/usr/lib32 dlldir=%s/usr/lib32/wine" % (install_dir,install_dir,install_dir)) 
         
 
