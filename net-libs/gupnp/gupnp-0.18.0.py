metadata = """
summary @ An object-oriented UPNP framework
homepage @ http://gupnp.org/
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/0.18/$name-$version.tar.xz
arch @ ~x86_64
options @ introspection networkmanager
"""

depends = """
runtime @ >=sys-libs/glib-2.24 dev-libs/libxml2
build @ dev-util/pkg-config sys-devel/gettext
"""

opt_runtime = """
introspection @ >=net-libs/gssdp-0.11.2[introspection] || >=net-libs/gssdp-0.11.2
"""

def configure():
    if opt("networkmanager"):
        backend = "network-manager"
    else:
        backend = "unix"

    conf(
    config_enable("introspection"),
    "--disable-static",
    "--disable-dependency-tracking",
    "--disable-gtk-doc",
    "--with-context-manager=%s" % backend)

def build():
    export("HOME", build_dir)
    make()

def install():
    installd()
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README")
