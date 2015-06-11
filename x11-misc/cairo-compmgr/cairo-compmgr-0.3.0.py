metadata = """
summary @  Cairo based composite manager
homepage @ http://cairo-compmgr.tuxfamily.org/
license @ GPL
src_url @ http://download.tuxfamily.org/ccm/cairo-compmgr/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/cairo x11-libs/gtk+:2 dev-lang/vala x11-libs/libSM gnome-base/gconf
build @ sys-devel/gettext dev-util/intltool
"""

def configure():
#	system("sed -i 's!vala-1.0!vala-0.11!' vapi/cairo-compmgr.deps")
#	system("sed -i 's!vala-1.0!vala-0.11!' configure configure.ac")
#	system("sed -i 's!VALA_REQUIRED=0.7.10!VALA_REQUIRED=0.11.6!' configure configure.ac")
#	system("./autogen.sh --prefix=/usr")
#	pass
	conf()

def build():
	make()

def post_install():
	system('gconf-merge-schema "$pkgdir/usr/share/gconf/schemas/cairo-compmgr.schemas" "$pkgdir/etc/gconf/schemas/*.schemas"')

