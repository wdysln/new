metadata = """
summary @ XML stylesheet transformation library
homepage @ http://xmlsoft.org/XSLT/
license @ MIT
src_url @ftp://xmlsoft.org/libxslt/libxslt-$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc dev-libs/libxml2 dev-libs/libgcrypt
"""
srcdir ="libxslt-%s" %version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")


def configure():
    flags()
    autoreconf("-fi")
    raw_configure("--prefix=/usr",
            "--libdir=/usr/lib32",
            "--without-python")
                    
def build():
    flags()
    export("PYTHONDONTWRITEBYTECODE", "1")
    make()

def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/{bin,include,share}"% install_dir)