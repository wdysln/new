metadata = """
summary @ KDE Frameworks 5 is a collection of libraries based on top of Qt5 and QML that can be used independently of KDE.
homepage @ https://projects.kde.org/projects/frameworks
license @ LGPL
src_url @ http://download.kde.org/stable/frameworks/5.15/kdnssd-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kwidgetsaddons-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kwindowsystem-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/solid-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/sonnet-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kauth-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/kfilemetadata-$version.tar.xz
arch @ ~x86_64
"""

depends = """
build @ kde5-base/kde5-framework1
"""
srcdir = "."

#get("main/cmake_utils")

names = ["kdnssd",
		"kwidgetsaddons",
		"kwindowsystem",
		"solid",
		"sonnet",
		"kauth",
		"kfilemetadata"]
					

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
