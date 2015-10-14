metadata = """
summary @ An image loading library for GTK+ V2
homepage @ http://www.gtk.org/
license @ GPL2
src_url @ ftp://ftp.gnome.org/pub/gnome/sources/gdk-pixbuf/2.31/gdk-pixbuf-$version.tar.xz
arch @ ~x86_64
options @ debug introspection X jpeg tiff
"""

depends = """
runtime @ sys-libs/glib media-libs/libpng x11-libs/libX11 media-libs/tiff media-libs/jpeg
build @ dev-util/pkg-config sys-devel/gettext media-libs/jasper
"""


def configure():
    export("HOME", build_dir)
    conf("--disable-static \
         --disable-silent-rules \
         --with-libjasper \
	 --with-x11 \
         --with-included-loaders=png")


def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING", "AUTHORS")

def post_install():
    if not system("/usr/bin/gdk-pixbuf-query-loaders --update-cache"):
        raise BuildError
