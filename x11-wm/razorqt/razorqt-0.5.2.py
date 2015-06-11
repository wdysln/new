metadata = """
summary @ Razor is a toolbox-like desktop-environment
homepage @ http://razor-qt.org
license @ GPL2
src_url @ http://razor-qt.org/downloads/razorqt-0.5.2.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ dev-util/cmake dev-util/automoc4 x11-libs/libX11 x11-libs/libXext x11-libs/libXklavier x11-libs/libXrender x11-libs/libXtst
    x11-libs/libXrandr x11-libs/libXft x11-libs/libXt x11-libs/qt x11-libs/libXcomposite x11-libs/libXcursor x11-libs/libXrender
dev-libs/libxml2 x11-libs/libXinerama x11-libs/libXrandr x11-libs/libXcursor media-libs/pango x11-libs/libXft x11-libs/libXt sys-libs/glib
dev-util/pkg-config x11-proto/xextproto x11-proto/xf86vidmodeproto x11-proto/xineramaproto dev-libs/icu
"""



get("main/cmake_utils")


def configure():
    makedirs("build")
    cd("build")
    cmake_conf("-DCMAKE_INSTALL_PREFIX=/usr",
               "-DLIB_SUFFIX=''", 
               "-DAutomoc4_DIR=/usr/lib/automoc4",
               "-DENABLE_LIGHTDM_GREETER=OFF",
               "-DMODULE_LIGHTDM=OFF", sourcedir=build_dir)
    
def build():
    cd("build")
    make()    

def install():
    cd("build")
    raw_install("DESTDIR=%s" % install_dir)

