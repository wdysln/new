metadata = """
summary @ Userspace interface to kernel DRM services
homepage @ http://dri.freedesktop.org/
license @ MIT
src_url @ http://dri.freedesktop.org/libdrm/libdrm-$version.tar.bz2
arch @ ~x86_64
options @ exynos intel nouveau radeon vmware
"""

depends = """
runtime @ sys-libs/glibc
build @ dev-lang/perl[ithreads] sys-devel/libtool lib32-apps/lib32-libpciaccess
"""

opt_common = """
intel @ >=x11-libs/libpciaccess-0.10
"""
get("main/lib32_utils")

srcdir = "libdrm-%s" %version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

def prepare():
    system("sed -i '/pthread-stubs/d' configure.ac")
    
    
def configure():
    flags()
    autoreconf("--force --install")
    raw_configure("--prefix=/usr --libdir=/usr/lib32  --enable-udev  --disable-cairo-tests ")
    
    
def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/{bin,include,share}"% install_dir)


