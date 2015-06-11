metadata = """
summary @ Wrapper library for evdev devices
homepage @ http://www.freedesktop.org
license @ LGPL + MPL
src_url @ http://www.freedesktop.org/software/libevdev/$fullname.tar.xz
arch @ ~x86_64
"""

    
def configure():
    conf("--disable-static \
          --disable-gcov")

def install():
    raw_install("DESTDIR=%s" % install_dir)
