metadata = """
summary @ A utility providing key negotiation for WPA wireless networks
homepage @ http://hostap.epitest.fi/wpa_supplicant
license @ GPL
src_url @ http://hostap.epitest.fi/releases/$fullname.tar.gz
arch @ ~x86_64
options @ dbus debug eap-sim readline gnutls 
"""

depends = """
runtime @ dev-libs/openssl sys-apps/dbus sys-libs/readline dev-libs/libnl:3.0
"""

opt_runtime = """
readline @ sys-libs/ncurses sys-libs/readline
gnutls @ net-libs/gnutls
"""

def prepare():
    cd(name)
    patch(level=1)
    copy("%s/config" % filesdir, "./.config")




def build():
    cd(name)
    make("LIBDIR=/usr/lib BINDIR=/usr/bin")

def install():
    cd(name)
    raw_install("LIBDIR=/usr/lib BINDIR=/usr/bin DESTDIR=%s" % install_dir)
