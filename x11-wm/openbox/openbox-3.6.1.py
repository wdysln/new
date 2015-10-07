metadata = """
summary @ A window manager for the X11 windowing system
homepage @ http://openbox.org/
license @ GPL
src_url @ http://openbox.org/dist/openbox/$fullname.tar.gz
arch @ ~x86_64
options @ startup-notification nls static-libs session
"""

depends = """
commons @ dev-libs/libxml2 x11-libs/libXinerama x11-libs/libXrandr x11-libs/libXcursor
    media-libs/pango x11-libs/libXft x11-libs/libXt sys-libs/glib
build @ dev-util/pkg-config x11-proto/xextproto x11-proto/xf86vidmodeproto x11-proto/xineramaproto
"""

opt_runtime = """
startup-notification @ x11-libs/startup-notification
nls @ sys-devel/gettext
"""


def configure():
    conf("--with-x",
         config_enable("nls"),
         config_enable("static-libs", "static"),
	  "--enable-startup-notification")


def install():
    raw_install("DESTDIR=%s" % install_dir)
