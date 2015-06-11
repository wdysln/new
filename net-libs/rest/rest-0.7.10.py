metadata = """
summary @ Helper library for RESTful services
homepage @ http://git.gnome.org/browse/librest
license @ GPL2
src_url @ http://download.gnome.org/sources/$name/0.7/$name-$version.tar.bz2
arch @ ~x86_64
options @ introspection
"""

depends = """
runtime @ >=sys-libs/glib-2.18 dev-libs/libxml2:2 net-libs/libsoup:2.4
build @ >=dev-util/intltool-0.40 dev-util/pkg-config
"""

opt_runtime = """
introspection @ >=dev-libs/gobject-introspection-0.6.7 
"""

def configure():
    conf(
    "--disable-static",
    "--disable-gcov",
    "--with-gnome",
    config_enable("introspection"))

def build():
    export("HOME", build_dir)
    make()

def install():
    installd()
    insdoc("AUTHORS", "NEWS", "README")

