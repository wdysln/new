metadata = """
summary @ An alternative implementation of Linux sound support
homepage @ http://www.alsa-project.org/
license @ GPL-2
src_url @ ftp://ftp.alsa-project.org/pub/lib/alsa-lib-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ dev-lang/python:2.7
"""
get("main/lib32_utils")

srcdir = "alsa-lib-%s" %version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
    
    
def configure():
    flags()
    lib32_conf('--disable-python')

def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/include"% install_dir)
    rmdir("/tmp32")