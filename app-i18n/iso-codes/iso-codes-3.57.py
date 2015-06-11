metadata = """
summary @ Lists of the country, language, and currency names
homepage @ http://pkg-isocodes.alioth.debian.org/
license @ LGPL
src_url @ http://pkg-isocodes.alioth.debian.org/downloads/$fullname.tar.xz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def install():
    raw_install("pkgconfigdir=/usr/lib/pkgconfig DESTDIR=%s" % install_dir)
