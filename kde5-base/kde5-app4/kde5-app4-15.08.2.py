metadata = """
summary @ KDE Frameworks 5 is a collection of libraries based on top of Qt5 and QML that can be used independently of KDE.
homepage @ https://projects.kde.org/projects/frameworks
license @ LGPL
src_url @ http://source.pisilinux.org/1.0/kde-baseapps-15.07.90_20150729.tar.xz
arch @ ~x86_64
"""


depends = """
build @ kde5-base/plasma-desktop4 
"""

srcdir = "."

#get("main/cmake_utils")

names = ["kde-baseapps"]	

		
standard_procedure = False

def configure():
	for packs in names:
		cd("%s" %(packs))
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
		cd("%s" %(packs))
		cd("build")
		make()
		cd("../..")
		
def install():
	for packs in names:
		cd("%s" %(packs))
		cd("build")
		installd()
		cd("../..")
