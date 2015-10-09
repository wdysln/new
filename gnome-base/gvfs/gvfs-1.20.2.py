metadata = """
summary @ GNOME Virtual Filesystem Layer
homepage @ http://www.gnome.org
license @ LGPL
src_url @ http://ftp.gnome.org/pub/gnome/sources/$name/1.20/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
common @ sys-libs/glib sys-apps/dbus dev-libs/libxml2 net-misc/openssh
"""

def prepare():
    patch("a.patch", level=1)

def configure():
    conf("--with-dbus-service-dir=/usr/share/dbus-1/services \
         --disable-hal \
         --disable-silent-rules \
         --disable-static \
         --enable-afc \
         --enable-archive \
         --enable-bash-completion \
         --disable-gphoto2 \
         --enable-bluray \
         --enable-keyring \
         --enable-udev \
         --enable-udisks2")
def build():
    make()
    
    




