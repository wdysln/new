metadata = """
summary @ KDE Frameworks 5 is a collection of libraries based on top of Qt5 and QML that can be used independently of KDE.
homepage @ https://projects.kde.org/projects/frameworks
license @ LGPL
src_url @ http://download.kde.org/stable/frameworks/5.15/attica-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kapidox-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/karchive-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kcodecs-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kconfig-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kcoreaddons-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kdbusaddons-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/ki18n-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kidletime-$version.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ sys-fs/udisks sys-power/upower sys-auth/polkit-qt5
build @ x11-libs/qt5 kde5-base/extra-cmake-modules kde5-base/libdbusmenu-qt5 x11-base/xorg-server dev-libs/boost
		media-libs/libjpeg-turbo x11-misc/shared-mime-info media-libs/libpng:1.5 media-gfx/exiv2 media-libs/taglib
		dev-libs/libgcrypt app-text/poppler app-text/hspell app-text/hunspell app-text/aspell dev-db/lmdb
		media-libs/phononqt5 app-text/docbook-xsl-stylesheets app-crypt/gpgme
"""
srcdir = "."

#get("main/cmake_utils")

names = ["attica",
			"kapidox",
			"karchive",
			"kcodecs",
			"kconfig",
			"ki18n",
			"kidletime",
			"kcoreaddons",
			"kdbusaddons"]
			

standard_procedure = False

def configure():
	for packs in names:
		cd("%s-%s" %(packs,version))
		makedirs("build")
		cd("build")
		system("cmake -DCMAKE_BUILD_TYPE=Release \
					-DCMAKE_INSTALL_PREFIX=/usr \
					-DLIB_INSTALL_DIR=lib \
					-DLIBEXEC_INSTALL_DIR=lib \
					-DBUILD_TESTING=OFF -Wno-dev ..")
		cd("../..")
		
def build():
	for packs in names:
		cd("%s-%s" %(packs,version))
		cd("build")
		make()
		cd("../..")
		
def install():
	for packs in names:
		cd("%s-%s" %(packs,version))
		cd("build")
		installd()
		cd("../..")
