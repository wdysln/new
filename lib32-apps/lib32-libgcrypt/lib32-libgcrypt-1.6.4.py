metadata = """
summary @ a general purpose crypto library based on the code used
homepage @ http://www.gnupg.org/
license @ LGPL
src_url @ ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc >dev-libs/libgpg-error-1.9 lib32-apps/lib32-libgpg-error
"""

srcdir = "libgcrypt-%s" % version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

def prepare():
  #  sed(""" -i 's/basic_LDADD = $(LDADD)/basic_LDADD = $(LDADD) -lgpg-error/' tests/Makefile.in """)
    system(""" sed 's:path="amd64":path="i586 i386":' -i mpi/config.links """)
    
def configure():
    flags()
    raw_configure("--prefix=/usr",
                    "--disable-static",
                    "--libdir=/usr/lib32",
                    "--disable-padlock-support")


def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/{bin,include,share,sbin}"% install_dir)
