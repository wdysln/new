metadata = """
summary @ A cross-platform C libraries that allow you to easily implement VNC server 
homepage @ https://libvnc.github.io
license @ GPL
src_url @ https://github.com/LibVNC/$name/archive/LibVNCServer-$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ net-libs/gnutls dev-libs/libgcrypt dev-libs/openssl media-libs/SDL
          media-libs/libjpeg-turbo media-libs/libpng
build @ dev-util/cmake dev-libs/boost dev-util/automoc4
"""
srcdir = "%s-LibVNCServer-%s" % (name, version)


def configure():
    system("./autogen.sh --prefix=/usr")

def build():
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)

