metadata = """
summary @ A C wrapper library for GnuPG
homepage @ http://delta.affinix.com/qca/
license @ LGPL
src_url @ ftp://ftp.gnupg.org/gcrypt/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ app-crypt/libassuan dev-libs/libksba dev-libs/pth
"""
def configure():
   # autoreconf("-vfi")
    patch(level=1)
    raw_configure("--enable-symcryptrun \
                         --disable-rpath \
                         --prefix=/usr \
                         --enable-gpgtar \
                         --enable-maintainer-mode")
def build():
    make()
    make("check")

def install():
    installd()
    makesym("gpg2", "/usr/bin/gpg")
    makesym("gpgv2", "/usr/bin/gpgv")
    
def post_install():
    system("/bin/chmod u+s,go-r /usr/bin/gpg2")
    system("/bin/chmod u+s,go-r /usr/bin/gpg-agent")       