metadata = """
summary @ Btrfs filesystem utilities
homepage @ http://btrfs.wiki.kernel.org
license @ GPL2
src_url @ http://source.pisilinux.org/1.0/btrfs-progs-v3.19.1.tar.xz
arch @ ~x86_64
"""

depends = """
build @ sys-apps/util-linux app-shells/bash app-arch/lzo dev-vcs/git sys-libs/zlib
"""

srcdir = "%s" % name

def configure():
    system("./autogen.sh")
    conf()

def install():
    installd()



