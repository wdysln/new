metadata = """
summary @ A library for portable low-level access to a video framebuffer, audio output, mouse, and keyboard
homepage @ http://www.libsdl.org/
license @ LGPL
src_url @ http://www.libsdl.org/release/$fullname.tar.gz
arch @ ~x86_64
options @ alsa nas X dga xv xinerama static-libs alsa-shared pulseaudio pulseaudio-shared
"""

depends = """
build @ media-libs/mesa
"""

opt_runtime = """
pulseaudio @ media-sound/pulseaudio
alsa @ media-libs/alsa-lib
X @ x11-libs/libXt x11-libs/libXext x11-libs/libX11 x11-libs/libXrandr
nas @ media-libs/nas x11-libs/libXt x11-libs/libXext x11-libs/libX11
"""

opt_build = """
nas @ x11-proto/xextproto x11-proto/xproto
X @ x11-proto/xextproto x11-proto/xproto
"""
def prepare():
    sed("-e '/_XData32/s:register long:register _Xconst long:' \
    -i src/video/x11/SDL_x11sym.h")
    
def configure():
    conf("--disable-static")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("BUGS", "CREDITS", "README", "README-SDL.txt", "README.CVS", "TODO", "WhatsNew")
