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
webgl @ media-libs/mesa media-libs/libwebp
"""

srcdir = "webkitgtk-%s" % version


def configure():
    conf("--disable-gtk-doc \
         --disable-silent-rules \
         --disable-webkit2 \
         --enable-dependency-tracking \
         --enable-introspection \
         --enable-video \
         --with-gnu-ld \
         --with-gtk=2.0")
    
def build():
    make()

def install():
    raw_install("-j1 DESTDIR=%s install" % install_dir)
    
