metadata = """
summary @ An interface to use kipi-plugins from a KDE application
homepage @ http://kde.org/
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ kde-base/kdelibs >=kde-base/kdepimlibs-4.14.3 >=kde-base/kdepim-runtime-4.14.3
build @ dev-util/cmake dev-util/automoc4 kde-base/kfilemetadata kde-base/libkdcraw dev-libs/xapian-core
"""

get("main/kde4_utils", "main/fdo_mime", "main/extract_utils")

post_install = lambda: xdg_icon_resource()
