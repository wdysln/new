get("waf")
metadata = """
summary @ The X MultiMedia System - a multimedia player
homepage @ http://legacy.xmms2.org/
license @ GPL3
src_url @ http://downloads.sourceforge.net/project/xmms2/xmms2/0.8%20DrO_o/xmms2-0.8DrO_o.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/gtk+:2 dev-libs/dbus-glib dev-util/desktop-file-utils
        x11-themes/hicolor-icon-theme 
"""
def prepare():
    patch(level=1)

def configure():
    raw_configure("--prefix=/usr")

def install():
    raw_install("DESTDIR=%s" % install_dir)
