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
headers @ >=sys-kernel/linux-api-headers-3.17.2
"""

def configure():
    copy("%s/config" % filesdir, ".config")
    pass

def build():
    kernopt = ""
    notify("")
    notify("****************************CAN I HAZ QUESTION?****************************")
    notify("")
    kernopt += "%s" % raw_input('Do you want to install with default config or editing via menuconfig [d/m]:')
    if kernopt == "" or kernopt == "d" or kernopt == "D":
        notify("Alright, going default...")
        m = "def"
    elif kernopt == 'm' or kernopt == 'M':
        notify("Going for menuconfig...")
        m = "men"
    else:
        notify("Not a valid option, going default...")
        m = "def"

    if m == "def":
        make()
    if m == "men":
        make("menuconfig")
        make()


def install():
    notify("Installing modules...")
    make("INSTALL_MOD_PATH=%s modules_install" % install_dir)

    notify("installing kernel as /boot/%s-hadron" % version)
    insfile("arch/x86/boot/bzImage", "/boot/%s-hadron" % version)

    if opt("sources"):
        notify("installing sources to /usr/src/%s-hadron" % version)
        insinto("*", "/usr/src/%s-hadron" % version)
