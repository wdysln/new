metadata = """
summary @ A IPC library used by some GnuPG related software
homepage @ http://www.gnupg.org/related_software/libassuan
license @ LGPL
src_url @ ftp://ftp.gnupg.org/gcrypt/$name/$fullname.tar.bz2
arch @ ~x86_64
"""

depends = """
build @ dev-libs/pth dev-libs/libgpg-error
"""

def configure():
    append_cflags("-fPIC -DPIC")
    append_ldflags("-fPIC")
    conf()
    
    
def build():
    make()
    make("check")
    
    
def install():
    installd()
    insdoc("COPYING")

