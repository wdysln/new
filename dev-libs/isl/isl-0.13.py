metadata = """
summary @ A free library for arbitrary precision arithmetic
homepage @ http://gmplib.org
license @ LGPL-3
src_url @ http://isl.gforge.inria.fr/isl-0.13.tar.bz2
options @ cxx
arch @ ~x86_64
"""

def configure():
    conf()

def install():
    raw_install("DESTDIR=%s install" % install_dir)
