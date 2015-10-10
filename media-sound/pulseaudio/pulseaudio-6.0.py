metadata = """
summary @ A featureful, general-purpose sound server
homepage @ http://pulseaudio.org/
license @ GPL + LGPL
src_url @ http://0pointer.de/lennart/projects/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc  sys-libs/libcap sys-apps/attr media-libs/alsa-lib
	  x11-libs/libSM media-libs/libsndfile sys-devel/libtool media-libs/libsamplerate
	  sys-apps/dbus x11-misc/xcb-util dev-util/intltool dev-libs/openssl dev-libs/json-c 
"""
#net-libs/libasyncns
def configure():
	conf("--prefix=/usr        \
            --sysconfdir=/etc    \
            --localstatedir=/var \
            --disable-bluez4     \
            --disable-rpath")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    
"""
def post_install():
	system("sed -e '/resample-method/iresample-method=speex-float-0' -i \"/etc/pulse/daemon.conf\"")
	system("sed -e 's|/usr/bin/pactl load-module module-x11-cork-request|#&|' -i \"/usr/bin/start-$pkgbase-x11\"")
	system("sed -e $'/module-console-kit/{i.nofail\n;a.fail\n;}' -i \"/etc/pulse/default.pa\"")

"""