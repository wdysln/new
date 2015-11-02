metadata = """
summary @ A GTK text editor
homepage @ http://mooedit.sourceforge.net
license @ GPL
src_url @ http://downloads.sourceforge.net/mooedit/$name-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/gtk+:2 sys-libs/glib x11-libs/vte
build @ dev-util/pkg-config dev-util/intltool dev-python/pygtk x11-libs/libSM
"""

get("gnome2_utils")

def configure():
	conf()

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    gnome2_icon_cache_update()

