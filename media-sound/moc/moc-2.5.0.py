metadata = """
summary @ An ncurses console audio player with support for the mp3, ogg, and wave formats
homepage @ http://moc.daper.net/
license @ GPL
src_url @ http://garr.dl.sourceforge.net/project/moc/moc%20unstable/2.5.0-alpha4/$fullname-alpha4.tar.bz2
arch @ ~x86_64
options @ flac libsamplerate aac mad vorbis sndfile curl debug
"""

depends = """
runtime @ sys-libs/glibc
"""

opt_runtime = """
flac @ media-libs/flac
libsamplerate @ media-libs/libsamplerate
aac @ media-libs/faad2
mad @ media-libs/libmad sys-libs/zlib media-libs/libid3tag
vorbis @ media-libs/libvorbis
sndfile @ media-libs/libsndfile
#ffmpeg @ media-video/ffmpeg
curl @ net-misc/curl
"""

srcdir = fullname + "-alpha4"

def prepare():
    patch()

def configure():
    conf(
    "--without-rcc",
    config_with("flac"),
    config_with("aac"),
    config_with("libsamplerate", "samplerate"),
    config_with("mad", "mp3"),
    config_with("vorbis"),
    config_with("sndfile"),
    "--without-ffmpeg",
    config_with("curl"),
    config_with("debug"))



#TODO new version, enable ffmpeg option
