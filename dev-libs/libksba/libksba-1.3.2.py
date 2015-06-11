metadata = """
summary @ A CMS and X.509 access library
homepage @ ftp://ftp.gnupg.org/gcrypt/alpha/libksba
license @ GPL
src_url @ ftp://ftp.gnupg.org/gcrypt/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc dev-libs/libxml2 dev-libs/libgcrypt 
"""


def install():
    installd()