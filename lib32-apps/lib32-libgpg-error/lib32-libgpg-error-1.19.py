metadata = """
summary @ Support library for libgcrypt
homepage @ http://www.gnupg.org/
license @ LGPL
src_url @ ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

srcdir = "libgpg-error-%s" % version



def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")


def configure():
    flags()
    raw_configure("--prefix=/usr \
                --libdir=/usr/lib32")

def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/{bin,include,share}"% install_dir)