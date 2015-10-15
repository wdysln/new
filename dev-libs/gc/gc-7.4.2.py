metadata = """
summary @ A garbage collector for C and C++
homepage @ http://www.hboehm.info/gc/
license @ GPL
src_url @ http://www.hboehm.info/$name/$name_source/$fullname.tar.gz
arch @ ~x86_64
"""
depends = """
build @ dev-libs/libatomic_ops
"""
#srcdir = "%s-libatomic_ops-7_4_2" % name

def configure():
    autoreconf("-fi")
    conf("--enable-cplusplus --disable-static")

def build():
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
