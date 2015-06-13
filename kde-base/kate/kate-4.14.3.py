metadata = """
summary @ KDE MDI editor/IDE
homepage @ http://www.kde.org
license @ GPL-2
src_url @ http://download.kde.org/stable/$version/src/kate-$version.tar.xz
arch @ ~x86_64
"""

depends = """
build @ >=kde-base/kde-runtime-4.14.3 >=kde-base/kdelibs-4.14.3 >=kde-base/kde-workspace-4.11.4
"""

get("main/kde4_utils")
