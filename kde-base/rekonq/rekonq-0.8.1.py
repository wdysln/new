metadata = """
summary @ A WebKit based web browser for KDE
homepage @ http://rekonq.kde.org/
license @ GPL-2
src_url @ http://garr.dl.sourceforge.net/project/rekonq/0.8.1/0.8.1/rekonq-0.8.1.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ kde-base/keditbookmarks
"""

get("main/cmake_utils", "main/fdo_mime", "main/extract_utils")

extract = lambda: tar_extract("%s.tar.bz2" % fullname)
prepare = lambda: makedirs("build")
configure = lambda: (cd("build"), cmake_conf(sourcedir=build_dir))
build = lambda: (cd("build"), make())
install = lambda: (cd("build"), installd())
post_install = lambda: (xdg_icon_resource(), desktop_database_update())

