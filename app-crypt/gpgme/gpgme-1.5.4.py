metadata = """
summary @ A C wrapper library for GnuPG
homepage @ http://delta.affinix.com/qca/
license @ LGPL
src_url @ ftp://ftp.gnupg.org/gcrypt/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ app-crypt/libassuan app-crypt/gnupg
"""

def configure():
    autoreconf("-vfi")
    raw_configure("--prefix=/usr \
                --disable-fd-passing \
                --disable-static \
              --disable-gpgsm-test")
def build():
    make()
    make("check")
    
def install():
    installd()


