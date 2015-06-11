metadata = """
summary @ Background browser and setter for X windows
homepage @ http://projects.l3ib.org/nitrogen/
license @ GPL
src_url @ http://projects.l3ib.org/nitrogen/files/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-cpp/gtkmm x11-themes/hicolor-icon-theme gnome-base/librsvg
"""

def post_install():
	system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
