metadata = """
summary @ Open source web browser engine
homepage @ http://www.webkitgtk.org/
license @ LGPL-2 LGPL-2.1 BSD
src_url @ http://webkitgtk.org/releases/webkitgtk-2.4.9.tar.xz
arch @ ~x86_64
options @ introspection debug gstreamer jit spell webgl coverage
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
    "--with-gtk=2.0",
    "--disable-webkit3")

def build():
    export("HOME", build_dir)
    make("XDG_DATA_HOME=\"./.local\"")

def install():
    installd()
    insdoc("Source/WebKit/gtk/ChangeLog")
