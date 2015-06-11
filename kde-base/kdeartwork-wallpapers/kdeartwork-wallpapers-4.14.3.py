metadata = """
summary @ KDE Wallpapers
homepage @ http://kde.org/
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/kdeartwork-$version.tar.xz
arch @ ~x86_64
"""

get("main/cmake_utils", "main/extract_utils")

srcdir = "kdeartwork-%s" % version

extract = lambda: tar_extract("kdeartwork-%s.tar.xz" % version)

prepare   = lambda: makedirs("build")

def configure():
    cd("build")
    cmake_conf(sourcedir=build_dir+"/wallpapers")
    cmake_conf(sourcedir=build_dir+"/HighResolutionWallpapers")
standard_procedure = False
def install():
    cd("build/wallpapers")
    installd()
    cd(build_dir)
    cd("build/HighResolutionWallpapers")
    installd()
#build     = lambda: (cd("build/dolphin"), make())
#install   = lambda: (cd("build/dolphin"), installd())
#post_install = lambda: xdg_icon_resource()
