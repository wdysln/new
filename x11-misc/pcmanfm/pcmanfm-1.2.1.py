metadata = """
summary @ Fast lightweight tabbed filemanager
homepage @ http://pcmanfm.sourceforge.net/
license @ GPL-2
src_url @ http://downloads.sourceforge.net/$name/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
common @ sys-libs/glib x11-libs/gtk+:2 lxde-base/menu-cache
lxde-base/libfm
"""


def configure():
    conf(config_enable("debug"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "ChangeLog", "COPYING", "README", 
            "NEWS")

