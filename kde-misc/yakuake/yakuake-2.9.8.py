metadata = """
summary @ A KDE konsole application with the look and feel of that in the Quake engine 
homepage @ http://yakuake.kde.org 
license @ GPL 
src_url @ http://download.kde.org/stable/$name/$version/src/$name-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ >=kde-base/konsole-4.8.0
build @ dev-util/cmake sys-devel/gettext
"""

get("main/kde4_utils", "main/fdo_mime")

def post_install():
    xdg_icon_resource()
