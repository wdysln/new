metadata = """
summary @ WebP library and conversion tools
homepage @ https://developers.google.com/speed/webp/
license @ BSD
src_url @ http://downloads.webmproject.org/releases/webp/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ media-libs/libogg
"""

def configure():
    conf("--prefix=/usr \
     --enable-swap-16bit-csp \
     --enable-experimental \
     --enable-libwebpmux \
     --enable-libwebpdemux \
     --enable-libwebpdecoder \
     --disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS", "CHANGES")
