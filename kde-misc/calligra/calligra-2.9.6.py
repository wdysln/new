metadata = """
summary @ An integrated office suite for KDE
homepage @ http://www.calligra-suite.org
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/calligra-2.9.6/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
build @ >=kde-base/kde-runtime-4.14.3 >=kde-base/kdelibs-4.14.3 >=kde-base/kde-workspace-4.11.4 
"""
get("main/kde4_utils")

