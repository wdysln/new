metadata = """
summary @ KDE Base Runtime Environment 
homepage @ http://www.kde.org
license @ GPL LGPL 
src_url @ http://download.kde.org/stable/$version/src/$name-$version.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ media-libs/libcanberra x11-themes/hicolor-icon-theme x11-misc/xprop x11-apps/xauth x11-misc/xsetroot sys-fs/udisks:2
build @ dev-util/cmake dev-util/pkg-config dev-util/automoc4 app-crypt/gpgme kde-base/kdepimlibs kde-base/kactivities
"""

get("main/fdo_mime", "main/cmake_utils", "main/extract_utils")

def extract():
    tar_extract("%s.tar.xz" % fullname)


def configure():
    makedirs("build")
    cd("build")
    cmake_conf(
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_SKIP_RPATH=ON",
    "-DAutomoc4_DIR=/usr/lib/automoc4",
    "-DCMAKE_INSTALL_PREFIX=/usr", sourcedir=build_dir)

def build():
    cd("build")
    make()

def install():
    cd("build")
    installd()
    rmfile("/usr/share/icons/hicolor/index.theme")
    if not islink("/usr/bin/kdesu"):
        makesym("/usr/lib/kde4/libexec/kdesu", "/usr/bin/kdesu")

def post_install():
    desktop_database_update()
    xdg_icon_resource()
