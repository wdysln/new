metadata = """
summary @ Subtitle rendering library
homepage @ http://code.google.com/p/libass/
license @ GPL2
src_url @ https://github.com/libass/libass/releases/download/$version/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ media-libs/fontconfig app-i18n/enca dev-libs/fribidi media-libs/harfbuzz
"""

def configure():
    autoreconf("-vfi")
    conf("--enable-fontconfig \
	--disable-static \
	--enable-enca \
	--enable-png")


def install():
    raw_install("DESTDIR=%s" % install_dir)

