metadata = """
summary @ A lightweight display manager
homepage @ https://launchpad.net/lightdm
license @ GPL3 + LGPL3
src_url @ http://people.ubuntu.com/~robert-ancell/lightdm/releases/$fullname.tar.gz
arch @ ~x86_64
options @ branding gtk3 introspection
"""
#TODO: Qt option

depends = """
runtime @ sys-libs/glib sys-libs/pam x11-libs/libXklavier x11-libs/libX11
dev-libs/libxml2 sys-apps/accountsservice
build @ dev-lang/vala dev-util/intltool dev-util/pkg-config sys-devel/gettext
"""

opt_runtime = """
gtk3 @ x11-libs/gtk+:3 x11-themes/gnome-icon-theme
"""

opt_build = """
introspection @ dev-libs/gobject-introspection
"""

def prepare():
    if opt("branding"):
        if not opt("gtk3"):
            import lpms
            lpms.terminate("branding option needs gtk3 option")
    sed("""-i -e "/minimum-uid/s:500:1000:" data/users.conf""")
    sed("""-i -e "s|/usr/sbin/nologin|/sbin/nologin|g" data/users.conf""")

def configure():
    if opt("gtk3"):
        greeter = "lightdm-gtk-greeter"
    else:
        greeter = ""

    conf(
    "--disable-static",
    config_enable("introspection"),
    config_enable("gtk3", "gtk-greeter"),
    "--with-greeter-session=%s" % greeter,
    "--with-greeter-user=root")
    sed("""-i 's/lightdm-session//' tests/src/Makefile""")

def build():
    export("HOME", build_dir)
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insexe("%s/lightdm" % filesdir, "/etc/rc.d/lightdm")
    insfile("%s/lightdm.service" % filesdir, "/lib/systemd/system/")
    insfile("%s/lightdm-gtk-greeter.conf" % filesdir, "/etc/lightdm/")
    insfile("%s/lightdm.pam" % filesdir, "/etc/pam.d/lightdm")
    if opt("branding"):
        insfile("%s/hdr.png" % filesdir, "/usr/share/lightdm/backgrounds/hadron.png")
        sed("-i -e \"/background/s:=.*:=/usr/share/lightdm/backgrounds/hadron.png:\" %s/etc/lightdm/lightdm-gtk-greeter.conf" % install_dir)
