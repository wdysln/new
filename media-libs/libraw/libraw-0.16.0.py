metadata = """
summary @ A library for reading RAW files obtained from digital photo cameras (CRW/CR2, NEF, RAF, DNG, and others)
homepage @ http://www.libraw.org/
license @ CDDL, custom, LGPL
src_url @ http://www.libraw.org/data/LibRaw-0.16.0.tar.gz
arch @ ~x86_64
options @ css
"""

depends = """
runtime @ media-libs/jasper media-libs/lcms
"""

opt_build = """
css @ media-libs/libdvdcss
"""
srcdir = "LibRaw-0.16.0"
def configure():
    conf("--disable-examples")


def install():
    raw_install("DESTDIR=%s" % install_dir)

