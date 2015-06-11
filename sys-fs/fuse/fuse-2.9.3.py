metadata = """
summary @ A library that makes it possible to implement a filesystem in a userspace program.
homepage @ http://fuse.sourceforge.net/
license @ GPL2
src_url @ http://downloads.sourceforge.net/fuse/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
"""

def configure():
    conf("--enable-lib",
            "--enable-util",
            "--bindir=/bin")

def install():
    raw_install("DESTDIR=%s" % install_dir)

    rmdir("/dev")
    rmdir("/etc")
    makedirs("/usr/bin")
    
    makesym("/bin/fusermount","/usr/bin/fusermount")
    makesym("/bin/ulockmgr_server","/usr/bin/ulockmgr_server")


    
