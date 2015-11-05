metadata = """
summary @ Freedesktop.org message bus system
homepage @ http://www.freedesktop.org/Software/dbus
license @ GPL-2
src_url @ http://dbus.freedesktop.org/releases/dbus/dbus-$version.tar.gz
arch @ ~x86_64
options @ X static-libs debug
"""

depends = """
build @ dev-libs/expat sys-libs/libcap
runtime @ dev-libs/expat sys-libs/libcap
"""
get("main/lib32_utils")

srcdir = "dbus-%s" %version
def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
    
def configure():
    flags()
    raw_configure("--prefix=/usr",
            "--sysconfdir=/etc",
            "--localstatedir=/var",
            "--libdir=/usr/lib32",
            "--libexecdir=/usr/lib/dbus-1.0",
            "--with-dbus-user=81",
            "--with-system-pid-file=/run/dbus/pid",
            "--with-console-auth-dir=/run/console/",
            "--enable-inotify",
            "--disable-dnotify",
            "--disable-verbose-mode",
            "--disable-static",
            "--disable-tests",
            "--disable-asserts",
            "--disable-systemd")
def build():
    flags()
    make()
    
    
def install():
    flags()
    raw_install('DESTDIR=%s' % install_dir)
    rmdir("/var") 
    rmdir("/etc") 
    system("rm -rf '%s'/usr/{bin,include,lib,share}"% install_dir)
    


