metadata = """
summary @ portable threads library
homepage @ ftp://ftp.gnu.org/gnu/pth/
license @ LGPL
src_url @ ftp://ftp.gnu.org/gnu/pth/pth-2.0.7.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc dev-libs/libxml2 dev-libs/libgcrypt 
"""

def build():
    make("-j1")
    
def install():
    installd()