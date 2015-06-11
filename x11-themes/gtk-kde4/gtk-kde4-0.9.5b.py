metadata = """
summary @ Allows you to change style, icons, font of GTK applications in KDE4.
homepage @  http://kde-look.org/content/show.php?content=74689
license @ GPL
src_url @ http://hadronproject.org/distfiles/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ kde-base/kde-workspace x11-themes/gtk-engines
build @ dev-util/cmake dev-util/automoc4
"""

get("main/cmake_utils", "main/extract_utils")

srcdir = name


def configure():
    cmake_conf()

def install():
    raw_install("DESTDIR=%s" % install_dir)

