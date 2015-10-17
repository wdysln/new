metadata = """
summary @ Graph based image processing framework
homepage @ http://www.gegl.org/
license @ GPL3 LGPL3
src_url @ http://download.gimp.org/pub/gegl/0.2/$fullname.tar.bz2
arch @ ~x86_64
options @ cairo exif ffmpeg graphviz jpeg jpeg2k lua openexr png sdl svg debug mmx sse introspection
"""

depends = """
runtime @ >=media-libs/babl-0.1.4 sys-libs/glib x11-libs/gtk+:2 x11-libs/gdk-pixbuf
media-libs/pango sys-libs/zlib
"""

opt_runtime = """
introspection @ >=dev-libs/gobject-introspection-0.10 >=dev-python/pygobject-2.26 media-libs/babl[introspection]
cairo @ x11-libs/cairo
exif @ media-gfx/exiv2
ffmpeg @ media-video/ffmpeg
jpeg @ media-libs/jpeg
jpeg2k @ media-libs/jasper
lua @ dev-lang/lua
openexr @ media-libs/openexr
png @ media-libs/libpng
sdl @ media-libs/SDL
svg @ gnome-base/librsvg
"""

#TODO: more options http://znurt.org/media-libs/gegl/gegl-0.1.6

def configure():
    conf()

def build():
    export("XDG_CONFIG_HOME", build_dir)
    export("XDG_CACHE_HOME", build_dir)
    export("HOME", build_dir)
    make()
