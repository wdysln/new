metadata = """
summary @ KDE Base Workspace 
homepage @ http://www.kde.org
license @ GPL LGPL FDL 
src_url @ http://ftp.osuosl.org/pub/blfs/conglomeration/kde-workspace/kde-workspace-4.11.14.tar.xz
arch @ ~x86_64
options @ xinerama qalculate semantic
"""

# TODO: media-libs/phonon[vlc] removed due to lpms bug. Don't need a revision for now, will add when adding back..

depends = """
build @ dev-util/cmake dev-util/automoc4 x11-libs/libX11 x11-libs/libXext dev-libs/qjson dev-libs/libical 
dev-libs/cyrus-sasl net-dns/openldap x11-libs/libXklavier x11-libs/libXrender x11-libs/libXtst kde-base/kactivities
runtime @ x11-proto/kbproto x11-proto/renderproto x11-misc/xcb-util-renderutil kde-base/kdepim-runtime
media-libs/libraw media-libs/qimageblitz media-libs/mesa media-libs/glu kde-base/kdepimlibs
"""



get("main/cmake_utils", "main/extract_utils")

def extract():
    system("tar xf %s/kde-workspace-%s.tar.xz -C %s" % (src_cache, version, dirname(build_dir)))

def configure():
    makedirs("build")
    cd("build")
    cmake_conf(
    cmake_config_with("qalculate"),
    "-DCMAKE_SKIP_RPATH=ON",
	"-DAutomoc4_DIR=/usr/lib/automoc4",
    "-DWITH_NepomukCore=OFF",
    "-DWITH_NetworkManager=OFF", sourcedir=build_dir)

def build():
    export("HOME", build_dir)
    cd("build")
    make()

def install():
    cd("build")
    raw_install("DESTDIR=%s" % install_dir)
    makedirs("/etc/rc.d")
    makedirs("/etc/pam.d")
  #  insexe("%s/kdm" % filesdir, "/etc/rc.d/kdm")
  #  insfile("%s/kde.pam" % filesdir, "/etc/pam.d/kde")
   # insfile("%s/kde-np.pam" % filesdir, "/etc/pam.d/kde-np")
   # insfile("%s/kscreensaver.pam" % filesdir, "/etc/pam.d/kscreensaver")
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
