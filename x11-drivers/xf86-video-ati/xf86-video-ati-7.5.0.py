metadata = """
summary @ X.org ati video driver
homepage @ http://xorg.freedesktop.org/
license @ GPL
src_url @ http://xorg.freedesktop.org/archive/individual/driver/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ x11-proto/glproto x11-proto/xf86driproto x11-proto/dri2proto x11-libs/libdrm x11-drivers/glamor-egl
"""
def configure():
    export("HOME", build_dir)
    conf("--disable-static",
	"--enable-dri")

def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)


