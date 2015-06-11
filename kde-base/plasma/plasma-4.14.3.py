metadata = """
summary @ KDE Plasma Desktop Framework
homepage @ http://kde.org/
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/kde-baseapps-$version.tar.xz
arch @ ~x86_64
"""



get("main/cmake_utils", "main/fdo_mime", "main/extract_utils")

srcdir = "kde-baseapps-%s" % version

extract = lambda: tar_extract("kde-baseapps-%s.tar.xz" % version)



def configure():
    makedirs("build")
    cd("build")
    cmake_conf("-DAutomoc4_DIR=/usr/lib/automoc4",
			sourcedir=build_dir+"/plasma")

build = lambda: (cd("build/plasma"), make())

install = lambda: (cd("build/plasma"), installd())

post_install = lambda: xdg_icon_resource()
