metadata = """
summary @ An open source client for Windows Remote Desktop Services
homepage @ http://www.rdesktop.org/
license @ Apache
src_url @ http://downloads.sourceforge.net/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
commons @ sys-fs/fuse media-libs/libjpeg-turbo x11-libs/libXrandr media-libs/libsamplerate
          media-libs/libao
"""
def prepare():
    patch("rdesktop-send_physical_buttons.diff") 
    
def configure():
    conf("--disable-smartcard \
         --with-ipv6")

def build():
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
 