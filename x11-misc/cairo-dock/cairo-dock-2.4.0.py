metadata = """
summary @ Cairo-dock is a fast, responsive, Mac OS X-like dock.
homepage @ http://www.glx-dock.org/
license @ GPL-3
src_url @ http://launchpad.net/cairo-dock-core/2.4/2.4.0/+download/cairo-dock-2.4.0~2.tar.gz
arch @ ~x86_64
options @ crypt xcomposite
"""

depends = """
common @ dev-util/cmake dev-libs/dbus-glib sys-libs/glib dev-libs/libxml2 gnome-base/librsvg net-misc/curl
sys-apps/dbus x11-libs/cairo x11-libs/gtk+:2 x11-libs/gtkglext x11-libs/libXrender
build @ dev-util/intltool dev-util/pkg-config sys-devel/gettext
"""

opt_runtime = """
crypt @ sys-libs/glibc
xcomposite @  x11-libs/libXcomposite x11-libs/libXinerama x11-libs/libXtst
"""

srcdir = fullname + "~2"

get("cmake_utils")

def configure():
    cmake_conf(
    "-DENABLE_GLITZ=OFF", myconf)
