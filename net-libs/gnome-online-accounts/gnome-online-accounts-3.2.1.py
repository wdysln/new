metadata = """
summary @ GNOME service to access online accounts
homepage @ http://www.gnome.org
license @ GPL
src_url @ http://download.gnome.org/sources/$pkgname/3.2/$pkgname-$pkgver.tar.xz
arch @ ~x86_64
options @ introspection
"""

depends = """
runtime @ >=sys-libs/glib-2.30.0 dev-libs/json-glib gnome-base/libgnome-keyring
net-libs/libsoup:2.4 net-libs/rest:0.7
net-libs/webkit-gtk:3 >=x11-libs/gtk+-3.0.0 >=x11-libs/libnotify-0.7
media-libs/pango
build @ dev-libs/libxslt dev-util/intltool sys-devel/gettext
postmerge @ >=gnome-base/gnome-control-center-3.2
"""
#build @ dev-libs/libxslt >=dev-util/gdbus-codegen-2.30.0 dev-util/intltool

opt_runtime = """
introspection @ >=dev-libs/gobject-introspection-0.6.2
"""

def configure():
    conf(
    "--disable-static",
    config_enable("introspection"))

def build():
    export("HOME", build_dir)
    make()

def install():
    installd()
