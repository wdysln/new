metadata = """
summary @ A tool to copy files into or out of a cpio or tar archive
homepage @ http://www.gnu.org/software/cpio
license @ GPL
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
common @ sys-libs/glibc
"""

def prepare():
    patch(level=1)
    system("sed -i '/gets is a security hole/d' gnu/stdio.in.h")
    
def configure():
    conf("--enable-nls \
          --bindir=/bin \
          --with-rmt=/usr/sbin/rmt \
          --disable-rpath")
    
def build():
    make()
    make("check")

def install():
    raw_install("DESTDIR=%s" % install_dir)
