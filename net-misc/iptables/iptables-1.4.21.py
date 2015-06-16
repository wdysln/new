metadata = """
summary @ Linux kernel packet control tool
homepage @ http://www.netfilter.org/projects/iptables/index.html
license @ GPL2
src_url @ http://www.netfilter.org/projects/iptables/files/iptables-1.4.21.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc dev-libs/openssl
          sys-fs/sysfsutils
"""

def configure():
    export("HOME", build_dir)
    conf("--disable-static")
    
def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)
