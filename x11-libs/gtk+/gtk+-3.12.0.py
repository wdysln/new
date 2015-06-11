metadata = """
summary @  The GTK+ Toolkit (v3)
homepage @  http://www.gtk.org/
license @  LGPL
src_url @  http://ftp.gnome.org/pub/gnome/sources/gtk+/3.12/$fullname.tar.xz
arch @ ~x86_64
slot @ 3
options @ xinerama cups introspection
"""

depends = """
common @ x11-libs/libXrender x11-libs/libX11 x11-libs/libXi x11-libs/libXt x11-libs/libXext
>=x11-libs/libXrandr-1.3 x11-libs/libXcursor x11-libs/libXfixes x11-libs/libXcomposite
x11-libs/libXdamage >=x11-libs/cairo-1.10.0 >=x11-libs/gdk-pixbuf-2.26.0[X]
>=sys-libs/glib-2.29.14 >=media-libs/pango-1.29.0 >=dev-libs/atk-2.1.5 x11-libs/gtk+:2
media-libs/fontconfig x11-misc/shared-mime-info
build @ dev-util/pkg-config
"""
#TODO: [introspection?] support
# FIXME: introspection data is built against system installation of gtk+:3
# Potential options: IUSE="aqua colord cups debug egl examples +introspection packagekit test vim-syntax wayland X xinerama"

opt_runtime = """
xinerama @ x11-libs/libXinerama
cups @ net-print/cups
introspection @ dev-libs/gobject-introspection
"""

opt_build = """
xinerama @ x11-proto/xineramaproto
"""

def configure():
    export("CXX", "/bin/false")
    conf(
    "--enable-gtk2-dependency",
    "--disable-schemas-compile",
    config_enable("introspection"),
    config_enable("cups"),
    config_enable("xinerama"))

    #FIX THAT
    #edit2 = """sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool"""
    #system(edit2)

def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog*", "HACKING", "NEWS*", "README*")
    insfile("%s/settings.ini" % filesdir, "/etc/gtk-3.0/settings.ini")

def post_install():
	if not system("/usr/bin/gtk-query-immodules-3.0 --update-cache") or \
                not system("/usr/bin/glib-compile-schemas /usr/share/glib-2.0/schemas"):
                    raise BuildError
