metadata = """
summary @ Remote desktop viewer display system
homepage @ http://www.tigervnc.org/
license @ GPL-2
src_url @ https://github.com/TigerVNC/tigervnc/archive/v1.5.0.tar.gz
ftp://ftp.freedesktop.org/pub/xorg/individual/xserver/xorg-server-1.17.2.tar.gz  
arch @ ~x86_64
"""


depends = """
runtime @ sys-libs/zlib x11-base/xorg-server media-libs/mesa
build @ x11-libs/fltk
"""


standard_procedure = False


def prepare():
   # copy("../xorg-server-1.17.2/*", "unix/xserver")
    #system("cp -r ../xorg-server-*/* unix/server")
    patch("gethomedir.patch", level=1)
    sed("-i 's/iconic/nowin/' unix/vncserver") 

  
def build():
    system("cmake -G 'Unix Makefiles' -DCMAKE_INSTALL_PREFIX=/usr")
    make()
    
    system("tar -xf %s/xorg-server-1.17.2.tar.gz -C unix/xserver --strip-components=1" % src_cache)
    cd("unix/xserver")
    system("patch -Np1 -i ../xserver117.patch")
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
    


