metadata = """
summary @ A program to extract Microsoft cabinet (.CAB) files
homepage @ http://www.cabextract.org.uk/
license @ GPL
src_url @ http://www.cabextract.org.uk/cabextract-$version.tar.gz
arch @ ~x86_64
"""

depends = """
common @ sys-libs/glibc
"""

    
def configure():
    conf()
    
def build():
    make()


def install():
    raw_install("DESTDIR=%s" % install_dir)
