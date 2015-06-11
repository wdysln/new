metadata = """
summary @ X.org evdev input driver
homepage @ http://xorg.freedesktop.org/
license @ custom
src_url @ http://xorg.freedesktop.org/releases/individual/driver/$fullname.tar.bz2
arch @ ~x86_64
options @ dri sna
"""

opt_common = """
sna @ x11-base/xorg-server x11-libs/pixman
"""

depends = """
common @ x11-libs/libXext x11-libs/libXfixes x11-libs/libXvMC >=x11-libs/libxcb-1.5
        x11-proto/fontsproto x11-proto/xf86driproto x11-libs/libdrm x11-misc/xcb-util
build @ >=x11-proto/dri2proto-2.6 >=x11-base/xorg-server-1.6
"""

def configure():
    conf()

def build():
    make()
    make("check")

def install():
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    notify("Warning: This driver requires KMS support in your kernel.")
