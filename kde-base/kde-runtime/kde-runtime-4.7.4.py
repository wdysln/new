metadata = """
summary @ KDE libraries for the basic desktop applications
homepage @ http://kde.org/
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/$name-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ kde-base/kdelibs
"""

get("main/cmake_utils", "main/extract_utils")

def extract():
    tar_extract("%s.tar.bz2" % fullname)

def configure():
    makedirs("build")
    cd("build")
    cmake_conf(sourcedir=build_dir)

def build():
    cd("build")
    make(j=9)

def install():
    cd("build")
    installd()
    rmfile("/usr/share/icons/hicolor/index.theme")
    makesym("/usr/lib/kde4/libexec/kdesu", "/usr/bin/kdesu")

def post_install():
    system("xdg-icon-resource forceupdate --theme hicolor &> /dev/null")

