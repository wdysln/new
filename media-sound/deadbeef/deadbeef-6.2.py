metadata = """
summary @ Audio player for GNU/Linux systems with X11
homepage @ http://deadbeef.sourceforge.net
license @ GPL2
src_url @ https://github.com/Alexey-Yakovenko/deadbeef/archive/master.zip
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/gtk+:2 dev-util/desktop-file-utils
        x11-themes/hicolor-icon-theme media-libs/pango x11-libs/cairo x11-libs/gdk-pixbuf media-libs/alsa-lib
        media-libs/imlib2 media-libs/libvorbis media-libs/libogg media-video/ffmpeg dev-libs/jansson
        media-plugins/gst-plugins-base:0 media-plugins/gst-plugins-good:0 media-plugins/gst-plugins-bad:0
        media-plugins/gst-plugins-ugly:0 media-libs/gstreamer:0 media-sound/lame x11-libs/libnotify media-libs/taglib        
"""
#srcdir = "deadbeef-master"

get("git_utils")

standard_procedure = False

reserve_files = ["/etc/lpms/build.conf", "/etc/lpms/repo.conf"]

def prepare():
    git_clone("git@github.com:Alexey-Yakovenko/deadbeef.git", subdir=name)
    
def configure():
    system("/bin/chmod u+x *.sh")
    system("./autogen.sh")
    conf("--prefix=/usr --enable-gtk3=no --enable-staticlink=no --without-jansson --enable-jansson=no")

def build():
    make()
    
def install():
    raw_install("DESTDIR=%s" % install_dir)
