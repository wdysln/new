metadata = """
summary @ Complete and free Internet live audio and video broadcasting solution for Linux/Unix
homepage @ http://ffmpeg.org/
license @ GPL
src_url @ http://www.ffmpeg.org/releases/$fullname.tar.bz2
arch @ ~x86_64
options @ lame rtmp vdpau vorbis xvid x264 vpx theora amr schroedinger jpeg2k cpudetection ieee1394 X vaapi
"""

depends = """
build @ dev-lang/yasm media-libs/libtheora
	media-video/rtmpdump dev-util/pkg-config media-libs/libdc1394 sys-libs/libraw1394 
	media-sound/lame media-libs/libvorbis media-libs/xvidcore media-libs/x264 
	media-libs/libvpx media-libs/libtheora media-libs/opencore-amr media-libs/schroedinger 
dev-util/pkg-config media-libs/openjpeg x11-libs/libX11 x11-libs/libXext x11-libs/libvdpau
runtime @ x11-libs/libXfixes media-libs/alsa-lib app-arch/bzip2
        sys-libs/zlib
        media-libs/SDL_image media-libs/SDL net-libs/gnutls x11-libs/libva x11-libs/libvdpau media-libs/openjpeg
"""

opt_runtime = """
media-video/rtmpdump dev-util/pkg-config media-libs/libdc1394 sys-libs/libraw1394 
media-sound/lame media-libs/libvorbis media-libs/xvidcore media-libs/x264 
media-libs/libvpx media-libs/libtheora media-libs/opencore-amr media-libs/schroedinger 
dev-util/pkg-config media-libs/openjpeg x11-libs/libX11 x11-libs/libXext x11-libs/libvdpau
"""

export("PATH", "%s:/usr/bin/core_perl" % get_env('PATH'))

def configure():
    raw_configure("--prefix=/usr \
--mandir=/usr/share/man \
--disable-debug \
--disable-static \
--disable-stripping \
--enable-avfilter \
--enable-avresample \
--enable-dxva2 \
--enable-fontconfig \
--enable-gnutls \
--enable-gpl \
--enable-libfreetype \
--enable-libopenjpeg \
--enable-libtheora \
--enable-libvorbis \
--enable-libvpx \
--enable-libx264 \
--enable-libxvid \
--enable-pic \
--enable-postproc \
--enable-shared \
--enable-swresample \
--enable-vdpau \
--enable-version3")

def build():
    make()
    make("tools/qt-faststart")
    make("doc/ff{mpeg,play,server}.1")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insexe("tools/qt-faststart", "/usr/bin/qt-faststart")


# more options, install-man etc
