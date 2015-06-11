metadata = """
summary @ A GObject-based API for handling resource discovery and announcement over SSDP
homepage @ http://gupnp.org/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/0.12/$name-$version.tar.xz
arch @ ~x86_64
options @ gtk introspection
"""

depends = """
runtime @ >=sys-libs/glib-2.22
build @ dev-util/pkg-config sys-devel/gettext
"""

opt_runtime = """
gtk @ >=x11-libs/gtk+-2.12:2
introspection @ >=dev-libs/gobject-introspection-0.6.7 >=net-libs/libsoup-2.26.1[introspection] || >=net-libs/libsoup-2.26.1
"""

def configure():
    conf(
    config_enable("introspection"),
    config_enable("gtk"),
    "--disable-dependency-tracking",
    "--disable-static",
    "--disable-gtk-doc")

def build():
    export("HOME", build_dir)
    make()
