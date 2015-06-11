metadata = """
summary @ Legacy polkit authentication agent for GNOME
homepage @ http://www.freedesktop.org/wiki/Software/polkit/
license @ LGPL
src_url @ https://download.gnome.org/sources/polkit-gnome/0.105/polkit-gnome-0.105.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ sys-auth/polkit dev-util/intltool x11-libs/gtk+:3
"""

def configure():
	conf()
	
def build():
    make()

def install():
	installd()
	insfile("%s/polkit-gnome-authentication-agent-1.desktop" % filesdir, "/etc/xdg/autostart/polkit-gnome-authentication-agent-1.desktop")
