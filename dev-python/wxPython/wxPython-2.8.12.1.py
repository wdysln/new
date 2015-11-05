metadata = """
summary @ GTK+ implementation of wxWidgets API for GUI
homepage @ http://wxwidgets.org
license @ wxWinLL-3 GPL-2
src_url @ http://downloads.sourceforge.net/wxpython/wxPython-src-$version.tar.bz2
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

srcdir = "wxPython-src-" + version

def prepare():
    patch(level=0)


def build():
    cd("wxPython")
    system("python2 setup.py WXPORT=gtk2 UNICODE=1 WX_CONFIG=/usr/bin/wx-config build")

def install():
    cd("wxPython")
    system("python2 setup.py WXPORT=gtk2 UNICODE=1 WX_CONFIG=/usr/bin/wx-config install")
    