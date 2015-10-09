metadata = """
summary @ File transfer program to keep remote files into sync
homepage @ http://rsync.samba.org/
license @ Apache
src_url @ https://github.com/neutrinolabs/xrdp/archive/v0.8.0.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-apps/acl
"""
def prepare():
    patch(level=1) 
    sed("-i 's|/etc/sysconfig/xrdp|/etc/xrdp/xrdp.ini|' instfiles/xrdp.service")
    sed("-i 's|/etc/sysconfig/xrdp|/etc/xrdp/xrdp.ini|' instfiles/xrdp-sesman.service")

    system("./bootstrap")
     
def configure():
    conf("--prefix=/usr \
              --with-systemdsystemunitdir=/usr/lib/systemd/system \
              --enable-jpeg \
              --enable-simplesound \
              --enable-fuse \
              --enable-loadpulsemodules")
    
def build():
    make("V=0")

def install():
    raw_install("DESTDIR=%s" % install_dir)

 