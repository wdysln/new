metadata = """
summary @ free library for encoding H264/AVC video streams
homepage @ http://www.videolan.org/developers/x264.html
license @ GPL
src_url @ http://download.videolan.org/pub/videolan/x264/snapshots/x264-snapshot-20141201-2245.tar.bz2
arch @ ~x86_64
options @ threads pic debug
"""

depends = """
runtime @ sys-libs/glibc
build @ >=dev-lang/yasm-1.2.0
"""

srcdir = name+"-snapshot-"+version+"-2245"

def configure():
    conf("--prefix=/usr \
	--enable-pic \
	--enable-shared \
	--disable-avs \
	--disable-ffms \
	--disable-lavf \
	--disable-swscale \
	--bit-depth=10")

def install():
    raw_install("DESTDIR=%s bindir=/usr/bin libdir=/usr/lib includedir=/usr/include" % install_dir)

    insdoc("AUTHORS")
