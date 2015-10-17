metadata = """
summary @ GNU Image Manipulation Program
homepage @ http://www.gimp.org/
license @ GPL LGPL
src_url @ http://download.gimp.org/pub/gimp/v2.8/$fullname.tar.bz2
arch @ ~x86_64
options @ alsa aalib altivec curl dbus debug doc exif gnome jpeg lcms mmx mng pdf png python smp sse svg tiff webkit wmf udev
slot @ 2
"""


get("fdo_mime")
get("gnome2_utils")

"""
def prepare():
    patch("gimp-2.7.4-no-deprecation.patch")
    patch("gimp-2.7.5-configure-gs-bzip2.patch", level=1)
"""

def configure():
  #  libtoolize("-f")
   # autoreconf()
    conf(
    "--disable-dependency-tracking",
    "--enable-default-binary",
    "--with-x",
    "--with-xmc",
    "--without-xvfb-run",
    config_with("aalib", "aa"),
    config_with("alsa"),
    config_enable("altivec"),
    config_with("curl", "libcurl"),
    config_with("dbus"),
    config_with("gnome", "gvfs"),                
    config_with("webkit"),
    config_with("jpeg", "libjpeg"),
    config_with("exif", "libexif"),
    config_with("lcms"),
    config_enable("mmx"),
    config_with("mng", "libmng"),
    config_with("pdf", "poppler"),
    config_with("png", "libpng"),
    config_enable("python"),
    config_enable("smp", "mp"),
    config_enable("sse"),
    config_with("svg", "librsvg"),
    config_with("tiff", "libtiff"),
    config_with("wmf"),
    config_with("udev", "gudev"))

def build():
    export("PYTHONDONTWRITEBYTECODE", "1")
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
  #  sed("-i 's|#!/usr/bin/env python|#!/usr/bin/env python2|' %s/usr/lib/gimp/2.0/plug-ins/*.py" % install_dir)
    insdoc("AUTHORS", "ChangeLog*", "HACKING", "NEWS", "README*")
    system("ln -s gimptool-2.0 %s/usr/bin/gimptool" % install_dir)

def post_install():
    desktop_database_update()
    gnome2_icon_cache_update()

def post_remove():
    post_install()
