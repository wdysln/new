metadata = """
summary @ Application development toolkit for controlling system-wide privileges
homepage @ http://www.freedesktop.org/wiki/Software/PolicyKit
license @ LGPL
src_url @ http://www.freedesktop.org/software/polkit/releases/$fullname.tar.gz
arch @ ~x86_64
options @ introspection
"""

depends = """
runtime @ sys-libs/pam dev-libs/expat sys-libs/glib dev-lang/spidermonkey
build @ dev-util/intltool
"""

opt_runtime = """
introspection @ dev-libs/gobject-introspection
"""

def configure():
    conf("--with-pam-module-dir=/lib/security/",
            "--libexecdir=/usr/lib/polkit-1",
            "--disable-man-pages",
            "--disable-gtk-doc",
            "--enable-libsystemd-login=no",
            "--disable-static",
            "--enable-examples",
            "--with-authfw=shadow",
            config_enable("introspection"))

def build():
    export("HOME", build_dir)
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insfile("%s/polkit.pam" % filesdir, "/etc/pam.d/polkit-1")
    
    makedirs("/var/lib/polkit-1")
    
def post_install():    
    #system("groupadd -fg 27 polkitd")
    #system("useradd -c 'PolicyKit Daemon Owner' -d /etc/polkit-1 -u 27 -g polkitd -s /bin/false polkitd")
    system("getent group polkitd >/dev/null || groupadd -g 102 polkitd")
    system("getent passwd polkitd >/dev/null || useradd -c 'Policy Kit Daemon' -u 102 -g polkitd -d '/' -s /bin/false polkitd")
    system("passwd -l polkitd &>/dev/null")
    system("chown 102 /var/lib/polkit-1")
    system("chown 102 /etc/polkit-1/rules.d")
    system("chown 102 /usr/share/polkit-1/rules.d")