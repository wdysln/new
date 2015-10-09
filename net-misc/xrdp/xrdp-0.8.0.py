metadata = """
summary @ File transfer program to keep remote files into sync
homepage @ http://rsync.samba.org/
license @ Apache
src_url @ https://github.com/neutrinolabs/xrdp/archive/v0.8.0.tar.gz
arch @ ~x86_64
"""

depends = """
commons @ sys-fs/fuse media-libs/libjpeg-turbo x11-libs/libXrandr x11-misc/tigervnc
"""
def prepare():
    patch(level=1) 
    sed("-i 's|/etc/sysconfig/xrdp|/etc/xrdp/xrdp.ini|' instfiles/xrdp.service")
    sed("-i 's|/etc/sysconfig/xrdp|/etc/xrdp/xrdp.ini|' instfiles/xrdp-sesman.service")
    
    sed("-i 's|/usr/local/sbin|/usr/bin|' instfiles/xrdp.sh")
    sed("-i 's|/usr/sbin|/usr/bin|' instfiles/xrdp.service")
    sed("-i 's|/usr/sbin|/usr/bin|' instfiles/xrdp-sesman.service")
    system("./bootstrap")
     
def configure():
    conf("--prefix=/usr \
         --with-systemdsystemunitdir=/usr/lib/systemd/system \
         --sbindir=/usr/bin \
         --enable-jpeg \
         --enable-fuse")

    
def build():
    make("V=0")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
def post_install():
    system("xrdp-keygen xrdp /etc/xrdp/rsakeys.ini")

def post_remove():
    post_install("rm /etc/xrdp/rsakeys.ini")
 