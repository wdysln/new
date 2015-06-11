metadata = """
summary @ Gtk2 theme switcher
homepage @ http://muhri.net/nav.php3?node=gts
license @ GPL2
src_url @ http://ftp.de.debian.org/debian/pool/main/g/gtk-theme-switch/gtk-theme-switch_$version.orig.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/gtk+:2 
"""

def configure():
    pass

def build():
    make()

def install():
    insexe("gtk-theme-switch2", "/usr/bin/gtk-theme-switch2")
