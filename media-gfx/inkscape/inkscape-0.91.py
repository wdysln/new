metadata = """
summary @ Vector graphics editor using the SVG file format
homepage @ http://inkscape.sourceforge.net/
license @ GPL LGPL
src_url @ https://inkscape.global.ssl.fastly.net/media/resources/file/$fullname.tar.bz2
arch @ ~x86_64
options @ 
"""

depends = """
runtime @ >=sys-libs/glib-2.18.1 dev-libs/libxml2 dev-libs/libxslt 
build @ >=dev-util/intltool-0.40 >=dev-util/pkg-config-0.12.0 dev-libs/boost
"""

get("fdo_mime")
get("gnome2_utils")


def configure():
    libtoolize("-f")
    autoreconf()
    conf(
    "--disable-dependency-tracking",
    "--enable-default-binary",
    "--with-x",
    "--with-xmc",
    "--without-xvfb-run")


def build():
    export("PYTHONDONTWRITEBYTECODE", "1")
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
    sed("-i 's|#!/usr/bin/env python|#!/usr/bin/env python2|' %s/usr/lib/gimp/2.0/plug-ins/*.py" % install_dir)
    insdoc("AUTHORS", "ChangeLog*", "HACKING", "NEWS", "README*")
    system("ln -s gimptool-2.0 %s/usr/bin/gimptool" % install_dir)

def post_install():
    desktop_database_update()
    gnome2_icon_cache_update()

def post_remove():
    post_install()
