metadata = """
summary @ A multi-platform MPEG, VCD/DVD, and DivX player
homepage @ http://www.videolan.org/vlc/
license @ LGPL2.1 + GPL2
src_url @ http://download.videolan.org/pub/videolan/$name/$version/$fullname.tar.xz
arch @ ~x86_64
options @ a52 aac alsa altivec avcodec avformat cddb dc1394 dvd dvdnav flac fontconfig gcrypt gnutls libnotify libsamplerate mp3 mpeg ncurses ogg opengl png schroedinger sdl sdl-image sqlite svg taglib theora truetype vaapi vorbis X x264 xcb xml postproc skins debug media-library mmx neon optimisememory run-as-root sse xv
"""

depends = """
build @ app-arch/xz sys-libs/zlib dev-util/pkg-config sys-apps/dbus >=media-libs/a52dec-0.7.4 >=media-libs/faad2-2.6.1 >=media-libs/alsa-lib-1.0.23 >=media-libs/libmpeg2-0.3.2 media-libs/libtheora
runtime @ sys-libs/zlib dev-util/pkg-config sys-apps/dbus >=media-libs/a52dec-0.7.4 >=media-libs/faad2-2.6.1 >=media-libs/alsa-lib-1.0.23 >=media-libs/libmpeg2-0.3.2 media-libs/libtheora
common @ <=dev-lang/lua-5.2.3
"""



#TODO: avcodec and X needed for vaapi
def prepare():
    patch("vlc-2.1.1-desktop.patch")
    patch("vlc-2.0.4-fix-definition.patch")
    patch("vlc-2.0.7-vaapi-compat.patch",level=1)
    patch("vlc-2.1.0-TomWij-bisected-PA-broken-underflow.patch",level=1)

def configure():
    conf(
     "--disable-optimizations",
    "--without-tuning",
    "--enable-fast-install",
    "--disable-swscale",
    "--enable-dbus --enable-dbus-control",
    "--enable-sout")

def install():
    installd()

    insdoc("README", "AUTHORS", "THANKS", "NEWS")

def post_install():
    warn("** Please run vlc-cache-gen manually **")
