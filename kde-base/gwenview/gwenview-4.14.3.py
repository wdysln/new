metadata = """
summary @ A fast and easy to use image viewer for KDE
homepage @ http://kde.org/
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ kde-base/kdelibs kde-base/libkipi
build @ dev-util/cmake dev-util/automoc4
"""

get("main/kde4_utils", "main/fdo_mime", "main/extract_utils")

post_install = lambda: (xdg_icon_resource(), desktop_database_update())
