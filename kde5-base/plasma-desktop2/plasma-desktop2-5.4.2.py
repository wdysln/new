metadata = """
summary @ KDE Frameworks 5 is a collection of libraries based on top of Qt5 and QML that can be used independently of KDE.
homepage @ https://projects.kde.org/projects/frameworks
license @ LGPL
src_url @ http://download.kde.org/stable/plasma/$version/breeze-$version.tar.xz
http://download.kde.org/stable/plasma/$version/plasma-pa-$version.tar.xz 
http://download.kde.org/stable/plasma/$version/oxygen-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/kwin-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/ksysguard-$version.tar.xz 
http://download.kde.org/stable/plasma/$version/kscreen-$version.tar.xz
arch @ ~x86_64
"""

depends = """
build @ kde5-base/plasma-desktop1 x11-misc/xcb-util-cursor
"""
srcdir = "."

#get("main/cmake_utils")

names = ["breeze",
		"plasma-pa", 
		"oxygen", 	
		"kwin", 
		"ksysguard", 
		"kscreen"] 	


		
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
