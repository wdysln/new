metadata = """
summary @ Common C routines used by GTK+ and other libs
homepage @ http://www.gtk.org
license @ LGPL-2
src_url @ http://ftp.gnome.org/pub/GNOME/sources/$name/2.44/glib-$version.tar.xz
options @ xattr doc static-libs
arch @ ~x86_64
"""

depends = """
common @ sys-libs/zlib dev-libs/libffi sys-libs/glibc dev-libs/pcre
build @ >=sys-devel/gettext-0.11 dev-lang/python:2.7
"""

srcdir ="glib-%s" %version

#get("main/lib32_utils")

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

def prepare():
    flags()
    patch("revert-warn-glib-compile-schemas.patch", level=1, reverse=True)


def configure():
    flags()
    raw_configure("--with-pcre=system \
                --libdir=/usr/lib32 \
               --with-threads=posix \
               --with-includedir=/usr/include \
               --disable-fam")


def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    move("%s/usr/local/bin/gio-querymodules" % install_dir, "/usr/bin/gio-querymodules-32")
    rmdir("/usr/local")