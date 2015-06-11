metadata = """
summary @ Paint program for KDE
homepage @ http://kde.org/
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ kde-base/kdebase-libs media-libs/qimageblitz
build @ dev-util/cmake dev-util/automoc4
"""

get("main/cmake_utils", "main/fdo_mime", "main/extract_utils")
extract = lambda: tar_extract("%s.tar.bz2" % fullname)
prepare   = lambda: makedirs("build")
configure = lambda: (cd("build"), cmake_conf(sourcedir=build_dir))
build     = lambda: (cd("build"), make())
install   = lambda: (cd("build"), installd())
post_install = lambda: (xdg_icon_resource(), desktop_database_update())
