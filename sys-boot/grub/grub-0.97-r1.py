metadata = """
summary @ A GNU multiboot boot loader
homepage @ http://www.gnu.org/software/grub/
license @ GPL
src_url @ ftp://alpha.gnu.org/gnu/$name/$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/ncurses sys-apps/sed sys-apps/diffutils
"""

def prepare():
    patch(level=1)

def configure():
    export("CFLAGS", "-fno-strict-aliasing")
    raw_configure("--prefix=/usr",
            "--bindir=/bin",
            "--sbindir=/sbin",
            "--mandir=/usr/share/man",
            "--infodir=/usr/share/info")

def build():
    unset_env_variable("CFLAGS")
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)

    insfile("%s/menu.lst" % filesdir, "/boot/grub/menu.lst")
    insexe("%s/install-grub" % filesdir, "/sbin/install-grub")
