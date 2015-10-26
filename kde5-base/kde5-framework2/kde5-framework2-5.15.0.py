metadata = """
summary @ KDE Frameworks 5 is a collection of libraries based on top of Qt5 and QML that can be used independently of KDE.
homepage @ https://projects.kde.org/projects/frameworks
license @ LGPL
src_url @ http://download.kde.org/stable/frameworks/5.15/kcrash-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kconfigwidgets-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kglobalaccel-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kpackage-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kservice-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kdesu-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kemoticons-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kiconthemes-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kjobwidgets-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kpeople-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/knotifications-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/ktextwidgets-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kwallet-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kxmlgui-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kbookmarks-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kio-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/frameworkintegration-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kdeclarative-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kinit-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/knewstuff-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/knotifyconfig-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kparts-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kxmlrpcclient-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kcmutils-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kded-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kdewebkit-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/ktexteditor-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kactivities-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kdesignerplugin-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/plasma-framework-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/portingAids/kjs-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/portingAids/kdelibs4support-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/portingAids/khtml-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/portingAids/kjsembed-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/portingAids/kmediaplayer-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/portingAids/kross-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/portingAids/krunner-$version.tar.xz
arch @ ~x86_64
"""

depends = """
build @ kde5-base/kde5-framework1
"""
srcdir = "."

#get("main/cmake_utils")

names = ["kcrash",		
		"kconfigwidgets",
		"kglobalaccel",
		"kpackage",
		"kservice",
		"kdesu",
		"kemoticons",
		"kiconthemes",
		"kjobwidgets",
		"kpeople",
		"knotifications",
		"ktextwidgets",
		"kwallet",
		"kxmlgui",
		"kbookmarks",
		"kio",
		"frameworkintegration",
		"kdeclarative",
		"kinit",
		"knewstuff",
		"knotifyconfig",
		"kparts",
		"kxmlrpcclient",
		"kcmutils",
		"kded",
		"kdewebkit",
		"ktexteditor",
		"kactivities",
		"kdesignerplugin",
		"plasma-framework",
		"kjs",
		"kdelibs4support",
		"khtml",
		"kjsembed",
		"kmediaplayer",
		"kross",
		"krunner"]


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
		
