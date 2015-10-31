metadata = """
summary @ Cairo vector graphics library
homepage @ http://cairographics.org/
license @ LGPL + MPL
src_url @ http://cairographics.org/releases/$fullname.tar.xz
arch @ ~x86_64
options @ X debug opengl svg xcb drm static-libs
"""

depends = """
common @ media-libs/fontconfig media-libs/freetype media-libs/libpng:1.2 sys-libs/zlib >=x11-libs/pixman-0.18.4 sys-libs/glib 
build @ dev-util/pkg-config sys-devel/libtool app-arch/xz x11-libs/libX11 media-libs/mesa
"""

opt_runtime = """
opengl @ media-libs/mesa
X @ >=x11-libs/libXrender-0.6 x11-libs/libXext x11-libs/libX11 x11-libs/libXft
    drm @ sys-apps/systemd
xcb @ x11-libs/libxcb x11-misc/xcb-util
svg @ dev-libs/libxml2
"""

opt_build = """
X @ x11-proto/renderproto
    drm @ x11-proto/xproto >=x11-proto/xextproto-7.1
"""
export("PATH", "%s:/usr/bin" % get_env('PATH'))
#TODO: Gallium and some opts
def prepare():
    append_cflags("-flto -ffat-lto-objects")
    patch(level=1)
    autoreconf("-vfi")
    
def configure():
    conf("--disable-static \
          --enable-xlib \
          --enable-ft \
          --enable-ps \
           --enable-pdf \
           --enable-svg \
           --enable-tee \
           --enable-gl \
           --enable-gobject \
           --disable-gtk-doc")

def install():
    #debug says parallel install fails
    raw_install("-j1 DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "README")