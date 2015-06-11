metadata = """
summary @ A featureful, general-purpose sound server
homepage @ http://pulseaudio.org/
license @ GPL + LGPL
src_url @ http://0pointer.de/lennart/projects/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc net-libs/libasyncns sys-libs/libcap sys-apps/attr x11-libs/libXtst 
	x11-libs/libSM media-libs/libsndfile sys-devel/libtool media-libs/speex media-libs/libsamplerate
	sys-apps/dbus sys-fs/udev x11-misc/xcb-util dev-util/intltool dev-libs/openssl

"""

def configure():
	conf(
	"--prefix=/usr \
	    --sysconfdir=/etc \
	    --libexecdir=/usr/lib \
	    --localstatedir=/var \
	    --with-database=gdbm \
	    --disable-hal \
	    --disable-tcpwrap \
	    --disable-rpath \
	    --disable-default-build-tests")

def install():
	raw_install("DESTDIR=%s" % install_dir)
	
	insfile("%s/pulseaudio.xinit" % filesdir, "/etc/X11/xinit/xinitrc.d/pulseaudio.xinit")

def post_install():
	system("sed -e '/resample-method/iresample-method=speex-float-0' -i \"/etc/pulse/daemon.conf\"")
	system("sed -e 's|/usr/bin/pactl load-module module-x11-cork-request|#&|' -i \"/usr/bin/start-$pkgbase-x11\"")
	system("sed -e $'/module-console-kit/{i.nofail\n;a.fail\n;}' -i \"/etc/pulse/default.pa\"")

#hatali gdbm instead of tdb build problem.. also fuckin lots of options: http://projects.archlinux.org/svntogit/packages.git/tree/pulseaudio/trunk/PKGBUILD
