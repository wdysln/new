metadata = """
summary @ KDE Base Workspace 
homepage @ http://www.kde.org
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/kde-workspace-$version.tar.bz2
arch @ ~x86_64
"""

# @seqizz klavuzu arch linux olanin burnu boktan cikmaz

#runtime @ sys-auth/consolekit x11-libs/libXinerama x11-libs/libXcomposite x11-libs/libXdamage
#    x11-libs/libXklavier media-libs/libdmtx sci-libs/libqalculate media-libs/qimageblitz
#    sys-libs/libraw1394 x11-misc/xprop x11-misc/xsetroot
depends = """
build @ dev-util/cmake media-libs/qimageblitz dev-util/desktop-file-utils kde-base/kdelibs
"""

get("main/cmake_utils", "main/extract_utils")

def extract():
    system("tar xf %s/kde-workspace-%s.tar.bz2 -C %s" % (src_cache, version, dirname(build_dir)))

def prepare():
    makedirs("build")

def configure():
    cd("build")
    cmake_conf("-DCMAKE_SKIP_RPATH=ON",
	"-DWITH_Xmms=OFF",
	"-DWITH_Googlegadgets=OFF",
        "-DWITH_NetworkManager=OFF", sourcedir=build_dir)

def build():
	cd("build")
        make()

def install():
    cd("build")
    raw_install("DESTDIR=%s" % install_dir)
    makedirs("/etc/rc.d")
    makedirs("/etc/pam.d")
    insexe("%s/kdm" % filesdir, "/etc/rc.d/kdm")
    insfile("%s/kde.pam" % filesdir, "/etc/pam.d/kde")
    insfile("%s/kde-np.pam" % filesdir, "/etc/pam.d/kde-np")
    insfile("%s/kscreensaver.pam" % filesdir, "/etc/pam.d/kscreensaver")
    makedirs("/usr/share/xsessions")
    makesym("/usr/share/apps/kdm/sessions/kde-plasma.desktop", "/usr/share/xsessions/kde-plasma.desktop")
    makesym("/usr/share/apps/kdm/sessions/kde-safe.desktop", "/usr/share/xsessions/kde-safe.desktop")
    makedirs("/etc/kde/env")
    makedirs("/etc/kde/shutdown")
    system("install -d -g 135 -o 135 %s/var/lib/kdm" % install_dir)

def post_install():
    for item in ('groupadd -g 135 kdm &>/dev/null', 'useradd -u 135 -g kdm -d /var/lib/kdm -s /bin/false -r -M kdm &>/dev/null', \
            'chown -R 135:135 /var/lib/kdm &>/dev/null', 'xdg-icon-resource forceupdate --theme hicolor &>/dev/null', 'update-desktop-database -q'):
        system(item)
