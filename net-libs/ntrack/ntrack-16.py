metadata = """
summary @ A network connectivity tracking library 
homepage @ http://launchpad.net/ntrack/ 
license @ LGPL 
src_url @ http://launchpad.net/$name/main/0$version/+download/$name-0$version.tar.gz
arch @ ~x86_64
options @ qt4
"""

depends = """
runtime @ dev-libs/libnl sys-libs/glib
build @ dev-lang/python net-misc/wget[ssl,gnutls]
"""

opt_runtime = """
qt4 @ x11-libs/qt
"""

srcdir = name+"-0"+version

def configure():
	conf(
	"--with-glib2",
	"--without-gobject",
	"--without-pygobject",
	config_with("qt4"))

def install():
    installd()
