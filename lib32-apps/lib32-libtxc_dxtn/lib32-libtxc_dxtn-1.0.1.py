metadata = """
summary @ S3 Texture Compression (S3TC) library for Mesa
homepage @ http://dri.freedesktop.org/wiki/S3TC
license @ custom BSD
src_url @ http://people.freedesktop.org/~cbrill/libtxc_dxtn/libtxc_dxtn-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc sys-libs/zlib
"""
srcdir = "libtxc_dxtn-%s" % version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

def configure():
    flags()
    conf("--prefix=/usr --libdir=/usr/lib32")

def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/include"% install_dir)
