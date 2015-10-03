metadata = """
summary @ XML parsing library, version 2
homepage @ http://www.xmlsoft.org/
license @ MIT
src_url @ ftp://ftp.xmlsoft.org/libxml2/$fullname.tar.gz
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

def prepare():
    patch("revert-catalog-initialize.patch", level=1)
    patch("fix-CVE-2014-3660.patch", level=1)


def configure():
    #autoreconf("-fi")
    conf(
        "--with-threads",
        "--with-history",
        config_enable("ipv6"),
        config_with("readline"),
        config_with("readline", "history"),
        config_with("debug", "run-debug"),
        config_with("icu"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")
