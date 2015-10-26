metadata = """
summary @ KDE Frameworks 5 is a collection of libraries based on top of Qt5 and QML that can be used independently of KDE.
homepage @ https://projects.kde.org/projects/frameworks
license @ LGPL
src_url @ http://download.kde.org/stable/frameworks/5.15/kfilemetadata-$version.tar.xz
http://download.kde.org/stable/frameworks/5.15/baloo-$version.tar.xz
arch @ ~x86_64
"""

depends = """
build @ kde5-base/kde5-framework2 
"""
srcdir = "."

#get("main/cmake_utils")

names = ["kfilemetadata",
		"baloo"]

				
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
