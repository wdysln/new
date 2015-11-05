metadata = """
summary @ Extended attribute support library for ACL support
homepage @ http://oss.sgi.com/projects/xfs/
license @ LGPL-2
src_url @ http://download.savannah.gnu.org/releases-noredirect/attr/attr-$version.src.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""
get("main/lib32_utils")

srcdir = "attr-%s" %version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
    export("INSTALL_USER","root")
    export("INSTALL_GROUP","root")
    
def configure():
    flags()
    raw_configure("--prefix=/usr --libdir=/usr/lib32 --libexecdir=/usr/lib32")
    
    
def install():
    flags()
    raw_install("DIST_ROOT=%s install install-lib install-dev" % install_dir)
    system("rm -rf '%s'/usr/{bin,include,share}"% install_dir)
    system("rm -f %s/usr/lib32/libattr.a" %install_dir)