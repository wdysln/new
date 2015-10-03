metadata = """
summary @ Hardware (PCI, USB, OUI, IAB) IDs databases
homepage @ https://github.com/gentoo/hwids
license @ GPL-2 BSD
src_url @ https://github.com/gentoo/hwids/archive/hwids-20150717.tar.gz
arch @ ~x86_64
"""

standard_procedure = False
srcdir = "hwids-hwids-%s" % version

def install():
    for ids in ('pci.ids', 'usb.ids'):
        insfile("%s/%s" % (build_dir, ids), \
                "/usr/share/hwdata/%s" % ids)
