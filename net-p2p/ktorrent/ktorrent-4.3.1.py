metadata = """
summary @ A powerful BitTorrent client for KDE 
homepage @ http://ktorrent.org 
license @ GPL2 
src_url @ http://ktorrent.pwsp.net/downloads/$version/$name-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ net-libs/libktorrent kde-base/kde-workspace media-libs/taglib
build @ dev-util/cmake dev-libs/boost dev-util/automoc4
"""

get("main/fdo_mime")

def prepare():
	patch("fix-link.patch", level=1)

def configure():
	pass

def build():
	system("mkdir build")
	cd("./build")
	system("cmake ../ \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=/usr \
	-DENABLE_MEDIAPLAYER_PLUGIN=true \
	-DAutomoc4_DIR=/usr/lib/automoc4 \
	-DENABLE_SYNDICATION_PLUGIN=false")
	make()

def install():
	cd("./build")
	raw_install("DESTDIR=%s" % install_dir)

def post_install():
    desktop_database_update()
    xdg_icon_resource()
    update_mime_database()

#opts http://gpo.zugaina.org/net-p2p/ktorrent
