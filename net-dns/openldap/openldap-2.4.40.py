metadata = """
summary @ Lightweight Directory Access Protocol (LDAP) client libraries
homepage @ http://www.openldap.org/
license @ OPENLDAP
src_url @ ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/openldap-$version.tgz
arch @ ~x86_64
options @ icu berkdb perl ssl gnutls tcpd sasl odbc iodbc debug ipv6 syslog 
"""

depends = """
runtime @ sys-libs/glibc dev-libs/cyrus-sasl sys-apps/tcp-wrappers dev-libs/icu dev-libs/openssl sys-libs/db dev-db/unixODBC dev-db/libiodbc
build @ sys-apps/groff 
"""


def configure():
    conf("--enable-crypt",
        "--enable-dynamic",
        "--disable-slapd",
        "--with-threads")


def install():
    raw_install("DESTDIR=%s" % install_dir)

    makesym("liblber.so", "/usr/lib/liblber.so.2")
    makesym("libldap.so", "/usr/lib/libldap.so.2")
    insdoc("ANNOUNCEMENT", "CHANGES", "COPYRIGHT", "README", "LICENSE")
    insexe("%s/slapd" % filesdir, "/etc/rc.d/slapd")
    insfile("%s/slapd.default" % filesdir, "/etc/conf.d/slapd")
    makedirs("/var/lib/openldap")
    makedirs("/etc/openldap/slapd.d")

def post_install():
    #setmod("640", "/etc/openldap/{slapd.conf,DB_CONFIG.example}")
    #setowner("root:439", "/etc/openldap/{slapd.conf,DB_CONFIG.example}")
    system("groupadd -g 439 ldap &>/dev/null")
    system("useradd -u 439 -g ldap -d /var/lib/openldap -s /bin/false ldap &>/dev/null")
    system("chown -R ldap:ldap /var/lib/openldap &>/dev/null")

#def post_remove():
#    system("userdel ldap >/dev/null 2>&1")
#    system("groupdel ldap >/dev/null 2>&1")
