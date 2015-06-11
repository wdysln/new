metadata = """
summary @ Extra tools for Ogg-Vorbis
homepage @ http://www.xiph.org/vorbis/
license @ GPL2
src_url @ http://downloads.xiph.org/releases/vorbis/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ media-libs/libao media-libs/libvorbis net-misc/curl media-libs/flac 
"""

def configure():
	conf(
	"--prefix=/usr \
	--without-speex \
	--enable-vcut")

def install():
	raw_install("DESTDIR=%s" % install_dir)

