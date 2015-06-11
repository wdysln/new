metadata = """
summary @ High-speed character set detection library
homepage @ http://atheme.org/project/libguess
license @ BSD
src_url @ https://launchpad.net/ubuntu/+archive/primary/+files/libguess_1.2.orig.tar.bz2
arch @ ~x86_64
options @ examples
"""

depends = """
runtime @ dev-libs/libmowgli
build @ dev-util/pkg-config
"""
srcdir = "libguess-1.2"

def configure():
    conf(
    config_enable("examples"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("README")
