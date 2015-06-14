metadata = """
summary @ A movie player for linux
homepage @ http://www.mplayerhq.hu/ 
license @ GPL 
src_url @ http://anduin.linuxfromscratch.org/sources/other/mplayer-2015-02-20.tar.xz
http://ffmpeg.org/releases/ffmpeg-2.5.tar.gz
arch @ ~x86_64
options @ bidi amr a52 theora cdparanoia dts encode lame x264 xvid faad mad schroedinger vpx mng X vdpau sdl vorbis
"""
#src_url @ ftp://ftp.mplayerhq.hu/MPlayer/releases/mplayer-checkout-snapshot.tar.bz2
depends = """
build @ dev-util/pkg-config dev-lang/yasm
runtime @ media-libs/SDL_image media-libs/SDL dev-libs/fribidi media-libs/opencore-amr media-libs/a52dec media-sound/lame media-libs/x264 media-libs/xvidcore media-libs/faad2 media-libs/libmad media-libs/schroedinger 
media-libs/libvpx media-libs/libmng x11-libs/libXinerama x11-libs/libXxf86dga x11-libs/libXxf86vm media-libs/fontconfig media-libs/mesa x11-libs/libXvMC x11-proto/videoproto x11-proto/xf86vidmodeproto x11-misc/libxss 
x11-libs/libvdpau media-libs/libtheora media-libs/libvorbis media-libs/openjpeg media-libs/jpeg media-libs/tiff media-libs/libass media-video/ffmpeg
""" 

import datetime
now = datetime.datetime.now()
srcdir = "mplayer-2015-02-20"
#srcdir = "mplayer-checkout-%s" % now.strftime("%Y-%m-%d")

def prepare():
    copytree("../ffmpeg-2.5", "ffmpeg")
    
def configure():
	raw_configure(
    "--prefix=/usr",
    "--disable-arts",
    "--disable-liblzo",
    "--disable-speex",
    "--disable-esd",
    "--disable-musepack",
    "--confdir=/etc/mplayer",
    "--disable-libdv",
    "--disable-ffmpeg_a")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insfile("%s/mplayer.desktop" % filesdir, "/usr/share/applications/mplayer.desktop")
    insfile("%s/mplayer.png" % filesdir, "/usr/share/pixmaps/mplayer.png")

def post_install():
	system("update-desktop-database -q")

#TODO: Hatalı
