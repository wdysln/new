metadata = """
summary @ Enter is a lightweight graphical login manager for X.
homepage @ http://enter.sf.net
license @ GPL
src_url @ http://downloads.sourceforge.net/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ x11-libs/libXau x11-libs/libXext x11-libs/libXft x11-libs/libX11 media-libs/imlib2
build @ media-libs/freetype x11-proto/xproto
"""

#maybeError: LDFLAGS? http://gpo.zugaina.org/AJAX/Ebuild/2220946/View

#ERROR XFT, wait for new version
