metadata = """
summary @ Open source web browser engine
homepage @ http://www.webkitgtk.org/
license @ LGPL-2 LGPL-2.1 BSD
src_url @ http://www.webkitgtk.org/webkit-$version.tar.gz
arch @ ~x86_64
options @ introspection debug gstreamer jit spell webgl coverage
"""

depends = """
runtime @ dev-libs/libxml2 dev-libs/libxslt media-libs/jpeg >=media-libs/libpng-1.4 
>=x11-libs/cairo-1.10 >=sys-libs/glib-2.27.90 >=dev-libs/icu-3.8.1-r1 
dev-db/sqlite >=media-libs/pango-1.12 x11-libs/libXrender
build @ >=sys-devel/flex-2.5.33 sys-devel/gettext  dev-util/gperf
dev-util/pkg-config
"""
#build @  dev-util/gtk-doc-am

opt_runtime = """
gstreamer @ media-libs/gstreamer >=media-libs/gst-plugins-base-0.10.30
introspection @  >=dev-libs/gobject-introspection-0.9.5 >=x11-libs/gtk+-3.0[introspection] >=net-libs/libsoup-2.33.6[introspection] || >=x11-libs/gtk+-3.0 >=net-libs/libsoup-2.33.6
spell @ >=app-text/enchant-0.22
webgl @ media-libs/mesa
"""

srcdir = "webkit-%s" % version

def prepare():
    sed(""" -i 's/-O2//g' configure.ac""")
    system("mkdir -p DerivedSources/ANGLE")
    system("AT_M4DIR=Source/autotools autoreconf")

def configure():
    conf(
    config_enable("coverage"),
    config_enable("debug"),
    config_enable("debug", "debug-features"),
    config_enable("spell", "spellcheck"),
    config_enable("introspection"),
    config_enable("gstreamer", "video"),
    config_enable("jit"),
    config_enable("webgl"),
    "--with-font-backend=freetype",
    "--enable-web-sockets",
    "--with-gtk=3.0",
    "--disable-webkit2")

def build():
    export("HOME", build_dir)
    make("XDG_DATA_HOME=\"./.local\"")

def install():
    installd()
    insdoc("Source/WebKit/gtk/ChangeLog")
