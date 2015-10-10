metadata = """
summary @ A jukebox, tagger and music collection manager
homepage @ http://kde.org/
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
build @ >=kde-base/kde-runtime-4.14.3 >=kde-base/kdelibs-4.14.3 >=kde-base/kde-workspace-4.11.4 media-libs/phonon-backend-gstreamer
"""
get("main/kde4_utils")

