metadata = """
summary @ A C wrapper library for GnuPG
homepage @ http://delta.affinix.com/qca/
license @ LGPL
src_url @ ftp://ftp.gnupg.org/gcrypt/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/qt app-misc/ca-certificates app-crypt/libassuan
"""

def configure():
    
            
    raw_configure("--prefix=/usr \
                --disable-fd-passing --disable-static \
              --disable-gpgsm-test")

def install():
    installd()
    insdoc("COPYING")

