metadata = """
summary @ The libsecret package contains a GObject based library for accessing the Secret Service API. 
homepage @ https://wiki.gnome.org/Projects/Libsecret
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/libsecret/0.18/libsecret-0.18.tar.xz
arch @ ~x86_64
"""

depends = """
common @ >=sys-libs/glib-2.26 >=dev-libs/dbus-glib-0.88 >=gnome-base/libgnome-keyring-2.20 
>=sys-apps/dbus-1.4.1 >=sys-auth/polkit-0.96-r1 >=x11-libs/gtk+-3:3 >=x11-libs/libnotify-0.7.0 
app-i18n/iso-codes >=net-misc/networkmanager-0.9.6
"""

def build():
    export("HOME", build_dir)
    
def install():
    export("HOME", build_dir)
    raw_install("INSTALL_ROOT=%s" % install_dir)
