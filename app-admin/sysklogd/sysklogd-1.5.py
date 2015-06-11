metadata = """
summary @ System and kernel log daemons
homepage @ http://www.infodrom.org/projects/sysklogd/
license @ GPL BSD
src_url @ http://www.infodrom.org/projects/sysklogd/download/$fullname.tar.gz
arch @ ~x86_64
"""

# FIXME: logrotate will be added 
depends = """
runtime @ sys-libs/glibc
"""

def install():
    for i in ("man8", "man5"):
        makedirs("/usr/share/man/%s" % i)
    makedirs("/usr/sbin")
    raw_install("INSTALL=/bin/install prefix=%s" % install_dir)
    copy("%s/syslog.conf" % filesdir, "/etc/syslog.conf")
