metadata = """
summary @ POSIX 1003.1e capabilities
homepage @ http://www.kernel.org/pub/linux/libs/security/linux-privs/
license @ GPL
src_url @ https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-$version.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc sys-apps/attr lib32-apps/lib32-attr

"""

standard_procedure = False

srcdir = "libcap-%s" %version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

def build():
    make("-C libcap CC='gcc -m32' prefix=/usr lib=lib32")

def install():
    raw_install("prefix=/usr lib=/lib32 DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/{sbin,include,share}"% install_dir)
  #  make("-C libcap prefix=/usr lib=lib32 DESTDIR=%s install" % install_dir)
    
  #  setmod("755 %s/usr/lib64/libcap.so.%s" % (install_dir, raw_version))
   # rmfile("/usr/lib64/libcap.a")
