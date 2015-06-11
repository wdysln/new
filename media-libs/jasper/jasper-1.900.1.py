metadata = """
summary @ A software-based implementation of the codec specified in the emerging JPEG-2000 Part-1 standard
homepage @ http://www.ece.uvic.ca/~mdadams/jasper/
license @ custom
src_url @ http://www.ece.uvic.ca/~mdadams/$name/software/$fullname.zip
arch @ ~x86_64
"""

depends = """
runtime @ media-libs/jpeg x11-libs/libXi x11-libs/libXmu media-libs/mesa media-libs/freeglut
build @ app-arch/unzip
"""

def prepare():
    patch(level=1)
    # weird :S
    setmod("+x configure")

def configure():
    conf("--enable-shared")

def install():
    raw_install("DESTDIR=%s" % install_dir)


