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
    system('CFLAGS="$CFLAGS -DPLUGIN_LIBDIR=\\\"/usr/lib/openvpn\\\"" ./configure \
            --prefix=/usr \
            --sbindir=/usr/bin \
            --enable-password-save \
            --mandir=/usr/share/man \
            --enable-iproute2 \
            --enable-systemd')


def install():
    raw_install("DESTDIR=%s" % install_dir)
    
    insfile("%s/sshdgenkeys.service" % filesdir,"/usr/lib/systemd/system/sshdgenkeys.service")
