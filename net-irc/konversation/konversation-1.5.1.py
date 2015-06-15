metadata = """
summary @ Archiving tool
homepage @ http://kde.org/
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$name/$version/src/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
build @ >=kde-base/kde-runtime-4.14.3 >=kde-base/kdelibs-4.14.3 >=kde-base/kde-workspace-4.11.4
"""
get("main/kde4_utils")

