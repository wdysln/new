metadata = """
summary @ XML parsing library, version 2
homepage @ http://www.xmlsoft.org/
license @ MIT
src_url @ ftp://ftp.xmlsoft.org/libxml2/libxml2-$version.tar.gz
arch @ ~x86_64
options @ icu debug ipv6 readline
"""

depends = """
runtime @ sys-libs/glibc sys-libs/ncurses sys-libs/zlib
build @ dev-lang/perl[ithreads]
"""

opt_runtime = """
readline @ sys-libs/readline
icu @ dev-libs/icu
"""
srcdir ="libxml2-%s" %version

def flags():
    append_cflags("-m32")
    append_cxxflags("-m32")
    append_ldflags("-m32")
    export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")


def prepare():
    patch("revert-catalog-initialize.patch", level=1)
    patch("fix-CVE-2014-3660.patch", level=1)


def configure():
    flags()
    autoreconf("-fi")
    raw_configure(
        "--with-threads",
        "--with-history",
        "--without-python",
        "--libdir=/usr/lib32",
        "--prefix=/usr",
        config_enable("ipv6"),
        config_with("readline"),
        config_with("readline", "history"),
        config_with("debug", "run-debug"),
        config_with("icu"))

def install():
    flags()
    raw_install("DESTDIR=%s" % install_dir)
    system("rm -rf '%s'/usr/{bin,include,share}"% install_dir)
