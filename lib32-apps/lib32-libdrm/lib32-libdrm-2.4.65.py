metadata = """
summary @ Userspace interface to kernel DRM services
homepage @ http://dri.freedesktop.org/
license @ MIT
src_url @ http://dri.freedesktop.org/libdrm/$fullname.tar.bz2
arch @ ~x86_64
options @ exynos intel nouveau radeon vmware
"""

depends = """
runtime @ sys-libs/glibc
build @ dev-lang/perl[ithreads] sys-devel/libtool
"""

opt_common = """
intel @ >=x11-libs/libpciaccess-0.10
"""

def prepare():
    system("sed -i '/pthread-stubs/d' configure.ac")

def configure():
    autoreconf("--force --install")
    conf("--enable-udev")
    
    
def install():
    raw_install("DESTDIR=%s" % install_dir)
    # This is no good.
    copy("%s/COPYING" % filesdir, build_dir)
    insdoc("COPYING")
