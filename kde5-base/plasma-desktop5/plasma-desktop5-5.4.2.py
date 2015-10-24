metadata = """
summary @ KDE Frameworks 5 is a collection of libraries based on top of Qt5 and QML that can be used independently of KDE.
homepage @ https://projects.kde.org/projects/frameworks
license @ LGPL
src_url @ http://download.kde.org/stable/plasma/$version/khotkeys-$version.tar.xz 
http://download.kde.org/stable/plasma/$version/powerdevil-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/plasma-desktop-$version.tar.xz 	
arch @ ~x86_64
"""
#TODO "user-manager" http://download.kde.org/stable/plasma/$version/user-manager-$version.tar.xz 		
#"plasma-sdk" http://download.kde.org/stable/plasma/$version/plasma-sdk-$version.tar.xz 
depends = """
build @ kde5-base/plasma-desktop4 
"""

srcdir = "."

#get("main/cmake_utils")

names = ["plasma-desktop",
		"khotkeys", 
		"powerdevil"] 	

		
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
