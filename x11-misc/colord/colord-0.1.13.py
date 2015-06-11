metadata = """
summary @ Color daemon
homepage @ http://www.freedesktop.org/software/colord
license @ GPL2
src_url @  http://www.freedesktop.org/software/colord/releases/$fullname.tar.xz
arch @ ~x86_64
options @ introspection scanner udev doc
"""

depends = """
common @ dev-db/sqlite >=sys-libs/glib-2.28.0 >=dev-libs/libusb-1.0.8:1 >=media-libs/lcms-2.2
build @ dev-libs/libxslt >=dev-util/intltool-0.35 dev-util/pkg-config >=sys-devel/gettext-0.17
"""

opt_runtime = """
introspection @ >=dev-libs/gobject-introspection-0.9.8
scanner @ media-gfx/sane-backends
udev @ sys-fs/udev[gudev,extras]
"""

opt_build = """
doc @ =app-text/docbook-xml-dtd:4.1.2 >=dev-util/gtk-doc-1.9
introspection @ dev-lang/vala:0.14
"""

def configure():
    conf(
    "--disable-examples",
    "--disable-static",
    "--disable-polkit",
    "--enable-reverse",
    "--disable-volume-search",
    "--localstatedir=/var",
    config_enable("doc", "gtk-doc"),
    config_enable("introspection"),
    config_enable("scanner", "sane"),
    config_enable("udev", "gudev"))

def build():
    export("HOME", build_dir)
    if opt("doc"):
        make(j=1)
    else:
        make()

def install():
    installd()
    insdoc("AUTHORS", "ChangeLog", "MAINTAINERS", "NEWS", "README", "TODO")
