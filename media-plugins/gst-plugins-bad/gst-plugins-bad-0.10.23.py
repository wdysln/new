metadata = """
summary @ GStreamer Bad Plugins + Libraries
homepage @ http://gstreamer.freedesktop.org/
license @ LGPL
src_url @ http://ftp.osuosl.org/pub/blfs/conglomeration/gst-plugins-bad/gst-plugins-bad-0.10.23.tar.xz
arch @ ~x86_64
"""

depends = """
common @ media-libs/gstreamer:0 media-plugins/gst-plugins-base:0 sys-libs/glib
"""

opt_build = """
orc @ dev-lang/orc
"""
def prepare():
    export("NOCONFIGURE", "1")
    system("./autogen.sh")

def configure():
    conf('--disable-examples',
         '--disable-debug',
         '--with-package-name="GStreamer Bad Plugins (Hadron GNU/Linux)"',
         '--with-package-origin="http://www.hadronproject.org/"',
	"--disable-static",
	"--disable-gtk-doc",
	"--disable-rpath",
	"--disable-experimental",
	"--disable-assrender")


def install():
    raw_install("DESTDIR=%s" % install_dir)
