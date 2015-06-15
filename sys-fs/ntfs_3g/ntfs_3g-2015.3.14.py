metadata = """
summary @ Userspace driver for NTFS read/write support
homepage @ http://www.tuxera.com/community/ntfs-3g-download
license @ GPL2 + LGPL2
src_url @ http://tuxera.com/opensource/$name_ntfsprogs-$version.tgz
arch @ ~x86_64
"""

depends = """
build @ sys-fs/fuse sys-libs/glibc
runtime @ sys-libs/glibc sys-fs/fuse
"""

srcdir = "ntfs-3g_ntfsprogs-%s" % version

def configure():
    conf("--disable-static \
          --with-fuse=external \
          --enable-extras \
          --enable-posix-acls \
          --enable-ldscript \
          --disable-ldconfig")              

def install():
    installd()

    move("%s/usr/bin/ntfs-3g.*" % install_dir, "/bin")
    makesym("/bin/ntfs-3g", "/sbin/mount.ntfs")

