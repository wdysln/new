metadata = """
summary @ Library for reading media metadata
homepage @ https://bitbucket.org/shuerhaaken/libtaginfo
license @ GPL2
src_url @ https://bitbucket.org/shuerhaaken/libtaginfo/downloads/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/zlib
build @ dev-util/gperf
"""

def configure():
    system("./autogen.sh")
    conf("--prefix=/usr")

def build():
    make()
    
def install():
    raw_install("DESTDIR=%s" % install_dir)
