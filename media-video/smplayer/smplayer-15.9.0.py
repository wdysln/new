metadata = """
summary @ A complete QT front-end for MPlayer
homepage @ http://smplayer.sourceforge.net/
license @ GPL 
src_url @ http://downloads.sourceforge.net/sourceforge/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
common @ media-video/mplayer x11-libs/qt
"""

def configure():
    pass

def build():
    make("PREFIX=/usr")
    pass

def install():
    raw_install("PREFIX=%s/usr" % install_dir)

