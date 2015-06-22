metadata = """
summary @ PCI bus configuration space access library and tools
homepage @ http://mj.ucw.cz/pciutils.html
license @ GPL-2
src_url @ ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci//$fullname.tar.gz
arch @ ~x86_64
"""

depends = """
runtime @ sys-libs/glibc
build @ net-misc/wget
"""

def build():
    patch("pciutils-remove-update-pciids.patch", level=1)
    copy("%s/pci.ids" % filesdir, "pci.ids")
    make('OPT="%s -fPIC -DPIC" SHARED="yes" PREFIX=/usr IDSDIR=/usr/share/misc \
            MANDIR=/usr/share/man all' % get_env('CFLAGS'))


def install():
    raw_install('DESTDIR="%s" \
            PREFIX=/usr \
            SHARED="yes" \
            IDSDIR="/usr/share/misc" \
            MANDIR="/usr/share/man" \
            install-lib' % install_dir)

