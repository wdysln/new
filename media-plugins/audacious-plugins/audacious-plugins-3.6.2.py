metadata = """
summary @ Plugins for Audacious
homepage @ http://audacious-media-player.org/
license @ GPL3
src_url @ http://distfiles.audacious-media-player.org/audacious-plugins-3.6.2.tar.bz2
arch @ ~x86_64
options @ aac alsa aqua cdda cue ffmpeg flac gnome ipv6 lame libnotify libsamplerate mp3 nls scrobbler sndfile sse2 vorbis wavpack
"""

depends = """
runtime @ app-arch/unzip dev-libs/dbus-glib dev-libs/libxml2 media-sound/audacious net-libs/neon x11-libs/gtk+:2 
build @ dev-util/pkg-config
"""

opt_runtime = """
aac @ media-libs/faad2
alsa @ media-libs/alsa-lib
cdda @ media-libs/libcddb dev-libs/libcdio
cue @ media-libs/libcue
ffmpeg @ media-video/ffmpeg
flac @ media-libs/libvorbis media-libs/flac
lame @ media-sound/lame
libnotify @ x11-libs/libnotify
libsamplerate @ media-libs/libsamplerate
mp3 @ media-sound/mpg123
scrobbler @ net-misc/curl
sndfile @ media-libs/libsndfile
vorbis @ media-libs/libvorbis media-libs/libogg
wavpack @ media-sound/wavpack
"""

def configure():
    conf(
    "--prefix=/usr \
            --enable-chardet \
            --disable-adplug \
            --disable-projectm",
            config_with("aac"),
            config_with("alsa"),
            config_enable("alsa", "bluetooth"),
            config_enable("alsa", "amidiplug-alsa"),
            config_enable("aqua", "coreaudio"),
            config_enable("aqua", "dockalbumart"),
            config_enable("cdda", "cdaudio"),
            config_enable("cue"),
            config_with("ffmpeg", "ffaudio"),
            config_with("flac", "flacng"),
            config_enable("flac", "filewriter_flac"),
            config_enable("ipv6"),
            config_enable("gnome", "gnomeshortcuts"),
            config_with("lame", "filewriter_mp3"),
            config_enable("libnotify", "notify"),
            config_enable("libsamplerate", "resample"),
            config_enable("nls"),
            config_enable("scrobbler"),
            config_enable("sndfile"),
            config_enable("sse2"),
            config_enable("vorbis"),
            config_enable("vorbis", "filewriter_vorbis"),
            config_enable("wavpack"))

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insdoc("AUTHORS")
