metadata = """
summary @  register interpreters for various binary formats
homepage @ http://packages.debian.org/en/sid/binfmt-support
license @ GPL
src_url @ http://ftp.de.debian.org/debian/pool/main/b/binfmt-support/binfmt-support_$version.orig.tar.gz
arch @ ~x86_64
options @ debug threads
"""

srcdir = "binfmt-support-%s" % version

depends = """
runtime @ sys-libs/glibc dev-libs/libpipeline 
"""
def configure():
    conf()
    
def build():
    make()


def install():  
    installd()
    insinto("%s/binfmt-support.service" % filesdir ,"/usr/lib/systemd/system")
    makedirs("/var/lib/binfmts")

    

