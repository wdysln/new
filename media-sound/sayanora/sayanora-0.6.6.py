metadata = """
summary @ Audio player for GNU/Linux systems with X11
homepage @ http://deadbeef.sourceforge.net
license @ GPL2
src_url @ https://github.com/Alexey-Yakovenko/deadbeef/archive/0.6.2.tar.gz
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


