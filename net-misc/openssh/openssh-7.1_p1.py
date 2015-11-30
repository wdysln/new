metadata = """
summary @ Free version of the SSH connectivity tools
homepage @ http://www.openssh.org/portable.html
license @ BSD
src_url @ ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/$name-7.1p1.tar.gz
arch @ ~x86_64
options @ libedit tcpd
"""

srcdir = name+"-6.1p1"

depends = """
runtime @ sys-libs/glibc >=dev-libs/openssl-1.0.1
"""

opt_runtime = """
libedit @ dev-libs/libedit
tcpd @ sys-apps/tcp-wrappers
"""

def configure():
    raw_configure("--prefix=/usr",
            "--libdir=/usr/lib",
            "--libexecdir=/usr/lib/ssh",
            "--sysconfdir=/etc/ssh --with-privsep-user=nobody",
            "--with-md5-passwords --with-pam --with-mantype=man --mandir=/usr/share/man",
            "--with-xauth=/usr/bin/xauth --with-ssl-engine",
            "--disable-strip",
            config_with("libedit"),
            config_with("tcpd", "tcp-wrappers"))


def install():
    raw_install("DESTDIR=%s" % install_dir)
    makedirs("/etc/conf.d")
    makedirs("/etc/pam.d")
    
    
    
    insfile("%s/sshdgenkeys.service" % filesdir,"/usr/lib/systemd/system/sshdgenkeys.service")
    insfile("%s/sshd@.service" % filesdir, "/usr/lib/systemd/system/sshd@.service")
    insfile("%s/sshd.service" % filesdir, "/usr/lib/systemd/system/sshd.service")
    insfile("%s/sshd.socket" % filesdir, "/usr/lib/systemd/system/sshd.socket")
    insfile("%s/sshd.conf" % filesdir, "/usr/lib/tmpfiles.d/sshd.conf")
    
   # insfile("%s/sshd.confd" % filesdir, "/etc/conf.d/sshd")
    insfile("%s/sshd.pam" % filesdir, "/etc/pam.d/sshd")
    insexe("%s/contrib/findssl.sh" % build_dir, "/usr/bin/findssl.sh")
    insexe("%s/contrib/ssh-copy-id" % build_dir, "/usr/bin/ssh-copy-id")
    insfile("%s/contrib/ssh-copy-id.1" % build_dir, "/usr/share/man/man1/ssh-copy-id.1")

    makedirs("/var/empty/sshd")

    insdoc("ChangeLog", "CREDITS", "OVERVIEW", "README*", "TODO", "sshd_config")
