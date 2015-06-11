metadata = """
summary @ Plugin that makes screenshots for the XFCE4 panel
homepage @ http://goodies.xfce.org/projects/applications/xfce4-screenshooter
license @ GPL2
src_url @ http://archive.xfce.org/src/apps/$name/1.8/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ net-libs/libsoup
"""


def configure():
    conf("--disable-static",
            "--disable-debug")

def install():
    raw_install("DESTDIR=%s" % install_dir)
