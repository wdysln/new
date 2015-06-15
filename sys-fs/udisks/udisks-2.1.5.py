metadata = """
summary @ Disk Management Service
homepage @ http://www.freedesktop.org/wiki/Software/udisks
license @ GPL
src_url @ http://udisks.freedesktop.org/releases/udisks-2.1.5.tar.bz2
arch @ ~x86_64
slot @ 2
"""

depends = """
runtime  @ sys-apps/systemd sys-apps/sg3_utils sys-libs/glib dev-libs/dbus-glib
           sys-auth/polkit sys-block/parted dev-libs/libatasmart sys-process/lsof
build @ dev-util/intltool
"""

def configure():
    raw_configure("--prefix=/usr --sysconfdir=/etc \
      --sbindir=/usr/bin \
      --with-systemdsystemunitdir=/usr/lib/systemd/system \
      --localstatedir=/var --disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)

