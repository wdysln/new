metadata = """
summary @ Audio player for GNU/Linux systems with X11
homepage @ http://deadbeef.sourceforge.net
license @ GPL2
src_url @ https://github.com/Alexey-Yakovenko/deadbeef/archive/0.6.2.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/gtk+:2 dev-util/desktop-file-utils
        x11-themes/hicolor-icon-theme media-libs/pango x11-libs/cairo x11-libs/gdk-pixbuf media-libs/alsa-lib
        media-libs/imlib2 media-libs/libvorbis media-libs/libogg media-video/ffmpeg
"""

def configure():
    system("./autogen.sh")
    conf("--prefix=/usr --enable-gtk3=no --enable-staticlink=no")

def install():
    raw_install("DESTDIR=%s" % install_dir)
