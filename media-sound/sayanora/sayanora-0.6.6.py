metadata = """
summary @ Linux music player written in C++. It supports all common audio files (like mp3, wav, flac, ogg...). The main focus is on managing your music library.
homepage @ http://sayonara-player.com
license @ GPL3
src_url @ ftp://sayonara-player.com/sayonara/sayonara-player-r57.tar.gz
arch @ ~x86_64
"""

depends = """
build @ dev-util/desktop-file-utils 
        x11-themes/hicolor-icon-theme media-libs/pango x11-libs/cairo x11-libs/gdk-pixbuf media-libs/alsa-lib
        media-libs/imlib2 media-libs/libvorbis media-libs/libogg media-video/ffmpeg
        media-plugins/gst-plugins-bad:0 media-plugins/gst-plugins-base:0 media-plugins/gst-plugins-good:0 media-plugins/gst-plugins-bad:0
        media-plugins/gst-plugins-ugly:0 media-libs/gstreamer:0 media-sound/lame x11-libs/qt x11-libs/libnotify media-libs/taglib
"""
get("main/cmake_utils")


