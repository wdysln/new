metadata = """
summary @ Linux music player written in C++. It supports all common audio files (like mp3, wav, flac, ogg...). The main focus is on managing your music library.
homepage @ http://sayonara-player.com
license @ GPL3
src_url @ https://github.com/clementine-player/Clementine/archive/1.2.3.tar.gz
arch @ ~x86_64
"""

depends = """
build @ media-plugins/gst-plugins-bad:0 media-plugins/gst-plugins-base:0 media-plugins/gst-plugins-good:0 media-plugins/gst-plugins-bad:0
        media-plugins/gst-plugins-ugly:0 media-libs/gstreamer:0 media-sound/lame x11-libs/qt x11-libs/libnotify media-libs/taglib
"""
srcdir ="tmp/sayonara-player-r57"

get("main/cmake_utils")

def prepare():
    patch(level=1)


