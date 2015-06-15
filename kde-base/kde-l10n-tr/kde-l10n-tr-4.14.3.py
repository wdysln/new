metadata = """
summary @ Turkish Localization for KDE
homepage @ http://kde.org/
license @ GPL 
src_url @ http://download.kde.org/stable/$version/src/kde-l10n/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
common @ >=kde-base/kdelibs-4.14.3
build @ dev-util/cmake dev-util/automoc4
"""

get("main/kde4_utils")
