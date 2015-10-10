metadata = """
summary @ A cross-platform C libraries that allow you to easily implement VNC server 
homepage @ https://libvnc.github.io
license @ GPL
src_url @ http://downloads.sourceforge.net/$name/LibVNCServer-$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ net-libs/gnutls dev-libs/libgcrypt dev-libs/openssl media-libs/SDL
          media-libs/libjpeg-turbo media-libs/libpng
build @ dev-util/cmake dev-libs/boost dev-util/automoc4
"""
srcdir = "LibVNCServer-%s" % version


def configure():
    conf("--disable-static \
          --disable-dependency-tracking")


def build():
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)

