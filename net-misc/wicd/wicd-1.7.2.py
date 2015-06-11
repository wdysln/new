metadata = """
summary @ Wired and wireless network manager for Linux
homepage @ http://wicd.sourceforge.net/
license @ GPL2
src_url @ http://launchpad.net/wicd/1.7/$version/+download/$fullname.tar.gz
arch @ ~x86_64
options @ gtk X libnotify ncurses nls pm-utils
"""

depends = """
runtime @ dev-python/dbus-python net-misc/dhcpcd net-wireless/wpa_supplicant net-wireless/wireless_tools sys-apps/ethtool
build @ dev-python/Babel
"""

#if not gtk, needs pygobject
#TODO: ioctl support

opt_runtime = """
X @ x11-misc/shared-mime-info
    gtk @ dev-python/pygtk
ncurses @ dev-python/urwid dev-python/pygobject
pm-utils @ sys-power/pm-utils
libnotify @ dev-python/notify-python
"""

def configure():
    rmfile("po/ast.po")
    myconf = ""

    if not opt("libnotify"):
        myconf += " --no-use-notifications "
    if not opt("ncurses"):
        myconf += " --no-install-ncurses "
    if not opt("pm-utils"):
        myconf += " --no-install-pmutils "
    if not opt("gtk"):
        myconf += " --no-install-gtk "

    system("find . -type f -exec sed -i 's@#!/usr.*python@#!/usr/bin/python2@' {} \;")
    
    export("PYTHON", "python2")

    system("python setup.py configure --no-install-docs \
            --no-install-init \
            --resume=/usr/share/wicd/scripts/ \
            --suspend=/usr/share/wicd/scripts/ \
            --python=/usr/bin/python2 \
            --verbose %s" % myconf)
    pass

def build():
    system("python setup.py build")
    pass

def install():
    system("python setup.py install --optimize=1 --root=%s" % install_dir)
    insexe("%s/wicd-daemon" % filesdir, "/etc/rc.d/wicd")
    insinto("%s/build/lib/wicd/*.py" % build_dir, "/usr/lib/wicd/")

def post_install():
    notify("You may need to restart the dbus service after upgrading wicd.")
    notify("Wicd-1.6 and newer requires your user to be in the 'users' group. If you are not in that group, then modify /etc/dbus-1/system.d/wicd.conf")
