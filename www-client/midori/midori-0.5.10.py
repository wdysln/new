metadata = """
summary @ Lightweight web browser (GTK2)
homepage @ http://www.midori-browser.org/
license @ LGPL2.1
src_url @ "http://www.midori-browser.org/downloads/$name_$version_all_.tar.bz2"
arch @ ~x86_64
"""

depends = """
runtime @ app-arch/bzip2 sys-libs/zlib dev-libs/openssl sys-libs/gpm
build @ gnome-base/librsvg net-libs/libsoup
"""

srcdir = "links-2.3pre2"

def configure():
    conf("--enable-javascript",
            "--disable-graphics",
            "--without-x",
            "--without-fb")

def install():
    raw_install("DESTDIR=%s" % install_dir)
