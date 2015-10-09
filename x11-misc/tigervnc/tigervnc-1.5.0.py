metadata = """
summary @ Remote desktop viewer display system
homepage @ http://www.tigervnc.org/
license @ GPL-2
src_url @ https://github.com/TigerVNC/tigervnc/archive/v1.5.0.tar.gz
ftp://ftp.freedesktop.org/pub/xorg/individual/xserver/xorg-server-1.17.2.tar.gz  
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

standard_procedure = False


def prepare():
    patch("gethomedir.patch", level=1)
    sed("-i 's/iconic/nowin/' unix/vncserver")
    cd("unix/xserver")
    system("cp -r xorg-server-*/* unix/server")
    patch("xserver117.patch", level=1)
    
  
  
def build():
    system("cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr")
    make()
    cd("unix/xserver")
    autoreconf("-fiv")
    
    system("./configure --prefix=/usr \
	--disable-static --without-dtrace \
	--disable-xorg --disable-xnest --disable-xvfb --disable-dmx \
	--disable-xwin --disable-xephyr --disable-kdrive --disable-xwayland \
	--disable-config-hal --disable-config-udev --with-pic \
	--disable-unit-tests --disable-devel-docs --disable-selective-werror \
	--disable-dri --enable-dri2 --enable-dri3 --enable-glx --enable-glx-tls")
    
    make()



def install():
    raw_install("DESTDIR=%s" % install_dir)
    cd("unix/xserver/hw/vnc")
    raw_install("DESTDIR=%s" % install_dir)
    insfile("%s/vncserver.service" % filesdir, "/usr/lib/systemd/system/vncserver.service")
    insfile("%s/vncviewer.desktop" % filesdir, "/usr/share/applications/vncviewer.desktop")
    


