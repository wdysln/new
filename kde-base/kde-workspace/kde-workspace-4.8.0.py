metadata = """
summary @ KDE Base Workspace 
homepage @ http://www.kde.org
license @ GPL LGPL FDL 
src_url @ http://download.kde.org/stable/$version/src/kde-workspace-$version.tar.bz2
arch @ ~x86_64
options @ xinerama qalculate semantic
"""

# TODO: media-libs/phonon[vlc] removed due to lpms bug. Don't need a revision for now, will add when adding back..





get("main/cmake_utils", "main/extract_utils")

def extract():
    system("tar xf %s/kde-workspace-%s.tar.bz2 -C %s" % (src_cache, version, dirname(build_dir)))

def configure():
    extraconf = ""

    if opt("semantic"):
        extraconf += " -DWITH_Akonadi=ON -DWITH_Nepomuk=ON -DWITH_Soprano=ON "
    else:
        extraconf += " -DWITH_Akonadi=OFF -DWITH_Nepomuk=OFF -DWITH_Soprano=OFF "
    if opt("xinerama"):
        extraconf += " -DWITH_X11_Xinerama=ON "
    else:
        extraconf += " -DWITH_X11_Xinerama=OFF "
    
    makedirs("build")
    cd("build")
    cmake_conf(
    cmake_config_with("qalculate"),
    "-DCMAKE_SKIP_RPATH=ON",
	"-DWITH_Xmms=OFF",
	"-DWITH_ksplashqml=OFF",
	"-DWITH_ksplashqml=NO",
	"-DWITH_Googlegadgets=OFF",
	"-DAutomoc4_DIR=/usr/lib/automoc4",
    "-DWITH_NetworkManager=OFF", extraconf, sourcedir=build_dir)

def build():
    export("HOME", build_dir)
    cd("build")
    make("-j1")

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
