metadata = """
summary @ Open source search engine library.
homepage @ http://www.xapian.org/
license @ GPL
src_url @ http://oligarchy.co.uk/xapian/1.2.18/xapian-core-1.2.18.tar.xz
arch @ ~x86_64
"""



def configure():
    export("HOME", build_dir)
    conf("--disable-static")
    
def build():
    export("HOME", build_dir)
    make()

def install():
    export("HOME", build_dir)
    raw_install("DESTDIR=%s" % install_dir)