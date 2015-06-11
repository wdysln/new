metadata = """
summary @ Remote desktop viewer display system
homepage @ http://www.tigervnc.org/
license @ GPL-2
arch @ ~x86_64
options @ nptl server
"""

depends = """
runtime @ sys-libs/zlib media-libs/freetype x11-libs/libSM x11-libs/libXtst
build @ dev-lang/yasm x11-proto/inputproto x11-proto/xextproto x11-proto/xproto
"""

opt_runtime = """
server @ x11-base/xorg-server x11-proto/bigreqsproto x11-proto/compositeproto
    x11-proto/damageproto x11-proto/dri2proto x11-proto/fixesproto x11-proto/fontsproto
    x11-proto/randrproto x11-proto/resourceproto x11-proto/scrnsaverproto x11-proto/trapproto
    x11-proto/videoproto x11-proto/xcmiscproto x11-proto/xineramaproto
    x11-proto/xf86bigfontproto x11-proto/xf86dgaproto x11-proto/xf86driproto
    x11-proto/xf86miscproto x11-proto/xf86vidmodeproto x11-proto/glproto 
    media-libs/mesa x11-proto/renderproto x11-libs/libpciaccess x11-libs/xtrans
"""

#if opt("server"):
#    src_url = ftp://ftp.freedesktop.org/pub/xorg/individual/xserver/xorg-server-1.10.4.tar.bz2  http://downloads.sourceforge.net/project/tigervnc/tigervnc/$version/$name-Linux-i686-$version.tar.gz
#else:
#     src_url = http://downloads.sourceforge.net/project/tigervnc/tigervnc/$version/$name-Linux-i686-$version.tar.gz


def configure():
    system("pwd")
    system("pwd")
    #if opt("server"):
        #system("cp -r xorg-server-*/* unix/server")
    conf()

def install():
    raw_install("DESTDIR=%s" % install_dir)

#TODO: ALL http://gpo.zugaina.org/AJAX/Ebuild/2420655/View
