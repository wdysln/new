metadata = """
summary @ GNU rewrite of netcat, the network piping application
homepage @ http://netcat.sourceforge.net/
license @ GPL
src_url @ http://downloads.sourceforge.net/netcat/netcat-$version.tar.bz2
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    conf("--prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info")

def install():
    raw_install("DESTDIR=%s" % install_dir)

