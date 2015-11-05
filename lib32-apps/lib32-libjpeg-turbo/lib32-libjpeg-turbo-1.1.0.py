metadata = """
summary @ libjpeg derivative with accelerated baseline JPEG compression and decompression
homepage @ http://libjpeg-turbo.virtualgl.org/
license @ GPL
src_url @ http://sourceforge.net/projects/$name/files/$version/libjpeg-turbo-$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
build @ dev-lang/nasm
"""
srcdir = "libjpeg-turbo-%s" % version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

def configure():
    flags()
    autoreconf("-fi")
    raw_configure("--prefix=/usr \
                    --with-jpeg8 --without-simd \
                    --libdir=/usr/lib32")

def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/{bin,include,share}"% install_dir)
