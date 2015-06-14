metadata = """
summary @ Linux Kernel
homepage @ http://www.kernel.org/
license @ GPL2
src_url @ http://www.kernel.org/pub/linux/kernel/v3.0/$fullname.tar.gz
arch @ ~x86_64
options @ sources headers
"""

standard_procedure = False

opt_runtime = """
headers @ >=sys-kernel/linux-3.17.2
"""

def configure():
    copy("%s/config" % filesdir, ".config")
    pass

def build():
	make()

def install():
    notify("Installing modules...")
    make("INSTALL_MOD_PATH=%s modules_install" % install_dir)

    notify("installing kernel as /boot/%s-hadron" % version)
    insfile("arch/x86/boot/bzImage", "/boot/kernel-%s" % version)
    insinto("*", "/usr/src/linux-headers-%s" % version)


