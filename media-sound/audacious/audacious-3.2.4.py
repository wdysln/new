metadata = """
summary @ Lightweight, GTK2-based advanced audio player focused on audio quality
homepage @ http://audacious-media-player.org/
license @ GPL3
src_url @ http://pkgs.fedoraproject.org/repo/pkgs/audacious/audacious-3.2.4.tar.bz2/7d1cabdaf5188abb4deddf628535a955/audacious-3.2.4.tar.bz2
arch @ ~x86_64
options @ altivec chardet nls session sse2
"""

depends = """
runtime @ x11-libs/gtk+:2 dev-libs/dbus-glib dev-libs/libguess dev-util/desktop-file-utils
        x11-themes/hicolor-icon-theme media-libs/pango x11-libs/cairo
"""

opt_runtime = """
session @ x11-libs/libSM
nls @ dev-util/intltool
"""

def configure():
    conf()

def install():
    raw_install("DESTDIR=%s" % install_dir)
