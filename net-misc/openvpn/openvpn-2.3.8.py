metadata = """
summary @ An easy-to-use, robust, and highly configurable VPN (Virtual Private Network)
homepage @ http://openvpn.net/index.php/open-source.html
license @ custom
src_url @ http://swupdate.openvpn.net/community/releases/$fullname.tar.gz
arch @ ~x86_64
"""

#srcdir = name+"-7.1p1"

depends = """
runtime @ sys-libs/glibc dev-libs/openssl sys-apps/iproute2 app-arch/lzo sys-apps/systemd
"""


def configure():
    system('./configure \
            --prefix=/usr \
            --enable-password-save \
            --with-plugindir="/usr/lib/openvpn/" \
            --enable-iproute2 \
            --enable-systemd')


def install():
    raw_install("DESTDIR=%s" % install_dir)
    makedirs("/etc/openvpn")
    makedirs("/usr/share/openvpn")
    makedirs("/usr/share/openvpn/contrib")
    insfile("sample/sample-config-files/*", "/usr/share/openvpn/examples/")
    copy("contrib", "/usr/share/openvpn")
    insfile("%s/openvpn@.service" % filesdir,"/usr/lib/systemd/system/openvpn@.service")
