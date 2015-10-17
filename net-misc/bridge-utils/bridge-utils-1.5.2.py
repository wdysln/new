metadata = """
summary @ Utilities for configuring the Linux ethernet bridge
homepage @ http://www.linuxfoundation.org/collaborate/workgroups/networking/bridge
license @ GPL
src_url @ http://downloads.sourceforge.net/bridge/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc dev-libs/openssl
"""

def configure():
    autoconf()
    conf("--prefix=/usr \
                         --datarootdir=/usr/share \
                         --with-linux-headers=/usr/include \
                         --sbindir=/usr/bin \
                         --sysconfdir=/etc")
    
def build():
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
