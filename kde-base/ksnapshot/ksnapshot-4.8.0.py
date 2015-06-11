metadata = """
summary @  Screen Capture Program
homepage @  http://kde.org/applications/graphics/ksnapshot/
license @  GPL + LGPL + FDL
src_url @  http://download.kde.org/stable/$version/src/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ >=kde-base/kde-workspace-4.8.0
build @ dev-util/cmake
"""

get("main/kde4_utils")

