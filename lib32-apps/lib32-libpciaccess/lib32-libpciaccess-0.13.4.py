metadata = """
summary @ Library providing generic access to the PCI bus and devices
homepage @ http://xorg.freedesktop.org/
license @ MIT
src_url @ http://xorg.freedesktop.org/releases/individual/lib/libpciaccess-$version.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
build @ x11-misc/util-macros
"""
get("main/lib32_utils")

srcdir = "libpciaccess-%s" %version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
    
    
def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/include"% install_dir)

