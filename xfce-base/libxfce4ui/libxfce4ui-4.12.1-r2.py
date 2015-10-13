metadata = """
summary @ Share commonly used Xfce widgets among the Xfce applications
homepage @ http://www.xfce.org
license @ GPL2
src_url @ http://archive.xfce.org/src/xfce/libxfce4ui/4.12/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ xfce-base/libxfce4util x11-libs/gtk+:2 xfce-base/xfconf x11-libs/startup-notification
"""

def configure():
    conf("--disable-static",
            "--disable-gtk-doc",
            "--libexecdir=/usr/lib/xfce4",
            "--disable-debug",
            '--with-vendor-info="Hadron Linux"')

def install():
    raw_install("DESTDIR=%s" % install_dir)
