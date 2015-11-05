metadata = """
summary @ Access control list utilities, libraries and headers
homepage @ http://savannah.nongnu.org/projects/acl
license @ LGPL-2
src_url @ http://download.savannah.gnu.org/releases/acl/acl-$version.src.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ >=sys-apps/attr-2.4.46
"""
srcdir = "acl-%s" %version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

def configure():
    flags()
    variables = {"INSTALL_USER": "root",
        "INSTALL_GROUP": "root"}
    for key in variables:
        export(key, variables[key])
    raw_configure("--prefix=/usr --libdir=/usr/lib32 --libexecdir=/usr/lib32")

def install():
    flags()
    raw_install("DIST_ROOT='%s' install install-lib install-dev" % install_dir)
    system("rm -rf '%s'/usr/{bin,include,share}"% install_dir)