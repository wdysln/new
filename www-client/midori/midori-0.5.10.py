metadata = """
summary @ Lightweight web browser (GTK2)
homepage @ http://www.midori-browser.org/
license @ LGPL2.1
src_url @ "http://www.midori-browser.org/downloads/$name_$version_all_.tar.bz2"
arch @ ~x86_64
"""

depends = """
runtime @ app-arch/bzip2 sys-libs/zlib dev-libs/openssl 
build @ gnome-base/librsvg net-libs/libsoup
"""

get("main/cmake_utils")

def configure():
    conf("-DUSE_GTK3=OFF \
          -DUSE_APIDOCS=ON \
          -DUSE_GRANITE=ON \
          -DUSE_ZEITGEIST=ON \
         -DCMAKE_SKIP_RPATH=ON \    
         -DCMAKE_SKIP_INSTALL_RPATH=ON")

def install():
    raw_install("DESTDIR=%s" % install_dir)
