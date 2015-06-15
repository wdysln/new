metadata = """
summary @ Network Management daemon
homepage @ http://www.gnome.org/projects/NetworkManager/
license @ GPL
src_url @ http://ftp.acc.umu.se/pub/gnome/sources/NetworkManager/1.0/NetworkManager-$version.tar.xz
arch @ ~x86_64
options @ gnutls dhcpcd introspection
"""

depends = """
common @ >=sys-apps/dbus-1.2 dev-libs/dbus-glib net-wireless/wireless_tools sys-apps/systemd
    sys-auth/polkit dev-libs/libnl:3.0 net-wireless/wpa_supplicant[dbus] net-libs/libsoup
    >=sys-libs/glib-2.30
"""


srcdir = "NetworkManager-" + version

def prepare():
    patch(level=1)

def configure():
    export("HOME", build_dir)
    autoreconf("-fi")
    system("intltoolize --force --copy --automake")    
    conf("--disable-static \
                         --disable-silent-rules \
                         --disable-wimax \
                         --disable-lto \
                         --disable-config-plugin-ibft \
                         --disable-ifnet \
                         --disable-more-warnings \
                         --enable-modify-system \
                         --enable-concheck \
                         --without-netconfig \
                         --with-libsoup=yes \
                         --with-session-tracking=consolekit \
                         --with-suspend-resume=upower \
                         --with-system-ca-path=/etc/ssl/certs \
                         --with-crypto=nss \
                         --with-dhcpcd=/sbin/dhcpcd \
                         --with-dbus-sys-dir=/etc/dbus-1/system.d \
                         --with-dhclient=/usr/sbin/dhclient \
                         --with-udev-dir=/lib/udev \
                         --with-resolvconf=/etc/resolv.default.conf \
                         --with-iptables=/usr/sbin/iptables \
                         --with-dnsmasq=/usr/sbin/dnsmasq \
                         --localstatedir=/var \
                         --sysconfdir=/etc \
                         --libexecdir=/usr/lib/NetworkManager")
    
    
    
def install():
    export("HOME", build_dir)
    installd()
    insfile("%s/NetworkManager.conf" % filesdir, "/etc/NetworkManager/")
    insfile("%s/NetworkManager.confd" % filesdir, "/etc/conf.d/NetworkManager/")
    
    insfile("%s/01-org.freedesktop.NetworkManager.settings.modify.system.pkla" % filesdir, "/etc/polkit-1/localauthority/10-vendor.d/")

    makedirs("/etc/NetworkManager/dnsmasq.d")

