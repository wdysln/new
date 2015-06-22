metadata = """
summary @ The Oil Runtime Compiler
homepage @ http://code.entropywave.com/projects/orc/
license @ BSD BSD-2
src_url @ http://gstreamer.freedesktop.org/data/src/$name/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    conf(
    "--prefix=/usr --disable-static")

def build():
    export("HOME", build_dir)
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("COPYING")
