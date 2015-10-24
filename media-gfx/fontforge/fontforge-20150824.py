metadata = """
summary @ Outline and bitmap font editor
homepage @ http://fontforge.github.io/
license @ BSD
src_url @ https://github.com/fontforge/fontforge/releases/download/20150612/fontforge-20150612.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ dev-python/pygtk dev-python/pygobject
          dev-python/py2cairo dev-libs/libxml2 media-libs/fontconfig
          media-libs/freetype dev-db/sqlite
"""
srcdir = "fontforge-20150612"

def configure():
	system("rm -rf libltdl")
	system("rm m4/argz.m4")
	
	system("./bootstrap")
	conf("--prefix=/usr     \
          --enable-gtk2-use \
          --disable-static")
          
def install():
    raw_install("DESTDIR=%s" % install_dir)

