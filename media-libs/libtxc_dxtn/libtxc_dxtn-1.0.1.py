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


def configure():
    conf()

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
