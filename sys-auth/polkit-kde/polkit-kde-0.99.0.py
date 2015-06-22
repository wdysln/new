metadata = """
summary @ A library that allows developers to access PolicyKit API with a nice Qt-style API
homepage @ http://www.kde.org/
license @ GPL
src_url @ http://download.kde.org/stable/apps/KDE4.x/admin/polkit-kde-agent-1-0.99.0.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-auth/polkit x11-libs/qt kde-base/kdelibs
"""
srcdir = "polkit-kde-agent-1-0.99.0"

get("main/kde4_utils")