metadata = """
summary @ Linux music player written in C++. It supports all common audio files (like mp3, wav, flac, ogg...). The main focus is on managing your music library.
homepage @ http://sayonara-player.com
license @ GPL3
src_url @ https://github.com/clementine-player/Clementine/archive/master.zip
arch @ ~x86_64
"""

depends = """
build @ media-plugins/gst-plugins-bad:0 media-plugins/gst-plugins-base:0 media-plugins/gst-plugins-good:0 media-plugins/gst-plugins-bad:0
        media-plugins/gst-plugins-ugly:0 media-libs/gstreamer:0 media-sound/lame x11-libs/qt x11-libs/libnotify media-libs/taglib
"""

get("main/cmake_utils")

srcdir = "Clementine-master"

def configure():
    cmake_conf(" -DBUILD_WERROR=OFF \
                 -DBUNDLE_PROJECTM_PRESETS=OFF \
                  -DUSE_BUILTIN_TAGLIB=OFF \
                  -DENABLE_BREAKPAD=OFF \
                  -DENABLE_GIO=ON \
                   -DUSE_SYSTEM_QXT=ON \
                   -DUSE_SYSTEM_GMOCK=ON")

                         
