metadata = """
summary @  Screen Capture Program
homepage @  http://kde.org/applications/graphics/ksnapshot/
license @  GPL + LGPL + FDL
src_url @  http://download.kde.org/stable/$version/src/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ kde-base/kde-workspace kde-base/kdelibs
build @ dev-util/cmake media-libs/taglib media-gfx/exiv2
"""

get("main/kde4_utils")

