metadata = """
summary @ Audio player for GNU/Linux systems with X11
homepage @ http://deadbeef.sourceforge.net
license @ GPL2
src_url @ https://bitbucket.org/shuerhaaken/xnoise/downloads/xnoise-0.2.21.tar.gz
arch @ ~x86_64
"""

depends = """
build @ x11-libs/gtk+:3 dev-util/desktop-file-utils
        media-plugins/gst-plugins-base:1 media-plugins/gst-plugins-good:1 media-plugins/gst-plugins-bad:1
        media-plugins/gst-plugins-ugly:1 media-libs/taglib        
"""
#media-libs/imlib2 media-libs/libvorbis media-libs/libogg media-video/ffmpeg dev-libs/jansson

#srcdir = "deadbeef-master"

    
def configure():
    system("/bin/chmod u+x *.sh")
    system("./autogen.sh")
    conf("--prefix=/usr")

def build():
    make()
    
def install():
    raw_install("DESTDIR=%s" % install_dir)
