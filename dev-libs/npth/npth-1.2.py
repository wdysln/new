metadata = """
summary @ New portable threads library
homepage @ http://git.gnupg.org/cgi-bin/gitweb.cgi?p=npth.git
license @ LGPL
src_url @ ftp://ftp.gnupg.org/gcrypt/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc dev-libs/libxml2 dev-libs/libgcrypt 
"""


def install():
    installd()