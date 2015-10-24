metadata = """
summary @ KDE Frameworks 5 is a collection of libraries based on top of Qt5 and QML that can be used independently of KDE.
homepage @ https://projects.kde.org/projects/frameworks
license @ LGPL
src_url @ http://download.kde.org/stable/frameworks/5.15/portingAids/khtml-$version.tar.xz
arch @ ~x86_64
"""

depends = """
build @ kde5-base/kde5-framework14 media-libs/giflib
"""

#get("main/cmake_utils")

srcdir = "khtml-5.15.0"
		
standard_procedure = False

def configure():
	makedirs("build")
	cd("build")
	system("cmake -DCMAKE_BUILD_TYPE=Release \
					-DCMAKE_INSTALL_PREFIX=/usr \
					-DLIB_INSTALL_DIR=lib \
					-DLIBEXEC_INSTALL_DIR=lib \
					-DBUILD_TESTING=OFF -Wno-dev ..")

		
def build():
	cd("build")
	make()

		
def install():
	cd("build")
	installd()

