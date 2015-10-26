metadata = """
summary @ KDE Frameworks 5 is a collection of libraries based on top of Qt5 and QML that can be used independently of KDE.
homepage @ https://projects.kde.org/projects/frameworks
license @ LGPL
src_url @ http://download.kde.org/stable/plasma/$version/breeze-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/kde-cli-tools-$version.tar.xz 
http://download.kde.org/stable/plasma/$version/kde-gtk-config-$version.tar.xz  
http://download.kde.org/stable/plasma/$version/kdecoration-$version.tar.xz    
http://download.kde.org/stable/plasma/$version/kdeplasma-addons-$version.tar.xz   
http://download.kde.org/stable/plasma/$version/kgamma5-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/khelpcenter-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/khotkeys-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/kinfocenter-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/kmenuedit-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/kscreen-$version.tar.xz    
http://download.kde.org/stable/plasma/$version/ksshaskpass-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/ksysguard-$version.tar.xz   
http://download.kde.org/stable/plasma/$version/kwallet-pam-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/kwayland-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/kwayland-integration-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/kwin-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/kwrited-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/libkscreen-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/libksysguard-$version.tar.xz 
http://download.kde.org/stable/plasma/$version/milou-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/oxygen-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/oxygen-fonts-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/plasma-desktop-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/plasma-nm-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/plasma-pa-$version.tar.xz 	
http://download.kde.org/stable/plasma/$version/plasma-workspace-$version.tar.xz 
http://download.kde.org/stable/plasma/$version/plasma-workspace-wallpapers-$version.tar.xz 
http://download.kde.org/stable/plasma/$version/polkit-kde-agent-1-$version.tar.xz 
http://download.kde.org/stable/plasma/$version/powerdevil-$version.tar.xz 
http://download.kde.org/stable/plasma/$version/systemsettings-$version.tar.xz 
http://download.kde.org/stable/applications/15.04.2/src/oxygen-icons-15.04.2.tar.xz
arch @ ~x86_64
"""

depends = """
build @ kde5-base/kde5-framework2 dev-libs/xapian-core
"""
srcdir = "."

#get("main/cmake_utils")

names = ["kde-cli-tools",
		"kdecoration",
		"kde-gtk-config",
		"kwayland",
		"kwayland-integration",
		"libkscreen",
		"libksysguard",
		"kgamma5",
		"breeze",
		"kwin",
		"oxygen",
		"oxygen-fonts",
		"khelpcenter",
		"kinfocenter",
		"ksysguard",
		"ksshaskpass",
		"kwallet-pam",
		"systemsettings",
		"plasma-workspace",
		"plasma-workspace-wallpapers",
		"khotkeys",
		"kmenuedit",
		"kscreen",
		"kwrited",
		"milou",
		"plasma-nm",
		"plasma-pa",
		"plasma-workspace-wallpapers",
		"polkit-kde-agent-1",
		"powerdevil",
		"plasma-desktop",
		"oxygen-icons",
		"kdeplasma-addons"]	


		
standard_procedure = False

def configure():
	rename("oxygen-icons-15.04.2","oxygen-icons-5.4.2")

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

