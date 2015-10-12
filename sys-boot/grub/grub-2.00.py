metadata = """
summary @ A GNU multiboot boot loader
homepage @ http://www.gnu.org/software/grub/
license @ GPL
src_url @ http://alpha.gnu.org/gnu/grub/grub-2.02~beta2.tar.xz
arch @ ~x86_64
slot @ 2
"""

# TODO: 
# * options: debug mount truetype libzfs static
# * perhaps, efi support?

depends = """
runtime @ sys-libs/ncurses sys-apps/sed sys-apps/diffutils app-arch/xz sys-libs/ncurses
build @ dev-lang/python:2.7 sys-devel/flex sys-devel/bison sys-apps/texinfo
"""

srcdir = "grub-2.02~beta2"
def configure():
    conf("--program-prefix=",
            "--with-grubdir=grub2",
            "--disable-grub-emu-usb",
            "--disable-efiemu",
            "--disable-werror")

def install():
    raw_install("DESTDIR=%s" % install_dir)
