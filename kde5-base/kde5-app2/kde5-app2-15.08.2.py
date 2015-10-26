metadata = """
summary @ KDE Frameworks 5 is a collection of libraries based on top of Qt5 and QML that can be used independently of KDE.
homepage @ https://projects.kde.org/projects/frameworks
license @ LGPL
src_url @ http://source.pisilinux.org/1.0/ksnapshot-15.04.3_20150731.tar.gz
arch @ ~x86_64
"""


depends = """
build @ kde5-base/plasma-desktop1
"""

srcdir = "."

#get("main/cmake_utils")

names = ["ksnapshot"]	

		
standard_procedure = False

def configure():
	for packs in names:
		cd("%s" % packs)
		makedirs("build")
		cd("build")
		system("cmake -DCMAKE_BUILD_TYPE=Release \
					-DCMAKE_INSTALL_PREFIX=/usr \
					-DLIB_INSTALL_DIR=lib \
					-DLIBEXEC_INSTALL_DIR=lib \
                                        -DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
					-DKMIX_KF5_BUILD=ON \
					-DQML_INSTALL_DIR=/usr/qml \
					-DBUILD_TESTING=OFF -Wno-dev ..")
		make()
		installd()
		cd("../..")

