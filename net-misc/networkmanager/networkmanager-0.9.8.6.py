metadata = """
summary @ Network Management daemon
homepage @ http://www.gnome.org/projects/NetworkManager/
license @ GPL
src_url @ http://ftp.acc.umu.se/pub/gnome/sources/NetworkManager/0.9/NetworkManager-$version.tar.xz
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
    autoreconf("-fi")
    system("intltoolize --force --copy --automake")
    raw_configure("--prefix=/usr \
    --sysconfdir=/etc \
    --localstatedir=/var \
    --with-crypto=nss \
    --with-iptables=/usr/sbin/iptables \
    --with-dnsmasq=/usr/bin/dnsmasq \
    --with-systemdsystemunitdir=/usr/lib/systemd/system \
    --disable-static \
    --disable-ppp \
    --enable-more-warnings=no \
    --disable-wimax \
    --with-udev-dir=/usr/lib/udev \
    --with-session-tracking=systemd \
    --enable-modify-system \
    --enable-doc")
    
    
def build():
    make("check")
    
    
def install():
    installd()
    insfile("%s/NetworkManager.conf" % filesdir, "/etc/NetworkManager/")
    insfile("%s/NetworkManager.confd" % filesdir, "/etc/conf.d/NetworkManager/")
    
    insfile("%s/01-org.freedesktop.NetworkManager.settings.modify.system.pkla" % filesdir, "/etc/polkit-1/localauthority/10-vendor.d/")

    makedirs("/etc/NetworkManager/dnsmasq.d")

