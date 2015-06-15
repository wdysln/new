metadata = """
summary @  Screen Capture Program
homepage @  http://kde.org/applications/graphics/ksnapshot/
license @  GPL + LGPL + FDL
src_url @  http://download.kde.org/stable/$version/src/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ >=kde-base/kde-workspace-4.14.3
build @ dev-util/cmake
"""

get("main/kde4_utils")

