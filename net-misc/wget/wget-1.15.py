metadata = """
summary @ A network utility to retrieve files from the Web
homepage @ http://www.gnu.org/software/wget/wget.html
license @ GPL-3
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.xz
arch @ ~x86_64
options @ ipv6 idn debug nls ssl gnutls ntlm
"""

depends = """
runtime @ sys-libs/glibc
"""
opt_runtime = """
idn @ net-dns/libidn
nls @ sys-devel/gettext
ssl @
    gnutls @ net-libs/gnutls || dev-libs/openssl
    ntlm @ dev-libs/openssl
"""

def configure():
    conf(
    "--disable-rpath",
"--with-ssl=openssl")
    

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    echo("ca_certificate=/etc/ssl/certs/ca-certificates.crt" ,"/etc/wgetrc")
    
    insdoc("AUTHORS", "COPYING", "ChangeLog*", "NEWS", "README", "MAILING-LIST")
