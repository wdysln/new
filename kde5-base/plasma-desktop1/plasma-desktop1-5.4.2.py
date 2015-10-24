metadata = """
summary @ KDE Frameworks 5 is a collection of libraries based on top of Qt5 and QML that can be used independently of KDE.
homepage @ https://projects.kde.org/projects/frameworks
license @ LGPL
src_url @ http://download.kde.org/stable/plasma/$version/kde-cli-tools-$version.tar.xz 
http://download.kde.org/stable/plasma/$version/kde-gtk-config-$version.tar.xz 
http://download.kde.org/stable/plasma/$version/kdecoration-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/kdeplasma-addons-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/kgamma5-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/khelpcenter-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/kinfocenter-$version.tar.xz 
http://download.kde.org/stable/plasma/$version/kmenuedit-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/kscreen-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/ksshaskpass-$version.tar.xz 		
http://download.kde.org/stable/plasma/$version/kwallet-pam-$version.tar.xz 		
http://download.kde.org/stable/plasma/$version/kwrited-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/libkscreen-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/libksysguard-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/milou-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/muon-$version.tar.xz 		
http://download.kde.org/stable/plasma/$version/plasma-mediacenter-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/plasma-nm-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/plasma-workspace-wallpapers-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/polkit-kde-agent-1-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/systemsettings-$version.tar.xz 	
arch @ ~x86_64
"""

depends = """
build @ kde5-base/kde5-framework15 media-sound/pulseaudio
"""
srcdir = "."

#get("main/cmake_utils")

names = ["kde-cli-tools", 
		"kde-gtk-config", 
		"kdecoration", 	
		"kdeplasma-addons", 	
		"kgamma5", 	
		"khelpcenter", 	
		"kinfocenter", 
		"kmenuedit", 	
		"ksshaskpass", 	
		"kwallet-pam", 	
		"kwrited", 	
		"libkscreen", 	
		"libksysguard", 	
		"milou",	
		"muon",		
		"plasma-mediacenter", 	
		"plasma-nm", 	
		"plasma-workspace-wallpapers", 	
		"polkit-kde-agent-1", 	
		"systemsettings"] 	


		
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
