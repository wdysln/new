metadata = """
summary @ Colibri provides an alternative to KDE4 Plasma notifications.
homepage @ http://kde-apps.org/content/show.php/Colibri?content=117147
license @ GPL
src_url @ http://kde-apps.org/CONTENT/content-files/117147-$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ >=kde-base/kde-workspace-4.8.0
build @ dev-util/cmake dev-util/automoc4
"""

get("main/kde4_utils", "main/fdo_mime")

def post_install():
    xdg_icon_resource()
