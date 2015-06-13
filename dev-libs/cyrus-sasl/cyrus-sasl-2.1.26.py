metadata = """
summary @ Cyrus Simple Authentication Service Layer (SASL) library
homepage @ http://cyrusimap.web.cmu.edu/downloads.html#sasl
license @ as-is
src_url @ ftp://ftp.cyrusimap.org/$name/$fullname.tar.gz	  
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/db sys-libs/pam
"""

def prepare():
    patch(level=1)

def configure():
    conf("--prefix=/usr        \
         --sysconfdir=/etc    \
         --enable-auth-sasldb \
         --with-dbpath=/var/lib/sasl/sasldb2 \
         --with-saslauthd=/var/run/saslauthd")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
