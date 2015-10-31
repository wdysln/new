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
http://download.kde.org/stable/frameworks/5.15/kdnssd-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kguiaddons-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/ki18n-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kidletime-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kimageformats-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kitemmodels-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kitemviews-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kplotting-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kwidgetsaddons-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kwindowsystem-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/networkmanager-qt-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/solid-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/sonnet-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/threadweaver-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kauth-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kcompletion-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kdoctools-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kpty-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kunitconversion-$version.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ sys-fs/udisks sys-power/upower sys-auth/polkit-qt5
build @ x11-libs/qt5 kde5-base/extra-cmake-modules kde5-base/libdbusmenu-qt5 x11-base/xorg-server dev-libs/boost
		media-libs/libjpeg-turbo x11-misc/shared-mime-info media-libs/libpng:1.5 media-gfx/exiv2 media-libs/taglib
		dev-libs/libgcrypt app-text/poppler app-text/hspell app-text/hunspell app-text/aspell dev-db/lmdb
		media-libs/phononqt5 app-text/docbook-xsl-stylesheets app-crypt/gpgme net-misc/networkmanager
		media-libs/giflib media-sound/pulseaudio x11-misc/xcb-util-cursor media-gfx/fontforge x11-libs/wayland
		dev-libs/xapian-core new/dev-perl/URI
"""
srcdir = "."


names = ["attica",
		"kapidox",
		"karchive",
		"kcodecs",
		"kconfig",
		"kcoreaddons",
		"kdbusaddons",
		"kdnssd",
		"kguiaddons",
		"ki18n",
		"kidletime",
		"kimageformats",
		"kitemmodels",
		"kitemviews",
		"kplotting",
		"kwidgetsaddons",
		"kwindowsystem",
		"networkmanager-qt",
		"solid",
		"sonnet",
		"threadweaver",
		"kauth",
		"kcompletion",
		"kdoctools",
		"kpty",
		"kunitconversion"]


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
			-DCMAKE_PREFIX_PATH=%s/usr \
			-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
			-DQML_INSTALL_DIR=/usr/qml \
			-DBUILD_TESTING=OFF -Wno-dev .."% install_dir)
		make()
		installd()
		cd("../..")
		
