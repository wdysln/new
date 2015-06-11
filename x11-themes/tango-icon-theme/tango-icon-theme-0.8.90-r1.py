metadata = """
summary @ The Tango Desktop Project exists to create a consistent user experience
homepage @ http://tango.freedesktop.org
license @ public-domain
src_url @ http://tango.freedesktop.org/releases/$fullname.tar.gz
options @ png
arch @ ~x86_64
"""

depends = """
runtime @ gnome-base/librsvg
build @ x11-misc/icon-naming-utils dev-util/intltool dev-util/pkg-config dev-lang/python:2.7 media-gfx/imagemagick
"""

get("gnome2_utils")

def configure():
    conf(config_enable("png"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")

post_install = lambda: gnome2_icon_cache_update()

