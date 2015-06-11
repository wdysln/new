metadata = """
summary @ GTK2 engine to make your desktop look like a 'murrina', an italian word meaning the art glass works done by Venicians glass blowers.
homepage @ http://cimitan.com/murrine/project/murrine
license @ LGPL3
src_url @ http://ftp.gnome.org/pub/GNOME/sources/murrine/0.98/murrine-$version.tar.xz
arch @ ~x86_64
options @ animation-rtl themes
"""

depends = """
runtime @ x11-libs/gtk+:2 x11-libs/cairo x11-libs/pixman
build @ dev-util/intltool sys-devel/gettext dev-util/pkg-config
"""

opt_postmerge = """
themes @ x11-themes/murrine-themes
"""

srcdir = "murrine-" + version

def configure():
	conf(
	"--prefix=/usr",
    "--enable-animation",
	config_enable("--enable-animationrtl", "animationrtl"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "ChangeLog", "NEWS", "TODO")
