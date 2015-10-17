metadata = """
summary @ Dynamic, any to any, pixel format conversion library
homepage @ http://gegl.org/babl/
license @ LGPL3
src_url @ http://download.gimp.org/pub/babl/0.1/$fullname.tar.bz2
arch @ ~x86_64
options @ altivec mmx sse introspection
"""

opt_runtime = """
introspection @ >=dev-libs/gobject-introspection-0.6.8
"""

def configure():
    conf(
    "--disable-docs",
    config_enable("altivec"),
    config_enable("introspection"),
    config_enable("mmx"),
    config_enable("sse"))

def build():
    export("HOME", build_dir)
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "README", "NEWS")

