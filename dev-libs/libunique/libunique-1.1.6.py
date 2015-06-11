metadata = """
summary @ Library for writing single instance applications
homepage @ http://live.gnome.org/LibUnique
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/1.1/$fullname.tar.bz2
arch @ ~x86_64
slot @ 1
"""

depends = """
common @ >=sys-libs/glib-2.25.7 x11-libs/libX11
build @ >=dev-util/pkg-config-0.17 x11-libs/gtk+:2 
"""

def prepare():
    patch("99_ltmain_as-needed.patch",level=0)
    patch("libunique-1.1.6-G_CONST_RETURN.patch",level=1)
    patch("fix-unused-but-set-variable.patch",level=0)
    patch("fix-disable-deprecated.patch",level=1)
    patch("unique-1.0.6-fix-str-fmt.patch",level=0)


def configure():
    conf(
    "--disable-static",
    "--disable-maintainer-flags",
    "--disable-dbus")

def build():
    export("HOME", build_dir)
    make()

def install():
    installd()
   
