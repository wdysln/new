metadata = """
summary @ PIM layer, which provides an asynchronous API to access all kind of PIM data
homepage @ http://community.kde.org/KDE_PIM/Akonadi
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$name/src/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ dev-db/sqlite dev-libs/boost x11-misc/shared-mime-info dev-libs/soprano
"""

get("main/kde4_utils")


