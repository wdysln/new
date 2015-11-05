metadata = """
summary @ System and service manager for Linux
homepage @ http://www.freedesktop.org/wiki/Software/systemd
license @ GPL-2 LGPL-2.1 MIT
src_url @ http://www.freedesktop.org/software/systemd/systemd-$version.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ sys-apps/hwids app-text/docbook-xsl-stylesheets
build @ dev-perl/XML-Parser dev-util/gperf dev-libs/gobject-introspection app-text/docbook-xsl-stylesheets lib32-apps/lib32-libgpg-error
common @ >=sys-apps/util-linux-2.20 >=sys-apps/dbus-1.6.8 sys-libs/libcap
sys-apps/acl >=sys-apps/kmod-12 sys-libs/pam sys-apps/attr 
"""

srcdir = "systemd-%s" % version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

def configure():
    flags()
    raw_configure("--libexecdir=/usr/lib32 \
                --libdir=/usr/lib32 \
                --localstatedir=/var \
                --sysconfdir=/etc \
                --enable-compat-libs \
                --disable-audit \
                --disable-tests \
                --disable-ima \
                --disable-seccomp \
                --disable-pam \
                --disable-kmod \
                --disable-networkd \
                --disable-blkid \
                --disable-libiptc \
                --disable-manpages \
                --without-python \
                --disable-libcryptsetup \
                --with-sysvinit-path= \
                --with-sysvrcnd-path=")

def build():
    flags()
    # I use export to prevent sandbox violations
    export("HOME", build_dir)
    make()

def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/{bin,lib,include,share}"% install_dir)
    rmdir("/etc")
    rmdir("/var")

