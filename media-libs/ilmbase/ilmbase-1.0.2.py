metadata = """
summary @ Base libraries from ILM for OpenEXR
homepage @ http://www.openexr.com/
license @ custom
src_url @ http://savannah.nongnu.org/download/openexr/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-devel/gcc
"""

def prepare():
    patch(level=1)

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING")
