metadata = """
summary @ The GNU Scientific Library (GSL) is a modern numerical library for C and C++ programmers
homepage @ http://www.gnu.org/software/gsl/gsl.html
license @ GPL
src_url @ http://ftp.gnu.org/gnu/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
build @ dev-libs/glibc app-shell/bash     
"""

"""
def prepare():
    patch("gcc.patch", level=1)
"""

def configure():
    conf()

def build():
    make()
    make("check")
    
def install():
    raw_install("DESTDIR=%s" % install_dir)
