metadata = """
summary @ Implementation for atomic memory update operations
homepage @ http://www.hpl.hp.com/research/linux/atomic_ops/
license @ MIT boehm-gc GPL-2+
src_url @ https://github.com/ivmai/$name/archive/$name-7_4_2.tar.gz
arch @ ~x86_64
"""

srcdir = "%s-libatomic_ops-7_4_2" % name

def configure():
    system("./autogen.sh")
    system("./configure --prefix=/usr --disable-static --enable-shared")

def build():
    make()
    make("check")

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("AUTHORS", "NEWS", "README")
