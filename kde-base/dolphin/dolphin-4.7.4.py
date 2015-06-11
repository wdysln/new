metadata = """
summary @ File Manager for KDE
homepage @ http://kde.org/
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/kde-baseapps-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ kde-base/kdelibs kde-base/kdebase-libs
"""

get("kde4_utils")

srcdir = "kde-baseapps-%s" % version
subdir = "dolphin"

