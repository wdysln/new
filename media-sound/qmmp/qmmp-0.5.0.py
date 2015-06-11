metadata = """
summary @ Qt4 based audio-player
homepage @ http://qmmp.ylsoftware.com/
license @ GPL
src_url @ http://qmmp.ylsoftware.com/files/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ media-libs/alsa-lib net-misc/curl x11-themes/hicolor-icon-theme media-libs/libmad media-libs/libvorbis media-libs/libogg x11-libs/qt media-libs/taglib x11-misc/xdg-utils
build @ dev-util/cmake media-libs/flac media-libs/libsamplerate media-libs/libsndfile media-sound/wavpack
"""

def configure():
	pass

def build():
	system("cmake . -DCMAKE_INSTALL_PREFIX=/usr")
	make()

def install():
	#postinstall shit
	#system("which xdg-icon-resource 1>/dev/null 2>/dev/null && xdg-icon-resource forceupdate || true")

	raw_install("DESTDIR=%s" % install_dir)


#hatali optional packages http://projects.archlinux.org/svntogit/community.git/tree/qmmp/trunk/PKGBUILD
