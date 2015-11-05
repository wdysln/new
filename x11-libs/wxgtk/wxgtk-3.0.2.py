metadata = """
summary @ GTK+ implementation of wxWidgets API for GUI
homepage @ http://wxwidgets.org
license @ wxWinLL-3 GPL-2
src_url @ http://downloads.sourceforge.net/wxwindows/wxWidgets-$version.tar.bz2
arch @ ~x86_64
options @ X debug gstreamer odbc opengl sdl tiff pch
"""

#TODO: More options http://znurt.org/x11-libs/wxGTK/wxGTK-2.8.12.0

depends = """
runtime @ dev-libs/expat
build @ dev-util/pkg-config
"""

opt_runtime = """
X @ >=x11-libs/gtk+-2.4:2 >=sys-libs/glib-2.4 media-libs/jpeg x11-libs/libSM x11-libs/libXinerama x11-libs/libXxf86vm
    gstreamer @ gnome-base/gconf >=media-libs/gstreamer-0.10 >=media-libs/gst-plugins-base-0.10
    opengl @ media-libs/mesa
    tiff @ media-libs/tiff
sdl @ media-libs/SDL
odbc @ dev-db/unixODBC
"""

opt_build = """
X @ x11-proto/xproto x11-proto/xineramaproto x11-proto/xf86vidmodeproto
"""

srcdir = "wxWidgets-" + version

def prepare():
    patch(level=1)

def configure():
    conf("--prefix=/usr --libdir=/usr/lib --with-gtk=2 --with-opengl --enable-unicode \
            --enable-graphics_ctx --enable-mediactrl --with-regex=builtin \
            --with-libpng=sys --with-libxpm=sys --with-libjpeg=sys --with-libtiff=sys \
            --disable-precomp-headers")
def build():
    make()
    make("-C locale allmo")



def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("changes.txt", "readme.txt", "todo30.txt", "base/readme.txt",
            "base_readme.txt", "gtk/readme.txt", "gtk_readme.txt")

    
    