metadata = """
summary @ Freedesktop.org message bus system
homepage @ http://www.freedesktop.org/Software/dbus
license @ GPL-2
src_url @ http://dbus.freedesktop.org/releases/$name/$name-$version.tar.gz
arch @ ~x86_64
options @ X static-libs debug
"""

depends = """
build @ dev-libs/expat sys-libs/libcap
runtime @ dev-libs/expat sys-libs/libcap
"""

#opt_runtime = """
#X @ x11-libs/libX11 x11-libs/libXt
#"""

def configure():
    autoreconf("-fi")
    raw_configure("--prefix=/usr --sysconfdir=/etc --localstatedir=/var \
      --libexecdir=/usr/lib/dbus-1.0 --with-dbus-user=dbus \
      --with-system-pid-file=/run/dbus/pid \
      --with-system-socket=/run/dbus/system_bus_socket \
      --with-console-auth-dir=/run/console/ \
      --enable-inotify --disable-dnotify \
      --disable-verbose-mode --disable-static \
      --disable-tests --disable-asserts \
      --with-systemdsystemunitdir=/usr/lib/systemd/system \
      --enable-systemd")


def install():
    raw_install('DESTDIR=%s' % install_dir)
    insexe("%s/30-dbus" % filesdir, "/etc/X11/xinit/xinitrc.d/30-dbus")



