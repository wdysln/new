metadata = """
summary @ KDE Frameworks 5 is a collection of libraries based on top of Qt5 and QML that can be used independently of KDE.
homepage @ https://projects.kde.org/projects/frameworks
license @ LGPL
arch @ ~x86_64
"""

depends = """
runtime @ sys-fs/udisks sys-power/upower sys-auth/polkit-qt5
build @ x11-libs/qt5 kde5-base/extra-cmake-modules kde5-base/libdbusmenu-qt5 x11-base/xorg-server dev-libs/boost
		media-libs/libjpeg-turbo x11-misc/shared-mime-info media-libs/libpng:1.5 media-gfx/exiv2 media-libs/taglib
		dev-libs/libgcrypt app-text/poppler app-text/hspell app-text/hunspell app-text/aspell dev-db/lmdb
		media-libs/phononqt5 app-text/docbook-xsl-stylesheets app-crypt/gpgme net-misc/networkmanager
		media-libs/giflib media-sound/pulseaudio x11-misc/xcb-util-cursor media-gfx/fontforge x11-libs/wayland
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

